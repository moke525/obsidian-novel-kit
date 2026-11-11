# -*- coding: utf-8 -*-
"""Generate Novel-kit guide pages into obsidian-novel-kit/pages/.

站点分两层：根 index.html 是产品主页（手工维护），本脚本只负责 pages/ 下的指南页。
历史上它会把总览写进根 index.html，把主页覆盖掉，已移除该行为。
"""
from __future__ import annotations

from pathlib import Path
import shutil
import sys

# 允许从任意工作目录执行本脚本，也能 import 同目录的章节渲染器
sys.path.insert(0, str(Path(__file__).resolve().parent))
from guide_sections import render_guide, validate_facts  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / "pages"
REPO_ASSETS = ROOT.parent / "assets"

NAV = [
	("开始", [
		("index", "指南总览"),
		("install", "安装"),
		("workspace", "作品工作区"),
		("settings", "插件设置"),
		("commands", "命令与入口"),
	]),
	("创作面板", [
		("home", "创作主页"),
		("panel", "创作面板"),
		("graph", "关系图"),
		("timeline", "时间线"),
		("timesystem", "时间体系"),
		("thread", "脉络"),
		("fission", "裂变"),
		("map", "地图"),
		("spacetime", "时空"),
		("cards", "卡片"),
		("table", "表格"),
		("inline", "内联视图"),
	]),
	("伏笔与剧情", [
		("destiny", "命运蓝图"),
		("foreshadow", "伏笔总览"),
		("plot", "剧情对照"),
		("marks", "标记账本"),
		("journal", "作品日志"),
	]),
	("写作辅助", [
		("inspiration", "灵感库"),
		("glossary", "词条"),
		("wordfreq", "词频"),
		("proofread", "校对"),
		("sticky", "悬浮便签"),
		("wordcount", "码字与字数"),
		("naming", "取名"),
		("phone", "手机预览"),
	]),
	("全局能力", [
		("highlight", "高亮"),
		("templates", "文件模板"),
		("filesort", "文件树排序"),
		("css", "CSS 片段"),
		("typewriter", "写作模式"),
		("snapshot", "历史快照"),
		("search", "高级搜索"),
		("json", "JSON Studio"),
		("series", "共享设定组"),
		("export", "导出"),
	]),
	("问题", [
		("faq", "常见问题"),
		("data", "数据与隐私"),
	]),
]


BLURBS = {
	"index": "本页",
	"install": "市场 / 手动安装、桌面限制",
	"workspace": "注册作品、目录与 tags",
	"settings": "全部设置页签",
	"commands": "命令面板、Ribbon、右键菜单",
	"home": "KPI、模板、日志",
	"panel": "八个视图怎么切",
	"graph": "筛选、pack、连线、正文节点",
	"timeline": "拖档期、文件夹分组、标记时段",
	"timesystem": "现实历法与自定义单位链",
	"thread": "蓝图、桑基、轨道圆点",
	"fission": "多列大纲与情绪曲线",
	"map": "全角坐标与 locale",
	"spacetime": "地图平面 × 时间",
	"cards": "模板与字段墙",
	"table": "钉列、方案、条件格式",
	"inline": "笔记内代码块视图",
	"destiny": "命运文件夹与蓝图节点",
	"foreshadow": "侧栏总览、筛选与跳转",
	"plot": "正文对照情节大纲",
	"marks": "选区标记与回收",
	"journal": "命运相关操作记录",
	"inspiration": "提取与拖成情节",
	"glossary": "类型文件 + 逐行词条",
	"wordfreq": "当前文件分词",
	"proofread": "错词与加入词典",
	"sticky": "悬浮、同步原文",
	"wordcount": "目标与四处字数开关",
	"naming": "批量取名",
	"phone": "窄屏排版预览",
	"highlight": "标记高亮与伏笔高亮",
	"templates": "新建即套模板",
	"filesort": "中文数字排序",
	"css": "snippets 与三色旋钮",
	"typewriter": "打字机、禅模式、海明威",
	"snapshot": "对比与恢复",
	"search": "全文搜索替换",
	"json": "编辑 System JSON",
	"series": "只读共享源卷",
	"export": "入口隐藏，命令仍在",
	"faq": "对不上号时从这里跳",
	"data": "data.json 与联网范围",
}



# 站点分两层：根 index.html = 产品主页（由 site/home.js + site/styles.css 驱动，
# 不归本生成器管）；pages/*.html = 指南页（含指南总览 pages/index.html）。
# 所有指南页都在同一个目录里，因此页间链接一律是同目录相对路径；
# 只有「回主页」与取 ../site/、../assets/ 才需要上一级。
def href(page_id: str, here: str) -> str:
	"""指南页之间的链接；here 仅为兼容既有调用点保留。"""
	return f"{page_id}.html"


def home_href() -> str:
	"""回到产品主页。"""
	return "../index.html"


def asset(name: str, here: str) -> str:
	return f"../assets/{name}"


def site(name: str, here: str) -> str:
	return f"../site/{name}"


def sidebar(here: str) -> str:
	chunks = ['<nav class="sidebar" id="sidebar" aria-label="文档目录">']
	for group, items in NAV:
		chunks.append(f"<h2>{group}</h2>")
		for pid, title in items:
			cls = ' class="active"' if pid == here else ""
			chunks.append(f'<a href="{href(pid, here)}"{cls}>{title}</a>')
	chunks.append("</nav>")
	return "\n".join(chunks)


def shell(here: str, title: str, crumb: str, body: str, prev_next: str) -> str:
	hub = href("index", here)
	crumb_html = (
		f'主页 / <a href="{home_href()}">Novel-kit</a> / 使用指南'
		if here == "index"
		else f'主页 / <a href="{home_href()}">Novel-kit</a> / <a href="{hub}">使用指南</a> / {crumb}'
	)
	return f"""<!doctype html>
<html lang="zh-CN" data-theme="dark">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} · Novel-kit 使用指南</title>
<meta name="description" content="Novel-kit 使用指南：{title}" />
<link rel="stylesheet" href="{site('docs.css', here)}" />
</head>
<body>
<header class="topbar">
<button class="icon-btn menu-btn" id="menuBtn" aria-label="打开目录" aria-expanded="false">☰</button>
<a class="brand" href="{home_href()}"><span class="brand-mark">N</span><span>Novel-kit</span></a>
<span class="crumb">{crumb_html}</span>
<div class="top-actions">
<a class="icon-btn" href="{home_href()}">主页</a>
<a class="icon-btn" href="../README.en.md">English</a>
<button class="icon-btn" id="themeBtn" title="切换主题"><span class="theme-icon">🌙</span></button>
</div>
</header>
<div class="layout">
{sidebar(here)}
<main class="article">
{body}
{prev_next}
<footer class="footer">© <span id="year"></span> Novel-kit · 仅桌面端 · Apache-2.0</footer>
</main>
</div>
<script src="{site('app.js', here)}"></script>
</body>
</html>
"""


def pager(here: str) -> str:
	flat = [item for _, items in NAV for item in items]
	idx = next(i for i, (pid, _) in enumerate(flat) if pid == here)
	prev_html = next_html = ""
	if idx > 0:
		pid, title = flat[idx - 1]
		prev_html = f'<a href="{href(pid, here)}"><span class="dir">上一篇</span>{title}</a>'
	if idx < len(flat) - 1:
		pid, title = flat[idx + 1]
		next_html = f'<a href="{href(pid, here)}" style="text-align:right"><span class="dir">下一篇</span>{title}</a>'
	return f'<nav class="pager">{prev_html}{next_html}</nav>'


def shot(file: str, alt: str, here: str) -> str:
	return f'<img class="shot" src="{asset(file, here)}" alt="{alt}" />'


def C(kind: str, title: str, html: str) -> str:
	return f'<div class="callout callout-{kind}"><div class="callout-title">{title}</div>{html}</div>'


# ---------- page bodies (here is filled later) ----------

