---
name: penpot-workflow
description: Use when a design task involves Penpot, self-hosted design assets, Penpot MCP, Design Tokens, or synchronizing structured design work with code.
---

# Penpot Workflow

## Core Positioning

Use Penpot as the preferred Agent-native design workflow when the user wants AI to read and modify real design structure instead of guessing from screenshots. This is an MCP/file-backed workflow: the source of truth must be a real Penpot file, its focused page, components, layers, styles, and Design Tokens.

Do not claim to have used this workflow if no Penpot MCP context or Penpot file was verified. Local HTML, React, screenshots, token JSON, and handoff notes are companion artifacts only after a Penpot file exists; they are not substitutes for the Penpot step.

Do not route Penpot work through `figma-workflow`. Use `figma-workflow` only when the user explicitly needs Figma files, Figma collaboration, a Figma link, or compatibility with an existing Figma-based team.

## Decision Boundary

Prefer this skill when:

- The user mentions Penpot, open-source design tools, self-hosted design, private design assets, Design Tokens, W3C DTCG, or Penpot MCP.
- The user wants Agent-readable UI design files rather than screenshot-based imitation.
- The user wants design-to-code, code-to-design, component cleanup, layer naming, token inspection, or design system maintenance through MCP.
- The project has privacy, compliance, local deployment, or vendor-lock-in concerns.

Prefer `figma-workflow` when:

- The user must deliver or consume a Figma file/link.
- Designers or collaborators already work in Figma.
- The task depends on Figma plugins, Figma templates, or a Figma-specific review flow.

## Execution Gate

Pass this gate before doing any design or code work under this skill.

1. Detect whether a Penpot MCP client/tool is available in the current environment.
2. If the user provided a Penpot file link or named an existing file, connect that file and run a read-only context check: file name, focused page, selected layers, components, libraries, and tokens.
3. If the user did not provide a file, create a new Penpot file/page for the task first. Use the available Penpot MCP, Penpot UI automation, or Penpot API path for creation. Name it from the task, for example `Personal Homepage - React Bits`.
4. If the current MCP/tool surface cannot create a file, tell the user the exact blocker and ask them to create/open a blank Penpot file and connect MCP. Stop before producing the final design. Do not silently fall back to a local page.
5. If MCP is not configured, complete one of the setup paths below. If credentials or user login are required, have the user configure them locally; never ask for keys in chat.
6. Only after a read-only MCP check succeeds may the agent modify Penpot content or produce code from the Penpot structure.

Required completion evidence:

- Penpot file name or link.
- Focused page name.
- Components/layers/tokens read or created through MCP.
- Summary of what changed in Penpot.
- Any generated code or local preview clearly marked as a companion output.

## Safety Rules

- Never ask the user to paste a Penpot MCP key, token, or session credential into chat.
- Treat the MCP key like an API key. If configuration is needed, tell the user to place it in the local MCP client config or use Penpot's own copy flow.
- Start with read-only prompts before applying changes to a design file.
- Remember that Penpot MCP acts on the currently focused Penpot page and only one active MCP browser tab. Confirm the intended file/page before destructive or broad edits.
- Do not use screenshots as the canonical source when MCP access is available. Screenshots are previews only.

## Setup Paths

### Local Codex Setup

If your environment provides a local Penpot MCP server, configure the MCP client with that environment's endpoint and keep its start/stop commands local. Do not commit machine-specific paths, credentials, or session URLs to a shared repository.

If a current Codex thread does not show Penpot MCP tools after setup, start a new thread or restart Codex so MCP tools are reloaded.

### Remote MCP

Use remote MCP for quick hosted Penpot workflows.

1. Open Penpot.
2. Enable MCP under `Your account -> Integrations -> MCP Server`.
3. Generate the MCP key from Penpot. Do not expose the key in chat.
4. Configure the MCP client with:

```text
https://<your-penpot-domain>/mcp/stream?userToken=YOUR_MCP_KEY
```

5. Open the target Penpot file and choose `File -> MCP Server -> Connect`.
6. Begin with read-only prompts such as:

```text
List pages in this file.
Show all components on this page.
Inspect tokens and summarize color, spacing, and typography usage.
```

### Local MCP

Use local MCP when the user wants more control or local resources.

1. Start the local MCP/plugin server:

