"""Regenerate the data-driven sections of COVERAGE.md from servas-ai/fertiggerichte-daten.
Hand-written sections (companies, datasets, online meal-prep, connector findings) are kept verbatim."""
import csv, collections, datetime, json, os, re, sys
HUB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATEN = os.environ.get("DATEN", os.path.join(os.path.dirname(HUB), "fertiggerichte-daten"))
COV = os.path.join(HUB, "COVERAGE.md")
rd = lambda n: list(csv.DictReader(open(f"{DATEN}/data/{n}.csv")))
P, PR, L = rd("products"), rd("prices"), rd("logos")
old = open(COV).read()
head, *secs = re.split(r"(?m)^## ", old)
S = {s.split("\n", 1)[0].strip(): "## " + s for s in secs}
branches = {}
for m in re.finditer(r"(?m)^\| ([^|]+?) \| \[.\] \| \d+ \| \[(.)\] \| (\d+) \| \[.\] \|$", S.get("Stores", "")):
    branches[m.group(1)] = (m.group(2), int(m.group(3)))
cnt = collections.Counter(p["chain"] for p in P); img = collections.Counter(p["chain"] for p in P if p["image_url"])
logo_names = {l["name"].lower() for l in L} | {l["slug"] for l in L} | {b.lower() for l in L for b in (l.get("brands") or "").split("|") if b}
LF = [l for l in L if (l.get("file") or "").strip()]  # rows that actually carry a logo file (file-less placeholder rows don't count)
logo_file_names = {l["name"].lower() for l in LF} | {l["slug"] for l in LF} | {b.lower() for l in LF for b in (l.get("brands") or "").split("|") if b}
CH = ["Spar", "Billa", "Billa Plus", "Hofer", "Lidl", "Penny", "dm", "denn's BioMarkt", "MPreis", "Unimarkt", "ADEG", "Nah&Frisch", "Fit to Go", "Gurkerl", "Eurospar", "Interspar"]
SLUG = {"denn's BioMarkt": "denns", "Nah&Frisch": "nah-frisch", "Billa Plus": "billa-plus", "Fit to Go": "fit2go", "Eurospar": "spar", "Interspar": "spar"}
x = lambda b: "[x]" if b else "[ ]"
st = ["## Stores", "", "| Chain | Products indexed? | # products | Branches (Linz+Umland OSM)? | # branches | Logo? |", "|---|---|---|---|---|---|"]
for c in CH:
    b = branches.get(c, (" ", 0)); lg = c.lower() in logo_names or SLUG.get(c, c.lower()) in logo_names
    st.append(f"| {c} | {x(cnt[c])} | {cnt[c]} | [{b[0] if b[1] or b[0]=='x' else ' '}] | {b[1]} | {x(lg)} |")
other = S.get("Stores", "").split("Other OSM chains in bbox:", 1)
st += ["", "Other OSM chains in bbox:" + (other[1].rstrip() if len(other) > 1 else ""), ""]
ph = ["## Ready meals with photos", "", "| Chain | Products | With image_url | % photos |", "|---|---|---|---|"]
for c, n in cnt.most_common():
    pc = img[c] / n * 100; ph.append(f"| {c} | {n} | {img[c]} ({'[x]' if pc >= 99.5 else '[~]' if pc else '[ ]'}) | {pc:.1f}% |")
tot_img = sum(img.values())
ph += ["", f"- [x] Total products: **{len(P)}**", f"- [x] Total with photos: **{tot_img}** ({tot_img/len(P)*100:.1f}%)",
       f"- {x(img['MPreis']==cnt['MPreis'] and cnt['MPreis'])} MPreis photos: live webshop connector `mpreis-shop` ({img['MPreis']}/{cnt['MPreis']})",
       f"- {x(img['Unimarkt']==cnt['Unimarkt'] and cnt['Unimarkt'])} Unimarkt photos: {img['Unimarkt']}/{cnt['Unimarkt']} — no source possible: shop.unimarkt.at shows only 'UNIONLINE hat seinen Service eingestellt' (verified 2026-10-13), chain left retail 2026; rows are historic-only", ""]
by = collections.defaultdict(collections.Counter)
for r in PR: by[r["chain"]][r["price_status"]] += 1
tp = ["## Tariffs & prices", "", "| Chain | Price rows | Status breakdown |", "|---|---|---|"]
for c, k in sorted(by.items(), key=lambda kv: -sum(kv[1].values())):
    n = sum(k.values()); live = k.get("live 2026", 0)
    tp.append(f"| {c} [{'x' if live == n else '~' if live else ' '}] | {n} | {' · '.join(f'{a}: {b}' for a, b in k.most_common())} |")
