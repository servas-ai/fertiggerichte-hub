#!/usr/bin/env python3
"""Builds report.json + README.md from results/ and git logs of all repos."""
import json, os, glob, subprocess, time
from config import APPS, REPOS
R = os.path.dirname(os.path.abspath(__file__))
def j(p):
    try: return json.load(open(p))
    except Exception: return None
conns = sorted([j(f) for f in glob.glob(f"{R}/results/connectors/*.json")], key=lambda c:(c["result"]!="pass", c["id"]))
apps = [j(f"{R}/results/apps/{a['id']}.json") or {"id":a["id"],"name":a["name"],"url":a["url"],"live":None,"tabs":[]} for a in APPS]
ds = j(f"{R}/results/dataset.json") or {}
def gitlog(repo):
    try:
        out = subprocess.run(["gh","api",f"repos/{repo}/commits?per_page=8","--jq",'.[]|[.sha[0:7],.commit.author.date[0:16],(.commit.message|split("\n")[0])]|@tsv'],capture_output=True,text=True,timeout=30).stdout
        return [l.split("\t") for l in out.strip().splitlines()]
    except Exception: return []
logs = {r: gitlog(r) for r in REPOS}
now = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime())
report = {"generated": now, "connectors": conns, "apps": apps, "dataset": ds, "changelog": logs}
json.dump(report, open(f"{R}/report.json","w"), indent=1, ensure_ascii=False, default=str)
np = sum(c["result"]=="pass" for c in conns); nf = sum(c["result"]=="fail" for c in conns)
icon = {"pass":"✅","fail":"❌","catalog":"📇"}
L = [f"# 🥘 Fertiggerichte-Hub", "", f"Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** {now} via `./run_all.sh` (stündlich).", "",
 f"**Connectors:** {np} ✅ / {nf} ❌ / {len(conns)-np-nf} 📇 catalog-only · **Apps:** {sum(bool(a.get('live')) for a in apps)}/{len(apps)} live · **Produkte im Datensatz:** {ds.get('products','?')}", "",
 "## Apps", "", "| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |", "|---|---|---|---|---|---|"]
for a in apps:
    t=a.get("tabs",[]); L.append(f"| {a['name']} | {a['url']} | {'✅' if a.get('live') else '❌'} | {len({x['tab'] for x in t})} | {sum(len(x.get('console_errors',[])) for x in t)} | {sum(len(x.get('broken_images',[])) for x in t)} |")
L += ["", "## Repositories", "", "| Repo | Zweck |", "|---|---|",
 "| [servas-ai/fertiggerichte-vergleich](https://github.com/servas-ai/fertiggerichte-vergleich) | Web-App (Vergleich, Netz 3D, Gesundheit, Hersteller …) |",
 "| [servas-ai/food-connectors](https://github.com/servas-ai/food-connectors) | Connectors + CLI + MCP-Server |",
 "| [servas-ai/fertiggerichte-daten](https://github.com/servas-ai/fertiggerichte-daten) | Offener Datensatz CSV/JSON |",
 "| [servas-ai/einkaufsanalyse](https://github.com/servas-ai/einkaufsanalyse) | Einkaufsanalyse-Dashboard (Kassenbons) |", "",
 "## Architektur", "", "```mermaid", "flowchart LR",
 "  subgraph Quellen", "    BILLA & PENNY[REWE API] --> FC", "    GURKERL[Gurkerl] --> FC", "    LIDL[Lidl] --> FC", "    HP[heisse-preise.io<br/>Spar/Hofer/dm/MPreis] --> FC", "    OFF[Open Food Facts] --> FC", "    MP[Meal-Prep: PrepMyMeal …] --> FC", "  end",
 "  FC[food-connectors<br/>CLI + MCP] --> DATA[(fertiggerichte-daten<br/>CSV/JSON)]", "  DATA --> APP[fertiggerichte-vergleich<br/>GitHub Pages]", "  BONS[Kassenbon-Fotos] --> EA[einkaufsanalyse]",
 "  HUB[fertiggerichte-hub<br/>E2E + README] -.testet.-> FC & DATA & APP & EA", "```", "",
 "## Connector-Status (Live-Smoke-Test)", "", "| | Connector | Store | Items | Latenz | Beispielprodukt (Beweis) | Zeitpunkt |", "|---|---|---|---|---|---|---|"]
for c in conns:
    s=c.get("sample") or {}
    ev = (f"[{s.get('name','')[:50]}]({s['source_url']})" if s.get("source_url") else s.get("name","")[:50]) + (f" · {s['price_eur']} €" if s.get("price_eur") else "")
    if c["result"]=="fail": ev = "`"+(c.get("error") or str(c.get("schema_errors") or "0 Treffer"))[:90].replace("|","/")+"`"
    L.append(f"| {icon.get(c['result'],'?')} | `{c['id']}` | {c.get('store','')} | {c.get('count',0)} | {c.get('latency_s','')} s | {ev} | {c.get('ts','')} |")
if os.path.exists(f"{R}/KNOWN_ISSUES.md"):
    L += ["", "### Bekannte Ausfälle (manuell gepflegt)", "", open(f"{R}/KNOWN_ISSUES.md").read().strip()]
cv = ds.get("coverage",{})
L += ["", "## Datensatz", "", f"**{ds.get('products','?')} Produkte** · Tabellen: " + ", ".join(f"{k} {v}" for k,v in sorted(ds.get("counts",{}).items())), "",
 "| Abdeckung | % |", "|---|---|"] + [f"| {k} | {v} |" for k,v in cv.items()]
L += ["", "<details><summary>Produkte nach Kette</summary>", "", "| Kette | Anzahl |", "|---|---|"] + [f"| {k} | {v} |" for k,v in ds.get("by_store",[])] + ["", "</details>", "",
 "<details><summary>Produkte nach Fertigstufe/Lagerung</summary>", "", "| Lagerung | Anzahl |", "|---|---|"] + [f"| {k} | {v} |" for k,v in ds.get("by_storage",[])] + ["", "</details>", ""]
L += ["## Screenshots", ""]
for a in apps:
    tabs=a.get("tabs",[])
    if not tabs: continue
    L += [f"### {a['name']}", "", "| Tab | Desktop 1920 | Mobil 390 |", "|---|---|---|"]
    for name in dict.fromkeys(x["tab"] for x in tabs):
        d=next((x for x in tabs if x["tab"]==name and x["viewport"]==1920 and x.get("screenshot")),None); m=next((x for x in tabs if x["tab"]==name and x["viewport"]==390 and x.get("screenshot")),None)
        L.append(f"| {name[:30]} | {'<img src=\"'+d['screenshot']+'\" width=\"420\">' if d else '–'} | {'<img src=\"'+m['screenshot']+'\" width=\"140\">' if m else '–'} |")
    L.append("")
L += ["## Changelog (letzte Commits)", ""]
for r, cs in logs.items():
    L += [f"**{r}**", ""] + [f"- `{c[0]}` {c[1].replace('T',' ')} — {c[2] if len(c)>2 else ''}" for c in cs] + [""]
L += ["## Ausführen", "", "```bash", "pip install pytest playwright && playwright install chromium", "./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)", "```", ""]
open(f"{R}/README.md","w").write("\n".join(L))
print(f"connectors {np} pass / {nf} fail; apps {[ (a['id'],a.get('live')) for a in apps]}; products {ds.get('products')}")
