---
name: obsidian-kb
description: Use when working on an Obsidian knowledge base with a three-layer source, knowledge, and schema structure, especially for `/kb <url-or-source>` ingestion tasks.
---

# Obsidian KB

这个 skill 需要一个已经存在的 Obsidian vault，并假定 vault 内有 `00_sources`、`10_wiki` 和 `90_schema` 三层目录。把文中的 `<vault-root>` 替换为实际 vault 根目录；不要把本机路径写进共享配置。

## Trigger

在这些场景使用：

- 用户发送 `/kb <url-or-source>`
- 用户要求“一步落库”“一条命令入库”“直接扩充知识库”
- 用户要按 `90_schema` 规则把新资料沉淀进 `10_wiki`

不要在这些场景使用：

- 纯 query 问答
- 需要修改 `90_schema` 规则
- 与目标 vault 无关的普通文档整理

## Required Read

执行前先读：

1. `<vault-root>/90_schema/agent-bootstrap.md`
2. `<vault-root>/docs/obsidian-wiki-operations-guide.md`（如果项目提供）
3. `<vault-root>/10_wiki/indexes/home.md`
4. `<vault-root>/90_schema/README.md`
5. `<vault-root>/90_schema/slash-commands.md`

如果要实际落库，再补读：

6. `<vault-root>/90_schema/maintenance-workflow.md`
7. `<vault-root>/90_schema/ingest-prompt.md`
8. `<vault-root>/90_schema/lint-prompt.md`
9. `<vault-root>/90_schema/web-clip-source-template.md`
10. `<vault-root>/90_schema/naming-rules.md`

优先用官方 CLI：

```text
obsidian vault=Wiki read path=90_schema/agent-bootstrap.md
```

如果 CLI 不可用，再直接读取文件。

## Command Contract

### `/kb <url>`

按这个顺序执行：

1. 在 `00_sources/web-clips` 创建 `YYYY-MM-DD-主题-web.md`
2. 保留原始 URL，并填写 `Content status`
3. 对新 source 执行 ingest
4. 对本轮改动涉及的 wiki 页面做 scoped lint

### `/kb <source-note>`

按这个顺序执行：

1. 在 `00_sources` 内定位 source note
2. 对该 source 执行 ingest
3. 对本轮改动涉及的 wiki 页面做 scoped lint

## Non-Negotiable Rules

- 当前库是 Karpathy 兼容模式，不是原样复制
- `90_schema` 是本地最高优先级规则层
- 只按 `00_sources -> 10_wiki -> 90_schema` 三层运行
- URL 输入时，只允许新建 source 于 `00_sources`
- ingest 时只读 `00_sources`，只写 `10_wiki`
- 优先更新旧页，必要时才新建页
- 所有改动过的 wiki 页面必须保留 `## 来源`
- 不允许改写原始 source
- 不允许 silent rename、silent merge、silent delete
- lint 只输出问题清单，不自动修
- 如果 source 证据不足，先停在 source 层并说明缺口，不要硬写 wiki

## Output Contract

执行时先说明：

1. 读了哪些规则文件
2. 当前执行的是 URL 入库还是 source 入库
3. 会写哪些目录，不会写哪些目录

执行后说明：

1. 创建或读取了哪些 source
2. 更新了哪些 wiki 页
3. 是否新建了 wiki 页，以及原因
4. scoped lint 查出了哪些问题
5. 是否还缺证据或需要补 source

## Examples

```text
/kb https://github.com/example/project
```

等价于：先把链接落成 source，再按 schema 做 ingest，最后对本轮改动做 scoped lint。

```text
/kb 2026-04-15-example-project-web
```

等价于：直接对已有 source 做 ingest，并在结束后做 scoped lint。
