# Fertiggerichte coverage checklist

**Last updated:** 2026-10-13T18:58:00Z UTC
**Next biggest gap:** Photos: Subway 0/59 — subway.com menu pages drop non-browser clients (HTTP/2 reset / HTTP/1.1 tarpit) and media.subway.com robots.txt is Disallow: / → needs a sanctioned source; Hofer 101/224 without photo are historic; Unimarkt 0/29 (chain closed). Logos (strict, file required): 104 brands / 305 products — almost all Handels-Eigenmarken (Good Choice 49, Pappudia 24, dmBio 16, Spar enjoy, Chef Select/Menü, Vemondo, M/MPreis); real producer brands left: Namdong 11, The Green Garden 6, Yum Yum 5 (unreachable), Vifon 2. Companies: **15/133** still without LEI or verified UID (28 product rows) — remaining hard cases (UK Gü, CH Planted Foods AG, dissolved Delikatessa, Bauck GmbH without public UID, Mochi/Kasnudl/Knödelwerkstatt name mismatches, Firmenbuch key for the rest).

Generated from `servas-ai/fertiggerichte-daten` (+ food-connectors catalog). Items are marked complete only when truly complete.

## Stores

| Chain | Products indexed? | # products | Branches (Linz+Umland OSM)? | # branches | Logo? |
|---|---|---|---|---|---|
| Spar | [x] | 660 | [x] | 50 | [x] |
| Billa | [x] | 775 | [x] | 74 | [x] |
| Billa Plus | [ ] | 0 | [x] | 9 | [x] |
| Hofer | [x] | 224 | [x] | 37 | [x] |
| Lidl | [x] | 37 | [x] | 20 | [x] |
| Penny | [x] | 22 | [x] | 22 | [x] |
| dm | [x] | 34 | [x] | 28 | [x] |
| denn's BioMarkt | [ ] | 0 | [x] | 2 | [x] |
| MPreis | [x] | 272 | [ ] | 0 | [x] |
| Unimarkt | [x] | 29 | [x] | 2 | [x] |
| ADEG | [ ] | 0 | [x] | 2 | [x] |
| Nah&Frisch | [ ] | 0 | [x] | 10 | [x] |
| Fit to Go | [x] | 29 | [ ] | 0 | [x] |
| Gurkerl | [x] | 505 | [ ] | 0 | [x] |
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
| Billa | 775 | 772 ([x]) | 99.6% |
| Spar | 660 | 654 ([~]) | 99.1% |
| Gurkerl | 505 | 505 ([x]) | 100.0% |
| MPreis | 272 | 262 ([~]) | 96.3% |
| Hofer | 224 | 123 ([~]) | 54.9% |
| unbekannt (OFF) | 112 | 100 ([~]) | 89.3% |
| PrepMyMeal | 90 | 90 ([x]) | 100.0% |
| Subway | 59 | 0 ([ ]) | 0.0% |
| NORDSEE | 39 | 39 ([x]) | 100.0% |
| Lidl | 37 | 25 ([~]) | 67.6% |
| dm | 34 | 32 ([~]) | 94.1% |
| Fit to Go | 29 | 29 ([x]) | 100.0% |
| Unimarkt | 29 | 0 ([ ]) | 0.0% |
| Penny | 22 | 17 ([~]) | 77.3% |
| FitTaste | 18 | 18 ([x]) | 100.0% |
| LiveFresh | 10 | 10 ([x]) | 100.0% |

- [x] Total products: **2915**
- [x] Total with photos: **2676** (91.8%)
- [ ] MPreis photos: live webshop connector `mpreis-shop` (262/272)
- [ ] Unimarkt photos: 0/29 — no source possible: shop.unimarkt.at shows only 'UNIONLINE hat seinen Service eingestellt' (verified 2026-10-13), chain left retail 2026; rows are historic-only

## Logos

- [x] Logo index rows: **250** (211 with a logo file) (`data/logos.csv`)
- Handelskette logos present: ['ADEG', 'Billa', 'Billa Plus', 'Gurkerl', 'Hofer', 'Lidl', 'MPreis', 'Nah&Frisch', 'Penny', 'REWE Group', 'Spar', 'Subway', 'Unimarkt', "denn's BioMarkt", 'dm']
- [x] All tracked Handelskette logos present (Eurospar/Interspar covered by Spar)
- Brands in products: 346; brands without a logo file: 104 (305 products) — strict count, file-less placeholder rows excluded (lenient 'no logo row at all': 65 brands / 155 products); logo rows with file: 211/250; top 8:
  - [ ] Good Choice (49 products)
  - [ ] Pappudia (24 products)
  - [ ] dmBio (16 products)
  - [ ] Chef Select (13 products)
  - [ ] Spar enjoy (12 products)
  - [ ] Namdong (11 products)
  - [ ] Chef Menü (9 products)
  - [ ] SPAR enjoy (7 products)
