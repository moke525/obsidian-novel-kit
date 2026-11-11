# -*- coding: utf-8 -*-
"""把每个功能指南页规范成统一的六段骨架。

六个必需章节：功能简介 / 界面元素 / 操作方法与步骤 / 键盘操作 / 命令行 / 注意事项，
之后允许有「其他」章节。原有 pages() 里的 h2 内容不会丢弃：按语义归并到对应章节，
标题降级为 h3；未归类的进「其他」。

事实表 KEYBOARD_GROUPS / COMMAND_NAMES 全部按插件源码核对：
  - 快捷键：src/utils/keyboard.ts、GraphCanvas.svelte、BlueprintCanvas.svelte、
    Gantt.svelte、PlaybackPanel.svelte、Table.svelte、CardsView.svelte、
    Fission.svelte、MapCanvas.svelte
  - 命令：各 features/*/manager.ts 的 addCommand，共 64 条，全部无默认 hotkeys
不要凭空补命令或默认快捷键；新增功能时同步这里。
"""
from __future__ import annotations

import re

# 前六项是必需章节；extra 是「还可以有的其他部分」
SECTIONS: list[tuple[str, str]] = [
	("intro", "功能简介"),
	("ui", "界面元素"),
	("steps", "操作方法与步骤"),
	("keyboard", "键盘操作"),
	("commands", "命令行"),
	("cautions", "注意事项"),
]
EXTRA_KEY, EXTRA_TITLE = "extra", "其他"

# ── 视图级快捷键（真实实现；输入框 / 正文编辑态内一律不触发） ──────────────
KEYBOARD_GROUPS: dict[str, list[tuple[str, str]]] = {
	"global": [
		("Ctrl/Cmd+P", "打开 Obsidian 命令面板，按名称搜索并执行本页「命令行」里的命令（Obsidian 自带，不是插件默认快捷键）"),
	],
	"graph": [
		("Esc", "停止创建连线、取消框选"),
		("Ctrl/Cmd+A", "全选节点"),
		("Ctrl/Cmd+C", "复制选中节点"),
		("Ctrl/Cmd+Z", "撤销"),
		("Ctrl/Cmd+Y / Ctrl/Cmd+Shift+Z", "重做"),
		("Ctrl/Cmd+= 或 +", "放大画布"),
		("Ctrl/Cmd+-", "缩小画布"),
		("Ctrl/Cmd+0", "缩放适配全部节点"),
		("Delete / Backspace", "删除选中项，优先级：分组 → 连线 → 节点（共享只读仍拦截）"),
		("Enter、Esc（连线标签内联输入）", "提交 / 取消标签编辑；详情面板标题框 Enter 提交"),
	],
	"thread": [
		("Esc", "取消连线、清除选中边、从子图返回父蓝图"),
		("Ctrl/Cmd+A", "全选"),
		("Ctrl/Cmd+C", "复制"),
		("Ctrl/Cmd+= / - / 0", "放大 / 缩小 / 缩放回 1"),
		("方向键", "轻移选中节点，步长 8 / zoom"),
		("Shift+方向键", "轻移选中节点，步长 32 / zoom"),
		("Delete / Backspace", "删除选中"),
		("Enter、Space（桑基图节点）", "聚焦节点时触发"),
	],
	"timeline": [
		("Ctrl/Cmd+C / Ctrl/Cmd+V", "复制 / 粘贴选中项"),
		("Ctrl/Cmd+= / -", "放大 / 缩小时间刻度"),
		("Delete", "删除选中项"),
		("← / →", "微调选中项的时间"),
		("Space（播放面板）", "播放 / 暂停"),
		("→、←（播放面板）", "下一事件 / 上一事件"),
		("Esc（播放面板）", "关闭播放面板；播放面板打开时甘特不抢方向键"),
	],
	"table": [
		("↑ / ↓", "在叶子行间移动活动单元格并滚动到可见"),
		("Enter", "进入当前单元格编辑"),
		("Ctrl/Cmd+N", "在当前行后新建行（需允许行编辑且非只读）"),
		("Enter、Esc（单元格编辑态）", "保存并结束编辑 / 取消编辑"),
	],
	"cards": [
		("Ctrl/Cmd+F", "聚焦卡片搜索框并全选"),
		("← / ↑ / → / ↓", "在可见卡片间移动焦点；无选中时从第 0 张开始"),
		("Enter（卡片聚焦时）", "打开该卡片"),
		("Enter、Space（模板编辑器）", "选中模板项"),
	],
	"fission": [
		("Ctrl/Cmd+Z、Ctrl/Cmd+Y 或 Ctrl/Cmd+Shift+Z", "撤销 / 重做"),
		("Ctrl/Cmd+F", "聚焦搜索框"),
		("Ctrl/Cmd+= / - / 0", "放大 / 缩小 / 缩放回 100%"),
		("[", "开关祖先栏"),
		("Ctrl/Cmd+C / V", "复制 / 粘贴卡片"),
		("Ctrl/Cmd+O", "打开当前卡片源文件"),
		("Ctrl/Cmd+Shift+L", "按空行拆分卡片"),
		("Ctrl/Cmd+M", "合并上一张；多选时合并所选"),
		("Ctrl/Cmd+Shift+G", "添加父卡"),
		("Ctrl/Cmd+N / Shift+Ctrl/Cmd+N", "新建同级 / 新建子卡；无选中时建根卡"),
		("F2", "改标题"),
		("Ctrl/Cmd+Space", "进出多选"),
		("↑ / ↓（Shift 范围多选）", "同列选卡；→ 进子卡、← 回父卡"),
		("Alt+↑、Alt+↓", "同列挪卡"),
		("Home、End、Ctrl/Cmd+Home、Ctrl/Cmd+End", "跳列首尾 / 跳兄弟组首尾"),
		("Esc", "多选收成当前卡"),
		("Enter", "打开卡片编辑"),
		("Shift+Delete / Shift+Backspace", "删除（仍走确认）"),
		("Ctrl/Cmd+Enter、Esc（正文编辑态）", "保存并在后方新建同级 / 保存退出"),
	],
	"map": [
		("Enter / Space（标记聚焦时）", "触发地点标记"),
	],
	"form": [
		("Enter", "提交当前输入 / 确认（各类弹窗、内联输入、列表项）"),
		("Esc", "取消编辑 / 关闭弹窗或抽屉"),
	],
}

