# Fertiggerichte coverage checklist

**Last updated:** 2026-10-13T12:53:59Z UTC
**Next biggest gap:** Logos (strict, file required): brands without a logo file still led by Hofer/Lidl/dm/Spar Eigenmarken (Good Choice 47, Pappudia 23, dmBio 15, Chef Select 13, SPAR enjoy 12 — no clean official asset; Aldi CDN 403). Company logos 111/133 (22 small producers without verified site). Companies: 62/133 without LEI or verified UID (JS-only imprints; Firmenbuch key missing). Hofer 102/224 without photo, 87 Hofer + 135 Spar rows on 2025 prices (Akamai/Cloudflare). Product deserts: denn's/ADEG/Nah&Frisch (catalog-only).

Generated from `servas-ai/fertiggerichte-daten` (+ food-connectors catalog). Items are marked complete only when truly complete.

## Stores

| Chain | Products indexed? | # products | Branches (Linz+Umland OSM)? | # branches | Logo? |
|---|---|---|---|---|---|
| Spar | [x] | 592 | [x] | 50 | [x] |
| Billa | [x] | 670 | [x] | 74 | [x] |
| Billa Plus | [ ] | 0 | [x] | 9 | [x] |
| Hofer | [x] | 224 | [x] | 37 | [x] |
| Lidl | [x] | 40 | [x] | 20 | [x] |
| Penny | [x] | 17 | [x] | 22 | [x] |
| dm | [x] | 33 | [x] | 28 | [x] |
| denn's BioMarkt | [ ] | 0 | [x] | 2 | [x] |
| MPreis | [x] | 211 | [ ] | 0 | [x] |
| Unimarkt | [x] | 29 | [x] | 2 | [x] |
| ADEG | [ ] | 0 | [x] | 2 | [x] |
| Nah&Frisch | [ ] | 0 | [x] | 10 | [x] |
| Fit to Go | [x] | 24 | [ ] | 0 | [x] |
| Gurkerl | [x] | 464 | [ ] | 0 | [x] |
| Eurospar | [ ] | 0 | [x] | 25 | [x] |
| Interspar | [ ] | 0 | [x] | 4 | [x] |

Other OSM chains in bbox:

- [x] Convenience (sonstige): 96 branches (products not separately tracked)
- [x] Supermarkt (sonstige): 42 branches (products not separately tracked)
- [x] Bipa: 35 branches (products not separately tracked)
- [x] Drogerie (sonstige): 9 branches (products not separately tracked)
- [x] Spar Express: 8 branches (products not separately tracked)
- [x] Müller: 6 branches (products not separately tracked)
- [x] Norma: 6 branches (products not separately tracked)
- [x] Bio (sonstige): 3 branches (products not separately tracked)
- [x] Sonnentor: 3 branches (products not separately tracked)
- [x] Maximarkt: 2 branches (products not separately tracked)
- [x] Weltladen: 2 branches (products not separately tracked)
- [x] Mutter Erde: 1 branches (products not separately tracked)

## Ready meals with photos

| Chain | Products | With image_url | % photos |
|---|---|---|---|
| Billa | 670 | 667 ([x]) | 99.6% |
| Spar | 592 | 592 ([x]) | 100.0% |
| Gurkerl | 464 | 464 ([x]) | 100.0% |
| Hofer | 224 | 122 ([~]) | 54.5% |
| MPreis | 211 | 207 ([~]) | 98.1% |
| unbekannt (OFF) | 135 | 124 ([~]) | 91.9% |
| PrepMyMeal | 91 | 91 ([x]) | 100.0% |
| Lidl | 40 | 29 ([~]) | 72.5% |
| dm | 33 | 31 ([~]) | 93.9% |
| Unimarkt | 29 | 0 ([ ]) | 0.0% |
| Fit to Go | 24 | 24 ([x]) | 100.0% |
| Penny | 17 | 12 ([~]) | 70.6% |
| LiveFresh | 10 | 10 ([x]) | 100.0% |
| FitTaste | 2 | 2 ([x]) | 100.0% |

- [x] Total products: **2542**
- [x] Total with photos: **2375** (93.4%)
- [ ] MPreis photos: live webshop connector `mpreis-shop` (207/211)
- [ ] Unimarkt photos: 0/29 — no source possible: shop.unimarkt.at shows only 'UNIONLINE hat seinen Service eingestellt' (verified 2026-10-13), chain left retail 2026; rows are historic-only

