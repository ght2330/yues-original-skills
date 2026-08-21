# Reference Analysis Rubric

Analyze evidence, not adjectives. Replace "premium", "clean", or "modern" with rules another agent can implement and verify.

## 1. Establish The Brief

Record:

- audience and primary task;
- page type and content volume;
- product constraints, framework, and component library;
- existing brand/design rules;
- target viewports and accessibility requirements;
- whether motion is necessary, optional, or unwanted.

## 2. Assign Reference Roles

Give each selected reference one main job:

- `visual`: composition, tone, typography, color, and imagery;
- `structure`: navigation, hierarchy, workflow, density, and states;
- `motion`: timing, triggers, transitions, and fallback behavior;
- `design-system`: tokens, component conventions, and implementation rules.

Do not average incompatible references. State which role wins each conflict.

## 3. Decompose Each Reference

| Dimension | Evidence to capture | Convert into |
|---|---|---|
| Purpose | What user or brand goal the page serves | project-specific design objective |
| Composition | grid, alignment, full-bleed areas, section rhythm | layout constraints and section order |
| Hierarchy | dominant content, reading order, density | heading scale, emphasis, and scan path |
| Typography | family category, sizes, weights, line length | type tokens and usage rules |
| Color | role of each color, contrast, state colors | semantic color tokens |
| Spacing | gutters, section gaps, component padding | spacing scale and container widths |
| Shape | radii, borders, shadows, separators | component surface rules |
| Components | repeated UI, controls, navigation | component inventory and states |
| Interaction | hover, focus, selection, loading, errors | explicit behavior and feedback |
| Motion | purpose, trigger, duration, easing | motion tokens and reduced-motion path |
| Assets | image/video/icon subject and treatment | asset brief, source, crop, and aspect ratio |
| Responsive | reflow, collapse, priority changes | desktop/mobile layout rules |
| Accessibility | contrast, keyboard, semantics, motion | non-waivable acceptance checks |

Respect evidence boundaries. A screenshot can support visible composition, hierarchy, approximate color relationships, and displayed states. It cannot prove exact fonts, CSS values, keyboard behavior, ARIA semantics, hidden states, or breakpoints that are not shown. Label every inference explicitly and verify implementation-level claims against code or a live page.

## 4. Separate Borrowing From Copying

Allowed:

- abstract grid and hierarchy patterns;
- semantic token relationships;
- interaction and feedback principles;
- motion purpose and timing patterns;
- content-density and responsive strategies.

Not allowed:

- trademarks, logos, or brand identifiers;
- proprietary copy or distinctive slogans;
- unlicensed photography, video, illustration, icons, or fonts;
- a near-identical page composition presented as original work.

## 5. Synthesize The Contract

For each accepted rule, write:

```text
Rule: what to implement
Source role: visual / structure / motion / design-system
Evidence: URL or screenshot path
Project adaptation: what changes for this brief
Acceptance: how to verify the result
```

Keep a short anti-goal list. It is often more useful than extra inspiration: no oversized marketing hero for an operational dashboard, no decorative motion without a task, no card nesting, no one-note palette, and no invented product state.

## 6. Resolve Existing-System Conflicts

Apply this order:

1. Safety, law, licensing, accessibility, and user hard requirements.
2. Existing project design system and component API.
3. Explicitly approved migration IDs that replace named existing rules.
4. Selected reference direction.

Show every migration as a diff. Do not treat general contract approval as permission to replace unnamed existing rules.