# 明确无视图级快捷键的功能（源码目录内搜不到 keydown / e.key）
NO_KEYBOARD = {
	"spacetime": "时空视图未注册视图级快捷键（该目录没有键盘事件绑定）。",
	"install": "安装过程不涉及插件内键盘操作。",
	"faq": "本页是问题索引，无插件内键盘操作。",
	"data": "本页是数据说明，无插件内键盘操作。",
	"export": "导出面板未注册视图级快捷键。",
	"series": "共享设定组未注册视图级快捷键。",
	"templates": "文件模板由新建文件触发，无视图级快捷键。",
	"timesystem": "时间体系是设置页内容，无视图级快捷键。",
}

# ── 命令总表：id -> 命令面板里显示的中文名（全部无默认 hotkeys） ────────────
COMMAND_NAMES: dict[str, str] = {
	# src/features/novel/manager.ts
	"novel-open-studio": "打开创作主页",
	"novel-open-panel": "打开小说创作面板",
	"novel-open-word-freq": "打开词频面板",
	"novel-open-proofread": "打开校对面板",
	"novel-open-foreshadow": "打开伏笔面板",
	"novel-open-inspiration": "打开灵感库",
	"novel-open-glossary": "打开词条面板",
	"novel-open-plot": "打开剧情面板",
	"novel-open-marks": "打开标记账本",
	"novel-new-sticky": "新建悬浮便签",
	"novel-new-inspiration": "新建灵感",
	"novel-register-workspace": "注册小说工作区",
	"novel-toggle-sticky": "开关悬浮便签",
	"novel-hide-all-sticky": "隐藏全部便签",
	"novel-show-sticky": "显示便签",
	"novel-toggle-highlight": "开关高亮设置",
	"novel-rebuild-workspace": "重建当前作品节点图",
	"novel-open-view-timeline": "打开时间线视图",
	"novel-open-view-thread": "打开脉络视图",
	"novel-open-view-fission": "打开裂变视图",
	"novel-open-view-map": "打开地图视图",
	"novel-open-view-spacetime": "打开时空视图",
	"novel-open-view-cards": "打开卡片视图",
	"novel-open-view-graph": "打开关系图",
	"novel-open-view-table": "打开表格视图",
	"novel-extract-sticky": "提取选区为悬浮便签",
	"novel-extract-inspiration": "提取选区为灵感",
	"novel-extract-filename": "提取选区为高亮文件",
	"novel-extract-annotation": "提取选区为高亮注释",
	"novel-insert-timeline-block": "插入时间线视图块",
	"novel-insert-table-block": "插入表格视图块",
	"novel-insert-cards-block": "插入卡片视图块",
	# src/features/wordcount/manager.ts
	"wordcount-open-panel": "打开码字面板",
	"wordcount-goal-file": "为当前文件设置字数目标",
	"wordcount-sprint-file": "为当前章节开始冲刺",
	"wordcount-toggle-tree": "开关文件树字数角标",
	"wordcount-toggle-paragraph": "开关行末字数",
	"wordcount-toggle-milestones": "开关正文阶段标尺",
	"wordcount-toggle-selection": "开关框选字数气泡",
	# 其它模块
	"vault-search-open": "高级搜索",
	"vault-search-open-modal": "打开悬浮搜索",
	"typewriter-open-menu": "打开写作模式菜单",
	"typewriter-turn-off": "关闭写作模式",
	"typewriter-set-typewriter": "写作模式：打字机滚动（Typewriter）",
	"typewriter-set-focus": "写作模式：行专注模式（Focus）",
	"typewriter-set-zen": "写作模式：禅模式（Zen）",
	"typewriter-set-zen-typewriter": "写作模式：禅 + 打字机",
	"typewriter-set-zen-focus": "写作模式：禅 + 专注行",
	"typewriter-set-all": "写作模式：全部组合（禅+打字机+专注）",
	"typewriter-set-hemingway": "写作模式：海明威单向写作（Hemingway）",
	"snapshot-open-panel": "打开历史快照面板",
	"snapshot-archive-current": "存档当前文件",
	"snapshot-cleanup-all": "清理全部快照",
	"export-open-modal": "打开导出面板",
	"export-current-file": "导出当前文件",
	"export-current-folder": "导出当前文件夹",
	"css-snippets-toggle-panel": "打开 CSS Snippets 面板",
	"css-snippets-reload": "重新加载 snippets",
	"json-studio-open-active": "用 JSON Studio 打开当前 JSON",
	"json-studio-open-active-tab": "在新标签用 JSON Studio 打开当前 JSON",
	"file-tree-sort-refresh": "重新应用文件树排序",
	"naming-kit-open": "打开取名面板",
	"phone-preview-open": "打开手机预览",
	"ui-test-open-panel": "打开 UI 组件测试",
}

