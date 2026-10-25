# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-25 09:04 UTC via `./run_all.sh` (stündlich).

**Connectors:** 52 ✅ / 9 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3664

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 22 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 22 | 0 | 0 |
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
| ✅ | `adamah` | Online: ADAMAH BioHof | 3 | 3.09 s | [Rindsgulasch im Weckglas](https://www.adamah.at/Produktdetailseite/RindsgulaschimWeckglas_42093) · 11.9 € | 2026-10-25T08:52:19Z |
| ✅ | `alfies` | Alfies | 3 | 7.23 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g-1) · 4.49 € | 2026-10-25T08:52:22Z |
| ✅ | `bauernladen` | Online: Bauernladen.at | 3 | 8.0 s | [Gulaschsuppe](https://bauernladen.at/produkte/fairkocht/gulaschsuppe-27262) · 15.5 € | 2026-10-25T08:52:29Z |
| ✅ | `bernos` | Online: Bernos Tauernwild | 2 | 5.75 s | [Hirschgulasch](https://www.bernos.at/produkt/hirschgulasch/) · 9.0 € | 2026-10-25T08:52:38Z |
| ✅ | `billa` | BILLA | 3 | 1.3 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-25T08:52:43Z |
| ✅ | `biohof-achleitner` | Online: Biohof Achleitner | 3 | 4.88 s | [Hausg'mocht Rindsgulasch](https://www.biohof.at/Hausgmocht-Rindsgulasch-4755) · 8.7 € | 2026-10-25T08:52:45Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 7.92 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-10-25T08:52:50Z |
| ✅ | `buchberger` | Online: Fleischerei Buchberger | 2 | 20.84 s | [Hausgemachte Gulasch-Suppe im Glas 450 ml](https://www.buchberger.shop/buchberger-hausgemachte-gulasch-suppe-im-glas-450-ml) · 7.5 € | 2026-10-25T08:52:58Z |
| ✅ | `bullinarium` | Online: Bullinarium (Hallers Bull Beef) | 1 | 10.34 s | [Bull Beef Gulasch 350g](https://www.bullinarium.com/online-shop/produkt/c/fix-fertig/p/bull-beef-gulasch-350g/) · 11.76 € | 2026-10-25T08:53:19Z |
| ✅ | `deflorian` | Online: Deflorian | 2 | 2.19 s | [Rindsgulasch](https://deflorian.tirol/products/rindsgulasch) · 13.1 € | 2026-10-25T08:53:30Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 3.8 s | [NaBio Bio-Eintopf oder -Suppe](https://www.denns-biomarkt.at/angebote/) · 2.49 € | 2026-10-25T08:53:32Z |
| ✅ | `diechtl` | Online: Fleischerei Diechtl | 1 | 4.65 s | [Rindsgulasch im Glas](https://www.diechtl-shop.at/rindsgulasch-im-glas) · 8.99 € | 2026-10-25T08:53:36Z |
| ✅ | `dm` | dm | 3 | 4.46 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-25T08:53:41Z |
| ✅ | `draxler` | Online: Draxler Geflügel-Wild | 3 | 5.88 s | [Rehragout](https://www.xn--geflgel-draxler-2vb.at/produkt/rehragout/) · 10.0 € | 2026-10-25T08:53:46Z |
| ✅ | `every` | Online: every. | 3 | 14.6 s | [Turkish Lentil Soup](https://every-foods.com/products/turkish-lentil-soup) · 8.99 € | 2026-10-25T08:53:52Z |
| ✅ | `fichtenbauer` | Online: Fleischerei Fichtenbauer | 1 | 14.71 s | [Rindsgulasch essfertig](https://www.fleischerei-fichtenbauer.at/shop/rindsgulasch-essfertig) · 6.9 € | 2026-10-25T08:54:07Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 8.8 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-10-25T08:54:21Z |
| ✅ | `gerbl` | Online: Gerbl im Glas | 3 | 23.93 s | [Gulaschsuppe](https://shop.gerbl.at/ecommerce/product?product_id=796882&category_id=150129) · 9.0 € | 2026-10-25T08:54:31Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.12 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-10-25T08:54:55Z |
| ✅ | `gourmet-daheim` | Online: GOURMET Daheim (Mahlzeit Linz) | 3 | 13.69 s | [Kartoffelgulasch mit Waldviertler Wurst](https://www.mahlzeit.co.at/wp-content/uploads/2026/03/Preisliste_Bestellschein_GDH_2026_inkl_MwSt_Mahlzeit_web.pdf) · 8.5 € | 2026-10-25T08:55:00Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.36 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-25T08:55:14Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.33 s | [Gissinger Rindsgulasch](https://www.gurkerl.at/21861-gissinger-rindsgulasch) · 12.77 € | 2026-10-25T08:55:22Z |
| ✅ | `hofer-shop` | HOFER | 2 | 3.73 s | [Sonnhof Rindsgulasch](https://www.hofer.at/produkt/sonnhof-rindsgulasch-000000000000510738) · 9.49 € | 2026-10-25T08:55:25Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 32.95 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-10-25T08:55:29Z |
| ✅ | `jenichl` | Online: Genussbauernhof Jenichl | 2 | 1.74 s | [Gulasch im Glas](https://www.genussbauernhof-jenichl.at/shop#!/Gulasch-im-Glas/p/241886285) · 5.5 € | 2026-10-25T08:56:02Z |
| ✅ | `juit` | Online: Juit | 1 | 1.51 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-10-25T08:56:04Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 16.76 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-10-25T08:56:05Z |
| ✅ | `kumitzberg` | Online: Kumitzberg | 3 | 7.07 s | [Tirolerknödel](https://kumitzberg.at/products/tirolerknodel) · 9.8 € | 2026-10-25T08:56:22Z |
| ✅ | `leitgeb` | Online: Leitgeb's Kärntnernudel | 2 | 7.79 s | [Italienischer Nudelteller](https://kaerntnernudel.co.at/produkt/italienischer-nudelteller/) · 11.2 € | 2026-10-25T08:56:30Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.29 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-25T08:56:50Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 1 | 3.32 s | [Veganes Gulasch](https://www.loewenanteil.com/products/veganes-gulasch) · 9.99 € | 2026-10-25T08:56:52Z |
| ✅ | `lomoalto` | Online: Lomo Alto | 1 | 1.47 s | [BIO Rindergulasch im Glas 400g](https://lomoalto.at/products/rindergulasch-im-glas-400g) · 12.4 € | 2026-10-25T08:56:55Z |
| ✅ | `moakt` | Online: Moakt.at (Weiz) | 2 | 36.5 s | [Rinder-Gulaschsuppe essfertig 400g](https://moakt.at/r-gulaschsuppe-essfertig-400g-pro-1glas) · 7.5 € | 2026-10-25T08:56:57Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 6.29 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 0.69 € | 2026-10-25T08:57:34Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 22.35 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-10-25T08:57:41Z |
| ✅ | `nah-frisch` | Nah&Frisch | 2 | 177.61 s | [Knorr . Bitte zu Tisch Suppen](https://www.nahundfrisch.at/de/aktuelles/angebote-der-woche) | 2026-10-25T08:58:03Z |
| ✅ | `nudlkudlmudl` | Online: Martina's Nudlkudlmudl | 3 | 4.34 s | [BAERLAUCHNUDELN Frühlingsboten SAISONALES SCHMANKE](https://www.nudlkudlmudl.com/onlineshop/) · 12.9 € | 2026-10-25T09:01:01Z |
| ✅ | `penny` | PENNY | 3 | 5.52 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-25T09:01:06Z |
| ✅ | `penny-shop` | PENNY | 3 | 7.07 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-10-25T09:01:12Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 10.3 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-25T09:01:19Z |
| ✅ | `purergenuss` | Online: Purer Genuss (Schüsseltrieb) | 1 | 12.41 s | [Wildsuppe mit Fleisch und Gemüse](https://www.purer-genuss.at/product/wildsuppe-mit-fleisch-und-gemuese/) · 6.99 € | 2026-10-25T09:01:29Z |
| ✅ | `regionalles` | Online: RegionAlles Joglland | 2 | 1.67 s | [Holdi's Gulasch im Glas](https://www.regionalles.com/products/gulasch-im-glas) · 8.4 € | 2026-10-25T09:01:42Z |
| ✅ | `ruckzuck` | Online: Ruck Zuck Laden (Dunzinger's) | 3 | 20.28 s | [Gulaschsaft](https://www.ruckzuck-laden.at/shop/Gulaschsaft-p731601508) · 6.4 € | 2026-10-25T09:01:44Z |
| ✅ | `scheffknecht` | Online: Ariane Scheffknecht | 2 | 27.09 s | [Gerstensuppe mit Selchfleisch](https://www.ariane-scheffknecht.at/product-page/gerstensuppe) · 13.5 € | 2026-10-25T09:02:04Z |
| ✅ | `spar-shop` | SPAR/INTERSPAR | 3 | 1.54 s | [TANN Rinds-Bratengulasch](https://www.interspar.at/shop/lebensmittel/tann-rinds-bratengulasch/p/835817) · 21.99 € | 2026-10-25T09:02:32Z |
| ✅ | `steiramarkt` | Online: Steira Markt | 2 | 12.18 s | [Gulaschsuppe im Glas 400g](https://www.steiramarkt.at/produkt/gulaschsuppe-im-glas-400g/) · 7.0 € | 2026-10-25T09:02:34Z |
| ✅ | `subway-at` | Subway | 3 | 33.36 s | [Italian B.M.T.®](https://www.subway.com/de-AT/MenuNutrition/Menu/Product?ProductId=5257&MenuCategoryId=238) | 2026-10-25T09:02:47Z |
| ✅ | `suppito` | Online: SUPPITO | 2 | 4.09 s | [Rindsgulasch à la Suppito scharf](https://www.suppito.at/produkt/rindsgulasch-a-la-suppito/) · 12.1 € | 2026-10-25T09:03:20Z |
| ✅ | `thaller` | Online: Fleischhauerei Thaller | 1 | 9.01 s | [Rindsgulasch im Glas](https://fleischhauerei-thaller.at/produkt/rindsgulasch-im-glas/) · 7.5 € | 2026-10-25T09:03:24Z |
| ✅ | `voeslauermanufaktur` | Online: voeslauermanufaktur | 2 | 6.67 s | [Erdäpfelgulasch](https://www.voeslauermanufaktur.at/shop/feinkost-im-glas/hauptgerichte/) · 9.9 € | 2026-10-25T09:03:34Z |
| ✅ | `wagyuhof` | Online: Wagyuhof | 1 | 2.27 s | [Wagyu Gulasch](https://wagyuhof.com/products/wagyu-gulasch) · 13.2 € | 2026-10-25T09:03:41Z |
| ✅ | `wiesbauer_gourmet` | Online: Wiesbauer Gourmet | 2 | 7.22 s | [Feines Hirschgulasch aus Österreich 300 g](https://www.wiesbauer-gourmet.at/produkt/feines-hirschgulasch-300-g) · 9.9 € | 2026-10-25T09:03:43Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-25T08:52:22Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-25T08:52:45Z |
| ❌ | `dm-heisse` | dm | 0 | 0.47 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T08:53:45Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-25T08:54:30Z |
| ❌ | `heisse-preise` | heisse-preise.io | 0 | 0.58 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T08:55:24Z |
| ❌ | `hofer` | HOFER | 0 | 0.36 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T08:55:24Z |
| ❌ | `lidl` | Lidl | 0 | 11.79 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-25T08:56:37Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-25T08:56:49Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-25T08:56:57Z |
| ❌ | `mpreis` | MPREIS | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T08:57:34Z |
| ❌ | `off` | Open Food Facts | 0 | 0.38 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-10-25T09:01:06Z |
| ❌ | `spar` | SPAR/INTERSPAR | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T09:02:31Z |
| ❌ | `sperchenedergut` | Online: Sperchenedergut | 0 | 0.47 s | `RobotsDisallowed: https://sperchenedergut.at/wp-json/wc/store/v1/products?per_page=100` | 2026-10-25T09:02:34Z |
| ❌ | `unimarkt` | Unimarkt | 0 | 0.37 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-10-25T09:03:33Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-25T09:03:34Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-25T09:03:51Z |

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
| Verpackungen | <img src="screenshots/vergleich/pack_1920.png" width="420"> | <img src="screenshots/vergleich/pack_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich/wer_1920.png" width="420"> | <img src="screenshots/vergleich/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich/qualitaet_390.png" width="140"> |
| Netz 3D | <img src="screenshots/vergleich/netz_1920.png" width="420"> | <img src="screenshots/vergleich/netz_390.png" width="140"> |
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
| Verpackungen | <img src="screenshots/vergleich-servas/pack_1920.png" width="420"> | <img src="screenshots/vergleich-servas/pack_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich-servas/wer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich-servas/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich-servas/qualitaet_390.png" width="140"> |
| Netz 3D | <img src="screenshots/vergleich-servas/netz_1920.png" width="420"> | <img src="screenshots/vergleich-servas/netz_390.png" width="140"> |
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

- `a4d7dac` 2026-10-25 08:33 — feat(sc74): P2.2 Straßenkurzname auf Heute-Filial-Chips, Viva Billa eingeschränktes Sortiment & SC74 Unit/E2E Gates
- `684512f` 2026-10-25 08:32 — SC74 P1 & P3 data sync (dataVersion 5d7674157f71, 206 rankable / 155 rankableLight)
- `5e84cdb` 2026-10-25 08:24 — fix(sc74): P2.1 einheitliche Gehzeit (ceil wie stores_linz_walk.json, walkMin an nähere Distanz gekoppelt) – Spar 378 m/7 min, dm 373/7, Hofer 385/7, Lidl 519/9, Penny 1124/19
- `2bf1395` 2026-10-25 07:46 — feat(sc73): P1.1 & P1.2 UI/Geo hardening (Zeitlhofer/Trafik exclusion, <60m Spar deduplication, Linz street address enrichment & E2E gates)
- `8903322` 2026-10-25 07:40 — SC73 data & Linz store sync (dataVersion 0e0a9dc8f98b, 206 rankable / 155 rankableLight)
- `5099ff1` 2026-10-25 06:55 — feat(sc72): Linz nearest store lookup (Denn's/Interspar/Unimarkt/Maximarkt/Nah&Frisch/Winkler), MeineShops gang='' default, Tabelle pliLight/Leicht & dataVersion d4f919f69d38
- `1d51037` 2026-10-25 06:46 — fix(sc72-p1b): Tabelle Preis-Leistung/Protein-Sort zeigt Light-Meals via isRowRankable (dm 25 -> nicht mehr 0 Treffer)
- `cbcf709` 2026-10-25 06:11 — feat(sc71-p1): MeineShops Leicht badge & online countsByChain sync

**servas-ai/food-connectors**

- `fa55ad5` 2026-10-25 08:55 — dengg: live Dengg Krapfen- und Knödelmanufaktur connector (dengg krapfen & knödel manufaktur GmbH, Hall in Tirol) — 26 frozen Knödel/Schlutzkrapfen/Kaskrapfen with datasheet nutrition, MCP tools, 3 offline tests
- `d20dae6` 2026-10-25 08:10 — regionalles: live RegionAlles Joglland connector (RegionALLES WB OG, Waldbach-Mönichwald Stmk) — 6 jar ready meals (Holdi's/Gastwirtschaft Hold, Krautgartner, Jobi), MCP tools, 3 offline tests
- `c896845` 2026-10-25 07:43 — bullinarium: live Hallers Bull Beef Fix & Fertig connector (Haller GmbH, Markt Allhau, Bgld) — 4 ready meals, MCP tools, 3 offline tests
- `b8e3d5c` 2026-10-25 07:15 — purergenuss: live connector for Purer Genuss / Schüsseltrieb Manufaktur (Szemes GmbH Pinkafeld, Burgenland) — 7 Wild-im-Glas ready meals (CLI + MCP purergenuss_product/purergenuss_search, offline tests)
- `f4a29aa` 2026-10-25 06:39 — moakt: live connector for Moakt.at (MoaktLaden Weiz Stmk) — 15 regional ready meals from Robert kocht, Feiertag mein Glas, Gemisch, Hirsch und mehr, Biohof Hirschbauer (CLI + MCP moakt_product/moakt_search, offline tests)
- `c01f599` 2026-10-25 06:10 — leitgeb: live connector Leitgeb's Kärntnernudel (Friesach, Ktn; WooCommerce Store API + product pages, 29 ready meals with nutrition)
- `6a884e8` 2026-10-25 05:39 — nudlkudlmudl: new live connector — Martina's Nudlkudlmudl (Martina Hinteregger, Hauptstrasse 28, 9545 Radenthein Kärnten; AMA-certified Nudelmanufaktur; no UID/FN published, no LEI): one public Jimdo /onlineshop/ page with schema.org Product microdata (1 request; robots disallow only /app/ + /j/, crawl-delay 5) → 7 ready meals: 6 hand-made Kärntner Nudeln 600 g / 5 Stk. (Kasnudel, Fleischnudel 13,90 €, Erdäpfel-, Spinat-, Tomate-Mozzarella-, Bärlauchnudel 12,90 €) + Schweinsbraten essfertig 250 g 6,00 €; Kletzennudel/Bratlfett/Sugo excluded; ingredients, availability, photos (vision 7/7); no nutrition/GTIN; Post Frischeversand AT only, free from 100 €; CLI + MCP nudlkudlmudl_product/_search; +3 offline tests
- `e2046db` 2026-10-25 05:14 — scheffknecht: new live connector — Ariane Scheffknecht webshop (sole trader Ariane Scheffknecht, Lorettoweg 14, Lustenau Vorarlberg; no UID/FN published → VIES not checkable, no LEI): public Wix store-products sitemap + product-page schema.org JSON-LD (1 + 9 requests at 1 s; robots allow all except ?lightbox=) → 8 pasteurised jar meals 470–480 g / 2 portions (Chili con Carne 13,50 €, Rotes Thai Curry mit Hühnerfilet 14,00 €, Indisches Hühner-Curry 14,00 €, Gelbes Zitronengras Linsen Dal 13,50 €, …) with availability, ingredients, portions, vision-checked photos (8/8); Ragù alla Bolognese (sauce) excluded; no nutrition/GTIN; shipping fee not published, free from 12 jars; CLI + MCP scheffknecht_product/_search; +3 offline tests

**servas-ai/fertiggerichte-daten**

- `71312a4` 2026-10-25 08:56 — Dengg Krapfen- und Knödelmanufaktur (Hall in Tirol): +26 frozen Knödel/Schlutzkrapfen/Kaskrapfen with datasheet nutrition (946→972); company dengg (dengg krapfen & knödel manufaktur GmbH FN 376199i, UID ATU67085156 VIES valid, no LEI)
- `96cfa1e` 2026-10-25 08:12 — regionalles: FN format 537480m (validate.py OK)
- `c02ed9c` 2026-10-25 08:10 — RegionAlles Joglland (Waldbach-Mönichwald Stmk): +6 jar ready meals (940→946) from Gastwirtschaft Hold, Biohof Krautgartner, Jobi; company regionalles (RegionALLES WB OG FN 537480 m, UID ATU75793759 VIES valid, no LEI)
- `d44e706` 2026-10-25 07:44 — Bullinarium / Hallers Bull Beef (Markt Allhau Bgld): +4 Fix & Fertig ready meals (936→940); company haller (Haller GmbH FN 492415s, UID ATU73356147 VIES valid, no LEI)
- `1cfe51f` 2026-10-25 07:16 — Purer Genuss / Schüsseltrieb Manufaktur (Pinkafeld Bgld): +7 Wild-im-Glas ready meals (929→936); company szemes (Szemes GmbH FN 660812h, UID ATU82450358 VIES valid, no LEI)
- `902850b` 2026-10-25 06:41 — Moakt.at (MoaktLaden Weiz Stmk): +15 regional ready meals (914→929) from Robert kocht, Feiertag mein Glas, Gemisch, Hirsch und mehr, Biohof Hirschbauer; companies moakt (Verein ZVR 1009369655, UID ATU80009358 VIES valid) + feiertag
- `84f0c57` 2026-10-25 06:12 — Leitgeb's Kärntnernudel (Friesach Ktn): +29 online meal-prep rows with nutrition (885→914), company leitgebs (FN 62213v, UID ATU82506478 VIES valid)
- `fc2579b` 2026-10-25 05:39 — nudlkudlmudl: Martina's Nudlkudlmudl (Martina Hinteregger, Hauptstrasse 28, 9545 Radenthein Kärnten; AMA-certified; no UID/FN published → VIES not checkable, no LEI) — 7 ready meals: 6 hand-made Kärntner Nudeln 600 g / 5 Stk. (Kasnudel, Fleischnudel 13,90 €, Erdäpfel-, Spinat-, Tomate-Mozzarella-, Bärlauchnudel 12,90 €; 5 vegetarian) + Schweinsbraten essfertig 250 g 6,00 €; photos 7/7 vision PASS, ingredients lt. Shop, no nutrition/GTIN; Post Frischeversand AT only, free from 100 €, fee not read (robots-disallowed /j/); Kletzennudel/Bratlfett/Sugo excluded; company staged, no logo; online meal-prep 878→885; validator OK

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
