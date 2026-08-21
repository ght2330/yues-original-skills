# YueS Original Skills

一组可以直接安装到 Codex、Claude Code 等支持 `SKILL.md` 的 Agent 工具中的工作流 Skill。

这些 Skill 解决的是具体工作问题：如何把参考网页变成设计规则、如何读写 Penpot 或 Figma、如何制作可编辑演示文稿、如何减少中文 AI 腔、如何审查界面状态，以及如何把网页资料放进可维护的 Obsidian 知识库。

## Skills

| Skill | 用途 |
| --- | --- |
| `reference-driven-web-design` | 从真实网页参考中提炼可批准、可实现的设计规则 |
| `penpot-workflow` | 围绕 Penpot 文件、组件、图层和 Design Tokens 工作 |
| `figma-workflow` | 在 Figma 与代码之间进行有边界的双向同步 |
| `visual-first-penpot-deck` | 先完成视觉，再重建为可编辑 Penpot 源和 PDF |
| `humanizer-zh` | 识别并改写中文文本中的模板化 AI 表达 |
| `ui-state-auditor` | 从用户视角定位状态、对象身份和几何布局问题 |
| `obsidian-kb` | 按 source → wiki → schema 三层维护 Obsidian 知识库 |

## 安装

安装单个 Skill：

```bash
npx skills add https://github.com/ght2330/yues-original-skills --skill reference-driven-web-design
```

把命令最后的 Skill 名换成表格中的任意名称即可。也可以直接下载仓库后，将对应目录复制到你的 Agent 工具的 skills 目录。

## 使用前的本地配置

- `penpot-workflow` 需要你自己的 Penpot MCP 或 Penpot 文件。
- `figma-workflow` 需要你自己的 Figma MCP、文件和授权环境。
- `obsidian-kb` 需要一个包含 `00_sources`、`10_wiki`、`90_schema` 的 vault；Skill 中的 `<vault-root>` 是占位符。

不要把 MCP key、访问令牌、知识库内容或本机绝对路径提交到仓库。

## 许可证与来源

本仓库中 YueS 编写的 Skill 采用 MIT License。`humanizer-zh` 保留其目录内原有的 MIT 许可证和上游来源说明；它的部分内容翻译或参考自 `blader/humanizer` 与 `hardikpandya/stop-slop`，请同时遵守对应项目的许可证和署名要求。

欢迎通过 Issue 或 Pull Request 提交修正、适配说明和新的公开参考资料。
