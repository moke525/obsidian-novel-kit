# Novel-kit complete reference

> [!IMPORTANT]
> **This plugin is built for the desktop version; using it on desktop is recommended.** Mobile support is basic adaptation only (see [Mobile](#mobile)).

This is the long form of the [README](../README.en.md). The README gets you started; this page holds the **full lists**: entry points, views, settings, mobile behaviour, storage locations and troubleshooting.

[中文](reference.zh-CN.md)

---

## Contents

1. [Entry points](#entry-points)
2. [Work workspace](#work-workspace)
3. [Studio home](#studio-home)
4. [Studio panel: seven views](#studio-panel-seven-views)
5. [Foreshadowing · hooks · plot · manuscript](#foreshadowing--hooks--plot--manuscript)
6. [Sidebars and writing aids](#sidebars-and-writing-aids)
7. [Vault-wide features](#vault-wide-features)
8. [Shared lore groups](#shared-lore-groups)
9. [Mobile](#mobile)
10. [Settings](#settings)
11. [Suggested workflow](#suggested-workflow)
12. [Troubleshooting](#troubleshooting)
13. [Where your data lives](#where-your-data-lives)
14. [Network use](#network-use)
15. [Development](#development)

---

## Entry points

Most entry points can be switched off individually in settings; doing so hides the ribbon icon and closes the related view.

### Ribbon icons

| Icon | Panel | Docked |
| --- | --- | --- |
| home | Studio home | main |
| book-open | Novel panel | main |
| hash | Word frequency | right sidebar |
| spell-check | Proofreading | right sidebar |
| git-branch | Foreshadow ledger | right sidebar |
| lightbulb | Inspiration library | right sidebar |
| list-tree | Glossary | right sidebar |
| scroll-text | Plot cross-check | right sidebar |
| bookmark | Marks ledger | right sidebar |
| pen-line | Word count | right sidebar |
| dices | Naming | right sidebar |
| history | Snapshots | right sidebar |
| search-alert | Advanced search | either sidebar |
| smartphone | Phone preview | right sidebar |
| file-down | Export (currently hidden) | desktop only |

### Commands

- **Open**: studio home / novel panel / each sub-view / word frequency / proofreading / foreshadowing / inspiration / glossary / plot / marks / word count / naming / search / phone preview / CSS snippets / snapshots
- **Create**: register workspace / sticky note / inspiration
- **Toggle**: highlight settings, sticky notes, file-tree word count, end-of-line word count, stage ruler, selection word count, focus mode
- **Selection**: extract to sticky note / inspiration / highlight file / highlight comment
- **Maintenance**: rebuild node graph, re-apply file-tree sort, reload CSS snippets

Editor context menus add: locate / create foreshadowing & hooks, edit hook/foreshadowing, generate manuscript, link to scene…

---

## Work workspace

A **workspace** is one root folder per work in your vault. The list of works and the active one live in the `novel` section of the plugin's `data.json`.

### Scaffold folders

```text
My Novel/
  设定/          # characters, places, props, techniques, factions, assets…
  事件/          # scenes / chapters / beats (outline)
  正文/          # manuscript (word count, highlighting read here by default)
  灵感/          # inspiration
  词条/          # glossary, optional
  System/
    workspace.json / graph.json / timeline.json / home.json …
    templates/   # file templates (default)
    示例导览.md  # written by “Load sample”
    伏笔钩子剧情正文.md
```

Content is plain Markdown plus frontmatter; view layouts and templates live in `System/*.json`.

### Workspace modes

| Mode | Difference |
| --- | --- |
| **Simple** | One fewer view (no fission); the graph has no pack / piece drilling; foreshadowing and hooks are called “marks” |
| **Full** | Every view, including hook / foreshadowing nodes and plot cross-check |

Marks are available in both modes (always called “marks”).

---

## Studio home

### Widgets

| Widget | What it shows |
| --- | --- |
| Current work | Work status and progress, and the way into the novel panel |
| KPI | Word count across all works, today's writing (net `last − start` and gross `max − start`) |
| Work status | Cards and charts for the indicators you picked |
| Journal | Outline entries in time order |
| Word frequency | Word usage for the current work |
| Daily words / Activity | Line chart and heatmap |
| Web table | Render a line chart from a chart URL |
| Todo list | Stored in `home.json`, kept between sessions |
| Clock / Daily quote | The quote needs a note in your vault as its source |
| Tasks / All works | Shortcuts and the list of every work |

### Home template editor

Studio home, top-right ⚙ → **Home template**. The window can be dragged and resized.

- **Left sidebar**: page settings (top banner image and its height), layouts, widgets, and the config for the selected node. On narrow screens it collapses into a drawer.
- **Canvas**: drag nodes to move them or change their container; layout kinds are **list (single column) / grid (auto-fit) / splitPanel (two panes) / tabs**.
- Everything is written to `System/home.json`: `templates` holds the template trees, `activeTemplateId` records which one is active, `todos` holds the todo list.

### The two default templates

On first run one of them is activated according to your device, and **both ship with the plugin**, so you can always switch back to the wide one.

| Template | For | Structure |
| --- | --- | --- |
| **Default layout** | Wide screens | Nested splitPanels: top / middle / bottom bands plus left / right panes |
| **Mobile layout** | Phones / narrow screens | Single-column list scroll + auto-fit grid + tabs folding the data area, no splitPanel |

The mobile layout avoids splitPanels because on a 390px screen a 72/28 split leaves the right pane a few dozen pixels wide, and every chart collapses into a vertical line.

---

## Studio panel: seven views

Top bar: work dropdown + refresh, then one row of view tabs: **graph · timeline · fission · map · spacetime · cards · table**.

| View | What it does |
| --- | --- |
| **Graph** | Relationship graph: `关系` / `relation` field links, org structures, pack / piece drilling; orange sockets are foreshadowing, blue ones are hooks. Toolbar **filter** controls visibility and special styles, **display config** controls type mapping and colours |
| **Timeline** | Scenes / chapters / beats arranged by time; with grouping set to folder, dragging moves the real file |
| **Fission** | Multi-column card outline (reads `事件/` by default). Hidden in simple mode |
| **Map** | Markers on a base image; the spacetime view needs at least one map |
| **Spacetime** | Three dimensions: x / y = map, z = time; per-character trail mode available |
| **Cards** | Configurable wall of fields; pick fields and controls in the template editor |
| **Table** | Grouping, filtering, pinned columns, inline editing; shares the same rule components as the graph |

**Highlight settings** are not in the panel: they live in **Settings → Highlight settings** and are global for every registered work. Word lists can be collected from all registered works; a legacy `System/highlight.json` inside a work is imported once when needed.

---

## Foreshadowing · hooks · plot · manuscript

**The main operations happen in the manuscript.** The graph and its siblings are visualisations.

| | Manuscript | Foreshadowing | Hook | Plot |
| --- | --- | --- | --- | --- |
| Role | Drafting and the entry point for planting | Plants the clue | Resolves the clue | Cross-checks the outline |
| Where | Select text in `{work}/正文/`, right-click | Create / locate / edit from the manuscript | Same | Ribbon scroll-text (read-only) |

Status is tracked on the foreshadowing: **not planted → planted → linked → resolved** (plus the abnormal **dangling** state). One foreshadowing can be pointed at by several hooks.

Suggested order: generate or link the manuscript → select text to create / locate → link hook and foreshadowing in the edit dialog → keep the plot panel open while writing → review unresolved ones in the ledger → open the graph only when you need to see relationships.

Details live in `System/伏笔钩子剧情正文.md` inside the work (Chinese).

---

## Sidebars and writing aids

| Module | What it does |
| --- | --- |
| **Inspiration library** | `{work}/灵感/`; cards can be dragged into graph / timeline / fission to become beats |
| **Glossary** | Filename = entry type, one entry per line |
| **Word frequency** | Counts the file in the active editor; tokenizer dictionaries must be **downloaded over the network** in settings (see "Network use") |
| **Proofreading** | Suspect characters and repeated words by dictionary |
| **Sticky notes** | Stored under the work's `System`; editor selections can become a note / inspiration / highlight |
| **Phone preview** | Simulates a reading-app layout |
| **Word count** | Goals and sprints; file-tree count, end-of-line count, stage ruler and selection count each have their own switch |
| **Naming** | Bulk generation for characters, places, factions and more |

---

## Vault-wide features

These are **not limited to the active work**: they apply inside any registered work folder, or vault-wide.

### File templates

**Settings → File templates**. A rule has: target folder, filename pattern, optional template file, naming tool, auto-fill.

- With a template file the body is written and the file renamed to the pattern; without one the file is **only renamed to the pattern**.
- Counters: `{n}/{nn}/{nnn}` for Arabic numerals, `{N}/{NN}/{NNN}` for Chinese numerals (`第{N}章` → 第一章).
- Applies when you create a note in the target folder of any registered work, subfolders included.

### Highlight settings

Global config; word lists come from all registered works (and shared source vaults). The “toggle highlight settings” command switches it on and off quickly.

### Open files in a new tab

**Settings → Novel writing**. Once on, opening from the file tree, a link or a plugin view always uses a new tab.

### Snapshots

Automatic and manual copies of the current note; browse, diff and restore in the panel. Diff reads **left = snapshot (deletions in red)**, **right = current file (additions in green)**.

### Export (currently hidden)

Export a work to PDF / DOCX and more. **Currently hidden** (all entries hidden, code kept — see the note at the top of `src/main.ts`); to bring it back, uncomment three spots in `main.ts` and `obsidian/settings/global.svelte`.

### Focus writing (typewriter)

Keeps the caret line centred while editing. Requires editing mode, not preview.

### File-tree sort

Vault-wide ordering: Chinese numerals, natural numbers, custom word order.

### Advanced search / JSON Studio / CSS snippets

Full-text search and replace; tree-edit your `System/*.json`; manage `.obsidian/snippets`. CSS snippets depend on desktop capabilities and are not shown on mobile.

---

## Shared lore groups

**Settings → Novel writing → Shared lore groups**: several works share one world view, referencing lore read-only (plus optional eras / scenes). Shared files never leave the source vault, carry a shared badge in views, and are protected from accidental edits.

---

## Mobile

**This plugin is developed for the desktop version; using it on desktop is recommended.** Mobile support is
basic adaptation only — it will open, read and edit fine, but layout density and interactions (dragging,
context menus, side-by-side panels) are designed for desktop and will feel cramped on a phone.
The table below lists what has been adapted on mobile; it is not a promise of full feature parity.

| Case | Behaviour |
| --- | --- |
| **CSS snippets, export** | Depend on Electron and printing; their settings tabs and entries do not appear at all (export is **additionally hidden** right now, code kept) |
| **Home layout** | The **mobile layout** is activated automatically on first run (single column + auto-fit grid + tabs); you can switch back to the wide one by hand |
| **Home / cards template editors** | The left sidebar becomes an overlay drawer, collapsed by default, pulled in and out from the title bar |
| **Graph / timeline / spacetime inspectors** | Float over the canvas on narrow screens and dock to an edge, instead of eating canvas width |
| **Advanced search** | Docks to the right sidebar (the left sidebar is the drawer-style main navigation and would be pushed away) |
| **Glossary config panel** | Drops its anchor on narrow screens and centres on the screen |
| **Glossary / marks / inspiration / plot / ledger** | Single-column layouts, usable as they are |

---

## Settings

Path: **Settings → Novel-kit**.

| Tab | Contents |
| --- | --- |
| **Novel writing** | Master switch, ribbons, rebuild debounce, open in new tab, word frequency, shared lore groups |
| **Highlight settings** | Global highlight rules |
| **File templates** | Rules, template folder, naming and auto-fill |
| **File-tree sort** | Custom ordering |
| **CSS snippets** | Snippet management (desktop) |
| ~~Export~~ | **Currently hidden** (export options, code kept) |
| **Focus writing** | Typewriter-style centred writing |
| **Snapshots** | Auto-save, retention policy, panel |
| **Word count** | Tree / end-of-line / ruler / selection |
| **Naming tool** | How many to generate |
| **Other settings** | Search / phone preview / JSON Studio |

---

## Suggested workflow

1. Write in the **manuscript**; generate or link beats only when you need the outline.
2. Select the planting / resolving sentence → create and locate → link hook and foreshadowing in the edit dialog.
3. Keep **plot** open while writing; sweep unresolved clues in the **ledger**; clicking a highlight scrolls to the card.
4. Open graph / timeline / fission / map / spacetime when you need relationships, pacing or space.
5. Check fields in table / cards, word usage in word frequency, suspects in proofreading, goals in word count, layout in phone preview; snapshot important moments by hand.

Inspiration → drag into graph / timeline / fission → fill in fields → generate manuscript → **back to selecting text in the draft to locate it**.

---

## Troubleshooting

### Getting started

- **How do I start a novel?**  
  Open the studio home and use **Add work**, or run the command *Register novel workspace*. The work folder is scaffolded with `设定/`, `事件/`, `正文/`, `System/` and the rest.

- **The panel is empty / no work in the dropdown?**  
  Make sure a work is registered and selected in the panel header. After switching vaults or machines, reopen that vault and enable the plugin.

- **I cannot see “Load sample”.**  
  It only appears while the vault has **no registered work at all**.

### Nodes missing from the graph

- **A character I just created showed up, then vanished after a restart?**  
  The graph only shows connected nodes by default. Anything without a relation, participant or similar link is hidden. Turn that option off, or give the note a relation.

- **The scene is there but its chapters / beats are not?**  
  The parent scene is probably hidden by the same “connected only” rule, or you have not drilled into it. Get the scene on the graph first, then double-click into its pack; or turn off “only show connected”.

- **A whole type (characters, places…) is missing?**  
  Open the toolbar **filter** or **display config** and tick that file type.

### Map · spacetime · timeline

- **I moved a place to another map and its marker is gone.**  
  Check that the new map's displayed types include `locale`, and that the note's coordinate reads `map name：x，y` (both **colon and comma are full-width**), with the map name matching the map's title.

- **The spacetime list has events but I cannot find them in 3D.**  
  Select a map first, and the beat has to resolve to a place that has a coordinate.

- **Editing start / end on the timeline does not stick.**  
  Open the note and edit **开始** / **结束** in its frontmatter.

- **I dragged an entry to another row but no file moved.**  
  Only the folder grouping moves real files under `事件/`; grouping by field changes display order only.

### Writing and sidebars

- **Selecting text and planting a foreshadowing does nothing?**  
  Work inside the `正文/` folder of a registered work, and check that novel writing is enabled in settings.

- **Why can't I edit notes in a shared lore group?**  
  Shared content is read-only in the borrowing work. Edit it in the source work.

- **I cannot find a sidebar entry.**  
  Look at the left ribbon or search the command palette; some modules have to be turned on in **Settings → Novel-kit** first.

- **Word counts and today's progress look wrong.**  
  The home page counts manuscripts inside the active workspace. Check that you selected the right work, then refresh.

### Export · templates · misc

- **There is no export entry.**  
  The export feature is **currently hidden** (all entries hidden, code kept). This is intended; it will return in a later version.

- **New files get no template / wrong names.**  
  Check the file-template rules and the template folder; name mapping lives in the same place.

- **Focus writing does not centre.**  
  Turn on **focus writing** and make sure you are in editing mode, not preview.

### Mobile

- **Two settings tabs are missing on my phone.**  
  CSS snippets and export depend on desktop capabilities and are not registered at all on mobile; export is also hidden on desktop right now. This is intended.

- **The home page looks squeezed on my phone.**  
  Make sure the **mobile layout** is the active template; you can also drag a narrow-screen variant out of the default layout on desktop.

If none of that helps: hit refresh in the novel panel, or run *Rebuild current work's node graph* from the command palette, and check that sync has not rolled back anything under `System/`.

---

## Where your data lives

| Content | Location |
| --- | --- |
| Work list, active work, global settings | The plugin's `data.json` (`.obsidian/plugins/novel-kit/data.json`), `novel` and sibling sections |
| View layouts, filter rules, home templates, todos | `System/*.json` inside the work (graph / timeline / fission / table / cards / home …) |
| Lore, events, manuscript, inspiration, glossary | The Markdown notes themselves, inside the work folder |
| Sticky notes | Under the work's `System/` |
| Snapshots | The snapshot folder (see the retention policy on the Snapshots tab) |

Deleting the plugin's `data.json` loses work registrations and global settings; **no note content is touched**. Deleting a work's `System/*.json` only resets that bit of view configuration.

---

## Network use

**The plugin collects no telemetry, uploads no notes, and works fully offline.** Only the features below reach the network, and only when you trigger them:

| Feature | How it's triggered | Endpoint contacted | Notes |
| --- | --- | --- | --- |
| Word-frequency tokenizer dictionaries | Clicking "Download" for a dictionary in settings | `cdn.jsdelivr.net` (jieba small/default/big), `www.mdbg.net` (CC-CEDICT) | Download only; saved to `.obsidian/plugins/novel-kit/word-freq-dicts/` |
| Homepage "web table" widget | Entering a URL and clicking "Fetch" | The URL you entered | Fetches that page's HTML and parses it into a table |

Both paths only **read from** the remote end and send nothing back. Without a downloaded dictionary, word frequency still works using the built-in stop-word list, with lower segmentation accuracy.

All requests go through Obsidian's `requestUrl`, so they honour the proxy and bypass rules configured in the app.

---

## Development

The entry point is `src/main.ts`: it loads the aggregated settings and then initialises each feature manager.

```text
novel · wordcount · naming-kit · json-studio · vault-search · phone-preview ·
file-tree-sort · css-snippets · export · snapshot · typewriter
```

Only `css-snippets` and `export` are **desktop-only**: guarded by `Platform.isDesktop`, and absent from the mobile settings tabs. `export` is currently **hidden altogether** (code kept).

`file-templates` is mounted as a settings module and called when files are created or scaffolds are written.

```text
src/
  main.ts
  features/     # feature modules
  ui/           # shared components
  I18N/         # zh-CN / en
  obsidian/     # settings, parsing, types
  utils/
scripts/        # 5 utility scripts (see below)
tests/
  unit/         # vitest: home templates / sample data / style rules
  visual/       # visual regression (pixel-by-pixel screenshot diff)
```

### Checks

| Command | What it does |
| --- | --- |
| `npm test` | all vitest suites (home templates / sample data / style rules) |
| `npm run check` | svelte-check type pass |
| `npm run check:ui-style` | style rules only (R7–R10 must be 0, R1–R6 must not grow) |
| `npm run visual:check` | visual regression; run `npm run build` first |
| `npm run visual:smoke` | self-proof: inject a style change, it must be detected |
| `npm run lint` / `npm run format` | Biome |

Everything kept in `scripts/` is **live**: `gen-theme-vars.ts` (token manifest generator),
`patch-vendor-types.mjs` (postinstall type patches), `visual-skin.mjs` (skin re-verification),
`ui-style-report.ts` (style-rule listing / baseline report), `extract-obsidian-tokens.py`
(extracts Obsidian's real tokens).

### Conventions

- Development output lands in `test-vault/.obsidian/plugins/novel-kit/`; never edit a user's vault directly.
- **Inside the plugin, always use Obsidian's `requestUrl` rather than a bare `fetch`** — only the former honours Obsidian's proxy bypass list.
- The standard shape for a new feature: `manager.ts` + `appView.ts` + `settings.ts` under `src/features/<name>/`, then register it in `main.ts`.
- The UI component library lives in `src/ui/components/`; check there before writing a new component.