def pages(here: str) -> dict[str, tuple[str, str]]:
	"""id -> (h1, inner html without pager)."""
	a = lambda f, alt: shot(f, alt, here)
	h = here
	return {
		"install": ("安装", f"""
<p class="lead">把 Novel-kit 装进桌面版 Obsidian。最低版本 1.8.7，manifest 声明仅桌面端。</p>
{C("important","Important","<p>不要在手机 / 平板上依赖本插件。创作面板、时空、CSS 片段、导出都按桌面交互编写。</p>")}
<h2>社区插件市场</h2>
<ol class="steps">
<li>设置 → 第三方插件 → 关闭安全模式。</li>
<li>浏览，搜索 <code>novel-kit</code>，安装并启用。</li>
<li>左侧 Ribbon 应出现房子（主页）和书本（创作面板）。若没有，到设置 → Novel-kit → 小说创作检查总开关与 Ribbon 勾选。</li>
</ol>
<h2>手动安装</h2>
<ol class="steps">
<li>从 GitHub Releases 取 <code>main.js</code>、<code>manifest.json</code>、<code>styles.css</code>。</li>
<li>放到 <code>&lt;库&gt;/.obsidian/plugins/novel-kit/</code>。</li>
<li>启用插件。改过 <code>manifest.json</code> 后必须重启 Obsidian。</li>
</ol>
<h2>注意事项</h2>
<ul>
<li>开发构建：生产输出在本目录；开发输出在测试库 <code>.obsidian/plugins/novel-kit/</code>。</li>
<li>试验功能请用空库，避免误改正式稿件（与 <a href="https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin" target="_blank" rel="noopener">Obsidian 插件教程</a> 同一原则）。</li>
</ul>
"""),
		"workspace": ("作品工作区", f"""
<p class="lead">一部作品 = 库里的一个根文件夹。插件只登记路径，笔记仍是你的 Markdown。</p>
<h2>怎么注册</h2>
<ol class="steps">
<li>创作主页「新增作品」，或命令「注册小说工作区」。</li>
<li>选空文件夹或已有作品根。插件铺脚手架（已有同名目录不会覆盖内容）。</li>
<li>在创作面板顶部下拉选中该作品。换电脑后打开同一 Vault 即可，注册信息在插件 <code>data.json</code>。</li>
</ol>
<h2>目录约定</h2>
<pre><code>作品根/
  设定/角色|地点|道具|功法|&lt;自定义分类&gt;/
  事件/          era / scene / chapter / plot
  正文/          tags: text
  命运/          因果蓝图 markdown（脉络工具栏可改文件夹名）
  灵感/ 词条/
  System/        视图 json，不要手改</code></pre>
<h2>类型怎么认</h2>
<ul>
<li>认的是 frontmatter <code>tags</code>，不是只认文件夹名。</li>
<li>设定可用中文 tag（角色/地点）或英文（character/locale）。</li>
<li>事件必须英文：<code>era</code> <code>scene</code> <code>chapter</code> <code>plot</code>。写成「章节」能当节点，但<strong>进不了时间线</strong>。</li>
<li>每篇要有稳定 <code>uuid</code>，创建时由插件写入，不要改、不要复用。</li>
</ul>
{C("note","Note","<p>旧「简单模式」已取消，始终全功能。关掉某个 Ribbon 只隐藏入口，不会删笔记。</p>")}
{C("warning","Warning","<p>「加载示例」只在库内还没有任何已注册作品时出现。已有作品后入口会关掉，避免冲掉你的登记。</p>")}
{C("note","Note","<p>设置文案里若仍出现「简单 / 全功能」创作模式，运行时始终按全功能：会建事件文件夹，八个面板视图都在。</p>")}
"""),
		"settings": ("插件设置", f"""
<p class="lead">路径：设置 → Novel-kit。多数 Ribbon 可单独关闭：关掉会藏图标并关掉已打开的对应视图。</p>
<table><thead><tr><th>页签</th><th>管什么</th></tr></thead><tbody>
<tr><td>小说创作</td><td>总开关、Ribbon、重建防抖、新标签打开文件、词频词典、共享设定组</td></tr>
<tr><td>高亮设置</td><td>标记高亮、伏笔高亮、正则/文件名/注释/敏感词/对白</td></tr>
<tr><td>文件模板</td><td>目标文件夹、文件名格式、模板文件、取名、自动填充</td></tr>
<tr><td>文件树排序</td><td>中文数字、自然数、自定义词序</td></tr>
<tr><td>CSS 片段</td><td>桌面端 snippets 与主题配色旋钮</td></tr>
<tr><td>写作模式</td><td>打字机居中</td></tr>
<tr><td>历史快照</td><td>自动存档、保留份数</td></tr>
<tr><td>字数统计</td><td>文件树 / 行末 / 阶段标尺 / 框选</td></tr>
<tr><td>取名工具</td><td>一次生成条数</td></tr>
<tr><td>其他</td><td>高级搜索、手机预览、JSON Studio</td></tr>
<tr><td>导出</td><td>当前隐藏</td></tr>
</tbody></table>
<h2>注意事项</h2>
<ul>
<li>改 Ribbon 后，下一次打开菜单即生效，不必重启。</li>
<li>「在新标签页打开文件」会影响文件树、双链和插件视图里的打开行为。</li>
<li>开发页签「测试」只在开发构建出现。</li>
<li>关掉「启用小说创作」后，Ribbon、相关命令、工作区文件监听全部停掉；笔记不会删。</li>
<li>关掉某个功能入口后，对应「打开××」命令也不再生效。</li>
</ul>
"""),
		"commands": ("命令与入口", f"""
<p class="lead">命令面板（Ctrl/Cmd+P）搜中文名即可。Ribbon 可在设置 → 小说创作 → 功能入口里逐个关掉。</p>
<h2>小说创作</h2>
<table><thead><tr><th>命令</th><th>做什么</th></tr></thead><tbody>
<tr><td>打开创作主页</td><td>Ribbon 房子。设置可「启动时打开创作主页」（新标签，不覆盖已开笔记）。</td></tr>
<tr><td>打开小说创作面板</td><td>Ribbon 书本。再切八个 Tab。</td></tr>
<tr><td>打开时间线 / 脉络 / 裂变 / 地图 / 时空 / 卡片 / 关系图 / 表格视图</td><td>打开面板并切到该 Tab。</td></tr>
<tr><td>打开伏笔面板</td><td>右侧伏笔总览。</td></tr>
<tr><td>打开剧情面板 / 灵感库 / 词条面板 / 词频面板 / 校对面板 / 标记账本</td><td>对应侧栏。</td></tr>
<tr><td>注册小说工作区</td><td>选作品根文件夹。</td></tr>
<tr><td>重建当前作品节点图</td><td>索引乱了时用。冷启动重建不阻塞界面。</td></tr>
<tr><td>新建灵感 / 提取选区为灵感</td><td>写入 <code>灵感/</code>。</td></tr>
<tr><td>新建悬浮便签 / 开关 / 隐藏全部 / 显示 / 提取选区</td><td>见 <a href="{href('sticky',h)}">悬浮便签</a>。</td></tr>
<tr><td>开关高亮设置</td><td>整套装饰开或关。</td></tr>
<tr><td>提取选区为高亮文件 / 高亮注释</td><td>见 <a href="{href('highlight',h)}">高亮</a>。</td></tr>
</tbody></table>
<h2>其它模块</h2>
<ul>
<li>码字：打开面板、给当前正文设目标/冲刺、四处字数开关。</li>
<li>写作模式：打开菜单、关闭、切到某一预设。</li>
<li>历史快照：打开面板、存档当前、清理。</li>
<li>高级搜索：停靠面板、浮动窗。</li>
<li>JSON Studio：打开当前 JSON / 新标签。</li>
<li>CSS 片段：打开编辑、重新加载。</li>
<li>文件树排序：重新应用。</li>
<li>取名、手机预览：各一条打开命令。</li>
<li>导出：打开导出面板、导出当前文件、导出当前文件夹（Ribbon / 设置里无入口，命令仍已注册）。</li>
</ul>
<h2>编辑器 / 文件树右键（需已打开作品）</h2>
<ul>
<li>正文：添加伏笔、添加到标记 / 回收标记、关联到情节/场景、编辑/清除故事线、提取灵感/便签/高亮。</li>
<li>功能开关：字数四处显示、高亮总开关。</li>
<li>文件树：码字目标、条目样式、隐藏 <code>_index</code> 时「打开文件夹文件」。</li>
</ul>
{C("warning","Warning","<p>无活动作品时，多数创作命令会提示先注册工作区。共享源卷上的写入菜单不可用。</p>")}
"""),
		"home": ("创作主页", f"""
<p class="lead">Ribbon 房子图标。仪表盘，不是第二套正文编辑器。</p>
{a("home.png","创作主页")}
<h2>怎么打开</h2>
<p>Ribbon home，或命令「打开创作主页」。</p>
<h2>组件</h2>
<table><thead><tr><th>组件</th><th>操作</th></tr></thead><tbody>
<tr><td>当前作品</td><td>看进度，点进创作面板；从这里新增 / 重命名 / 删除作品登记</td></tr>
<tr><td>KPI</td><td>全库字数、今日净增量（last−start）与实际增量（max−start）</td></tr>
<tr><td>每日码字 / 热力图</td><td>只统计<strong>当前作品工作区</strong>里的正文</td></tr>
<tr><td>词频</td><td>当前作品用词</td></tr>
<tr><td>待办</td><td>写在 <code>System/home.json</code>，关库再开还在</td></tr>
<tr><td>网页表格</td><td>填 URL → 获取；会联网请求该地址</td></tr>
<tr><td>每日一句</td><td>必须指定库内某篇 md 当数据源</td></tr>
<tr><td>作品日志</td><td>记录命运文件增删与关联，分类名显示为「命运」</td></tr>
</tbody></table>
<h2>改布局</h2>
<ol class="steps">
<li>右上角齿轮 → 主页模板。窗口可拖、可缩放。</li>
<li>左侧：页面背景图与高度、布局类型、组件列表、选中节点属性。窄屏收成抽屉。</li>
<li>画布上拖组件换位置或换容器。布局：<code>list</code> 单列、<code>grid</code> 自适应、<code>splitPanel</code> 两栏、<code>tabs</code> 页签。</li>
</ol>
<p>首次按视口挑默认模板：宽屏多层 splitPanel，窄屏单列（避免 390px 再切两栏只剩几十像素）。两套都保留，可随时切回。</p>
{C("warning","Warning","<p>字数对不上时，先看顶部选中的是不是你以为的那部作品，以及稿子是否在该作品的 <code>正文/</code> 下。</p>")}
"""),
		"panel": ("创作面板", f"""
<p class="lead">Ribbon 书本。顶部：作品下拉 + 刷新，然后一层视图 Tab。</p>
<h2>视图一览</h2>
<table><thead><tr><th>Tab</th><th>看什么</th></tr></thead><tbody>
<tr><td><a href="{href('graph',h)}">关系图</a></td><td>人物组织地点与 pack 嵌套</td></tr>
<tr><td><a href="{href('timeline',h)}">时间线</a></td><td>按开始/结束排大纲</td></tr>
<tr><td><a href="{href('thread',h)}">脉络</a></td><td>命运蓝图 + 正文/事件轨道</td></tr>
<tr><td><a href="{href('fission',h)}">裂变</a></td><td>多列卡片大纲</td></tr>
<tr><td><a href="{href('map',h)}">地图</a> / <a href="{href('spacetime',h)}">时空</a></td><td>平面标记与三维轨迹</td></tr>
<tr><td><a href="{href('cards',h)}">卡片</a> / <a href="{href('table',h)}">表格</a></td><td>同一批笔记的字段墙与表</td></tr>
</tbody></table>
<h2>操作</h2>
<ul>
<li>换作品：只用顶部下拉，不要靠「当前打开的那篇笔记」猜。无活动作品时各 Tab 是空态。</li>
<li>切 Tab 默认 keep-alive，不销毁，布局还在 <code>System/workspace.json</code>。</li>
<li>外部改了文件：点刷新；裂变有时还要再点该视图的重新加载。</li>
<li>索引乱了：命令「重建当前作品节点图」。启动时重建是异步的，大库会先出界面再补节点。</li>
<li>共享源卷节点只读，带徽章。</li>
</ul>
{C("tip","Tip","<p>这些 Tab 读写同一批 Markdown。在表格改「开始」日期，时间线也会变。</p>")}
"""),
		"graph": ("关系图", f"""
<p class="lead">设定与事件笔记画成图。连线来自 frontmatter 的关系字段；pack/piece 按文件夹嵌套。</p>
{a("graph.png","关系图")}
<h2>怎么打开</h2>
<p>创作面板 Tab「关系图」，或从带关系字段的笔记右键「编辑关系图」聚焦该节点。</p>
<h2>工具栏</h2>
<ul>
<li>左上拖出类型到画布 = 按筛选允许的类型<strong>新建笔记</strong>。</li>
<li>漏斗 = 筛选规则（显示/隐藏/样式，从上到下）。</li>
<li>齿轮 = 显示配置：文件 type 如何映射成角色/组织/地点/pack/piece/正文。</li>
<li>「只显示有关系的文件」：没有关系、参与者等关联的节点会被藏起来。</li>
<li>创建连线：点按钮后依次点两个节点；或按住 Shift 点起点再点终点。</li>
<li>缩放、适合视图、力导向布局、对齐、全选、全屏。</li>
</ul>
<h2>节点与连线</h2>
<ul>
<li>双击场景 pack 下钻；面包屑返回（当前实现已取消面包屑导航的话，用工具栏返回/退出下钻）。</li>
<li>pack 上参与者、地点、关联事件字段左侧有圆点，可拖到对应类型节点。</li>
<li>正文节点：参与者/地点/关联事件可连线；伏笔用 Markdown 双链跳转命运文件；摘要是 textarea，失焦写入。</li>
<li>章节/情节角标的伏笔状态来自命运蓝图，不读事件 FM 槽。</li>
<li>组织节点可展开结构、改组织类型。</li>
<li>右键：颜色（右侧 color picker 圆点）、固定、移入/移出 pack、复制尺寸、删除等。</li>
<li>连线右键：改标签、粗细、颜色、方向、删除。标签下方弹出编辑。</li>
<li>中继节点已取消，不要找「添加中继」。</li>
</ul>
<h2>复制粘贴</h2>
<p>复制按路径拷笔记；剪切会进回收站，粘贴用缓存全文重建。共享源卷节点只读，不能当写入端。</p>
{C("warning","Warning","<p>重启后角色不见：先关掉「只显示有关系的文件」，或给它连一条关系。某一类整类消失：去筛选/显示配置勾选该类型。</p>")}
"""),
		"timeline": ("时间线", f"""
<p class="lead">按笔记「开始」「结束」排场景、章节、情节。拖动就是改档期。</p>
{a("timeline.png","时间线")}
<h2>怎么打开</h2>
<p>创作面板 Tab「时间线」。历法在时间体系弹窗里配（含自定义历法）。</p>
<h2>操作细节</h2>
<ul>
<li>拖条块改起止，松手写回该事件笔记 frontmatter。</li>
<li><strong>分组方式 = 文件夹</strong>：拖到另一行会移动 <code>事件/</code> 下真实文件。</li>
<li><strong>分组方式 = 字段</strong>（故事线等）：只改显示，不挪文件。正文右键「编辑故事线 / 清除故事线」写的就是这个字段。</li>
<li>工具栏「播放时间线」按时间先后逐个高亮。</li>
<li>「添加分组字段」之后，编辑器右键才能把当前事件设到某条线索。</li>
<li>标记时段：纵跨全部轨道，可拖、可在头部折叠；折叠后压成不超过「最大宽度」的斜线隔离带，后续刻度左移。事件块压到时段起止线会自动让位。</li>
<li>行高在压缩布局下按泳道均分，单条不低于最小高度。</li>
</ul>
{C("warning","Warning","<p>拖了文件路径却没变：检查分组是不是「文件夹」。保存后日期没变：直接打开 md 看「开始」「结束」键（中文落盘）。</p>")}
<p>历法换算见 <a href="{href('timesystem',h)}">时间体系</a>。内联时间线见 <a href="{href('inline',h)}">内联视图</a>：面板与代码块配置互相独立。</p>
"""),
		"timesystem": ("时间体系", f"""
<p class="lead">时间线刻度用哪套历法。默认「现实时间」。可自建单位链（由细到粗）的幻想历。</p>
<h2>怎么打开</h2>
<ol class="steps">
<li>创作面板 → 时间线 → 视图配置 / 历法（界面文案为「时间体系」一类入口）。</li>
<li>选内置现实时间，或新建自定义系统。</li>
</ol>
<h2>自定义历法</h2>
<ul>
<li>单位按<strong>由细到粗</strong>排列，界面自上而下，顶行最细（如「时」在「日」上面）。</li>
<li>每个单位只配「进制」：含多少个下一级。长度固定，不能做成「这个月 29 天、下个月 31 天」。</li>
<li>可拖动单位行排序。锚定行和「添加单位」不在拖拽区内。</li>
<li>日期格式用单位名拼显示样例；事件「开始」「结束」按当前历法解析。</li>
<li>内置现实时间仍有变长月 / 闰年，只用于它自己，不影响你在编辑器里建的系统。</li>
</ul>
<h2>数据落盘</h2>
<p>系统列表在插件 <code>data.json</code> 的 <code>novel.timeSystems</code>，不是作品 System。各作品时间线只记录「选用哪套」。</p>
{C("warning","Warning","<p>填了「146年3月」却写不进去：格式必须能被当前历法解析，且结束晚于开始。解析失败会保留原值。</p>")}
"""),
		"thread": ("脉络", f"""
<p class="lead">上半是命运蓝图（节点 + 桑基），下半是正文/事件多轨道。伏笔挂在蓝图节点上，不是事件 FM。</p>
<h2>怎么打开</h2>
<p>创作面板 Tab「脉络」。工具栏最左选一份因果/命运文件；齿轮里改「命运文件夹」（相对作品根，默认 <code>命运</code>）。</p>
<h2>蓝图画布</h2>
<ul>
<li>空白右键「添加节点」，没有子菜单。节点不是文件链接，不要指望双击打开某篇设定。</li>
<li>可添加分组、子图；钉住；改颜色（菜单项右侧 color picker 圆点）。</li>
<li>节点字段：标题、描述（可折叠）、类型（标签）、cause / effect 圆点。</li>
<li>从节点拖线到另一节点，松开默认接到该节点。cause 在右、effect 在左；两端都能拖，方向是 cause→effect。</li>
<li>连线可改标签（标签下方弹出编辑）、粗细、形状、箭头；右键删除。</li>
<li>桑基图：条宽约 4px，高度随输入连线；缩放用画布手势。连线画在节点之下以免被挡住。</li>
<li>删除画布节点<strong>不会删除</strong>命运文件夹里的 markdown。</li>
</ul>
<h2>轨道</h2>
<ul>
<li>只能有<strong>一条正文轨道</strong>。事件轨道可多条，可从裂变「导入列范围」。</li>
<li>从文件树把当前作品的正文拖进正文轨道、事件拖进事件轨道。左右拖改时间范围，滚轮缩放时间轴。</li>
<li>轨道卡片最小宽度 120px；已有正文宽度不因导入变窄。父轨宽度 = 子项之和。</li>
<li>卡片右键：颜色（右侧圆点）、删除。</li>
<li>正文圆点靠左一格（删除图标左侧），连到事件轨道圆点；重叠即表示剧情面板里的联系。正文默认只连一条，连线右键断开。允许从正文点再拖到其他轨道。</li>
<li>正文卡片靠近事件 8px 时吸附。</li>
<li>工具栏分支图标：显示节点与文件连线（圆点对圆点）。另一个开关显示命运节点与事件/正文的包围盒连线。</li>
<li>锁定缩放：画布与轨道同步缩放、左右平移。</li>
</ul>
<h2>添加到因果线</h2>
<ol class="steps">
<li>在正文或事件里框选（事件也可不选）→ 右键「添加伏笔」。</li>
<li>弹窗标题是「添加到因果线」。没有命运文件时可在此新建默认节点。</li>
<li>选区写成节点上的关联正文/事件（路径 + 偏移 + 原文），不写事件 frontmatter。</li>
</ol>
{C("important","Important","<p>空画布提示里若仍提到「伏笔标签笔记」，以蓝图节点为准。显示关联已改为命运节点的 events/prose。</p>")}
"""),
		"fission": ("裂变", f"""
<p class="lead">多列卡片大纲，默认看 <code>事件/</code>。每张卡就是一篇笔记。旧视图 id 叫 gingko，会迁到 fission。</p>
{a("fission.png","裂变")}
<h2>怎么打开</h2>
<p>创作面板 Tab「裂变」，命令「打开裂变视图」。</p>
<h2>操作</h2>
<ul>
<li>点卡展开下一列。上/下/右小箭头：前兄弟、后兄弟、子卡。</li>
<li>拖卡调整顺序，写的是文件夹与文件位置。列序也会反映到文件侧。</li>
<li>搜索、规则、外观在工具栏。卡片上可直接改字段。</li>
<li>右键改事件类型（时代/场景/章节/情节），角标换图标，滚动位置尽量保持。</li>
<li>右侧情绪曲线：每张卡一个「情绪变化」，相对上一张加减，从 0 累加。拖点写回该笔记。</li>
<li>角标伏笔状态按命运蓝图 + 事件路径推断，不读事件 YAML 槽。</li>
<li>灵感可拖入生成情节。大操作（加父卡、合并、拆分）底部有进度条。</li>
</ul>
<p>数据：<code>System/fission.json</code>（顺序、外观、规则）。</p>
{C("tip","Tip","<p>演示或外部改过文件后，点工具栏「重新加载」。裂变不自动跟随外部刷新，避免正在看时被打断。</p>")}
"""),
		"map": ("地图", f"""
<p class="lead">底图上打地点标记。时空视图至少需要一张地图。</p>
{a("map.png","地图")}
<h2>怎么打开</h2>
<p>创作面板 Tab「地图」，或命令「打开地图视图」。</p>
<h2>操作</h2>
<ol class="steps">
<li>新建或选择地图（<code>System/maps/index.json</code> + <code>System/maps/{{id}}.json</code>）。</li>
<li>设底图、显示类型、类型样式。</li>
<li>标记分普通点与传送门。可在画布拖放或新建地点笔记。</li>
<li>地点笔记坐标字段 <code>coord</code> / <code>坐标</code> 写成：<code>地图名：x，y</code>。<strong>冒号、逗号必须全角</strong>，地图名与地图标题一致。</li>
<li>该地图的显示类型要包含地点（locale），<code>enabledTypes</code> 为空则一个钉子都没有。</li>
</ol>
{C("warning","Warning","<p>半角 <code>:</code> 或英文逗号都不认。把地点换到另一张地图后，两边的显示类型和坐标都要改。</p>")}
"""),
		"spacetime": ("时空", f"""
<p class="lead">三维：x/y 是地图平面，z 是时间。可按角色开轨迹。</p>
{a("spaceTime.png","时空")}
<h2>怎么打开</h2>
<p>创作面板 Tab「时空」，命令「打开时空视图」。无地图时会提示先去地图视图建一张。</p>
<h2>操作</h2>
<ul>
<li>先选地图。事件表、人物表在侧栏。</li>
<li>情节要挂到带坐标的地点，且自身有开始时间，才会出现球体。</li>
<li>轨迹模式：多选角色，沿时间画出路径；此时旋转锁定，避免拖轨迹时转视角。</li>
<li>可对齐事件球、配网格 / 轴 / 管线。</li>
</ul>
<p>数据：<code>System/spaceTime.json</code> + 地图坐标 + 事件时间/地点。</p>
{C("warning","Warning","<p>列表有事件、空间里没有：检查选的地图、地点全角坐标、事件「开始」是否按当前历法能解析。</p>")}
"""),
		"cards": ("卡片", f"""
<p class="lead">可配置字段墙。事件卡默认模板会用命运节点标题当摘要。</p>
{a("card.png","卡片")}
<h2>操作</h2>
<ol class="steps">
<li>工具栏「模板」打开编辑器。</li>
<li>左侧是全库字段并集，点字段名加到画布。</li>
<li>右侧改控件：文本、标题、徽章、标签、进度、图片；调宽高与网格。</li>
<li>分组 / 排序可存多套方案。未选方案时右侧只读。</li>
<li>卡片可拖拽排序、跨组拖拽。</li>
</ol>
<p>内联卡片见 <a href="{href('inline',h)}">内联视图</a>。块内方案写回该块 config，不改面板存档。</p>
"""),
		"table": ("表格", f"""
<p class="lead">同一批笔记的表：筛选、排序、钉列、双击改单元格写回 frontmatter。</p>
{a("table.png","表格")}
<h2>操作</h2>
<ul>
<li>列属性里可打开默认隐藏的系统列（uuid、关联、时间戳）。旧「钩子」「伏笔」列默认藏。</li>
<li>分组 / 排序 / 条件格式支持多套方案。条件格式按字段给单元格上色。</li>
<li>筛选规则组件与关系图共用。</li>
<li>支持拖拽排序与跨组拖拽。</li>
</ul>
{C("note","Note","<p>改的是笔记本身。时间线、裂变会读到同一字段。</p>")}
"""),
		"inline": ("内联视图", f"""
<p class="lead">在任意笔记里插入可交互的时间线、表格、卡片。</p>
<pre><code>```novel-timeline
height: 560
```

```novel-table
height: 560
```

```novel-cards
height: 560
```</code></pre>
<h2>规则</h2>
<ul>
<li>命令「插入时间线/表格/卡片视图块」在光标处插入骨架。</li>
<li><code>height</code> 200–1600，默认 560。</li>
<li><strong>数据来自承载该块的笔记所属作品</strong>，不是你在面板里选中的作品。</li>
<li>块内改列、筛选、分组、排序、条件格式、模板、时间线标记时段，只写回该块 <code>height</code> 与 <code>config</code> 两行。</li>
<li>打开内联时间线配置时延迟落盘，避免写回关掉面板。</li>
<li>搜索词、页码是临时状态，不写入代码块。</li>
<li>没有 config 的块跟随作品存档。</li>
<li>命运文件模板会带 <code>novel-blueprint</code> 块；命令面板没有「插入蓝图」项。</li>
</ul>
{C("warning","Warning","<p>块在 A 作品的笔记里，读的就是 A 的 System，即使面板顶部正选着 B。</p>")}
"""),
		"destiny": ("命运蓝图", f"""
<p class="lead">伏笔的主路径是 <code>命运/</code> 里的蓝图节点，外加右侧「伏笔总览」。不再把槽位写进事件 frontmatter。</p>
{a("foreshadowing.png","伏笔总览")}
<h2>怎么打开总览</h2>
<p>Ribbon 分支图标，或命令打开伏笔总览。设置里关闭「伏笔面板」会连右键「添加伏笔」和高亮一起停用。</p>
<h2>状态（不写盘，按蓝图推断）</h2>
<table><thead><tr><th>状态</th><th>条件</th></tr></thead><tbody>
<tr><td>空悬</td><td>无正文、无事件</td></tr>
<tr><td>已计划</td><td>有事件，无正文</td></tr>
<tr><td>已埋设</td><td>本节点有正文，同蓝图还没有其他节点有正文</td></tr>
<tr><td>执行中</td><td>本节点有正文，同蓝图另有节点也有正文，但尚未全部有</td></tr>
<tr><td>已回收</td><td>同蓝图所有节点都有正文</td></tr>
</tbody></table>
<h2>总览操作</h2>
<ul>
<li>过滤行左侧：标签筛选（来自节点上出现过的标签）。</li>
<li>排序：标题正/倒序、按关联正文的章节顺序、按关联事件时间。</li>
<li>「只显示关联事件」：按当前活动正文在 <code>textBySource</code> 上的事件 uuid 过滤。</li>
<li>卡片上因果线、正文、事件用 Link 组件；右上角文档图标打开命运文件。</li>
</ul>
<h2>从编辑器添加</h2>
<ol class="steps">
<li>在已注册作品的正文或事件里框选。</li>
<li>右键「添加伏笔」→「添加到因果线」→ 选文件与节点；没有文件时可新建。</li>
<li>选区作为 <code>ThreadNodeRef</code> 挂到节点的 prose（正文）或 events（事件）。</li>
</ol>
<p>关系图 pack、裂变角标、卡片摘要、正文伏笔高亮都读这套关联。作品日志记录命运文件的增删与关联。</p>
{C("warning","Warning","<p>旧事件里的 <code>伏笔</code>/<code>钩子</code> 数组界面不再读、也不会自动迁移或删除。表格把这两列藏掉。</p>")}
<p>侧栏筛选与跳转见 <a href="{href('foreshadow',h)}">伏笔总览</a>。画布操作见 <a href="{href('thread',h)}">脉络</a>。</p>
"""),
		"foreshadow": ("伏笔总览", f"""
<p class="lead">右侧账本：把命运文件夹里所有蓝图节点聚合成一张表。只读聚合，不另存 json。</p>
{a("foreshadowing.png","伏笔总览")}
<h2>怎么打开</h2>
<ul>
<li>Ribbon 分支图标，命令「打开伏笔面板」。</li>
<li>设置 → 功能入口关掉「伏笔面板」后：图标、命令、右键「添加伏笔」、正文伏笔高亮、关系图/裂变角标一并停。</li>
</ul>
<h2>界面</h2>
<ul>
<li>搜索：节点标题、因果文件、正文或事件路径。</li>
<li>状态筛选：全部 / 未回收 / 未定位正文。状态本身不写盘，按节点有没有 prose/events 推断。</li>
<li>标签筛选：节点上出现过的类型标签。</li>
<li>排序：标题正/倒序、按关联正文顺序、按关联事件时间。</li>
<li>「只显示当前正文相关」：用正在编辑的正文在轨道/关联上的事件 uuid 过滤。没有打开正文、或该正文还没挂事件时，列表会空并提示原因。</li>
<li>卡片：因果线、正文、事件用链接；可跳转打开命运文件、打开正文选区、在关系图定位。</li>
<li>选区改过导致偏移失效时提示「定位已失效」，需重新框选添加。</li>
</ul>
<h2>和标记账本的区别</h2>
<p>总览管命运节点；<a href="{href('marks',h)}">标记账本</a>管正文选区书签。两套高亮样式也分开。</p>
{C("note","Note","<p>界面若仍残留「钩子总览」一类旧文案，槽位数据已不再维护。不要在事件 YAML 里填钩子数组指望这里出现。</p>")}
"""),
		"plot": ("剧情对照", f"""
<p class="lead">跟随主区正在写的正文，对照已关联的场景 / 章节 / 情节大纲。只读，不替代脉络连线。</p>
<h2>怎么打开</h2>
<p>Ribbon scroll-text，命令「打开剧情面板」。关掉「剧情面板」入口后图标与命令停用。</p>
<h2>操作细节</h2>
<ol class="steps">
<li>主区打开一篇属于当前作品的 Markdown 正文（可分栏）。没有正文时提示「请在主区分栏打开一篇 Markdown 正文」。</li>
<li>若该篇尚未关联场景/章节/情节：提示到正文右键「关联到情节/场景…」，或在关系图节点上「生成正文 / 关联到正文」。</li>
<li>一篇正文可挂多个情节：顶部切换「选择关联情节」。显示「共 n 个情节」。</li>
<li>卡片内：大纲正文（渲染事件 md 去掉 frontmatter）、元数据折叠块（描述、视角、地点、参与者、开始、结束）、情绪张力（相对上一情节的变化）。</li>
<li>「打开大纲文件」打开该事件笔记；「在关系图中定位」聚焦对应节点。</li>
</ol>
<p>设置 → 小说创作 →「剧情卡片折叠块默认展开」：开则每次换情节默认展开元信息；关则默认折上。</p>
{C("note","Note","<p>面板里若仍列出「伏笔/钩子」计数，那是旧文案。真正的伏笔在命运节点。改关联请用脉络圆点或「关联到情节/场景」。与脉络「卡片重叠即有联系」是同一套 uuid 联系。</p>")}
"""),
		"marks": ("标记账本", f"""
<p class="lead">把正文选区收成「标记」账本：源头位置 + 可选回收位置。与命运伏笔完全独立。</p>
<h2>怎么打开</h2>
<p>Ribbon bookmark，命令「打开标记账本」。关掉「标记面板」后菜单与<strong>标记高亮</strong>一起停。</p>
<h2>编辑器</h2>
<ul>
<li>框选后右键「添加到标记」。同一位置重复添加会提示。</li>
<li>「回收标记」：把已有标记标为已回收（再框选一次回收位置）。</li>
<li>侧栏可改标题、说明、标签；跳转「源头」或「回收」选区。正文改过导致偏移失效时显示「位置已失效」。</li>
<li>搜索标题、原文、文件；按标签筛选。</li>
</ul>
<h2>数据落盘</h2>
<p>作品 <code>System/marks.json</code>。不写命运文件，也不写事件 YAML。</p>
<h2>高亮</h2>
<p>设置 → 高亮 → <strong>标记高亮</strong>。命运选区走另一套「伏笔高亮」。两套可同时开。</p>
"""),
		"journal": ("作品日志", f"""
<p class="lead">创作主页上的「创作历程」组件，不是独立标签页。</p>
<h2>怎么打开</h2>
<p>打开创作主页，确保模板里放了日志组件（⚙ 模板编辑器可加回来）。</p>
<h2>操作</h2>
<ul>
<li>按日 / 周 / 月 / 年缩放时间颗粒。</li>
<li>分类大致包括：写作、设定、剧情、命运（内部 id 可能仍叫 foreshadow）、关系图、空间、灵感、作品。</li>
<li>点卡片跳到对应笔记或视图。</li>
<li>老条目可能没有 path，加载时按标题尽量回填。</li>
</ul>
<h2>会记什么</h2>
<ul>
<li>命运文件新建、把正文/事件挂到节点、解除关联。</li>
<li>关系图连线、生成正文等创作动作。</li>
</ul>
<h2>数据落盘</h2>
<p><code>System/journal/YYYY-MM-DD.json</code>。不是 Git、不能当版本对比，对比用 <a href="{href('snapshot',h)}">历史快照</a>。</p>
"""),
		"inspiration": ("灵感库", f"""
<p class="lead">突发想法、片段、章节变体。卡片可拖进创作面板变成情节或 pack。</p>
{a("inspiration.png","灵感")}
<h2>怎么打开</h2>
<p>Ribbon 灯泡，命令「打开灵感库」。需已注册作品。</p>
<h2>操作</h2>
<ul>
<li>「新建灵感」或选区右键「提取为灵感」，写入作品 <code>灵感/</code>。</li>
<li>搜索标题或正文；筛选全部 / 有正文 / 仅标题；排序：最近修改、最早修改、标题、最近创建。</li>
<li>打开、删除（进回收站）。卡片可「转为事件」「放到便签」。</li>
<li>拖到<strong>关系图</strong>：生成独立 pack；拖到<strong>时间线 / 裂变</strong>：创建情节。目标必须是当前作品。</li>
</ul>
{C("warning","Warning","<p>拖到别的作品的视图会被拒绝。共享源卷只读，不要指望把灵感写进别人的设定。</p>")}
"""),
		"glossary": ("词条", f"""
<p class="lead">功法、称谓、器物名等速查列表。不是角色卡（角色在 <code>设定/角色</code>）。</p>
{a("glossary.png","词条")}
<h2>怎么打开</h2>
<p>Ribbon list-tree，命令「打开词条面板」。</p>
<h2>操作</h2>
<ol class="steps">
<li>右上角齿轮打开「词条配置」。</li>
<li>文件名 = 词条类型。点 + 新建类型文件，或把已有笔记的 type/tags 设为「词条」「glossary」「【词条】」。</li>
<li>勾选要展示的类型；拖左侧把手改显示顺序。</li>
<li>每个类型可「按行拆分」（默认一行一条）或「按标题拆分」（<code>#</code> 标题）。</li>
<li>主界面点卡片换一条随机词条。</li>
</ol>
<h2>数据落盘</h2>
<p>词条正文在作品 <code>词条/</code>；勾选与顺序在 <code>System/glossary.json</code>。</p>
"""),
		"wordfreq": ("词频", f"""
<p class="lead">统计<strong>当前编辑器里那一篇</strong>的用词。整部书用词看创作主页的词频组件。</p>
{a("wordfreq.png","词频")}
<h2>怎么打开</h2>
<p>Ribbon hash，命令「打开词频面板」。侧栏不要当普通 Markdown 标签用（避免其它插件往里插内容）。</p>
<h2>操作</h2>
<ul>
<li>打开一篇笔记后，面板列出 TopN。切文件会重算。</li>
<li>词典：设置 → 小说创作 → 词频，可下载 jieba 小/标准/大（jsdelivr）和 CC-CEDICT（mdbg）。不下载也能跑，只用内置停用词，分词更粗。</li>
<li>词频<strong>不会</strong>自动校对。校对是另一个面板。</li>
</ul>
{C("note","Note","<p>下载是你点按钮才联网，文件落到插件目录 <code>word-freq-dicts/</code>。插件不回传笔记。</p>")}
"""),
		"proofread": ("校对", f"""
<p class="lead">按词典标疑似错字、近音近形、敏感词、设定名写错。作品内任意笔记都能检，不限 <code>正文/</code>。</p>
{a("proofread.png","校对")}
<h2>怎么打开</h2>
<p>Ribbon 拼写检查，命令「打开校对面板」。依赖词频同一套词典；没下词典时能力会变弱。</p>
<h2>操作</h2>
<ul>
<li>列表分：未登录词（OOV）、近形/近音、设定/注释名不一致、敏感词表。</li>
<li>点条目可跳到正文波浪线处；确认替换，或框选 1–12 个汉字/字母后右键「加入词典」。</li>
<li>敏感词表在插件目录 <code>sensitive-words.json</code>（高亮模块也会用）。</li>
</ul>
"""),
		"sticky": ("悬浮便签", f"""
<p class="lead">浮在编辑器上的便签，自动写入当前作品 System，刷新后还在。</p>
{a("sticky-note.png","悬浮便签")}
<h2>怎么打开</h2>
<p>命令「新建悬浮便签」；状态栏便签图标；选区「提取为悬浮便签」。必须已激活作品。</p>
<h2>操作</h2>
<ul>
<li>拖动位置、改颜色、钉住（不被其它窗口挤走）。</li>
<li>隐藏 / 显示全部（命令）。Obsidian 弹窗打开时便签可能临时沉底，关掉弹窗回来。</li>
<li>「存为笔记」落到作品文件夹；「同步回原文」把便签内容写回当初提取的那段。原文找不到该段会失败。</li>
</ul>
<p>数据：<code>System/note.json</code>。</p>
"""),
		"wordcount": ("码字与字数", f"""
<p class="lead">右侧码字面板管目标与冲刺；另外四处字数显示可单独开关。口径与主页 KPI 不同。</p>
{a("writing-goal.png","码字")}
<h2>怎么打开</h2>
<p>Ribbon 钢笔，命令打开码字面板。设置 → 字数统计可关总开关。</p>
<h2>四处显示</h2>
<table><thead><tr><th>开关</th><th>位置</th><th>命令 / 菜单</th></tr></thead><tbody>
<tr><td>文件树字数</td><td>资源管理器条目旁</td><td>切换文件树字数</td></tr>
<tr><td>行末字数</td><td>编辑器每段行尾</td><td>切换行末字数</td></tr>
<tr><td>阶段标尺</td><td>编辑器标尺里程碑</td><td>切换阶段标尺</td></tr>
<tr><td>框选字数</td><td>选区统计</td><td>切换框选字数</td></tr>
</tbody></table>
<p>编辑器右键「功能开关 → 字数统计」同样可切。文件树/编辑器菜单可给当前正文设写作目标或冲刺（仅作品正文树内的文件）。</p>
{C("warning","Warning","<p>主页 KPI 统计的是当前作品 <code>正文/</code> 的 last−start / max−start，不是码字面板里某一篇的冲刺值。</p>")}
"""),
		"naming": ("取名", f"""
<p class="lead">按人物、地名、势力等大类批量生成名字，可接到文件模板。</p>
{a("naming.png","取名")}
<h2>怎么打开</h2>
<p>Ribbon 骰子，命令打开取名工具。设置 → 取名工具：一次生成条数。</p>
<h2>和模板一起用</h2>
<p>文件模板规则可勾选取名工具，在目标文件夹新建 md 时自动填名。见 <a href="{href('templates',h)}">文件模板</a>。</p>
"""),
		"phone": ("手机预览", f"""
<p class="lead">在桌面模拟阅读 App 的窄屏排版，检查段长和标题折行。</p>
<h2>怎么打开</h2>
<p>Ribbon 手机，设置 → 其他里可关总开关。同步主区当前 Markdown。</p>
{C("important","Important","<p>这是预览，不是移动端插件。创作面板、时空、CSS 窗口材质都按桌面写，不要指望手机 Obsidian 跑完整套件。</p>")}
"""),
		"highlight": ("高亮", f"""
<p class="lead">全局装饰规则，对所有已注册作品生效。入口在设置 → 高亮设置，不在创作面板 Tab。</p>
<h2>规则类型</h2>
<ul>
<li>正则、文件名（设定名等）、注释、敏感词、对白（对白着色 / 弱化旁白）、长句。</li>
<li><strong>标记高亮</strong>：标记账本的源头/回收选区（旧名曾叫伏笔/钩子样式）。</li>
<li><strong>伏笔高亮</strong>：正文里挂到命运节点的选区。点高亮可打开已开着的伏笔总览。</li>
</ul>
<h2>操作</h2>
<ul>
<li>命令「开关高亮设置」一键关装饰。</li>
<li>选区「提取为高亮文件 / 高亮注释」。</li>
<li>词表来自全部已注册作品 + 共享源卷。默认排除 <code>System/</code> 和点开头的文件夹。</li>
<li>旧作品若有 <code>System/highlight.json</code>，需要时导入一次到全局设置。</li>
</ul>
<p>关「伏笔面板」入口会停伏笔高亮；关「标记面板」会停标记高亮。互不影响。</p>
"""),
		"templates": ("文件模板", f"""
<p class="lead">在已注册作品的目标文件夹（含子目录）新建 md 时套用。</p>
{a("file-template.png","文件模板")}
<h2>规则字段</h2>
<ul>
<li>目标文件夹、文件名格式、可选模板文件、取名工具、自动填充。</li>
<li>有模板 → 写入正文并按格式重命名；无模板 → <strong>只改文件名</strong>。</li>
<li><code>{{n}}/{{nn}}/{{nnn}}</code> 阿拉伯数字；<code>{{N}}/{{NN}}/{{NNN}}</code> 中文数字（第{{N}}章 → 第一章）。</li>
</ul>
{C("warning","Warning","<p>新建没套上：文件夹路径与规则不一致，或点在未注册作品目录外。</p>")}
"""),
		"filesort": ("文件树排序", f"""
<p class="lead">只改资源管理器<strong>显示顺序</strong>，不改磁盘文件名。</p>
<h2>怎么打开</h2>
<p>设置 → 文件树排序。命令「重新应用文件树排序」在排序看起来没跟上时用。</p>
<h2>能力</h2>
<ul>
<li>中文数字（第一章、十）、自然数、自定义词序。</li>
<li>条目样式与排序独立：文件树右键可给文件/文件夹加样式，或删除样式。</li>
<li>可隐藏 <code>_index</code> 一类文件夹文件的显示，同时提供右键「打开文件夹文件」。</li>
</ul>
"""),
		"css": ("CSS 片段", f"""
<p class="lead">桌面端管理 <code>.obsidian/snippets</code>，三色旋钮混主题，以及窗口材质与壁纸。</p>
{a("css0.png","CSS 片段")}
<h2>怎么打开</h2>
<p>状态栏画笔；命令打开 CSS 面板 / 重新加载 CSS 片段。移动端设置页不出现本模块。</p>
<h2>操作</h2>
<ul>
<li>开关 snippets、在面板里编辑、重载。</li>
<li>paper / ink / accent 三色旋钮混入当前主题；也可走 Style Settings。删掉片段里的自定义配色注释即回主题默认。</li>
<li>窗口材质：Windows 11 亚克力（旧档 mica/clear 会并到亚克力）。失焦时系统会把亚克力降回实色。打开 DevTools 时会暂时切回实色，避免停靠面板白屏。</li>
<li>壁纸走 CSS 变量 <code>--osp-bg-image</code>。禅模式可勾「透明背景」让编辑区透出壁纸。</li>
</ul>
{C("warning","Warning","<p>仅桌面。改窗口材质后若「毫无变化」，先看是不是失焦、是不是开了 DevTools、是不是系统不支持 setBackgroundMaterial。</p>")}
"""),
		"typewriter": ("写作模式", f"""
<p class="lead">四类能力组合成预设：打字机滚动、行专注、禅模式、海明威单向写。必须在 Markdown <strong>编辑模式</strong>。</p>
<h2>怎么打开</h2>
<p>状态栏图标弹出预设菜单；命令「打开写作模式菜单」「关闭写作模式」以及「写作模式：××」直达。设置里可关总开关。</p>
<h2>预设</h2>
<table><thead><tr><th>预设</th><th>效果</th></tr></thead><tbody>
<tr><td>打字机滚动</td><td>光标行停在视口偏移位置（设置里 0% 顶 ~ 100% 底，默认居中）。</td></tr>
<tr><td>行专注</td><td>非当前行变淡；可按距离渐变。</td></tr>
<tr><td>禅模式</td><td>隐藏 ribbon、左右侧栏、标签头、非活动 leaf，只留当前编辑。退出按钮在顶部。可透出 CSS 壁纸。</td></tr>
<tr><td>禅+打字机 / 禅+专注 / 全部组合</td><td>叠加。</td></tr>
<tr><td>海明威</td><td>禁退格、删除、撤销、回跳，只能往前写。</td></tr>
</tbody></table>
{C("warning","Warning","<p>阅读预览无效。禅模式不是系统全屏 API，用 CSS 藏外围；壁纸要靠 CSS 片段先设好 <code>--osp-bg-image</code>。</p>")}
"""),
		"snapshot": ("历史快照", f"""
<p class="lead">给打开过的 Markdown 自动或手动存版本，面板里对比、批注、恢复、清理。</p>
{a("snapshot.png","历史快照")}
<h2>怎么打开</h2>
<p>Ribbon history；编辑器菜单存档；命令打开面板 / 存档当前 / 清理。设置可关总开关或只关自动保存。</p>
<h2>操作</h2>
<ul>
<li>对比默认：左 = 快照（删除红），右 = 当前（新增绿）。</li>
<li>默认目录 <code>.obsidian/snapshots</code>；录入记录 <code>.memory/</code>（旧 <code>.printRecord</code> 会迁移）。</li>
<li>超过约 1MB 的文件会跳过自动存。</li>
<li>「录入记录」开关可独立于快照总开关。</li>
</ul>
<p>不是 Git，也不进作品 <code>System/</code>。</p>
"""),
		"search": ("高级搜索", f"""
<p class="lead">库级全文搜索与替换。可停靠左右，也可开浮动窗。</p>
<h2>怎么打开</h2>
<p>Ribbon search-alert；命令打开面板 / 打开浮动窗。设置 → 其他关掉后停索引、命令失效。</p>
<h2>操作</h2>
<ul>
<li>文件菜单、编辑器菜单可把范围收到当前文件或文件夹。</li>
<li>替换前先看命中列表。</li>
<li>浮动窗的 leaf 在 popout 里，主窗口 <code>getLeavesOfType</code> 看不到它，关掉浮动窗再从主窗打开即可。</li>
</ul>
<p>不替代关系图筛选或表格筛选。</p>
"""),
		"json": ("JSON Studio", f"""
<p class="lead">用树形编辑器打开 JSON。默认接管 <code>.json</code>，适合改作品 <code>System/*.json</code>。</p>
<h2>怎么打开</h2>
<p>没有 Ribbon。点 JSON 文件，或命令「打开当前 JSON / 在新标签打开」。文件菜单同样有入口。设置 → 其他可关。</p>
{C("warning","Warning","<p>坏 JSON 会提示，不要强行保存半截。graph.json / timeline.json / thread.json 结构复杂，宁可在对应视图里改，除非你清楚字段。</p>")}
"""),
		"series": ("共享设定组", f"""
<p class="lead">多部作品共用世界观：组内互相<strong>只读引用</strong>设定，文件仍留在各自源卷。</p>
<h2>怎么打开</h2>
<p>设置 → 小说创作 → 共享设定组。</p>
<h2>规则</h2>
<ul>
<li>一个作品只能进一组。勾选成员；组名称自定。</li>
<li>「共享设定」：角色、地点、道具等在组内可见、可引用、参与高亮。</li>
<li>「共享时代 / 场景」默认关。打开后时间线、关系图可只读显示别人的时代/场景。</li>
<li>地点地图始终组内互用，不受时代/场景开关影响。</li>
<li>视图带共享徽章。不能在本作品里改源文件，也不能把伏笔关联写进源卷节点。</li>
</ul>
<p>要改人设：面板顶部切到源作品再改。</p>
"""),
		"export": ("导出", f"""
<p class="lead">把作品导出为 PDF / DOCX 等。<strong>当前版本不在 Ribbon / 设置里提供可见入口</strong>，但命令面板里仍可搜到三条导出命令；不是安装损坏。</p>
<p>代码仍在；恢复需在源码 <code>main.ts</code> 与设置页取消注释。隐藏期间请用 Obsidian 自己的导出或外部工具。</p>
"""),
		"faq": ("常见问题", f"""
<p class="lead">先看这一页，再去对应功能页看操作细节。</p>
<details class="faq" open><summary>面板空、没有作品？</summary><p>先注册并在创作面板顶部选中。换库要重新打开 Vault。</p></details>
<details class="faq"><summary>看不到加载示例？</summary><p>库里已经有注册作品。</p></details>
<details class="faq"><summary>关系图角色重启后消失？</summary><p>关掉「只显示有关系的文件」，或先连线。见 <a href="{href('graph',h)}">关系图</a>。</p></details>
<details class="faq"><summary>地图没有钉子？</summary><p>全角「：」「，」，地图名一致，类型含 locale。见 <a href="{href('map',h)}">地图</a>。</p></details>
<details class="faq"><summary>时间线拖了文件没动？</summary><p>分组改成「文件夹」。见 <a href="{href('timeline',h)}">时间线</a>。</p></details>
<details class="faq"><summary>添加伏笔没反应？</summary><p>文件要在已注册作品内；小说创作总开关开着；未关伏笔 Ribbon。见 <a href="{href('destiny',h)}">命运蓝图</a> 与 <a href="{href('foreshadow',h)}">伏笔总览</a>。</p></details>
<details class="faq"><summary>简单模式在哪？</summary><p>运行时始终全功能。设置里若仍有简单/全功能文案，可忽略。</p></details>
<details class="faq"><summary>共享笔记改不了？</summary><p>到源作品改。见 <a href="{href('series',h)}">共享设定组</a>。</p></details>
<details class="faq"><summary>字数不对？</summary><p>主页统计当前作品正文。见 <a href="{href('home',h)}">创作主页</a>。</p></details>
<details class="faq"><summary>导出按钮呢？</summary><p>故意隐藏。见 <a href="{href('export',h)}">导出</a>。</p></details>
<details class="faq"><summary>视图配置回滚？</summary><p>同步冲突打回了 System/*.json。</p></details>
<p>仍异常：刷新创作面板，或「重建当前作品节点图」。</p>
"""),
		"data": ("数据与隐私", f"""
<table><thead><tr><th>内容</th><th>位置</th></tr></thead><tbody>
<tr><td>作品列表、激活作品、历法、全局设置</td><td><code>.obsidian/plugins/novel-kit/data.json</code></td></tr>
<tr><td>面板当前 Tab</td><td><code>System/workspace.json</code></td></tr>
<tr><td>关系图 / 时间线 / 脉络 UI / 裂变 / 时空 / 卡片 / 表格</td><td><code>System/graph.json</code>（旧 relations.json 会迁移）、<code>timeline.json</code>、<code>thread.json</code>、<code>fission.json</code>、<code>spaceTime.json</code>、<code>cards.json</code>、<code>table.json</code></td></tr>
<tr><td>地图</td><td><code>System/maps/</code></td></tr>
<tr><td>主页模板与待办</td><td><code>System/home.json</code></td></tr>
<tr><td>作品日志</td><td><code>System/journal/*.json</code></td></tr>
<tr><td>标记 / 便签 / 词条勾选 / 字段映射</td><td><code>marks.json</code>、<code>note.json</code>、<code>glossary.json</code>、<code>field-map.json</code></td></tr>
<tr><td>命运蓝图</td><td>作品 <code>命运/*.md</code> 内 <code>novel-blueprint</code> 代码块（旧文件夹名「因果」只读兼容）</td></tr>
<tr><td>设定、事件、正文、灵感、词条</td><td>作品下对应文件夹 Markdown</td></tr>
<tr><td>词频词典 / 敏感词</td><td>插件目录 <code>word-freq-dicts/</code>、<code>sensitive-words.json</code></td></tr>
<tr><td>历史快照</td><td><code>.obsidian/snapshots</code> 与 <code>.memory/</code></td></tr>
</tbody></table>
{C("danger","Danger","<p>删 data.json 丢登记与设置，不删笔记。删某个 System json 只重置那块视图。同步冲突时不要用旧的 System json 覆盖新布局。</p>")}
<h2>网络</h2>
<p>默认可完全离线，无遥测。仅主动触发：</p>
<ul>
<li>下载分词词典 → jsdelivr / mdbg，只下载。</li>
<li>主页网页表格 → 你填的 URL，只读 HTML。</li>
</ul>
<p>一律 <code>requestUrl</code>，走 Obsidian 代理。</p>
<p>QQ 群 431076635 · 微信 mtztm525 ·
<a href="https://github.com/moke525/obsidian-novel-kit/issues" target="_blank" rel="noopener">Issues</a></p>
<div class="pay-row">
<figure><img src="{asset('wechat-pay.png',h)}" alt="微信" /><figcaption>微信</figcaption></figure>
<figure><img src="{asset('ali-pay.png',h)}" alt="支付宝" /><figcaption>支付宝</figcaption></figure>
</div>
"""),
	}


