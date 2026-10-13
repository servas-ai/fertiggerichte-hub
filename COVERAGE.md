# Fertiggerichte coverage checklist

**Last updated:** 2026-10-13T03:16:47Z UTC
**Next biggest gap:** Spar photos/prices: 228/592 ready meals without photo and 135 prices only 2025; then Hofer 134/224 without photo + 87 Preis-2025 rows (Unimarkt verified closed → no live source possible; denn's/ADEG/Nah&Frisch have no product source)

Generated from `servas-ai/fertiggerichte-daten` (+ food-connectors catalog). Items are marked complete only when truly complete.

## Stores

| Chain | Products indexed? | # products | Branches (Linz+Umland OSM)? | # branches | Logo? |
|---|---|---|---|---|---|
| Spar | [x] | 592 | [x] | 50 | [x] |
| Billa | [x] | 618 | [x] | 74 | [x] |
| Billa Plus | [ ] | 0 | [x] | 9 | [x] |
| Hofer | [x] | 224 | [x] | 37 | [x] |
| Lidl | [x] | 40 | [x] | 20 | [x] |
| Penny | [x] | 17 | [x] | 22 | [x] |
| dm | [x] | 24 | [x] | 28 | [x] |
| denn's BioMarkt | [ ] | 0 | [x] | 2 | [x] |
| MPreis | [x] | 101 | [ ] | 0 | [x] |
| Unimarkt | [x] | 29 | [x] | 2 | [x] |
| ADEG | [ ] | 0 | [x] | 2 | [x] |
| Nah&Frisch | [ ] | 0 | [x] | 10 | [x] |
| Fit to Go | [x] | 24 | [ ] | 0 | [x] |
| Gurkerl | [x] | 356 | [ ] | 0 | [ ] |
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
| Billa | 618 | 615 ([x]) | 99.5% |
| Spar | 592 | 364 ([~]) | 61.5% |
| Gurkerl | 356 | 356 ([x]) | 100.0% |
| Hofer | 224 | 90 ([~]) | 40.2% |
| unbekannt (OFF) | 136 | 125 ([~]) | 91.9% |
| MPreis | 101 | 101 ([x]) | 100.0% |
| PrepMyMeal | 90 | 90 ([x]) | 100.0% |
| Lidl | 40 | 29 ([~]) | 72.5% |
| Unimarkt | 29 | 0 ([ ]) | 0.0% |
| dm | 24 | 1 ([~]) | 4.2% |
| Fit to Go | 24 | 24 ([x]) | 100.0% |
| Penny | 17 | 12 ([~]) | 70.6% |
| LiveFresh | 10 | 10 ([x]) | 100.0% |
| FitTaste | 2 | 2 ([x]) | 100.0% |

- [x] Total products: **2263**
- [x] Total with photos: **1819** (80.4%)
- [x] MPreis photos: live webshop connector `mpreis-shop` (101/101)
- [ ] Unimarkt photos: 0/29 — no source possible: shop.unimarkt.at shows only 'UNIONLINE hat seinen Service eingestellt' (verified 2026-10-13), chain left retail 2026; rows are historic-only

## Logos

- [x] Logo index rows: **149** (`data/logos.csv`)
- Handelskette logos present: ['ADEG', 'Billa', 'Billa Plus', 'Hofer', 'Lidl', 'MPreis', 'Nah&Frisch', 'Penny', 'Spar', 'Unimarkt', "denn's BioMarkt", 'dm']
- [x] All tracked Handelskette logos present (Eurospar/Interspar covered by Spar)
- Brands in products: 263; top brands missing logo file: 6
  - [ ] fit2go.meals (Fit2go GmbH) (24 products)
  - [ ] TCM Emaille-Auflaufform (8 products)
  - [ ] I LIKE (7 products)
  - [ ] Riso Gallo (5 products)
  - [ ] GOOD (5 products)
  - [ ] Rana Ravioli (5 products)
- Producers missing logo (sample): 17 of top 20
  - [ ] BILLA AG
  - [ ] Unilever Austria
  - [ ] BILLA AG, Billa AG, IZ NÖ Süd, Straße 3, Objekt 16, 2355 Wr. Neudorf
  - [ ] Maresi Austria GmbH
  - [ ] Billa AG
  - [ ] Fit2go GmbH, Pucking (Produktion lt. Krone: Manufaktur Wien)
  - [ ] Iglo Austria
  - [ ] Pastificio RANA S.p.A.

## Companies

- [x] GLEIF lookups in dataset: **25/83** companies have LEI
- [~] Firmenbuchnummer (FN) present: **18/83** (from GLEIF register fields, not live HVD)
- [ ] Firmenbuch HVD API: **blocked** — `FIRMENBUCH_API_KEY` not set
- [x] VIES connector: live in food-connectors (`food company --vies`)
- [x] North Data connector: live public-page mode (`food company --northdata`)
- [~] Revenue fields filled: **16/83**

## Tariffs & prices

| Chain | Price rows | Status breakdown |
|---|---|---|
| Billa [~] | 596 | live 2026: 594 · Preis 2025: 2 |
| Spar [~] | 577 | live 2026: 442 · Preis 2025: 135 |
| Gurkerl [x] | 356 | live 2026: 356 |
| Hofer [~] | 123 | Preis 2025: 87 · live 2026: 35 · Preis unbestätigt: 1 |
| MPreis [x] | 101 | live 2026: 101 |
| PrepMyMeal [x] | 90 | live 2026: 90 |
| Unimarkt [ ] | 29 | Preis 2023: 20 · Preis 2024: 9 |
| Fit to Go [x] | 24 | live 2026: 24 |
| dm [~] | 23 | live 2026: 12 · Preis 2025: 11 |
| LiveFresh [x] | 10 | live 2026: 10 |
| Lidl [x] | 6 | live 2026: 6 |
| Penny [x] | 2 | live 2026: 2 |
- [x] MPreis: live 2026 prices from the webshop (stale 2023/24 dump rows replaced; only 52/149 still listed)
- [ ] Fresh live prices for Hofer/dm/Spar-2025 rows: need shop connectors or browser
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

## Totals snapshot

- Products: 2263
- Prices: 1937 (live 2026: 1672)
- Logos: 149
- Stores (OSM Linz bbox): 498
- Companies: 83
- Online meal-prep: 96
- External datasets catalogued: 11
