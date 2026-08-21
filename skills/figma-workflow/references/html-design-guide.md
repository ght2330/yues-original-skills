# HTML Design Guide for Figma Workflow

生成可推送到 Figma 的 HTML 设计时，遵循以下规范。

## 必须包含的 Figma 脚本

在 `<head>` 标签内引入 Figma capture 脚本：

```html
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
```

没有此脚本，HTML 无法被推送到 Figma。

## HTML 结构规范

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>页面标题</title>
    <style>
        /* CSS 样式 */
    </style>
    <script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>
```

## CSS 设计规范

### 颜色系统

使用 CSS 变量统一管理主题色：

```css
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --primary-light: #818cf8;
    --accent: #06b6d4;
    --dark: #0f172a;
    --gray: #64748b;
    --light: #f8fafc;
    --white: #ffffff;
    --gradient-1: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
}
```

### 现代设计元素

- **圆角**: 按钮 10-14px，卡片 16-24px
- **阴影**: 使用多层阴影增加层次感
- **渐变**: 用于按钮、背景装饰、文字高亮
- **毛玻璃效果**: `backdrop-filter: blur(20px)` 用于导航栏等
- **悬浮动画**: `transform: translateY(-2px)` 搭配 transition

### 字体选择

推荐使用系统字体栈或 Google Fonts：

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

### 布局方式

- 容器宽度: `max-width: 1400px; margin: 0 auto;`
- 使用 Flexbox 做水平排列
- 使用 CSS Grid 做卡片网格布局
- 间距建议: 8px 的倍数（8, 16, 24, 32, 40, 48, 60, 80, 120）

## 常用页面组件

### 导航栏
- 固定顶部 `position: fixed`
- 毛玻璃背景
- Logo + 导航链接 + 操作按钮

### Hero 区域
- 大标题 + 副标题 + CTA 按钮
- 可选数据统计条
- 右侧视觉元素（代码卡片、产品截图等）

### 特性展示
- 3 列网格布局
- 图标 + 标题 + 描述文字
- 悬浮效果

### 数据展示
- 左右布局（图表 + 文字说明）
- 指标卡片

### 用户评价
- 3 列卡片
- 星级评分 + 引言 + 用户信息

### CTA 区域
- 深色背景卡片
- 标题 + 描述 + 按钮组

### 页脚
- 多列链接
- Logo + 简介
- 社交媒体图标

## Figma 推送注意事项

1. 所有样式内联或写在 `<style>` 标签中（不要引用外部 CSS 文件）
2. 使用具体的颜色值，不要依赖外部主题
3. 图片建议使用 SVG 内联或纯 CSS 图形
4. 文字内容要完整，不要用占位符
5. 保持单文件结构，一个 HTML 文件包含所有内容