## Logos

- [x] Logo index rows: **223** (178 with a logo file) (`data/logos.csv`)
- Handelskette logos present: ['ADEG', 'Billa', 'Billa Plus', 'Gurkerl', 'Hofer', 'Lidl', 'MPreis', 'Nah&Frisch', 'Penny', 'REWE Group', 'Spar', 'Unimarkt', "denn's BioMarkt", 'dm']
- [x] All tracked Handelskette logos present (Eurospar/Interspar covered by Spar)
- Brands in products: 350; brands without a logo file: 140 (394 products) — strict count, file-less placeholder rows excluded (lenient 'no logo row at all': 88 brands / 222 products); logo rows with file: 178/223; top 8:
  - [ ] Good Choice (47 products)
  - [ ] Pappudia (24 products)
  - [ ] Wagner (19 products)
  - [ ] dmBio (15 products)
  - [ ] Chef Select (13 products)
  - [ ] Spar enjoy (12 products)
  - [ ] The Green Garden (11 products)
  - [ ] GAON - Koreanisches Restaurant (10 products)
- [~] Company/producer logos (app Firmen view, `companies.json`): **111/133** companies with a logo (was 88; 2026-10-13T12:44 +13 vision-gated company logos — Alimentastic, Bauck Mühle, Cecchin, ehrenwort, Greisinger, Hamker, Heiderbeck, Hiel, Mochi, Rila, Tops Foods from official sites with imprint/legal-name check, REWE Group + Mars from Wikimedia Commons (public domain) — plus brand-alias fallback in `scripts/app_companies.py`, e.g. Kasnudl→Stadtküche, Berglandmilch→Schärdinger, Allos→Little Lunch). Still without logo (22): BS Gastro (Wiener Virtshaus), Stangl, Staudinger, Ager, Amlacher, Glatz (Njami), Plant Based Power, BioGourmet, Dairy 4 Fun, Doppelt, Franuí (SSL EOF), Ablinger, Galana (HTTP 406), Gastrotech, Hildegard-Grünkraft, La Crêpe de Brocéliande, Lamercantile Scardovi, Rügenwalder Mühle (windmill icon only, no wordmark), Whollees/Winkelbauer (TLS hostname mismatch, not bypassed), Zum Dorfkrug (domain parked), deli gourmet. Evidence `fertiggerichte-daten/raw/logos_companies_2026-10-13T13.json`.

## Companies

