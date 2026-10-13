# Fertiggerichte coverage checklist

**Last updated:** 2026-10-13T02:27:25Z UTC
**Next biggest gap:** MPreis/Unimarkt products have no image_url (heisse dump provides none)

Generated from `servas-ai/fertiggerichte-daten` (+ food-connectors catalog). Items are marked complete only when truly complete.

## Stores

| Chain | Products indexed? | # products | Branches (Linz+Umland OSM)? | # branches | Logo? |
|---|---|---|---|---|---|
| Spar | [x] | 531 | [x] | 50 | [x] |
| Billa | [x] | 494 | [x] | 74 | [x] |
| Billa Plus | [ ] | 0 | [x] | 9 | [x] |
| Hofer | [x] | 139 | [x] | 37 | [x] |
| Lidl | [x] | 18 | [x] | 20 | [x] |
| Penny | [x] | 2 | [x] | 22 | [x] |
| dm | [x] | 23 | [x] | 28 | [x] |
| denn's BioMarkt | [ ] | 0 | [x] | 2 | [ ] |
| MPreis | [x] | 149 | [ ] | 0 | [ ] |
| Unimarkt | [x] | 29 | [x] | 2 | [ ] |
| ADEG | [ ] | 0 | [x] | 2 | [ ] |
| Nah&Frisch | [ ] | 0 | [x] | 10 | [ ] |
| Fit to Go | [x] | 24 | [ ] | 0 | [x] |
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
| Spar | 531 | 358 ([~]) | 67.4% |
| Billa | 494 | 491 ([~]) | 99.4% |
| MPreis | 149 | 0 ([ ]) | 0.0% |
| Hofer | 139 | 56 ([~]) | 40.3% |
| unbekannt (OFF) | 62 | 49 ([~]) | 79.0% |
| Unimarkt | 29 | 0 ([ ]) | 0.0% |
| Fit to Go | 24 | 24 ([x]) | 100.0% |
| dm | 23 | 0 ([ ]) | 0.0% |
| Lidl | 18 | 17 ([~]) | 94.4% |
| Penny | 2 | 2 ([x]) | 100.0% |

- [x] Total products: **1471**
- [x] Total with photos: **997** (67.8%)
- [ ] MPreis/Unimarkt photos: heisse-preise dump has no image URLs (0%)
- [x] Filtering: classics `dishes.dish_key` + pack-size ≥150 g + non-meal exclusions

## Logos

- [x] Logo index rows: **135** (`data/logos.csv`)
- Handelskette logos present: ['Billa', 'Hofer', 'Lidl', 'Penny', 'Spar', 'dm']
- [ ] Missing Handelskette logos: MPreis, Unimarkt, denn's BioMarkt, ADEG, Nah&Frisch, Fit to Go, Billa Plus (separate), Eurospar/Interspar (covered by Spar)
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
| Spar [~] | 526 | live 2026: 401 · Preis 2025: 125 |
| Billa [~] | 483 | live 2026: 481 · Preis 2025: 2 |
| MPreis [ ] | 149 | Preis 2023: 79 · Preis 2024: 70 |
| Hofer [~] | 86 | Preis 2025: 55 · live 2026: 30 · Preis unbestätigt: 1 |
| Unimarkt [ ] | 29 | Preis 2023: 20 · Preis 2024: 9 |
| Fit to Go [x] | 24 | live 2026: 24 |
| dm [~] | 23 | live 2026: 12 · Preis 2025: 11 |
| Lidl [x] | 6 | live 2026: 6 |
- [x] MPreis/Unimarkt prices appended from heisse-preise.io (stale 2023–2024 dump dates — marked `Preis YYYY`, not live)
- [ ] Fresh live tariffs for MPreis/Unimarkt/Hofer/dm: need browser or revived shop APIs

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

## Totals snapshot

- Products: 1471
- Prices: 1326
- Stores (OSM Linz bbox): 498
- Logos: 135
- Companies: 83
- Online meal-prep: 96
- External datasets catalogued: 11
