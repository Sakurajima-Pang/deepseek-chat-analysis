# 页面结构图

> 更新: 2026-05-13  |  视口约定: 实际窗口大小（由用户手动最大化决定，1920x1080为参考）

## 零件树

```
root  根容器
├── sidebar  侧边栏
    ├── sidebar-inner  侧边栏主容器
        ├── sidebar-inner-header  顶部栏
            ├── sidebar-inner-header-logo  DeepSeek图标
            └── sidebar-inner-header-actions  头部操作按钮组
                ├── sidebar-inner-header-actions-search  搜索按钮
                └── sidebar-inner-header-actions-collapse  收起按钮
        ├── sidebar-inner-history  历史对话列表
            └── sidebar-inner-history-scroll  滚动容器
                ├── sidebar-inner-history-list  对话列表
                └── sidebar-inner-history-scrollmarker  滚动标记
        └── sidebar-inner-user  用户信息
            ├── sidebar-inner-user-avatar  用户头像
            ├── sidebar-inner-user-name  用户名称
            └── sidebar-inner-user-settings  设置按钮(三点)
    └── sidebar-handle  收起的把手
        ├── sidebar-handle-icon  展开图标(鲸鱼)
        └── sidebar-handle-actions  操作按钮组
            ├── sidebar-handle-actions-spacer  占位元素
            ├── sidebar-handle-actions-expand  展开按钮
            ├── sidebar-handle-actions-search  搜索按钮
            └── sidebar-handle-actions-newchat  新建对话按钮
└── main-panel  主面板
    └── main-content  主内容容器
        ├── main-content-title  标题栏
        ├── main-content-scrollbar  滚动条占位
        ├── main-content-list  主要交互界面
            ├── main-content-messages  对话消息列表
            ├── main-content-gap  间隔条
            └── main-content-input  输入面板
        ├── main-content-quicknav  快速定位列表
        └── main-content-welcome  欢迎界面
```

## 状态字典

### sidebar  — 侧边栏  <i>角色: 侧边栏整体展开，允许用户查看历史对话和操作</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 展开 | - | classes=dc04ec1d / width=261 / childCount=1 | - |
| 收起 | - | classes=dc04ec1d, a02af2e6 / width=0 / childCount=2 | - |

### sidebar-inner  — 侧边栏主容器  <i>角色: 承载全部侧边栏内容（顶部栏+历史列表+用户信息），依赖sidebar=展开</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 展开 | sidebar=展开 | classes=b8812f16, a2f3d50e / width=261 / childCount=4 | - |
| 隐藏 | sidebar=收起 | classes=b8812f16, a2f3d50e, _70b689f / width=0 / childCount=4 | - |

### sidebar-inner-header  — 顶部栏  <i>角色: 顶部栏：品牌logo + 搜索/收起按钮</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_262baab / width=236 / childCount=2 | - |

### sidebar-inner-header-logo  — DeepSeek图标  <i>角色: DeepSeek品牌图标（鲸鱼+文字），鼠标pointer。上下文相关行为：无活跃对话时点击无效果；有活跃对话时等价于「开启新对话」按钮</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=e066abb8 / childCount=1 | - |

### sidebar-inner-header-actions  — 头部操作按钮组  <i>角色: 头部操作按钮容器，包含搜索和收起两个按钮</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_23e1c55 / childCount=2 | - |

### sidebar-inner-header-actions-search  — 搜索按钮  <i>角色: 打开对话搜索面板（带放大镜图标）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=d05a0287, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-icon / childCount=3 | - |

### sidebar-inner-header-actions-collapse  — 收起按钮  <i>角色: 收起侧边栏（带侧边栏图标）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_7d1f5e2, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-icon / childCount=3 | - |

### sidebar-inner-history  — 历史对话列表  <i>角色: 可滚动区域，展示按日期分组的聊天列表</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_3586175, ds-scroll-area, ds-scroll-area--show-on-focus-within / width=236 / childCount=3 | - |

### sidebar-inner-history-scroll  — 滚动容器  <i>角色: 内部滚动容器：承载对话列表节点 + 滚动条</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_6d215eb, ds-scroll-area, ds-scroll-area--show-on-focus-within / childCount=2 | - |

### sidebar-inner-history-list  — 对话列表  <i>角色: 按日期分组的对话条目列表（如'今天'、'昨天'、'7天内'等），内容量不定</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_77cdc67, _8a693f3 / childCount=9 | - |

### sidebar-inner-history-scrollmarker  — 滚动标记  <i>角色: 滚动条底部的空标记div，无可见内容</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=de3d058c / childCount=0 | - |

### sidebar-inner-user  — 用户信息  <i>角色: 底部用户信息区：头像 + 用户名 + 设置入口</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_2afd28d / width=236 / childCount=4 | - |

### sidebar-inner-user-avatar  — 用户头像  <i>角色: 用户头像图片</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=ede5bc47 / childCount=1 | - |