- [~] GLEIF lookups in dataset: **50/133** companies have LEI (was 25/83; +25 via stricter-but-broader matcher, 2026-10-13T10). Remaining 83 have no GLEIF record under their label name (many small AT producers never needed an LEI) or only a non-matching candidate (rejected list in `fertiggerichte-daten/raw/gleif_matching_2026-10-13T10.json`)
- [~] Firmenbuchnummer (FN) present: **39/133** (27 from GLEIF RA000017 + 12 from the companies' own legal notices)
- [~] Legal entity identified (LEI or VIES-verified UID): **71/133** (was 50); UID present: **21/133** (11 ATU, 10 DE), all checked live in EU VIES 2026-10-13
- [~] Konzernmutter (GLEIF ultimate parent): **8/133**
- [ ] Firmenbuch HVD API: **blocked** — `FIRMENBUCH_API_KEY` not set
- [x] VIES connector: live in food-connectors (`food company --vies`)
- [x] Impressum connector: live in food-connectors (`food company NAME --impressum DOMAIN`, MCP `company_impressum`): FN/HRB/UID from the public legal notice (robots.txt respected, no JS/cookies), every UID verified via VIES + name match
- [x] North Data connector: live public-page mode (`food company --northdata`)
- [~] Revenue fields filled: **16/133**

## Tariffs & prices

| Chain | Price rows | Status breakdown |
|---|---|---|
| Billa [~] | 648 | live 2026: 646 · Preis 2025: 2 |
| Spar [~] | 577 | live 2026: 442 · Preis 2025: 135 |
| Gurkerl [x] | 464 | live 2026: 464 |
| MPreis [x] | 210 | live 2026: 210 |
| Hofer [~] | 123 | Preis 2025: 87 · live 2026: 35 · Preis unbestätigt: 1 |
| PrepMyMeal [x] | 91 | live 2026: 91 |
| dm [~] | 32 | live 2026: 26 · Preis 2025: 6 |
| Unimarkt [ ] | 29 | Preis 2023: 20 · Preis 2024: 9 |
| Fit to Go [x] | 24 | live 2026: 24 |
| LiveFresh [x] | 10 | live 2026: 10 |
| Lidl [x] | 6 | live 2026: 6 |
| Penny [x] | 2 | live 2026: 2 |
- [x] MPreis: live 2026 prices from the webshop (stale 2023/24 dump rows replaced; only 52/149 still listed)
- [ ] Fresh live prices for Hofer/Spar-2025 rows: need shop connectors or browser (hofer.at Akamai 403, interspar.at Cloudflare)
- [x] dm: live 2026 prices via food-connectors `dm` (dm.at sitemap + products.dm.de product JSON); the 6 remaining 'Preis 2025' dm rows are not in the dm.at 2026 product sitemap (delisted) -> no live price possible, kept flagged
- [-] Unimarkt: no live price possible — webshop closed 02/2024, chain exited retail 02-03/2026 (29 rows kept as flagged 2023/24 history)

## Public datasets

- [x] `off-hf` — Open Food Facts product-database (Parquet) (freshness: daily)
- [x] `off-kaggle` — Open Food Facts world-food-facts (Kaggle) (freshness: stale (2017 snapshot))
- [x] `heisse-preise` — heisse-preise.io daily dump (badlogic/heissepreise, MIT) (freshness: daily)
- [x] `heisse-preise-data` — falknerdominik/heisse-preise-data (freshness: pushed 2026-10-12)
- [x] `ciqual` — ANSES CIQUAL 2020 (freshness: 2020)
- [x] `usda-fdc` — USDA FoodData Central (freshness: semi-annual 2026)
- [x] `swiss-fcdb` — Swiss Food Composition Database (BLV) (freshness: V7.0 (2024+))
- [x] `bls` — Bundeslebensmittelschlüssel BLS 4.0 (MRI) (freshness: 2025)
- [x] `zenodo-nl` — Dutch supermarket product data (Zenodo 10.5281/zenodo.19220002) (freshness: 2026-03)
- [x] `kaggle-de-retail` — German retail supermarket dataset (Kaggle sanku758) (freshness: unknown, likely synthetic)
- [x] `data-gv-lebensmittelbuch` — Österreichisches Lebensmittelbuch (data.gv.at) (freshness: 2021)
- [x] Catalog searchable live via `food datasets --search` / MCP `search_datasets`

## Online meal-prep

- [x] Online: PrepMyMeal: 86 dishes (`data/online_mealprep.csv`)
- [x] Online: LiveFresh: 10 dishes (`data/online_mealprep.csv`)
- [x] Total online meal-prep rows: **96**
- [x] Connectors: `prepmymeal`, `livefresh`, `gourmetfein` (Shopify `/products.json`)
- [ ] fit2go.meals / more providers: Hydrogen-shop or no public API (catalog)

## Connectors / catalog findings (this run)

- [x] `osm-stores` — live Overpass connector (`food stores --chain X --near linz`, MCP `list_stores`)
- [x] `mpreis` / `unimarkt` — ready meals imported from heisse-preise dump into fertiggerichte-daten
- [ ] `denns` — **catalog-only**: denns-biomarkt.at is Sanity marketing/info site; no product listing, `/sitemap.xml` 404, robots → biomarkt.de sitemap 404; no public product JSON/API; not bypassing bot protection (none needed — simply no shop data)
- [ ] `adeg` — **catalog-only**: adeg.at sitemap = pages/news/recipes only; no online shop / product API
- [ ] `nah-frisch` — **catalog-only**: nahundfrisch.at franchise info site; no webshop
- [x] `mpreis-shop` — **live** MPreis webshop connector (sitemap + category pages + product JSON-LD; robots-allowed, `/search/` never used): 271 pages crawled, 0 errors → 101 ready meals with photo, live 2026 price, GTIN, pack size; 85 with nutrition table. CLI `food search … --store mpreis-shop`, MCP `mpreis_product`.
- [-] `unimarkt-shop` — **closed, verified 2026-10-13**: shop.unimarkt.at answers 200 but sampled sitemap slugs (/fertiggerichte, /suppen, /snacks-fertiggerichte, /gulaschsuppe) 302 → / (others 404) = splash "UNIONLINE hat seinen Service eingestellt – Vielen Dank für Ihre Treue"; ajaxGateway only cart/merkliste actions; /suche/ 403 (not retried). Shop closed 02/2024 (cash.at), Unimarkt left retail 02–03/2026 (ooe.ORF.at: ~90 stores, ADEG 21 / Spar 23 / Nah&Frisch 2). Registered as catalog-only in food-connectors; evidence `fertiggerichte-daten/raw/unimarkt_shop_probe_2026-10-13.json`. OSM still tags some ex-Unimarkt branches.
- [x] `spar` CDN images — **live** (2026-10-13): heisse-preise spar article id → `cdn1.interspar.at/cachableservlets/articleImage.dam/at/{id}/dt_main.jpg` HEAD-verified for all 228 previously photo-less Spar ready meals (228/228). CLI/MCP `food search` / Spar adapter now returns `image_url`. Evidence `fertiggerichte-daten/raw/spar_cdn_images_2026-10-13.json`. interspar.at HTML still Cloudflare-blocked.
- Hofer photos +35→32 net strict OFF matches (90→122/224); prices: 86 heisse provenance refresh (no 2026 dates; hofer.at Akamai 403). Script: fertiggerichte-daten/scripts/enrich_hofer_images.py.

- Hofer enrichment 2026-10-13: photos 90→122/224 via strict OFF match (scripts/enrich_hofer_images.py in fertiggerichte-daten); 86 heisse price provenance refreshes (no 2026 Hofer dates; hofer.at Akamai 403). Aldi CDN brandfam near-misses unused after strict filter.
- [x] `dm` photos — **live** (2026-10-13T09): dm.at product sitemap (robots-allowed) → DAN → public product JSON `products.dm.de/product/products/detail/AT/dan/{dan}` (no login/cookies, non-AI images only), + Lotao official Shopify `products.json` + OFF barcode API; all GET-verified. dm photos 1→22/24 (open: Lotao Chili sin Carne 350 g — no 350 g variant anywhere; dmBio Veganuary Chili con Grünkern — delisted). dm.at `/search` robots-disallowed → not used. Script `fertiggerichte-daten/scripts/enrich_dm_images.py`, evidence `raw/dm_images_2026-10-13.json`.
- [~] Eigenmarke logos (2026-10-13T09): Primana (pack crop, vision-gate pass) → 43 Hofer/Spar rows, Asia Green Garden → 12 rows, Lotao (official og:image, vision-gate pass) → 9 rows. Aldi CDN `2026_MA_/2025_MA_/Brandpage-Logo_*` probed for 22 Hofer Eigenmarken (616 GET variants, control Le Gusto 200) → all 403; Wikimedia Commons no hits; lidl.at has only a /c/deluxe photo banner (no clean logo). Good Choice, Nature's Gold, PIZZ'AH, Leibspeis', Natur Aktiv, Rettenswert, Wonnemeyer, Chef Select, Vemondo, Vitasia, McEnnedy, Kania … stay empty (no fabricated logos). Evidence `fertiggerichte-daten/raw/hofer_lidl_logo_probe_2026-10-13.json`.
- [x] `dm` — **live connector** (2026-10-13T10): food-connectors `dm` adapter = dm.at product sitemap (robots-allowed) → public product JSON `products.dm.de/product/products/detail/AT/dan/{dan}` (price, GTIN, nutrition table, ingredients, origin, non-AI image; no login/cookies; `/search` never used). Ready meals = dm breadcrumb 'Fertiggerichte & Konserven'. CLI `food search … --store dm`, `food fetch --store dm`, MCP `search_products`/`fetch_ready_meals` with stores=dm. Old heisse snapshot moved to `dm-heisse`. Data: dm 25→34 rows (+14 new meals/soups, 5 heisse Altpreis duplicates excluded), live 2026 prices 12→26, photos 32/34; 3 instant mixes flagged dry (nutrition per prepared product); BioGourmet Baked Beans macros dropped (dm table all 0 g). Script `fertiggerichte-daten/scripts/enrich_dm_live.py`, evidence `raw/dm_live_2026-10-13.json`.

- [~] Brand logos (2026-10-13T10): +10 vision-gated logos wired to ~79 app rows — Bertagni, Bonduelle, HOFMANNs, Landliebe, Alpro, Müller (Molkerei Müller), Picard, Schärdinger (Wikimedia Commons, licence noted) + Freshery (freshery.sk shop logo), Every. (every-foods.com header); Karnerta logo now also mapped to brand 'Karnerta' (MPreis). Pappudia, GAON, The Green Garden, Deflorian, Bibigo, Strauss, Mochi: no verifiable official logo source found this run (no own site / Commons hit; Bibigo site has no extractable logo asset) → stay empty. Lidl `/q/api/search` again 401 for every sweep request after 4 OK single probes → stopped (no workaround). Penny online API (453 items) has only flyer items without nutrition/GTIN → not imported. Evidence `fertiggerichte-daten/raw/logos_lidl_penny_2026-10-13T10.json`.
- [x] `company:gleif` matcher (2026-10-13T10, food-connectors 27ed143): GLEIF exact legalName + fulltext over spelling variants (original / ASCII / ö→oe / legal-form-stripped); accept only token-Jaccard ≥ 0.85 on legal-form-agnostic, diacritic-folded names, same legal-form family (AG≡SpA≡NV, GmbH≡m.b.H.≡srl≡s.r.o.) and legal-address country = hint. LEI 25→50 (e.g. BILLA AG = Billa Aktiengesellschaft FN 118556y, Nestlé Österreich, FELIX Austria → parent Orkla, NÖM, Berglandmilch, Dr. Oetker AT, Danone AT, Radatz, Dr. Schär SpA, Rügenwalder Mühle). Rejected on purpose: Lidl Österreich GmbH LEI = German HRB entity (Neckarsulm), dm Verwaltungsgesellschaft, Ehrmann SE vs label 'Ehrmann GmbH', Unimarkt KG. Evidence `fertiggerichte-daten/raw/gleif_matching_2026-10-13T10.json`.
- [~] Brand logos (2026-10-13T11, Daten-Squad, daten 8abca80): **+30 vision-gated logos** — Wikimedia Commons (licence in source/note): Danone, Heinz, Hilcona, Hengstenberg (CC BY-SA 4.0, TIFF→PNG thumb), Kotányi, Nongshim, Perutnina Ptuj, Riso Scotti, SalzburgMilch, eismann, Uncle Ben's, Weight Watchers, Andechser Natur; official site headers (robots.txt checked, no JS/cookies): NÖM (+ nöm PRO/Cremix aliases), Zurück zum Ursprung, Bibigo, Berger Schinken, Bürger, Delamaris, DimmidiSì, Golfera, GREENFORCE, Gü (wordmark cropped from official og:image), Jeden Tag, Meica, NENI, Stadtküche (kasnudl.com), Wiegert, Bauernland (weinbergmaier.at), Brajlović (192 px site icon). **+14 aliases** only onto rows that really have a file (Tressbrüder, Planted., 'Maggi, Nestlé', Hubers, Little Lunch, Knorr Kaiser Teller, FitTaste, Hut & Stiel, VEGA VITA, Billabio, Spar Natur Pur, Dr. Oetker Ristorante …). Strict logo-less (file required): **208→154 brands, 555→430 products** (lenient row count 151/349→97/224). Rejected: Findus favicon (shape only), La Fermière (white-only SVG), miil.at/oyakata.de (other companies), Basenbox favicon, Riso Gallo (photo of a sign), Esterhazy (entity unverified), Thai President Foods (producer ≠ Mama brand). coverage.py now counts only logo rows with a file (file-less Hofer/Lidl Eigenmarken placeholders no longer hide gaps). Evidence fertiggerichte-daten/raw/logos_squad_2026-10-13T11.json. Deployed app 3d60a5b (99 app rows now show one of the new logos; app rows with logo 1600→1741 incl. hourly T11).

## Totals snapshot

- Products: 2542
- Prices: 2216 (live 2026: 1956)
- Logos: 223
- Stores (OSM Linz bbox): 498
- Companies: 133 (50 with LEI, 71 with LEI or verified UID, 39 with FN)
- Online meal-prep: 96
- External datasets catalogued: 11
