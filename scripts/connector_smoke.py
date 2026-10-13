"""Live smoke test for one food-connectors adapter. Prints JSON result."""
import sys, json, time, datetime
sys.path.insert(0, sys.argv[2])
from food_connectors.adapters import ADAPTERS
from dataclasses import asdict, is_dataclass
aid = sys.argv[1]; a = ADAPTERS[aid]
r = {"id": aid, "store": getattr(a,"store",""), "status_declared": getattr(a,"status",""), "ts": datetime.datetime.utcnow().isoformat(timespec="seconds")+"Z"}
t = time.time()
try:
    items = []
    for q in ["gulasch", "lasagne", "suppe"]:
        items = a.search(q, limit=3)[:3]
        if items: break
    if not items and getattr(a,"status","")!="catalog-only":
        items = a.fetch(limit=3)[:3]
    r["latency_s"] = round(time.time()-t, 2); r["count"] = len(items)
    errs = []
    for p in items:
        d = asdict(p) if is_dataclass(p) else dict(p)
        if not d.get("name"): errs.append("missing name")
        if not (d.get("source") or d.get("store")): errs.append("missing source/store")
        pr = d.get("price_eur")
        if pr is not None and not (0 < float(pr) < 500): errs.append(f"bad price {pr}")
    r["schema_errors"] = errs
    if items:
        d = asdict(items[0]) if is_dataclass(items[0]) else dict(items[0])
        r["sample"] = {k: d.get(k) for k in ["name","brand","store","price_eur","source_url","image_url","fetched_at"]}
    r["result"] = "catalog" if getattr(a,"status","")=="catalog-only" else ("pass" if items and not errs else "fail")
except Exception as e:
    r["latency_s"] = round(time.time()-t, 2); r["count"]=0; r["result"]="fail"; r["error"]=f"{type(e).__name__}: {e}"[:300]
print(json.dumps(r, default=str))
