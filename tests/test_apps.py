import json, os, re, sys, time, pytest, urllib.request
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import APPS
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "results", "apps"); os.makedirs(OUT, exist_ok=True)
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")[:40] or "tab"
def discover(url):
    try:
        html = urllib.request.urlopen(url, timeout=20).read().decode()
        out=[]
        for js in re.findall(r'assets/[^"]+\.js', html):
            src = urllib.request.urlopen(url+js, timeout=30).read().decode("utf8","ignore")
            out += [{"id":i,"t":l,"mode":"hash"} for i,l in re.findall(r'\["([a-z][a-z0-9-]+)","([^"]{2,40})",[A-Za-z$_]{1,4}\]', src)]
            out += [{"id":i,"t":l,"mode":"click"} for i,l in re.findall(r'\{id:"([a-z][a-z0-9-]+)",t:"([^"]{2,40})"', src)]
        seen=set(); return [o for o in out if not (o["id"] in seen or seen.add(o["id"]))]
    except Exception: return []
def live(url):
    try: return urllib.request.urlopen(url, timeout=20).status == 200
    except Exception: return False
@pytest.mark.parametrize("app", APPS, ids=[a["id"] for a in APPS])
def test_app(app):
    res = {"id": app["id"], "name": app["name"], "url": app["url"], "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "live": live(app["url"]), "tabs": []}
    if not res["live"]:
        json.dump(res, open(f"{OUT}/{app['id']}.json","w"), indent=1); pytest.skip("not live")
    sd = os.path.join(ROOT, "screenshots", app["id"]); os.makedirs(sd, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for vw, vh in [(1920,1080),(390,844)]:
            pg = b.new_page(viewport={"width":vw,"height":vh})
            errs = []
            pg.on("console", lambda m: errs.append(m.text[:200]) if m.type=="error" else None)
            pg.on("pageerror", lambda e: errs.append(("pageerror: "+str(e))[:200]))
            pg.goto(app["url"], wait_until="networkidle", timeout=60000)
            tabs = [{"id":None,"t":"home"}] + discover(app["url"])
            for t in tabs[:30]:
                errs.clear()
                try:
                    if t["id"] and t["mode"]=="hash":
                        pg.goto(app["url"]+"#tab="+t["id"], wait_until="networkidle", timeout=45000)
                    elif t["id"]:
                        el = pg.get_by_text(t["t"], exact=True).first
                        if not el.is_visible():
                            for b2 in pg.locator('button[aria-label*="enu"], button:has(svg.lucide-menu), [data-sidebar=trigger]').all()[:1]: b2.click(timeout=3000)
                        pg.get_by_text(t["t"], exact=True).first.click(timeout=5000)
                    pg.wait_for_timeout(1500)
                    broken = pg.evaluate("[...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.src).map(i=>i.src).slice(0,10)")
                    nimg = pg.evaluate("document.images.length")
                    fn = f"screenshots/{app['id']}/{slug(t["id"] or "home")}_{vw}.png"
                    pg.screenshot(path=os.path.join(ROOT, fn))
                    res["tabs"].append({"tab":t["t"],"viewport":vw,"console_errors":list(errs),"broken_images":broken,"images":nimg,"screenshot":fn,"ok":True})
                except Exception as e:
                    res["tabs"].append({"tab":t["t"],"viewport":vw,"ok":False,"error":str(e)[:200]})
            pg.close()
        b.close()
    json.dump(res, open(f"{OUT}/{app['id']}.json","w"), indent=1)
    assert all(t["ok"] for t in res["tabs"])
