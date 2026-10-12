/* ============================================================
   Novel-kit showcase — app.js
   Bilingual (zh/en) + dark/light theme + SVG mockups
   ============================================================ */
;(function () {
	'use strict'

	var C = {
		accent: 'var(--accent)',
		accent2: 'var(--accent-2)',
		border: 'var(--border)',
		dim: 'var(--text-dim)',
		faint: 'var(--text-faint)',
		good: 'var(--good)',
		warn: 'var(--warn)',
		panel: 'var(--bg-elev)',
		card2: 'var(--bg-card-2)',
	}
	function s(name, extra) {
		return 'style="fill:' + C[name] + (extra ? ';' + extra : '') + '"'
	}
	function st(name, extra) {
		return 'style="stroke:' + C[name] + (extra ? ';' + extra : '') + '"'
	}

	/* ---------- i18n static strings ---------- */
	var DICT = {
		zh: {
			'nav.features': '功能',
			'nav.tools': '创作工具',
			'nav.install': '安装',
			'nav.start': '快速开始',
			'nav.faq': '常见问题',
			'nav.pricing': '定价',
			'hero.badge': 'Obsidian 插件 · 桌面优先',
			'hero.title': '为长篇写作服务的<br/>Obsidian 一站式套件',
			'hero.lead': '一部作品就是库里的一个文件夹。设定、大纲、正文全是明文 Markdown——七个联动的视图，加一套随你自定义的配色与高亮，陪你写完一整本书。',
			'hero.cta1': '在 Obsidian 中安装',
			'hero.cta2': '查看 GitHub 仓库',
			'hero.p1': '七个视图',
			'hero.p2': '明文 Markdown',
			'hero.p3': '完全离线',
			'hero.p4': '桌面优先',
			'nav.highlight': '高亮',
			'highlight.title': '自定义高亮 · 你的 vault，你的风格',
			'highlight.sub':
				'用 CSS 片段与三色自定义配色，把库调成顺眼的模样。墨 / 纸 / 强调色三个旋钮一改即生效，还能经 Style Settings 逐项微调——高亮、背景、链接，全听你的。',
			'strip.1': '一部作品 = 一个文件夹',
			'strip.2': '设定 / 大纲 / 正文 全是 Markdown',
			'strip.3': '七大视图看同一批笔记',
			'strip.4': '你的笔记，永远在你手里',
			'features.title': '七大视图，一套笔记',
			'features.sub': '从宏观的世界观到微观的每一句话，Novel-kit 用七个相互联动的视图陪你写完一整本书。',
			'tools.title': '创作辅助工具',
			'tools.sub': '九个轻量但顺手的小工具，散落在写作流程的各个角落，帮你把灵感接住、把文字打磨干净。',
			'install.title': '安装',
			'install.sub': '需要 Obsidian 1.8.7 或更高版本（仅桌面端）。',
			'start.title': '快速开始',
			'start.sub': '三步，从空文件夹到动笔。',
			'faq.title': '常见问题',
			'faq.sub': '大多数「看不起来」的问题，都是这三件事之一。',
			'privacy.title': '数据 & 隐私',
			'privacy.p1': '设定、大纲与正文都是你自己 vault 里的 Markdown 笔记。插件只额外维护两份东西：',
			'privacy.d1': '作品列表、当前激活作品、全局设置。删掉会丢注册信息，碰不到任何笔记。',
			'privacy.d2': '视图布局、筛选规则、主页模板等。删掉只重置那一小块视图配置。',
			'privacy.p2': '插件本身完全离线可用，不收集任何遥测，不上传你的笔记。',
			'footer.tag': '为长篇写作服务的 Obsidian 套件',
			'footer.issues': '提交问题',
			'footer.releases': '版本发布',
			'footer.project': '项目',
			'footer.thanks': '致谢（开源组件）',
			'footer.built': '用 ✍️ 与代码写就，祝你写作愉快。',
			'pricing.title': '定价',
			'pricing.sub': '全部功能可免费试用 30 天（自首次打开小说面板起算），试用结束后需要授权码继续使用。',
			'pricing.halfYear': '半年',
			'pricing.yearly': '一年',
			'pricing.perpetual': '永久',
			'pricing.d183': '183 天',
			'pricing.d365': '365 天',
			'pricing.lifetime': '不限时长',
			'pricing.best': '一次买断',
			'pricing.note': '授权一机一码；按天档续费可叠加时长。安装后在插件设置的「授权」页输入授权码即可激活。',
			'contact.title': '联系我们',
			'contact.sub': '购买授权码、换机转移、反馈问题，都可以通过下面的方式找到我们。',
			'contact.qqLabel': 'QQ 群',
			'contact.wechatLabel': '微信',
		},
		en: {
			'nav.features': 'Features',
			'nav.tools': 'Toolkit',
			'nav.install': 'Install',
			'nav.start': 'Get started',
			'nav.faq': 'FAQ',
			'nav.pricing': 'Pricing',
			'hero.badge': 'Obsidian plugin · Desktop-first',
			'hero.title': 'An all-in-one Obsidian toolkit<br/>for long-form writing',
			'hero.lead':
				'One folder is one novel. Settings, outlines, and drafts are plain Markdown — seven linked views, plus a color & highlight scheme you fully control.',
			'hero.cta1': 'Install in Obsidian',
			'hero.cta2': 'View on GitHub',
			'hero.p1': 'Seven views',
			'hero.p2': 'Plain Markdown',
			'hero.p3': 'Fully offline',
			'hero.p4': 'Desktop-first',
			'nav.highlight': 'Highlight',
			'highlight.title': 'Custom highlighting · your vault, your style',
			'highlight.sub':
				'Use CSS snippets and a 3-color palette to make the vault feel like yours. Three knobs — ink / paper / accent — apply instantly, and every variable can be fine-tuned via Style Settings.',
			'strip.1': 'One folder = one novel',
			'strip.2': 'Settings / outline / draft are Markdown',
			'strip.3': 'Seven views, one set of notes',
			'strip.4': 'Your notes stay in your hands',
			'features.title': 'Seven views, one notebook',
			'features.sub': 'From the grand worldview down to a single sentence, seven linked views carry you through the whole book.',
			'tools.title': 'Creative toolkit',
			'tools.sub': 'Nine lightweight helpers tucked along your writing flow — catch the inspiration, polish the prose.',
			'install.title': 'Install',
			'install.sub': 'Requires Obsidian 1.8.7 or later (desktop only).',
			'start.title': 'Get started',
			'start.sub': 'Three steps from an empty folder to writing.',
			'faq.title': 'FAQ',
			'faq.sub': "Most “can't see my novel” issues come down to one of these three things.",
			'privacy.title': 'Data & privacy',
			'privacy.p1': 'Settings, outlines and drafts are Markdown notes inside your own vault. The plugin only keeps two extra things:',
			'privacy.d1': 'work list, active work, and global settings. Deleting it loses registration info but never touches your notes.',
			'privacy.d2': 'view layout, filter rules, home templates, etc. Deleting one only resets that small slice of config.',
			'privacy.p2': 'The plugin itself is fully offline — no telemetry, no uploading your notes.',
			'footer.tag': 'An Obsidian toolkit for long-form writing',
			'footer.issues': 'Report issue',
			'footer.releases': 'Releases',
			'footer.project': 'Project',
			'footer.thanks': 'Thanks (open source)',
			'footer.built': 'Written with ✍️ and code. Happy writing!',
			'pricing.title': 'Pricing',
			'pricing.sub': 'Every feature is free to try for 30 days (counted from the first time you open the novel panel); a licence key is required afterwards.',
			'pricing.halfYear': 'Half year',
			'pricing.yearly': 'Yearly',
			'pricing.perpetual': 'Lifetime',
			'pricing.d183': '183 days',
			'pricing.d365': '365 days',
			'pricing.lifetime': 'No time limit',
			'pricing.best': 'One-time purchase',
			'pricing.note': 'One licence per machine; day-based plans stack. After installing, enter your licence key on the “Licence” page in the plugin settings.',
			'contact.title': 'Contact us',
			'contact.sub': 'Buy a licence, transfer to a new machine, or report issues — reach us through either channel below.',
			'contact.qqLabel': 'QQ group',
			'contact.wechatLabel': 'WeChat',
		},
	}

	/* ---------- feature data ---------- */
	var FEATURES = [
		{
			icon: '🏠',
			mock: 'home',
			zh: { t: '创作主页', en: 'Home', d: '进度与 KPI、每日码字曲线与热力图、词频、待办、时钟。组件可拖拽增删，布局写进作品的 System/home.json。' },
			en: {
				t: 'Home dashboard',
				en: 'Home',
				d: "Progress & KPIs, daily writing curve & heatmap, word frequency, todos, clock. Drag widgets in/out; layout saved to the work's System/home.json.",
			},
		},
		{
			icon: '🕸️',
			mock: 'graph',
			zh: { t: '关系图', en: 'Relations', d: '关系与伏笔 / 钩子的可视化。「筛选」管哪些文件显示与特殊样式，「显示配置」管文件类型、配色与连线。' },
			en: {
				t: 'Relation graph',
				en: 'Relations',
				d: 'Visualize relationships, foreshadowing and hooks. “Filter” controls which files show and get special styles; “Display config” controls types, colors and links.',
			},
		},
		{
			icon: '📅',
			mock: 'timeline',
			zh: { t: '时间线', en: 'Timeline', d: '按时间排场景；分组选「文件夹」时拖动会真的移动文件；起止日期直接改 frontmatter。' },
			en: {
				t: 'Timeline',
				en: 'Timeline',
				d: 'Arrange scenes on a timeline. In folder groups, dragging really moves files; start/end dates edit frontmatter directly.',
			},
		},
		{
			icon: '🧬',
			mock: 'fission',
			zh: { t: '裂变', en: 'Fission', d: '多列卡片大纲；拖动调整情节顺序；卡片就是笔记，改的是同一份文件；右键改事件类型（时代 / 场景 / 章节 / 情节）。' },
			en: {
				t: 'Fission outline',
				en: 'Fission',
				d: 'Multi-column card outline. Drag to reorder; cards are notes editing the same file; right-click to change event type.',
			},
		},
		{
			icon: '🗺️',
			mock: 'map',
			zh: { t: '地图与时空', en: 'Map & Spacetime', d: '底图打坐标标记；时空把地图当平面、时间当 z 轴；坐标写成「地图名：x，y」（全角冒号与逗号）。' },
			en: {
				t: 'Map & Spacetime',
				en: 'Map & Spacetime',
				d: 'Plot coordinates on a base map; Spacetime uses the map as plane and time as z-axis. Coordinates written as “Map: x, y” (full-width punctuation).',
			},
		},
		{
			icon: '🃏',
			mock: 'cards',
			zh: { t: '卡片与表格', en: 'Cards & Tables', d: '卡片是可配置的字段墙；表格能分组、过滤、钉列、就地改字段；两者都支持拖拽排序与跨组拖拽。' },
			en: {
				t: 'Cards & Tables',
				en: 'Cards & Tables',
				d: 'Cards are configurable field walls; tables group, filter, pin columns, edit in place; both support drag sorting and cross-group dragging.',
			},
		},
		{
			icon: '🧵',
			mock: 'foreshadow',
			zh: {
				t: '伏笔 · 钩子 · 剧情 · 正文',
				en: 'Foreshadowing',
				d: '主操作全在正文里：框选句子 → 右键 → 埋设 / 回收，状态走 未埋设 → 已埋设 → 已关联 → 已回收。',
			},
			en: {
				t: 'Foreshadowing · hooks',
				en: 'Foreshadowing',
				d: 'Core actions live in the text: select a sentence → right-click → plant/recover. Status flows Planted → Linked → Recovered.',
			},
		},
	]

	var TOOLS = [
		{
			e: '💡',
			zh: { t: '灵感卡片', d: '可直接拖进关系图 / 时间线 / 裂变变成情节。' },
			en: { t: 'Inspiration cards', d: 'Drag straight into the graph, timeline or fission to become a plot beat.' },
		},
		{ e: '📖', zh: { t: '词条', d: '设定速查，按层级组织。' }, en: { t: 'Glossary', d: 'Quick-lookup for worldbuilding, organized by hierarchy.' } },
		{ e: '🔤', zh: { t: '词频', d: '统计正文用词，看出偏好与重复。' }, en: { t: 'Word frequency', d: 'Tally words in your drafts to spot habits and repetition.' } },
		{ e: '✨', zh: { t: '校对', d: '就地检查，逐条确认修改。' }, en: { t: 'Proofread', d: 'Inline checks, confirm each fix one by one.' } },
		{ e: '🎯', zh: { t: '码字目标', d: '每日目标与进度提醒。' }, en: { t: 'Writing goals', d: 'Daily targets with progress nudges.' } },
		{ e: '🏷️', zh: { t: '取名', d: '按风格生成角色与地名。' }, en: { t: 'Name generator', d: 'Generate character and place names by style.' } },
		{
			e: '📄',
			zh: { t: '文件模板', d: '按「目标文件夹 + 文件名格式」自动套模板并重命名。' },
			en: { t: 'File templates', d: 'Auto-apply templates and rename by target folder + name format.' },
		},
		{ e: '📸', zh: { t: '历史快照', d: '自动存档，恢复前能左右对比。' }, en: { t: 'Snapshots', d: 'Auto-archive notes; compare side by side before restoring.' } },
		{ e: '📌', zh: { t: '悬浮便签', d: '随手记，自动保存。' }, en: { t: 'Sticky notes', d: 'Jot anything; auto-saved.' } },
	]

	var HIGHLIGHT = {
		zh: [
			'三色旋钮：墨 / 纸 / 强调色，一改即混入风格 CSS',
			'CSS 片段级作用域，只为你的 vault 上色',
			'对接 Style Settings，逐项微调变量',
			'预设主题与自定义片段自由切换',
		],
		en: [
			'Three knobs — ink / paper / accent — mixed into the style CSS on change',
			'Snippet-scoped styling that only paints your vault',
			'Wired to Style Settings for per-variable fine-tuning',
			'Switch freely between presets and your own snippets',
		],
	}

	var INSTALL = {
		zh: [
			{ h: '社区插件市场', pill: '推荐', steps: ['设置 → 第三方插件 → 浏览', '搜索 <code>novel-kit</code>', '安装并启用'] },
			{
				h: '手动安装',
				pill: '',
				steps: [
					'下载 <code>main.js</code> / <code>manifest.json</code> / <code>styles.css</code>',
					'放进 <code>&lt;vault&gt;/.obsidian/plugins/novel-kit/</code>',
					'在设置里启用',
				],
			},
		],
		en: [
			{ h: 'Community store', pill: 'Recommended', steps: ['Settings → Community plugins → Browse', 'Search <code>novel-kit</code>', 'Install and enable'] },
			{
				h: 'Manual install',
				pill: '',
				steps: [
					'Download <code>main.js</code> / <code>manifest.json</code> / <code>styles.css</code>',
					'Put them in <code>&lt;vault&gt;/.obsidian/plugins/novel-kit/</code>',
					'Enable in Settings',
				],
			},
		],
	}

	var STEPS = {
		zh: [
			'<b>注册一部作品</b>：打开创作主页点「新增作品」，或运行命令「注册小说工作区」，文件夹里会自动铺好 设定 / 事件 / 正文 / 灵感 / System。',
			'<b>先看示例（可选）</b>：库里没有作品时，面板顶部出现「加载示例」，写入一部《残虹夜雨》——跟着导览走一遍最快。',
			'<b>开始写</b>：在 正文/ 下写稿，框选句子埋伏笔与钩子；需要看全局时再打开小说创作面板。',
		],
		en: [
			'<b>Register a work</b>: open Home and click “New work”, or run “Register novel workspace”. A folder is populated with 设定 / 事件 / 正文 / 灵感 / System.',
			'<b>Try the sample (optional)</b>: with no works, a “Load sample” button appears — it writes a demo novel 《残虹夜雨》. Follow the tour.',
			'<b>Start writing</b>: draft under 正文/, select sentences to plant foreshadowing; open the novel panel when you need the big picture.',
		],
	}

	var FAQ = {
		zh: [
			{ q: '一部作品看不起来？', a: '通常是三件事：没注册作品（先「新增作品」）、创作面板顶部没选中它、或者 正文/ 路径不对（要在已注册作品的 正文/ 下写作）。' },
			{
				q: '关系图里找不到笔记？',
				a: '默认「仅显示有关联」把没有关系的节点藏了起来——关掉该选项，或给它加一条关联；整类不显示则去「筛选」或「显示配置」勾选文件类型。',
			},
			{ q: '地图上看不到标记？', a: '检查笔记里的坐标写成「地图名：x，y」（冒号与逗号都是全角），且地图的显示类型包含 locale。' },
			{ q: '时间线改了没生效？', a: '直接去改笔记 frontmatter 里的「开始」「结束」字段即可，视图会随之更新。' },
			{ q: '字数与今日进度对不上？', a: '主页统计的是当前作品工作区里的正文，先确认选中了正确的作品再刷新。' },
			{
				q: '插件会联网吗？',
				a: '插件本身完全离线可用，不收集遥测、不上传笔记。只有词频 / 校对的分词词典（你点「下载」时）与主页网页表格组件（你填网址并获取时）会在你主动触发时联网下载数据到本地。',
			},
		],
		en: [
			{
				q: "Can't see my novel?",
				a: "Usually one of three things: the work isn't registered (click “New work” first), it isn't selected at the top of the panel, or the 正文/ path is wrong (write under the registered work's 正文/).",
			},
			{
				q: 'Notes missing in the graph?',
				a: 'By default “show only linked” hides nodes with no relations — turn it off, or add a relation. If a whole type is hidden, check “Filter” or “Display config” for file types.',
			},
			{
				q: 'No markers on the map?',
				a: "Coordinates must be written as “Map: x, y” (full-width colon and comma), and the map's display type must include locale.",
			},
			{ q: "Timeline edits didn't apply?", a: "Edit the “开始” / “结束” fields in the note's frontmatter directly; the view updates from there." },
			{ q: 'Word count / progress mismatch?', a: "Home counts drafts in the current work's workspace — make sure the right work is selected, then refresh." },
			{
				q: 'Does the plugin use the network?',
				a: 'The plugin is fully offline — no telemetry, no uploading. Only the word-frequency/proofread dictionaries (when you click Download) and the home web-table widget (when you fetch a URL) connect, to download data locally.',
			},
		],
	}

	/* ---------- SVG mockups ---------- */
	function heroSVG() {
		var defs =
			'<defs><linearGradient id="area" x1="0" y1="0" x2="0" y2="1">' +
			'<stop offset="0%" ' +
			s('accent', 'stop-opacity:0.45') +
			'/>' +
			'<stop offset="100%" ' +
			s('accent', 'stop-opacity:0.02') +
			'/></linearGradient></defs>'
		var panel = '<rect x="0" y="0" width="480" height="320" rx="16" ' + s('panel') + ' ' + st('border', 'stroke-width:1.5') + '/>'
		var bar =
			'<rect x="16" y="14" width="10" height="10" rx="3" ' +
			s('accent') +
			'/>' +
			'<rect x="32" y="14" width="10" height="10" rx="3" ' +
			s('border') +
			'/>' +
			'<rect x="48" y="14" width="10" height="10" rx="3" ' +
			s('border') +
			'/>'
		// KPI cards
		var kpi = ''
		var kx = [16, 172, 328]
		for (var i = 0; i < 3; i++) {
			kpi +=
				'<rect x="' +
				kx[i] +
				'" y="48" width="136" height="62" rx="10" ' +
				s('card2') +
				' ' +
				st('border', 'stroke-width:1') +
				'/>' +
				'<rect x="' +
				(kx[i] + 12) +
				'" y="60" width="60" height="8" rx="4" ' +
				s('dim', 'opacity:0.5') +
				'/>' +
				'<rect x="' +
				(kx[i] + 12) +
				'" y="78" width="48" height="16" rx="4" ' +
				s('accent2') +
				'/>' +
				'<rect x="' +
				(kx[i] + 12) +
				'" y="100" width="92" height="6" rx="3" ' +
				s('border') +
				'/>'
		}
		// chart
		var chart =
			'<rect x="16" y="126" width="300" height="150" rx="10" ' +
			s('card2') +
			' ' +
			st('border', 'stroke-width:1') +
			'/>' +
			'<polyline points="30,250 70,210 110,228 150,170 190,196 230,140 270,168 300,120" fill="none" ' +
			st('accent2', 'stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round') +
			'/>' +
			'<polygon points="30,250 70,210 110,228 150,170 190,196 230,140 270,168 300,120 300,260 30,260" ' +
			s('accent', 'opacity:1') +
			' fill="url(#area)"/>' +
			'<line x1="30" y1="262" x2="300" y2="262" ' +
			st('border', 'stroke-width:1') +
			'/>'
		// heatmap
		var heat = '<rect x="332" y="126" width="132" height="74" rx="10" ' + s('card2') + ' ' + st('border', 'stroke-width:1') + '/>'
		var hc = [
			'accent',
			'accent2',
			'border',
			'good',
			'accent',
			'border',
			'accent2',
			'accent',
			'border',
			'good',
			'accent2',
			'border',
			'accent',
			'good',
			'border',
			'accent2',
			'border',
			'accent',
			'good',
			'border',
			'accent2',
			'border',
			'accent',
			'border',
		]
		for (var r = 0; r < 4; r++)
			for (var c = 0; c < 6; c++) {
				heat += '<rect x="' + (342 + c * 19) + '" y="' + (136 + r * 15) + '" width="14" height="10" rx="3" ' + s(hc[r * 6 + c], 'opacity:0.85') + '/>'
			}
		// clock
		var clock =
			'<rect x="332" y="210" width="132" height="66" rx="10" ' +
			s('card2') +
			' ' +
			st('border', 'stroke-width:1') +
			'/>' +
			'<circle cx="368" cy="243" r="22" ' +
			s('panel') +
			' ' +
			st('accent2', 'stroke-width:2') +
			'/>' +
			'<line x1="368" y1="243" x2="368" y2="228" ' +
			st('accent', 'stroke-width:2.5;stroke-linecap:round') +
			'/>' +
			'<line x1="368" y1="243" x2="380" y2="243" ' +
			st('dim', 'stroke-width:2.5;stroke-linecap:round') +
			'/>' +
			'<rect x="402" y="226" width="52" height="8" rx="4" ' +
			s('dim', 'opacity:0.5') +
			'/>' +
			'<rect x="402" y="242" width="40" height="8" rx="4" ' +
			s('border') +
			'/>' +
			'<rect x="402" y="258" width="46" height="8" rx="4" ' +
			s('border') +
			'/>'
		return '<svg viewBox="0 0 480 320" role="img" aria-label="Novel-kit home dashboard">' + defs + panel + bar + kpi + chart + heat + clock + '</svg>'
	}

	function mockSVG(type) {
		var W = 400,
			H = 200
		var frame = '<rect x="1" y="1" width="' + (W - 2) + '" height="' + (H - 2) + '" rx="10" ' + s('panel') + ' ' + st('border', 'stroke-width:1.2') + '/>'
		if (type === 'graph') {
			var nodes = [
				[70, 60],
				[180, 40],
				[300, 70],
				[120, 130],
				[250, 140],
				[330, 150],
				[200, 95],
			]
			var edges = [
				[0, 1],
				[1, 2],
				[0, 3],
				[1, 4],
				[3, 4],
				[4, 5],
				[2, 5],
				[1, 6],
				[6, 3],
				[6, 4],
			]
			var e = ''
			edges.forEach(function (p) {
				e +=
					'<line x1="' +
					nodes[p[0]][0] +
					'" y1="' +
					nodes[p[0]][1] +
					'" x2="' +
					nodes[p[1]][0] +
					'" y2="' +
					nodes[p[1]][1] +
					'" ' +
					st('border', 'stroke-width:1.4') +
					'/>'
			})
			var n = ''
			nodes.forEach(function (p, i) {
				var fill = i === 1 || i === 6 ? 'accent' : i === 4 ? 'accent2' : 'card2'
				var rad = i === 1 || i === 6 ? 13 : 9
				n += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + rad + '" ' + s(fill) + ' ' + st('border', 'stroke-width:1.2') + '/>'
			})
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + e + n + '</svg>'
		}
		if (type === 'timeline') {
			var ax = '<line x1="20" y1="160" x2="380" y2="160" ' + st('dim', 'stroke-width:1.6') + '/>'
			var bars = [
				[40, 90],
				[90, 130],
				[140, 70],
				[190, 110],
				[240, 60],
				[290, 100],
				[340, 80],
			]
			var b = ''
			bars.forEach(function (p, i) {
				var h = p[1]
				b +=
					'<rect x="' +
					p[0] +
					'" y="' +
					(160 - h) +
					'" width="26" height="' +
					h +
					'" rx="4" ' +
					s(i % 3 === 0 ? 'accent' : 'accent2', 'opacity:0.85') +
					'/>'
				b += '<circle cx="' + (p[0] + 13) + '" cy="160" r="3.5" ' + s('dim') + '/>'
			})
			var link = '<path d="M53,70 C80,55 103,55 103,30" fill="none" ' + st('warn', 'stroke-width:1.6;stroke-dasharray:4 3') + '/>'
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + ax + b + link + '</svg>'
		}
		if (type === 'fission') {
			var cols = [40, 165, 290]
			var heights = [
				[60, 44],
				[50, 70, 40],
				[56, 48],
			]
			var f = ''
			cols.forEach(function (cx, ci) {
				f += '<rect x="' + cx + '" y="24" width="78" height="152" rx="8" ' + s('card2') + ' ' + st('border', 'stroke-width:1') + '/>'
				var y = 36
				heights[ci].forEach(function (hh, ri) {
					f +=
						'<rect x="' +
						(cx + 8) +
						'" y="' +
						y +
						'" width="62" height="' +
						(hh - 14) +
						'" rx="5" ' +
						s((ci + ri) % 2 === 0 ? 'accent' : 'accent2', 'opacity:0.8') +
						'/>'
					y += hh
				})
			})
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + f + '</svg>'
		}
		if (type === 'map') {
			var map = '<rect x="30" y="24" width="240" height="152" rx="8" ' + s('card2') + ' ' + st('border', 'stroke-width:1.2') + '/>'
			var grid = ''
			for (var gx = 0; gx <= 4; gx++)
				grid +=
					'<line x1="' +
					(30 + gx * 60) +
					'" y1="24" x2="' +
					(30 + gx * 60) +
					'" y2="176" ' +
					st('border', 'stroke-width:0.8;stroke-dasharray:3 3') +
					'/>'
			for (var gy = 0; gy <= 3; gy++)
				grid +=
					'<line x1="30" y1="' +
					(24 + gy * 50) +
					'" x2="270" y2="' +
					(24 + gy * 50) +
					'" ' +
					st('border', 'stroke-width:0.8;stroke-dasharray:3 3') +
					'/>'
			var pts = [
				[80, 70],
				[150, 110],
				[210, 60],
				[120, 140],
			]
			var pp = ''
			pts.forEach(function (p, i) {
				pp += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + (i === 1 ? 7 : 5) + '" ' + s(i === 1 ? 'warn' : 'accent2') + '/>'
			})
			var z =
				'<rect x="300" y="24" width="70" height="152" rx="8" ' +
				s('panel') +
				' ' +
				st('border', 'stroke-width:1.2') +
				'/>' +
				'<line x1="335" y1="40" x2="335" y2="160" ' +
				st('dim', 'stroke-width:1.4') +
				'/>' +
				'<circle cx="335" cy="40" r="4" ' +
				s('accent') +
				'/>' +
				'<circle cx="335" cy="100" r="4" ' +
				s('accent2') +
				'/>' +
				'<circle cx="335" cy="160" r="4" ' +
				s('dim') +
				'/>' +
				'<text x="352" y="44" font-size="10" ' +
				s('dim') +
				'>T+</text>' +
				'<text x="352" y="164" font-size="10" ' +
				s('dim') +
				'>T-</text>'
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + map + grid + pp + z + '</svg>'
		}
		if (type === 'cards') {
			var tbl = '<rect x="24" y="28" width="352" height="146" rx="8" ' + s('card2') + ' ' + st('border', 'stroke-width:1.2') + '/>'
			var t = ''
			// header
			for (var c2 = 0; c2 < 4; c2++) t += '<rect x="' + (32 + c2 * 86) + '" y="38" width="78" height="22" rx="4" ' + s('accent', 'opacity:0.3') + '/>'
			for (var r2 = 0; r2 < 4; r2++)
				for (var c3 = 0; c3 < 4; c3++) {
					t +=
						'<rect x="' +
						(32 + c3 * 86) +
						'" y="' +
						(66 + r2 * 24) +
						'" width="78" height="18" rx="3" ' +
						s((r2 + c3) % 3 === 0 ? 'accent2' : 'panel', 'opacity:0.7') +
						'/>'
				}
			// pinned column marker
			t += '<rect x="24" y="28" width="6" height="146" rx="3" ' + s('warn') + '/>'
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + tbl + t + '</svg>'
		}
		if (type === 'foreshadow') {
			var lines = [
				'<rect x="28" y="34" width="120" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>' +
					'<rect x="152" y="34" width="60" height="9" rx="4" ' +
					s('accent') +
					'/>' +
					'<rect x="216" y="34" width="100" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>',
				'<rect x="28" y="62" width="200" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>' +
					'<rect x="232" y="62" width="50" height="9" rx="4" ' +
					s('accent2') +
					'/>' +
					'<rect x="286" y="62" width="30" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>',
				'<rect x="28" y="90" width="160" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>' +
					'<rect x="192" y="90" width="70" height="9" rx="4" ' +
					s('accent') +
					'/>' +
					'<rect x="266" y="90" width="50" height="9" rx="4" ' +
					s('dim', 'opacity:0.5') +
					'/>',
			].join('')
			var flow =
				'<rect x="28" y="130" width="78" height="34" rx="17" ' +
				s('accent2', 'opacity:0.25') +
				'/>' +
				'<rect x="118" y="130" width="78" height="34" rx="17" ' +
				s('accent', 'opacity:0.35') +
				'/>' +
				'<rect x="208" y="130" width="78" height="34" rx="17" ' +
				s('good', 'opacity:0.3') +
				'/>' +
				'<rect x="298" y="130" width="74" height="34" rx="17" ' +
				s('dim', 'opacity:0.25') +
				'/>' +
				'<text x="67" y="152" font-size="11" text-anchor="middle" ' +
				s('accent2') +
				'>plant</text>' +
				'<text x="157" y="152" font-size="11" text-anchor="middle" ' +
				s('accent') +
				'>link</text>' +
				'<text x="247" y="152" font-size="11" text-anchor="middle" ' +
				s('good') +
				'>recover</text>' +
				'<text x="335" y="152" font-size="11" text-anchor="middle" ' +
				s('dim') +
				'>done</text>'
			return '<svg viewBox="0 0 ' + W + ' ' + H + '">' + frame + lines + flow + '</svg>'
		}
		// home fallback
		return heroSVG()
	}

	function mockHighlightSVG() {
		var frame = '<rect x="1" y="1" width="398" height="198" rx="10" ' + s('panel') + ' ' + st('border', 'stroke-width:1.2') + '/>'
		var lc = '<rect x="20" y="24" width="168" height="152" rx="10" ' + s('card2') + ' ' + st('border', 'stroke-width:1') + '/>'
		var ltitle = '<rect x="34" y="38" width="86" height="9" rx="4" ' + s('dim', 'opacity:0.5') + '/>'
		var rows = [
			['#1f2937', '墨 ink'],
			['#e2e8f0', '纸 paper'],
			[null, '强调 accent'],
		]
		var y = 60,
			left = ''
		rows.forEach(function (r) {
			left += '<rect x="34" y="' + y + '" width="74" height="8" rx="4" ' + s('dim', 'opacity:0.45') + '/>'
			var sw = r[0] ? 'style="fill:' + r[0] + '"' : s('accent')
			left += '<rect x="146" y="' + (y - 5) + '" width="28" height="18" rx="5" ' + sw + ' ' + st('border', 'stroke-width:1') + '/>'
			y += 36
		})
		var rc = '<rect x="204" y="24" width="176" height="152" rx="10" style="fill:#f8fafc" ' + st('border', 'stroke-width:1') + '/>'
		var text = [
			'<rect x="218" y="40" width="120" height="9" rx="4" style="fill:#334155"/>',
			'<rect x="218" y="60" width="150" height="6" rx="3" style="fill:#94a3b8"/>',
			'<rect x="218" y="72" width="140" height="6" rx="3" style="fill:#94a3b8"/>',
			'<rect x="218" y="86" width="58" height="9" rx="4" ' + s('accent') + '/>',
			'<rect x="280" y="86" width="78" height="6" rx="3" style="fill:#94a3b8"/>',
			'<rect x="218" y="102" width="150" height="6" rx="3" style="fill:#94a3b8"/>',
			'<rect x="218" y="116" width="120" height="6" rx="3" style="fill:#94a3b8"/>',
		].join('')
		return '<svg viewBox="0 0 400 200" role="img" aria-label="Custom highlight theme editor">' + frame + lc + ltitle + left + rc + text + '</svg>'
	}

	/* ---------- render ---------- */
	function pick(o) {
		return o[currentLang] || o.zh
	}

	function renderStatic() {
		var nodes = document.querySelectorAll('[data-i18n]')
		nodes.forEach(function (n) {
			var key = n.getAttribute('data-i18n')
			var val = (DICT[currentLang] && DICT[currentLang][key]) || DICT.zh[key] || ''
			n.innerHTML = val
		})
	}

	function renderFeatures() {
		var html = FEATURES.map(function (f) {
			var t = pick(f)
			return (
				'<article class="feature-card reveal">' +
				'<div class="feature-top">' +
				'<div class="feature-icon">' +
				f.icon +
				'</div>' +
				'<div><h3 class="feature-title">' +
				t.t +
				'</h3>' +
				'<div class="feature-en">' +
				t.en +
				'</div></div></div>' +
				'<p class="feature-desc">' +
				t.d +
				'</p>' +
				'<div class="feature-mock">' +
				mockSVG(f.mock) +
				'</div>' +
				'</article>'
			)
		}).join('')
		document.getElementById('featureGrid').innerHTML = html
	}

	function renderTools() {
		var html = TOOLS.map(function (t) {
			var o = pick(t)
			return (
				'<div class="tool-card reveal"><div class="tool-emoji">' +
				t.e +
				'</div>' +
				'<div class="tool-body"><h4>' +
				o.t +
				'</h4><p>' +
				o.d +
				'</p></div></div>'
			)
		}).join('')
		document.getElementById('toolGrid').innerHTML = html
	}

	function renderHighlight() {
		var arr = HIGHLIGHT[currentLang] || HIGHLIGHT.zh
		document.getElementById('highlightList').innerHTML = arr
			.map(function (x) {
				return '<li>' + x + '</li>'
			})
			.join('')
		document.getElementById('highlightArt').innerHTML = mockHighlightSVG()
	}

	function renderInstall() {
		var arr = INSTALL[currentLang] || INSTALL.zh
		var html = arr
			.map(function (c) {
				return (
					'<div class="install-card reveal"><h3>' +
					c.h +
					(c.pill ? ' <span class="pill">' + c.pill + '</span>' : '') +
					'</h3><ol>' +
					c.steps
						.map(function (s2) {
							return '<li>' + s2 + '</li>'
						})
						.join('') +
					'</ol></div>'
				)
			})
			.join('')
		document.getElementById('installGrid').innerHTML = html
	}

	function renderSteps() {
		var arr = STEPS[currentLang] || STEPS.zh
		document.getElementById('stepsList').innerHTML = arr
			.map(function (x) {
				return '<li>' + x + '</li>'
			})
			.join('')
	}

	function renderFAQ() {
		var arr = FAQ[currentLang] || FAQ.zh
		var html = arr
			.map(function (f) {
				return (
					'<div class="faq-item reveal"><button class="faq-q">' +
					f.q +
					'<span class="chev">▾</span></button><div class="faq-a"><div class="faq-a-inner">' +
					f.a +
					'</div></div></div>'
				)
			})
			.join('')
		document.getElementById('faqList').innerHTML = html
		document.querySelectorAll('.faq-q').forEach(function (btn) {
			btn.addEventListener('click', function () {
				var item = btn.parentElement
				var a = btn.nextElementSibling
				var open = item.classList.toggle('open')
				a.style.maxHeight = open ? a.scrollHeight + 'px' : '0'
			})
		})
	}

	function renderAll() {
		renderStatic()
		renderFeatures()
		renderHighlight()
		renderTools()
		renderInstall()
		renderSteps()
		renderFAQ()
		observeReveal()
	}

	/* ---------- reveal observer ---------- */
	var io = null
	function observeReveal() {
		if (io) io.disconnect()
		io = new IntersectionObserver(
			function (entries) {
				entries.forEach(function (e) {
					if (e.isIntersecting) {
						e.target.classList.add('in')
						io.unobserve(e.target)
					}
				})
			},
			{ threshold: 0.12 },
		)
		document.querySelectorAll('.reveal:not(.in)').forEach(function (el) {
			io.observe(el)
		})
	}

	/* ---------- language / theme ---------- */
	var currentLang = 'zh'
	function setLang(l) {
		currentLang = l
		document.documentElement.lang = l === 'zh' ? 'zh-CN' : 'en'
		try {
			localStorage.setItem('nk-lang', l)
		} catch (e) {}
		renderAll()
	}
	function setTheme(t) {
		document.documentElement.setAttribute('data-theme', t)
		try {
			localStorage.setItem('nk-theme', t)
		} catch (e) {}
		var icon = document.querySelector('#themeBtn .theme-icon')
		if (icon) icon.textContent = t === 'dark' ? '🌙' : '☀️'
	}

	/* ---------- init ---------- */
	function init() {
		try {
			currentLang = localStorage.getItem('nk-lang') || 'zh'
		} catch (e) {}
		var savedTheme = 'dark'
		try {
			savedTheme = localStorage.getItem('nk-theme') || 'dark'
		} catch (e) {}
		setTheme(savedTheme)
		setLang(currentLang)
		document.getElementById('heroArt').innerHTML = heroSVG()
		var y = document.getElementById('year')
		if (y) y.textContent = new Date().getFullYear()

		document.getElementById('langBtn').addEventListener('click', function () {
			setLang(currentLang === 'zh' ? 'en' : 'zh')
		})
		document.getElementById('themeBtn').addEventListener('click', function () {
			var cur = document.documentElement.getAttribute('data-theme')
			setTheme(cur === 'dark' ? 'light' : 'dark')
		})
		var menuBtn = document.getElementById('menuBtn')
		var navLinks = document.getElementById('navLinks')
		menuBtn.addEventListener('click', function () {
			var open = navLinks.classList.toggle('open')
			menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false')
		})
		navLinks.querySelectorAll('a').forEach(function (a) {
			a.addEventListener('click', function () {
				navLinks.classList.remove('open')
				menuBtn.setAttribute('aria-expanded', 'false')
			})
		})
	}

	if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init)
	else init()
})()