def index_body(here: str) -> str:
	blocks = [
		"<h1>Novel-kit 使用指南</h1>",
		'<p class="lead">这里是全部功能的操作说明，按主题拆成独立页面。只想先看插件能做什么，请回 '
		'<a href="../index.html">产品主页</a>；本页只负责索引，细节都在子页。写法参考 '
		'<a href="https://docs.obsidian.md/Home" target="_blank" rel="noopener">Obsidian Developer Docs</a>。</p>',
		'<div class="meta"><span class="pill">仅桌面端</span><span class="pill">Obsidian ≥ 1.8.7</span><span class="pill">明文 Markdown</span></div>',
		C("important", "Important", "<p>本插件不能在手机上当完整写作套件用。Obsidian 本体的同步、主题、双链请看 <a href='https://help.obsidian.md/' target='_blank' rel='noopener'>官方 Help</a>。</p>"),
		'<p>第一次用建议先读 <a href="' + href("install", here) + '">安装</a> 与 <a href="' + href("workspace", here) + '">作品工作区</a>，再进创作面板；出问题先看 <a href="' + href("faq", here) + '">常见问题</a>。</p>',
		'<div class="catalog">',
	]
	for group, items in NAV:
		blocks.append(f'<section class="cat-group"><h2>{group}</h2><div class="cat-grid">')
		for pid, title in items:
			if pid == "index":
				continue
			b = BLURBS.get(pid, "")
			blocks.append(f'<a class="cat-card" href="{href(pid, here)}"><h3>{title}</h3><p>{b}</p></a>')
		blocks.append("</div></section>")
	blocks.append("</div>")
	return "\n".join(blocks)


