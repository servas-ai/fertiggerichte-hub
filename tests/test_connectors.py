import json, subprocess, sys, pytest, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import CONNECTORS_DIR
sys.path.insert(0, CONNECTORS_DIR)
from food_connectors.adapters import ADAPTERS
OUT = os.path.join(os.path.dirname(__file__), "..", "results", "connectors")
os.makedirs(OUT, exist_ok=True)
@pytest.mark.parametrize("aid", sorted(ADAPTERS))
def test_connector(aid):
    here = os.path.dirname(os.path.abspath(__file__))
    r = None
    for attempt in range(2):  # retry once on empty output (OOM) or timeout (slow OCR e.g. nah-frisch ~230s)
        try:
            p = subprocess.run([sys.executable, os.path.join(here,"..","scripts","connector_smoke.py"), aid, CONNECTORS_DIR], capture_output=True, text=True, timeout=300)
            if p.stdout.strip():
                r = json.loads(p.stdout.strip().splitlines()[-1]); break
            r = {"id":aid,"result":"fail","error":f"smoke exited rc={p.returncode} without output: "+p.stderr[-300:]}
        except subprocess.TimeoutExpired:
            r = {"id":aid,"result":"fail","error":"timeout 300s","latency_s":300,"count":0}
            if attempt == 0:
                continue  # retry once; OCR connectors can exceed 180s under load
            break
    json.dump(r, open(os.path.join(OUT, f"{aid}.json"),"w"), indent=1, default=str)
    if r["result"] == "catalog": pytest.skip("catalog-only")
    assert r["result"] == "pass", r.get("error") or r.get("schema_errors")
