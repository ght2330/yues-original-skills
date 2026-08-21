# Semantic Visual Grammar

Use this reference to choose a visual structure before drawing. It is informed by semantic component atlases that separate content, comparison, flow, relationship, and data grammars. Start from the slide's completed reading unit; visual grammar organizes meaning but must not replace the words that express the relationship.

## Route By Meaning

The route is selected after `slide-content-script.json` passes the plain-text and relationship tests. A component archetype is optional, but a dominant composition is not optional for ordinary content slides. Editorial prose, an image-caption pair, or a chart with a concise interpretation can be the right structure without becoming a diagram, yet it still needs spatial tension, a memorable focal idea, support, and deliberate depth.

### Content And Layout

Use for title-led pages, quotes, lists, code, tables, key statements, and two/three-column editorial compositions.

### Comparison And Evaluation

Use for before/after, pros/cons, side-by-side alternatives, SWOT, quadrant, matrix, scorecard, Venn, tradeoff triangle, or decision criteria.

### Flow And Time

Use for process chains, cycles, feedback loops, timelines, roadmaps, stages, handoffs, funnels, or branching paths.

### Structure And Relationship

Use for concentric layers, hierarchy, pyramid, architecture stack, hub-and-spoke, fishbone, iceberg, system map, dependency network, or nested ownership.

### Data And Charts

Use for exact quantitative comparison, trend, composition, distribution, schedule, heatmap, Sankey, benchmark, uncertainty, or anomaly evidence.

## Component Selection Contract

Each slide in `semantic-visual-plan.json` should include:

```json
{
  "slide": "04",
  "content_function": "compare two strategies and expose the tradeoff",
  "reading_form": "comparison",
  "complete_expression": "Strategy A is faster to produce, but Strategy B preserves editability and reduces later rework.",
  "semantic_relationships": ["contrast", "tradeoff", "reason for choice"],
  "expression_spine": "one readable comparison sentence",
  "dominant_visual": "large tradeoff field with one decisive intersection",
  "visual_anchor_type": "diagram",
  "recognizable_subject": null,
  "subject_cues": [],
  "illustration_job": "make the two-dimensional tradeoff and selected intersection memorable",
  "non_card_visual_area": {"content_area_ratio": 0.46},
  "supporting_regions": ["evidence artifact", "decision annotation"],
  "depth_strategy": "muted context in background, tradeoff field in midground, decision annotation in foreground",
  "richness_floor": "axes, evidence positions, decision intersection, annotation route",
  "grammar_family": "comparison-evaluation",
  "component_archetype": "quadrant",
  "component_variant": "labeled axes with center decision",
  "mutation_needed": ["add evidence chips", "reserve image crop"],
  "why_this_grammar": "the decision depends on two independent dimensions",
  "rejected_alternatives": ["two equal cards", "timeline"]
}
```

`component_archetype` may be `null` when a prose, image-caption, quote, or chart-led composition is clearer. `dominant_visual`, `visual_anchor_type`, `illustration_job`, `non_card_visual_area`, `supporting_regions`, `depth_strategy`, and `richness_floor` remain required unless a valid sparse exception is recorded. `recognizable_subject` and at least three `subject_cues` are additionally required when `visual_anchor_type` is `illustration`.

## Meaning-First, Template-Aware Rule

- Start from the closest proven grammar or deck/page archetype.
- Preserve `complete_expression`, `semantic_relationships`, and reading order before optimizing visual variety.
- Build the composition around the expression spine; do not mistake the spine for the entire page.
- Change labels, hierarchy, colors, count, geometry, and layout in the deck-specific instance.
- If no exact match exists, use the nearest component as a structural reference, then build the required mutation.
- Do not force content into the first match.
- Do not write deck-specific mutations back into a global catalog.
- Do not use a generic grid merely because it is easy to code.
- Do not promote cards, rails, ledgers, status ladders, or dashboard frames into the visual anchor. They can organize evidence around an illustration, chart, diagram, artifact, photo, or expressive-type anchor.
- On a visually rich five-slide deck, plan recognizable illustration subjects for at least two content slides unless a deck-level exception names more truthful substitute anchors.
- Do not create one visual object per phrase. Split text only when the parts are genuinely independent categories, states, steps, or evidence units.
- Do not force every slide into a conclusion headline plus three supporting cards.
- Do not finish ordinary content slides as title + paragraph + one rectangular image.
- Enrich with evidence, artifacts, annotations, contextual visuals, scale contrast, routes, and depth that clarify or substantiate the expression rather than fragment it.

## Penpot Translation

Translate a selected grammar into native Penpot components when quality permits. Use SVG/figedit/generated assets for curves or complex visuals that Penpot primitives cannot reproduce faithfully. The fallback must preserve meaning, topology, focal hierarchy, visual-anchor type, recognizable subject, subject cues, and non-card visual area, not only the number of boxes.

Shared chrome and semantic grammar are separate concerns: title/footer/page-number consistency should not make every content region use the same skeleton. The translation also preserves reading continuity: text regions that belong to one thought stay visually and semantically connected.
