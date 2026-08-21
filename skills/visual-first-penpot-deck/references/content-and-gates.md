# Content And Delivery Gates

Use this reference before comp generation and again before delivery. The purpose is to prevent a visually polished deck from carrying weak, unsupported, or poorly routed content.

## Evidence Table

Create `source-evidence-table.json` with one entry per important fact, number, claim, or uncertainty:

```json
{
  "id": "E-07",
  "type": "fact | number | judgment | uncertainty",
  "content": "...",
  "source": "file/page/section/url",
  "confidence": "high | medium | low",
  "allowed_slide_uses": ["03", "05"],
  "gap_action": "use | qualify | research | omit"
}
```

Do not invent evidence to fill a visual slot. Mark gaps or omit the unsupported claim.

## Storyline Checkpoint

Generate at least two storyline options before locking the outline. For each option record:

- audience and decision to influence;
- opening tension;
- sequence of claims;
- evidence coverage;
- page count and rhythm;
- strengths, risks, and why it was selected or rejected.

SCR (Situation, Complication, Resolution) is a useful default for analytical decks, but it is not mandatory for narrative, teaching, or personal-expression decks.

## Slide Reading Unit

Before visual planning, write each slide as a complete reading unit in `slide-content-script.json`. The purpose is not to force one headline conclusion. It is to preserve enough language and structure that the viewer does not have to reconstruct the author's sentence from disconnected fragments.

A valid reading unit can be:

- a short paragraph that makes one continuous explanation;
- a comparison with an explicit axis and a stated difference;
- a process whose transitions and outcome are clear;
- an image-caption pair in which the caption explains why the image matters;
- a chart plus an interpretation that states what should be learned from it;
- a sparse quote, cover, section divider, or emotional beat used intentionally.

Labels are valid only when they name a real category, state, step, object, source, or piece of metadata. Do not convert ordinary prose into labels merely to create more visual objects.

Run two tests:

1. Plain-text test: extract visible copy in reading order and read it without layout. It should still be understandable.
2. Relationship test: cause, contrast, sequence, qualification, evidence, and conclusion must be stated in words or made unambiguous by the visual structure.

Fail the slide if it contains many individually understandable phrases but no complete expression of how they relate.

## Two Independent Quality Axes

Readability and compositional richness are evaluated separately.

**Semantic coherence:** visible copy and visual relationships form a complete expression without requiring the viewer to reconstruct missing logic.

**Compositional richness:** the page has a deliberate dominant visual, supporting evidence or contextual detail, scale contrast, depth, visual routes, and enough internal structure to preserve its intended visual memory.

A slide can pass one axis and fail the other. Do not simplify a visually rich comp merely because the copy is now coherent. Do not hide fragmented copy inside a complex composition. Both axes must pass.

Ordinary content slides require a `composition-richness-contract.json` entry. Covers, section dividers, quotes, emotional beats, or intentionally restrained editorial pages may be sparse only when `sparse_exception_reason` states the rhetorical purpose.

## Density Targets

Set one target per slide: `low`, `medium`, `high`, or a concrete element/value count. Density must reflect the slide's job.

- Low density is valid for a thesis, quote, emotional beat, or section divider.
- High density is valid for evidence, comparison, architecture, and decision slides.
- Never add filler to satisfy density.
- Never solve overflow by shrinking the title/body below the deck hierarchy.
- Never lower density automatically to satisfy readability. Reorganize the expression spine while preserving evidence, visual memory, depth, and useful supporting detail.

## Presentation-Distance Typography

Typography is checked by semantic role, not by the smallest number that happens to fit. For a `1440x810` slide:

| Text role | Default | Hard floor |
| --- | ---: | ---: |
| Main explanatory body | `24px` | `22px` |
| Supporting copy | `20px` | `20px` |
| Meaningful label, stage, axis, category, or status | `16px` | `16px` |
| Caption, source, footer, or page metadata | `14px` | `14px` |
| Explicitly nonessential metadata | `12px` | `12px` with exception |

Scale the system proportionally for another canvas size. Every native text node must record `text_role`, `font_size_px`, `role_floor_px`, and any `small_text_exception`.

`12px` text cannot carry a claim, step, category, status, relationship, required source, or any copy the audience must read to understand the slide. When text does not fit at its role floor, rewrite, regroup, recompose, or split the slide. Overflow, high density, and schedule pressure are never reasons to shrink below the floor.

## Visual Anchor Classification

