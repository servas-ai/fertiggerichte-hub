# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-17 03:34 UTC via `./run_all.sh` (stündlich).

**Connectors:** 21 ✅ / 3 ❌ / 5 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** ?

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 9 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 9 | 0 | 0 |
| Einkaufsanalyse | https://servas-ai.github.io/einkaufsanalyse/ | ✅ | 8 | 0 | 0 |

## Repositories

| Repo | Zweck |
|---|---|
| [servas-ai/fertiggerichte-vergleich](https://github.com/servas-ai/fertiggerichte-vergleich) | Web-App (Vergleich, Netz 3D, Gesundheit, Hersteller …) |
| [servas-ai/food-connectors](https://github.com/servas-ai/food-connectors) | Connectors + CLI + MCP-Server |
| [servas-ai/fertiggerichte-daten](https://github.com/servas-ai/fertiggerichte-daten) | Offener Datensatz CSV/JSON |
| [servas-ai/einkaufsanalyse](https://github.com/servas-ai/einkaufsanalyse) | Einkaufsanalyse-Dashboard (Kassenbons) |

## Architektur

```mermaid
flowchart LR
  subgraph Quellen
    BILLA & PENNY[REWE API] --> FC
    GURKERL[Gurkerl] --> FC
    LIDL[Lidl] --> FC
    HP[heisse-preise.io<br/>Spar/Hofer/dm/MPreis] --> FC
    OFF[Open Food Facts] --> FC
    MP[Meal-Prep: PrepMyMeal …] --> FC
  end
  FC[food-connectors<br/>CLI + MCP] --> DATA[(fertiggerichte-daten<br/>CSV/JSON)]
  DATA --> APP[fertiggerichte-vergleich<br/>GitHub Pages]
  BONS[Kassenbon-Fotos] --> EA[einkaufsanalyse]
  HUB[fertiggerichte-hub<br/>E2E + README] -.testet.-> FC & DATA & APP & EA
```

## Connector-Status (Live-Smoke-Test)

| | Connector | Store | Items | Latenz | Beispielprodukt (Beweis) | Zeitpunkt |
|---|---|---|---|---|---|---|
| ✅ | `alfies` | Alfies | 3 | 8.62 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g) · 4.49 € | 2026-10-17T02:56:15Z |
| ✅ | `billa` | BILLA | 3 | 1.59 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-17T02:56:24Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 8.11 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-17T02:56:26Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 4.85 s | [MyDeli Bio-Fleischsuppe](https://www.denns-biomarkt.at/angebote/) · 3.49 € | 2026-10-17T02:56:34Z |
| ✅ | `dm` | dm | 3 | 4.72 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-17T02:56:39Z |
| ✅ | `dm-heisse` | dm | 3 | 2.78 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-17T02:56:44Z |
| ✅ | `every` | Online: every. | 3 | 17.29 s | [Pumpkin Zucchini Risotto](https://every-foods.com/products/pumpkin-zucchini-risotto) · 8.99 € | 2026-10-17T02:56:47Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 8.91 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-17T02:57:05Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.44 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-17T02:57:14Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.2 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-17T02:57:20Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.46 s | [Rinder Gulaschfleisch am Stück](https://www.gurkerl.at/42171-rinder-gulaschfleisch-am-stueck) · 21.47 € | 2026-10-17T02:57:28Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 2.8 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-17T02:57:29Z |
| ✅ | `hofer` | HOFER | 3 | 2.74 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-17T02:57:33Z |
| ✅ | `juit` | Online: Juit | 1 | 1.84 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-17T03:16:05Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 36.47 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-17T03:28:31Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.25 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-17T03:29:21Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 3.02 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-17T03:29:23Z |
| ✅ | `mpreis` | MPREIS | 3 | 2.95 s | AIA Puten Gulasch · 6.5 € | 2026-10-17T03:29:26Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 8.9 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-10-17T03:29:30Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 33.19 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-10-17T03:29:40Z |
| ✅ | `nah-frisch` | Nah&Frisch | 3 | 242.95 s | [Inzersdorfer Fertiggerichte oder Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-17T03:30:13Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-17T02:56:15Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-17T02:56:25Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-17T02:57:14Z |
| ❌ | `issmich` |  | 0 | 300 s | `timeout 300s` |  |
| ❌ | `lidl` | Lidl | 0 | 12.99 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-17T03:29:08Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-17T03:29:21Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-17T03:29:26Z |
| ❌ | `off` | Open Food Facts | 0 | 0.76 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-10-17T03:34:16Z |

### Bekannte Ausfälle (manuell gepflegt)

- `off` (Open Food Facts) ❌ seit 2026-10-16 (Hub-Lauf 22:59 UTC) dauerhaft, nicht mehr nur Upstream-503: OFF `robots.txt` verbietet für `User-agent: *` jetzt `/api`, `/cgi` und `/facets`, und der neue harte robots.txt-Gate in food-connectors (`0eaa455`) blockiert `cgi/search.pl` (Suche) und `api/v2/product` (EAN-Lookup) bewusst vor dem Request. `search.openfoodfacts.org` ist ebenfalls `Disallow: /`. Fix-Pfad (offen, food-connectors `adapters/off.py`): EAN-Lookup über die erlaubte Produktseite `/product/<ean>` (HTML), Suche über Open Prices / Datensatz-Dump statt Live-Suche. Kein Bypass des Gates.
- `lidl` ❌ HTTP 401 (bekannt, Lidl-API verlangt Auth; kein Login erlaubt).

## Datensatz

**? Produkte** · Tabellen: 

| Abdeckung | % |
|---|---|

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|

</details>

## Screenshots

### Fertiggerichte-Vergleich

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich/home_1920.png" width="420"> | <img src="screenshots/vergleich/home_390.png" width="140"> |
| Was kaufe ich heute? | <img src="screenshots/vergleich/heute_1920.png" width="420"> | <img src="screenshots/vergleich/heute_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich/plan_1920.png" width="420"> | <img src="screenshots/vergleich/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich/ki_1920.png" width="420"> | <img src="screenshots/vergleich/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich/hofer-top30_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich/marken_1920.png" width="420"> | <img src="screenshots/vergleich/marken_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich/filialen_1920.png" width="420"> | <img src="screenshots/vergleich/filialen_390.png" width="140"> |

### Fertiggerichte-Vergleich (servas-ai Pages)

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich-servas/home_1920.png" width="420"> | <img src="screenshots/vergleich-servas/home_390.png" width="140"> |
| Was kaufe ich heute? | <img src="screenshots/vergleich-servas/heute_1920.png" width="420"> | <img src="screenshots/vergleich-servas/heute_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich-servas/plan_1920.png" width="420"> | <img src="screenshots/vergleich-servas/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich-servas/ki_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich-servas/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hofer-top30_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich-servas/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich-servas/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich-servas/marken_1920.png" width="420"> | <img src="screenshots/vergleich-servas/marken_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich-servas/filialen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/filialen_390.png" width="140"> |

### Einkaufsanalyse

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/einkaufsanalyse/home_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/home_390.png" width="140"> |
| Übersicht | <img src="screenshots/einkaufsanalyse/uebersicht_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/uebersicht_390.png" width="140"> |
| Verlauf | <img src="screenshots/einkaufsanalyse/verlauf_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/verlauf_390.png" width="140"> |
| Läden | <img src="screenshots/einkaufsanalyse/laeden_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/laeden_390.png" width="140"> |
| Kategorien | <img src="screenshots/einkaufsanalyse/kategorien_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/kategorien_390.png" width="140"> |
| Protein & Gesundheit | <img src="screenshots/einkaufsanalyse/protein_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/protein_390.png" width="140"> |
| Kassenbons | <img src="screenshots/einkaufsanalyse/bons_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/bons_390.png" width="140"> |
| Import | <img src="screenshots/einkaufsanalyse/import_1920.png" width="420"> | <img src="screenshots/einkaufsanalyse/import_390.png" width="140"> |

## Changelog (letzte Commits)

**servas-ai/fertiggerichte-vergleich**

- `f10b741` 2026-10-16 22:40 — UI: Online-Shop myProduct (Online/Kategorien, Farbe #be185d, Text-Logo SVG)
- `2fe7940` 2026-10-16 22:45 — data: Sensecheck 19 (pipeline fertig 4d27cfe): BILLA Bami Goreng 650 g = 2 portions (Billa label 302 kcal/19 g per portion) → light pool, out of topPLI/topPE; every. 51 rows delivers_4020 true→null (every. AGB §6 Abs.1: Lieferung nur Deutschland; shipping page says AT → contradictory, not ranked); Iglo Backteig Garnelen (Billa + Gurkerl) = component; myProduct Goldblatt jars merged into goldblatt.at rows (dupOf + alsoAt myProduct), Bio Kichererbsen Curry nutrition = Goldblatt 390 kcal/28.5 g. rows 3921, rankable 211→181. Gates: prepush_gate.sh OK (build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10808 broken images, gaps applied, top50 regress 0), pipeline pytest 118/118. No deploy.
- `b0eab37` 2026-10-16 22:30 — data: hourly T22 — new online store myProduct.at (+37 heat-up meals/soups from regional producers: Little Lunch 9, Danke Bauer 4, Goldblatt 4, Followfood 4, Rettergut 3, Perfect Earth 3, Hartls Kulinarikum Linz 2, Ökoland 2, Zwergenwiese 2 …), delivers_4020 true (myproduct.at/lieferung, 7,90 €/10 kg AT). Nutrition: 11 myproduct.at, 6 identical EAN in dataset, 20 Open Food Facts product page by exact EAN; never estimated (27 without nutrition kept out). Multipacks priced per pack, portion = unit glass (multipack_unit). Pipeline fertig bd00502. rows 3885→3921, rankable 211. Gates: prepush_gate.sh OK (build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10814 broken images, gaps applied, top50 regress 0), pipeline pytest 114/114. No deploy.
- `bf14026` 2026-10-16 22:18 — data: iglo Genießer-Pfanne per-portion fix (pipeline fertig a7dc722/b679a46): 650 g packs = 2 portions per iglo.at 'Pro Portion' (≈325 g; Tagliatelle Funghi/Ravioli 600 g → 300 g), incl. SPAR 'Iglo Französische Art Penne…' + MPreis 'Französische Pfanne' — 22 rows: portion 650→325, price/portion 7.69→3.85 €, kcal/portion halved (Billa Tortellini 656→328). Billa Tortellini/Französische Art/Paprika-Huhn + Spar Französische Art now light_meal (own ranking) → rankable 215→211, light pool 106→110; topPLI/topPE/topHealth/topLight unchanged. rows 3885. Sensecheck 18 re-verified on 64f6970: all points closed (Kernbeißer source = kernbeisser.at/agbs/ §7, no dedicated shipping page per sitemap; 0 rankable rows with delivers_4020 null/false). Gates: prepush_gate.sh OK (build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10698 broken images, gaps applied, top50 regress 0), pipeline pytest 111/111. No deploy.
- `64f6970` 2026-10-16 22:01 — Merge remote-tracking branch 'origin/main' into HEAD
- `8986842` 2026-10-16 22:01 — publish_only.sh: disk gate - abort before worktree/build if / or /tmp has < MIN_DISK_GB (default 3) GB free
- `d2bc354` 2026-10-16 21:56 — data: merge hourly T21 (+9 SPAR heat-up rows) + 9 verified rows from the 21:11 run; +15 bofrost* rows (bofrost.at verified); every. Mushroom Gnocchi vegan; SPAR Tradizionale Diavola without the wrong Ristorante twin nutrition. rows 3885, rankable 215. Pipeline fertig 130350a. pytest 98/98, top50 ok, regress ok, gaps_overlay applied. No deploy.
- `00e9135` 2026-10-16 21:53 — MealKits: per-box delivery text from delivers_4020/delivery_note (false → note or 'Liefert nicht nach 4020 Linz', true → 'Online / Lieferung', null/undefined → grey 'Lieferung nach 4020 nicht geprüft'), tooltip via deliveryTitle

**servas-ai/food-connectors**

- `c2b408b` 2026-10-16 23:50 — Daten-Squad T2336: denns connector extended — (1) dennree brand catalog (own brand of the dennree group / denn's BioMarkt) from www.dennree.de category + product pages (robots '*' allows; /productreload?id= ajax matches Disallow /*?id=* → not used): name, net weight, denomination, ingredients, nutrition/100 g with Atwater check, packshot by denn's article no., 'BILD FOLGT' placeholder detected by md5; no price/GTIN published; (2) 'Neu im Sortiment' page-data (isInAustria, regular shelf price, €/kg, Sanity image); (3) in-store bistro lunch menu (Mittagsgerichte page-data per market, current + next week, price, diet flags; counter dishes, not products). CLI food fetch --store denns --category eigenmarke|neu, MCP denns_brand_catalog / denns_new_products / denns_lunch_menu; 6 offline fixture tests (suite 104 passed / 3 skipped)
- `0eaa455` 2026-10-16 22:02 — polite: hard robots.txt gate + 1 s/host for every HTTP path. RobotsDisallowed raised before the request (cached per host, UA group + '*', RFC 9309: robots 4xx = allow, 5xx/unreachable = disallow); http.get and the 4 direct urlopen sites (alfies, osm_stores, issmich, company/registries) use polite_urlopen; package import installs the gate for urllib/requests/httpx/curl subprocess. tests/test_polite.py (interspar product page blocked without network call, allowed URL, UA group, 4xx/5xx/unreachable, rate limit, install routing). pytest 98 passed, 3 skipped.
- `32c9237` 2026-10-16 21:26 — Daten-Squad T2111: new live connector myproduct (myproduct.at regional-producer marketplace, category Fertiggerichte): category dataLayer + product JSON-LD Offer + Magento attribute table (EAN check digit, Nettofüllmenge, producer address, ingredients, allergens, MHD, nutrition per 100 g when published, Atwater check); exclusion rules for fonds/sauces/spreads/dry mixes/soup powders/meat-substitute raw goods; CLI food fetch|search --store myproduct, MCP myproduct_product/myproduct_search; 5 offline fixture tests
- `a00ce43` 2026-10-16 20:48 — Daten-Squad T2038: new live connector open-prices (Open Food Facts Open Prices REST API, ODbL): food prices EAN [--country AT --since], MCP open_prices_lookup, datasets catalog entry; 2 offline fixture tests (suite 82 passed / 3 skipped)
- `ac16ed7` 2026-10-16 19:53 — bofrost: starters += Pizzettis, Rösti-Baguette, Gemüse-/Broccoli-Laibchen, Schinken-Käse-Röllchen (warm baked snacks; breaded cheese stays out); ready-meals DISH_SLUG += schlemmerfilet; tests
- `994f35c` 2026-10-16 18:33 — bofrost: opt-in course fetches — fetch(category="desserts") warm Mehlspeisen (Knödel, Kaiserschmarrn, Topfennockerl, Mohnnudeln, Strudel, Palatschinken; no Torten/Eis/raw dough) and fetch(category="starters") warm Vorspeisen (Frühlingsrollen, Teigtaschen, Flammkuchen, Kaspressknödel); extra.course; default ready-meal filter unchanged; test_course_url_filters
- `8777b7a` 2026-10-14 07:30 — Daten-Squad T0740: new live connector alfies (Alfies Wien/Graz online supermarket, Alfie's GmbH, Wien)
- `9650f94` 2026-10-14 06:57 — Daten-Squad T0636: new live connector issmich (iss mich! Wiener Bio-Eintöpfe & Suppen im WECK-Glas, iss mich! GmbH, Wien)

**servas-ai/fertiggerichte-daten**

- `9b1a42e` 2026-10-17 01:04 — Daten-Squad T0039: DE VIES back (check-status Available) — 5 DE UIDs from legal notices now VIES-valid (ARCHE DE322242442, Ökoland Nord DE116156996, Rapunzel DE129088402, EgeSun DE455151638, Petersilchen DE124612378; DE discloses no name/address); Petersilchen GmbH now identified (HRB 11924 + valid UID) → legal entity 136→137/148; evidence raw/vies_de_2026-10-17T0039.json
- `c0bbc5b` 2026-10-17 00:14 — Daten-Squad T0003: Spar photo tail 729→732/735 via SPAR public search API (spar-shop): Inzersdorfer Rindsgulasch 800 g, Inzersdorfer Speckknödelsuppe, ehrenwort BIO Bangkok rotes Thai Curry 35g; dt_main.jpg GET 200, vision-gated; 3 Knorr rows rejected (SPAR names differ); photos 3425→3428/3651
- `2c7935c` 2026-10-16 23:50 — Daten-Squad T2336: denn's BioMarkt 5→15 products — +9 dennree brand-catalog ready meals (dennree = own brand of the dennree group / denn's BioMarkt; www.dennree.de category+product pages, DE brand site, AT availability per article not stated, marked in source): Al Forno Pizza Käse-Lauch 275 g / Spinat 350 g, Al Forno Flammkuchen Elsässer Art 260 g (TK), Vegane Falafel 200 g, Vegane Burger auf Seitanbasis 180 g, Vegane Gemüsebratlinge Champignon / Rote Bete 150 g, Vegetarische Knuspernuggets 180 g / Schnitzel 200 g — nutrition per 100 g as published (9/9 Atwater ok), ingredients, net weight, packshot by denn's article no. (7 HTTP 200 + vision-gated; 2 'BILD FOLGT' placeholders → no photo); no price/EAN published → none; +1 followfood Piccoli Tomate & Mozzarella 270 g from denns-biomarkt.at 'Neu im Sortiment' (AT, Regalpreis 6,29 €, 1 kg = 23,22 €, official packshot vision-gated; no EAN/nutrition published). Excluded: 8 dennree Tütensuppen (dry mixes), sugo/brühe/canned sides. products 3641→3651, photos 3417→3425, nutrition +9, prices +1; rows also in data/supplemental (kept by export.py); evidence raw/denns_2026-10-16T2336.json (incl. denn's Linz bistro lunch menus, not products); food-connectors c2b408b
- `b17335b` 2026-10-16 23:24 — Daten-Squad T2307: companies revenue 32→37/148 via North Data public company pages (Jahres-/Konzernabschluss data points, uncensored, estimate=false, register court+number = row, LEI where present) — Zott SE & Co. KG Konzern 1,28 Mrd. € GJ 2025, Allos Hof-Manufaktur 101 Mio. € GJ 2025, followfood 67,4 Mio. € GJ 2025, Euryza 50,2 Mio. € GJ 2024, Kikkoman Trading Europe 188,7 Mio. € GJ 2024/25; employees 47/148 unchanged ('Mitarbeiter' premium-censored on every page); iglo GmbH rejected (unit-inconsistent series); 40 North Data requests ≥10 s apart, all HTTP 200, no 429/captcha; DE VIES check-status still Unavailable (5 DE UIDs unverified, legal entity 136/148). Photo tail: +6 vision-gated official BILLA packshots by exact-EAN BILLA search — Billa 804→807 (BILLA immer gut Miso Suppe, Tom Kha Gai Tofu, Tom Kha Gai Huhn), MPreis 374→377 (Njami Chicken Bowl Curry/Mexicana, Wagner Big Sensation Salami & BBQ), total 3411→3417/3641; 11 MPreis rows stay without photo (shop placeholder, no exact-EAN official packshot elsewhere); evidence raw/companies_northdata_2026-10-16T2307.json
- `0ef5ec1` 2026-10-16 22:47 — Daten-Squad T2238: +5 vision-gated producer/brand logos for the myProduct.at producers (T2139) — Rapunzel (Commons File:Rapunzel_Naturkost.svg, Public domain, unmodified SVG), ARCHE Naturküche (arche-naturkueche.de header PNG), EgeSun company logo (egesun.de; not mapped to brand Vegan Pete), Sanchon (petersilchen.de brand PNG), Petersilchen company logo; logo rows 299/284→304/289; rettergut.de robots disallow, derit.nl/bioart.at/perfectearth.eu robots.txt unreachable (not fetched); Zwergenwiese/Vegan Pete/Hartl's no own asset; evidence raw/logos_squad_2026-10-16T2238.json
- `ab418e2` 2026-10-16 22:14 — Daten-Squad T2203: companies employees 46→47/148, revenue 31→32/148 — Rapunzel Naturkost GmbH & Co. KG from its own press page (rapunzel.de/ueber-uns/presse: 'Mitarbeitende: ca. 530', 'Umsatz 2024: 232 Mio. € netto'); 7 other T2139 company sites probed, no published figures; evidence raw/companies_facts_2026-10-16T2203.json
- `0f8de56` 2026-10-16 22:11 — Daten-Squad T2203: Hofer photo tail via Open Food Facts by exact EAN — +3 vision-gated front packshots (Good Choice Chicken Burger 300 g, Good Choice Schwammerlsauce mit Serviettenknödeln 380 g, Original Greisinger Berner Würstel 400 g), Hofer photos 129→132/223, total 3408→3411/3641; 38 EAN candidates probed (Hofer 21, Lidl 12, Penny 5): 32 have no image on OFF, 3 rejected (unpacked pizza, back label, lid label); Lidl 25/37 and Penny 24/29 unchanged; DE VIES re-run for 5 DE UIDs (ARCHE, Ökoland Nord, Rapunzel, EgeSun, Petersilchen) still MS_UNAVAILABLE (check-status DE Unavailable) → not verified, legal entity stays 136/148, UID 94/148 (VIES-verified unchanged)
- `2982232` 2026-10-16 21:49 — Daten-Squad T2139: +10 companies behind the myProduct.at ready meals (T2111) — Hartl's Kulinarikum Linz (sole trader, Impressum), Danke Bauer = Roman Fenz e.U. (LEI+FN 368109m+VIES), BioArt AG (LEI+FN 306867a+VIES), ARCHE Naturprodukte (LEI, HRB 85754), Ökoland GmbH Nord (LEI, HRB 201209), Rapunzel Naturkost GmbH & Co. KG (LEI, HRA 14236; +Zwergenwiese), EgeSun GmbH & Co. KG (LEI, HRA 205719; Vegan Pete), Petersilchen GmbH (HRB 11924, Impressum only), Schenkel Erich GmbH (label only, unidentified), myProduct GmbH retailer (FN 431059k, VIES, owners evi.gv.at); companies 138→148, legal entity identified 129→137/148; DE VIES MS_UNAVAILABLE → DE UIDs recorded, not counted; + vision-gated myProduct.at store logo (theme SVG = MageSuite placeholder rejected); logo rows 298/283→299/284

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