PANEL_VIEW_CMDS = [
	"novel-open-view-timeline", "novel-open-view-thread", "novel-open-view-fission",
	"novel-open-view-map", "novel-open-view-spacetime", "novel-open-view-cards",
	"novel-open-view-graph", "novel-open-view-table",
]
INSERT_BLOCK_CMDS = [
	"novel-insert-timeline-block", "novel-insert-table-block", "novel-insert-cards-block",
]
WORDCOUNT_TOGGLES = [
	"wordcount-toggle-tree", "wordcount-toggle-paragraph",
	"wordcount-toggle-milestones", "wordcount-toggle-selection",
]
TYPEWRITER_PRESETS = [
	"typewriter-set-typewriter", "typewriter-set-focus", "typewriter-set-zen",
	"typewriter-set-zen-typewriter", "typewriter-set-zen-focus",
	"typewriter-set-all", "typewriter-set-hemingway",
]

# 每页关联的命令；空列表 = 该页没有独立命令，会渲染「无独立命令」说明
PAGE_COMMANDS: dict[str, list[str]] = {
	"install": [], "workspace": ["novel-register-workspace", "novel-rebuild-workspace"],
	"settings": ["novel-toggle-highlight"] + WORDCOUNT_TOGGLES + ["ui-test-open-panel"],
	"commands": [],  # 本页原始三张表就是命令总表，见 render 特判
	"home": ["novel-open-studio"],
	"panel": ["novel-open-panel"] + PANEL_VIEW_CMDS,
	"graph": ["novel-open-view-graph"],
	"timeline": ["novel-open-view-timeline", "novel-insert-timeline-block"],
	"timesystem": [], "thread": ["novel-open-view-thread"],
	"fission": ["novel-open-view-fission"], "map": ["novel-open-view-map"],
	"spacetime": ["novel-open-view-spacetime"],
	"cards": ["novel-open-view-cards", "novel-insert-cards-block"],
	"table": ["novel-open-view-table", "novel-insert-table-block"],
	"inline": INSERT_BLOCK_CMDS,
	"destiny": [], "foreshadow": ["novel-open-foreshadow"],
	"plot": ["novel-open-plot"], "marks": ["novel-open-marks"], "journal": [],
	"inspiration": ["novel-open-inspiration", "novel-new-inspiration", "novel-extract-inspiration"],
	"glossary": ["novel-open-glossary"], "wordfreq": ["novel-open-word-freq"],
	"proofread": ["novel-open-proofread"],
	"sticky": ["novel-new-sticky", "novel-toggle-sticky", "novel-hide-all-sticky",
	           "novel-show-sticky", "novel-extract-sticky"],
	"wordcount": ["wordcount-open-panel", "wordcount-goal-file", "wordcount-sprint-file"] + WORDCOUNT_TOGGLES,
	"naming": ["naming-kit-open"], "phone": ["phone-preview-open"],
	"highlight": ["novel-toggle-highlight", "novel-extract-filename", "novel-extract-annotation"],
	"templates": [], "filesort": ["file-tree-sort-refresh"],
	"css": ["css-snippets-toggle-panel", "css-snippets-reload"],
	"typewriter": ["typewriter-open-menu", "typewriter-turn-off"] + TYPEWRITER_PRESETS,
	"snapshot": ["snapshot-open-panel", "snapshot-archive-current", "snapshot-cleanup-all"],
	"search": ["vault-search-open", "vault-search-open-modal"],
	"json": ["json-studio-open-active", "json-studio-open-active-tab"],
	"series": [], "export": ["export-open-modal", "export-current-file", "export-current-folder"],
	"faq": [], "data": [],
}

