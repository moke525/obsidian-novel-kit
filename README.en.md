<a id="english"></a>

<div align="center">

# ✍️ Novel-kit

**[中文](README.md)** | **English**

[![Obsidian plugin](https://img.shields.io/badge/Obsidian-plugin-7C3AED?logo=obsidian&logoColor=white)](https://community.obsidian.md/plugins/novel-kit)
[![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcommunity.obsidian.md%2Fapi%2Fv1%2Fplugins%2Fnovel-kit&query=%24.downloads&label=downloads&logo=obsidian&logoColor=white&color=7C3AED)](https://community.obsidian.md/plugins/novel-kit)
[![Latest release](https://img.shields.io/github/v/release/moke525/obsidian-novel-kit?sort=semver)](https://github.com/moke525/obsidian-novel-kit/releases/latest)
[![Minimum Obsidian version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fmoke525%2Fobsidian-novel-kit%2Fmain%2Fmanifest.json&query=%24.minAppVersion&label=min%20Obsidian&color=blue)](manifest.json)
[![License](https://img.shields.io/github/license/moke525/obsidian-novel-kit)](LICENSE)

An all-in-one writing suite for long-form web novels in Obsidian.<br />
One work is one folder in your vault · Settings, outlines and manuscripts are all plain Markdown · Seven views over the same notes.

<br />

<a href="docs/reference.en.md"><kbd>📖 Full Reference</kbd></a>
<a href="docs/reference.en.md#troubleshooting"><kbd>❓ FAQ</kbd></a>

<br />

<br />

<img width="100%" alt="Creative homepage" src="assets/home_en.gif" />

</div>

> [!IMPORTANT]
> **This plugin is built for the desktop version — using it on desktop is recommended.**
> Mobile support is basic adaptation only: it opens, reads and edits, but layout density and interactions
> (dragging, context menus, side-by-side panels) are designed for desktop, so the phone experience is noticeably worse.

<br />

## ✨ Feature Highlights

### 🏠 Creative Homepage
<sub>Progress & KPIs · Daily word-count curve and heatmap · Word frequency · Todos · Clock · Drag to add or remove widgets, layout saved to System/home.json</sub>

<img width="100%" alt="Creative homepage" src="assets/home_en.gif" />

### 🕸️ Graph
<sub>Visualizes relations plus foreshadowing / hooks · "Filter" decides what shows and what gets highlighted · "Display config" handles file types, colors and edges</sub>

<img width="100%" alt="Graph" src="assets/graph_en.gif" />

### 📅 Timeline
<sub>Scenes ordered by time · With "Folder" grouping, dragging really moves files · Edit start/end dates straight in the frontmatter</sub>

<img width="100%" alt="Timeline" src="assets/timeline_en.gif" />

### 🧬 Fission
<sub>Multi-column card outline · Drag to reorder plot beats · Cards *are* the notes — you are editing the same files · Right-click to retag the event kind (era / scene / chapter / plot)</sub>

<img width="100%" alt="Fission" src="assets/fission_en.gif" />

### 🗺️ Map & Spacetime
<sub>Coordinate markers on a base image · Spacetime maps the image to a plane and time to the z axis · Coordinates read "map name：x，y" (full-width colon and comma)</sub>

<img width="100%" alt="Map and Spacetime" src="assets/map-spacetime_en.gif" />

### 🃏 Cards & Table
<sub>Cards form a configurable field wall · Table supports grouping, filtering, pinning columns and in-place editing · Both support drag ordering and cross-group drag</sub>

<img width="100%" alt="Cards and Table" src="assets/cards-table_en.gif" />

### 🧵 Foreshadowing · Hooks · Plot · Manuscript
<sub>The main operation happens in the prose: select a sentence → right click → plant or resolve; state walks through Unplanted → Planted → Linked → Resolved</sub>

<img width="100%" alt="Foreshadowing and hooks" src="assets/foreshadowing_en.gif" />

### 📱 Mobile (basic adaptation)
<sub>Desktop is the main target; mobile is only kept usable: homepage switches to single column + grid + tabs, template editor side panel collapses into a drawer, graph / timeline inspectors float above the canvas</sub>
<sub>Touch interactions were not redesigned — dragging, context menus and multi-panel workflows are desktop habits and feel awkward on a phone</sub>

<img width="100%" alt="Mobile" src="assets/mobile_en.gif" />

### 📝 Creative Assistants

<table>
<tr>
<td width="33%" align="center" valign="top"><img width="100%" alt="Inspiration cards" src="assets/inspiration_en.gif" /><br /><b>Inspiration Cards</b><br /><sub>Drag into graph / timeline / fission to become plot beats</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Glossary" src="assets/glossary_en.gif" /><br /><b>Glossary</b><br /><sub>Quick lore lookup, organized in layers</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Word frequency" src="assets/wordfreq_en.gif" /><br /><b>Word Frequency</b><br /><sub>See your habits and repeats at a glance</sub></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><img width="100%" alt="Proofreading" src="assets/proofread_en.gif" /><br /><b>Proofreading</b><br /><sub>In-place checks, confirm each fix</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Writing goal" src="assets/writing-goal_en.gif" /><br /><b>Writing Goal</b><br /><sub>Daily targets and progress nudges</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Naming" src="assets/naming_en.gif" /><br /><b>Naming</b><br /><sub>Generate character and place names by style</sub></td>
</tr>
<tr>
<td width="33%" align="center" valign="top"><img width="100%" alt="File templates" src="assets/file-template_en.gif" /><br /><b>File Templates</b><br /><sub>Auto-apply a template and rename by "target folder + filename pattern"</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Snapshots" src="assets/snapshot_en.gif" /><br /><b>History Snapshots</b><br /><sub>Auto-archived, side-by-side diff before restoring</sub></td>
<td width="33%" align="center" valign="top"><img width="100%" alt="Sticky notes" src="assets/sticky-note_en.gif" /><br /><b>Sticky Notes</b><br /><sub>Jot things down, auto-saved</sub></td>
</tr>
</table>

### 🖥️ Desktop · 📱 Mobile

**Using it on desktop is recommended**: every feature is designed around desktop interactions, and mobile is
basic adaptation only (see the note at the top of this file).

| 🖥️ Desktop | 📱 Mobile (basic adaptation) |
|:---|:---|
| **All features available** | Single-column homepage + responsive grid + tabs |
| **CSS Snippets**: inject custom styles into your vault | Template editor side panel becomes a drawer |
| **Writing Mode**: typewriter, keeps the cursor line centered | Inspectors float above the canvas |
| Mouse drag, context menus, side-by-side panels | CSS Snippets / Writing Mode are **not registered at all** (they need Electron) |
| Mouse dragging, context menus, side-by-side panels | Touch interactions were not redesigned; dragging and right-click flows are limited |

## 📥 Installation

| Method | Steps |
|:-----|:-----|
| **Community plugins** *(recommended)* | Settings → Community plugins → Browse → search `novel-kit` → install and enable |
| **Manual** | Put `main.js`, `manifest.json` and `styles.css` into `<your vault>/.obsidian/plugins/novel-kit/`, then enable it |

Requires Obsidian 1.8.7 or later; **desktop only** (the plugin uses Node / Electron APIs).

## 🚀 Quick Start

1. **Register a work**: open the creative homepage and click "New work", or run the command "Register novel workspace". The folders `设定/`, `事件/`, `正文/`, `灵感/` and `System/` are created for you.
2. **Try the sample** (optional): when no work exists yet, the panel top shows **"Load sample"**, which writes *《残虹夜雨》* — 1 era (北境乱世), 3 scenes and 6 outline sections, 4 manuscript chapters, 14 clues (8 resolved, 6 deliberately left open to demo filtering), one "北境" map with four coordinates, 4 inspiration cards, 2 sticky notes, plus two Chinese walkthrough notes. Following the tour is the fastest way in.
3. **Start writing**: draft under `正文/`, select sentences to plant foreshadowing and hooks; open the main panel (book icon in the ribbon) when you want the whole picture.

<details>
<summary><kbd>🎯 Key Commands</kbd></summary>

<br />

| Command | Description |
|:-----|:-----|
| Register novel workspace | Register a folder in your vault as a work |
| Switch active work | Move between registered works |
| Open novel panel | Open the main panel with all seven views |
| Open creative homepage | Open the dashboard homepage |
| Load sample | Write the sample work 《残虹夜雨》 |
| New / Resolve foreshadowing | Plant and resolve on the current selection |
| Toggle writing mode | Desktop: typewriter scrolling |

See the [commands section of the reference](docs/reference.en.md#commands).

</details>

<details>
<summary><kbd>⚙️ Key Settings</kbd></summary>

<br />

| Setting | Default | Description |
|:-----|:-------|:-----|
| Default view | Graph | Which view opens first in the panel |
| View layout | By device | Multi-column on wide screens; single column + tabs on mobile |
| Stop words | Built-in | Words ignored by word-frequency counting |
| Auto snapshot | On | Whether notes are archived automatically |
| CSS snippets | Off | Desktop: inject custom styles into the vault |

See the [settings section of the reference](docs/reference.en.md#settings).

</details>

## ❓ FAQ

If a work won't open, it's usually one of three things: **it isn't registered** (click "New work" first), **it isn't selected at the top of the panel**, or **the `正文/` path is wrong** (write under the `正文/` of a registered work).

Notes missing from the graph is usually "Only show connected" hiding nodes with no relations — turn that off, or add a relation; if a whole category is missing, tick its file type under "Filter" or "Display config" in the toolbar.

Markers missing on the map: check that coordinates read "map name：x，y" (**full-width colon and comma**) and that the map's enabled types include `locale`. If a timeline edit doesn't stick, change the "开始" / "结束" fields directly in the note's frontmatter.

Word counts not adding up usually means the homepage counts manuscripts in the **currently active work** — confirm the right work is selected, then refresh.

More Q&A in the [reference FAQ](docs/reference.en.md#troubleshooting).

## 💾 Data

Settings, outlines and manuscripts are all Markdown notes in your vault. The plugin only maintains two extra things:

- **Plugin `data.json`** (`.obsidian/plugins/novel-kit/data.json`): the work list, the active work, and global settings. Deleting it loses registrations and settings and **touches no notes**.
- **Per-work `System/*.json`**: view layouts, filter rules, homepage templates, todos, sticky notes. Deleting one only resets that slice of view configuration.

## 🌐 Network use

**The plugin works fully offline**, collects no telemetry, and never uploads your notes. Only the two features below reach the network, and only when you trigger them yourself — there are no background requests:

| Feature | When it goes online | Service it contacts |
|:--------|:--------------------|:--------------------|
| Word-frequency / proofreading dictionaries | When you click "Download" for a dictionary in settings | `cdn.jsdelivr.net` (jieba dictionaries), `www.mdbg.net` (CC-CEDICT) |
| Homepage web-table widget | When you enter a URL and click "Fetch" | The URL you entered |

Both only **download** data to your machine (dictionaries are saved to `.obsidian/plugins/novel-kit/word-freq-dicts/`); nothing of yours is sent out. Word frequency still works without downloading a dictionary — only the built-in stop-word list is available and segmentation is less accurate.

## ⚖️ Disclosures

- **Some features require a paid licence**: the plugin has a **30-day free trial** (counted from the first time you open the novel panel), after which a licence key is required to keep using the full feature set. Licences are **bound to one machine**, so switching machines requires a new purchase; pricing and checkout are in the plugin's "Licence" settings page.
- **One file outside your vault is read and written**: on desktop the licence state (key, expiry, trial start) is stored in `novel-kit/license.json` under your user directory — `%APPDATA%\novel-kit\license.json` on Windows, `~/Library/Application Support/novel-kit/license.json` on macOS, and `$XDG_CONFIG_HOME/novel-kit/license.json` on Linux (`~/.config/novel-kit/license.json` when unset). This is what lets you **switch vaults or create a new vault without re-activating**. The file is encrypted and contains nothing from your notes. On mobile, the out-of-vault path is unavailable, so the plugin falls back to `data.json` inside the vault.
- **No telemetry**: there is no client-side telemetry and no background network requests (network use is limited to the two cases in the previous section).
- **Open source**: the full source is in this repository, released under the [Apache-2.0 License](LICENSE).

## 🛠️ Development

Requires Node.js 18 or later. `npm install`, then `npm run dev` to develop (output goes to `test-vault/.obsidian/plugins/novel-kit/`), and `npm run build` for a production bundle in `build/`.

After making changes:

```bash
npm test              # vitest: homepage templates / sample data / style rules
npm run check         # svelte-check type checking
npm run visual:check  # visual regression (run npm run build first)
npm run lint          # Biome
```

The entry point is `src/main.ts`; each feature lives in its own `src/features/<name>/` folder (`manager.ts` + `appView.ts` + `settings.ts`), and only `css-snippets` and `export` are desktop-only. See the [reference's development notes](docs/reference.en.md#development).

<br />

<div align="center">

## 📄 License & 💬 Feedback

[Apache-2.0 License](LICENSE) · [NOTICE](NOTICE)

### Third-party components

This plugin bundles and uses the following open-source projects, with thanks (copyright notices retained as their licences require):

| Component | Licence | Copyright |
|:----------|:--------|:----------|
| [three.js](https://github.com/mrdoob/three.js) | MIT | © 2010–2024 three.js authors |
| [Chart.js](https://github.com/chartjs/Chart.js) | MIT | © 2014–2024 Chart.js Contributors |
| [3d-force-graph](https://github.com/vasturiano/3d-force-graph) | MIT | © Vasco Asturiano |
| [MiniSearch](https://github.com/lucaong/minisearch) | MIT | © Luca Ongaro |
| [jsdiff](https://github.com/kpdecker/jsdiff) | BSD-3-Clause | © 2009–2015 Kevin Decker &lt;kpdecker@gmail.com&gt; |
| [relation-graph](https://github.com/seeksdream/relation-graph) | MIT | © seeksdream |
| [CC-CEDICT](https://cc-cedict.org/) | CC BY-SA 4.0 | © CC-CEDICT project (downloaded on demand, not bundled) |

⭐ Star · 🐛 [Issues](https://github.com/moke525/obsidian-novel-kit/issues)

<br />

**Happy writing!** ✍️

</div>