```powershell
npx -y @penpot/mcp@stable
```

2. Keep that terminal running.
3. Open the Penpot plugin manifest if needed:

```text
http://localhost:4400/manifest.json
```

4. Configure the MCP client with HTTP transport:

```text
http://localhost:4401/mcp
```

5. Open the target Penpot file and choose `File -> MCP Server -> Connect`.

### Self-Hosted Penpot

Use self-hosting when the user wants private design assets or internal deployment.

Minimal official Docker path:

```powershell
curl -o docker-compose.yaml https://raw.githubusercontent.com/penpot/penpot/main/docker/images/docker-compose.yaml
docker compose -p penpot -f docker-compose.yaml up -d
```

Then open:

```text
http://localhost:9001
```

For production, verify DNS, HTTPS, reverse proxy, storage, backups, and Penpot upgrade process before treating the instance as durable.

## Agent Workflow

1. Pass the Execution Gate. If no Penpot file exists, create one before generating design output.
2. Identify intent: inspect, generate, refactor, sync to code, sync from code, or maintain design system.
3. Verify MCP context with read-only prompts: file name, focused page, selected layers, components, libraries, and tokens.
4. Summarize the current design structure before changing it.
5. For edits, describe intended changes first when the scope is broad or potentially destructive.
6. Apply changes through Penpot MCP where possible: create pages, create/update tokens, create components, organize layers, rename layers, inspect consistency, or map components to code.
7. For code output, generate implementation from structured Penpot data: components, tokens, layouts, layers, and styles. Do not rely on a screenshot alone.
8. Validate after changes: re-list affected pages/layers/tokens and compare against the request.
9. If a local preview is useful, create it only after the Penpot file has been created or verified. Label it as companion code, not the primary Penpot deliverable.

## Design Tokens Workflow

When tokens are relevant:

1. Inspect existing tokens before inventing new values.
2. Preserve token names, aliases, and semantic meaning.
3. Prefer W3C DTCG-compatible token structures for exported or code-facing artifacts.
4. Map design tokens to code variables deliberately, for example CSS variables, Tailwind theme tokens, or TypeScript token objects.
5. Report token gaps separately from visual implementation gaps.

## Prompt Patterns

Read-only context check:

```text
Read the active Penpot file. List pages, the focused page, components, token groups, and selected layers. Do not modify anything.
```

Design system cleanup:

```text
Inspect the focused page for inconsistent layer names, duplicated components, and token misuse. Summarize proposed changes before applying them.
```

Design-to-code:

```text
Read the focused Penpot page through MCP and generate a component implementation using the actual components, layers, layout rules, and Design Tokens. Do not infer from screenshots unless MCP data is missing.
```

Code-to-design:

```text
Create or update the focused Penpot page to match this UI structure. Use reusable components and tokens where possible, then report the created pages, layers, components, and tokens.
```

New-file start:

```text
Create a new Penpot file named "[task name]". Add a page named "Homepage", create the core color, spacing, and radius tokens, then build the first screen with named components and layers. Report the file name, focused page, created tokens, components, and top-level layers.
```

## Troubleshooting

- MCP tools show the wrong page: switch focus in Penpot to the intended page, then reconnect `File -> MCP Server -> Connect`.
- MCP cannot modify the file: confirm MCP is enabled, the plugin is connected, and the active MCP tab is the intended Penpot tab.
- No Penpot file is provided: create a new file first. If file creation is not available from the current tools, stop and ask the user to create/open a blank Penpot file and connect MCP.
- No Penpot MCP tools are available: do not proceed with a fake Penpot workflow. Complete MCP setup or state that the Penpot step is blocked.
- Remote MCP authentication fails: regenerate the MCP key in Penpot and update the local MCP client config. Do not paste the key into chat.
- Local MCP fails: restart `npx -y @penpot/mcp@stable`, reload the MCP client, and keep the plugin/server terminal open.
- Design-to-code looks generic: re-run a read-only inspection and require use of actual components, tokens, layers, and layout data.

## References

- Penpot MCP docs: `https://help.penpot.app/mcp/`
- Penpot Docker self-hosting: `https://help.penpot.app/technical-guide/getting-started/docker/`
- Penpot Design Tokens: `https://help.penpot.app/user-guide/design-systems/design-tokens/`