# 每页的视图快捷键分组（global 会自动补上）
PAGE_KEYBOARD: dict[str, list[str]] = {
	"graph": ["graph"], "thread": ["thread"], "timeline": ["timeline"],
	"table": ["table"], "cards": ["cards"], "fission": ["fission"],
	"map": ["map"], "spacetime": [],
	"panel": ["form"], "commands": ["form"], "settings": ["form"],
	"inline": ["table", "cards", "timeline"],  # 代码块内复用三个视图组件
}
for _pid in ("home", "destiny", "foreshadow", "plot", "marks", "journal",
             "inspiration", "glossary", "wordfreq", "proofread", "sticky",
             "wordcount", "naming", "phone", "highlight", "filesort", "css",
             "snapshot", "search", "json", "typewriter", "workspace"):
	PAGE_KEYBOARD.setdefault(_pid, ["form"])

# 原 h2 标题归并到哪一章；长词优先，避免「操作」抢走「操作细节」
SECTION_MAP: dict[str, str] = {
	"ui": ["状态（不写盘，按蓝图推断）", "和标记账本的区别", "和模板一起用",
	       "编辑器 / 文件树右键（需已打开作品）", "节点与连线", "蓝图画布",
	       "视图一览", "目录约定", "四处显示", "类型怎么认", "规则类型", "规则字段",
	       "自定义历法", "会记什么", "复制粘贴", "数据落盘", "组件", "界面",
	       "工具栏", "编辑器", "轨道", "预设", "能力", "规则", "网络", "状态"],
	"steps": ["怎么打开总览", "添加到因果线", "社区插件市场", "手动安装",
	          "从编辑器添加", "总览操作", "操作细节", "怎么打开", "怎么注册",
	          "改布局", "操作", "小说创作", "其它模块"],
	"cautions": ["注意事项"],
}
_MAP_LOOKUP: dict[str, str] = {
	word: key for key, words in SECTION_MAP.items() for word in words
}
_SORTED_WORDS = sorted(_MAP_LOOKUP, key=len, reverse=True)