- [~] Company/producer logos (app Firmen view, `companies.json`): **118/133** companies with a logo (was 114 before 2026-10-13T14: deli gourmet→deli dip, Ablinger, BioGourmet, Zum Dorfkrug now have vision-gated official logos; T15 brand logos Podravka/Heura/Nordsee/Mama/Maza/Englert are brand rows only — none of the 133 companies maps to them, so still 118; earlier 2026-10-13T13b via Stangl, Amlacher, Blue Elephant→Winkelbauer brand fallback; `NO_BRAND_FALLBACK` keeps PLANT BASED POWER from inheriting the Alimentastic distributor logo; 2026-10-13T12:44 +13 vision-gated company logos — Alimentastic, Bauck Mühle, Cecchin, ehrenwort, Greisinger, Hamker, Heiderbeck, Hiel, Mochi, Rila, Tops Foods, REWE Group, Mars). Still without logo (15, known dead ends): BS Gastro (Wiener Virtshaus, no site), Staudinger (logo white lettering, 238px), Ager (icon-font logo only), Glatz (Njami), Plant Based Power, Dairy 4 Fun (TLS), Doppelt, Franuí (SSL EOF), Galana (HTTP 406), Gastrotech, Hildegard-Grünkraft (TLS), La Crêpe de Brocéliande (TLS), Lamercantile Scardovi, Rügenwalder Mühle (windmill icon only), Whollees (TLS hostname mismatch, not bypassed). Evidence `fertiggerichte-daten/raw/logos_companies_2026-10-13T13.json`, `raw/logos_squad_2026-10-13T13b.json`, `raw/logos_squad_2026-10-13T14.json`, `raw/logos_squad_2026-10-13T15.json`.

## Companies

- [~] GLEIF lookups in dataset: **60/133** companies have LEI (was 59; +1 ANDROS for BONNE MAMAN 2026-10-13T19, evidence `fertiggerichte-daten/raw/gleif_verified_2026-10-13T19.json`; was 50 before T16). Remaining without LEI have no GLEIF record under their label name or only a non-matching candidate
- [~] Firmenbuchnummer (FN) present: **54/133** (was 47; +7 from T19 Impressum/VIES); German register no. (HRA/HRB) present: **20/133**
- [~] Legal entity identified (LEI or VIES-verified UID): **118/133** (was 106 before 2026-10-13T19, 80 before T17, 71 before T16); UID present: **60/133** (35 ATU, 20 DE, 3 IT, 1 FR, 1 NL), all checked live in EU VIES. Products whose producer is still unidentified: **28** company-linked rows (was 53)
- [~] Konzernmutter (GLEIF ultimate parent): **11/133**
- [ ] Firmenbuch HVD API: **blocked** — `FIRMENBUCH_API_KEY` not set
- [x] VIES connector: live in food-connectors (`food company --vies`)
- [x] Impressum connector: live in food-connectors (`food company NAME --impressum DOMAIN`, MCP `company_impressum`): FN/HRB/UID from the public legal notice (robots.txt respected, no JS/cookies), every UID verified via VIES + name match
- [x] North Data connector: live public-page mode (`food company --northdata`)
- [~] Revenue fields filled: **16/133**

## Tariffs & prices

| Chain | Price rows | Status breakdown |
|---|---|---|
| Billa [~] | 763 | live 2026: 746 · : 12 · Preis 2025: 5 |
| Spar [~] | 647 | live 2026: 493 · Preis 2025: 150 · : 4 |
| Gurkerl [x] | 505 | live 2026: 505 |
| MPreis [x] | 268 | live 2026: 268 |
| Hofer [~] | 164 | Preis 2025: 130 · live 2026: 27 · Preis unbestätigt: 7 |
| PrepMyMeal [x] | 90 | live 2026: 90 |
| dm [~] | 33 | live 2026: 27 · Preis 2025: 6 |
| Fit to Go [x] | 29 | live 2026: 29 |
| Unimarkt [ ] | 29 | Preis 2023: 20 · Preis 2024: 9 |
| FitTaste [x] | 16 | live 2026: 16 |
| LiveFresh [x] | 10 | live 2026: 10 |
| Penny [x] | 7 | live 2026: 7 |
| Lidl [x] | 6 | live 2026: 6 |
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

