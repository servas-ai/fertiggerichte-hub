# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-13 01:26 UTC via `./run_all.sh` (stündlich).

**Connectors:** 10 ✅ / 4 ❌ / 7 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 1293

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
| ✅ | `dm` | dm | 3 | 2.62 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-13T01:25:31Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 6.58 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-13T01:25:35Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 0.79 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 16.1 € | 2026-10-13T01:25:42Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 2.59 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-13T01:25:43Z |
| ✅ | `hofer` | HOFER | 3 | 2.63 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-13T01:25:47Z |
| ✅ | `mpreis` | MPREIS | 3 | 2.79 s | AIA Puten Gulasch · 6.5 € | 2026-10-13T01:26:10Z |
| ✅ | `penny` | PENNY | 2 | 7.12 s | [Schweinefleisch für Reisfleisch/Gulasch](https://www.penny.at/produkte/schweinefleisch-fuer-reisfleischgulasch-78544771) · 3.99 € | 2026-10-13T01:26:27Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 5.34 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-13T01:26:34Z |
| ✅ | `spar` | SPAR/INTERSPAR | 3 | 2.72 s | Baron de Sel Gourmet Gulasch Bio 55g · 4.99 € | 2026-10-13T01:26:40Z |
| ✅ | `unimarkt` | Unimarkt | 3 | 2.88 s | [Felix Erdäpfelgulasch](/Felix-Erdaepfelgulasch-3692) · 5.39 € | 2026-10-13T01:26:44Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-13T01:25:23Z |
| ❌ | `billa` | BILLA | 0 | 7.74 s | `0 Treffer` | 2026-10-13T01:25:23Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-13T01:25:31Z |
| 📇 | `fittogo` | Fit to Go | 0 | 0.0 s |  | 2026-10-13T01:25:35Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-13T01:25:35Z |
| ❌ | `lidl` | Lidl | 0 | 12.57 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-13T01:25:51Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-13T01:26:03Z |
| ❌ | `livefresh` | Online: LiveFresh | 0 | 6.33 s | `0 Treffer` | 2026-10-13T01:26:04Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-13T01:26:10Z |
| ❌ | `off` | Open Food Facts | 0 | 12.73 s | `HTTPError: HTTP Error 503: Service Temporarily Unavailable` | 2026-10-13T01:26:14Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-13T01:26:48Z |

## Datensatz

**1293 Produkte** · Tabellen: brand_tree 8, companies 76, establishments 4706, logos 135, nutrition 736, online_mealprep 96, online_providers 3, prices 1148, producer_quality 4, producers 22, products 1293

| Abdeckung | % |
|---|---|
| nutrition | 56.8 |
| price | 88.8 |
| photo | 77.1 |
| producer | 42.2 |
| brand | 69.2 |
| logos_total | 135 |

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|
| Spar | 531 |
| Billa | 494 |
| Hofer | 139 |
| unbekannt (OFF) | 62 |
| Fit to Go | 24 |
| dm | 23 |
| Lidl | 18 |
| Penny | 2 |

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|
| Unklar (keine Lagerangabe) | 479 |
| Kühlregal (Menüschale/frisch) | 232 |
| Trocken/Instant | 205 |
| Tiefkühl (TK) | 178 |
| Dose/Konserve | 167 |
| Glas | 16 |
| Sous-vide (vakuum) | 11 |
| Beutel ungekühlt (Retort-Pouch) | 5 |

</details>

## Screenshots

### Fertiggerichte-Vergleich

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich/home_1920.png" width="420"> | <img src="screenshots/vergleich/home_390.png" width="140"> |
| 🍲 Gericht vergleichen | <img src="screenshots/vergleich/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich/top_1920.png" width="420"> | <img src="screenshots/vergleich/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich/kategorien_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich/marken_1920.png" width="420"> | <img src="screenshots/vergleich/marken_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich/filialen_1920.png" width="420"> | <img src="screenshots/vergleich/filialen_390.png" width="140"> |
| 🩺 Gesundheit & Qualität | <img src="screenshots/vergleich/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich/gesundheit_390.png" width="140"> |
| Analyse | <img src="screenshots/vergleich/analyse_1920.png" width="420"> | <img src="screenshots/vergleich/analyse_390.png" width="140"> |
| Preis vs. Protein | <img src="screenshots/vergleich/scatter_1920.png" width="420"> | <img src="screenshots/vergleich/scatter_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich/pack_1920.png" width="420"> | <img src="screenshots/vergleich/pack_390.png" width="140"> |
| Hersteller | <img src="screenshots/vergleich/hersteller-seiten_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller-seiten_390.png" width="140"> |
| 🕵️ Wer steckt dahinter? | <img src="screenshots/vergleich/wer_1920.png" width="420"> | <img src="screenshots/vergleich/wer_390.png" width="140"> |
| 🏢 Firmenvergleich | <img src="screenshots/vergleich/firmen_1920.png" width="420"> | <img src="screenshots/vergleich/firmen_390.png" width="140"> |
| Marken-Matrix | <img src="screenshots/vergleich/matrix_1920.png" width="420"> | <img src="screenshots/vergleich/matrix_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich/logos_1920.png" width="420"> | <img src="screenshots/vergleich/logos_390.png" width="140"> |
| 🕸️ Netz 3D | <img src="screenshots/vergleich/netz_1920.png" width="420"> | <img src="screenshots/vergleich/netz_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller_390.png" width="140"> |
| Wochenplaner | <img src="screenshots/vergleich/planer_1920.png" width="420"> | <img src="screenshots/vergleich/planer_390.png" width="140"> |
| Kombi-Ideen | <img src="screenshots/vergleich/kombi_1920.png" width="420"> | <img src="screenshots/vergleich/kombi_390.png" width="140"> |
| Fit to Go vs. Supermarkt | <img src="screenshots/vergleich/ftg_1920.png" width="420"> | <img src="screenshots/vergleich/ftg_390.png" width="140"> |
| Multipot-Pro Garzeiten | <img src="screenshots/vergleich/multipot_1920.png" width="420"> | <img src="screenshots/vergleich/multipot_390.png" width="140"> |
| Methodik & Quellen | <img src="screenshots/vergleich/methodik_1920.png" width="420"> | <img src="screenshots/vergleich/methodik_390.png" width="140"> |

### Fertiggerichte-Vergleich (servas-ai Pages)

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich-servas/home_1920.png" width="420"> | <img src="screenshots/vergleich-servas/home_390.png" width="140"> |
| Alle Gerichte | <img src="screenshots/vergleich-servas/alle_1920.png" width="420"> | <img src="screenshots/vergleich-servas/alle_390.png" width="140"> |
| 🍲 Gericht vergleichen | <img src="screenshots/vergleich-servas/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich-servas/top_1920.png" width="420"> | <img src="screenshots/vergleich-servas/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich-servas/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kategorien_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich-servas/marken_1920.png" width="420"> | <img src="screenshots/vergleich-servas/marken_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich-servas/filialen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/filialen_390.png" width="140"> |
| 🩺 Gesundheit & Qualität | <img src="screenshots/vergleich-servas/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gesundheit_390.png" width="140"> |
| Analyse | <img src="screenshots/vergleich-servas/analyse_1920.png" width="420"> | <img src="screenshots/vergleich-servas/analyse_390.png" width="140"> |
| Preis vs. Protein | <img src="screenshots/vergleich-servas/scatter_1920.png" width="420"> | <img src="screenshots/vergleich-servas/scatter_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich-servas/pack_1920.png" width="420"> | <img src="screenshots/vergleich-servas/pack_390.png" width="140"> |
| Hersteller | <img src="screenshots/vergleich-servas/hersteller-seiten_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller-seiten_390.png" width="140"> |
| 🕵️ Wer steckt dahinter? | <img src="screenshots/vergleich-servas/wer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/wer_390.png" width="140"> |
| Marken-Matrix | <img src="screenshots/vergleich-servas/matrix_1920.png" width="420"> | <img src="screenshots/vergleich-servas/matrix_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich-servas/logos_1920.png" width="420"> | <img src="screenshots/vergleich-servas/logos_390.png" width="140"> |
| 🕸️ Netz 3D | <img src="screenshots/vergleich-servas/netz_1920.png" width="420"> | <img src="screenshots/vergleich-servas/netz_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich-servas/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller_390.png" width="140"> |
| Wochenplaner | <img src="screenshots/vergleich-servas/planer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/planer_390.png" width="140"> |
| Kombi-Ideen | <img src="screenshots/vergleich-servas/kombi_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kombi_390.png" width="140"> |
| Fit to Go vs. Supermarkt | <img src="screenshots/vergleich-servas/ftg_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ftg_390.png" width="140"> |
| Multipot-Pro Garzeiten | <img src="screenshots/vergleich-servas/multipot_1920.png" width="420"> | <img src="screenshots/vergleich-servas/multipot_390.png" width="140"> |
| Methodik & Quellen | <img src="screenshots/vergleich-servas/methodik_1920.png" width="420"> | <img src="screenshots/vergleich-servas/methodik_390.png" width="140"> |

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

- `047595e` 2026-10-13 01:23 — Nutri-Score 2023 (offiziell/berechnet), NOVA, Zusatzstoffe via food-connectors nutri
- `c0a06ae` 2026-10-13 01:15 — Redesign: ProductCard X-artig – großes Foto, weniger Badges
- `d7c36f4` 2026-10-13 01:12 — Verpackungen: X-artig minimal, monochrom + Akzent
- `bade6f0` 2026-10-13 01:08 — fix: Sheet per Portal (Filter-Panel), Filial-Marker-Logos
- `e7bfbfa` 2026-10-13 01:03 — feat(verpackungen): Dashboard + packaging_v2
- `d41c735` 2026-10-13 01:01 — Redesign: X-artig minimal, shadcn Tokens/Komponenten, Inter, monochrom + ein Akzent
- `49d8e54` 2026-10-13 00:53 — feat(verpackungen): Dashboard mit KPI-Kacheln, Boxplot, Radar, MHD-Zeitstrahl, Top 5 + Klassifikation v2
- `200c19b` 2026-10-13 00:50 — Wer steckt dahinter? view + brand_tree.json

**servas-ai/food-connectors**

- `fc9fe93` 2026-10-13 01:19 — nutri: OFF Nutri-Score/NOVA/Eco-Score/additives, USDA FDC, CIQUAL + catalog; local Nutri-Score 2023; CLI food nutri/nutriscore; MCP tools
- `67cf932` 2026-10-13 01:18 — feat: online meal-prep adapters (PrepMyMeal, LiveFresh, Gourmetfein)
- `a9c358e` 2026-10-13 01:05 — food-connectors 0.1: adapters, CLI, MCP server, tests

**servas-ai/fertiggerichte-daten**

- `d2e35b2` 2026-10-13 01:19 — data: online meal-prep products, online providers, producer quality profiles
- `d6e1bf2` 2026-10-13 01:06 — Offener Datensatz Fertiggerichte AT: products, prices, nutrition, producers, companies (GLEIF), establishments (ÖVIS), brand_tree, logos + datapackage, validation, company CLI/MCP

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