def copy_assets() -> None:
	dst = ROOT / "assets"
	dst.mkdir(exist_ok=True)
	if not REPO_ASSETS.is_dir():
		return
	for p in REPO_ASSETS.iterdir():
		if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
			shutil.copy2(p, dst / p.name)


def main() -> None:
	"""只生成 pages/ 下的指南页；根 index.html 是产品主页，这里绝不碰。

	每个功能页都过一遍 guide_sections.render_guide()，统一成六段骨架，
	原有 pages() 的正文按语义归并，不丢内容。
	"""
	validate_facts()
	PAGES_DIR.mkdir(exist_ok=True)
	copy_assets()
	hub = shell("index", "指南总览", "指南总览", index_body("index"), pager("index"))
	(PAGES_DIR / "index.html").write_text(hub, encoding="utf-8")
	inner = pages("x")
	# pages() 只把 here 传给 href/shot，用占位值即可
	group_of: dict[str, str] = {}
	siblings_of: dict[str, list[tuple[str, str]]] = {}
	for group, items in NAV:
		for pid, _ in items:
			group_of[pid] = group
			siblings_of[pid] = items
	for pid, (title, html) in inner.items():
		body = render_guide(
			pid, title, html, BLURBS.get(pid, title),
			group_of.get(pid, "使用指南"), siblings_of.get(pid, []),
		)
		doc = shell(pid, title, title, body, pager(pid))
		(PAGES_DIR / f"{pid}.html").write_text(doc, encoding="utf-8")
	print("wrote", 1 + len(inner), "guide pages (6-section skeleton); root index.html untouched")


if __name__ == "__main__":
	main()
