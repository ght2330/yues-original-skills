# DESIGN.md Template

Use this structure for both new files and incremental updates. Replace guidance text with project evidence. Write `N/A - <reason>` where a section truly does not apply.

```markdown
# Design Contract - <Project Name>

## 1. Project Intent

- Audience:
- Page/product type:
- Primary tasks:
- Success signal:
- Target viewports:
- Existing framework/component library:

## 2. Selected References

| Reference | Source/evidence | Primary role | Project adaptation |
|---|---|---|---|
| <name> | <URL or screenshot path> | visual/structure/motion/design-system | <rule> |

- Reference audit: <absolute path to reference-research.md>

## 3. Visual Direction And Anti-Goals

### Direction

- <implementable visual rule>

### Anti-Goals

- <specific style or behavior to avoid>

## 4. Design Tokens

### Color

| Token | Value | Role | Contrast requirement |
|---|---|---|---|

### Typography

| Token | Family | Size/line height | Weight | Usage |
|---|---|---|---|---|

### Spacing, Radius, Border, Shadow

- Spacing scale:
- Container/gutters:
- Radius:
- Border:
- Shadow:

## 5. Page Structure And Responsive Rules

- Section/order map:
- Grid/container rules:
- Desktop behavior:
- Mobile behavior:
- Content density:
- Horizontal-overflow whitelist, if any:

## 6. Components And States

| Component | Default | Hover/focus | Loading | Empty | Error | Disabled |
|---|---|---|---|---|---|---|

- Mark inapplicable states `N/A` with a reason.
- Critical components/regions for overlap checks:
- Implementation selectors/test IDs: <may be added during implementation before verification>
- Approved overlay relationships:

## 7. Motion

- Purpose:
- Trigger:
- Duration/easing:
- Reduced-motion behavior:
- Heavy-motion approval ID and performance budget, or `N/A`:

## 8. Asset Requirements

| Asset | Subject/content | Format/aspect | Source/license | Responsive treatment |
|---|---|---|---|---|

## 9. Accessibility And Mobile Constraints

- Keyboard order and focus visibility:
- Contrast target:
- Semantic/ARIA requirements:
- Touch targets:
- Text fitting/overflow:
- Reduced motion:

## 10. Acceptance Checks

- [ ] Applicable reference roles are reflected without copying brand identity.
- [ ] Desktop and mobile screenshots match the approved hierarchy.
- [ ] No uncaught console errors.
- [ ] No unintended horizontal overflow or critical-control overlap.
- [ ] Interactive controls are keyboard reachable.
- [ ] WCAG AA contrast passes.
- [ ] Reduced-motion behavior works when motion exists.
- [ ] Every applicable component state is present.

## 11. Existing-System Migrations

| ID | Existing rule | Proposed replacement | Reason | Approval |
|---|---|---|---|---|
| MIG-001 | <rule> | <replacement> | <reason> | pending/approved/rejected |

Use `None` when no migration is required. Every migration ID needs explicit approval.

## 12. Intellectual Property And Asset Rules

- Do not reuse trademarks, logos, proprietary copy, or distinctive brand identifiers.
- Use only user-provided, generated, public-domain, or properly licensed assets.
- Record source and license for every external asset.
- Borrow abstract layout, hierarchy, token, and interaction principles only.
```
