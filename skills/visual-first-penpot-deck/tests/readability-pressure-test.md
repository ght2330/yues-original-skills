# Readability Pressure Test

Use this regression test when changing content planning, semantic grammar, comp prompting, reconstruction, or visual QA rules.

## Scenario

Under time pressure, design one information-rich dark-editorial slide explaining this chain:

- Direct prompt-to-Penpot work loses visual intent.
- Comp analysis produces design rules and a scene graph.
- Design rules control color, type, spacing, and components.
- The scene graph controls position, depth, regions, and illustration.
- Both reduce reconstruction drift.

Ask for title, visible copy, information structure, visual elements, and layout specifications.

## RED Baseline

Without the reading-unit rules, the response repeated the same idea across an error path, a correct path, two modules, a merge statement, and many English micro-labels. The subtitle contained a complete explanation, but most of the page became isolated labels and equal-weight visual objects. The viewer still had to reconstruct the argument.

## PASS Criteria

- A `complete_expression` states the full relationship before layout planning.
- `canonical_visible_copy` remains understandable when extracted in `reading_order`.
- Cause, contrast, sequence, qualification, evidence, and outcome are explicit.
- Labels name real categories, states, steps, objects, sources, or metadata.
- Responsibilities are not reduced to isolated labels without explanatory sentences.
- The layout follows the reading unit; it does not create one card per phrase.
- The response does not force a conclusion headline plus three cards when another reading form is clearer.

## GREEN Observation

With the updated skill, the response first wrote the complete causal expression, preserved responsibility sentences for design rules and the scene graph, recorded fragmentation risks, and used a continuous failure-path/translation-path composition. Short terms remained only as valid category labels inside the two responsibility groups.
