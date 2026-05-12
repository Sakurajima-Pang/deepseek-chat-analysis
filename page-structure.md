# 页面结构图

> 更新: 2026-05-12  |  视口约定: 1920x1080 (最大化 + 固定 DevTools)

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
```

## 状态字典

### sidebar  — 侧边栏

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 展开 | - | classes=dc04ec1d | width=261 | childCount=1 | - |
| 收起 | - | classes=dc04ec1d, a02af2e6 | width=0 | childCount=2 | - |

### sidebar-inner  — 侧边栏主容器

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 展开 | sidebar=展开 | classes=b8812f16, a2f3d50e | width=261 | childCount=4 | - |
| 隐藏 | sidebar=收起 | classes=b8812f16, a2f3d50e, _70b689f | width=0 | childCount=4 | - |

### sidebar-inner-header  — 顶部栏

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_262baab | width=236 | childCount=2 | - |

### sidebar-inner-header-logo  — DeepSeek图标

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=e066abb8 | childCount=1 | - |

### sidebar-inner-header-actions  — 头部操作按钮组

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_23e1c55 | childCount=2 | - |

### sidebar-inner-header-actions-search  — 搜索按钮

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=d05a0287, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-icon | childCount=3 | - |

### sidebar-inner-header-actions-collapse  — 收起按钮

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_7d1f5e2, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-icon | childCount=3 | - |

### sidebar-inner-history  — 历史对话列表

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_3586175, ds-scroll-area, ds-scroll-area--show-on-focus-within | width=236 | childCount=3 | - |

### sidebar-inner-history-scroll  — 滚动容器

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_6d215eb, ds-scroll-area, ds-scroll-area--show-on-focus-within | childCount=2 | - |

### sidebar-inner-history-list  — 对话列表

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_77cdc67, _8a693f3 | childCount=9 | - |

### sidebar-inner-history-scrollmarker  — 滚动标记

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=de3d058c | childCount=0 | - |

### sidebar-inner-user  — 用户信息

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_2afd28d | width=236 | childCount=4 | - |

### sidebar-inner-user-avatar  — 用户头像

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=ede5bc47 | childCount=1 | - |

### sidebar-inner-user-name  — 用户名称

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=_9d8da05 | childCount=0 | - |

### sidebar-inner-user-settings  — 设置按钮(三点)

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 默认 | - | classes=ds-icon, _39cc453 | childCount=1 | - |

### sidebar-handle  — 收起的把手

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=ca6d4be1, _5a20a69 | width=157 | childCount=2 | - |

### sidebar-handle-icon  — 展开图标(鲸鱼)

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_6acebc2 | childCount=1 | - |

### sidebar-handle-actions  — 操作按钮组

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=e5bf614e | width=114 | childCount=4 | - |

### sidebar-handle-actions-spacer  — 占位元素

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | width=1 | childCount=0 | - |

### sidebar-handle-actions-expand  — 展开按钮

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container | width=34 | childCount=3 | ⚠ |

**可见** 备注:
> 与搜索/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD: M9.67272 0.522841...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector: div.e5bf614e > div:nth-child(2)

### sidebar-handle-actions-search  — 搜索按钮

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container | width=34 | childCount=3 | ⚠ |

**可见** 备注:
> 与展开/新建按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD(2条): M11.894845 6.647401... / M16.000417 15.041079...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector: div.e5bf614e > div:nth-child(3)

### sidebar-handle-actions-newchat  — 新建对话按钮

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 可见 | sidebar=收起 | classes=_4f3769f, ds-icon-button, ds-icon-button--l, ds-icon-button--sizing-container | width=34 | childCount=3 | ⚠ |

**可见** 备注:
> 与展开/搜索按钮 class 及 HTML 结构完全相同(均为 div._4f3769f.ds-icon-button.ds-icon-button--l.ds-icon-button--sizing-container > div.ds-icon > svg)，无法通过 class 区分。
> 标识方法(按稳定性排序):
> ① pathD: M8 0.599609...
> ② SVG 属性: viewBox=0 0 16 16 width=16 height=16
> ③ selector: div.e5bf614e > div:nth-child(4)

### main-panel  — 主面板

| 状态 | 前置条件 | 特征 | 备注 |
|------|----------|------|------|
| 侧边栏展开时 | sidebar=展开 | x=261 | width=995 | - |
| 侧边栏收起时 | sidebar=收起 | x=0 | width=1256 | - |
