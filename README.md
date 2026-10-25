# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-25 05:03 UTC via `./run_all.sh` (stündlich).

**Connectors:** 45 ✅ / 9 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3664

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 20 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 20 | 0 | 0 |
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
| ✅ | `adamah` | Online: ADAMAH BioHof | 3 | 3.13 s | [Rindsgulasch im Weckglas](https://www.adamah.at/Produktdetailseite/RindsgulaschimWeckglas_42093) · 11.9 € | 2026-10-25T04:53:48Z |
| ✅ | `alfies` | Alfies | 3 | 6.89 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g-1) · 4.49 € | 2026-10-25T04:53:52Z |
| ✅ | `bauernladen` | Online: Bauernladen.at | 3 | 7.81 s | [Kalbsgulasch](https://bauernladen.at/produkte/fairkocht/kalbsgulasch-27286) · 17.9 € | 2026-10-25T04:53:59Z |
| ✅ | `bernos` | Online: Bernos Tauernwild | 2 | 4.96 s | [Hirschgulasch](https://www.bernos.at/produkt/hirschgulasch/) · 9.0 € | 2026-10-25T04:54:07Z |
| ✅ | `billa` | BILLA | 3 | 1.29 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-25T04:54:12Z |
| ✅ | `biohof-achleitner` | Online: Biohof Achleitner | 3 | 4.98 s | [Hausg'mocht Rindsgulasch](https://www.biohof.at/Hausgmocht-Rindsgulasch-4755) · 8.7 € | 2026-10-25T04:54:13Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 8.85 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-25T04:54:18Z |
| ✅ | `buchberger` | Online: Fleischerei Buchberger | 2 | 12.36 s | [Hausgemachte Gulasch-Suppe im Glas 450 ml](https://www.buchberger.shop/buchberger-hausgemachte-gulasch-suppe-im-glas-450-ml) · 7.5 € | 2026-10-25T04:54:27Z |
| ✅ | `deflorian` | Online: Deflorian | 2 | 1.28 s | [Rindsgulasch](https://deflorian.tirol/products/rindsgulasch) · 13.1 € | 2026-10-25T04:54:40Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 3.8 s | [NaBio Bio-Eintopf oder -Suppe](https://www.denns-biomarkt.at/angebote/) · 2.49 € | 2026-10-25T04:54:41Z |
| ✅ | `diechtl` | Online: Fleischerei Diechtl | 1 | 4.6 s | [Rindsgulasch im Glas](https://www.diechtl-shop.at/rindsgulasch-im-glas) · 8.99 € | 2026-10-25T04:54:45Z |
| ✅ | `dm` | dm | 3 | 4.75 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-25T04:54:50Z |
| ✅ | `draxler` | Online: Draxler Geflügel-Wild | 3 | 6.55 s | [Rehragout](https://www.xn--geflgel-draxler-2vb.at/produkt/rehragout/) · 10.0 € | 2026-10-25T04:54:55Z |
| ✅ | `every` | Online: every. | 3 | 14.99 s | [Turkish Lentil Soup](https://every-foods.com/products/turkish-lentil-soup) · 8.99 € | 2026-10-25T04:55:02Z |
| ✅ | `fichtenbauer` | Online: Fleischerei Fichtenbauer | 1 | 14.84 s | [Rindsgulasch essfertig](https://www.fleischerei-fichtenbauer.at/shop/rindsgulasch-essfertig) · 6.9 € | 2026-10-25T04:55:17Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 8.57 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-25T04:55:32Z |
| ✅ | `gerbl` | Online: Gerbl im Glas | 3 | 24.28 s | [Gulaschsuppe](https://shop.gerbl.at/ecommerce/product?product_id=796882&category_id=150129) · 9.0 € | 2026-10-25T04:55:41Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.02 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-25T04:56:05Z |
| ✅ | `gourmet-daheim` | Online: GOURMET Daheim (Mahlzeit Linz) | 3 | 12.87 s | [Kartoffelgulasch mit Waldviertler Wurst](https://www.mahlzeit.co.at/wp-content/uploads/2026/03/Preisliste_Bestellschein_GDH_2026_inkl_MwSt_Mahlzeit_web.pdf) · 8.5 € | 2026-10-25T04:56:10Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.31 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-25T04:56:23Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.33 s | [Gissinger Rindsgulasch](https://www.gurkerl.at/21861-gissinger-rindsgulasch) · 12.77 € | 2026-10-25T04:56:32Z |
| ✅ | `hofer-shop` | HOFER | 2 | 4.04 s | [Sonnhof Rindsgulasch](https://www.hofer.at/produkt/sonnhof-rindsgulasch-000000000000510738) · 9.49 € | 2026-10-25T04:56:35Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 29.27 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-10-25T04:56:39Z |
| ✅ | `jenichl` | Online: Genussbauernhof Jenichl | 2 | 1.86 s | [Gulasch im Glas](https://www.genussbauernhof-jenichl.at/shop#!/Gulasch-im-Glas/p/241886285) · 5.5 € | 2026-10-25T04:57:08Z |
| ✅ | `juit` | Online: Juit | 1 | 1.61 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-25T04:57:10Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 18.99 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-25T04:57:12Z |
| ✅ | `kumitzberg` | Online: Kumitzberg | 3 | 6.46 s | [Tirolerknödel](https://kumitzberg.at/products/tirolerknodel) · 9.8 € | 2026-10-25T04:57:31Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.46 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-25T04:57:50Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 3.42 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-25T04:57:52Z |
| ✅ | `lomoalto` | Online: Lomo Alto | 1 | 1.45 s | [BIO Rindergulasch im Glas 400g](https://lomoalto.at/products/rindergulasch-im-glas-400g) · 12.4 € | 2026-10-25T04:57:56Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 6.65 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 0.69 € | 2026-10-25T04:57:58Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 16.66 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-10-25T04:58:05Z |
| ✅ | `nah-frisch` | Nah&Frisch | 2 | 180.2 s | [Knorr . Bitte zu Tisch Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-25T04:58:22Z |
| ✅ | `penny` | PENNY | 3 | 5.35 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-25T05:01:23Z |
| ✅ | `penny-shop` | PENNY | 3 | 6.85 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-25T05:01:28Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 10.47 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-25T05:01:35Z |
| ✅ | `ruckzuck` | Online: Ruck Zuck Laden (Dunzinger's) | 3 | 20.11 s | [Gulaschsaft](https://www.ruckzuck-laden.at/shop/Gulaschsaft-p731601508) · 6.4 € | 2026-10-25T05:01:46Z |
| ✅ | `spar-shop` | SPAR/INTERSPAR | 3 | 1.82 s | [TANN Rinds-Bratengulasch](https://www.interspar.at/shop/lebensmittel/tann-rinds-bratengulasch/p/835817) · 21.99 € | 2026-10-25T05:02:07Z |
| ✅ | `steiramarkt` | Online: Steira Markt | 2 | 11.69 s | [Gulaschsuppe im Glas 400g](https://www.steiramarkt.at/produkt/gulaschsuppe-im-glas-400g/) · 7.0 € | 2026-10-25T05:02:09Z |
| ✅ | `subway-at` | Subway | 3 | 33.24 s | [Italian B.M.T.®](https://www.subway.com/de-AT/MenuNutrition/Menu/Product?ProductId=5257&MenuCategoryId=238) | 2026-10-25T05:02:21Z |
| ✅ | `suppito` | Online: SUPPITO | 2 | 3.32 s | [Rindsgulasch à la Suppito scharf](https://www.suppito.at/produkt/rindsgulasch-a-la-suppito/) · 12.1 € | 2026-10-25T05:02:55Z |
| ✅ | `thaller` | Online: Fleischhauerei Thaller | 1 | 9.06 s | [Rindsgulasch im Glas](https://fleischhauerei-thaller.at/produkt/rindsgulasch-im-glas/) · 7.5 € | 2026-10-25T05:02:58Z |
| ✅ | `voeslauermanufaktur` | Online: voeslauermanufaktur | 2 | 6.69 s | [Erdäpfelgulasch](https://www.voeslauermanufaktur.at/shop/feinkost-im-glas/hauptgerichte/) · 9.9 € | 2026-10-25T05:03:08Z |
| ✅ | `wagyuhof` | Online: Wagyuhof | 1 | 2.46 s | [Wagyu Gulasch](https://wagyuhof.com/products/wagyu-gulasch) · 13.2 € | 2026-10-25T05:03:15Z |
| ✅ | `wiesbauer_gourmet` | Online: Wiesbauer Gourmet | 2 | 7.26 s | [Feines Hirschgulasch aus Österreich 300 g](https://www.wiesbauer-gourmet.at/produkt/feines-hirschgulasch-300-g) · 9.9 € | 2026-10-25T05:03:17Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-25T04:53:51Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-25T04:54:13Z |
| ❌ | `dm-heisse` | dm | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T04:54:55Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-25T04:55:41Z |
| ❌ | `heisse-preise` | heisse-preise.io | 0 | 0.43 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T04:56:33Z |
| ❌ | `hofer` | HOFER | 0 | 0.53 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T04:56:34Z |
| ❌ | `lidl` | Lidl | 0 | 12.0 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-25T04:57:38Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-25T04:57:50Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-25T04:57:58Z |
| ❌ | `mpreis` | MPREIS | 0 | 0.64 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T04:57:58Z |
| ❌ | `off` | Open Food Facts | 0 | 0.38 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-10-25T05:01:22Z |
| ❌ | `spar` | SPAR/INTERSPAR | 0 | 0.58 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T05:02:06Z |
| ❌ | `sperchenedergut` | Online: Sperchenedergut | 0 | 0.44 s | `RobotsDisallowed: https://sperchenedergut.at/wp-json/wc/store/v1/products?per_page=100` | 2026-10-25T05:02:09Z |
| ❌ | `unimarkt` | Unimarkt | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T05:03:07Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-25T05:03:08Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-25T05:03:25Z |

### Bekannte Ausfälle (manuell gepflegt)

- `off` (Open Food Facts) ❌ seit 2026-10-16 (Hub-Lauf 22:59 UTC) dauerhaft, nicht mehr nur Upstream-503: OFF `robots.txt` verbietet für `User-agent: *` jetzt `/api`, `/cgi` und `/facets`, und der neue harte robots.txt-Gate in food-connectors (`0eaa455`) blockiert `cgi/search.pl` (Suche) und `api/v2/product` (EAN-Lookup) bewusst vor dem Request. `search.openfoodfacts.org` ist ebenfalls `Disallow: /`. Fix-Pfad (offen, food-connectors `adapters/off.py`): EAN-Lookup über die erlaubte Produktseite `/product/<ean>` (HTML), Suche über Open Prices / Datensatz-Dump statt Live-Suche. Kein Bypass des Gates.
- `lidl` ❌ HTTP 401 (bekannt, Lidl-API verlangt Auth; kein Login erlaubt).
- `heisse-preise`, `dm-heisse`, `hofer`, `mpreis`, `spar`, `unimarkt` ❌ seit Hub-Lauf 2026-10-17 20:07 UTC: Upstream-Ausfall bei heisse-preise.io. `https://heisse-preise.io/robots.txt` liefert HTTP 500 (nginx), und der robots.txt-Gate in food-connectors (`food_connectors/polite.py`) behandelt 5xx gemäß RFC 9309 korrekt als „alles verboten“, darum wird `data/latest-canonical.json` vor dem Request geblockt. Kein Code-Fehler, kein Bypass; erholt sich automatisch, sobald robots.txt wieder 200/4xx liefert.
- `sperchenedergut` ❌ seit Hub-Lauf 2026-10-24 22:07 UTC: Upstream-Ausfall beim Hoster (Host Europe). `https://sperchenedergut.at/robots.txt` liefert HTTP 502, der robots.txt-Gate behandelt 5xx gemäß RFC 9309 als „alles verboten“ und blockt die WooCommerce Store API vor dem Request. Kein Code-Fehler, kein Bypass; erholt sich automatisch, sobald die Seite wieder erreichbar ist.

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
| Wer steckt dahinter? | <img src="screenshots/vergleich/wer_1920.png" width="420"> | <img src="screenshots/vergleich/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich/qualitaet_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich/filialen_1920.png" width="420"> | <img src="screenshots/vergleich/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich/online_1920.png" width="420"> | <img src="screenshots/vergleich/online_390.png" width="140"> |
| Kombi-Ideen | <img src="screenshots/vergleich/kombi_1920.png" width="420"> | <img src="screenshots/vergleich/kombi_390.png" width="140"> |
| Fit to Go vs. Supermarkt | <img src="screenshots/vergleich/ftg_1920.png" width="420"> | <img src="screenshots/vergleich/ftg_390.png" width="140"> |
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
| Wer steckt dahinter? | <img src="screenshots/vergleich-servas/wer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich-servas/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich-servas/qualitaet_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich-servas/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich-servas/filialen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich-servas/online_1920.png" width="420"> | <img src="screenshots/vergleich-servas/online_390.png" width="140"> |
| Kombi-Ideen | <img src="screenshots/vergleich-servas/kombi_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kombi_390.png" width="140"> |
| Fit to Go vs. Supermarkt | <img src="screenshots/vergleich-servas/ftg_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ftg_390.png" width="140"> |
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

- `df68652` 2026-10-25 04:17 — chore(data): update data.json (bc6cbb567dc7), online_providers.json, and test_sc33_ui.mjs for SC68
- `7918495` 2026-10-25 03:59 — data(sc67): export data.json (684af70ab124, rankable=185, rankableLight=152) & sync test_sc33_ui
- `5838c92` 2026-10-25 03:45 — fix(sc67-p1.2): Light-Meal-Erklärtexte in Top/Heute an SC64+SC66-Definition (250–399 kcal ab 15 g P, ≥400 kcal mit 15–19,9 g P)
- `ab336c5` 2026-10-25 02:50 — data(sc66): export dataVersion 8bb86dd879eb (rankable=182, rankableLight=148===passesLightRank)
- `1e56caa` 2026-10-25 02:45 — fix(sc65-p2.1): ScoreWaterfall zeigt Zucker-Malus (sugar in PARTS + Info-Tooltip), Einzelbalken summieren sich auf total
- `9da81dc` 2026-10-25 02:12 — fix(sc65): sync ScoreWaterfall breakdown with score_parts/score, refine NONMEAL (#2885,#1492,#1785), and add goto-online E2E assertion
- `7f72692` 2026-10-25 02:07 — fix(sc64-p1.1,p1.2): useHashState feuert hashchange (Banner-Button → Online wechselt wirklich den Tab); passesLightRank vertraut explizitem Pipeline-rankableLight ab 240 kcal/11 g (Dead-Zone-Rettung, d252972a9be9)
- `20df8b9` 2026-10-25 02:01 — data(sc64): export dataVersion d252972a9be9 (180 rankable, 121 rankableLight)

**servas-ai/food-connectors**

- `ac46df9` 2026-10-25 04:12 — jenichl: new live connector — Genussbauernhof Jenichl farm shop (Franz & Brigitte Jenichl, Wagham 1, 4950 Altheim OÖ; Einzelunternehmen, no UID/FN published, no LEI): public Ecwid storefront catalog JSON (one request; no robots on either host) → 4 heat-up jar meals 'essfertig' (Gulasch im Glas 390 g, Gulaschsuppe 390 g, Beuschel 390 g, Gefüllte Paprika 640 g, 5,50 € each) + 7 frozen Knödel packs (Innviertler Surspeck/Selchfleisch/Haschee/Grammel/Spinat/Bärlauch 10 Stk. 10 €, Tiroler Knödel 4 Stk. 6,20 €) with ingredients, allergens, vision-checked photos 8/11 (3 Knödel share a generic plate photo → none); sauces, plain Semmelknödel, Speck, sausages excluded; no nutrition/GTIN; Post AT 11,50 € up to 20 kg; CLI + MCP jenichl_product/_search; +4 offline tests
- `58109ed` 2026-10-25 03:44 — bernos: new live connector — Bernos Tauernwild webshop (Bernos Wildkammer, Berno Mühlburger, Oberdrum/Oberlienz Osttirol, UID ATU68061919 VIES valid, no FN/LEI): public WooCommerce Store API (one request; robots allow all) → 4 heat-up wild-game jar meals 290 g (Rehragout 9,50 €, Hirschgulasch 9,00 €, Gamseintopf 9,00 €, Gulaschsuppe vom Wild 6,50 €) with stock, meat share, ingredients, vision-checked packshots (4/4); Wildsugo (sauce), Henkele and Dauerwürste excluded; no nutrition/GTIN; AT shipping 5,60 €; CLI + MCP bernos_product/_search; +3 offline tests
- `f743475` 2026-10-25 03:11 — kumitzberg: new live connector — Kumitzberg webshop (Großarler Genuss GmbH, Großarl Sbg, FN 473130f, UID ATU72344714 VIES valid, no LEI): public Shopify products.json + product pages (robots Allow: /) → 5 chilled heat-up meals (Rehragout im Glas 380 g 12,90 €, Tirolerknödel 420 g 9,80 €, Kaspressknödel 450 g 10,80 €, Schweinsbraten fertig gebraten 1 kg 17,90 €, Sous-Vide Spareribs ca. 1,2 kg 18,90 €) with availability, ingredients, nutrition per 100 g where printed (3/5); pasteten, Leberknödel, sausages excluded; no GTIN; DHL AT 9,90 €, free from 95 €; CLI + MCP kumitzberg_product/_search; +3 offline tests
- `f77bda5` 2026-10-25 02:37 — thaller: new live connector — Fleischhauerei Thaller webshop (Eduard Thaller, Markt Hartmannsdorf Stmk, UID ATU74028946 VIES valid, no FN/LEI): public WooCommerce Store API (one request; robots allow) → 'Speisen im Glas' minus broth (Rindssuppe) and raw Leberkäse → 1 chilled jar meal Rindsgulasch im Glas 350 g 7,50 € (21,43 €/kg) with stock, ingredients, shelf life 60 d at 2–4 °C, packshots; no nutrition/GTIN; Post AT 18,90 €/10,90 €, free from 250 €; CLI + MCP thaller_product/_search; +3 offline tests
- `c6242b5` 2026-10-25 02:10 — fichtenbauer: new live connector — Land-Fleischerei Fichtenbauer webshop (Land-Fleischerei Fichtenbauer GmbH, Amaliendorf/Gmünd Waldviertel NÖ, FN 523618b, UID ATU74965969 VIES valid): public Contao HTML shop listing + product microdata (3 s spacing, rate-verification page never bypassed) → 3 jar meals 400 g (Rindsgulasch 6,90 €, Beuschel 6,50 €, Wildragout 9,90 €) with €/kg, ingredients, packshots; sauce and smoked cold cuts excluded; no nutrition/GTIN; AT shipping 10 €, free from 99 €; CLI + MCP fichtenbauer_product/_search; +3 offline tests
- `ad29d9e` 2026-10-25 01:10 — diechtl: new live connector — Fleischerei Diechtl webshop (Fleischerei Diechtl Erich Ernst e.U., Bad Mitterndorf Stmk, FN 338325m, UID ATU41616104 VIES valid): public Shopware HTML 'Feinkost im Glas' (ItemList + Product JSON-LD, robots allow except /*?) → 1 jar meal (Rindsgulasch im Glas 390 g, 8,99 €, 23,05 €/kg) with availability, ingredients/allergens transcribed from the shop's label packshot (guarded by image name), photo; Gulaschsaft/Bolognese (sauces) and Rinderbrühe excluded; no nutrition/GTIN; Kühlpaket AT 6,90 €, free from 70 €; CLI + MCP diechtl_product/_search; +3 offline tests
- `0471a3f` 2026-10-25 00:39 — buchberger: new live connector — Fleischerei Buchberger webshop (Buchberger GmbH & Co KG, Pöllau Stmk, FN 14170p, UID ATU29190201 VIES valid): public HTML 'Essen im Glas' → 5 jar meals 450 ml (Gulasch-Suppe, Rindsgulasch, Putencurry, Kalbs-/Hirschragout; 7,50–13,50 €) with price, €/100 ml, ingredients/allergens, MHD, nutrition as printed with Atwater flag, packshots; sauces excluded; Kühlversand free from 120 €; CLI + MCP buchberger_product/_search; +3 offline tests
- `c961c3f` 2026-10-25 00:12 — deflorian: new live connector — Deflorian Tiefkühlspezialitäten webshop (Deflorian Tiefkühlspezialitäten GmbH, Gnadenwald Tirol, UID ATU64259769 VIES valid): public Shopify products.json + product-page ingredients → 27 frozen ready meals (Schlutzkrapfen, Knödel, Kaskrapfen, Rindsgulasch, Hühnercurry, Rindsbraten, soups, fruit dumplings; 3,70–19,80 €) with pack variants, weight, €/100 g, availability, allergens, photos; AT-wide frozen shipping 14,99 € / free from 40 €; no nutrition/GTIN on the shop; CLI + MCP deflorian_product/_search; +3 offline tests

**servas-ai/fertiggerichte-daten**

- `76a606d` 2026-10-25 04:42 — Bauernladen: Bio Galloway Hof Kerschbaumlehen Rindsbeuscherl 1 kg (online meal-prep 869→870); Schnelle-Küche re-check
- `46fbc55` 2026-10-25 04:12 — Daten-Squad T0405: Genussbauernhof Jenichl (genussbauernhof-jenichl.at, Franz & Brigitte Jenichl, Wagham 1, 4950 Altheim OÖ; Einzelunternehmen, no UID/FN published, no LEI) — 11 rows: 4 heat-up jar meals (Gulasch im Glas, Gulaschsuppe, Beuschel 390 g; Gefüllte Paprika 640 g; 5,50 €) + 7 frozen Knödel packs (10 €/6,20 €); ingredients lt. Shop, photos 8/11, no nutrition/GTIN; Post AT 11,50 € bis 20 kg; company + logo staged; online meal-prep 858→869
- `4731f5d` 2026-10-25 03:45 — bernos: Bernos Tauernwild (Bernos Wildkammer, Berno Mühlburger, Oberdrum/Oberlienz Osttirol, UID ATU68061919 VIES valid, no FN/LEI) — 4 heat-up wild-game jar meals 290 g (Rehragout 9,50 €, Hirschgulasch 9,00 €, Gamseintopf 9,00 €, Gulaschsuppe vom Wild 6,50 €), photos 4/4 vision PASS, ingredients + meat share, no nutrition/GTIN; AT shipping 5,60 €; company + logo staged; online meal-prep 854→858; validator OK
- `022f383` 2026-10-25 03:12 — Kumitzberg: new online store Kumitzberg (Großarler Genuss GmbH, Großarl Sbg, FN 473130f, UID ATU72344714 VIES valid, EU AT 50774 EU, no LEI) with 5 chilled heat-up meals (Rehragout im Glas 380 g 12,90 €, Tirolerknödel 420 g 9,80 €, Kaspressknödel 450 g 10,80 €, Schweinsbraten fertig gebraten 1 kg 17,90 €, Sous-Vide Spareribs ca. 1,2 kg 18,90 €; nutrition as printed 3/5, photos 4/5 vision PASS, spareribs styled image rejected; no GTIN; DHL AT 9,90 €, free from 95 €); online meal-prep 849→854; company + logo staged (T0307)
- `b501539` 2026-10-25 02:37 — Thaller: new online store Fleischhauerei Thaller (Eduard Thaller, Markt Hartmannsdorf Stmk, UID ATU74028946 VIES valid, no FN/LEI) with 1 jar meal Rindsgulasch im Glas 350 g 7,50 € (jar packshot vision PASS, ingredients, no nutrition/GTIN; Post AT 18,90 €, free from 250 €); online meal-prep 848→849; company + logo staged; Metzker Wien closed (delivery only 1160–1180 Wien) (T0233)
- `bc7bc7d` 2026-10-25 02:11 — Fichtenbauer: new online store Land-Fleischerei Fichtenbauer (Amaliendorf/Gmünd NÖ, FN 523618b, UID ATU74965969 VIES valid, no LEI) with 3 jar meals 400 g (Rindsgulasch 6,90 €, Beuschel 6,50 €, Wildragout 9,90 €; photos 3/3, ingredients, no nutrition/GTIN; AT shipping 10 €, free from 99 €); online meal-prep 845→848; company + logo staged (T0205)
- `4cb72dd` 2026-10-25 01:37 — T0133: evidence for format chains — Billa Plus covered via Billa (shop.billa.at shared assortment, REWE 2021 press release), Eurospar/Interspar via Spar (spar-shop index = interspar.at catalogue; per-market availability only on spar.at Cloudflare 403, not bypassed; pos-visible ids unmapped), ADEG no product source (REWE private labels already under Billa, 322 rows); Fleischerei Bergmann closed (no shipping terms; Bergmann GmbH FN 170260h, ATU55671605 VIES valid)
- `5f91023` 2026-10-25 01:10 — T0103: new online store Fleischerei Diechtl (diechtl-shop.at; Fleischerei Diechtl Erich Ernst e.U., Bad Mitterndorf Stmk, FN 338325m, UID ATU41616104 VIES valid, no LEI) — +1 jar meal Rindsgulasch im Glas 390 g 8,99 € via food-connectors diechtl; online meal-prep 844→845; ingredients/allergens transcribed from the shop's label packshot, no nutrition/GTIN (not estimated), photo vision 1/1; Kühlpaket AT 6,90 €, free from 70 €; Gulaschsaft/Bolognese/Rinderbrühe excluded; company row diechtl; logos staged for buchberger (header mark cropped from Rib-Eye-Boys combo) and diechtl (vision PASS); validate.py OK

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