### sidebar-inner-user-name  — 用户名称  <i>角色: 显示用户名文本（如'吉吉国王'），不可交互</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_9d8da05 / childCount=0 | - |

### sidebar-inner-user-settings  — 设置按钮(三点)  <i>角色: 三点设置按钮，hover时显示设置弹出框</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=ds-icon, _39cc453 / childCount=1 | - |

### sidebar-handle  — 收起的把手  <i>角色: 侧边栏收起时出现的替代操作区（鲸鱼图标 + 快捷按钮）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=ca6d4be1, _5a20a69 / width=157 / childCount=2 | - |

### sidebar-handle-icon  — 展开图标(鲸鱼)  <i>角色: 展开图标（鲸鱼），点击展开侧边栏，功能与展开按钮重复</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_6acebc2 / childCount=1 | - |

### sidebar-handle-actions  — 操作按钮组  <i>角色: 收起状态下的快捷按钮组，含占位+展开+搜索+新建对话</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=e5bf614e / width=114 / childCount=4 | - |

### sidebar-handle-actions-spacer  — 占位元素  <i>角色: 结构占位元素，无功能</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | width=1 / childCount=0 | - |

### sidebar-handle-actions-expand  — 展开按钮  <i>角色: 展开按钮（侧边栏箭头图标），与鲸鱼图标点击效果相同</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container / width=34 / childCount=3 | ! 与搜索/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。 |

**可见** 备注:
> 与搜索/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD: M9.67272 0.522841...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector 位置: div.e5bf614e > div:nth-child(2)

### sidebar-handle-actions-search  — 搜索按钮  <i>角色: 对话搜索按钮（收起状态下替代顶部栏搜索按钮）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container / width=34 / childCount=3 | ! 与展开/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。 |

**可见** 备注:
> 与展开/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD(2条): M11.894845 6.647401... / M16.000417 15.041079...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector 位置: div.e5bf614e > div:nth-child(3)

### sidebar-handle-actions-newchat  — 新建对话按钮  <i>角色: 新建对话按钮（收起状态下创建新对话）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container / width=34 / childCount=3 | ! 与展开/搜索按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。 |

**可见** 备注:
> 与展开/搜索按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法仅通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD: M8 0.599609...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector 位置: div.e5bf614e > div:nth-child(4)

### main-panel  — 主面板  <i>角色: 聊天内容展示区，位置在侧边栏右侧。内部内容取决于会话状态（已有会话 or 新建会话）</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 侧边栏展开时 | sidebar=展开 | x=261 / width=995 | - |
| 侧边栏收起时 | sidebar=收起 | x=0 / width=1256 | - |

### main-content  — 主内容容器  <i>角色: 主内容容器，承载标题栏+滚动历史+输入面板。childCount=4 时为此状态</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 已有会话 | - | - | - |
| 新建会话 | - | - | - |

### main-content-title  — 标题栏  <i>角色: 已有会话的标题栏，显示会话名称和操作按钮</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 已有会话 | - | classes=_2be88ba / width=995 / height=60 / childCount=3 | sel: class=_2be88ba |
| 新建会话 | - | classes=_2be88ba, _1551317 / width=995 / height=60 / childCount=2 | sel: class=_2be88ba._1551317 |

### main-content-scrollbar  — 滚动条占位  <i>角色: 滚动条轨道，仅在已有会话（可滚动历史列表时）出现</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | classes=ds-scroll-area__gutters / childCount=2 | - |

### main-content-list  — 主要交互界面  <i>角色: 虚拟列表，主要交互界面，承载所有对话消息和底部输入面板</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | classes=_2bd7b35, ds-virtual-list, ds-virtual-list--printable / width=995 / height=841 / childCount=3 | - |

### main-content-messages  — 对话消息列表  <i>角色: 按日期分组的对话消息容器，内含所有用户消息和LLM回复。高度随内容动态增长</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | classes=ds-virtual-list-items, _6f2c522 / width=907 / childCount=1 | - |

### main-content-gap  — 间隔条  <i>角色: 消息列表和输入面板之间的空间隔条（占位），无可见内容</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | childCount=0 / height=24 | - |

### main-content-input  — 输入面板  <i>角色: 输入面板区域，包含配置按钮、文件上传按钮和发送按钮等。详情待分析</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | classes=_871cbca / width=931 / height=152 / childCount=3 | - |

### main-content-quicknav  — 快速定位列表  <i>角色: 侧边快速导航条，hover时展开显示各条目的摘要内容。仅在已有会话时出现</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | - | classes=_189b4a0 / width=34 / childCount=2 | - |

### main-content-welcome  — 欢迎界面  <i>角色: 新建会话的欢迎/模式选择面板，包含快速模式、专家模式、深度思考、智能搜索等入口</i>

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | main-content=新建会话 | classes=_660ca72 / width=995 / childCount=2 | - |
