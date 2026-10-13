# Repo-Inventur (Martin-Hausleitner + servas-ai)

Stand 2026-10-13. Gesamt **867** Repos: Martin-Hausleitner 548, servas-ai 319; PRIVATE 747, PUBLIC 120.

> Dieser Hub ist öffentlich: private Repos erscheinen nur als Anzahl. Duplikat-/Stale-Markierungen sind **nur Vorschläge**; nichts wurde gelöscht, archiviert oder umgestellt.

Es gibt keinen breiteren zentralen Repo-Index (`servas-ai/central-knowledge-repo` = Agenten-Flottenstatus, `Martin-Hausleitner/data-inventory` = alter Datenreport), daher liegt die Inventur hier.

## Anzahl pro Projektgruppe

| Gruppe | Public | Private |
|---|---|---|
| Fertiggerichte/food | 6 | 3 |
| Mirrors/Mac-Archiv | 1 | 78 |
| OpenCLI-Connectoren/Tarife | 0 | 83 |
| RAT/Fintaro | 0 | 20 |
| Sonstige | 113 | 560 |
| radar | 0 | 3 |

## Food-Connectoren & Datensätze

- [servas-ai/food-connectors](https://github.com/servas-ai/food-connectors) – Connectoren: Open Food Facts, USDA, CIQUAL, BILLA, Penny, Spar, Hofer, dm, MPreis, Unimarkt, Gurkerl, Heisse Preise, GLEIF, Datensatz-Suche (HF/Kaggle/Zenodo/data.gv.at)
- [servas-ai/fertiggerichte-daten](https://github.com/servas-ai/fertiggerichte-daten) – Datensatz: Produkte, Preise, Nährwerte, Firmen (CSV+JSON); gespeist von food-connectors
- [Martin-Hausleitner/fertiggerichte-vergleich](https://github.com/Martin-Hausleitner/fertiggerichte-vergleich) – App; nutzt fertiggerichte-daten + food-connectors
- [servas-ai/fertiggerichte-vergleich](https://github.com/servas-ai/fertiggerichte-vergleich) – App-Spiegel von Martin-Hausleitner/fertiggerichte-vergleich
- [servas-ai/einkaufsanalyse](https://github.com/servas-ai/einkaufsanalyse) – Kassenbon-Dashboard
- [servas-ai/fertiggerichte-hub](https://github.com/servas-ai/fertiggerichte-hub) – Zentraler Index/E2E

## Fertiggerichte/food (öffentlich)

| Repo | Zweck | Sprache | Letzter Push | Deploy | CI | README | Vorschläge |
|---|---|---|---|---|---|---|---|
| [servas-ai/fertiggerichte-daten](https://github.com/servas-ai/fertiggerichte-daten) | Offener Datensatz: Fertiggerichte im österreichischen Handel (Preise, Nährwerte, Herstelle | Python | 2026-10-13 |  | none | ja |  |
| [servas-ai/food-connectors](https://github.com/servas-ai/food-connectors) | Open connectors + CLI + MCP server for Austrian grocery & ready-meal data | Python | 2026-10-13 |  | none | ja |  |
| [servas-ai/fertiggerichte-vergleich](https://github.com/servas-ai/fertiggerichte-vergleich) | This template provides a minimal setup to get React working in Vite with HMR and some ESLi | TypeScript | 2026-10-13 | https://servas-ai.github.io/fertiggerichte-vergleich/ | none | ja | mögliches Duplikat von Martin-Hausleitner/fertiggerichte-vergleich |
| [Martin-Hausleitner/fertiggerichte-vergleich](https://github.com/Martin-Hausleitner/fertiggerichte-vergleich) | This template provides a minimal setup to get React working in Vite with HMR and some ESLi | TypeScript | 2026-10-13 | https://martin-hausleitner.github.io/fertiggerichte-vergleich/ | none | ja | mögliches Duplikat von servas-ai/fertiggerichte-vergleich |
| [servas-ai/fertiggerichte-hub](https://github.com/servas-ai/fertiggerichte-hub) | Zentraler Index, Live-Status & E2E-Tests aller Fertiggerichte-Projekte | Python | 2026-10-13 |  | none | ja |  |
| [servas-ai/einkaufsanalyse](https://github.com/servas-ai/einkaufsanalyse) | Einkaufsanalyse – Dashboard für Supermarkt-Bons (Österreich) | TypeScript | 2026-10-13 | https://servas-ai.github.io/einkaufsanalyse/ | none | ja |  |

## Mirrors/Mac-Archiv (öffentlich)

| Repo | Zweck | Sprache | Letzter Push | Deploy | CI | README | Vorschläge |
|---|---|---|---|---|---|---|---|
| [servas-ai/code-quality-skills-kit](https://github.com/servas-ai/code-quality-skills-kit) | Self-bootstrapping multi-agent code-quality audit kit for Claude Code. Universal — works o | Python | 2026-06-10 | https://servas-ai.github.io/code-quality-skills-kit/ | SUCCESS | ja |  |

## Sonstige (öffentlich)

| Repo | Zweck | Sprache | Letzter Push | Deploy | CI | README | Vorschläge |
|---|---|---|---|---|---|---|---|
| [Martin-Hausleitner/tarife-at](https://github.com/Martin-Hausleitner/tarife-at) | Tarif-Vergleich Österreich: Handytarife, 5G-Internet & Router (Stand 12.10.2026) | JavaScript | 2026-10-13 | https://martin-hausleitner.github.io/tarife-at/ | SUCCESS | ja |  |
| [Martin-Hausleitner/helixworld-modal](https://github.com/Martin-Hausleitner/helixworld-modal) | Modal.com deployment for HelixWorld (NoizAI) real-time audio-visual world model. Preview v |  | 2026-10-12 |  | none | nein | mögliches Duplikat von servas-ai/helixworld-modal |
| [Martin-Hausleitner/cat-sounds-app](https://github.com/Martin-Hausleitner/cat-sounds-app) | Simple cat soundboard web app | HTML | 2026-10-11 |  | none | ja |  |
| [servas-ai/network-canvas-oneshots](https://github.com/servas-ai/network-canvas-oneshots) | Proprietary Canvas & Whiteboard One-Shot Prototypes | HTML | 2026-10-11 | https://servas-ai.github.io/network-canvas-oneshots/ | SUCCESS | ja |  |
| [servas-ai/brain-cli](https://github.com/servas-ai/brain-cli) | brain – CLI für das brain (sync, check, clone-cell, doctor) | Go | 2026-10-10 |  | none | ja |  |
| [servas-ai/brain](https://github.com/servas-ai/brain) | brain – firmenweites Second Brain für KI-Harnesses (Template) |  | 2026-10-10 |  | none | ja |  |
| [servas-ai/qdrantcli](https://github.com/servas-ai/qdrantcli) | qdrantcli – Qdrant-Vektorsuche mit dem eigenen Token | Go | 2026-10-10 |  | none | ja |  |
| [servas-ai/sharepointcli](https://github.com/servas-ai/sharepointcli) | sharepointcli – SharePoint mit dem eigenen Microsoft-Login | Go | 2026-10-10 |  | none | ja |  |
| [Martin-Hausleitner/aw-importer-whoop](https://github.com/Martin-Hausleitner/aw-importer-whoop) | Local WHOOP to ActivityWatch importer with OAuth sync | Python | 2026-10-10 |  | SUCCESS | ja |  |
| [servas-ai/multi-oracle](https://github.com/servas-ai/multi-oracle) | Oracle bundles your prompt and files so another AI can answer with real context. It speaks | TypeScript | 2026-10-08 |  | none | ja | mögliches Duplikat von Martin-Hausleitner/multi-oracle |
| [Martin-Hausleitner/Luna-Raum](https://github.com/Martin-Hausleitner/Luna-Raum) | LUNA RAUM: unofficial browser-only 3D kitchen measure-up demo. WebGPU, Canvas fallback, lo | HTML | 2026-10-04 | https://martin-hausleitner.github.io/Luna-Raum/ | none | ja |  |
| [Martin-Hausleitner/Luna-Korpus](https://github.com/Martin-Hausleitner/Luna-Korpus) | Luna theme and German launchers on real Aster Desktop, with 19 original upstream applicati | HTML | 2026-10-04 | https://martin-hausleitner.github.io/Luna-Korpus/ | none | ja |  |
| [Martin-Hausleitner/Luna-Stage](https://github.com/Martin-Hausleitner/Luna-Stage) | LUNA STAGE — one-file spatial kitchen sales instrument for EDV Hausleitner, Linz | HTML | 2026-10-04 | https://martin-hausleitner.github.io/Luna-Stage/ | none | ja |  |
| [Martin-Hausleitner/CloakBrowser-Manager](https://github.com/Martin-Hausleitner/CloakBrowser-Manager) | Web-based browser profile manager for CloakBrowser — create, launch, and manage isolated b | Python | 2026-10-04 |  | none | ja |  |
| [Martin-Hausleitner/beeper-matrix-proxy](https://github.com/Martin-Hausleitner/beeper-matrix-proxy) | Matrix-to-Beeper bridgev2 proxy for exposing private Matrix rooms in stock Beeper Desktop | Go | 2026-10-04 |  | none | ja |  |
| [servas-ai/phantomdroid](https://github.com/servas-ai/phantomdroid) | Academic research planner — empirical layer-by-layer evaluation of Android container detec | Kotlin | 2026-10-03 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/Sonar](https://github.com/Martin-Hausleitner/Sonar) | iOS-Voice-App für zwei Leute, die so klingen soll, als stünden sie direkt | Swift | 2026-10-02 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/martins-awesome-skills](https://github.com/Martin-Hausleitner/martins-awesome-skills) | Martin's Awesome Skills: public-safe Hermes and OpenClaw agent skills with Telegram approv | Python | 2026-10-02 |  | none | ja |  |
| [Martin-Hausleitner/screenpipe-context-pipes](https://github.com/Martin-Hausleitner/screenpipe-context-pipes) | Local-first Screenpipe pipe for ActivityWatch, WHOOP, YouTube, and skill metadata | JavaScript | 2026-10-02 |  | none | ja |  |
| [Martin-Hausleitner/interactive-deep-research](https://github.com/Martin-Hausleitner/interactive-deep-research) | Interactive Deep Research is a deterministic, token-frugal research pipeline | HTML | 2026-10-02 | https://martin-hausleitner.github.io/interactive-deep-research/ | SUCCESS | ja |  |
| [Martin-Hausleitner/discord-repair-skill](https://github.com/Martin-Hausleitner/discord-repair-skill) | Safe, repeatable Discord Stable + Vencord repair and performance profile skill for macOS | Shell | 2026-10-02 |  | none | ja |  |
| [Martin-Hausleitner/lunis-status](https://github.com/Martin-Hausleitner/lunis-status) | Lunis Ist-Zeit — Live-Status und Berichte (automatisch erzeugt) | HTML | 2026-10-02 | https://martin-hausleitner.github.io/lunis-status/ | SUCCESS | ja |  |
| [Martin-Hausleitner/aqua-logitech-discord](https://github.com/Martin-Hausleitner/aqua-logitech-discord) | Monorepo: Aqua Voice, Vencord mute sync, Logitech G5 mouse bridge for Discord | JavaScript | 2026-10-02 |  | none | ja |  |
| [Martin-Hausleitner/lokal-vorlesen](https://github.com/Martin-Hausleitner/lokal-vorlesen) | Compact offline macOS text-to-speech player with Piper, a voice gallery, and local OCR. | Objective-C | 2026-09-28 |  | none | ja |  |
| [servas-ai/aws-batch1-gruppe1-showcase](https://github.com/servas-ai/aws-batch1-gruppe1-showcase) | Dieses Repository versammelt modernste, interaktive Webanwendungen und 1:1 One-Shot-Megapr | HTML | 2026-09-23 | https://servas-ai.github.io/aws-batch1-gruppe1-showcase/ | SUCCESS | ja |  |
| [Martin-Hausleitner/OVAL-SUS](https://github.com/Martin-Hausleitner/OVAL-SUS) | OVAL SUS Miniature Edition — standalone HTML social-deduction minigame, original miniature | HTML | 2026-09-22 | https://martin-hausleitner.github.io/OVAL-SUS/ | SUCCESS | ja |  |
| [Martin-Hausleitner/NIGHTSHIFT](https://github.com/Martin-Hausleitner/NIGHTSHIFT) | Single-file 2.5D browser sandbox with living-city NPCs, vehicles, police and dolphin harbo | HTML | 2026-09-22 |  | none | ja |  |
| [Martin-Hausleitner/recorder-device-sdks](https://github.com/Martin-Hausleitner/recorder-device-sdks) | Headless wraps of existing Soundcore Work and Plaud Note Pro OSS SDKs. No UI. No device-de | Python | 2026-09-17 |  | none | ja |  |
| [servas-ai/langcas](https://github.com/servas-ai/langcas) | LANGKAS – lokaler KI-Arbeitsplatz für CLI-Assistenten. KI, oba koa Kas. | HTML | 2026-09-16 |  | none | ja |  |
| [Martin-Hausleitner/Luna-Line](https://github.com/Martin-Hausleitner/Luna-Line) | LUNA LINE — one continuous spatial joinery thread. EDV Hausleitner GmbH Linz. | HTML | 2026-09-15 | https://martin-hausleitner.github.io/Luna-Line/ | FAILURE | ja |  |
| [Martin-Hausleitner/test1](https://github.com/Martin-Hausleitner/test1) | Der Root-Stand bleibt Takt. Der interne Helpdesk wird zusätzlich unter `/helpdesk/` aus de | HTML | 2026-09-14 |  | none | ja |  |
| [Martin-Hausleitner/prompting-workflow-playbook](https://github.com/Martin-Hausleitner/prompting-workflow-playbook) | Eine öffentliche, bereinigte Anleitung für nachvollziehbare Prompt-Arbeit mit mehreren par | HTML | 2026-09-13 |  | none | ja |  |
| [Martin-Hausleitner/local-voice-ai](https://github.com/Martin-Hausleitner/local-voice-ai) | Local voice AI powered by llama-cpp, Kokoro, Nemotron STT, and LiveKit. | Python | 2026-09-06 |  | none | ja |  |
| [Martin-Hausleitner/tribunal-public](https://github.com/Martin-Hausleitner/tribunal-public) | Auditable hard-critical Tribunal library, personas, Codex skill, and OSS comparison | Python | 2026-09-05 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/vencord-autostream](https://github.com/Martin-Hausleitner/vencord-autostream) | Vencord userplugin for configurable one-click screen sharing with honest desired/effective | TypeScript | 2026-08-31 |  | none | ja |  |
| [Martin-Hausleitner/storage-watcher](https://github.com/Martin-Hausleitner/storage-watcher) | A conservative, rule-driven macOS disk cleaner | Shell | 2026-08-30 |  | none | ja |  |
| [Martin-Hausleitner/agent-skills](https://github.com/Martin-Hausleitner/agent-skills) | Portable agent skills: Ideon canvas MCP + MCP Order CLI | Python | 2026-08-26 |  | none | ja |  |
| [Martin-Hausleitner/iphone-mirroring-eu-patch](https://github.com/Martin-Hausleitner/iphone-mirroring-eu-patch) | Working iPhone Mirroring EU enabler for recent macOS (26.x) — with a safe --check mode. Ve | Shell | 2026-08-20 |  | none | ja |  |
| [Martin-Hausleitner/AuraCap](https://github.com/Martin-Hausleitner/AuraCap) | The first open-source project to use GitHub Release as a transient middleware: Turn iOS ca | Python | 2026-08-09 |  | none | ja |  |
| [Martin-Hausleitner/martins-agent-manager](https://github.com/Martin-Hausleitner/martins-agent-manager) | Manager-only orchestration discipline for a fleet of coding agents (Claude Code 🦀, Antigra |  | 2026-07-31 |  | none | ja |  |
| [Martin-Hausleitner/aqua-mute-sync](https://github.com/Martin-Hausleitner/aqua-mute-sync) | Experimental Aqua Voice recording detector and Vencord Discord mute sync for macOS | TypeScript | 2026-07-31 |  | none | ja |  |
| [Martin-Hausleitner/limit-reset-notifier](https://github.com/Martin-Hausleitner/limit-reset-notifier) | 🔔 Notifies you (via self-hosted Matrix) when your Claude Code / Codex usage limits reset,  | JavaScript | 2026-07-31 |  | none | ja |  |
| [Martin-Hausleitner/aqua-voice-exporter](https://github.com/Martin-Hausleitner/aqua-voice-exporter) | Export transcription history, daily stats, and device data from Aqua Voice (macOS) | Python | 2026-07-31 |  | none | ja |  |
| [Martin-Hausleitner/opencodex-grok-linux](https://github.com/Martin-Hausleitner/opencodex-grok-linux) | OpenCodex (ocx) + Grok 4.5 High als Codex-Harness auf Linux — Setup-Skill |  | 2026-07-30 |  | none | ja |  |
| [Martin-Hausleitner/paperclip](https://github.com/Martin-Hausleitner/paperclip) | The open-source app everyone uses to manage agents at work | TypeScript | 2026-07-24 | https://paperclip.ing | none | ja | mögliches Duplikat von servas-ai/paperclip |
| [Martin-Hausleitner/etiketo](https://github.com/Martin-Hausleitner/etiketo) | Etiketo is a simple next.js webapp to create shipping labels for private persons. So you c | TypeScript | 2026-07-22 | https://etiketo.vercel.app/ | none | ja |  |
| [Martin-Hausleitner/headroom-context-idr](https://github.com/Martin-Hausleitner/headroom-context-idr) | [Vollständiger IDR-Report](headroom-context-report.md) · [Öffentlich gerenderter Report](h | Python | 2026-07-20 |  | none | ja |  |
| [Martin-Hausleitner/headroom](https://github.com/Martin-Hausleitner/headroom) | Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer to | Python | 2026-07-18 | https://headroom-docs.vercel.app/docs | none | ja |  |
| [Martin-Hausleitner/paperclip-plugins](https://github.com/Martin-Hausleitner/paperclip-plugins) | Four self-built plugins for [Paperclip](https://github.com/paperclipai/paperclip): | JavaScript | 2026-07-17 |  | none | ja |  |
| [Martin-Hausleitner/paperclip-tribunal](https://github.com/Martin-Hausleitner/paperclip-tribunal) | Paperclip decision component: deterministic multi-lens AI tribunals with fail-closed verdi | Python | 2026-07-14 |  | none | ja |  |
| [Martin-Hausleitner/paperclip-plugin-content-verifier](https://github.com/Martin-Hausleitner/paperclip-plugin-content-verifier) | Content verification plugin for Paperclip. Validates published content (word count, images | TypeScript | 2026-07-13 |  | none | ja |  |
| [Martin-Hausleitner/paperclip-plugin-pipeline-controller](https://github.com/Martin-Hausleitner/paperclip-plugin-pipeline-controller) | Pipeline orchestration plugin for Paperclip. Visual pipeline editor, auto-advance, stuck d | TypeScript | 2026-07-13 |  | none | ja |  |
| [Martin-Hausleitner/agent-orchestration](https://github.com/Martin-Hausleitner/agent-orchestration) | How a single human orchestrates a fleet of AI coding agents — a five-layer model that turn |  | 2026-07-04 |  | none | ja |  |
| [Martin-Hausleitner/tts-studio-reader](https://github.com/Martin-Hausleitner/tts-studio-reader) | Studio-Split text-to-speech reader for pasted Markdown. It renders a large reading stage,  | TypeScript | 2026-07-03 |  | none | ja |  |
| [Martin-Hausleitner/aiusage-widget-proof-screenshots](https://github.com/Martin-Hausleitner/aiusage-widget-proof-screenshots) | Public proof screenshots for the macOS AI Usage Native Widget. |  | 2026-06-22 |  | none | ja |  |
| [Martin-Hausleitner/cmux-remote-guide](https://github.com/Martin-Hausleitner/cmux-remote-guide) | Willkommen zum ultimativen Setup-Guide für **Cmux Remote**! |  | 2026-06-10 |  | none | ja |  |
| [servas-ai/openclaw-update-scripts](https://github.com/servas-ai/openclaw-update-scripts) | Standalone update scripts for OpenClaw workflows | Shell | 2026-06-10 |  | none | ja |  |
| [Martin-Hausleitner/CodexBar](https://github.com/Martin-Hausleitner/CodexBar) | Show usage stats for OpenAI Codex and Claude Code, without having to login. | Swift | 2026-06-10 | https://codex.bar | none | ja |  |
| [Martin-Hausleitner/cmux-control-skill](https://github.com/Martin-Hausleitner/cmux-control-skill) | name: cmux-control |  | 2026-06-09 |  | none | ja |  |
| [Martin-Hausleitner/credo](https://github.com/Martin-Hausleitner/credo) | The agent OS for DAOs. Self-hosted Matrix backbone, Ed25519-signed actions, m-of-n quorum, | HTML | 2026-05-31 | https://martin-hausleitner.github.io/credo/ | SUCCESS | ja | mögliches Duplikat von servas-ai/credo |
| [Martin-Hausleitner/cognitor-ui-kit](https://github.com/Martin-Hausleitner/cognitor-ui-kit) | Public-safe Cognitor dashboard components and macOS tray UI shell | TypeScript | 2026-05-29 |  | none | ja |  |
| [Martin-Hausleitner/autonomous-deep-research](https://github.com/Martin-Hausleitner/autonomous-deep-research) | Public-safe autonomous Deep Research browser automation toolkit with live-CDP guards, Orac | Python | 2026-05-26 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/aw-importer-apple-screentime](https://github.com/Martin-Hausleitner/aw-importer-apple-screentime) | Local Apple iPhone Screen Time to ActivityWatch importer | Python | 2026-05-25 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/obsidian-notion-ui-customization](https://github.com/Martin-Hausleitner/obsidian-notion-ui-customization) | Clean Notion-style Obsidian workspace setup using real community plugins and local Markdow |  | 2026-05-25 |  | none | ja |  |
| [Martin-Hausleitner/aw-importer-youtube](https://github.com/Martin-Hausleitner/aw-importer-youtube) | ActivityWatch importer for high-quality local YouTube watch sessions | JavaScript | 2026-05-20 |  | none | ja |  |
| [Martin-Hausleitner/activitywatch-xbar-plugin](https://github.com/Martin-Hausleitner/activitywatch-xbar-plugin) | Ein einfaches xbar-Plugin für macOS, um die heutige aktive Zeit aus ActivityWatch extrem k | Python | 2026-05-20 |  | none | ja |  |
| [Martin-Hausleitner/openclaw-apple-findmy-skill](https://github.com/Martin-Hausleitner/openclaw-apple-findmy-skill) | Local Apple Find My data pipeline for Martin's OpenClaw and Hermes agents. | Python | 2026-05-20 |  | none | ja |  |
| [Martin-Hausleitner/aw-activitywatch-stack](https://github.com/Martin-Hausleitner/aw-activitywatch-stack) | ActivityWatch local lifelog stack: WHOOP, Apple Screen Time, launchd and privacy-safe expo | Python | 2026-05-18 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/codex-computer-use-eu-activate](https://github.com/Martin-Hausleitner/codex-computer-use-eu-activate) | Codex Computer Use EU Activate skill and self-test prompt | Shell | 2026-05-18 |  | none | ja |  |
| [Martin-Hausleitner/iphone-mirroring-eu-guide](https://github.com/Martin-Hausleitner/iphone-mirroring-eu-guide) | Guide: iPhone Mirroring in der EU aktivieren + iPhone via OpenAI Codex CLI auf macOS steue | Shell | 2026-05-10 |  | none | ja |  |
| [Martin-Hausleitner/aw-importer-apple-health](https://github.com/Martin-Hausleitner/aw-importer-apple-health) | Local-first Apple Health / HealthKit importer for ActivityWatch. | Python | 2026-05-10 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/sonar-skills](https://github.com/Martin-Hausleitner/sonar-skills) | Claude Code skills for Sonar — pairing, audio, release flow. Watch → Releases to subscribe |  | 2026-05-09 |  | SUCCESS | ja |  |
| [Martin-Hausleitner/G0DM0D3](https://github.com/Martin-Hausleitner/G0DM0D3) | LIBERATED AI CHAT | TypeScript | 2026-04-10 |  | none | ja | stale (>180 Tage) – ggf. archivieren; mögliches Duplikat von Martin-Hausleitner/Documents-GitHub-G0DM0D3-mirror |
| [servas-ai/replit-swarm](https://github.com/servas-ai/replit-swarm) | Multi-tier AI agent orchestration system — 9 agents, 20 parallel slots, reflection loop, T |  | 2026-03-22 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/video-project](https://github.com/Martin-Hausleitner/video-project) |  | TypeScript | 2026-03-17 |  | none | nein | stale (>180 Tage) – ggf. archivieren |
| [servas-ai/paperclip-fullstack-agent-swarm](https://github.com/servas-ai/paperclip-fullstack-agent-swarm) | 🏢 15 AI agents that autonomously design, build, test & ship full-stack Next.js apps — a co |  | 2026-03-15 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [servas-ai/openclaw-agent-browser](https://github.com/servas-ai/openclaw-agent-browser) | Agent Browser setup for Tailscale-connected machines — remote browser control via Playwrig | Shell | 2026-03-13 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/excalidraw-mcp-app](https://github.com/Martin-Hausleitner/excalidraw-mcp-app) | Excalidraw MCP App Server — hand-drawn diagrams for Claude | TypeScript | 2026-02-08 | https://excalidraw-mcp-app-two.vercel.app | SUCCESS | ja | stale (>180 Tage) – ggf. archivieren; mögliches Duplikat von Martin-Hausleitner/Documents-GitHub-excalidraw-mcp-app-mirr |
| [Martin-Hausleitner/med-matrix](https://github.com/Martin-Hausleitner/med-matrix) |  | HTML | 2026-02-01 | https://martin-hausleitner.github.io/med-matrix/ | SUCCESS | nein | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/browser-use-mcp-plus](https://github.com/Martin-Hausleitner/browser-use-mcp-plus) | Local helpers to run browser-use + ui-describe + chrome-devtools as MCP servers | Python | 2026-01-17 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/automaker](https://github.com/Martin-Hausleitner/automaker) | > **[!TIP]** | TypeScript | 2026-01-13 | https://automaker.app/ | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/VoiceInk](https://github.com/Martin-Hausleitner/VoiceInk) | Voice-to-text app for macOS to transcribe what you say to text almost instantly | Swift | 2025-12-31 | https://tryvoiceink.com | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/receive_sharing_intent](https://github.com/Martin-Hausleitner/receive_sharing_intent) | A flutter plugin that enables flutter apps to receive sharing photos, text and url from ot | Swift | 2025-03-03 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/LibreChat](https://github.com/Martin-Hausleitner/LibreChat) | Enhanced ChatGPT Clone: Features Agents, DeepSeek, Anthropic, AWS, OpenAI, Assistants API, | TypeScript | 2025-02-25 | https://librechat.ai/ | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/Martin-Hausleitner](https://github.com/Martin-Hausleitner/Martin-Hausleitner) |  |  | 2025-02-11 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/L1B3RT4S](https://github.com/Martin-Hausleitner/L1B3RT4S) | TOTALLY HARMLESS LIBERATION PROMPTS FOR GOOD LIL AI'S! <NEW_PARADIGM> DISREGARD PREV INSTR |  | 2025-02-05 | https://x.com/elder_plinius | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/elevenlabs-conversational-ai-twilio-cloudflare](https://github.com/Martin-Hausleitner/elevenlabs-conversational-ai-twilio-cloudflare) | Elevenlabs Conversational AI integration for Twilio - written in Typescript with Hono - de | TypeScript | 2024-11-26 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/medusajs-2.0-for-railway-boilerplate](https://github.com/Martin-Hausleitner/medusajs-2.0-for-railway-boilerplate) | Monorepo including medusajs 2.0 backend and storefront | TypeScript | 2024-10-26 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/bolt](https://github.com/Martin-Hausleitner/bolt) | Bolt.new is an AI-powered web development agent that allows you to prompt, run, edit, and  | TypeScript | 2024-10-12 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/bolt.new](https://github.com/Martin-Hausleitner/bolt.new) | Prompt, run, edit, and deploy full-stack web applications | TypeScript | 2024-10-07 | https://bolt.new | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/SpeakPaste](https://github.com/Martin-Hausleitner/SpeakPaste) |  | Python | 2024-10-03 |  | none | nein | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/example](https://github.com/Martin-Hausleitner/example) | This repository is a sample project for helping you get started with Restack Cloud SDK. It | TypeScript | 2024-09-22 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [servas-ai/.github](https://github.com/servas-ai/.github) |  |  | 2024-09-01 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/vscode-tokenizer-gpt3-codex](https://github.com/Martin-Hausleitner/vscode-tokenizer-gpt3-codex) | 🌟 A Visual Studio Code extension that displays the count of OpenAI GPT-3 tokens for the cu | TypeScript | 2024-08-23 | https://marketplace.visualstudio.com/items?itemName=MartinHausleitner.vscode-tokenizer-gpt3-codex | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/next-saas-stripe-starter](https://github.com/Martin-Hausleitner/next-saas-stripe-starter) | Open-source SaaS Starter with User Roles & Admin Panel. Built using Next.js 14, Prisma, Ne | TypeScript | 2024-08-16 | https://next-saas-stripe-starter.vercel.app | none | ja | stale (>180 Tage) – ggf. archivieren |
| [servas-ai/SmtpServer](https://github.com/servas-ai/SmtpServer) | A SMTP Server component written in C# | C# | 2024-07-03 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/Nochba](https://github.com/Martin-Hausleitner/Nochba) | Verbinde dich mit deiner Nochbaschaft | Dart | 2024-05-26 | http://nochba.at/ | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/powersync.dart](https://github.com/Martin-Hausleitner/powersync.dart) | SDK that enables local-first and real-time reactive apps with embedded SQLite for Flutter/ | Dart | 2024-04-03 | https://www.powersync.com | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/ChecklistAI](https://github.com/Martin-Hausleitner/ChecklistAI) | This project harnesses the capabilities of OpenAI's GPT-4 Vision API to identify diseases  | C++ | 2024-02-07 | https://checklist-ai.vercel.app | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/willhaben-chrome-extension](https://github.com/Martin-Hausleitner/willhaben-chrome-extension) |  | JavaScript | 2024-01-24 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/ProgrammingCamp-QTTaxiDriver](https://github.com/Martin-Hausleitner/ProgrammingCamp-QTTaxiDriver) |  | C# | 2023-04-21 |  | none | nein | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/nochba-thesis](https://github.com/Martin-Hausleitner/nochba-thesis) | This is the repository for my diploma thesis. | TeX | 2023-03-31 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/vscode-copyminify](https://github.com/Martin-Hausleitner/vscode-copyminify) | "CopyMinify" is a VS Code extension that allows users to quickly and easily minify selecte | TypeScript | 2023-03-17 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/plantuml-markdown](https://github.com/Martin-Hausleitner/plantuml-markdown) | ) |  | 2023-02-16 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/ClubsOfExcellenceHTLLeonding](https://github.com/ManuelPuchner/ClubsOfExcellenceHTLLeonding) | ``kubectl apply -f ./k8s/clubsofexcellence_test.yml`` | TypeScript | 2022-11-07 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/flutter-firebase-test-01](https://github.com/Martin-Hausleitner/flutter-firebase-test-01) | A new Flutter project. | C++ | 2022-07-28 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/JPALibraryManager](https://github.com/Zeno-Paukner/JPALibraryManager) | A simple Quarkus JPA exercise for a library management system. | Java | 2022-07-28 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/if.05.01_04a-threads](https://github.com/Martin-Hausleitner/if.05.01_04a-threads) | The goal of this week's assignment is to make you familiar with threadsn in Java. | Java | 2020-10-23 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/instagram_network_analysis-1](https://github.com/Martin-Hausleitner/instagram_network_analysis-1) | Step by step guide on how to use the code and interpret the results: https://medium.com/@m | Python | 2020-09-28 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/webapp-votelist](https://github.com/Martin-Hausleitner/webapp-votelist) | A Votlist Website: https://votelistt.herokuapp.com/ | JavaScript | 2020-09-03 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/information-website-to-do-list-comparison](https://github.com/Martin-Hausleitner/information-website-to-do-list-comparison) | information-website-to-do-list-comparison created by GitHub Classroom | HTML | 2019-12-19 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/reading-assignment-4-advanced-css-Martin-Hausleitner](https://github.com/zzArchive-if-03-01-C-fall-2019/reading-assignment-4-advanced-css-Martin-Hausleitner) | reading-assignment-4-advanced-css-Martin-Hausleitner created by GitHub Classroom |  | 2019-12-05 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
| [Martin-Hausleitner/reading-assignment-3-lists-and-tables-Martin-Hausleitner](https://github.com/zzArchive-if-03-01-C-fall-2019/reading-assignment-3-lists-and-tables-Martin-Hausleitner) | reading-assignment-3-lists-and-tables-Martin-Hausleitner created by GitHub Classroom |  | 2019-12-05 |  | none | ja | stale (>180 Tage) – ggf. archivieren |
