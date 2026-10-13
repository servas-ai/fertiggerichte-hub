# 🥘 Fertiggerichte-Hub

Zentraler Index & Live-Status aller Fertiggerichte-Projekte (servas-ai). **Automatisch generiert:** 2026-10-13 13:02 UTC via `./run_all.sh` (stündlich).

**Connectors:** 15 ✅ / 1 ❌ / 10 📇 catalog-only · **Apps:** 3/3 live · **Produkte im Datensatz:** 2542

## Apps

| App | URL | Live | Tabs getestet | Konsolen-Fehler | Kaputte Bilder |
|---|---|---|---|---|---|
| Fertiggerichte-Vergleich | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | ✅ | 30 | 0 | 0 |
| Fertiggerichte-Vergleich (servas-ai Pages) | https://servas-ai.github.io/fertiggerichte-vergleich/ | ✅ | 30 | 0 | 0 |
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
| ✅ | `billa` | BILLA | 3 | 0.97 s | [MAGGI Fix für Gulasch](https://shop.billa.at/produkte/maggi-fix-fuer-gulasch-0056152) · 1.49 € | 2026-10-13T13:00:37Z |
| ✅ | `dm` | dm | 3 | 5.38 s | [babylove Menü Kartoffeltopf mit Rindergulasch ab d](https://www.dm.at/p/d/1602887/babylove-menue-kartoffeltopf-mit-rindergulasch-ab-dem-8-monat) · 1.15 € | 2026-10-13T13:00:38Z |
| ✅ | `dm-heisse` | dm | 3 | 2.81 s | HiPP Menü Spätzle mit Gulasch ab 8 Monaten, 220 g · 1.75 € | 2026-10-13T13:00:44Z |
| ✅ | `gourmetfein` | Online: Gourmetfein | 3 | 7.19 s | [Weißwurst 1,8kg](https://shop.gourmetfein.com/products/weisswurst-1-8kg) · 24.9 € | 2026-10-13T13:00:48Z |
| ✅ | `gurkerl` | Gurkerl.at | 3 | 0.89 s | [AMA Kalb Rosé Austria Gulasch geschnitten](https://www.gurkerl.at/22932-ama-kalb-rose-austria-gulasch-geschnitten) · 16.1 € | 2026-10-13T13:00:55Z |
| ✅ | `heisse-preise` | heisse-preise.io | 3 | 2.72 s | [Ager Hirschgulasch geschnitten](ager-hirschgulasch-geschnitten-00730647) · 11.99 € | 2026-10-13T13:00:56Z |
| ✅ | `hofer` | HOFER | 3 | 2.78 s | [GENUSS 100% AUS ÖSTERREICH Rindsgulasch 1kg](sortiment/GENUSS-100-AUS-OSTERREICH-Rindsgulasch-1kg) · 19.98 € | 2026-10-13T13:01:01Z |
| ✅ | `livefresh` | Online: LiveFresh | 3 | 2.5 s | [Pasta Cheesy Spinat – Protein Bowl](https://livefresh.at/products/pasta-cheesy-spinat-400g) · 5.99 € | 2026-10-13T13:01:19Z |
| ✅ | `mpreis` | MPREIS | 3 | 2.73 s | AIA Puten Gulasch · 6.5 € | 2026-10-13T13:01:21Z |
| ✅ | `mpreis-shop` | MPreis | 3 | 9.42 s | [Basis Gulasch](https://www.mpreis.at/shop/p/knorr-basis-gulasch-282001) · 1.39 € | 2026-10-13T13:01:26Z |
| ✅ | `off` | Open Food Facts | 3 | 8.86 s | [Gulasch (Rind)](https://world.openfoodfacts.org/product/4099200121543) | 2026-10-13T13:01:35Z |
| ✅ | `penny` | PENNY | 2 | 7.09 s | [Schweinefleisch für Reisfleisch/Gulasch](https://www.penny.at/produkte/schweinefleisch-fuer-reisfleischgulasch-78544771) · 3.99 € | 2026-10-13T13:01:44Z |
| ✅ | `prepmymeal` | Online: PrepMyMeal | 3 | 10.86 s | [CH: Gemüse Lasagne](https://prepmymeal.at/products/ch-gemuse-lasagne-3) · 14.5 € | 2026-10-13T13:01:51Z |
| ✅ | `spar` | SPAR/INTERSPAR | 3 | 3.12 s | Baron de Sel Gourmet Gulasch Bio 55g · 4.99 € | 2026-10-13T13:02:02Z |
| ✅ | `unimarkt` | Unimarkt | 3 | 2.92 s | [Felix Erdäpfelgulasch](/Felix-Erdaepfelgulasch-3692) · 5.39 € | 2026-10-13T13:02:07Z |
| 📇 | `adeg` | ADEG | 0 | 0.0 s |  | 2026-10-13T13:00:37Z |
| 📇 | `bio-kistl` | Biohof Achleitner / Bio-Kistl OÖ | 0 | 0.0 s |  | 2026-10-13T13:00:38Z |
| 📇 | `denns` | denn's BioMarkt | 0 | 0.0 s |  | 2026-10-13T13:00:38Z |
| 📇 | `fittogo` | Fit to Go | 0 | 0.0 s |  | 2026-10-13T13:00:48Z |
| 📇 | `foodora-market` | foodora market (Dmart) | 0 | 0.0 s |  | 2026-10-13T13:00:48Z |
| ❌ | `lidl` | Lidl | 0 | 13.39 s | `HTTPError: HTTP Error 401: Unauthorized` | 2026-10-13T13:01:05Z |
| 📇 | `lieferando-shops` | Lieferando Shops | 0 | 0.0 s |  | 2026-10-13T13:01:18Z |
| 📇 | `mjam` | mjam (now foodora) | 0 | 0.0 s |  | 2026-10-13T13:01:21Z |
| 📇 | `nah-frisch` | Nah&Frisch | 0 | 0.0 s |  | 2026-10-13T13:01:35Z |
| 📇 | `unimarkt-shop` | Unimarkt (UNIONLINE Shop) | 0 | 0.0 s |  | 2026-10-13T13:02:11Z |
| 📇 | `wokostswas` | wokostswas.at | 0 | 0.0 s |  | 2026-10-13T13:02:11Z |

## Datensatz

**2542 Produkte** · Tabellen: brand_tree 8, companies 133, establishments 4706, logos 223, nutrition 1789, online_mealprep 96, online_providers 3, prices 2216, producer_quality 4, producers 22, products 2542, stores 498

| Abdeckung | % |
|---|---|
| nutrition | 70.3 |
| price | 87.2 |
| photo | 93.4 |
| producer | 36.0 |
| brand | 87.3 |
| logos_total | 223 |

<details><summary>Produkte nach Kette</summary>

| Kette | Anzahl |
|---|---|
| Billa | 670 |
| Spar | 592 |
| Gurkerl | 464 |
| Hofer | 224 |
| MPreis | 211 |
| unbekannt (OFF) | 135 |
| PrepMyMeal | 91 |
| Lidl | 40 |
| dm | 33 |
| Unimarkt | 29 |
| Fit to Go | 24 |
| Penny | 17 |
| LiveFresh | 10 |
| FitTaste | 2 |

</details>

<details><summary>Produkte nach Fertigstufe/Lagerung</summary>

| Lagerung | Anzahl |
|---|---|
| Unklar (keine Lagerangabe) | 1063 |
| Tiefkühl (TK) | 449 |
| Kühlregal (Menüschale/frisch) | 377 |
| Dose/Konserve | 334 |
| Trocken/Instant | 274 |
| Glas | 18 |
| Sous-vide (vakuum) | 14 |
| Beutel ungekühlt (Retort-Pouch) | 13 |

</details>

## Screenshots

### Fertiggerichte-Vergleich

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich/home_1920.png" width="420"> | <img src="screenshots/vergleich/home_390.png" width="140"> |
| Feed | <img src="screenshots/vergleich/feed_1920.png" width="420"> | <img src="screenshots/vergleich/feed_390.png" width="140"> |
| Galerie | <img src="screenshots/vergleich/galerie_1920.png" width="420"> | <img src="screenshots/vergleich/galerie_390.png" width="140"> |
| Vergleichs-Board | <img src="screenshots/vergleich/board_1920.png" width="420"> | <img src="screenshots/vergleich/board_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich/top_1920.png" width="420"> | <img src="screenshots/vergleich/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich/marken_1920.png" width="420"> | <img src="screenshots/vergleich/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich/familien_1920.png" width="420"> | <img src="screenshots/vergleich/familien_390.png" width="140"> |
| Dashboard | <img src="screenshots/vergleich/dashboard_1920.png" width="420"> | <img src="screenshots/vergleich/dashboard_390.png" width="140"> |
| Gesundheit & Qualität | <img src="screenshots/vergleich/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich/gesundheit_390.png" width="140"> |
| Analyse | <img src="screenshots/vergleich/analyse_1920.png" width="420"> | <img src="screenshots/vergleich/analyse_390.png" width="140"> |
| Preis vs. Protein | <img src="screenshots/vergleich/scatter_1920.png" width="420"> | <img src="screenshots/vergleich/scatter_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich/pack_1920.png" width="420"> | <img src="screenshots/vergleich/pack_390.png" width="140"> |
| Marken-Matrix | <img src="screenshots/vergleich/matrix_1920.png" width="420"> | <img src="screenshots/vergleich/matrix_390.png" width="140"> |
| Hersteller | <img src="screenshots/vergleich/hersteller-seiten_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller-seiten_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich/wer_1920.png" width="420"> | <img src="screenshots/vergleich/wer_390.png" width="140"> |
| Firmenvergleich | <img src="screenshots/vergleich/firmen_1920.png" width="420"> | <img src="screenshots/vergleich/firmen_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich/qualitaet_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich/logos_1920.png" width="420"> | <img src="screenshots/vergleich/logos_390.png" width="140"> |
| Netz 3D | <img src="screenshots/vergleich/netz_1920.png" width="420"> | <img src="screenshots/vergleich/netz_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich/filialen_1920.png" width="420"> | <img src="screenshots/vergleich/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich/online_1920.png" width="420"> | <img src="screenshots/vergleich/online_390.png" width="140"> |
| Wochenplaner | <img src="screenshots/vergleich/planer_1920.png" width="420"> | <img src="screenshots/vergleich/planer_390.png" width="140"> |
| Kombi-Ideen | <img src="screenshots/vergleich/kombi_1920.png" width="420"> | <img src="screenshots/vergleich/kombi_390.png" width="140"> |
| Fit to Go vs. Supermarkt | <img src="screenshots/vergleich/ftg_1920.png" width="420"> | <img src="screenshots/vergleich/ftg_390.png" width="140"> |
| Multipot-Pro Garzeiten | <img src="screenshots/vergleich/multipot_1920.png" width="420"> | <img src="screenshots/vergleich/multipot_390.png" width="140"> |

### Fertiggerichte-Vergleich (servas-ai Pages)

| Tab | Desktop 1920 | Mobil 390 |
|---|---|---|
| home | <img src="screenshots/vergleich-servas/home_1920.png" width="420"> | <img src="screenshots/vergleich-servas/home_390.png" width="140"> |
| Feed | <img src="screenshots/vergleich-servas/feed_1920.png" width="420"> | <img src="screenshots/vergleich-servas/feed_390.png" width="140"> |
| Galerie | <img src="screenshots/vergleich-servas/galerie_1920.png" width="420"> | <img src="screenshots/vergleich-servas/galerie_390.png" width="140"> |
| Vergleichs-Board | <img src="screenshots/vergleich-servas/board_1920.png" width="420"> | <img src="screenshots/vergleich-servas/board_390.png" width="140"> |
| Gericht vergleichen | <img src="screenshots/vergleich-servas/gerichte_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gerichte_390.png" width="140"> |
| Top-Listen | <img src="screenshots/vergleich-servas/top_1920.png" width="420"> | <img src="screenshots/vergleich-servas/top_390.png" width="140"> |
| Kategorien | <img src="screenshots/vergleich-servas/kategorien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/kategorien_390.png" width="140"> |
| Marken-Profil | <img src="screenshots/vergleich-servas/markenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/markenprofil_390.png" width="140"> |
| Laden-Profil | <img src="screenshots/vergleich-servas/ladenprofil_1920.png" width="420"> | <img src="screenshots/vergleich-servas/ladenprofil_390.png" width="140"> |
| Marken | <img src="screenshots/vergleich-servas/marken_1920.png" width="420"> | <img src="screenshots/vergleich-servas/marken_390.png" width="140"> |
| Markenfamilien | <img src="screenshots/vergleich-servas/familien_1920.png" width="420"> | <img src="screenshots/vergleich-servas/familien_390.png" width="140"> |
| Dashboard | <img src="screenshots/vergleich-servas/dashboard_1920.png" width="420"> | <img src="screenshots/vergleich-servas/dashboard_390.png" width="140"> |
| Gesundheit & Qualität | <img src="screenshots/vergleich-servas/gesundheit_1920.png" width="420"> | <img src="screenshots/vergleich-servas/gesundheit_390.png" width="140"> |
| Analyse | <img src="screenshots/vergleich-servas/analyse_1920.png" width="420"> | <img src="screenshots/vergleich-servas/analyse_390.png" width="140"> |
| Preis vs. Protein | <img src="screenshots/vergleich-servas/scatter_1920.png" width="420"> | <img src="screenshots/vergleich-servas/scatter_390.png" width="140"> |
| Verpackungen | <img src="screenshots/vergleich-servas/pack_1920.png" width="420"> | <img src="screenshots/vergleich-servas/pack_390.png" width="140"> |
| Marken-Matrix | <img src="screenshots/vergleich-servas/matrix_1920.png" width="420"> | <img src="screenshots/vergleich-servas/matrix_390.png" width="140"> |
| Hersteller | <img src="screenshots/vergleich-servas/hersteller-seiten_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller-seiten_390.png" width="140"> |
| Wer steckt dahinter? | <img src="screenshots/vergleich-servas/wer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/wer_390.png" width="140"> |
| Firmenvergleich | <img src="screenshots/vergleich-servas/firmen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/firmen_390.png" width="140"> |
| Hersteller-Qualität | <img src="screenshots/vergleich-servas/qualitaet_1920.png" width="420"> | <img src="screenshots/vergleich-servas/qualitaet_390.png" width="140"> |
| Logos | <img src="screenshots/vergleich-servas/logos_1920.png" width="420"> | <img src="screenshots/vergleich-servas/logos_390.png" width="140"> |
| Netz 3D | <img src="screenshots/vergleich-servas/netz_1920.png" width="420"> | <img src="screenshots/vergleich-servas/netz_390.png" width="140"> |
| Läden & Werke | <img src="screenshots/vergleich-servas/hersteller_1920.png" width="420"> | <img src="screenshots/vergleich-servas/hersteller_390.png" width="140"> |
| Filialen in der Nähe | <img src="screenshots/vergleich-servas/filialen_1920.png" width="420"> | <img src="screenshots/vergleich-servas/filialen_390.png" width="140"> |
| Online-Anbieter | <img src="screenshots/vergleich-servas/online_1920.png" width="420"> | <img src="screenshots/vergleich-servas/online_390.png" width="140"> |
| Wochenplaner | <img src="screenshots/vergleich-servas/planer_1920.png" width="420"> | <img src="screenshots/vergleich-servas/planer_390.png" width="140"> |
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

- `7b49e37` 2026-10-13 12:52 — logos: +13 company/producer logos (Firmen 111/133 with logo)
- `657dac8` 2026-10-13 12:36 — hourly 2026-10-13T12: +52 BILLA meals (Dr. Oetker Ristorante/Tradizionale/La Mia Grande/Suprema, Gustavo Gusto, Wagner Steinofen/Piccolinis, Freda High Protein, iglo Holy Slice/Krautfleckerl, Namdong K-Noodles, Coppenrath & Wiese Apfelstrudel, Frosta), pizza-pesto stage fix, brand tree Coppenrath→Oetker/Freda→siu foods/Namdong→Unilever, Dashboard 'Gleiches Produkt – wo am günstigsten?' cross-store price compare
- `a5ba738` 2026-10-13 12:21 — Daten-Squad 2026-10-13T12: +16 vision-gated brand logos (YOUCOOK, Andros, deFLORiAN, AIA, Indomie, Arla, Thiriet, Hammermühle, Landtmann's, Ashoka, Strauss, Danke Bauer, Shan'shi, Riso Gallo, Esterhazy, Galbani) + Iglo case aliases; strict logo-less 154→139 brands / 430→368 products
- `3d60a5b` 2026-10-13 11:58 — Daten-Squad 2026-10-13T11b: +30 vision-gated brand logos (NÖM, Danone, Bibigo, Zurück zum Ursprung, Meica, Heinz, Hilcona, Hengstenberg, Kotányi, NENI, Golfera, Stadtküche, Jeden Tag, Gü …) + 14 brand aliases
- `90f271d` 2026-10-13 11:53 — hourly 2026-10-13T11: +72 meals (Gurkerl 38 / MPreis 34: Wagner, Dr. Oetker Ristorante/Tradizionale, Gustavo Gusto, Alnatura, Iglo Holy Slice, followfood, Frosta Nasi Goreng), MPreis per-portion nutrition fix (19 rows corrected), logos Gustavo Gusto/Morgentau + Samyang alias, brand tree European Pizza Group/Oetker/followfood/Gustavo Gusto, Dashboard Protein-Effizienz Bestenliste + Makro-Mix chart
- `8c5cda5` 2026-10-13 11:32 — Daten-Squad 2026-10-13T11: +24 companies from public legal notices (21 VIES-verified UIDs, FN 27→39, LEI-or-UID 50→71/133)
- `b600986` 2026-10-13 11:06 — Daten-Squad 2026-10-13T10: companies GLEIF LEI 25→50 (133 companies, FN 18→27) via stricter/broader food-connectors matcher
- `77c55cf` 2026-10-13 10:47 — hourly 2026-10-13T10: +30 meals (Ashoka/Südtiroler Kochwerk/Morgentau/Rana/PICARD/Buldak/PrepMyMeal), brand tree ADF/Kochwerk/Morgentau/Samyang, Dashboard Logo-Abdeckung chart, Billa fetch fix in food-connectors

**servas-ai/food-connectors**

- `641914b` 2026-10-13 12:36 — feat(billa): more ready-meal search stems (TK pizza, Krautfleckerl, Germknödel, Kaiserschmarrn, noodle cups) (2026-10-13T12)
- `71f01a7` 2026-10-13 11:45 — fix(mpreis): take nutrition only from the 'je 100 g' block (pages listing a portion block first were parsed as per-100 g; portion-only pages now stay empty); add TK pizza categories to mpreis-shop + gurkerl ready-meal fetch; tests (2026-10-13T11)
- `fd204f4` 2026-10-13 11:30 — feat(company): impressum adapter — FN/HRB/UID from public legal notices (robots.txt respected), every UID verified live via EU VIES with name match; CLI --impressum, MCP company_impressum; tests
- `27ed143` 2026-10-13 11:03 — fix(company): stricter + broader GLEIF matching — spelling variants (ASCII/ö→oe/legal-form-stripped), legal-form families (AG≡SpA, GmbH≡m.b.H.≡srl), country must match legal address, min score 0.85; tests
- `8862425` 2026-10-13 10:43 — fix(billa): category listing 404 — fetch falls back to meal search stems (2026-10-13T10)
- `d838413` 2026-10-13 10:01 — feat(dm): live dm.at connector (sitemap + public products.dm.de product JSON: price, GTIN, nutrition, ingredients, origin, non-AI image); heisse dm snapshot moved to dm-heisse
- `3772004` 2026-10-13 04:34 — docs(hofer): note OFF/Aldi CDN photo path; Akamai blocks hofer.at
- `0980843` 2026-10-13 04:00 — fix(livefresh): fetch(limit=N) must filter bowls before truncating

**servas-ai/fertiggerichte-daten**

- `db3096d` 2026-10-13 12:51 — logos: +13 vision-gated company/producer logos (Alimentastic, Bauck Mühle, Cecchin, ehrenwort, Greisinger, Hamker, Heiderbeck, Hiel, Mochi, Rila, Tops Foods, REWE Group, Mars) from official sites (imprint-verified) or Wikimedia Commons; app_companies brand-alias fallback; company logos 88→111/133; evidence raw/logos_companies_2026-10-13T13.json
- `5f1959d` 2026-10-13 12:37 — data: refresh 2026-10-13T12:37Z
- `09e6788` 2026-10-13 12:20 — logos: +16 vision-gated brand logos (YOUCOOK, Andros, deFLORiAN, AIA, Indomie, Arla, Thiriet, Hammermühle, Landtmann's, Ashoka, Strauss, Danke Bauer, Shan'shi, Riso Gallo, Esterhazy, Galbani) from official sites or Wikimedia Commons + Iglo case aliases; fill file-less youcook/indomie rows; strict logo-less 154→139 brands / 430→368 products; evidence raw/logos_squad_2026-10-13T12.json
- `8abca80` 2026-10-13 11:54 — logos: +30 vision-gated brand logos (NÖM, Danone, Bibigo, Zurück zum Ursprung, Meica, Heinz, Hilcona, Hengstenberg, Kotányi, Nongshim, NENI, Golfera, Stadtküche, Jeden Tag, Gü, Greenforce, Wiegert, Berger Schinken, Bürger …) from Wikimedia Commons (licence noted) or official site headers + 14 safe aliases to existing logo files; strict logo-less 208→160 brands / 555→464 products; evidence raw/logos_squad_2026-10-13T11.json
- `4d0d6c9` 2026-10-13 11:31 — companies: +24 legal entities from public legal notices — 21 UIDs verified live via EU VIES (11 AT, 10 DE), FN 27→39, LEI-or-UID 50→71/133; 12 candidates rejected with reasons (evidence raw/impressum_vies_2026-10-13.json); overlay survives GLEIF reruns; validator UID/FN format checks
- `a83547a` 2026-10-13 11:04 — companies: GLEIF LEI 25→50 (133 companies, FN 18→27) via food-connectors stricter/broader matcher; Rügenwalder Mühle alias; rejected-candidate evidence (Lidl AT LEI is German HRB entity, dm Verwaltungsges., Ehrmann SE, Unimarkt KG)
- `e7517d2` 2026-10-13 10:44 — data: hourly T10 +30 verified meals (Ashoka/Südtiroler Kochwerk/Morgentau/Rana/Buldak/PICARD) evidence
- `916debf` 2026-10-13 10:21 — logos: +10 vision-gated brand logos (Bertagni, Bonduelle, HOFMANNs, Landliebe, Alpro, Müller, Picard, Schärdinger via Commons; Freshery, Every. official sites) + Karnerta brand mapping (166 rows); evidence incl. Lidl API 401 sweep + Penny online probe

**servas-ai/einkaufsanalyse**

- `66934e3` 2026-10-13 01:10 — Einkaufsanalyse v1: shadcn Sidebar-Dashboard, Import, OCR, Beispieldaten

## Ausführen

```bash
pip install pytest playwright && playwright install chromium
./run_all.sh   # Tests + Report + Push (mit Lock, stündlich via cron)
```