# 界面元素兜底：原页面没有可归类表格时，给出该功能真实存在的界面部件
PAGE_UI: dict[str, list[str]] = {
	"install": ["设置 → 第三方插件 / 社区插件市场", "Ribbon 的房子（创作主页）与书本（创作面板）图标", "插件目录 <code>&lt;库&gt;/.obsidian/plugins/novel-kit/</code>"],
	"workspace": ["创作主页「新增作品」", "作品根文件夹与 <code>设定/ 事件/ 正文/ System/</code> 脚手架", "frontmatter <code>tags</code> 与 <code>uuid</code>"],
	"settings": ["设置 → Novel-kit 的十个页签", "总开关与逐项 Ribbon 勾选", "词频词典、共享设定组等页内控件"],
	"commands": ["命令面板 <code>Ctrl/Cmd+P</code>", "左侧 Ribbon", "设置 → 快捷键 / 设置 → 小说创作 → 功能入口", "编辑器与文件树右键菜单"],
	"home": ["Ribbon 房子图标", "当前作品、KPI、每日码字 / 热力图、词频、待办等组件", "右上角齿轮 → 主页模板编辑器"],
	"panel": ["Ribbon 书本图标", "顶部作品下拉与刷新按钮", "八个视图 Tab"],
	"graph": ["画布与缩放控件", "工具栏", "筛选 / 显示配置面板", "详情面板（Inspector）", "节点与画布右键菜单"],
	"timeline": ["甘特画布与刻度", "「开始」「结束」列", "分组行与标记时段", "播放面板"],
	"timesystem": ["时间体系设置", "现实时间 / 自定义单位链切换", "由细到粗的单位与锚定单位", "时间线刻度"],
	"thread": ["上半：命运蓝图画布与桑基视图", "下半：正文 / 事件多轨道", "因果线与轨道圆点"],
	"fission": ["多列看板与列内卡片", "工具栏的重新加载与搜索", "祖先栏", "缩放与平移控件"],
	"map": ["地图画布与底图", "地点标记", "地点笔记里的全角坐标字段", "<code>System/maps/index.json</code> 与 <code>System/maps/{id}.json</code>", "底图与显示类型 / 类型样式", "普通点与传送门两类标记"],
	"spacetime": ["三维画布：x / y 为地图平面", "z 轴时间", "角色轨迹开关", "事件表 / 人物表侧栏", "地图选择入口", "事件球体与角色轨迹", "网格 / 轴 / 管线显示开关"],
	"cards": ["卡片墙与字段单元格", "卡片搜索框", "模板编辑器", "工具栏「模板」按钮", "左侧全库字段并集", "右侧控件属性：文本 / 标题 / 徽章 / 标签 / 进度 / 图片", "分组 / 排序方案"],
	"table": ["表格视图与列头", "单元格编辑器", "钉列 / 方案 / 条件格式控件"],
	"inline": ["<code>```novel-timeline</code> / <code>```novel-table</code> / <code>```novel-cards</code> 代码块", "笔记内嵌视图与其工具栏"],
	"destiny": ["<code>命运/</code> 文件夹", "蓝图节点", "右侧伏笔总览的状态列"],
	"foreshadow": ["右侧伏笔总览侧栏", "聚合表格与筛选", "跳转到源笔记的链接"],
	"plot": ["剧情对照侧栏", "跟随主区正文的展示区", "已关联场景 / 章节 / 情节列表"],
	"marks": ["标记账本侧栏", "源头位置与回收位置列", "编辑器选区右键菜单", "对应高亮规则"],
	"journal": ["创作主页上的「创作历程」组件", "事件列表", "<code>System/</code> 下的日志文件"],
	"inspiration": ["灵感库侧栏", "灵感卡片", "创作面板里的拖放目标（情节 / pack）"],
	"glossary": ["词条面板", "类型文件", "逐行词条与顺序"],
	"wordfreq": ["词频面板", "当前编辑器文件范围指示", "词典下载按钮与词频列表", "TopN 词频列表", "设置 → 小说创作 → 词频的词典下载项", "内置停用词"],
	"proofread": ["校对面板", "疑似错字 / 近音近形 / 敏感词列表", "加入词典操作"],
	"sticky": ["悬浮在编辑器上的便签窗口", "便签列表与显隐控制", "当前作品 <code>System/</code> 存储"],
	"wordcount": ["右侧码字面板（目标 / 冲刺）", "文件树字数角标", "行末字数、阶段标尺、框选字数气泡"],
	"naming": ["取名面板", "人物 / 地名 / 势力大类选择", "生成条数与结果列表"],
	"phone": ["手机预览侧栏", "窄屏排版画布", "段长与标题折行预览", "Ribbon 手机图标", "同步主区当前 Markdown 的预览区", "设置 → 其他里的总开关"],
	"highlight": ["设置 → 高亮设置", "规则类型列表", "正则 / 文件名 / 注释 / 敏感词 / 对白规则项"],
	"templates": ["设置 → 文件模板", "目标文件夹与文件名格式", "模板文件与自动填充项"],
	"filesort": ["设置 → 文件树排序", "资源管理器显示顺序", "中文数字 / 自然数 / 自定义词序"],
	"css": ["CSS Snippets 面板与 snippets 列表", "三色旋钮", "窗口材质与壁纸设置"],
	"typewriter": ["写作模式菜单", "预设列表", "Markdown 编辑模式下的居中 / 淡出效果"],
	"snapshot": ["历史快照面板", "版本列表与对比视图", "批注 / 恢复 / 清理按钮"],
	"search": ["高级搜索停靠面板", "浮动搜索窗", "查询、替换与结果列表", "Ribbon search-alert 图标", "文件菜单 / 编辑器菜单的范围限定项", "替换前的命中列表"],
	"json": ["JSON Studio 树形编辑器", "<code>.json</code> 文件标签", "坏 JSON 校验提示"],
	"series": ["设置里的共享设定组", "组内源卷列表", "只读引用标记"],
	"export": ["导出面板（当前不提供可见入口）", "导出格式与范围选项", "命令面板搜索结果里的三条导出命令项"],
	"faq": ["问题索引列表", "指向各功能页的跳转链接", "按主题分组的问答条目", "顶栏「主页 / English / 主题」与左侧目录", "上一篇 / 下一篇翻页"],
	"data": ["插件 <code>data.json</code>", "作品 <code>System/*.json</code>", "数据位置对照表与联网范围说明"],
}