- [~] Brand logos (2026-10-13T15, Daten-Squad): **+6 vision-gated logos** — Wikimedia Commons (Public domain): Podravka (2024 SVG), Heura (Foods for Tomorrow, freigestellt), Nordsee (2024 SVG; LEH-Lizenzmarke von HOMANN); official sites (imprint/robots checked, no JS/cookies): Mama (red MAMA wordmark, mama.co.th — not the TF parent logo), Maza (maza.at SVG), Englert (feinkost-englert.de header logo, white mono recoloured to #1f1f1f for light UI). **+3 aliases** onto file-backed rows: Omis→Omis Schmankerl (REWE-AT GS1 9010437), Danny→Danone (OFF 'Danone Dany'), Spar Linguine→Spar (SPAR-AT GS1 9100000). Strict logo-less **98→89 brands / 273→262 products**; logo rows with file 203→209/248. Rejected: Yopokki (ypfoods.co.kr timeout, yopokki-us.com TLS handshake failure — not bypassed), Windisch ('W' icon only), innocent (cream icon only), Findus (en.wiki fair-use only), Feinkost Leitinger (white-only + generic brand string 'Feinkost'), Thai Delight (product photo only), La Cocina de Lola (entity unverified). Evidence fertiggerichte-daten/raw/logos_squad_2026-10-13T15.json.
- [~] Brand logos (2026-10-13T18, Daten-Squad): **+2 vision-gated logos** — **Subway** (Wikimedia Commons File:Subway 2016 logo.svg, Public domain/trademarked, unmodified SVG; now on all 59 Subway rows — previously the largest logo-less brand) and **Alpenhain** (Commons File:Alpenhain Logo.png, CC BY-SA 4.0 Robert Winkelmann, resized 512 px; 2 Gurkerl rows). Strict logo-less (file required) on the same product set **106→104 brands / 366→305 products** (header said 89/262 from the T15 snapshot of 2483 products; the product set has since grown to 2915, so 101/356 at 2841 and 106/366 at 2915 before this pass — header and this section now use the same strict count). Subway photos **0/59 unchanged**: subway.com/de-AT menu pages drop non-browser clients (HTTP/2 stream reset, HTTP/1.1 tarpit; WebFetch text-only/404), media.subway.com robots.txt Disallow: /, the nutrition PDF has no product photos → nothing mapped, no URLs guessed. Rejected: Vifon (official vifon.com.vn SVG OK, but MPreis/Gurkerl VIFON products may be the European Vifon brand — producer unverified), Yum Yum (yumyum.co.th unreachable), Staudinger/Schulzi's/Chef Select (no Commons file; Eigenmarken by policy). Evidence fertiggerichte-daten/raw/subway_2026-10-13T18.json.
- [~] Companies GLEIF pass (2026-10-13T16, Daten-Squad): all 62 companies without LEI/UID queried via GLEIF `lei-records?filter[fulltext]` (cleaned label names), every hit reviewed against the product label: **+9 verified LEIs** — Alnatura (label address = GLEIF address, AlnaturA Produktions- und Handels GmbH), Molkerei Alois Müller (Zollerstraße 7; ultimate parent Unternehmensgruppe Theo Müller), Pastificio Rana (Via Pacinotti 25), Ehrmann GmbH Oberschönegg im Allgäu, Galana NV, Delamaris, Doppelt Sp. z o.o., Dairy 4 Fun s.r.o., La Crêpe de Brocéliande (8 rue Pierre Legault; parent Financière RT). 19 candidates rejected with reasons (Danone GmbH ambiguous, Gas Ager ≠ Ager, Recheis Holding ≠ Teigwaren, Hammermühle Diät GmbH, Gastrotech UG ≠ s.r.o., MEICA Construction, Blaško s.r.o. …). Overlay `fertiggerichte-daten/scripts/enrich_companies_gleif_verified.py` (hooked into companies_enrich so 24h reruns keep them); evidence `raw/gleif_verified_2026-10-13T16.json`. Also: daten re-exported from the current app build (products 2630→2841) — the 14:15 export left uncommitted by the DNS outage had under-reported 2483.
- [~] Companies Impressum + VIES pass (2026-10-13T17, Daten-Squad): all 53 companies without LEI/UID re-tried; real domains located via web search where the guessed ones were dead (youcook-food.com, fittogo.at, stanglnudeln.at, ager.cc, amlachernudel.com, andros-fruit.eu, feel-food.com, harvestmoon.de, kikkoman.de, zum-dorfkrug.de, bio-gourmet.com, delidip.com …); every UID checked live in EU VIES. **+26 legal entities** (LEI-or-UID 80→106/133, UID 21→47, FN 39→47): Unilever Austria (ATU49997507, FN 197801i), iglo Austria (ATU62784838, FN 279637g), Fit2go (ATU80022878, FN 615822x), YOUCOOK (DE118545567, HRB 111731 Köln), Stangl Teigwaren (ATU68093234, FN 400694g), Andros Austria (ATU69012506, FN 423232a), BS Gastro & Event Services, Caro Fratello, Ager (FN 43270h), Amlacher Nudel GmbH, deli gourmet (FN 396515k), Lamercantile Scardovi (FN 187561a), Cecchin (IT03248880282), AIA (IT00233470236), Heiploeg International (NL853640804B01), Kikkoman Trading Europe, Planted Foods GmbH, PLANT BASED POWER, Whollees, BioGourmet, Hammermühle, Zum Dorfkrug KG, Every. (label-artifact record), PENNY (ATU43203403), dm drogerie markt (ATU35195908), Wilhelm Blasko (ATU27179709). `uid_source` in the evidence separates ids printed on the own legal notice (19) from directory UIDs accepted only on exact VIES name + address match (7). 16 rejected with reasons (BauckOnline ≠ Bauck, Strauss Josef ≠ 'Strauss GmbH', Hiel & Co ≠ Peter Hiel, Knödelwerkstatt UID invalid in VIES, Unimarkt KG ≠ 'Unimarkt GmbH', Gastrotech ambiguous, Franuí no VIES name, Delikatessa dissolved …). Box egress: Unilever/iglo HTTP 403 (bot protection, not bypassed — read via public fetch only), several .at hosts TLS EOF. food-connectors impressum adapter: VAT regex now accepts grouped digits ('ATU 43 20 34 03', 'NL 853 640 804 B 01'). Evidence `fertiggerichte-daten/raw/impressum_vies_2026-10-13T17.json`.
- [~] Companies Impressum + VIES + GLEIF pass (2026-10-13T19, Daten-Squad): the remaining 27 companies without LEI/UID re-tried. **+12 legal entities** (LEI-or-UID 106→118/133, UID 47→60, LEI 59→60, FN 47→54): Recheis Teigwaren (ATU31064200 = Josef Recheis Eierteigwarenfabrik…, re-queried with exact VIES name), Rewe Austria Fleischwaren (ATU36273108, FN 65329y), Rewe Austria Genussküche (ATU51289001, FN 204764z), Graninger Holding→Graninger GmbH (ATU76281514), Hochreiter Quality Meat Factory→Hochreiter Lebensmittelbetriebe (ATU58071589), Landtmann´s feine Patisserie→Querfeld's Wiener Konditorei (ATU61901400), Inzersdorfer Nahrungsmittelwerke→MARESI Austria (ATU61613203; historic Nahrungsmittelwerke dissolved), Meica→Meica Ammerländische Fleischwarenfabrik Fritz Meinen GmbH & Co. KG (DE117832698), Deflorian S.r.l.→Deflorian Tiefkühlspezialitäten GmbH (ATU64259769), Strauss GmbH→STRAUSS JOSEF GMBH (IT01438820217), Danone GmbH→Danone Österreich GmbH (ATU34705405; also fills UID on the existing LEI row), BONNE MAMAN→ANDROS (FR13428682447 + LEI 9695006ARZU1PBC9M649, ultimate parent ANDROS ET CIE). 15 rejected with reasons (Alimentastic UID ATU70319525 VIES-INVALID; Bauck GmbH no public UID; Planted Foods AG CH; Gü UK; Knödelwerkstatt empty/invalid; Mochi/Kasnudl/Stadtküche/Delikatessa/Franuí/Gastrotech/Hildegard/Hiel/Unimarkt/MPREIS-Partner unchanged). Evidence `fertiggerichte-daten/raw/impressum_vies_2026-10-13T19.json` + `raw/gleif_verified_2026-10-13T19.json`. Logos not changed this run (Namdong/Ager/Leitgeb's — no clean Commons/official freigestelltes asset found in time).

- [-] Hofer photo gap (2026-10-13T16): fuzzy brand+name match of the 101 photo-less Hofer rows against the 1276-product hofer.at sitemap crawl (raw/hofer_2026-10-13) → only FAIRHOF Spareribs Sous Vide matches; the rest (Good Choice/Primana/Cucina Nobile heisse-preise 2023–25 rows) are no longer listed → no photo source, kept as historic.
- [-] Subway (2026-10-13T18): nutrition PDF (subway.com/v1v2/assets/de-at/…c2-march-2026) still OK (200, parser on local branch squad/linz-providers); per-item photos blocked — subway.com/de-AT menu HTML: HTTP/2 INTERNAL_ERROR / HTTP/1.1 25 s timeout from the box, WebFetch text-only or 404; media.subway.com robots Disallow: /; not bypassed. Evidence fertiggerichte-daten/raw/subway_2026-10-13T18.json.

## Totals snapshot

- Products: 2915
- Prices: 2567 (live 2026: 2224)
- Logos: 250
- Stores (OSM Linz bbox): 498
- Companies: 133 (60 with LEI, 118 with LEI or verified UID, 54 with FN)
- Online meal-prep: 96
- External datasets catalogued: 11