tp += ["- [x] MPreis: live 2026 prices from the webshop (stale 2023/24 dump rows replaced; only 52/149 still listed)",
       "- [ ] Fresh live prices for Hofer/Spar-2025 rows: need shop connectors or browser (hofer.at Akamai 403, interspar.at Cloudflare)",
       "- [x] dm: live 2026 prices via food-connectors `dm` (dm.at sitemap + products.dm.de product JSON); the 6 remaining 'Preis 2025' dm rows are not in the dm.at 2026 product sitemap (delisted) -> no live price possible, kept flagged",
       "- [-] Unimarkt: no live price possible — webshop closed 02/2024, chain exited retail 02-03/2026 (29 rows kept as flagged 2023/24 history)", ""]
lgsec = S.get("Logos", "")
missing = [c for c in ["MPreis", "Unimarkt", "denn's BioMarkt", "ADEG", "Nah&Frisch", "Fit to Go", "Billa Plus", "Gurkerl"] if not (c.lower() in logo_names or SLUG.get(c, c.lower()) in logo_names)]
lgsec = re.sub(r"- \[.\] Logo index rows: \*\*\d+\*\*(?: \(\d+ with a logo file\))?", f"- [x] Logo index rows: **{len(L)}** ({len(LF)} with a logo file)", lgsec)
lgsec = re.sub(r"- Handelskette logos present: .*", f"- Handelskette logos present: {sorted(l['name'] for l in L if l['category']=='Handelskette')}", lgsec)
lgsec = re.sub(r"- \[.\] Missing Handelskette logos: .*", (f"- [ ] Missing Handelskette logos: {', '.join(missing)}" if missing else "- [x] All tracked Handelskette logos present") + " (Eurospar/Interspar covered by Spar)", lgsec)
bc = collections.Counter(p["brand"].strip() for p in P if p.get("brand", "").strip())
bmiss = [(b, n) for b, n in bc.most_common() if b.lower() not in logo_file_names]
bmiss_row = [(b, n) for b, n in bc.most_common() if b.lower() not in logo_names]
blk = f"- Brands in products: {len(bc)}; brands without a logo file: {len(bmiss)} ({sum(n for _, n in bmiss)} products) — strict count, file-less placeholder rows excluded (lenient 'no logo row at all': {len(bmiss_row)} brands / {sum(n for _, n in bmiss_row)} products); logo rows with file: {len(LF)}/{len(L)}; top 8:\n" + "\n".join(f"  - [ ] {b} ({n} products)" for b, n in bmiss[:8]) + "\n"
lgsec = re.sub(r"(?ms)^- Brands in products:.*?(?=^- Producers missing logo)", lambda m: blk, lgsec)
meal = len(P); prices = len(PR)
tot = ["## Totals snapshot", "", f"- Products: {meal}", f"- Prices: {prices} (live 2026: {sum(v.get('live 2026',0) for v in by.values())})",
       f"- Logos: {len(L)}"] + [l for l in S.get("Totals snapshot", "").splitlines() if re.match(r"- (Stores|Companies|Online|External)", l)]
now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
gap = os.environ.get("NEXT_GAP") or re.search(r"\*\*Next biggest gap:\*\* (.*)", head).group(1)
head = re.sub(r"\*\*Last updated:\*\* .*", f"**Last updated:** {now} UTC", head)
head = re.sub(r"\*\*Next biggest gap:\*\* .*", f"**Next biggest gap:** {gap}", head)
conn = S.get("Connectors / catalog findings (this run)", "## Connectors / catalog findings (this run)\n\n")
extra = os.environ.get("CONNECTOR_NOTE")
if extra and extra not in conn: conn = conn.rstrip() + "\n" + extra + "\n\n"
order = ["Stores", "Ready meals with photos", "Logos", "Companies", "Tariffs & prices", "Public datasets", "Online meal-prep", "Connectors / catalog findings (this run)", "Totals snapshot"]
gen = {"Stores": "\n".join(st), "Ready meals with photos": "\n".join(ph), "Logos": lgsec, "Tariffs & prices": "\n".join(tp),
       "Connectors / catalog findings (this run)": conn, "Totals snapshot": "\n".join(tot) + "\n"}
out = head.rstrip() + "\n\n" + "\n".join((gen.get(k) or S.get(k, "")).rstrip() + "\n" for k in order if gen.get(k) or S.get(k))
open(COV, "w").write(out); print("COVERAGE.md updated", meal, "products")