# 完全没有原有步骤章节的页面兜底
PAGE_STEPS_FALLBACK: dict[str, list[str]] = {
	"export": ["命令面板搜索「导出当前文件」或「导出当前文件夹」。", "也可搜「打开导出面板」选择范围与格式。", "当前版本不在 Ribbon / 设置里放入口，功能仍在维护中。"],
	"faq": ["按现象在本页找到对应条目。", "点条目里的链接跳到对应功能页看界面元素与操作步骤。"],
	"data": ["先看「数据位置对照表」确认要改的是哪个文件。", "需要重置某块视图时，只删对应的 <code>System/*.json</code>，不要删 <code>data.json</code>。"],
	"series": ["在设置里新建共享设定组并加入要共享的作品。", "组内作品互相只读引用设定，源文件仍留在各自卷内。", "勾选成员并自定组名称；一个作品只能进一组。", "要改设定：在面板顶部切到源作品再改。"],
	"destiny": ["在 <code>命运/</code> 下新建蓝图节点，或在脉络蓝图里连因果线。", "右侧伏笔总览会聚合这些节点并按状态显示。"],
	"journal": ["打开创作主页，找到「创作历程」组件。", "组件的记录来自命运文件的增删与关联，不需要单独维护。"],
}

# 个别页的命令表需要额外说明（不改变命令名本身）
PAGE_COMMAND_NOTES: dict[str, str] = {
	"settings": "其中「打开 UI 组件测试」通向开发用的 UI 组件测试面板（<code>src/features/Test/</code>），日常写作不需要它。",
}

GENERAL_CAUTIONS = [
	"本插件 manifest 声明 <code>isDesktopOnly: true</code>，最低 Obsidian 1.8.7；笔记始终是明文 Markdown，插件只读写 frontmatter 与 <code>System/*.json</code>。",
	"插件没有为任何命令注册默认快捷键，需要快捷键请到「设置 → 快捷键」按命令名搜索后自行绑定。",
]


def _classify(title: str) -> str:
	"""原 h2 标题 -> 标准章节 key。精确优先，再按最长关键词包含。"""
	if title in _MAP_LOOKUP:
		return _MAP_LOOKUP[title]
	for word in _SORTED_WORDS:
		if word in title:
			return _MAP_LOOKUP[word]
	return EXTRA_KEY


def _split_callouts(text: str) -> tuple[list[str], str]:
	"""把 C() 生成的 callout 从一段 HTML 里分出来，剩下的原样保留。"""
	parts = re.split(r"(?=<div class=\"callout callout-)", text)
	calls = [p.strip() for p in parts if p.strip().startswith('<div class="callout callout-')]
	rest = "".join(p for p in parts if not p.strip().startswith('<div class="callout callout-')).strip()
	return calls, rest


def _split_original(body: str) -> tuple[str, str, list[tuple[str, str]]]:
	"""返回 (lead 段, h2 之前的散段, [(原 h2 标题, 章节 HTML)])。"""
	lead_m = re.search(r'<p class="lead">[\s\S]*?</p>', body)
	lead = lead_m.group(0) if lead_m else ""
	rest = body.replace(lead, "", 1) if lead else body
	pieces = re.split(r"(?=<h2[^>]*>)", rest)
	head, sections = pieces[0].strip(), []
	for piece in pieces[1:]:
		m = re.match(r"<h2[^>]*>([\s\S]*?)</h2>([\s\S]*)", piece.strip())
		if m:
			sections.append((m.group(1).strip(), m.group(2).strip()))
	return lead, head, sections


def _kbd(text: str) -> str:
	"""把按键串画成 <kbd>，斜杠分隔的多个按键各自成块。"""
	chunks = [c.strip() for c in text.split(" / ") if c.strip()]
	return ' <span class="guide-or">或</span> '.join(
		f'<kbd class="kbd">{c}</kbd>' for c in chunks
	)


