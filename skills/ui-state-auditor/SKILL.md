---
name: ui-state-auditor
description: Use when a frontend review needs user-perspective checks for contradictory state signals, unclear action ownership, mixed object identity, transient-state leaks, misalignment, overlap, clipping, or responsive geometry failures.
---

# UI State Auditor

从用户视角审查 UI 细节。这个 skill 不做泛泛的“美化建议”，只抓会让用户困惑、犹豫、误操作，或让界面显得破裂的具体问题。

核心判断：用户现在以为自己在哪里、当前对象是谁、下一步操作会影响谁；界面发出的状态信号和视觉几何是否支持这个判断。

## 何时使用

自动轻量使用：

- 完成前端 UI 改动后，若改动涉及侧边栏、列表、表格、卡片、聊天面板、导航、标签页、菜单、多对象仪表盘。
- 完成截图验证后，若界面包含 selected、hover、focus、loading、current-object、menu-open 等状态。
- 改动可能造成按钮文字溢出、元素不居中、尺寸比例异常、内容重叠、浮层错位、长文本撑破布局。

手动深度使用：

- 用户说 `/ui-state-audit`、`检查 UI 状态`、`从用户视角查细节`、`看看这个 UI 有没有细小问题`、`这个界面哪里让用户困惑`。
- 用户提供截图并指出“感觉不对”“不好描述”“细节有问题”。
- 用户要求在真实路径里复查 hover、focus、点击、菜单打开/关闭、响应式、长文本、多语言等状态。

## 不做什么

- 不做整页视觉重设计。
- 不评价纯审美偏好，例如“高级不高级”。
- 不替代完整无障碍审查。
- 不替代像素级视觉回归测试。
- 不替代通用代码 review。

## 审查支柱

### 1. 状态语义

检查界面的状态信号是否和用户心智模型一致：

- 状态信号矛盾：多个同级对象同时像当前项、选中项、焦点项、按下项或主操作。
- 操作入口噪音：太多控件同时显得可以立即操作，用户不知道操作会作用于谁。
- 对象身份混淆：重复名称、图标、徽标或状态让多个对象看起来像同一个对象。
- 瞬态状态泄漏：hover、focus、pressed、menu-open、loading、active 等临时状态残留。

详见 `references/state-taxonomy.md`。

### 2. 视觉几何与可读性

检查基础布局是否可靠：

- 位置与对齐异常：不居中、不同组、边距不均、图标文字基线错位。
- 尺寸比例不合理：按钮、图标、输入框、卡片、侧栏、列表行高过大或过小。
- 重叠、遮挡与层级错误：文本、按钮、菜单、浮层、角标互相遮挡或错层。
- 文本溢出与容器不适配：文字超出按钮/标签/卡片，长词不换行，省略号错误。
- 视觉节奏不稳定：同组元素高度、圆角、间距、图标尺寸、按钮密度不一致。

详见 `references/visual-geometry-checks.md`。

## 轻量审查流程

用于前端改动后的默认自检。只看改动范围和当前可见 UI，不默认写文件。

1. 写一句用户心智模型：
   - 用户以为自己在哪里？
   - 当前对象是谁？
   - 当前任务是什么？

2. 盘点状态信号：
   - active、selected、hover、focus、pressed、loading、menu-open、disabled、primary、badge。

3. 盘点视觉几何信号：
   - 是否居中、是否对齐、尺寸是否合理、是否重叠、文字是否溢出、浮层是否错位。

4. 判断归属：
   - 每个状态或视觉强调属于哪个对象、哪个任务、哪个层级。

5. 标记问题：
   - 只报告能具体说明证据、影响和修复方向的问题。

6. 简短输出：
   - 不写长篇审美建议。
   - 不把“可能”包装成确定结论。
   - 如果没有证据，说明未覆盖路径或视口。

## 深度审查流程

用户明确要求深度检查时使用。必要时结合 `webapp-testing`、Playwright、截图和 DOM 检查。

1. 确定审查路径：
   - 页面 URL 或本地应用入口。
   - 用户路径：进入页面、选择对象、hover、focus、打开菜单、关闭菜单、切换对象、切换视口。

2. 收集证据：
   - 静止截图。
   - hover 后截图。
   - 键盘 focus 后截图。
   - 点击或打开菜单后截图。
   - 菜单关闭或路由切换后截图。
   - 窄屏、宽屏和常用桌面视口截图。
   - 长文本、重复名称、多语言或极端数据截图。
   - DOM 状态属性：`aria-selected`、`aria-current`、`aria-expanded`、`disabled`、`data-state`、class 名。
   - 元素尺寸、bounding box、computed style、overflow 状态。

3. 对照参考文件：
   - 状态问题看 `references/state-taxonomy.md`。
   - 视觉几何问题看 `references/visual-geometry-checks.md`。
   - 取证方法看 `references/inspection-playbook.md`。
   - 示例看 `references/examples.md`。

4. 输出结论：
   - 默认在终端输出。
   - 只有用户要求或问题较多时，才写 `UI-STATE-AUDIT.md`。

## 输出格式

发现问题时：

```text
UI 细节审查：发现 N 个问题

[HIGH] 简短标题
证据：用户实际看到什么。
影响：为什么这会让用户困惑或误操作。
修复：具体改法。
```

没有发现问题时：

```text
UI 细节审查：未发现关键状态或视觉几何问题。
已检查：当前对象、状态信号归属、操作入口、重复对象身份、瞬态状态清理、对齐、尺寸、重叠、文字溢出。
残余风险：未覆盖的路径或视口。
```

严重程度：

- `HIGH`：用户可能操作错对象、失去信任，或无法判断当前对象；或布局破裂影响核心操作。
- `MEDIUM`：界面仍可理解，但会造成明显犹豫；或常见内容下出现可见破裂。
- `LOW`：轻微细节问题，不影响任务信心。

## 修复建议要求

每个问题都必须给具体修复方向：

- 保留哪个状态，移除或弱化哪个状态。
- current、selected、hover、focus 分别应使用哪个视觉 token。
- 是否需要增加对象身份信息，例如时间、来源、路径、状态。
- 控件是否应只在 hover/focus 或选中时出现。
- 交互结束后是否需要清理残留状态。
- 是否需要 `min-width`、`max-width`、`flex-wrap`、`text-overflow`、`line-clamp` 或响应式约束。
- 是否需要统一同组控件的高度、图标尺寸、圆角、间距。
- 是否需要调整浮层定位、z-index、滚动容器或碰撞检测。
- 是否需要为长文本、多语言、窄屏设置兜底样式。
