# Composition Richness Pressure Test

Use this regression test whenever readability, semantic grammar, density, scene-graph, or Penpot reconstruction rules change.

## Scenario

Create a five-slide deck whose copy is already readable and coherent. The topic is conceptual rather than data-heavy. The user wants the second stable visual quality: strong editorial composition, centerpieces, depth, evidence-bearing illustrations, and editable Penpot output.

The pressure is to interpret readability as fewer visual regions and faster native-shape reconstruction.

## RED Baseline

The 2026-07-18 readable-deck smoke passed the reading-unit checks but overcorrected composition:

- Slide 01 became title + paragraph + one illustration.
- Slide 02 became one comparison split with minimal supporting structure.
- Slide 03 became three simple paper cards on a line.
- Slide 05 became three question rows + one illustration.
- Only slide 04 retained a strong centerpiece, internal detail, two systems, and a meaningful merge.

The failure was not unreadability. It was the absence of a compositional richness floor when `component_archetype` was optional.

## PASS Criteria

- Every slide declares one `expression_spine`: the coherent path that remains readable.
- Every non-sparse slide also declares one `dominant_visual`: the visual memory the audience should retain.
- Supporting evidence, annotations, artifacts, or contextual visuals enrich the dominant visual without becoming equal-weight fragments.
- The scene graph distinguishes foreground, midground, and background or records an intentional depth alternative.
- `component_archetype: null` does not mean `dominant_composition: null`.
- A content slide cannot finish as only title + paragraph + single image unless `sparse_exception_reason` explains why that restraint is rhetorically necessary.
- Comp-to-Penpot reconstruction preserves internal structure, depth, visual routes, and supporting evidence, not only the count of major boxes.
- Visual complexity comes from relationships, evidence, scale contrast, layering, and illustration detail, not from splitting prose into chips.
- Readability and composition are evaluated independently; passing one cannot compensate for failing the other.

## Failure Signals

- Large unused regions with no rhetorical purpose.
- One paragraph and one rectangular image filling an ordinary content slide.
- A rich comp translated into flat text blocks and simple outlines.
- Repeated two-column or three-card skeletons despite different slide roles.
- Removal of evidence-bearing details under the excuse of readability.

## GREEN Observation

With the composition rebalance rules, the same conceptual slide retained one complete sentence as its expression spine while proposing:

- a large relationship lens with internal tracks and focal detail;
- one continuous route through the expression, relationship, and carrier stages;
- four unequal carrier specimens with different internal grammars;
- three process artifacts as evidence of the working method;
- explicit foreground, midground, and background layers;
- a `richness_floor` that blocks Penpot from simplifying these into plain cards.

The response explicitly rejected three-step cards, generic left-text/right-image composition, and four equal label blocks. Readability remained intact without lowering compositional ambition.
