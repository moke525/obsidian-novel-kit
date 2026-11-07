# Novel-kit complete reference

> [!IMPORTANT]
> **This plugin is built for the desktop version — desktop only.**

This is the long form of the [README](../README.en.md). The README gets you started; this page holds the **full lists**: entry points, views, settings, storage locations and troubleshooting.

[中文](reference.zh-CN.md)

---

## Contents

1. [Entry points](#entry-points)
2. [Work workspace](#work-workspace)
3. [Studio home](#studio-home)
4. [Studio panel: seven views](#studio-panel-seven-views)
5. [Causal · plot · manuscript](#causal--plot--manuscript)
6. [Sidebars and writing aids](#sidebars-and-writing-aids)
7. [Vault-wide features](#vault-wide-features)
8. [Shared lore groups](#shared-lore-groups)
9. [Settings](#settings)
10. [Suggested workflow](#suggested-workflow)
11. [Troubleshooting](#troubleshooting)
12. [Where your data lives](#where-your-data-lives)
13. [Network use](#network-use)
14. [Development](#development)

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
| git-branch | Causal ledger | right sidebar |
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

- **Open**: studio home / novel panel / each sub-view / word frequency / proofreading / causal / inspiration / glossary / plot / marks / word count / naming / search / phone preview / CSS snippets / snapshots
- **Create**: register workspace / sticky note / inspiration
- **Toggle**: highlight settings, sticky notes, file-tree word count, end-of-line word count, stage ruler, selection word count, focus mode
- **Selection**: extract to sticky note / inspiration / highlight file / highlight comment
- **Insert**: timeline / table / cards view block (drops a ready-to-use inline view code block at the cursor)
- **Maintenance**: rebuild node graph, re-apply file-tree sort, reload CSS snippets

Editor context menus add: remove blank lines, anchor the selected text to a 因 / 痕 / 果 entry, add or recycle a mark, extract to sticky note / inspiration / highlight file / highlight comment, add to dictionary, and feature toggles.

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
```

Content is plain Markdown plus frontmatter; view layouts and templates live in `System/*.json`.

### Workspace modes

| Mode | Difference |
| --- | --- |
| **Simple** | One fewer view (no fission); the graph has no pack / piece drilling; causal is replaced by the “marks” wording |
| **Full** | Every view, including causal and plot cross-check |

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
| **Narrow layout** | Narrow screens | Single-column list scroll + auto-fit grid + tabs folding the data area, no splitPanel |

The narrow layout avoids splitPanels because on a 390px screen a 72/28 split leaves the right pane a few dozen pixels wide, and every chart collapses into a vertical line.

---

## Studio panel: seven views

Top bar: work dropdown + refresh, then one row of view tabs: **graph · timeline · fission · map · spacetime · cards · table**.

| View | What it does |
| --- | --- |
| **Graph** | Relationship graph: `关系` / `relation` field links, org structures, pack / piece drilling. Toolbar **filter** controls visibility and special styles, **display config** controls type mapping and colours |
| **Timeline** | Scenes / chapters / beats arranged by time; with grouping set to folder, dragging moves the real file; the toolbar's **Play timeline** steps through events in chronological order. View config can add **marker periods** — spanning the header down through the body, draggable and collapsible from their head; when collapsed the period is removed from the axis and replaced by a hatched divider no wider than the **maximum width** setting, labelled with its start / end times, shifting later ticks and events leftward. Events dropped onto their edges are nudged clear automatically |
| **Fission** | Multi-column card outline (reads `事件/` by default). Hidden in simple mode |
| **Map** | Markers on a base image; the spacetime view needs at least one map |
| **Spacetime** | Three dimensions: x / y = map, z = time; per-character trail mode available |
| **Cards** | Configurable wall of fields; pick fields and controls in the template editor; grouping and sorting support multiple schemes (switching a scheme swaps the whole configuration; the right side is read-only until a scheme is selected) |
| **Table** | Grouping, filtering, pinned columns, inline editing; grouping / sorting / conditional formatting each support multiple schemes, and conditional formatting colours cells by field condition; shares the same rule components as the graph; system fields such as uuid and relation / timestamp keys are hidden by default and can be re-enabled in the columns panel |

**Highlight settings** are not in the panel: they live in **Settings → Highlight settings** and are global for every registered work. Word lists can be collected from all registered works; a legacy `System/highlight.json` inside a work is imported once when needed.

### Inline views (code blocks)

Timeline, table and cards can also live directly in any note's body:

```novel-timeline
height: 560
```

```novel-table
height: 560
```

```novel-cards
height: 560
```

- `height` is in pixels, 200–1600, default 560; optional.
- **Data comes from the work that owns the note**: put the block in another work's note and you see that work's data, not the currently open one.
- **Display config is per block**: changing columns / filters / grouping / sorting / conditional formatting / templates inside a block writes back to that block's own `config: {...}` line, and only the `height` / `config` lines are rewritten. One block never affects another block or the panel. Multiple blocks of the same kind in one note stay independent too, and a write-back only replaces the lines of its own block; an inline timeline holds off writing while a config panel is open, so the panel is not closed by a write-back. Search terms and the current page are transient and are not written into the block.
- **Inline timeline markers and inline cards grouping / sorting schemes are per block too**: marker add / remove, maximum width and collapsed state, as well as a scheme's selection and contents, write back to that block's own config and never rewrite the work archive.
- Blocks without a `config` line keep following the work archive (timeline, table and cards each follow their own archive).

---

## Causal · plot · manuscript

**The main operations happen in the manuscript.** The graph and its siblings are visualisations.

| | Manuscript | Causal file | Plot |
| --- | --- | --- | --- |
| Role | Drafting and the entry point for anchoring | Records 因 / 痕 / 果 | Cross-checks the outline |
| Where | Select text in the manuscript or an event note, right-click to anchor | Add / edit / jump from the causal ledger | Ribbon scroll-text (read-only) |

### How causal files are recognised

Any Markdown inside a work counts as a causal file when its `tags` contain `因果` — no folder convention. The plugin **does not provide a create-causal-file entry**; when no causal file exists the panel shows an empty-state hint.

The three slots are `因`, `痕`, `果`. Each is an object field storing “entry id → entry object”; an empty slot is `{}`. The owning line lives in `因果线` (default `主线`).

```yaml
---
tags: [因果]
因果线: 主线
因:
  1a2b:
    id: 1a2b
    label: A disappearance in the rain
    content: Who took the person away that night
    tags: [clue]
    anchors:
      - path: 事件/开篇.md
        type: 事件
        position: { from: 120, to: 132 }
        text: 雨夜里少了个人
痕: {}
果: {}
---
```

An entry's `content` is free-form notes and `tags` are custom labels. Each anchor is `{ path, type, position, text }`: `type` is `事件` (event note) or `正文` (anything else), `position` is an absolute document offset `{ from, to }` (frontmatter included, same as editor selections), and `text` stores the selected text at anchor time for comparison.

### How status is derived (never persisted)

An anchor holds when the file exists **and** the text at `position` still equals the recorded `text` (leading / trailing whitespace ignored).

| Slot | Event anchor holds | Event anchor fails | Body anchor holds | Body anchor fails | No anchors |
| --- | --- | --- | --- | --- | --- |
| `因` / `痕` | 已设 (set) | 失设 (unset) | 已种 (planted) | 失种 (unplanted) | 悬空 (dangling) |
| `果` | 已育 (raised) | 空育 (empty) | 已收 (collected) | 丢失 (lost) | 悬空 (dangling) |

With several anchors, any success wins; when all fail the event state takes priority. Hovering or jumping reports the reason (file missing, position out of range, text at the position changed, and so on).

### Causal ledger panel

Open it from the `git-branch` ribbon or the command; it is available only in full mode with **Causal panel** enabled in settings. Four views sit on top: **all causal / 因 / 痕 / 果**. Each causal file gets one card showing all three slots; entries carry a status badge and anchor chips, and can be added / edited / deleted, unanchored, or jumped to. Docked in the right sidebar the panel is a single column; dragged into a tab the cards switch to an adaptive grid.

### Anchoring and jumping

Select text in the editor → right-click **Anchor as causal** → pick a 因 / 痕 / 果 entry: offsets are normalised automatically, event notes are recorded as `事件` and everything else as `正文`, and anchoring the same position twice is rejected. Clicking an entry in the panel returns to the anchored position and selects that range; if the file was deleted or the text changed, you get a clear warning instead of a wrong jump.

Legacy `伏笔` / `钩子` arrays in frontmatter are no longer read, and are never rewritten or migrated automatically.

Details live in `System/示例导览.md` inside the work (Chinese).

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

Full-text search and replace; tree-edit your `System/*.json`; manage `.obsidian/snippets`. CSS snippets depend on desktop capabilities.

---

## Shared lore groups

**Settings → Novel writing → Shared lore groups**: several works share one world view, referencing lore read-only (plus optional eras / scenes). Shared files never leave the source vault, carry a shared badge in views, and are protected from accidental edits.

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
2. Select key sentences in the manuscript or an event note → right-click to anchor them to a 因 / 痕 / 果 entry.
3. Keep **plot** open while writing; sweep statuses in the **causal ledger** (失设 / 失种 / 空育 / 丢失 / 悬空); clicking an entry returns to its anchor.
4. Open graph / timeline / fission / map / spacetime when you need relationships, pacing or space.
5. Check fields in table / cards, word usage in word frequency, suspects in proofreading, goals in word count, layout in phone preview; snapshot important moments by hand.

Inspiration → drag into graph / timeline / fission → fill in fields → generate manuscript → **back to selecting text in the draft to anchor it**.

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

- **Selecting text and anchoring it as causal does nothing?**  
  Make sure the file belongs to a registered work, novel writing is enabled, the workspace mode is full, and the causal panel is not switched off.

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

Only `css-snippets` and `export` are **desktop-only** (guarded by `Platform.isDesktop`). `export` is currently **hidden altogether** (code kept).

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
