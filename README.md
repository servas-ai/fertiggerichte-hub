# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-24 20:58 UTC via `./run_all.sh` (stündlich).

**Connectors:** 33 ✅ / 8 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3664

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 17 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 17 | 0 | 0 |
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
| ✅ | `adamah` | Online: ADAMAH BioHof | 3 | 2.86 s | [Rindsgulasch im Weckglas](https://www.adamah.at/Produktdetailseite/RindsgulaschimWeckglas_42093) · 11.9 € | 2026-10-24T20:50:14Z |
| ✅ | `alfies` | Alfies | 3 | 7.2 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g-1) · 4.49 € | 2026-10-24T20:50:17Z |
| ✅ | `bauernladen` | Online: Bauernladen.at | 3 | 8.37 s | [Gulaschsuppe](https://bauernladen.at/produkte/fairkocht/gulaschsuppe-27262) · 15.5 € | 2026-10-24T20:50:25Z |
| ✅ | `billa` | BILLA | 3 | 1.29 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-24T20:50:33Z |
| ✅ | `biohof-achleitner` | Online: Biohof Achleitner | 3 | 4.65 s | [Hausg'mocht Rindsgulasch](https://www.biohof.at/Hausgmocht-Rindsgulasch-4755) · 8.7 € | 2026-10-24T20:50:35Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 8.67 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-24T20:50:40Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 3.88 s | [NaBio Bio-Eintopf oder -Suppe](https://www.denns-biomarkt.at/angebote/) · 2.49 € | 2026-10-24T20:50:49Z |
| ✅ | `dm` | dm | 3 | 4.52 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-24T20:50:53Z |
| ✅ | `draxler` | Online: Draxler Geflügel-Wild | 3 | 4.47 s | [Rehragout](https://www.xn--geflgel-draxler-2vb.at/produkt/rehragout/) · 10.0 € | 2026-10-24T20:50:58Z |
| ✅ | `every` | Online: every. | 3 | 16.67 s | [Turkish Lentil Soup](https://every-foods.com/products/turkish-lentil-soup) · 8.99 € | 2026-10-24T20:51:03Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 9.03 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-24T20:51:19Z |
| ✅ | `gerbl` | Online: Gerbl im Glas | 3 | 24.09 s | [Gulaschsuppe](https://shop.gerbl.at/ecommerce/product?product_id=796882&category_id=150129) · 9.0 € | 2026-10-24T20:51:29Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.53 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-24T20:51:53Z |
| ✅ | `gourmet-daheim` | Online: GOURMET Daheim (Mahlzeit Linz) | 3 | 12.64 s | [Kartoffelgulasch mit Waldviertler Wurst](https://www.mahlzeit.co.at/wp-content/uploads/2026/03/Preisliste_Bestellschein_GDH_2026_inkl_MwSt_Mahlzeit_web.pdf) · 8.5 € | 2026-10-24T20:51:59Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.36 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-24T20:52:11Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.4 s | [Gissinger Rindsgulasch](https://www.gurkerl.at/21861-gissinger-rindsgulasch) · 12.77 € | 2026-10-24T20:52:20Z |
| ✅ | `hofer-shop` | HOFER | 2 | 3.69 s | [Sonnhof Rindsgulasch](https://www.hofer.at/produkt/sonnhof-rindsgulasch-000000000000510738) · 9.49 € | 2026-10-24T20:52:23Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 27.24 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-10-24T20:52:27Z |
| ✅ | `juit` | Online: Juit | 1 | 1.86 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-24T20:52:54Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 18.96 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-24T20:52:56Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.54 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-24T20:53:28Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 3.11 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-24T20:53:31Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 6.46 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 0.69 € | 2026-10-24T20:53:35Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 29.22 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-10-24T20:53:42Z |
| ✅ | `nah-frisch` | Nah&Frisch | 2 | 176.39 s | [Knorr . Bitte zu Tisch Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-24T20:54:11Z |
| ✅ | `penny` | PENNY | 3 | 6.19 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-24T20:57:08Z |
| ✅ | `penny-shop` | PENNY | 3 | 8.42 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-24T20:57:15Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 8.98 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-24T20:57:23Z |
| ✅ | `ruckzuck` | Online: Ruck Zuck Laden (Dunzinger's) | 3 | 20.36 s | [Gulaschsaft](https://www.ruckzuck-laden.at/shop/Gulaschsaft-p731601508) · 6.4 € | 2026-10-24T20:57:32Z |
| ✅ | `spar-shop` | SPAR/INTERSPAR | 3 | 1.77 s | [TANN Rinds-Bratengulasch](https://www.interspar.at/shop/lebensmittel/tann-rinds-bratengulasch/p/835817) · 21.99 € | 2026-10-24T20:57:53Z |
| ✅ | `sperchenedergut` | Online: Sperchenedergut | 1 | 22.98 s | [Gulaschsuppe vom Bio-Angusrind](https://sperchenedergut.at/produkt/gulaschsuppe-vom-angusrind/) · 9.5 € | 2026-10-24T20:57:55Z |
| ✅ | `subway-at` | Subway | 3 | 33.54 s | [Italian B.M.T.®](https://www.subway.com/de-AT/MenuNutrition/Menu/Product?ProductId=5257&MenuCategoryId=238) | 2026-10-24T20:58:18Z |
| ✅ | `wagyuhof` | Online: Wagyuhof | 1 | 2.29 s | [Wagyu Gulasch](https://wagyuhof.com/products/wagyu-gulasch) · 13.2 € | 2026-10-24T20:58:53Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-24T20:50:17Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-24T20:50:35Z |
| ❌ | `dm-heisse` | dm | 0 | 0.58 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:50:57Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-24T20:51:29Z |
| ❌ | `heisse-preise` | heisse-preise.io | 0 | 0.49 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:52:21Z |
| ❌ | `hofer` | HOFER | 0 | 0.64 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:52:22Z |
| ❌ | `lidl` | Lidl | 0 | 12.12 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-24T20:53:15Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-24T20:53:28Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-24T20:53:34Z |
| ❌ | `mpreis` | MPREIS | 0 | 0.43 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:53:35Z |
| ❌ | `off` | Open Food Facts | 0 | 0.45 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-10-24T20:57:08Z |
| ❌ | `spar` | SPAR/INTERSPAR | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:57:53Z |
| ❌ | `unimarkt` | Unimarkt | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-24T20:58:52Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-24T20:58:52Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-24T20:58:55Z |

### Bekannte Ausfälle (manuell gepflegt)

- `off` (Open Food Facts) ❌ seit 2026-10-16 (Hub-Lauf 22:59 UTC) dauerhaft, nicht mehr nur Upstream-503: OFF `robots.txt` verbietet für `User-agent: *` jetzt `/api`, `/cgi` und `/facets`, und der neue harte robots.txt-Gate in food-connectors (`0eaa455`) blockiert `cgi/search.pl` (Suche) und `api/v2/product` (EAN-Lookup) bewusst vor dem Request. `search.openfoodfacts.org` ist ebenfalls `Disallow: /`. Fix-Pfad (offen, food-connectors `adapters/off.py`): EAN-Lookup über die erlaubte Produktseite `/product/<ean>` (HTML), Suche über Open Prices / Datensatz-Dump statt Live-Suche. Kein Bypass des Gates.
- `lidl` ❌ HTTP 401 (bekannt, Lidl-API verlangt Auth; kein Login erlaubt).
- `heisse-preise`, `dm-heisse`, `hofer`, `mpreis`, `spar`, `unimarkt` ❌ seit Hub-Lauf 2026-10-17 20:07 UTC: Upstream-Ausfall bei heisse-preise.io. `https://heisse-preise.io/robots.txt` liefert HTTP 500 (nginx), und der robots.txt-Gate in food-connectors (`food_connectors/polite.py`) behandelt 5xx gemäß RFC 9309 korrekt als „alles verboten“, darum wird `data/latest-canonical.json` vor dem Request geblockt. Kein Code-Fehler, kein Bypass; erholt sich automatisch, sobald robots.txt wieder 200/4xx liefert.

## Datensatz

**3664 Produkte** · Tabellen: brand_tree 8, companies 162, establishments 4706, logos 318, nutrition 2825, online_mealprep 406, online_providers 3, prices 3270, producer_quality 4, producers 22, products 3664, stores 498

| Abdeckung | % |
|---|---|
| nutrition | 77.1 |
| price | 89.2 |
| photo | 94.5 |
| producer | 48.4 |
| brand | 90.9 |
| logos_total | 318 |

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|
| Billa | 807 |
| Spar | 735 |
| Gurkerl | 536 |
| MPreis | 388 |
| Hofer | 231 |
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
| Fit to Go | 32 |
| Penny | 29 |
| Unimarkt | 29 |
| FitTaste | 18 |
| Denn's | 15 |
| Nah&Frisch | 10 |
| LiveFresh | 10 |

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|
| Unklar (keine Lagerangabe) | 1223 |
| Tiefkühl (TK) | 1020 |
| Kühlregal (Menüschale/frisch) | 603 |
| Dose/Konserve | 422 |
| Trocken/Instant | 337 |
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
| Fertiggerichte filtern | <img src="screenshots/vergleich/tabelle_1920.png" width="420"> | <img src="screenshots/vergleich/tabelle_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich/plan_1920.png" width="420"> | <img src="screenshots/vergleich/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich/ki_1920.png" width="420"> | <img src="screenshots/vergleich/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich/hofer-top30_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich/gerichte_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich/marken_1920.png" width="420"> | <img src="screenshots/vergleich/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich/familien_1920.png" width="420"> | <img src="screenshots/vergleich/familien_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich/qualitaet_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich/filialen_1920.png" width="420"> | <img src="screenshots/vergleich/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich/online_1920.png" width="420"> | <img src="screenshots/vergleich/online_390.png" width="140"> |
| Multipot-Pro Garzeiten | <img src="screenshots/vergleich/multipot_1920.png" width="420"> | <img src="screenshots/vergleich/multipot_390.png" width="140"> |

### Fertiggerichte-Vergleich (servas-ai Pages)

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich-servas/home_1920.png" width="420"> | <img src="screenshots/vergleich-servas/home_390.png" width="140"> |
| Was kaufe ich heute? | <img src="screenshots/vergleich-servas/heute_1920.png" width="420"> | <img src="screenshots/vergleich-servas/heute_390.png" width="140"> |
| Fertiggerichte filtern | <img src="screenshots/vergleich-servas/tabelle_1920.png" width="420"> | <img src="screenshots/vergleich-servas/tabelle_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich-servas/plan_1920.png" width="420"> | <img src="screenshots/vergleich-servas/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich-servas/ki_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich-servas/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hofer-top30_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich-servas/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gerichte_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich-servas/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich-servas/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich-servas/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich-servas/marken_1920.png" width="420"> | <img src="screenshots/vergleich-servas/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich-servas/familien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/familien_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich-servas/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich-servas/qualitaet_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich-servas/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich-servas/filialen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich-servas/online_1920.png" width="420"> | <img src="screenshots/vergleich-servas/online_390.png" width="140"> |
| Multipot-Pro Garzeiten | <img src="screenshots/vergleich-servas/multipot_1920.png" width="420"> | <img src="screenshots/vergleich-servas/multipot_390.png" width="140"> |

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

- `ebc814d` 2026-10-24 20:27 — data+app: Sensecheck 53 P1 - #2851 sold-out fields (no stale PLI 50 badge), isRankable excludes sold_out rows client-side (pipeline fertig c4c1971): rows 4049, rankable 158, dataVersion ddd0a39a9ce1 -> ce8d8d111664
- `27cc458` 2026-10-24 20:10 — data: Sensecheck 52 P2-P4 - topLight rebuilt via _collapse (refills to 30), PrepMyMeal dupOf #2859->#2854, #2822->#2821, legacy #1534/#1535/#1536 -> current rows, MPreis #1770->#1769 Cevapcici (alsoAt Billa) (pipeline fertig 8876a1a): rows 4049, rankable 159 -> 158, top lists unchanged, dataVersion ccb1d68ff387 -> ddd0a39a9ce1
- `3288277` 2026-10-24 19:58 — data: Sensecheck 52 P1 fresh availability snapshot 2026-10-24 - #2851 PrepMyMeal Noodles Asian Style sold out, #2783 Chicken Teriyaki XL into topPLI, #2824 into topPE (pipeline fertig 868490a): rows 4049, rankable 160 -> 159, dataVersion e110ef577376 -> ccb1d68ff387
- `6998910` 2026-10-24 19:36 — data: Sensecheck 51 shipBox = 6 default - ship-box providers (PrepMyMeal) max 6 per top list, topPLI/topHealth/topPE stay at 30 (pipeline fertig 5dbaf40): rows 4049, rankable 160, dataVersion d79e6d508db1 -> e110ef577376
- `2484311` 2026-10-18 17:09 — data: Sensecheck 48 nutrition gap - Dean & David Teriyaki / Black Rice Protein Chicken Bowl (#2753, #2756) and Cevapcici #455 get the shop.billa.at label (pipeline fertig 55e89ee, local): rows 4049, dataVersion b6c978af0ace -> d79e6d508db1
- `4adce47` 2026-10-18 16:46 — data: Sensecheck 48 BILLA Kärntner Kasnudeln #558 satfat 2.0 -> 0.3 g/100 g (label; parser took the polyunsaturated line) (pipeline fertig ef98bf0, local): rows 4049, dataVersion 8e64539828f6 -> b6c978af0ace
- `5f30193` 2026-10-18 16:35 — data: Sensecheck 48 MPreis Käsnudeln #2774 <-> BILLA Kasnudeln #558 linked as same product (alsoAt both ways), #2774 label portion 200 g (pipeline fertig 51c450f, local): rows 4049, dataVersion 07bd2e089c23 -> 8e64539828f6
- `33b9df8` 2026-10-18 16:30 — data: online availability snapshot refreshed 2026-10-18T16:28:44Z (pipeline fertig a9d38f1, local): rows 4049, dataVersion 65ba832648f7 -> 07bd2e089c23

**servas-ai/food-connectors**

- `187aeb1` 2026-10-24 19:10 — draxler: new live connector — Draxler Geflügel-Wild 'Kulinarik im Glas' (Draxler Geflügel-Wild GmbH, Mooskirchen Stmk, FN 214255g, ATU52668607 VIES valid, LEI 894500FBIXCSSEWGP628 lapsed): public WooCommerce Store API → 9 chilled 360 g heat-up jar meals 6,90–10,00 € (Rehragout, Gulasch vom Wild, Wildfleisch Chili, Maishendl Curry/Gulasch/Suppe/Einmachsuppe, vegetarisches Gulasch, veganes Chili sin Carne) with SKU, stock, ingredients, photos; product-page fallback for a wrong API description; excludes clear broth, Genusspaket bundle, Gutschein; Post NEXT DAY FRESH within AT; no nutrition/GTIN published; CLI + MCP draxler_product/draxler_search; +3 offline tests
- `a4e52eb` 2026-10-24 18:39 — wagyuhof: new live connector — Wagyuhof Frischglas (Wagyuhof GmbH, Haag NÖ, FN 478220s, ATU72584759 VIES valid, LEI 98450053J99E55F43D03): public Shopify storefront collection 'frischglas' + product pages → 4 shelf-stable 300 g Wagyu jar meals (Gulasch, Ragout, Beuschel 13,20 €; Rouladen 14,90 € sold out) with nutrition per 100 g, ingredients, availability, packshots; excludes Sugo/Jus/Rindsuppe, 3+1 packs and boxes; ships AT+DE (14,90/9,90 €, free from 150 €); no GTIN; CLI + MCP wagyuhof_product/wagyuhof_search; +4 offline tests
- `761b841` 2026-10-24 17:38 — sperchenedergut: README CLI usage
- `2f7bb2d` 2026-10-24 17:38 — sperchenedergut: new live connector — Bio-Angus farm Sperchenedergut (Monika und Karl Mayer, Aspach OÖ, ATU76061208 VIES valid): public WooCommerce Store API → 3 heat-up jar meals 330 ml at 9,50 € incl. MwSt. (Gulaschsuppe, Beuschel, Chili con Carne) with stock + jar packshots; excludes Rinderfond/Bolognese sauce/Leberknödel and Geschenkbox duplicates; Post-Kühlversand 9,90 €, free from 150 €; no nutrition/GTIN published; CLI + MCP sperchenedergut_product/sperchenedergut_search; +3 offline tests
- `24492f1` 2026-10-18 04:59 — bauernladen: new live connector — Bauernladen.at farm-direct marketplace (Fundula Medien GmbH, vormals MN Anzeigenservice GmbH, Wien, FN 304617t, ATU64133538 VIES valid), category 'Schnelle Küche': server-rendered listing → product JSON-LD (price incl. MwSt., availability, images, seller) + pack size + producer address + producer AT delivery terms + Bio/Vegan/Kühl flags; robots allow, polite 1 req/s; no GTIN, nutrition only as unreferenced free text (not mapped); CLI + MCP bauernladen_product/bauernladen_search; +5 offline tests (140 passed)
- `1b57e85` 2026-10-18 04:16 — ruckzuck: new live connector — Ruck Zuck Laden / Dunzinger's Ruck Zuck Glasl (ruckzuck-laden.at, Schimpl OG, Hirschbach im Mühlkreis OÖ, FN 306047w, ATU64017307 VIES valid): WP store sitemap → public Ecwid storefront JSON (same unauthenticated call as the shop widget; robots allow; polite 1 req/s); 7 shelf-stable jar meals 7,40–9,70 € incl. 10 % MwSt. with ingredients, capital-marked allergens, vegan flag, jar packshot with printed dish label (serving illustration only in extra); ships AT 15 € / free from 100 €; no GTIN/nutrition published; CLI + MCP ruckzuck_product/ruckzuck_search; +4 offline tests (135 passed)
- `5174ba5` 2026-10-18 02:44 — gerbl: new live connector — Gerbl im Glas (shop.gerbl.at, Fleischhauerei Gerbl GmbH, Vöcklamarkt OÖ): category page (product_id links + vanity slug /rindsgulasch) → product pages (price incl. MwSt., 450 ml jar, ingredients, allergens, shelf life, official jar photo; HEAD 404 on gallery files → GET-verified); 19 pasteurised jar meals shipped within AT incl. Linz (9,90 € EMS); no GTIN/nutrition published; CLI + MCP gerbl_product/gerbl_search; +4 offline tests (131 passed)
- `96b59f4` 2026-10-18 01:44 — fittogo: take the hero packshot (first <img> in the --photo frame) before og:image/png fallback — new pages have no og:image and the png fallback returned the cross-sell grid photo of another meal (30.png Thai Red Curry) for Cheesy Taco Bowl + Topfennockerl; 30 existing meals re-checked live, image unchanged; +1 offline test with fixture

**servas-ai/fertiggerichte-daten**

- `af80136` 2026-10-24 19:41 — GOURMET Daheim: Speisekarte 2026 photo map (127/141 dish pages), no per-dish linkable photo -> image_url unchanged (T1936)
- `0275fd5` 2026-10-24 19:11 — Daten-Squad T1904: new online store Draxler Geflügel-Wild 'Kulinarik im Glas' (Draxler Geflügel-Wild GmbH, Mooskirchen Stmk; FN 214255g evi eingetragen, ATU52668607 VIES valid, LEI 894500FBIXCSSEWGP628 lapsed): +9 chilled 360 g heat-up jar meals 6,90–10,00 € (Rehragout, Gulasch vom Wild, Wildfleisch Chili, Maishendl Curry/Gulasch/Suppe/Einmachsuppe, vegetarisches Gulasch, veganes Chili sin Carne) with ingredients and vision-gated packshots 9/9; no nutrition/GTIN published; ships within AT by Post NEXT DAY FRESH (fee only in checkout). Company +1 (162), vision-gated logo +1 (318, staged scripts/logo_work_T1904). Online meal-prep 727→736. validate.py OK
- `a711e18` 2026-10-24 18:40 — Daten-Squad T1833 fix: Wagyuhof fn as 'FN 478220s' (validate.py format); validate.py OK (0 errors)
- `c75731c` 2026-10-24 18:40 — Daten-Squad T1833: new online store Wagyuhof Frischglas (Wagyuhof GmbH, Haag NÖ; FN 478220s evi eingetragen, ATU72584759 VIES valid, LEI 98450053J99E55F43D03): +4 shelf-stable 300 g Wagyu jar meals (Gulasch, Ragout in Steinpilz-Rahmsoße, Beuschel 13,20 €; Rouladen 14,90 € ausverkauft) with full nutrition per 100 g (Atwater ok), vision-gated packshots 4/4, ships AT+DE (14,90 €/<30 €, 9,90 €, free from 150 €); no GTIN. Company +1 (161), vision-gated logo +1 (317, staged scripts/logo_work_T1833). Online meal-prep 723→727. validate.py OK
- `d18fa19` 2026-10-24 18:15 — Daten-Squad T1811: +3 Bauernladen.at-only Dunzinger's Ruck Zuck jar meals (Rehragout, Hirschragout vom heimischen Wild 370 g 9,50 €; BBQ Kokos Eintopf VEGAN 330 ml 8,40 €) not sold in the own shop ruckzuck-laden.at; no photo (shared Gulasch image / flyer composite → vision gate FAIL), no nutrition/GTIN; sitemap re-check of 14 254 Bauernladen offers found no further ready meals outside 'Schnelle Küche'. Online meal-prep 720→723. validate.py OK
- `d897e4e` 2026-10-24 17:39 — Sperchenedergut (Aspach OÖ): 3 Bio-Angus jar meals, company (UID ATU76061208 VIES valid), logo — online meal-prep 717→720
- `f83b7c8` 2026-10-24 17:06 — Daten-Squad T1703: +3 vision-gated producer logos for the Bauernladen.at producers — FAIRKOCHT (fairkocht.at header PNG, 19 meals), Christöphl Manufaktur (christoephl.at header SVG, 5), Genusss-Manufaktur Bruckner (nudelmanufaktur.at footer PNG, low-res, 2); logo rows 312→315; Hackl (hoster WAF block, not bypassed) and Venatio (no HTTP response) open. Files staged in scripts/logo_work_T1703. validate.py OK
- `01d312f` 2026-10-18 05:16 — Daten-Squad T0506: company rows for the Bauernladen.at producers (T0439 open item 2) — companies 154→159: +fairkocht gmbh FN 531976v/ATU75453279 (Andelsbuch, 19 meals), +Christöphl Manufaktur GmbH FN 414202x/ATU68596628 (Raaba-Grambach; 100 % parent MACH Genussprodukte GmbH FN 568278d), +"GENUSSS-MANUFAKTUR" Bruckner KG FN 428315a/ATU69302248 (Wien), +Hackls Happy Turkey GmbH FN 550716b/ATU76907224 (Atzelsdorf), +Venatio Wildspezialitäten (Einzelunternehmen lt. Impressum, no FN/UID → impressum-only); existing Roman Fenz e.U. (Danke Bauer) +chain Bauernladen.at, products 4→7. All FN from the producers' own Impressum, confirmed on evi.gv.at (status Eingetragen, Eintragungsdatum, Stammkapital, Geschäftszweig; natural-person shareholders counted not named) and VIES (valid, name+address match). No GLEIF records except Fenz. vom Sandriegel: no legal identity published → no row. online_mealprep: manufacturer field of 30 Bauernladen rows now carries legal name + FN. Evidence raw/companies_bauernladen_2026-10-18T0506.json. validate.py OK

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
