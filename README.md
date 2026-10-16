# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-16 18:06 UTC via `./run_all.sh` (stündlich).

**Connectors:** 27 ✅ / 2 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3641

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 9 | 1 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 9 | 1 | 0 |
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
| ✅ | `alfies` | Alfies | 3 | 5.3 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g) · 4.49 € | 2026-10-16T17:58:59Z |
| ✅ | `billa` | BILLA | 3 | 0.47 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-16T17:59:04Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 6.4 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-16T17:59:05Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 3.97 s | [MyDeli Bio-Fleischsuppe](https://www.denns-biomarkt.at/angebote/) · 3.49 € | 2026-10-16T17:59:11Z |
| ✅ | `dm` | dm | 3 | 5.48 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-16T17:59:15Z |
| ✅ | `dm-heisse` | dm | 3 | 18.54 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-16T17:59:21Z |
| ✅ | `every` | Online: every. | 3 | 14.15 s | [Pumpkin Zucchini Risotto](https://every-foods.com/products/pumpkin-zucchini-risotto) · 8.99 € | 2026-10-16T17:59:41Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 5.07 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-16T17:59:55Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 4.16 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-16T18:00:00Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 3.18 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-16T18:00:04Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 0.39 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 19.22 € | 2026-10-16T18:00:08Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 3.07 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-16T18:00:08Z |
| ✅ | `hofer` | HOFER | 3 | 2.91 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-16T18:00:13Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 30.33 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-10-16T18:00:17Z |
| ✅ | `juit` | Online: Juit | 1 | 0.58 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-16T18:00:47Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 21.05 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-16T18:00:48Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 1.31 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-16T18:01:22Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 2.17 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-16T18:01:23Z |
| ✅ | `mpreis` | MPREIS | 3 | 3.37 s | AIA Puten Gulasch · 6.5 € | 2026-10-16T18:01:25Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 6.64 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-10-16T18:01:30Z |
| ✅ | `nah-frisch` | Nah&Frisch | 3 | 248.79 s | [Inzersdorfer Fertiggerichte oder Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-16T18:01:37Z |
| ✅ | `penny` | PENNY | 3 | 4.13 s | [Rindsgulaschfleisch](https://www.penny.at/produkte/rindsgulaschfleisch-78544603) · 15.99 € | 2026-10-16T18:05:58Z |
| ✅ | `penny-shop` | PENNY | 3 | 7.53 s | [Rindsgulaschfleisch](https://www.penny.at/produkte/rindsgulaschfleisch-78544603) · 15.99 € | 2026-10-16T18:06:02Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 6.58 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-16T18:06:09Z |
| ✅ | `spar` | SPAR/INTERSPAR | 3 | 3.51 s | Baron de Sel Gourmet Gulasch Bio 55g · 4.99 € | 2026-10-16T18:06:16Z |
| ✅ | `spar-shop` | SPAR/INTERSPAR | 3 | 0.5 s | [TANN Rinds-Bratengulasch](https://www.interspar.at/shop/lebensmittel/tann-rinds-bratengulasch/p/835817) · 21.99 € | 2026-10-16T18:06:21Z |
| ✅ | `unimarkt` | Unimarkt | 3 | 2.85 s | [Felix Erdäpfelgulasch](/Felix-Erdaepfelgulasch-3692) · 5.39 € | 2026-10-16T18:06:22Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-16T17:58:59Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-16T17:59:05Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-16T18:00:00Z |
| ❌ | `lidl` | Lidl | 0 | 12.14 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-16T18:01:09Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-16T18:01:21Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-16T18:01:25Z |
| ❌ | `off` | Open Food Facts | 0 | 11.82 s | `HTTPError: HTTP Error 503: Service Temporarily Unavailable` | 2026-10-16T18:05:46Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-16T18:06:26Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-16T18:06:26Z |

## Datensatz

**3641 Produkte** · Tabellen: brand_tree 8, companies 138, establishments 4706, logos 298, nutrition 2811, online_mealprep 406, online_providers 3, prices 3259, producer_quality 4, producers 22, products 3641, stores 498

| Abdeckung | % |
|---|---|
| nutrition | 77.2 |
| price | 89.5 |
| photo | 93.6 |
| producer | 48.4 |
| brand | 90.9 |
| logos_total | 298 |

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

- `44f4d16` 2026-10-16 17:56 — Merge remote-tracking branch 'origin/main' into feature/variant-cap
- `62d713f` 2026-10-16 17:56 — price_condition badge shows price_condition_info source (tooltip: host + checked date; https-only link)
- `4fcdce3` 2026-10-16 17:55 — data: sensecheck 14 — SPAR Natur*pur baby jars verified via SPAR category Baby/Menüs: Bio-Gemüse-Risotto 250 g and Mediterrane Bio-Kartoffelpfanne 220 g now baby_food (were ready_meal); Steinpilz-/Tomaten-Risotto 2,49 € stay non-baby. rows 3770, rankable 337. Pipeline fertig 0390483. pytest 73/73, top50 ok, regress ok, build ok. No deploy.
- `223f80e` 2026-10-16 17:53 — Merge remote-tracking branch 'origin/main' into feature/variant-cap
- `0f4f069` 2026-10-16 17:53 — variant_note under product name (cards, table, detail, Heute); price_condition badge next to price; 'ohne Limit' toggle (URL nolimit=1) switching top*/top*Uncapped and respecting topCap in Top lists + Heute; label 'Preis-Sieger, Gesundheit mittel' for medium-health price winners
- `67b4c00` 2026-10-16 17:51 — data: review 13 decisions — roasts with a named side are dishes (bofrost Surbraten mit Sauerkraut), sauce-only roasts stay components; Steinofenpizza price_condition_info (mpreis.at, checked 2026-10-16); store restored for 7 OFF rows matched via heisse-preise (Billa Thai Red Chicken Curry, Spar Kräftige Hühnersuppe …) lost in 6c11fb6. rows 3770, rankable 337. Pipeline fertig 6f75adb. pytest 70/70, top50 ok, regress ok. No deploy.
- `6c11fb6` 2026-10-16 17:45 — data: review 13 — meat/fish pieces without carb word (Rindsbackerl Sous Vide, Braten, Stelze, Iglo Goldschatz) are components, out of topLight; one variant per dish in top lists (variant_note), delivery shipping/6 in pli (shipPor/pPorEff, PrepMyMeal +1,00 €), max 10/30 per provider (+ top*Uncapped, topCap); SPAR Natur*pur jars baby_food (risotto excluded); Goldschatz portion 200 g; breaded += karaage/tempura/katsu; Steinofenpizza 710 g + price_condition. rows 3770, rankable 347→337. Pipeline fertig fc82d64. pytest 66/66, top50 ok, regress ok. No deploy.
- `80131d5` 2026-10-16 17:17 — data: sensecheck 13 — same shop URL with different pack size/price collapsed to one visible row (28 twins hidden via dupOf, e.g. BILLA Lasagne Bolognese 700 g/4,99 € out of topPE, live 400 g/3,19 € kept; Iglo Lasagne al Forno Billa 700 g kept per shop API); Iglo Polar-Dorsch Mediterrane/Serbische Art/Müllerin, Schlemmerfilet, Filegro, Ofenfisch and Planted 'Chicken Kräuter & Zitrone' are components ('Zum Kombinieren'), out of topHealth/topLight; Iglo 'Französische Art Penne, Gemüse & Hühnerfilet' and 'Faschierte Laibchen mit Püree' are meals again. rows 3766, rankable 353→347. Pipeline fertig e8bdca5. Gates: pytest 58/58, top50 ok, build ok. No deploy.

**servas-ai/food-connectors**

- `8777b7a` 2026-10-14 07:30 — Daten-Squad T0740: new live connector alfies (Alfies Wien/Graz online supermarket, Alfie's GmbH, Wien)
- `9650f94` 2026-10-14 06:57 — Daten-Squad T0636: new live connector issmich (iss mich! Wiener Bio-Eintöpfe & Suppen im WECK-Glas, iss mich! GmbH, Wien)
- `cf54f79` 2026-10-14 06:08 — Daten-Squad T0605: new live connector goldblatt (Goldblatt High Protein Bio glass-jar ready meals, Golden Veggies GmbH, Bad Waltersdorf)
- `6597c0d` 2026-10-14 05:08 — Daten-Squad T0504: new live connector kernbeisser (Kernbeißer vegan Vollkorn-Fertiggerichte im Glas, Wien)
- `241e063` 2026-10-14 04:52 — Daten-Squad T0441: new live connector loewenanteil (Löwenanteil Bio glass-jar ready meals)
- `bab2e1d` 2026-10-14 03:58 — feat(every): live every. (every-foods.com) connector — frozen plant-based ready meals shipped to AT (DPD per shop shipping policy, 5,99 €, free from 8 meals) via public Shopify storefront JSON eat.every-foods.com/products.json (price EUR, SKU, availability, packshots) + product pages (Storyblok product blok: weight, nutrition per 100 g + pack, ingredients, preparation; bilingual DE/EN table parser, pack-column typo flag); ready meals = product_type Meal, price > 0, in DE product sitemap; robots-allowed, no login/cookies, 1 req/s; no GTIN → ean None; MCP every_product + every_search; offline tests with fixture (2026-10-14T0341)
- `402f219` 2026-10-14 03:20 — feat(fittogo): live fit2go.meals connector (frozen ready meals, AT-wide Express 4,99 €) via public product sitemap + product HTML — Hydrogen shop (/products.json 404); pack nutrition + Einwaage → per 100 g; price_eur = published 12er-box 9,99 €/Meal (Einzel-SKU 0,00 €); MCP fittogo_product + fittogo_search; offline tests with fixture; Gourmetfein noted as Wurst-only ready-meal dead end (2026-10-14T0307)
- `c4418a1` 2026-10-14 03:01 — feat(bofrost): live bofrost* Austria connector (frozen ready meals, home delivery across AT) via public sitemap + product pages — schema.org JSON-LD price/availability/images, pack line with €/kg, nutrition per 100 g, ingredients, Nutri-Score badge; robots-allowed paths only, no login/cookies, 1 req/s; no GTIN published → ean None; MCP bofrost_product + bofrost_search; offline tests with fixture (2026-10-14T0238)

**servas-ai/fertiggerichte-daten**

- `2260dfc` 2026-10-16 17:43 — Daten-Squad T1736: drop unverified legal-name alias from the 11er logo row (only brand names kept)
- `686eab7` 2026-10-16 17:41 — Daten-Squad T1736: logo long tail — +4 vision-gated brand logos (11er/elfer 11er.at SVG, Ajinomoto Commons PD wordmark incl. 'Ajinomoto Oyakata' rows, getvoila getvoila.com SVG recoloured dark, Mamma Emma mammaemma.it SVG) + aliases Followfood/Frank Juice/Die Knödelwerkstatt onto existing file-backed rows; Followfish alias rejected (old wordmark); strict logo-less 61→54 brands / 100→75 products
- `37a4feb` 2026-10-16 17:17 — Daten-Squad T1706: Alfies restock — +4 ready meals restocked at T0809 (Feel Food Chili sin Carne, Followfood Pizza BIG Mediterrana, Humza Frühlingsrollen, Mama Noodles Beef; 182 kept); T1706 re-probe of all 5 warehouses: remaining 111 still out of stock everywhere 57 h later → treated as delisted
- `348294c` 2026-10-16 17:17 — Daten-Squad T1706: legal entity identified for Stadtküche (Knödelhütte GmbH FN 675365i, ATU83103945 VIES valid via kasnudl.at Impressum) and Unimarkt (GLEIF 529900X5GBP4KNVUYQ35, FN 25076b); Alimentastic GmbH legal name/address/court from Impressum (UID VIES-invalid, not marked verified); rejected 4 look-alike matches with evidence
- `83b291a` 2026-10-14 07:32 — Daten-Squad T0740: logo alias 'Every Foods' → every-foods (Alfies lists every. meals as 'Every Foods', 9 rows; existing vision-gated logo) + CRLF fix for the appended Alfie's GmbH companies.csv row
- `f688a37` 2026-10-14 07:30 — Daten-Squad T0740: new retail chain Alfies (Wiener Online-Supermarkt, Wien + Graz) — 178 ready meals with live price, nutrition, photo
- `701ffe6` 2026-10-14 07:04 — Daten-Squad T0636: new online provider iss mich! (35 Wiener Bio-Eintöpfe & Suppen im WECK-Pfandglas, iss mich! GmbH, Wien)
- `8a7c203` 2026-10-14 06:09 — Daten-Squad T0605: new online provider Goldblatt (8 High Protein Bio glass-jar ready meals, Bad Waltersdorf, AT)

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
