# Illustration Contract

Use this reference when a slide needs a generated or native explanation image, complex evidence visual, chart redraw, reference-specific object, or scientific/cultural mechanism.

## Visual Anchor Contract

Classify the main anchor before choosing its production route:

- `illustration`: a recognizable subject or scene that makes a mechanism, contrast, or idea tangible;
- `chart`: quantitative marks whose values and relationships carry the claim;
- `diagram`: topology, sequence, hierarchy, or system relationships;
- `artifact`: a document, interface state, report, specimen, or other evidence-bearing object;
- `photo`: a real person, place, object, or event;
- `expressive-typography`: words or numbers are intentionally the main visual object.

Cards, rails, ledgers, status ladders, and dashboard panels are supporting geometry, not anchor types. An `illustration` anchor must declare:

- `recognizable_subject`: the concrete thing or scene a viewer should identify within three seconds;
- `subject_cues`: at least three structural cues, such as silhouette, parts, inputs/outputs, pose, tools, or spatial relationship;
- `illustration_job`: what the subject explains, proves, or makes memorable;
- `non_card_visual_area`: target bbox and approximate share of the content region occupied by the subject rather than UI chrome.

For a visually rich five-slide deck, use recognizable illustration subjects on at least two content slides. A deck-level exception is valid only when charts, artifacts, photos, or domain-faithful diagrams communicate the evidence more truthfully; name those substitute anchors and the reason.

## Cover Background Brief

A cover is not generated as a complete slide. Use `gpt-image-2` to create one text-free, `16:9`-safe background asset, then typeset the cover again in Penpot.

The brief must record:

- one concrete subject or scene tied to the deck thesis;
- rhetorical job and visual mood;
- normalized focal point and title-safe zone;
- crop tolerance for full-bleed `16:9` placement;
- palette relationship to the deck;
- negative constraints: no text, letters, logo, UI, chart, watermark, slide frame, or decorative card.

The accepted asset must keep its subject recognizable after crop. Place it full bleed, declare a native `cover_overlay`, and keep title/subtitle/metadata as native Penpot text. The overlay may be a uniform solid or a single-hue alpha gradient whose color stays constant while opacity changes; multi-hue decorative gradients are not part of this cover system. The overlay defaults to enabled; if disabled, record exported-preview and contrast evidence.

One available composition biases the subject to the right and keeps the left `50-58%` calm for typography. A theme-colored title mask may fade from high opacity on the left to low opacity on the right. An optional black lower mask may support tags, author/date, or pagination without darkening the subject more than necessary. Choose this only when it fits the new subject and brief.

This is one mechanism, not a reusable template. When a reference cover is supplied, extract only production and composition principles such as full-bleed image use, safe-zone ownership, mask behavior, and native-text layering. The new cover must use the current deck's own subject, copy, hierarchy, palette, and geometry. Do not copy names, tags, metadata, exact proportions, or the complete reference anatomy.

## Brief

Create one `illustration_brief` per asset:

```json
{
  "id": "slide-04-evidence-machine",
  "content_need": "explain how three source types become one decision visual",
  "visual_anchor_type": "illustration",
  "recognizable_subject": "evidence processing machine",
  "subject_cues": ["three input trays", "central processing chamber", "single decision output"],
  "illustration_job": "make source consolidation tangible and show where evidence changes form",
  "non_card_visual_area": {"bbox": [420, 260, 620, 350], "content_area_ratio": 0.36},
  "information_job": "show inputs, transformation, and outputs",
  "claim_supported": "the image is an argument carrier, not decoration",
  "evidence_payload": ["input types", "processing step", "output uses"],
  "visual_structure": "pipeline",
  "labels": ["文章笔记", "数据说明", "产品说明", "中心配图"],
  "reference_needed": false,
  "data_semantics": null,
  "negative_constraints": ["no stock photo", "no prompt leakage", "no long legend"],
  "target_bbox": [420, 260, 620, 350],
  "safe_margin": 32
}
```

## Structure Routing

- Cycle: repeated work, feedback, iteration.
- Pipeline: ordered transformation or routing.
- Hub-and-spoke: one coordinator and several branches.
- Before/after: state change or migration.
- Layer stack: architecture, hierarchy, dependency.
- Data-first scene: quantitative evidence with restrained contextual objects.
- Scientific mechanism: parts, forces, reactions, or biological process.
- Text scene: atmosphere that anchors a humanities idea without pretending to be evidence.

## Text Rules

- Keep in-image Chinese labels concrete and short: 2-5 characters is ideal; 6 is usually the upper limit.
- Put labels next to the object or flow they name.
- Keep explanatory sentences as native Penpot text outside the image.
- Avoid dense in-image legends.
- Do not remove labels merely because image generation may misspell them. Generate, inspect, and regenerate.

## Reference Rule

Research visually specific or unfamiliar concepts before prompting. Extract stable cues such as silhouette, parts, color conventions, scale, and topology. Use references to understand the subject, not to copy layout, watermarks, UI chrome, or visual noise.

## Chart Redraw Rule

Do not ask the image model to beautify a screenshot directly. Extract:

- chart type and intended conclusion;
- exact data values and units;
- axes, ranges, ticks, and category order;
- highlighted extremes/anomalies;
- error bars or uncertainty.

Redesign from those semantics. Reject an attractive chart if any number or visual mark is wrong.

## Asset QA

Before upload to Penpot, verify:

- the asset answers the slide's content need;
- the exported slide still reveals the declared `recognizable_subject` within three seconds;
- at least three declared `subject_cues` remain visible and attached to the subject;
- `non_card_visual_area` is large enough to establish a visual anchor rather than a decorative icon;
- labels are correct, readable, short, and attached to the right objects;
- data and reference cues are accurate;
- nothing important is cropped;
- no accidental logos, watermarks, extra English, prompt leakage, or copied UI appears;
- the asset remains understandable at its actual slide size;
- the style matches the deck's `theme-profile.json`.
- for a cover background, the raster contains no accidental text/logo/UI, preserves the title-safe zone, survives full-bleed crop, and remains behind a declared native overlay and editable text stack;

Regenerate failed assets. Do not hide broken labels or data with disconnected overlay text unless the deck intentionally uses external annotation and the image itself remains semantically correct.

The same checks apply to native-only illustration fallbacks. Editability, shape count, and a large bounding box do not prove illustration quality when the result reads as generic UI chrome.
