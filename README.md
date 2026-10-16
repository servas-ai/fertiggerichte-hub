# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-16 23:00 UTC via `./run_all.sh` (stündlich).

**Connectors:** 28 ✅ / 2 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3641

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
| ✅ | `alfies` | Alfies | 3 | 8.8 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g) · 4.49 € | 2026-10-16T22:51:52Z |
| ✅ | `billa` | BILLA | 3 | 1.48 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-16T22:52:01Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 8.87 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-16T22:52:03Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 4.96 s | [MyDeli Bio-Fleischsuppe](https://www.denns-biomarkt.at/angebote/) · 3.49 € | 2026-10-16T22:52:12Z |
| ✅ | `dm` | dm | 3 | 4.41 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-16T22:52:17Z |
| ✅ | `dm-heisse` | dm | 3 | 3.38 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-16T22:52:21Z |
| ✅ | `every` | Online: every. | 3 | 15.56 s | [Pumpkin Zucchini Risotto](https://every-foods.com/products/pumpkin-zucchini-risotto) · 8.99 € | 2026-10-16T22:52:26Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 8.73 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-16T22:52:42Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.49 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-16T22:52:51Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.16 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-16T22:52:57Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.38 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 19.22 € | 2026-10-16T22:53:05Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 2.88 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-16T22:53:07Z |
| ✅ | `hofer` | HOFER | 3 | 2.67 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-16T22:53:10Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 31.87 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-10-16T22:53:14Z |
| ✅ | `juit` | Online: Juit | 1 | 1.81 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-16T22:53:46Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 38.79 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-16T22:53:48Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.23 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-16T22:54:40Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 3.85 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-16T22:54:42Z |
| ✅ | `mpreis` | MPREIS | 3 | 3.85 s | AIA Puten Gulasch · 6.5 € | 2026-10-16T22:54:46Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 9.71 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-10-16T22:54:51Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 28.22 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-10-16T22:55:01Z |
| ✅ | `nah-frisch` | Nah&Frisch | 3 | 243.21 s | [Inzersdorfer Fertiggerichte oder Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-16T22:55:30Z |
| ✅ | `penny` | PENNY | 3 | 5.8 s | [Rindsgulaschfleisch](https://www.penny.at/produkte/rindsgulaschfleisch-78544603) · 15.99 € | 2026-10-16T22:59:34Z |
| ✅ | `penny-shop` | PENNY | 3 | 9.41 s | [Rindsgulaschfleisch](https://www.penny.at/produkte/rindsgulaschfleisch-78544603) · 15.99 € | 2026-10-16T22:59:40Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 9.56 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-16T22:59:50Z |
| ✅ | `spar` | SPAR/INTERSPAR | 3 | 3.32 s | Baron de Sel Gourmet Gulasch Bio 55g · 4.99 € | 2026-10-16T22:59:59Z |
| ✅ | `spar-shop` | SPAR/INTERSPAR | 3 | 1.7 s | [TANN Rinds-Bratengulasch](https://www.interspar.at/shop/lebensmittel/tann-rinds-bratengulasch/p/835817) · 21.99 € | 2026-10-16T23:00:04Z |
| ✅ | `unimarkt` | Unimarkt | 3 | 2.73 s | [Felix Erdäpfelgulasch](/Felix-Erdaepfelgulasch-3692) · 5.39 € | 2026-10-16T23:00:06Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-16T22:51:52Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-16T22:52:03Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-16T22:52:51Z |
| ❌ | `lidl` | Lidl | 0 | 12.4 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-16T22:54:27Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-16T22:54:40Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-16T22:54:46Z |
| ❌ | `off` | Open Food Facts | 0 | 0.74 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-10-16T22:59:33Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-16T23:00:10Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-16T23:00:10Z |

## Datensatz

**3641 Produkte** · Tabellen: brand_tree 8, companies 148, establishments 4706, logos 304, nutrition 2811, online_mealprep 406, online_providers 3, prices 3259, producer_quality 4, producers 22, products 3641, stores 498

| Abdeckung | % |
|---|---|
| nutrition | 77.2 |
| price | 89.5 |
| photo | 93.7 |
| producer | 48.4 |
| brand | 90.9 |
| logos_total | 304 |

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|
| Billa | 807 |
| Spar | 735 |
| Gurkerl | 536 |
| MPreis | 388 |
| Hofer | 223 |
| Alfies | 182 |
| bofrost | 144 |
| unbekannt (OFF) | 93 |
| HelloFresh | 93 |
| PrepMyMeal | 92 |
| Subway | 59 |
| Juit | 50 |
| NORDSEE | 39 |
| Lidl | 37 |
| dm | 35 |
| Fit to Go | 30 |
| Penny | 29 |
| Unimarkt | 29 |
| FitTaste | 18 |
| LiveFresh | 10 |
| Nah&Frisch | 7 |
| Denn's | 5 |

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|
| Unklar (keine Lagerangabe) | 1222 |
| Tiefkühl (TK) | 1009 |
| Kühlregal (Menüschale/frisch) | 597 |
| Dose/Konserve | 422 |
| Trocken/Instant | 332 |
| Glas | 34 |
| Sous-vide (vakuum) | 14 |
| Beutel ungekühlt (Retort-Pouch) | 11 |

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

- `b0eab37` 2026-10-16 22:30 — data: hourly T22 — new online store myProduct.at (+37 heat-up meals/soups from regional producers: Little Lunch 9, Danke Bauer 4, Goldblatt 4, Followfood 4, Rettergut 3, Perfect Earth 3, Hartls Kulinarikum Linz 2, Ökoland 2, Zwergenwiese 2 …), delivers_4020 true (myproduct.at/lieferung, 7,90 €/10 kg AT). Nutrition: 11 myproduct.at, 6 identical EAN in dataset, 20 Open Food Facts product page by exact EAN; never estimated (27 without nutrition kept out). Multipacks priced per pack, portion = unit glass (multipack_unit). Pipeline fertig bd00502. rows 3885→3921, rankable 211. Gates: prepush_gate.sh OK (build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10814 broken images, gaps applied, top50 regress 0), pipeline pytest 114/114. No deploy.
- `bf14026` 2026-10-16 22:18 — data: iglo Genießer-Pfanne per-portion fix (pipeline fertig a7dc722/b679a46): 650 g packs = 2 portions per iglo.at 'Pro Portion' (≈325 g; Tagliatelle Funghi/Ravioli 600 g → 300 g), incl. SPAR 'Iglo Französische Art Penne…' + MPreis 'Französische Pfanne' — 22 rows: portion 650→325, price/portion 7.69→3.85 €, kcal/portion halved (Billa Tortellini 656→328). Billa Tortellini/Französische Art/Paprika-Huhn + Spar Französische Art now light_meal (own ranking) → rankable 215→211, light pool 106→110; topPLI/topPE/topHealth/topLight unchanged. rows 3885. Sensecheck 18 re-verified on 64f6970: all points closed (Kernbeißer source = kernbeisser.at/agbs/ §7, no dedicated shipping page per sitemap; 0 rankable rows with delivers_4020 null/false). Gates: prepush_gate.sh OK (build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10698 broken images, gaps applied, top50 regress 0), pipeline pytest 111/111. No deploy.
- `64f6970` 2026-10-16 22:01 — Merge remote-tracking branch 'origin/main' into HEAD
- `8986842` 2026-10-16 22:01 — publish_only.sh: disk gate - abort before worktree/build if / or /tmp has < MIN_DISK_GB (default 3) GB free
- `d2bc354` 2026-10-16 21:56 — data: merge hourly T21 (+9 SPAR heat-up rows) + 9 verified rows from the 21:11 run; +15 bofrost* rows (bofrost.at verified); every. Mushroom Gnocchi vegan; SPAR Tradizionale Diavola without the wrong Ristorante twin nutrition. rows 3885, rankable 215. Pipeline fertig 130350a. pytest 98/98, top50 ok, regress ok, gaps_overlay applied. No deploy.
- `00e9135` 2026-10-16 21:53 — MealKits: per-box delivery text from delivers_4020/delivery_note (false → note or 'Liefert nicht nach 4020 Linz', true → 'Online / Lieferung', null/undefined → grey 'Lieferung nach 4020 nicht geprüft'), tooltip via deliveryTitle
- `103cd4b` 2026-10-16 21:51 — data: hourly T21 (pipeline fertig ea43768, branch hourly-T21 on 1dbcc57) — +9 SPAR heat-up rows with verified nutrition (6 strict BILLA twins: Schär Pizza Margherita glutenfrei, Knorr Meisterkessel XL Serbische Bohnensuppe/Leberknödelsuppe replacing nutrition-less SPAR rows, Inzersdorfer Rahmschnitzerl mit Spiralen, Iglo Kürbis + Quinoa, Iglo Broccoli-Laibchen; 3 via Open Food Facts: DESPAR Pizza Margherita 423 g, Little Lunch Pasta Napoli/Volognese); brand_families regenerated (761→762). rows 3853→3860, rankable 214→215. Gates: build ok, Playwright 32 tabs×1920/390 0 errors/0 blank/0 overflow, 0/10662 broken images, gaps applied, top50 regress 0, pytest 98/98. No deploy.
- `1ec81be` 2026-10-16 21:25 — chore: ignore .gate_rows (prepush_gate.sh row-count state, as its comment asks) so deploy.sh's 'git add -A' never commits it

**servas-ai/food-connectors**

- `0eaa455` 2026-10-16 22:02 — polite: hard robots.txt gate + 1 s/host for every HTTP path. RobotsDisallowed raised before the request (cached per host, UA group + '*', RFC 9309: robots 4xx = allow, 5xx/unreachable = disallow); http.get and the 4 direct urlopen sites (alfies, osm_stores, issmich, company/registries) use polite_urlopen; package import installs the gate for urllib/requests/httpx/curl subprocess. tests/test_polite.py (interspar product page blocked without network call, allowed URL, UA group, 4xx/5xx/unreachable, rate limit, install routing). pytest 98 passed, 3 skipped.
- `32c9237` 2026-10-16 21:26 — Daten-Squad T2111: new live connector myproduct (myproduct.at regional-producer marketplace, category Fertiggerichte): category dataLayer + product JSON-LD Offer + Magento attribute table (EAN check digit, Nettofüllmenge, producer address, ingredients, allergens, MHD, nutrition per 100 g when published, Atwater check); exclusion rules for fonds/sauces/spreads/dry mixes/soup powders/meat-substitute raw goods; CLI food fetch|search --store myproduct, MCP myproduct_product/myproduct_search; 5 offline fixture tests
- `a00ce43` 2026-10-16 20:48 — Daten-Squad T2038: new live connector open-prices (Open Food Facts Open Prices REST API, ODbL): food prices EAN [--country AT --since], MCP open_prices_lookup, datasets catalog entry; 2 offline fixture tests (suite 82 passed / 3 skipped)
- `ac16ed7` 2026-10-16 19:53 — bofrost: starters += Pizzettis, Rösti-Baguette, Gemüse-/Broccoli-Laibchen, Schinken-Käse-Röllchen (warm baked snacks; breaded cheese stays out); ready-meals DISH_SLUG += schlemmerfilet; tests
- `994f35c` 2026-10-16 18:33 — bofrost: opt-in course fetches — fetch(category="desserts") warm Mehlspeisen (Knödel, Kaiserschmarrn, Topfennockerl, Mohnnudeln, Strudel, Palatschinken; no Torten/Eis/raw dough) and fetch(category="starters") warm Vorspeisen (Frühlingsrollen, Teigtaschen, Flammkuchen, Kaspressknödel); extra.course; default ready-meal filter unchanged; test_course_url_filters
- `8777b7a` 2026-10-14 07:30 — Daten-Squad T0740: new live connector alfies (Alfies Wien/Graz online supermarket, Alfie's GmbH, Wien)
- `9650f94` 2026-10-14 06:57 — Daten-Squad T0636: new live connector issmich (iss mich! Wiener Bio-Eintöpfe & Suppen im WECK-Glas, iss mich! GmbH, Wien)
- `cf54f79` 2026-10-14 06:08 — Daten-Squad T0605: new live connector goldblatt (Goldblatt High Protein Bio glass-jar ready meals, Golden Veggies GmbH, Bad Waltersdorf)

**servas-ai/fertiggerichte-daten**

- `0ef5ec1` 2026-10-16 22:47 — Daten-Squad T2238: +5 vision-gated producer/brand logos for the myProduct.at producers (T2139) — Rapunzel (Commons File:Rapunzel_Naturkost.svg, Public domain, unmodified SVG), ARCHE Naturküche (arche-naturkueche.de header PNG), EgeSun company logo (egesun.de; not mapped to brand Vegan Pete), Sanchon (petersilchen.de brand PNG), Petersilchen company logo; logo rows 299/284→304/289; rettergut.de robots disallow, derit.nl/bioart.at/perfectearth.eu robots.txt unreachable (not fetched); Zwergenwiese/Vegan Pete/Hartl's no own asset; evidence raw/logos_squad_2026-10-16T2238.json
- `ab418e2` 2026-10-16 22:14 — Daten-Squad T2203: companies employees 46→47/148, revenue 31→32/148 — Rapunzel Naturkost GmbH & Co. KG from its own press page (rapunzel.de/ueber-uns/presse: 'Mitarbeitende: ca. 530', 'Umsatz 2024: 232 Mio. € netto'); 7 other T2139 company sites probed, no published figures; evidence raw/companies_facts_2026-10-16T2203.json
- `0f8de56` 2026-10-16 22:11 — Daten-Squad T2203: Hofer photo tail via Open Food Facts by exact EAN — +3 vision-gated front packshots (Good Choice Chicken Burger 300 g, Good Choice Schwammerlsauce mit Serviettenknödeln 380 g, Original Greisinger Berner Würstel 400 g), Hofer photos 129→132/223, total 3408→3411/3641; 38 EAN candidates probed (Hofer 21, Lidl 12, Penny 5): 32 have no image on OFF, 3 rejected (unpacked pizza, back label, lid label); Lidl 25/37 and Penny 24/29 unchanged; DE VIES re-run for 5 DE UIDs (ARCHE, Ökoland Nord, Rapunzel, EgeSun, Petersilchen) still MS_UNAVAILABLE (check-status DE Unavailable) → not verified, legal entity stays 136/148, UID 94/148 (VIES-verified unchanged)
- `2982232` 2026-10-16 21:49 — Daten-Squad T2139: +10 companies behind the myProduct.at ready meals (T2111) — Hartl's Kulinarikum Linz (sole trader, Impressum), Danke Bauer = Roman Fenz e.U. (LEI+FN 368109m+VIES), BioArt AG (LEI+FN 306867a+VIES), ARCHE Naturprodukte (LEI, HRB 85754), Ökoland GmbH Nord (LEI, HRB 201209), Rapunzel Naturkost GmbH & Co. KG (LEI, HRA 14236; +Zwergenwiese), EgeSun GmbH & Co. KG (LEI, HRA 205719; Vegan Pete), Petersilchen GmbH (HRB 11924, Impressum only), Schenkel Erich GmbH (label only, unidentified), myProduct GmbH retailer (FN 431059k, VIES, owners evi.gv.at); companies 138→148, legal entity identified 129→137/148; DE VIES MS_UNAVAILABLE → DE UIDs recorded, not counted; + vision-gated myProduct.at store logo (theme SVG = MageSuite placeholder rejected); logo rows 298/283→299/284
- `5a788a0` 2026-10-16 21:26 — Daten-Squad T2111: new online store myProduct (myproduct.at, myProduct GmbH Zwettl, FN 431059k, ATU69436808 VIES valid) — 64 Fertiggerichte/Suppen regionaler Produzenten from 218 category items (Hartls Kulinarikum Linz 19, Little Lunch 9, Rettergut 5, Danke Bauer 4, Goldblatt 4, Bioart 3 …): price, EAN 63/64, Nettofüllmenge, producer address, ingredients, MHD, 64/64 HEAD-200 packshots; nutrition only where published (11, Atwater ok) — 53 rows nut_flag 'keine Nährwertangabe' (never estimated); 154 excluded with reason (fonds, sauces/Bolognese, spreads, dry mixes, soup powders, raw meat substitutes, Großgebinde); shipping 7,90 €/10 kg AT; online_mealprep 406→470; food-connectors 32c9237
- `e5e010f` 2026-10-16 20:49 — Daten-Squad T2038: Open Prices (Open Food Facts) probed for all 240 dataset EANs without a live 2026 price — 7 with any observation, 0 usable (AT hits are 2024/Jan-2025 Mödling receipts, Lidl hits are Berlin DE, 1 without location); no price changed; external_datasets +open-prices (11→12); evidence raw/open_prices_2026-10-16T2038.json
- `88c65f9` 2026-10-16 20:15 — Daten-Squad T1938: company employees 17→46/138, revenue 16→31/138, founded 88→106/138 (company-owned pages on the verified website: 27 employees, 12 revenue, 15 founded — e.g. FRoSTA AG IR key figures, Alnatura Daten & Fakten, Lidl/dm/Hofer/SPAR/REWE/PENNY own figures; de.wikipedia infobox of identifier-matched items: Rügenwalder Konzern 2023, Maresi; Wikidata P571 via P856: AIA 1968, Hamker 1907; Lidl founded via de.wikipedia; Hofer revenue from labelled Die Presse advertorial; every value re-fetched and phrase-verified, group/brand scope labelled; conflicts recorded not overwritten: followfood 2007 vs 2001, Revo 2020 vs 2021, efko 1976 vs 1973, NÖM 645 vs 534 Mio. both kept)
- `5bf43ba` 2026-10-16 19:18 — Daten-Squad T1907: record founded-source breakdown in evidence (GLEIF 45, Firmenbuch ≥1996 18, Wikidata 2; corrects 47/16 split in 200c17d message)

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
