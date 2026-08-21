# 检查取证手册

这个手册说明如何收集证据。目标不是跑尽所有自动化，而是让问题可复现、可定位、可修。

## 轻量模式

适合完成 UI 改动后的自检。

步骤：

1. 看当前截图或当前页面。
2. 写一句用户心智模型。
3. 标出所有高优先级状态信号。
4. 标出明显视觉几何问题。
5. 只报告有清晰证据的问题。

轻量模式可以不启动浏览器自动化，但不能凭空猜测。

## 深度模式

适合用户明确要求检查 UI 细节，或问题只在交互后出现。

建议路径：

1. 打开页面。
2. 等待动态内容加载完成。
3. 截静止状态。
4. hover 关键对象并截图。
5. 用键盘 Tab focus 关键控件并截图。
6. 点击打开菜单、popover、dialog 并截图。
7. 关闭菜单或切换对象，再截图。
8. 切换窄屏、宽屏、常见桌面视口。
9. 注入或模拟长文本、重复名称、多语言、空状态、加载状态、错误状态。

## DOM 与样式证据

优先检查：

- `aria-current`
- `aria-selected`
- `aria-expanded`
- `aria-pressed`
- `disabled`
- `data-state`
- `data-active`
- `data-selected`
- class 名中的 active/selected/focus/hover/open/loading/current
- bounding box
- computed style
- overflow 状态
- z-index

判断原则：

- DOM 状态和视觉状态不一致时，按用户看到的视觉状态优先报告。
- 视觉状态有争议时，用 DOM 状态辅助解释。
- 如果没有运行环境，明确说明只做了静态审查。

## Playwright 建议

如果需要浏览器验证，可使用 Playwright：

- 截图：`page.screenshot(...)`
- 鼠标悬停：`locator.hover()`
- 键盘导航：`page.keyboard.press('Tab')`
- 点击：`locator.click()`
- 视口：`page.set_viewport_size(...)`
- 尺寸：`locator.bounding_box()`
- 样式：`locator.evaluate(...)` 读取 computed style

常用视口：

- 375x812：移动端窄屏
- 768x1024：平板
- 1280x720：小桌面
- 1440x900：常见桌面
- 1920x1080：宽桌面

## 极端内容样本

用于发现文字溢出和对象身份混淆：

- 很长的中文标题
- 很长的英文单词
- 文件路径
- 重复名称
- 带编号的重复对象
- 多语言混排
- 超长金额或数字
- 空状态
- 错误状态
- 加载中状态

## 报告证据要求

每个问题至少包含：

- 触发路径
- 观察到的界面表现
- 用户为什么会被误导或受阻
- 具体修复方向

不要只写：

- “优化布局”
- “调整样式”
- “这里不太好看”
- “建议美化”

要写：

- “当前只有一个会话打开，但三个同级列表项都有 selected-like 背景。”
- “按钮宽度 72px，但文本需要 96px，导致文字越过右边界。”
- “菜单关闭后 trigger 仍保留 open 背景，用户会以为菜单还在打开。”

