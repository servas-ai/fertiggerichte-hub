import json, os, sys, collections, time
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import DATA_DIR
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(n):
    p=os.path.join(DATA_DIR,n+".json"); return json.load(open(p)) if os.path.exists(p) else []
def fill(rows):
    keys = sorted({k for r in rows for k in r})
    return {k: round(100*sum(1 for r in rows if r.get(k) not in (None,"",[]))/max(len(rows),1),1) for k in keys}
def test_dataset():
    P, N, PR, L = load("products"), load("nutrition"), load("prices"), load("logos")
    if isinstance(L, dict): L = list(L.values())
    nut = {n["product_id"] for n in N if n.get("kcal_100g") not in (None,"")}
    price = {p["product_id"] for p in PR if p.get("price_eur") not in (None,"")}
    n=len(P) or 1
    pct=lambda c: round(100*c/n,1)
    stats = {"ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "products": len(P),
      "by_store": collections.Counter(p.get("chain") or "?" for p in P).most_common(),
      "by_storage": collections.Counter(p.get("storage") or "?" for p in P).most_common(),
      "coverage": {"nutrition": pct(sum(p["product_id"] in nut for p in P)), "price": pct(sum(p["product_id"] in price for p in P)),
                   "photo": pct(sum(bool(p.get("image_url")) for p in P)), "producer": pct(sum(bool(p.get("producer")) for p in P)),
                   "brand": pct(sum(bool(p.get("brand")) for p in P)), "logos_total": len(L)},
      "fill_rate_products": fill(P), "counts": {f[:-5]: len(load(f[:-5])) for f in os.listdir(DATA_DIR) if f.endswith(".json") and not f.startswith("_")}}
    os.makedirs(os.path.join(ROOT,"results"),exist_ok=True)
    json.dump(stats, open(os.path.join(ROOT,"results","dataset.json"),"w"), indent=1, ensure_ascii=False)
    assert len(P) > 500
    assert len({p["product_id"] for p in P}) == len(P), "duplicate product_id"
    assert stats["fill_rate_products"].get("name",0) == 100
