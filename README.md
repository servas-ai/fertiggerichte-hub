# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-13 09:55 UTC via `./run_all.sh` (stündlich).

**Connectors:** 14 ✅ / 1 ❌ / 10 📇 catalog-only · **Apps:** 0/3 live · **Produkte im Datensatz:** 2360

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ❌ | 0 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ❌ | 0 | 0 | 0 |
| Einkaufsanalyse | https://servas-ai.github.io/einkaufsanalyse/ | ❌ | 0 | 0 | 0 |

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
| ✅ | `billa` | BILLA | 3 | 0.93 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-13T09:54:14Z |
| ✅ | `dm` | dm | 3 | 2.75 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-13T09:54:15Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 5.75 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-13T09:54:19Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 0.77 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 16.1 € | 2026-10-13T09:54:25Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 2.68 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-13T09:54:26Z |
| ✅ | `hofer` | HOFER | 3 | 2.67 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-13T09:54:30Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.27 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-13T09:54:47Z |
| ✅ | `mpreis` | MPREIS | 3 | 2.8 s | AIA Puten Gulasch · 6.5 € | 2026-10-13T09:54:50Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 8.3 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-10-13T09:54:54Z |
| ✅ | `off` | Open Food Facts | 3 | 1.78 s | [Gulasch (Rind)](https://world.openfoodfacts.org/product/4099200121543) | 2026-10-13T09:55:02Z |
| ✅ | `penny` | PENNY | 2 | 5.9 s | [Schweinefleisch für Reisfleisch/Gulasch](https://www.penny.at/produkte/schweinefleisch-fuer-reisfleischgulasch-78544771) · 3.99 € | 2026-10-13T09:55:04Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 7.49 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-13T09:55:10Z |
| ✅ | `spar` | SPAR/INTERSPAR | 3 | 2.64 s | Baron de Sel Gourmet Gulasch Bio 55g · 4.99 € | 2026-10-13T09:55:18Z |
| ✅ | `unimarkt` | Unimarkt | 3 | 2.83 s | [Felix Erdäpfelgulasch](/Felix-Erdaepfelgulasch-3692) · 5.39 € | 2026-10-13T09:55:22Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-13T09:54:14Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-13T09:54:15Z |
| 📇 | `denns` | denn's BioMarkt | 0 | 0.0 s |  | 2026-10-13T09:54:15Z |
| 📇 | `fittogo` | Fit to Go | 0 | 0.0 s |  | 2026-10-13T09:54:19Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-13T09:54:19Z |
| ❌ | `lidl` | Lidl | 0 | 12.95 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-13T09:54:34Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-13T09:54:47Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-13T09:54:50Z |
| 📇 | `nah-frisch` | Nah&Frisch | 0 | 0.0 s |  | 2026-10-13T09:55:02Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-13T09:55:26Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-13T09:55:26Z |

## Datensatz

**2360 Produkte** · Tabellen: brand_tree 8, companies 83, establishments 4706, logos 156, nutrition 1596, online_mealprep 96, online_providers 3, prices 2034, producer_quality 4, producers 22, products 2360, stores 498

| Abdeckung | % |
|---|---|
| nutrition | 67.6 |
| price | 86.2 |
| photo | 92.9 |
| producer | 34.6 |
| brand | 85.8 |
| logos_total | 156 |

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|
| Billa | 618 |
| Spar | 592 |
| Gurkerl | 381 |
| Hofer | 224 |
| MPreis | 174 |
| unbekannt (OFF) | 135 |
| PrepMyMeal | 90 |
| Lidl | 40 |
| Unimarkt | 29 |
| dm | 24 |
| Fit to Go | 24 |
| Penny | 17 |
| LiveFresh | 10 |
| FitTaste | 2 |

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|
| Unklar (keine Lagerangabe) | 1063 |
| Kühlregal (Menüschale/frisch) | 341 |
| Tiefkühl (TK) | 328 |
| Dose/Konserve | 317 |
| Trocken/Instant | 268 |
| Glas | 16 |
| Sous-vide (vakuum) | 14 |
| Beutel ungekühlt (Retort-Pouch) | 13 |

</details>

## Screenshots

## Changelog (letzte Commits)

**servas-ai/fertiggerichte-vergleich**

- `3ebe8fb` 2026-10-13 09:53 — hourly 2026-10-13T09: +23 meals (Gurkerl GAON/Bibigo/Hengstenberg/Virtshaus + MPreis soups), dm photos 1→22, brand tree GAON/Hengstenberg/Mochi, Dashboard Foto-Abdeckung chart
- `5fbb1db` 2026-10-13 09:35 — Daten-Squad 2026-10-13T09: dm photos 1→22/24 (dm.at product JSON via sitemap DAN, Lotao Shopify, OFF strict), Hofer sub-brand logos wired (Primana 43 rows, Asia Green Garden 12 rows), Lotao logo (official), Aldi CDN probe for 22 Hofer Eigenmarken = 403 evidence
- `5952763` 2026-10-13 04:41 — hourly 2026-10-13T04: +25 Gurkerl meals (Pappudia, Mochi Ramen, HOFMANNs TK, Freshery, Bonduelle, M&S) via food-connectors gurkerl enrich, brand tree Hofmann→Compass Group, Dashboard Preis-Aktualität je Laden (shadcn Chart)
- `d06fb05` 2026-10-13 04:36 — Hofer photos 90→122 OFF strict + heisse price provenance
- `555e27d` 2026-10-13 03:52 — Spar photos 100% via heisse CDN (228 verified)
- `a09149e` 2026-10-13 03:37 — hourly 2026-10-13T03: +74 MPreis meals via mpreis-shop (food-connectors), OFF EAN nutri×5, brand tree MPreis/AIA/Youcook/Deflorian/…, Abdeckung Lücken-Spotlight + Ident-Kennz. cards (shadcn Progress)
- `df59df5` 2026-10-13 03:25 — logos: +6 verified official logos (PrepMyMeal, Gurkerl, LiveFresh, Gissinger, Suppito, Zátiší) — 47 more products with logo
- `ebe13e3` 2026-10-13 03:08 — data: hourly sync

**servas-ai/food-connectors**

- `3772004` 2026-10-13 04:34 — docs(hofer): note OFF/Aldi CDN photo path; Akamai blocks hofer.at
- `0980843` 2026-10-13 04:00 — fix(livefresh): fetch(limit=N) must filter bowls before truncating
- `b32e017` 2026-10-13 03:50 — feat(spar): attach CDN image_url from heisse article id
- `32abd1c` 2026-10-13 03:17 — catalog: unimarkt-shop note precision (sampled slugs)
- `cde29e5` 2026-10-13 03:16 — catalog: unimarkt-shop verified CLOSED (shop.unimarkt.at = 'Service eingestellt' splash, all slugs 302 -> /; chain left retail 2026); unimarkt dump notes = history only; test
- `b3577e9` 2026-10-13 02:53 — feat(mpreis-shop): live MPreis webshop connector (sitemap + category pages + product JSON-LD: price, GTIN, image, pack size, nutrition, ingredients), CLI + MCP mpreis_product, fixture test
- `d5b2327` 2026-10-13 02:29 — feat(gurkerl): walk ready-meal categories via category API, batch prices+stock, EAN/producer from composition; tests
- `0876e1d` 2026-10-13 02:28 — test: remove remaining orphaned gurkerl category live test

**servas-ai/fertiggerichte-daten**

- `5fdc6da` 2026-10-13 09:36 — data: dm photos 1→22/24 (dm.at product JSON via sitemap DAN, Lotao Shopify, OFF strict; GET-verified), logos: Primana + Asia Green Garden wired, Lotao added, Aldi CDN/Commons/Lidl logo probe evidence; resync with app (2360 products)
- `7343416` 2026-10-13 04:37 — scripts: enrich_hofer_images also writes fertig overlay
- `81ef711` 2026-10-13 04:35 — data: Hofer images overlay for fertig score.py rebuilds
- `45cf7a9` 2026-10-13 04:34 — data: Hofer photos 90→122 via strict OFF match; refresh heisse prices
- `722cab2` 2026-10-13 03:52 — export: refresh after Spar CDN photo deploy (2335 products, 2115 photos)
- `dba60fd` 2026-10-13 03:50 — data: Spar photos 364→592 (100%) via heisse→cdn1.interspar.at
- `5319516` 2026-10-13 03:23 — logos: Wiesbauer brand alias (4 products resolve to verified official logo)
- `30de9b9` 2026-10-13 03:22 — logos: +6 official logos (PrepMyMeal, Gurkerl, LiveFresh, Gissinger, Suppito, Zátiší) + fit2go.meals brand alias — vision gate pass, source URLs from official sites

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
