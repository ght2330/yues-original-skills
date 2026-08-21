---
name: figma-workflow
description: Use when a task explicitly requires Figma files, Figma links, Figma plugins, Figma MCP, or keeping a Figma design and its code counterpart synchronized.
---

# Figma Workflow

Claude Code 与 Figma 双向同步的完整工作流 skill，覆盖环境配置、设计生成、推送到 Figma 和从 Figma 回传代码的全流程。

## 使用场景

- 用户需要配置 Claude Code 与 Figma 的 MCP 连接
- 用户需要用 AI 生成 UI 设计并推送到 Figma
- 用户需要从 Figma 设计稿同步变更到代码
- 用户提到 Figma、设计同步、UI 生成等关键词

## 与 Penpot Workflow 的边界

如果用户没有明确要求 Figma，而是提到 Penpot、开源设计平台、自部署设计工具、私有设计资产、Design Tokens、MCP 直接读取 components/layers/tokens，优先使用 `penpot-workflow`。

本 skill 保留为 Figma 生态兼容路线：外部团队已经使用 Figma、必须交付 Figma 文件/链接、依赖 Figma 插件或模板时使用。

## 工作流概览

本 skill 包含五个阶段：

1. **环境检查** — 验证 Claude Code 版本、Figma MCP 配置
2. **MCP 连接** — 添加 Figma MCP 并完成授权
3. **Plugin 安装** — 安装 Figma 官方插件
4. **Code → Figma** — 生成 HTML 设计并推送到 Figma
5. **Figma → Code** — 从 Figma 变更同步回代码

## 阶段一：环境检查

运行环境检查脚本确认当前状态：

```bash
python "<skill_dir>/scripts/figma_env_check.py"
```

脚本会检查：
- Claude Code 是否已安装及版本号
- Figma MCP 是否已配置在 `~/.claude.json`
- Node.js / npm 是否可用

若环境检查通过，跳过配置阶段直接进入使用阶段。

## 阶段二：连接 Figma MCP

若 Figma MCP 尚未配置，执行以下命令添加：

```bash
claude mcp add --scope user --transport http figma https://mcp.figma.com/mcp
```

此命令将 Figma MCP 注册为全局用户级配置，所有项目共享。

添加后需要手动授权（需在 Claude Code 交互终端中操作）：

1. 在 Claude Code 终端输入 `/mcp` 回车
2. 选择 **figma** 回车
3. 选择 **Authenticate** 回车
4. 浏览器会自动弹出 Figma 登录页面
5. 登录 Figma 账号并点击 **Allow Access**
6. 回到终端看到 `Authentication successful. Connected to figma.` 即成功

**重要：** 授权步骤需要用户在 Claude Code 交互终端中手动操作，无法通过脚本自动完成。提醒用户切换到 Claude Code 终端执行。

## 阶段三：安装 Figma Plugin

在 Claude Code 交互终端中执行：

```
/plugin install figma@claude-plugins-official
```

验证安装：输入 `/plugin` → 选择 `installed` 确认 figma 插件已列出。

**注意：** 此步骤同样需要在 Claude Code 交互终端中操作。

## 阶段四：Code → Figma（生成设计并推送）

### 前置条件
- Figma MCP 已连接且授权
- Figma Plugin 已安装
- 用户提供一个空的 Figma 文件链接

### 工作流程

1. 用户创建一个空的 Figma 文件，复制文件链接
2. 在 HTML 文件的 `<head>` 中引入 Figma capture 脚本：

```html
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
```

3. 根据用户需求生成产品 UI 的 HTML/CSS/JS 代码
4. 在 Claude Code 中使用如下格式的提示词：

```
直接在这个空的 Figma 文件里，为我设计[具体需求描述]。
设计完成后，再帮我生成对应的 HTML/CSS/JS 代码：[Figma文件链接]
```

5. 执行过程中遇到选项提示，选择 yes 继续
6. 执行完成后浏览器会弹出预览，点击「发送到 Figma」推送设计

### HTML 设计模板

生成 HTML 时遵循以下原则：
- 使用语义化 HTML5 标签
- CSS 使用 CSS 变量管理主题色
- 引入 `capture.js` 脚本以支持 Figma 推送
- 使用现代设计风格（圆角、渐变、阴影、玻璃态等）
- 响应式布局

参考 `references/html-design-guide.md` 获取详细的设计规范。

## 阶段五：Figma → Code（设计变更回传）

当用户在 Figma 中修改了设计稿后：

1. 在 Figma 中选择修改的部分
2. 右键选择 **Copy link to selection**（复制选区链接）
3. 在 Claude Code 中输入：

```
update changes:[粘贴复制的Figma选区链接]
```

4. Claude Code 会自动根据 Figma 设计变更重新构建对应的代码部分

## 常见问题排查

### 400 错误
若遇到 HTTP 400 错误，可能是 Claude Code 版本兼容性问题：
- 查看当前版本：`claude --version`
- 尝试降级一个小版本：让 AI 帮忙执行降级命令

### MCP 连接失败
- 确认网络可访问 `https://mcp.figma.com`
- 重新执行 `claude mcp add` 命令
- 检查 `~/.claude.json` 中是否有 figma 配置

### 推送到 Figma 失败
- 确认 HTML 中已引入 `capture.js` 脚本
- 确认 Figma 文件链接正确
- 确认 Figma 授权未过期，必要时重新授权

## 注意事项

- Figma MCP 授权和 Plugin 安装必须在 Claude Code 交互终端中手动完成
- HTML 文件必须包含 Figma capture.js 脚本才能推送到 Figma
- Figma 免费账户可能有 API 调用限制
- 建议使用最新版 Claude Code 以获得最佳兼容性
