# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-11-02 14:07 UTC via `./run_all.sh` (stündlich).

**Connectors:** 55 ✅ / 12 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 3664

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 29 | 4 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 29 | 0 | 0 |
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
| ✅ | `adamah` | Online: ADAMAH BioHof | 3 | 3.2 s | [Rindsgulasch im Weckglas](https://www.adamah.at/Produktdetailseite/RindsgulaschimWeckglas_42093) · 11.9 € | 2026-11-02T13:53:18Z |
| ✅ | `alfies` | Alfies | 3 | 7.26 s | [Knorr Meisterkessel Gulaschsuppe](https://www.alfies.at/produkt/knorr-meisterkessel-gulaschsuppe-dose-500g-1) · 4.49 € | 2026-11-02T13:53:22Z |
| ✅ | `bauernladen` | Online: Bauernladen.at | 3 | 7.93 s | [Gulaschsuppe](https://bauernladen.at/produkte/fairkocht/gulaschsuppe-27262) · 15.5 € | 2026-11-02T13:53:29Z |
| ✅ | `bernos` | Online: Bernos Tauernwild | 2 | 5.24 s | [Hirschgulasch](https://www.bernos.at/produkt/hirschgulasch/) · 9.0 € | 2026-11-02T13:53:37Z |
| ✅ | `billa` | BILLA | 3 | 1.32 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-11-02T13:53:43Z |
| ✅ | `biohof-achleitner` | Online: Biohof Achleitner | 3 | 4.99 s | [Hausg'mocht Rindsgulasch](https://www.biohof.at/Hausgmocht-Rindsgulasch-4755) · 8.7 € | 2026-11-02T13:53:44Z |
| ✅ | `bofrost` | Online: bofrost* | 3 | 11.78 s | [Wiener Rindsgulasch](https://www.bofrost.at/shop/fleisch_44196/fleischzubereitungen_34987/wiener-rindsgulasch_03373.html) · 14.99 € | 2026-11-02T13:53:49Z |
| ✅ | `buchberger` | Online: Fleischerei Buchberger | 2 | 12.74 s | [Hausgemachte Gulasch-Suppe im Glas 450 ml](https://www.buchberger.shop/buchberger-hausgemachte-gulasch-suppe-im-glas-450-ml) · 7.5 € | 2026-11-02T13:54:01Z |
| ✅ | `bullinarium` | Online: Bullinarium (Hallers Bull Beef) | 1 | 10.22 s | [Bull Beef Gulasch 350g](https://www.bullinarium.com/online-shop/produkt/c/fix-fertig/p/bull-beef-gulasch-350g/) · 11.76 € | 2026-11-02T13:54:14Z |
| ✅ | `deflorian` | Online: Deflorian | 2 | 1.61 s | [Rindsgulasch](https://deflorian.tirol/products/rindsgulasch) · 13.1 € | 2026-11-02T13:54:25Z |
| ✅ | `dengg` | Online: Dengg Krapfen- und Knödelmanufaktur | 3 | 27.56 s | [Spinatknödel 4 Stk.](https://www.dengg.info/spinatknoedel-4-stk--62241021-de.html) · 5.7 € | 2026-11-02T13:54:26Z |
| ✅ | `denns` | denn's BioMarkt | 1 | 3.78 s | [NaBio Bio-Eintopf oder -Suppe](https://www.denns-biomarkt.at/angebote/) · 2.49 € | 2026-11-02T13:54:54Z |
| ✅ | `diechtl` | Online: Fleischerei Diechtl | 1 | 4.59 s | [Rindsgulasch im Glas](https://www.diechtl-shop.at/rindsgulasch-im-glas) · 8.99 € | 2026-11-02T13:54:58Z |
| ✅ | `dm` | dm | 3 | 4.71 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-11-02T13:55:03Z |
| ✅ | `draxler` | Online: Draxler Geflügel-Wild | 3 | 4.02 s | [Rehragout](https://www.xn--geflgel-draxler-2vb.at/produkt/rehragout/) · 10.0 € | 2026-11-02T13:55:08Z |
| ✅ | `egle` | Online: Egle | 3 | 11.66 s | [BIO Rinder-Gulasch, 400 g](https://www.egleshop.at/BIO-Rinder-Gulasch-400-g) · 7.49 € | 2026-11-02T13:55:12Z |
| ✅ | `every` | Online: every. | 3 | 17.99 s | [Turkish Lentil Soup](https://every-foods.com/products/turkish-lentil-soup) · 8.99 € | 2026-11-02T13:55:24Z |
| ✅ | `fichtenbauer` | Online: Fleischerei Fichtenbauer | 3 | 84.13 s | [Beuschel essfertig](https://www.fleischerei-fichtenbauer.at/shop/beuschel-essfertig) · 6.5 € | 2026-11-02T13:55:42Z |
| ✅ | `fittogo` | Online: Fit2go | 3 | 8.72 s | [Auberginen-Chili con Carne mit Käse Überbacken](https://fittogo.at/products/auberginen-chili-con-carne-mit-kase-uberbacken) · 9.99 € | 2026-11-02T13:57:07Z |
| ✅ | `flottelotte` | Online: Flotte Lotte | 3 | 9.04 s | [Kartoffel Gulasch](https://flottelottezwettl.at/Kartoffel-Gulasch) · 6.5 € | 2026-11-02T13:57:16Z |
| ✅ | `gerbl` | Online: Gerbl im Glas | 3 | 26.08 s | [Gulaschsuppe](https://shop.gerbl.at/ecommerce/product?product_id=796882&category_id=150129) · 9.0 € | 2026-11-02T13:57:25Z |
| ✅ | `goldblatt` | Online: Goldblatt | 2 | 5.2 s | [Erdäpfel Gulasch](https://goldblatt.at/products/bio-erdapfel-gulasch) · 11.99 € | 2026-11-02T13:57:51Z |
| ✅ | `gourmet-daheim` | Online: GOURMET Daheim (Mahlzeit Linz) | 3 | 12.28 s | [Kartoffelgulasch mit Waldviertler Wurst](https://www.mahlzeit.co.at/wp-content/uploads/2026/03/Preisliste_Bestellschein_GDH_2026_inkl_MwSt_Mahlzeit_web.pdf) · 8.5 € | 2026-11-02T13:57:56Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 8.44 s | [Chili Cheddar 1,8kg](https://shop.gourmetfein.com/products/chili-cheddar-1-8kg) · 26.9 € | 2026-11-02T13:58:09Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 1.2 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 18.79 € | 2026-11-02T13:58:17Z |
| ✅ | `hofer-shop` | HOFER | 3 | 4.67 s | [Sonnhof Rindsgulasch](https://www.hofer.at/produkt/sonnhof-rindsgulasch-000000000000510738) · 9.49 € | 2026-11-02T13:58:20Z |
| ✅ | `issmich` | Online: iss mich! | 3 | 27.78 s | [Bio Rotweingulasch vom Freilandrind](https://www.issmich.at/Bio-Shop/Eintoepfe/Fleisch/15/Bio-Rotweingulasch-vom-Freilandrind) · 11.5 € | 2026-11-02T13:58:25Z |
| ✅ | `jenichl` | Online: Genussbauernhof Jenichl | 2 | 1.84 s | [Gulasch im Glas](https://www.genussbauernhof-jenichl.at/shop#!/Gulasch-im-Glas/p/241886285) · 5.5 € | 2026-11-02T13:58:52Z |
| ✅ | `juit` | Online: Juit | 1 | 1.52 s | [Rindergulasch mit gegrillter Paprika](https://www.juit.com/de/gerichte/rindergulasch-mit-paprika) | 2026-11-02T13:58:54Z |
| ✅ | `kernbeisser` | Online: Kernbeißer | 3 | 17.59 s | [Maghreb-Hirse mit Artischocken](https://kernbeisser.at/produkt/maghreb-hirse-mit-artischocken/) · 9.0 € | 2026-11-02T13:58:56Z |
| ✅ | `kumitzberg` | Online: Kumitzberg | 3 | 7.2 s | [Tirolerknödel](https://kumitzberg.at/products/tirolerknodel) · 9.8 € | 2026-11-02T13:59:14Z |
| ✅ | `leitgeb` | Online: Leitgeb's Kärntnernudel | 2 | 9.12 s | [Italienischer Nudelteller](https://kaerntnernudel.co.at/produkt/italienischer-nudelteller/) · 11.2 € | 2026-11-02T13:59:21Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.37 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-11-02T13:59:43Z |
| ✅ | `loewenanteil` | Online: Löwenanteil | 2 | 5.24 s | [Rindergulasch](https://www.loewenanteil.com/products/rindergulasch) · 12.99 € | 2026-11-02T13:59:45Z |
| ✅ | `lomoalto` | Online: Lomo Alto | 1 | 1.41 s | [BIO Rindergulasch im Glas 400g](https://lomoalto.at/products/rindergulasch-im-glas-400g) · 12.4 € | 2026-11-02T13:59:51Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 12.88 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-11-02T14:00:14Z |
| ✅ | `myproduct` | Online: myProduct | 3 | 32.97 s | [Bio Szegediner Gulasch 460g - Fertiggericht von Ha](https://myproduct.at/bio-szegediner-gulasch-450ml-hartls-kulinarikum) · 12.79 € | 2026-11-02T14:00:27Z |
| ✅ | `noglu` | Online: NoGlu (glutenfreie Knödel) | 2 | 4.25 s | [Glutenfreie Speckknödel, 4 Stück (500 g)](https://www.noglu.at/product/glutenfreie-speckknoedel/) · 9.0 € | 2026-11-02T14:03:36Z |
| ✅ | `nudlkudlmudl` | Online: Martina's Nudlkudlmudl | 3 | 4.33 s | [BAERLAUCHNUDELN Frühlingsboten SAISONALES SCHMANKE](https://www.nudlkudlmudl.com/onlineshop/) · 12.9 € | 2026-11-02T14:03:40Z |
| ✅ | `penny` | PENNY | 3 | 5.4 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-11-02T14:03:45Z |
| ✅ | `penny-shop` | PENNY | 3 | 10.62 s | [Gulasch- od. Bratensaft](https://www.penny.at/produkte/gulasch-od-bratensaft-7818089) · 1.39 € | 2026-11-02T14:03:51Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 9.61 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-11-02T14:04:01Z |
| ✅ | `purergenuss` | Online: Purer Genuss (Schüsseltrieb) | 1 | 12.57 s | [Wildsuppe mit Fleisch und Gemüse](https://www.purer-genuss.at/product/wildsuppe-mit-fleisch-und-gemuese/) · 6.99 € | 2026-11-02T14:04:11Z |
| ✅ | `regionalles` | Online: RegionAlles Joglland | 2 | 2.15 s | [Holdi's Gulasch im Glas](https://www.regionalles.com/products/gulasch-im-glas) · 8.4 € | 2026-11-02T14:04:24Z |
| ✅ | `ruckzuck` | Online: Ruck Zuck Laden (Dunzinger's) | 3 | 20.33 s | [Gulaschsaft](https://www.ruckzuck-laden.at/shop/Gulaschsaft-p731601508) · 6.4 € | 2026-11-02T14:04:26Z |
| ✅ | `scheffknecht` | Online: Ariane Scheffknecht | 2 | 27.16 s | [Gerstensuppe mit Selchfleisch](https://www.ariane-scheffknecht.at/product-page/gerstensuppe) · 13.5 € | 2026-11-02T14:04:47Z |
| ✅ | `schmankerl` | Online: Schmankerl Österreich | 1 | 1.57 s | [Gulaschsuppe](https://schmankerl-oesterreich.at/products/gulaschsuppe) · 7.9 € | 2026-11-02T14:05:14Z |
| ✅ | `sperchenedergut` | Online: Sperchenedergut | 1 | 22.64 s | [Gulaschsuppe vom Bio-Angusrind](https://sperchenedergut.at/produkt/gulaschsuppe-vom-angusrind/) · 9.5 € | 2026-11-02T14:05:18Z |
| ✅ | `steiramarkt` | Online: Steira Markt | 2 | 11.13 s | [Gulaschsuppe im Glas 400g](https://www.steiramarkt.at/produkt/gulaschsuppe-im-glas-400g/) · 7.0 € | 2026-11-02T14:05:41Z |
| ✅ | `subway-at` | Subway | 3 | 34.96 s | [Italian B.M.T.®](https://www.subway.com/de-AT/MenuNutrition/Menu/Product?ProductId=5257&MenuCategoryId=238) | 2026-11-02T14:05:52Z |
| ✅ | `suppito` | Online: SUPPITO | 1 | 3.03 s | [Erdäpfelgulasch mit Räuchertofu](https://www.suppito.at/produkt/erdaepfelgulaschmitgeraeuchertemtofu/) · 11.1 € | 2026-11-02T14:06:28Z |
| ✅ | `thaller` | Online: Fleischhauerei Thaller | 1 | 8.55 s | [Rindsgulasch im Glas](https://fleischhauerei-thaller.at/produkt/rindsgulasch-im-glas/) · 7.5 € | 2026-11-02T14:06:31Z |
| ✅ | `voeslauermanufaktur` | Online: voeslauermanufaktur | 2 | 6.61 s | [Erdäpfelgulasch](https://www.voeslauermanufaktur.at/shop/feinkost-im-glas/hauptgerichte/) · 9.9 € | 2026-11-02T14:06:40Z |
| ✅ | `wagyuhof` | Online: Wagyuhof | 1 | 2.37 s | [Wagyu Rindsgulasch im Glas](https://wagyuhof.com/products/wagyu-gulasch) · 13.2 € | 2026-11-02T14:06:47Z |
| ✅ | `wiesbauer_gourmet` | Online: Wiesbauer Gourmet | 2 | 7.99 s | [Feines Hirschgulasch aus Österreich 300 g](https://www.wiesbauer-gourmet.at/produkt/feines-hirschgulasch-300-g) · 9.9 € | 2026-11-02T14:06:49Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-11-02T13:53:22Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-11-02T13:53:44Z |
| ❌ | `dm-heisse` | dm | 0 | 0.48 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T13:55:08Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-11-02T13:57:25Z |
| ❌ | `heisse-preise` | heisse-preise.io | 0 | 0.36 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T13:58:19Z |
| ❌ | `hofer` | HOFER | 0 | 0.36 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T13:58:19Z |
| ❌ | `lidl` | Lidl | 0 | 11.84 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-11-02T13:59:31Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-11-02T13:59:43Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-11-02T13:59:52Z |
| ❌ | `moakt` | Online: Moakt.at (Weiz) | 0 | 21.03 s | `RobotsDisallowed: https://moakt.at/robert-kocht` | 2026-11-02T13:59:52Z |
| ❌ | `mpreis` | MPREIS | 0 | 0.48 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T14:00:13Z |
| ❌ | `nah-frisch` | Nah&Frisch | 0 | 155.38 s | `0 Treffer` | 2026-11-02T14:01:00Z |
| ❌ | `off` | Open Food Facts | 0 | 0.44 s | `RobotsDisallowed: https://world.openfoodfacts.org/cgi/search.pl?search_terms=gulasch&count` | 2026-11-02T14:03:45Z |
| ❌ | `spar` | SPAR/INTERSPAR | 0 | 0.47 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T14:05:16Z |
| ❌ | `spar-shop` | SPAR/INTERSPAR | 0 | 1.91 s | `HTTPError: HTTP Error 400: Bad Request` | 2026-11-02T14:05:16Z |
| ❌ | `unimarkt` | Unimarkt | 0 | 0.47 s | `RobotsDisallowed: https://heisse-preise.io/data/latest-canonical.json` | 2026-11-02T14:06:39Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-11-02T14:06:40Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-11-02T14:06:58Z |
| ❌ | `zoart` | Online: Sous Vide Fertiggerichte (zoart) | 0 | 12.99 s | `HTTPError: HTTP Error 403: Forbidden` | 2026-11-02T14:06:58Z |

### Bekannte Ausfälle (manuell gepflegt)

- `off` (Open Food Facts) ❌ seit 2026-10-16 (Hub-Lauf 22:59 UTC) dauerhaft, nicht mehr nur Upstream-503: OFF `robots.txt` verbietet für `User-agent: *` jetzt `/api`, `/cgi` und `/facets`, und der neue harte robots.txt-Gate in food-connectors (`0eaa455`) blockiert `cgi/search.pl` (Suche) und `api/v2/product` (EAN-Lookup) bewusst vor dem Request. `search.openfoodfacts.org` ist ebenfalls `Disallow: /`. Fix-Pfad (offen, food-connectors `adapters/off.py`): EAN-Lookup über die erlaubte Produktseite `/product/<ean>` (HTML), Suche über Open Prices / Datensatz-Dump statt Live-Suche. Kein Bypass des Gates.
- `lidl` ❌ HTTP 401 (bekannt, Lidl-API verlangt Auth; kein Login erlaubt).
- `heisse-preise`, `dm-heisse`, `hofer`, `mpreis`, `spar`, `unimarkt` ❌ seit Hub-Lauf 2026-10-17 20:07 UTC: Upstream-Ausfall bei heisse-preise.io. `https://heisse-preise.io/robots.txt` liefert HTTP 500 (nginx), und der robots.txt-Gate in food-connectors (`food_connectors/polite.py`) behandelt 5xx gemäß RFC 9309 korrekt als „alles verboten“, darum wird `data/latest-canonical.json` vor dem Request geblockt. Kein Code-Fehler, kein Bypass; erholt sich automatisch, sobald robots.txt wieder 200/4xx liefert.
- `sperchenedergut` ❌ seit Hub-Lauf 2026-10-24 22:07 UTC: Upstream-Ausfall beim Hoster (Host Europe). `https://sperchenedergut.at/robots.txt` liefert HTTP 502, der robots.txt-Gate behandelt 5xx gemäß RFC 9309 als „alles verboten“ und blockt die WooCommerce Store API vor dem Request. Kein Code-Fehler, kein Bypass; erholt sich automatisch, sobald die Seite wieder erreichbar ist.
- `spar-shop` ❌ seit 2026-10-30 (Hub-Lauf 18:15 UTC): INTERSPAR-Relaunch (Nuxt), der FACT-Finder-Kanal `products_lmos_at` liefert HTTP 400; die neue `/api/search/results` liegt hinter einer Cloudflare-Challenge und wird bewusst nicht umgangen (Details: COVERAGE T1738/T1809, food-connectors `7d4eeec`). Fix braucht den neuen Kanal aus einer normalen Browser-Sitzung.
- `nah-frisch` ❌ seit Hub-Lauf 2026-10-30 18:15 UTC, aber kein Defekt: die Angebotsseite ist erreichbar (robots 200, KW44+KW45 mit 32 Kacheln, `offers()` parst sie korrekt). Diese Woche ist nur kein Fertiggericht im Flugblatt, darum findet der Smoke-Test (gulasch/lasagne/suppe, dann Kategorie ready-meals) 0 Treffer. Erholt sich mit dem nächsten passenden Wochenangebot.
- `fichtenbauer` ⚠️ im Hub-Lauf 2026-10-30 18:15 UTC mit 0 Treffern (86 s Latenz), Einzel-Retest um 18:15 UTC bestanden (3 Treffer). Langsamer Upstream, kein Code-Fehler.
- `zoart` ⚠️ Hub-Lauf 2026-10-30 19:18 UTC: einmaliges HTTP 403 (flaky), Retest direkt danach grün; kein Fix nötig.
- `penny-shop` ⚠️ Hub-Lauf 2026-10-30 20:09 UTC: sporadisches HTTP 403 der REWE product-discovery API auf einzelnen Listing-Seiten (z. B. page=4, wechselnd; vermutlich WAF/Rate-Limit), Retest 20:11 UTC grün (3 Treffer); kein Code-Fehler, kein Bypass. Falls es sich häuft: Retry mit Backoff in `penny_shop.listing()`. `zoart` ist im selben Lauf wieder grün.
- `gourmet-daheim` ⚠️ Hub-Lauf 2026-10-30 20:55 UTC: einmal `RobotsDisallowed` für die Preisliste-PDF auf mahlzeit.co.at (vermutlich robots.txt-Abruf kurz fehlgeschlagen), Einzel-Retest 21:12 UTC grün; kein Code-Fehler. `penny-shop` ist im selben Lauf wieder grün. Erneut im Hub-Lauf 22:48 UTC (gleicher RobotsDisallowed), Einzel-Retest 23:05 UTC wieder grün: robots.txt-Abruf von mahlzeit.co.at ist offenbar flaky. Erneut im Hub-Lauf 2026-10-31 00:57 UTC, Einzel-Retest 01:06 UTC grün.
- `purergenuss` ⚠️ Hub-Lauf 2026-10-31 01:03 UTC: einmal `RobotsDisallowed` für /wp-json/wc/store/v1/products, obwohl robots.txt (200, text/plain) /wp-json nicht sperrt; Einzel-Retest 01:06 UTC grün. Gleiches Muster wie gourmet-daheim: robots.txt-Abruf kurz fehlgeschlagen, kein Code-Fehler.
- `suppito` + `purergenuss` ⚠️ Hub-Lauf 2026-10-31 02:10 UTC: beide fail; Einzel-Retest 02:17 UTC weiterhin fail. Ursache extern: TLS-Handshake zu suppito.at/www.suppito.at und purergenuss.at/www.purergenuss.at bricht vom Box-Netz ab (curl exit 35 / SSL UNEXPECTED_EOF), robots.txt daher nicht abrufbar → RobotsDisallowed (fail-closed, korrekt). Kein Code-Fehler; Host-Ausfall oder WAF-Sperre der Box-IP. Nicht umgehen; nächste Läufe beobachten.
- `bernos` + `gourmet-daheim` + `purergenuss` ⚠️ Hub-Lauf 2026-10-31 07:55–08:05 UTC: alle drei einmal `RobotsDisallowed` (robots.txt-Abruf kurz fehlgeschlagen; bernos.at robots.txt sperrt nichts), Einzel-Retests 08:08–08:09 UTC grün. Flaky robots.txt-Abruf, kein Code-Fehler. `suppito` ist im selben Lauf wieder grün.
- `adamah` ⚠️ im Hub-Lauf 2026-11-01 01:00 UTC HTTP 404, `fichtenbauer` 0 Treffer (92 s); Einzel-Retest 01:15 UTC beide bestanden (3 bzw. 2 Treffer). Transienter Upstream, kein Code-Fehler.
- `fichtenbauer` ⚠️ im Hub-Lauf 2026-11-01 02:01 UTC erneut 0 Treffer (136 s Latenz); Einzel-Retest 02:16 UTC bestanden (1 Treffer, 25 s). Langsamer/transienter Upstream, kein Code-Fehler.
- `fichtenbauer` ⚠️ im Hub-Lauf 2026-11-01 02:57 UTC zum dritten Mal in Folge 0 Treffer (115 s Latenz); Einzel-Retest 03:09 UTC bestanden (1 Treffer, 36 s). Scheitert nur unter Last im Gesamtlauf, kein Code-Fehler; ggf. Timeout/Retry im Smoke-Test erhöhen.
- `penny-shop` ⚠️ im Hub-Lauf 2026-11-01 03:55 UTC wieder einmal HTTP 403 (REWE product-discovery API, sporadisch, nicht umgangen); Einzel-Retest 04:14 UTC bestanden (3 Treffer, 8.6 s). `fichtenbauer` und `sperchenedergut` diesmal grün. Kein Fix nötig.

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
| Meine Shops & Ranking | <img src="screenshots/vergleich/meine-shops_1920.png" width="420"> | <img src="screenshots/vergleich/meine-shops_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich/plan_1920.png" width="420"> | <img src="screenshots/vergleich/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich/ki_1920.png" width="420"> | <img src="screenshots/vergleich/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich/hofer-top30_390.png" width="140"> |
| Feed | <img src="screenshots/vergleich/feed_1920.png" width="420"> | <img src="screenshots/vergleich/feed_390.png" width="140"> |
| Galerie | <img src="screenshots/vergleich/galerie_1920.png" width="420"> | <img src="screenshots/vergleich/galerie_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich/top_1920.png" width="420"> | <img src="screenshots/vergleich/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich/marken_1920.png" width="420"> | <img src="screenshots/vergleich/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich/familien_1920.png" width="420"> | <img src="screenshots/vergleich/familien_390.png" width="140"> |
| Dashboard | <img src="screenshots/vergleich/dashboard_1920.png" width="420"> | <img src="screenshots/vergleich/dashboard_390.png" width="140"> |
| Gesundheit & Qualität | <img src="screenshots/vergleich/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich/gesundheit_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich/pack_1920.png" width="420"> | <img src="screenshots/vergleich/pack_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich/wer_1920.png" width="420"> | <img src="screenshots/vergleich/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich/qualitaet_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich/logos_1920.png" width="420"> | <img src="screenshots/vergleich/logos_390.png" width="140"> |
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
| Meine Shops & Ranking | <img src="screenshots/vergleich-servas/meine-shops_1920.png" width="420"> | <img src="screenshots/vergleich-servas/meine-shops_390.png" width="140"> |
| Ernährungsplan | <img src="screenshots/vergleich-servas/plan_1920.png" width="420"> | <img src="screenshots/vergleich-servas/plan_390.png" width="140"> |
| KI-Ansicht | <img src="screenshots/vergleich-servas/ki_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ki_390.png" width="140"> |
| Hofer Top 30 | <img src="screenshots/vergleich-servas/hofer-top30_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hofer-top30_390.png" width="140"> |
| Feed | <img src="screenshots/vergleich-servas/feed_1920.png" width="420"> | <img src="screenshots/vergleich-servas/feed_390.png" width="140"> |
| Galerie | <img src="screenshots/vergleich-servas/galerie_1920.png" width="420"> | <img src="screenshots/vergleich-servas/galerie_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich-servas/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich-servas/top_1920.png" width="420"> | <img src="screenshots/vergleich-servas/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich-servas/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich-servas/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich-servas/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich-servas/marken_1920.png" width="420"> | <img src="screenshots/vergleich-servas/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich-servas/familien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/familien_390.png" width="140"> |
| Dashboard | <img src="screenshots/vergleich-servas/dashboard_1920.png" width="420"> | <img src="screenshots/vergleich-servas/dashboard_390.png" width="140"> |
| Gesundheit & Qualität | <img src="screenshots/vergleich-servas/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gesundheit_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich-servas/pack_1920.png" width="420"> | <img src="screenshots/vergleich-servas/pack_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich-servas/wer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/wer_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich-servas/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich-servas/qualitaet_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich-servas/logos_1920.png" width="420"> | <img src="screenshots/vergleich-servas/logos_390.png" width="140"> |
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

- `774a70d` 2026-11-02 13:16 — fix(sc102-p3-1): Fabrik-Kartenkopf Spannen-Badge nicht mehr hart „€/kg-Spanne“, sondern spreadLabel(rs): €/kg-, €/l-Spanne bzw. gemischt g/ml neutral „Grundpreis-Spanne“; Werte/Ranking unverändert (alle 13 same-Gruppen heute g → weiter „€/kg-Spanne“); test_size_unit: Quelltext-Check + 2 Mutationen rot; prepush_gate grün
- `ccb9055` 2026-11-02 11:08 — fix(sc101b-p3-2): Gerichte-Karte €/100 g ohne Packungsgröße und ohne p100g zeigt „–“ statt ppk/10 (25 Zeilen mit ppk = Stück-/Packungspreis, z. B. #111 2,99 € → 29,90 €/100 g unplausibel; 5 davon auf der Karte); ppk/10-Fallback nur noch mit size>0; Werte/Ranking unverändert; test_p100g: Quelltext-Check + neue Mutation rot, Daten-Check alle 25 Zeilen „–“; prepush_gate grün
- `418ca3f` 2026-11-02 10:55 — SC101: Misc Fabrik-Karten zeigen €/l bei ml-Packungen statt hart €/kg (perKgLabel), test_size_unit + Mutation
- `7ed020a` 2026-11-02 10:27 — fix(sc101-p3-2): Gerichte-Karte €/100 g aus p100g statt ppk/10 – keine doppelte Rundung mehr (#77 2,99 €/200 g 1,49→1,50, #123 0,99 €/41 g 2,42→2,41, #221 1,24→1,25); ppk/10 nur noch Fallback ohne p100g; Werte/Ranking unverändert; test_p100g: Quelltext-Check + 2 Mutationen rot; prepush_gate grün
- `eac028d` 2026-11-02 09:52 — fix(sc100-p3-2/3): gemischter Produktvergleich (€/kg neben €/l) vergibt keinen 🏆 und keinen Sieg für die Grundpreis-Zeile, Hinweis „kg und l nicht direkt vergleichbar – kein Sieger“; Wert-Zelle whitespace-nowrap/min-w-16, damit „🏆 7,97 €/kg“ auf 390 px nicht umbricht; Werte unverändert; test_size_unit: Quelltext-Check + 3 Mutationen rot; prepush_gate grün
- `f646263` 2026-11-02 09:27 — fix(sc100-p3-1): €/kg bzw. €/l bei exakt halbem Cent kaufmännisch aufrunden – App-Pass consistentPpk (toPrecision(12) vor Math.round) korrigiert 333 Zeilen um +0,01 (#8 3,19 €/400 g 7,97→7,98, #2143 4,39 €/400 g 10,97→10,98, #2402 44,97→44,98); nur reine Rundungsabweichungen (|ppk−exakt| ≤ 0,005, 0 echte Abweichungen), Preis/Größe/p100g/pPor/Score/Ranking unverändert; test_ppk: Ganzzahl-Orakel, Selftest + 4 Mutationen rot; prepush_gate grün
- `4cac6e6` 2026-11-02 09:05 — fix(sc99-p3-1): Grundpreis bei ml-Packungen „€/l“ statt „€/kg“ – Detail „Packung & Preis“ per perKgLabel (#3221 €/l 10,91, #2722 €/l 16,59), Produktvergleich-Sheet Kopf €/kg | €/l | „€/kg bzw. €/l“ (gemischt) und Wert-Einheit je Zeile; Werte unverändert; test_size_unit: perKgLabel + Quelltext-Check, 3 Mutationen rot; prepush_gate grün
- `2168999` 2026-11-02 08:26 — fix(sc97-p3-5): Anbieter-Limit-Badge auf 390 px unter dem Absatz statt mittendrin – p < sm flex-col, Badge order-last (vorher 80 px Text darunter); Desktop unverändert inline (sm:block/sm:order-none); Werte 12/23/5/0, light kein Hinweis, weg mit „ohne Limit“; e2e_cap_mobile: Abstand Badge-Unterkante/Absatzende ≤ 1 px, alter Code rot (80 px); prepush_gate grün

**servas-ai/food-connectors**

- `7d4eeec` 2026-10-30 17:39 — status: spar-shop broken — SPAR fact-finder channel products_lmos_at removed (HTTP 400), shop pages 403 to non-browser clients (not bypassed)
- `5a5615e` 2026-10-25 15:12 — bauernladen: fairkocht_nutrition() — producer-side per-100 g nutrition for fairkocht rows from fairkocht.at Store API (Atwater gate flags inconsistent tables); offline fixture test; reproduces daten 58c57a6 18/19
- `09680ec` 2026-10-25 14:12 — bofrost: off_gtin() — GTIN from Open Food Facts pack barcodes (article no. embedded 0PPPP69AAAAAC, GS1-validated) only when article no. + net weight match and kcal/protein/fat/carbs per 100 g within ±5%; offline fixture test (236 pass, 3 skipped); reproduces daten a1f5420 6/144
- `e786140` 2026-10-25 13:50 — wiesbauer_gourmet: GTIN from product-page JSON-LD (jsonld_gtin/page_gtin, opt-in fetch(with_gtin=True), GS1-validated, 19/20 meals 2026-10-25); offline fixture test (235 pass)
- `c9b24a3` 2026-10-25 13:09 — gourmet-daheim: fallback dish photos (127 arts) from the official Speisekarte 2026 PDF, repo-hosted in fertiggerichte-daten; 234 tests pass
- `4dcd4bf` 2026-10-25 12:44 — every: GTIN via shopify_gtin per-product JSON (50/50 meals, 2026-10-25)
- `4030f6c` 2026-10-25 12:23 — shopify_gtin: read GS1-valid variant barcodes from public /products/<handle>.json (empty in products.json) for deflorian, kumitzberg, goldblatt, loewenanteil; drop barcodes shared by several products (placeholder pattern); fix 'no GTIN published' docstrings; 3 offline tests (233 pass)
- `7f25e3b` 2026-10-25 11:16 — schmankerl: live Schmankerl Österreich connector (Pamela Plüschke – Salzburg Spezialitäten, Feldkirchen; Shopify reseller, chilled shipping AT/DE/IT/EU) — 9 chilled Innviertel Knödel, Kaspressknödel, Fleischstrudel and canned Gulaschsuppe, MCP tools, 4 offline tests

**servas-ai/fertiggerichte-daten**

- `1e7d5ed` 2026-10-25 15:42 — T1540: nutrition backfill 14 Hartl's Kulinarikum rows (8 myProduct + 6 ADAMAH) from the producer's own hartls-kulinarikum.at Nährwert label images (je 100 g, vision-transcribed; matches myProduct's published Bohnentopf/Puten tables exactly; Atwater ±15%); kJ/kcal label mismatches flagged; 9 Hartl's dishes publish no table
- `58c57a6` 2026-10-25 15:11 — T1509: nutrition backfill 18/19 fairkocht rows (via Bauernladen.at) from the producer's own fairkocht.at product pages (Nährwerte je 100 g; same producer, name, price; Atwater ±15%); Paprikahendl skipped (published 19 kcal inconsistent with macros); Kalbsgulasch/Kalbsragout flagged identical tables; Christöphl/Deflorian publish no nutrition
- `ba14ca9` 2026-10-25 14:43 — T1437: nutrition backfill 24 myProduct multipack rows by identical GTIN (5 dm + 1 Gurkerl retail rows, 18 Open Food Facts; Atwater ±15% check; 4 skipped for OFF name/size mismatch) + Leitgeb's GTIN 4/29 from identical Gurkerl articles (name + 450 g + nutrition); Deflorian 21, Hartl's 17, Wiesbauer 7, SUPPITO 7, Kumitzberg 2 GTINs have no OFF nutrition (404)
- `a1f5420` 2026-10-25 14:12 — T1402: GTIN backfill bofrost* 6/144 via Open Food Facts — pack barcode embeds bofrost article no. (0PPPP69AAAAAC) = bofrost.at article no., name + net weight equal, nutrition ±5% (4 identical/within 4%, 2 OFF without nutrition); 29 article-matched candidates skipped (nutrition/weight mismatch or OFF weight missing); GOURMET Daheim 0/141 (OFF has only 36 GMS GOURMET retail codes, no match)
- `aebbe62` 2026-10-25 13:50 — T1339: GTIN backfill 27 rows — Wiesbauer Gourmet 19/20 from product-page JSON-LD gtin, Egle 8/31 via Open Food Facts (own GS1 prefix 4262468; 2 nutrition-identical, 2 photo-confirmed, unique names); WooCommerce Leitgeb/Steira Markt/Draxler publish no GTIN (Store API global_unique_id null)
- `7422341` 2026-10-25 13:08 — T1305: GOURMET Daheim photos 8→127/141 — 119 official dish photos from the Mahlzeit Linz Speisekarte 2026 PDF, matched by order number position (127/127 unique), vision gate passed, stored under images/gourmet_daheim/
- `99cde6b` 2026-10-25 12:44 — T1241: GTIN backfill 57 rows — every. 50/50 from Shopify per-product JSON, SUPPITO 7 via identical Gurkerl product+weight (Kürbis 500/510 g mismatches skipped); Gurkerl publishes no SUPPITO nutrition
- `eaa7126` 2026-10-25 12:21 — T1207: GTIN backfill 76 rows from Shopify per-product JSON (Löwenanteil 17, Deflorian 25, PrepMyMeal 13, Goldblatt 8, LiveFresh 7, Kumitzberg 5, Schmankerl 1) + 7 nutrition fills via identical GTIN (Deflorian 6 via MPreis/OFF, Schmankerl FELIX Gulaschsuppe); Wagyuhof placeholder barcodes + Deflorian shared Erdbeer/Zwetschken barcode skipped

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