def _keyboard_html(pid: str) -> str:
	groups = ["global"] + PAGE_KEYBOARD.get(pid, [])
	rows: list[str] = []
	seen: set[str] = set()
	for g in groups:
		for keys, desc in KEYBOARD_GROUPS.get(g, []):
			if (keys, desc) in seen:
				continue
			seen.add((keys, desc))
			rows.append(f"<tr><td>{_kbd(keys)}</td><td>{desc}</td></tr>")
	note = NO_KEYBOARD.get(pid, "")
	if not rows:
		rows.append('<tr><td colspan="2">未注册视图级快捷键</td></tr>')
	blocks = [
		'<table class="key-table"><thead><tr><th>按键</th><th>作用</th></tr></thead><tbody>'
		+ "".join(rows) + "</tbody></table>"
	]
	if note:
		blocks.append(f"<p>{note}</p>")
	blocks.append(
		"<p>所有视图级快捷键在输入框、正文编辑态内都不触发（<code>isTypingTarget</code> 判定）；"
		"隐藏或失焦的面板也不响应。下表的「命令行」是另一套入口，两者不要混为一谈。</p>"
	)
	return "\n".join(blocks)


def _commands_html(pid: str, mapped: list[str]) -> str:
	ids = PAGE_COMMANDS.get(pid, [])
	blocks: list[str] = []
	if ids:
		unknown = [i for i in ids if i not in COMMAND_NAMES]
		if unknown:
			raise ValueError(f"{pid}: 命令 id 不在 COMMAND_NAMES 里: {unknown}")
		rows = "".join(
			f"<tr><td>{COMMAND_NAMES[i]}</td><td><code>{i}</code></td></tr>" for i in ids
		)
		blocks.append(
			"<p>在命令面板（<kbd class=\"kbd\">Ctrl/Cmd+P</kbd>）里搜「命令面板里的名称」这一列的中文名即可执行。"
			"下表同时给出命令 ID，方便在「设置 → 快捷键」里精确查找、以及在 <code>data.json</code> / 同步配置里核对。</p>"
		)
		blocks.append(
			'<table class="cmd-table"><thead><tr><th>命令面板里的名称</th><th>命令 ID</th></tr></thead>'
			f"<tbody>{rows}</tbody></table>"
		)
	elif pid == "commands":
		blocks.append(
			"<p>本页下面三张表按功能模块索引命令：小说创作、其它模块、编辑器 / 文件树右键入口。"
			"每条命令的中文名与命令 ID 对照表，列在对应功能页的「命令行」章节。</p>"
		)
	else:
		blocks.append(
			"<p>本功能没有注册独立的命令面板命令，入口见上方「操作方法与步骤」与「界面元素」。"
			'全部命令清单见 <a href="commands.html">命令与入口</a>。</p>'
		)
	blocks.append(
		"<p>以上命令<strong>均没有默认快捷键</strong>：源码里的 <code>addCommand</code> 没有声明 "
		"<code>hotkeys</code>，需要快捷键请自行到「设置 → 快捷键」绑定。"
		"命令面板本身由 Obsidian 提供，不是插件命令。</p>"
	)
	if pid in PAGE_COMMAND_NOTES:
		blocks.append(f"<p>{PAGE_COMMAND_NOTES[pid]}</p>")
	blocks.extend(mapped)  # commands 页原有的三张命令表
	return "\n".join(blocks)


