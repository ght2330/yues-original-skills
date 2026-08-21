---
name: reference-driven-web-design
description: Use when a frontend task needs concrete website references analyzed, compared, approved, or translated into an explicit design contract before implementation.
---

# Reference-Driven Web Design

Turn vague visual language into explicit, approved design rules. Treat references as evidence to decompose, not pages to clone.

## Load References

- Read [references/source-catalog.md](references/source-catalog.md) when searching for candidates or choosing sources.
- Read [references/reference-analysis.md](references/reference-analysis.md) before analyzing or synthesizing references.
- Read [references/design-md-template.md](references/design-md-template.md) before drafting or updating `DESIGN.md`.

## Choose The Mode

- `research`: collect or analyze references and produce an approved `DESIGN.md`; stop before code implementation.
- `build`: complete the same reference and contract gates, then hand the approved contract to `frontend-design` for implementation and verification.

Infer the mode from the request. Ask only when the requested endpoint is unclear.

## Workflow

### 1. Inspect The Project

Confirm the project root before drafting. Read the brief, existing frontend conventions, component library, brand rules, and any existing `DESIGN.md`.

If an existing `DESIGN.md` is complete and the user confirms it still represents the desired direction, Build mode may reuse it. Otherwise prepare an incremental diff; never silently replace compatible rules.

### 2. Collect References

#### User-Provided References

Analyze supplied links or screenshots first. Give each source a traceable URL, absolute screenshot path, or user label. Search only dimensions the supplied set does not cover.

Two or three complementary references are normal. One reference is enough when the user explicitly makes it authoritative and confirms that it, together with the existing design system, covers visual direction, product structure, and design-system detail.

First mark the applicable roles from the brief: visual direction and product structure are normally required; design-system detail may come from the existing project; motion is required only when the brief calls for it. Mark non-applicable roles `N/A`. For every applicable but missing role, present two supplemental candidates and wait for selection.

#### Autonomous Search

When the user provides no references, return exactly six candidates:

- Expressive marketing, brand, or portfolio: `2 visual + 2 structure + 2 motion`.
- SaaS, dashboard, or operational tool: `2 visual + 3 structure + 1 design-system`.
- Restrained content or static site: `2 visual + 2 structure + 2 design-system`.

Give each candidate one primary slot. Do not repeat the same page, product, or case study.

Use these evidence levels:

- `A`: direct page plus visible evidence or screenshot; eligible.
- `B`: accessible text or metadata without visible evidence; context only.
- `C`: inaccessible or unverifiable; reject.

Try at most two replacements for a missing slot. If six level-A candidates remain unavailable, report the verified partial list as `blocked_insufficient_references`; do not pad it with guesses.

For each eligible candidate show:

```markdown
### Candidate N - Name
- Primary role: visual / structure / motion / design-system
- Source: direct URL
- Preview evidence: directly visible page evidence or screenshot
- Why it fits: brief-specific reason
- Borrow: concrete layout, hierarchy, token, or interaction rules
- Avoid: mismatch, access limit, performance cost, or overdesign risk
```

Stop after the shortlist. Do not select references on the user's behalf.

### 3. Confirm The Reference Set

Wait for explicit selection. Adding, removing, replacing, or changing the role of a reference invalidates this approval and any downstream contract approval.

Assign every selected reference one responsibility: visual direction, product structure, motion language, or design-system detail. Resolve conflicts by declaring priority rather than averaging incompatible styles.

Safety, legal, and accessibility requirements are non-negotiable. Approved migrations replace only the existing rules they name; all other existing design-system rules remain above reference preferences.

### 4. Draft The Design Contract

Use the template to draft `DESIGN.md` at the project root unless the user names another path. Mark irrelevant sections `N/A` with a reason rather than inventing requirements.

If `DESIGN.md` exists:

1. Record its SHA-256.
2. Present an incremental diff.
3. Wait for approval.
4. Recheck the hash before writing; if it changed, reread and regenerate the diff.

Also prepare `reference-research.md` in the Codex artifact area with search dimensions, queries, candidate evidence, access dates, rejections, and final selections. Keep the implementation contract concise by linking to this audit rather than copying the full search log into `DESIGN.md`.

### 5. Confirm And Write

Present the complete contract draft or diff. Wait for explicit approval before writing either `DESIGN.md` or the reference audit.

Every proposed existing-system migration needs an ID. Approval must accept or reject each migration ID; unresolved migrations keep the draft pending.

If writing fails, save the approved draft under `$CODEX_HOME/artifacts/reference-driven-web-design/` (or `~/.codex/artifacts/...`) and report the path. Do not begin implementation without a written approved contract.

### 6. Finish Research Or Build

- Research mode: report the `DESIGN.md` and reference-audit paths, then stop.
- Build mode: use `frontend-design` as the sole implementation and repair owner. Pass it the approved `DESIGN.md`; it must not restart research or redefine the direction.

For landing pages and portfolios, apply `design-taste-frontend` only as an optional pre-contract checklist. It must not implement code or override an approved contract.

### 7. Verify Build Mode

Verify the rendered result at project-defined viewports, defaulting to `1440x900` and `390x844`:

- capture screenshots and compare every applicable contract item;
- require zero uncaught console errors;
- check horizontal overflow and incoherent text/control overlap;
- verify keyboard access for interactive controls;
- verify WCAG AA contrast;
- verify `prefers-reduced-motion` when motion exists.

Return structured failures to `frontend-design` for at most two repair-and-full-reverify rounds. Do not claim completion while console, accessibility, overflow, or reduced-motion failures remain.

## Hard Gates

- No autonomous search result may skip user reference selection.
- No `DESIGN.md` write may occur before contract approval.
- No Build implementation may occur before an approved `DESIGN.md` exists.
- No inaccessible source may be described as visually inspected.
- No reference justifies copying trademarks, logos, proprietary copy, or unlicensed media.
- No marketing hero or decorative WebGL should be imposed on an operational product without brief-specific justification and explicit approval.

## Failure Rules

- Search unavailable: ask for user links or screenshots and stop.
- Project root unclear: ask for the root before drafting.
- Existing contract unreadable or changed during approval: stop and regenerate from current content.
- `frontend-design`, build, browser, or verification tools unavailable: report the blocker and the exact resume point.
- Heavy WebGL, canvas, 3D, or full-viewport motion: require explicit approval and a measurable performance budget before implementation.