Every non-sparse slide must classify its main anchor as `illustration`, `chart`, `diagram`, `artifact`, `photo`, or `expressive-typography`, and record `illustration_job` plus `non_card_visual_area`. Card grids, rails, ledgers, status ladders, and dashboard panels may support an anchor but are not anchor types.

An illustration anchor also requires a concrete `recognizable_subject` and at least three `subject_cues` that remain visible in the exported preview. For a visually rich five-slide deck, at least two content slides require recognizable subjects unless a deck-level exception identifies stronger chart, artifact, photo, or domain-faithful diagram anchors and explains why illustration would be less truthful.

## Fixed Cover Route

When a cover exists, verify this exact composition chain:

```text
gpt-image-2 text-free background -> full-bleed Penpot image fill -> declared native single-hue mask -> native editable cover text
```

The background must preserve one relevant subject and a calm title-safe zone; it cannot contain title, subtitle, logo, UI, chart, watermark, or slide framing. `cover_overlay` is always declared and defaults to enabled. It may use a uniform solid or single-hue alpha gradient, but not a multi-hue decorative gradient; a disabled overlay requires recorded preview and contrast evidence. Derive the safe-zone direction from the new subject; right-subject/left-title is only one option. On `1440x810`, cover title, subtitle, and meaningful metadata use at least `56px`, `24px`, and `16px` respectively. The final composite targets at least `4.5:1` title/subtitle contrast without putting the title inside a card.

If a reference cover is supplied, run a reference-boundary check: the result may reuse the production mechanism but must not copy the reference's topic, wording, names, tags, image subject, palette, exact geometry, or full information hierarchy. Record the selected new composition and why it belongs to the current deck.

## Three Checkpoints

1. Content checkpoint: evidence table, storylines, page count, and claims.
2. Blueprint checkpoint: theme profile, shared chrome, semantic visual plan, illustration briefs, and comps.
3. Delivery checkpoint: exported previews, fidelity audit, editable source, and PDF.

The agent may self-approve checkpoints for smoke tests and low-risk personal decks, but must record the decision. Use explicit user confirmation for high-stakes or source-heavy decks.

## Seventeen Gates

Record each gate as `pass`, `fail`, `not-applicable`, or `pass-with-caveat`, with evidence.

1. Source Gate: all source files/links were read and preserved.
2. Evidence Gate: claims and numbers trace to sources; gaps are visible.
3. Storyline Gate: at least two routes were compared before selection.
4. Reading Unit Gate: visible copy remains a coherent expression in plain-text reading order; relationships are not replaced by decorative fragments.
5. Composition And Density Gate: each slide's density matches its rhetorical job; its dominant visual, allowed `visual_anchor_type`, meaningful `non_card_visual_area`, support regions, depth, and richness floor survive reconstruction.
6. Theme Gate: one tokenized visual system is locked before page production; when a cover exists, its fixed background, safe-zone, solid-overlay, and native-text system is explicit.
7. Chrome Gate: title, page number, footer, progress, and repeated slots are consistent.
8. Semantic Grammar Gate: each slide has an intentional reading form; a component archetype is used only when it clarifies meaning.
9. Illustration Evidence Gate: every image or native illustration adds information, evidence, explanation, or controlled atmosphere; illustration anchors have a recognizable subject and at least three surviving subject cues; deck-level subject coverage or its exception is explicit; a cover background is text-free, relevant, full bleed, and crop-safe.
10. Reference Accuracy Gate: unfamiliar entities/objects are researched and stylized without copying noise or watermarks.
11. Data Fidelity Gate: chart type, axes, values, units, order, and uncertainty are exact.
12. Editable Layer Gate: titles, body, key numbers, chart labels, conclusion bars, footers, and all canonical cover copy remain native/editable.
13. Geometry Gate: curves, loops, Venns, Sankey-like paths, and complex shapes are not downgraded to crude boxes.
14. Overflow Gate: no clipped, overlapping, off-board, or unreadable content.
15. Typography Gate: hierarchy is consistent; every native text node meets its role-aware presentation-distance floor; all `12px` uses are explicitly nonessential and documented; font shrinking is not used as a hiding strategy.
16. Comp Fidelity Gate: lost visual memory and justified deviations are recorded per slide; cover background, overlay state, title-safe zone, native text, crop, and final contrast are checked against the cover contract.
17. Delivery Gate: Penpot source, previews, QA report, and PDF status are explicit.

Any failed required gate blocks completion.