def render_guide(pid: str, title: str, body: str, blurb: str, group: str, siblings: list[tuple[str, str]]) -> str:
	"""把 pages() 产出的旧正文重排成六段骨架。"""
	lead, head, original = _split_original(body)
	buckets: dict[str, list[str]] = {k: [] for k, _ in SECTIONS}
	buckets[EXTRA_KEY] = []

	# h2 之前的散段：callout 归注意事项，图片归界面元素，其余归其他
	head_calls, head_rest = _split_callouts(head)
	buckets["cautions"].extend(head_calls)
	if head_rest:
		target = "ui" if re.search(r"<img|<figure", head_rest) else EXTRA_KEY
		buckets[target].append(head_rest)

	for old_title, html in original:
		calls, plain = _split_callouts(html)
		buckets["cautions"].extend(calls)
		key = _classify(old_title)
		if pid == "commands" and key in {"ui", "steps", EXTRA_KEY}:
			key = "commands"  # 该页三张表本身就是命令索引
		if plain:
			buckets[key].append(f"<h3>{old_title}</h3>\n{plain}")

	# ① 功能简介
	intro = [lead] if lead else [f'<p class="lead">{blurb}</p>']
	intro.append(
		f"<p>本页属于「{group}」，按 <strong>功能简介 → 界面元素 → 操作方法与步骤 → 键盘操作 → "
		"命令行 → 注意事项</strong> 组织，末尾的「其他」放补充说明与相关页面。</p>"
	)
	buckets["intro"] = intro + buckets["intro"]

	# ② 界面元素：兜底清单在前，页面原有界面章节在后
	ui_items = PAGE_UI.get(pid, [])
	if ui_items:
		buckets["ui"].insert(0, "<h3>界面元素一览</h3>\n<ul>"
			+ "".join(f"<li>{x}</li>" for x in ui_items) + "</ul>")
	if not buckets["ui"]:
		buckets["ui"].append(f"<p>{title}的入口与部件见上方「功能简介」和下方「操作方法与步骤」。</p>")

	# ③ 操作方法与步骤：原有步骤偏薄时也补一份，保证这一章有可执行的动作
	steps_text = re.sub(r"<[^>]+>", "", "\n".join(buckets["steps"])).strip()
	steps = PAGE_STEPS_FALLBACK.get(pid, [])
	if steps and len(steps_text) < 60:
		buckets["steps"].append(
			'<h3>补充步骤</h3>\n<ol class="steps">'
			+ "".join(f"<li>{x}</li>" for x in steps) + "</ol>"
		)
	if not buckets["steps"]:
		buckets["steps"].append(
			'<p>本功能的操作入口与细则见「界面元素」以及 <a href="commands.html">命令与入口</a>；'
			'本页正文以规则与数据说明为主。</p>'
		)

	# ④ 键盘操作 ⑤ 命令行
	# 注意：buckets 的值必须始终是 list[str]，否则下面 "\n".join() 会把字符串逐字符拆开
	buckets["keyboard"].insert(0, _keyboard_html(pid))
	cmd_extra = buckets["commands"][:]
	buckets["commands"] = [_commands_html(pid, cmd_extra)]

	# ⑥ 注意事项
	cautions = list(GENERAL_CAUTIONS)
	if PAGE_KEYBOARD.get(pid) and pid not in NO_KEYBOARD:
		cautions.append("视图级快捷键只在画布 / 视图聚焦且可见时生效，输入框内不触发。")
	buckets["cautions"].append("<h3>通用限制</h3>\n<ul>"
		+ "".join(f"<li>{c}</li>" for c in cautions) + "</ul>")

	# ⑦ 其他：相关页面（同分组的其它功能）
	related = [(p, t) for p, t in siblings if p not in {"index", pid}][:6]
	if related:
		buckets[EXTRA_KEY].append(
			"<h3>相关页面</h3>\n<p>" + " · ".join(
				f'<a href="{p}.html">{t}</a>' for p, t in related
			) + "</p>"
		)
	buckets[EXTRA_KEY].append(
		'<p><a href="index.html">← 返回指南总览</a> · '
		'<a href="../index.html">↑ 返回产品主页</a></p>'
	)

	# 防御：章节桶必须是 list[str]，否则 "\n".join 会把字符串按字符拆开（标签碎裂）
	for key, value in buckets.items():
		if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
			raise TypeError(f"章节 {key} 不是 list[str]，拒绝生成碎裂的 HTML")

	# 导览 + 章节
	toc = '<nav class="guide-toc" aria-label="本页导览">' + "".join(
		f'<a href="#sec-{k}"><span class="guide-toc__no">{i}</span><span>{t}</span></a>'
		for i, (k, t) in enumerate(SECTIONS, 1)
	) + "</nav>"

	out = [f"<h1>{title}</h1>", toc]
	for key, label in SECTIONS:
		out.append(
			f'<section class="guide-section" id="sec-{key}" data-section="{key}">'
			f"<h2>{label}</h2>\n" + "\n".join(buckets[key]) + "\n</section>"
		)
	if buckets[EXTRA_KEY]:
		out.append(
			f'<section class="guide-section" id="sec-{EXTRA_KEY}" data-section="{EXTRA_KEY}">'
			f"<h2>{EXTRA_TITLE}</h2>\n" + "\n".join(buckets[EXTRA_KEY]) + "\n</section>"
		)
	return "\n".join(out)


def validate_facts() -> None:
	"""生成器自检：事实表不许出现悬空引用。"""
	for pid, ids in PAGE_COMMANDS.items():
		for cid in ids:
			if cid not in COMMAND_NAMES:
				raise ValueError(f"PAGE_COMMANDS[{pid}] 引用了未知命令 {cid}")
	for pid, groups in PAGE_KEYBOARD.items():
		for g in groups:
			if g not in KEYBOARD_GROUPS:
				raise ValueError(f"PAGE_KEYBOARD[{pid}] 引用了未知快捷键组 {g}")
	for pid in NO_KEYBOARD:
		if PAGE_KEYBOARD.get(pid):
			raise ValueError(f"{pid} 同时被标为「无快捷键」和「有快捷键组」")
	referenced = {cid for ids in PAGE_COMMANDS.values() for cid in ids}
	orphan = sorted(set(COMMAND_NAMES) - referenced)
	if orphan:
		raise ValueError(f"COMMAND_NAMES 有命令没被任何指南页引用: {orphan}")
