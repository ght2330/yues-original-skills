---
name: visual-first-penpot-deck
description: Use when creating AI-made presentation decks without relying on WPS, Office, or PowerPoint as the production environment, especially when the source of truth should be an editable Penpot design and the primary delivery format is PDF.
---

# Visual First Penpot Deck

## Overview

Create presentation decks as editable Penpot design files first, then export stable PDFs for delivery. Treat PPTX as an optional compatibility adapter, not the main source format.

This skill's restored default is the **VFDeck6 / v2 stable path**, strengthened with evidence planning, semantic visual routing, and explicit delivery gates:

```text
profile/capabilities -> brief -> evidence/storyline -> plain-language slide scripts -> theme + semantic blueprint -> expected-result comps or approved native route -> temporary deck DESIGN.md -> slide contracts -> comp-to-Penpot scene graph -> fidelity reconstruction -> 17-gate visual audit -> bounded delivery status
```

The first raster image pass is used to establish visual ambition and slide roles. The Penpot build is not a pixel-chasing remake and not an image-only deck. It should look like the second stable version: strong dark editorial system, large readable type, cyan accents, native Penpot shapes, clear process cards, and restrained visual density. Visual polish must not break complete thoughts into isolated labels, chips, and card fragments.

Readability and compositional richness are independent quality axes, and each has a concrete failure mode: content can be coherent but too small at presentation distance, while a composition can be busy but lack a recognizable visual anchor. A slide can preserve complete sentences and still use a strong centerpiece, evidence-bearing illustration, layered depth, supporting artifacts, scale contrast, visual routes, and dense internal detail. Never use the readability rules as permission to flatten a rich comp into title + paragraph + one simple image, and never let cards, rails, or layer count stand in for an illustration.

Before any Penpot reconstruction, the agent must use visual understanding on the generated comps to write a temporary, deck-specific `DESIGN.md`. This file is the design-system translation layer between raster ambition and editable Penpot execution.

`deck-design.md` is not enough by itself. The agent must also write a concrete `comp-to-penpot-scene-graph.json` that turns each comp into executable geometry, layer depth, component recipes, illustration placement, and fidelity checks. Otherwise the Penpot build will collapse into flat rectangles and lose the comp's visual quality.

Local generated assets are optional and quality-gated on content slides. The cover is the explicit exception: when a deck has a cover, use the fixed cover route `gpt-image-2 background -> Penpot image fill -> native single-hue mask -> native editable text`. If a generated illustration, dashboard, or screenshot-like asset makes a content slide worse, use native Penpot geometry instead.

## When To Use

Use this skill when the user wants:

- AI-made PPT/deck/presentation without WPS, Office, or PowerPoint.
- A visually strong presentation with editable source layers.
- Penpot as the design source of truth.
- PDF as the primary delivery format.
- A workflow combining `GordenImagePPTGen`, `image-to-code` discipline, and `penpot-workflow`.

Do not use this as the main path when:

- The user explicitly requires a native editable `.pptx` as the primary deliverable.
- The team cannot open or edit Penpot.
- The task is a simple text-only outline or speaker notes request.

If `.pptx` is mandatory, treat it as a compatibility export after the Penpot deck exists. Do not make image-only PPTX the main output.

## Required Skill Order

Use the minimal applicable set in this order:

1. Read `references/production-contract.md`, select `fast | standard | premium`, write `capability-report.json`, and initialize `deck-run-manifest.json` before artifact planning.
2. Use `GordenImagePPTGen` through A1-A4 only when the selected profile and capability report require or allow visual comps: outline, per-slide prompts, real raster visual comps, and `imagegen-manifest.json`.
   - In this Codex environment, the raster backend is normally `image-studio-generation` / local `image-studio` / `gpt-image-2`.
   - Stop before `GordenImagePPTGen` A5 unless the user explicitly asks for a compatibility image PPTX.
   - This optional comp route does not control the cover. When a cover exists, run the fixed `gpt-image-2` background route in step 2A even when content slides use native-only reconstruction.
3. Before comp generation, build the evidence/storyline and a plain-language reading unit for every slide as described in `references/content-and-gates.md`.
4. Only after the reading units work as text, build the semantic visual blueprint and `composition-richness-contract.json` from `references/semantic-visual-grammar.md`.
5. Use visual capability on real comps to create a temporary deck `DESIGN.md`. For an approved native-only route, derive it from the locked theme, semantic plan, composition contracts, and explicit visual references; do not invent comp-fidelity evidence.
6. Use `image-to-code` discipline for visual analysis when comps or reference images exist: identify role, hierarchy, major regions, typography mood, reusable visual tokens, and slide-specific reconstruction constraints.
7. Use `penpot-workflow` to create the real editable deck in Penpot.
8. Use `ui-state-auditor`-style visual geometry checks and the 17 delivery gates after export previews, then apply the delivery status cap.

Optional support:

- Use `image-studio-generation` during reconstruction only for high-quality assets that pass the asset quality gate below.
- Read `references/illustration-contract.md` whenever a slide needs a generated or native explanatory illustration, reference-informed object, or data/chart redraw.
- Use `design-taste-frontend` as a taste QA gate for density, repetition, hierarchy, and AI-slop.
- Use `figedit` only for chart/figure regions that need semantic vector recovery.
- Use `GordenImage2PPTX` only as a fallback or compatibility adapter, not as the main route.

## V2 Stable Visual System

Default to the visual direction that produced the second stable version (`VFDeck6`):

- Canvas: 16:9, preferably `1440x810` in Penpot.
- Background: deep near-black / ink surface, not beige, not purple-blue gradient.
- Accent: electric cyan/teal as the primary signal; secondary accents are muted green, red, amber.
- Typography: very large bold display titles, complete and readable supporting copy, high contrast, and role-specific presentation-distance floors. Brevity is useful only after causal, comparative, temporal, or explanatory relationships remain explicit.
- Title system: all non-cover slides must share one recognizable title grammar. Keep the title anchor, progress/meta label, underline/rail behavior, and subtitle placement consistent across the deck. Slides may vary content layout, but not randomly change how a page starts.
- Structure: open editorial layout with a recognizable visual anchor, strong native shapes, supporting rails/cards/panels, decision blocks, evidence, and deliberate foreground/midground/background depth. UI-like structures may organize the page but cannot be the only visual subject.
- Density: information-rich but not cluttered. Readability may reorganize density but must not automatically lower it. Avoid generated dashboard noise and blurry raster UI panels.
- Imagery: the cover uses one full-bleed `gpt-image-2` background with native secondary typography; content slides remain mostly native Penpot vector/shape systems. Other raster images are rare and must be crisp, relevant, and visually better than native reconstruction.
- Template discipline: choose a proven page archetype and semantic component grammar before drawing. Mutate the closest fit; do not improvise every diagram from rectangles.

Good five/six page chains:

- `cover-method`: thesis and visual path.
- `failure-mode`: why image-only PPT and generic wireframes both fail.
- `pipeline`: brief -> comp -> scene graph -> Penpot -> audit -> PDF.
- `evidence` or `scene-graph`: proof artifacts, manifests, constraints, and layer mapping.
- `penpot-source`: editable design source, layer stack, native text, components.
- `delivery`: PDF handoff, PPTX compatibility policy, next-step checklist.

For a five-page deck, merge `evidence` into `pipeline` or `delivery`. Do not compress all roles into identical left-text/right-image pages.

## Non-Negotiable Principles

- Do not use WPS, Office, or PowerPoint as the production environment.
- Keep Penpot as the editable source file.
- Export PDF as the main delivery artifact.
- Keep canonical slide text native in Penpot. Raster comp text is not canonical.
- Treat raster comps as visual direction and ambition, not as a strict OCR source or a mandatory pixel-perfect target.
- Do not make image-only PPTX the main output.
- Do not force local generated images into every page.
- Do not generate visual comps before facts, claims, evidence gaps, and storyline alternatives are explicit.
- Do not enter visual planning before every slide works as one coherent reading unit in plain text.
- Do not turn clauses into separate cards, chips, badges, or floating labels merely to make a slide look designed.
- Do not force every slide into a conclusion headline plus three supporting points. A coherent paragraph, comparison, process, image-caption pair, or evidence explanation can each be the page's primary reading form.
- Do not equate complete expression with sparse composition. Keep the expression spine coherent while restoring centerpieces, evidence, annotations, artifacts, depth, routes, and internal visual detail.
- Do not finish an ordinary content slide as only title + paragraph + one rectangular image. This is valid only for an intentional sparse beat with a recorded `sparse_exception_reason`.
- Do not let readability pass compensate for a composition failure, or composition pass compensate for unreadable text. Both axes must pass independently.
- Do not draw semantic diagrams from scratch when an existing grammar such as comparison, quadrant, cycle, timeline, architecture, concentric layers, or data chart already fits.
- Do not let generated assets lower the deck's taste. A poor image-fill is worse than a clean native Penpot system.
- Do not collapse every slide into the same anatomy. Shared visual system is good; repeated slide skeleton is not.
- Do not claim Penpot work unless a real Penpot MCP/file context has been verified.
- Do not plan artifacts before selecting a production profile and recording actual capabilities.
- Do not infer a capability from its mention in this skill. Require observed evidence in `capability-report.json`.
- Do not use free-form completion language. Use only the bounded delivery statuses from `references/production-contract.md`.
- Do not claim a status above `deck-run-manifest.json.status_cap`.
- Do not silently change an object's planned delivery route or editability. Record actual route, reason codes, fallback, and QA evidence in the existing scene graph and run manifest.
- Do not silently downgrade generated illustration assets into primitive native shapes. If media upload fails, re-plan the slide and prove the fallback is visually comparable, or block completion.
- Do not treat board count, layer count, or containment checks as visual QA. They are structural checks only.
- Do not shrink explanatory body copy, supporting copy, or meaningful labels below their presentation-distance role floors to satisfy density or avoid recomposition.
- Do not classify card grids, rails, ledgers, status ladders, or dashboard frames as illustrations. They are support structures unless they depict a concrete subject with at least three recognizable cues.
- Do not ask `gpt-image-2` to render the final cover title, subtitle, logo, author, date, chart, UI, or complete slide. It generates the text-free visual background only.
- Do not silently replace a required cover background with native boxes, gradients, rails, or a dashboard cover. A cover-specific image-generation or upload failure blocks the fixed route unless the user explicitly approves a different cover route.

## Canonical Artifacts

Create or maintain these artifacts conceptually, even when some are embedded in the Penpot file:

```text
deck-brief.json
capability-report.json
deck-run-manifest.json
source-evidence-table.json
storyline-options.json
slide-content-script.json
composition-richness-contract.json
outline.json
theme-profile.json
semantic-visual-plan.json
prompts/NN-*.md
imagegen-manifest.json
cover-background-brief.json
visual-comp-manifest.json
layout-contracts.json
comp-reconstruction-plan.json
slide-scene-graph.json
asset-plan.json
asset-manifest.json
illustration-briefs.json
deck-design.md
comp-visual-analysis.json
comp-to-penpot-scene-graph.json
fidelity-audit-report.md
penpot-build-report.json
qa-report.md
visual-audit-report.md
quality-gates-report.json
speaker-notes.md
export-previews/NN.png
deck.pdf
```

`capability-report.json` and `deck-run-manifest.json` are required for every run. The selected profile controls which other artifacts are required; follow `references/production-contract.md` without weakening evidence, reading, composition, accessibility, or delivery promises. For `standard` and `premium`, `source-evidence-table.json`, `storyline-options.json`, `slide-content-script.json`, `composition-richness-contract.json`, `semantic-visual-plan.json`, `deck-design.md`, and `comp-to-penpot-scene-graph.json` are required before Penpot reconstruction. `cover-background-brief.json` is required whenever a cover exists, regardless of profile. `asset-plan.json`, `asset-manifest.json`, `illustration-briefs.json`, and `penpot-image-upload-report.json` are required when reconstruction uses local image assets, including the required cover background, or the profile requires complete asset evidence. `speaker-notes.md` is optional but presenter-only content must never be placed visibly on a slide. If an asset is planned but cannot be uploaded, record the route change and reason code, update the scene graph, and re-run the fidelity gate.

## Workflow

### 0. Resolve Production Contract

Read `references/production-contract.md` before deciding which artifacts to create.

1. Select exactly one profile: `fast`, `standard`, or `premium`.
2. Write `capability-report.json` from observed tool, Penpot, font, media, preview, and PDF evidence. Use `unknown` when a capability has not yet been tested.
3. Initialize `deck-run-manifest.json` with `schema_version`, profile, status, status cap, stages, artifact references, warnings/errors, and resume point.
4. Decide whether the run uses real visual comps or an allowed native-only route. Record missing capabilities and stable reason codes.
5. Update both files after every completed or failed stage. Never reconstruct the same production state from chat memory alone.

Profiles reduce process overhead, not the quality promised to the user. A fast smoke still needs readable native text, coherent composition, current previews, and a recorded 17-gate verdict. A premium run blocks when required comp, export, or approval evidence is unavailable.

### 1. Establish Deck Brief

Define:

- Audience and presentation context.
- Page count and section rhythm.
- Source text that must be preserved.
- Visual tone, especially whether the deck should use the V2 stable system.
- Whether `.pptx` is truly mandatory or only habit.

If the user says "做 PPT" but does not explicitly require Office editing, default to Penpot source + PDF delivery.

### 1A. Build Evidence And Storyline

Before outlining slides, read `references/content-and-gates.md` and create:

- `source-evidence-table.json`: source fact, claim, number, uncertainty, and traceable source location;
- `storyline-options.json`: at least two plausible storylines, their audience fit, tradeoffs, and selected route;
- per-slide `content_claim`, `evidence_refs`, and `density_target`.

For a low-risk personal or smoke deck, the agent may self-approve the checkpoint and record why. For research, consulting, board, investor, or data-heavy decks, require explicit user confirmation of the storyline before visual production.

### 1B. Write Plain-Language Slide Scripts

Before choosing a component, template, or layout, write `slide-content-script.json`. Each slide must first work without visual styling.

For every slide record:

- `slide_job`: what this page contributes to the deck;
- `reading_form`: `narrative | comparison | process | evidence-explanation | image-caption | data-explanation | quote-or-beat`;
- `complete_expression`: the page's meaning written as normal prose or a naturally structured comparison/process, not as design labels;
- `canonical_visible_copy`: the exact title, body, captions, and labels intended to remain native in Penpot;
- `semantic_relationships`: the causal, comparative, temporal, evidentiary, or qualifying relationships the layout must preserve;
- `reading_order`: the intended sequence through visible copy and visuals;
- `presenter_only`: detail that belongs in speaker notes rather than on the slide;
- `fragmentation_risks`: phrases that would become ambiguous if split into cards, chips, or badges.

Run the plain-text test before visual production: hide all boxes, colors, icons, and spatial grouping, then read the visible copy in order. The slide fails if a viewer must infer missing verbs, subjects, causality, comparison axes, or the relationship between adjacent fragments.

This is not a requirement to write a slogan plus three bullets. The reading unit may be a short paragraph, a two-sided comparison with a stated axis, a process whose transitions are written, an image with an explanatory caption, or a chart followed by an interpretation. Covers, section dividers, quotes, and deliberate emotional beats may remain sparse.

The plain-text test validates meaning only. It does not define the finished composition and must not be used to remove visual regions, evidence, depth, or detail from the later comp and Penpot build.

### 1C. Choose Theme And Semantic Blueprint

Do not author every page from scratch. Before comp generation:

- lock a `theme-profile.json`: colors, type hierarchy, grid, shared title/chrome slots, chart language, image language;
- read `references/semantic-visual-grammar.md` and choose a visual structure that preserves the slide's reading unit;
- write `semantic-visual-plan.json` with `content_function`, `reading_form`, `semantic_relationships`, optional `component_archetype`, `component_variant`, `mutation_needed`, and `why_this_grammar`;
- write `composition-richness-contract.json` for every slide with `expression_spine`, `dominant_visual`, `visual_anchor_type`, `recognizable_subject`, `subject_cues`, `illustration_job`, `non_card_visual_area`, `supporting_regions`, `evidence_or_artifact_layer`, `depth_strategy`, `visual_memory`, `richness_floor`, and optional `sparse_exception_reason`;
- vary the content grammar while preserving the shared title/chrome system.

If the closest component is imperfect, use it as a reference and mutate the generated instance. If prose, an image-caption pair, or a chart with interpretation is clearer than a diagram, no component archetype is required. However, `component_archetype: null` never means `dominant_composition: null`: the slide still needs a strong spatial idea, visual memory, depth strategy, and supporting evidence or contextual detail unless it records an intentional sparse exception. Do not force the content into a bad component or write the mutation back into the global catalog.

### 2. Generate Expected-Result Visual Comps

Use `GordenImagePPTGen` for A1-A4:

- A1: infer or confirm the brief.
- A2: write an outline with slide roles.
- A3: write one prompt per slide.
- A4: call a real raster image backend and write `imagegen-manifest.json`.

On this machine, default to `image-studio-generation`. For smoke tests use `Quality medium`; for production use `Quality high`.

Important:

- Do not compose image-only PPTX unless explicitly requested.
- Do not use code/SVG/HTML/Canvas to fake raster comp generation.
- If comp text is wrong, keep the visual role but use canonical text from the brief in Penpot.
- Tell the image model to preserve the reading unit and visible relationships. Do not reward a comp for replacing complete copy with decorative micro-labels.
- If a comp is visually weak, do not blindly rebuild it. Use it as a warning signal and fall back to the V2 stable visual system.
- If image generation is unavailable, follow the profile rule in `references/production-contract.md`. `fast` and `standard` may use a recorded native-only route; `premium` blocks when comp evidence is required. Never create a fake `imagegen-manifest.json`.

### 2A. Build The Fixed Cover Background

When the deck contains a cover, run this route even when content slides use approved native-only reconstruction:

```text
cover-background-brief.json -> gpt-image-2 text-free background -> asset QA -> Penpot full-bleed image fill -> native single-hue mask -> native editable cover text -> exported cover preview
```

Create `cover-background-brief.json` before prompting:

```json
{
  "slide": "01",
  "backend": "gpt-image-2",
  "asset_role": "cover_background",
  "subject": "one concrete visual subject or scene tied to the deck thesis",
  "rhetorical_job": "establish the topic, tension, or offer before any body slide",
  "focal_point": {"x": 0.72, "y": 0.48},
  "title_safe_zone": {"x": 0.05, "y": 0.16, "w": 0.52, "h": 0.60},
  "crop_tolerance": "safe for 16:9 full-bleed center crop",
  "palette_relationship": "supports the deck palette without baking in the final color treatment",
  "reference_use": {
    "borrowed_mechanisms": ["full-bleed background", "mask separates image from native type"],
    "must_not_copy": ["topic", "title", "subtitle", "names", "tags", "palette", "image subject", "exact layout"]
  },
  "negative_constraints": ["no text", "no letters", "no logo", "no UI", "no chart", "no watermark", "no slide frame"]
}
```

Cover rules:

- Generate a background image, not a complete slide. No canonical cover copy may appear in the raster asset.
- Compose for `16:9` full bleed. Keep the declared title-safe zone calm and place the visual subject outside or around it rather than behind the title.
- Use a real subject, product, place, person, artifact, or scene relevant to the deck. Do not settle for generic atmospheric blur, decorative gradients, or stock-like darkness.
- Upload the accepted asset and use it as an edge-to-edge Penpot image fill. Do not place it inside a card or right-side image panel.
- Declare a native `cover_overlay` between background and text. It may be a uniform solid layer or a single-hue alpha gradient: the color remains constant while opacity changes to blend the image into the title field. Do not use a multi-hue decorative gradient.
- `cover_overlay.enabled` may be `false` only when the exported preview and contrast check prove the title-safe zone already supports the text; record the reason.
- Place title, subtitle, author/date, logo, and metadata as native Penpot layers above the overlay. For `1440x810`, use at least `56px` for the cover title, `24px` for the subtitle, and `16px` for meaningful cover metadata.
- Target at least `4.5:1` contrast for title and subtitle in the final composite. Increase overlay coverage/opacity or reposition the text instead of adding a text card.
- Regenerate the background when the subject, crop, safe zone, or accidental image text fails. Do not patch broken raster text because raster text is forbidden here.
- If `gpt-image-2` or required media upload is unavailable, record the cover-specific reason code and block before claiming the cover built. A general `fast` or `standard` native-only fallback does not override this rule.
- Use another cover route only after explicit user approval; record `ROUTE_USER_APPROVED_NATIVE_COVER_OVERRIDE` and remove the fixed-background claim.

Reference-informed composition heuristics, not a template:

- The fixed part is the production chain, not the reference cover's composition. Choose the subject, safe zone, mask direction, text hierarchy, and metadata from the current deck brief and generated image.
- Never copy a reference cover's topic, title, subtitle, names, tags, image subject, palette, exact coordinates, or complete left/right anatomy. Record what mechanism was learned and what was deliberately changed.
- When the new subject naturally sits on the right, one valid option is to keep details in the right `42-50%` and reserve the left `50-58%` as a title field. Other valid routes include a bottom title band, centered editorial window, top title field, or reversed subject/text direction.
- For a right-subject route, one theme-colored mask may start around `90%` opacity at the text edge, `55%` near the transition, and `10%` at the subject edge. These are starting values, not reference coordinates to copy.
- When tags, author/date, or a page number sit near the bottom, an optional second black single-hue mask may rise through the lower `35-42%`, from transparent to roughly `60%` opacity.
- Keep the cover title left aligned, card-free, and allowed to use two strong lines. It may enter the transition zone but must not cover the subject's face, product, or evidence hotspot.
- Use only the hierarchy the current cover needs. Title and subtitle are common; thesis, author/date, tags, logo, and page number are optional. Do not copy or invent metadata merely to fill a reference-derived template.
- Treat the reference values as a compositional default, not a fixed navy palette. Derive the mask color and text accents from the active deck theme.

### 3. Create Temporary Deck DESIGN.md

Before Penpot reconstruction, inspect the generated comp images with visual capability. Do not infer the design system from prompts alone.

Write `deck-design.md` with this structure:

```markdown
---
name: vfdeck-temp-[short-topic]
canvas:
  width: 1440
  height: 810
colors:
  background: "#..."
  surface: "#..."
  text-primary: "#..."
  text-muted: "#..."
  accent-cyan: "#..."
  accent-danger: "#..."
  accent-warn: "#..."
typography:
  display: { family: "...", weight: 700, size: "...", lineHeight: "..." }
  title: { family: "...", weight: 700, size: "...", lineHeight: "..." }
  body: { family: "...", weight: 400, size: "...", lineHeight: "..." }
presentation_distance_scale:
  baseline_canvas: "1440x810"
  body: { preferred_px: 24, floor_px: 22 }
  supporting_copy: { floor_px: 20 }
  meaningful_label: { floor_px: 16 }
  caption_source_footer: { floor_px: 14 }
  nonessential_metadata: { floor_px: 12, exception_required: true }
text_system:
  reading_unit: "..."
  body_composition: "paragraph | comparison | process | caption | data-explanation"
  label_policy: "labels only for real categories, states, steps, or metadata"
  sentence_fragment_policy: "never split clauses into separate decorative objects"
composition_system:
  expression_spine: "..."
  dominant_visual: "..."
  visual_anchor_type: "illustration | chart | diagram | artifact | photo | expressive-typography"
  recognizable_subject: "concrete subject name or null when the anchor type does not require one"
  subject_cues: ["cue 1", "cue 2", "cue 3"]
  illustration_job: "what the anchor explains, proves, or makes memorable"
  non_card_visual_area: "bbox and approximate share of the content region"
  supporting_regions: "..."
  evidence_or_artifact_layer: "..."
  depth_strategy: "foreground / midground / background or an intentional alternative"
  richness_floor: "minimum internal structure and visual memory that Penpot must preserve"
  sparse_exception_rule: "only covers, dividers, quotes, emotional beats, or documented rhetorical restraint"
spacing:
  page-margin: ...
  card-padding: ...
  grid-gap: ...
radii:
  panel: ...
  badge: ...
components:
  rail: ...
  badge: ...
  process-card: ...
  comparison-panel: ...
title_system:
  cover: "full-bleed gpt-image-2 background + declared single-hue mask + native title/subtitle/meta"
  section_or_content_slide: ...
  progress_label: ...
  subtitle_rule: ...
illustration:
  usage-principle: ...
  recognizable-subject-policy: ...
  minimum-subject-cues: 3
  five-slide-coverage: "at least two content slides, or a recorded deck-level exception"
cover_system:
  background_route: "gpt-image-2 -> Penpot full-bleed image fill"
  title_safe_zone: "normalized x/y/w/h"
  overlay: { enabled: true, mode: "solid | single-hue-alpha-gradient", color: "#...", opacity_or_stops: "...", coverage: "full | title-side", optional_lower_mask: "..." }
  native_text_layers: ["title", "subtitle", "author/date", "required metadata"]
  contrast_target: "4.5:1"
  image-weight: ...
  crop-style: ...
  acceptable-subjects: ...
  forbidden-subjects: ...
---

## Visual Intent
...

## Layout Grammar
...

## Slide Family Rules
...

## Illustration Rules
...

## Forbidden Drift
...
```

Requirements:

- Use actual visual observation from comps: color samples, approximate type scale, spacing, density, hierarchy, card anatomy, rail/badge behavior, image crop behavior.
- Be specific. Avoid vague words like "premium", "modern", "high-end" unless followed by concrete geometry and token rules.
- Include both machine-readable tokens and human-readable design rationale.
- Define how complete expressions remain readable after layout: body width, paragraph grouping, comparison axes, process transitions, captions, and reading order.
- Define the presentation-distance type scale. On a `1440x810` canvas, body copy is `24px` by default and never below `22px`; supporting copy is at least `20px`; meaningful labels are at least `16px`; captions, sources, footers, and page metadata are at least `14px`. `12px` is reserved for explicitly nonessential metadata with a recorded exception.
- If copy does not fit at its role floor, rewrite, regroup, split the slide, or recompose the layout. Never shrink below the floor as an overflow or density fix.
- Define how compositional richness survives reconstruction: dominant focal object, support regions, evidence/artifact detail, depth, scale contrast, routes, texture, and minimum internal complexity.
- Define the visual anchor separately from supporting UI-like structures. A card grid, rail, status ladder, or ledger cannot satisfy the anchor requirement unless it depicts a concrete subject with at least three recognizable structural cues.
- Define a shared `title_system`. The cover may be special, but content slides must have a stable title entry pattern: same rough title zone, same progress/meta treatment, same subtitle relationship, and consistent accent rail behavior.
- Define the cover as a separate fixed production system: full-bleed `gpt-image-2` background, left/right subject-safe composition, title-safe zone, explicit native single-hue mask object, native editable copy, and final-composite contrast target.
- Include `Forbidden Drift`: colors, gradients, card shapes, stock-photo habits, dashboard noise, and repeated skeletons that would make the deck worse.
- If comps conflict, choose the strongest V2-stable pattern and document the override.

### 4. Extract V2 Slide Contracts

For each slide write a compact contract:

- `role`
- `dominant_visual_grammar`
- `deck_design_refs`
- `native_text_regions`
- `native_shape_regions`
- `illustration_decision`
- optional `image_asset_regions`
- `title_system_compliance`
- `content_claim`
- `reading_form`
- `complete_expression`
- `canonical_visible_copy`
- `semantic_relationships`
- `reading_order`
- `fragmentation_risks`
- `expression_spine`
- `dominant_visual`
- `visual_anchor_type`
- `recognizable_subject`
- `subject_cues`
- `illustration_job`
- `non_card_visual_area`
- `supporting_regions`
- `evidence_or_artifact_layer`
- `depth_strategy`
- `visual_memory`
- `richness_floor`
- optional `sparse_exception_reason`
- `evidence_refs`
- `density_target`
- `component_archetype`
- `component_mutations`
- optional `illustration_brief_ref`
- required `cover_background_brief_ref` and `cover_contract` when `role` is `cover`
- `quality_risks`

Use roles such as:

- `cover-method`
- `failure-mode`
- `pipeline`
- `scene-graph`
- `penpot-source`
- `delivery`

The contract should produce visibly different slide structures while obeying `deck-design.md` and keeping the same dark/cyan V2 design language. Structural variety must come from different meanings, not from splitting one sentence into more visual objects. Coherent copy is the expression spine, not the whole composition.

### 5. Create Comp-to-Penpot Scene Graph

Before building in Penpot, translate every comp and slide contract into `comp-to-penpot-scene-graph.json`.

This is the executable reconstruction contract. It must be more concrete than `deck-design.md`.

For every slide include:

```json
{
  "slide": "03",
  "board": "VFDeck / 03 / Temporary DESIGN.md",
  "fidelity_target": "preserve pipeline machine as the primary visual memory",
  "regions": [
    {
      "id": "title",
      "type": "native-text",
      "planned_route": "native_penpot_text",
      "actual_route": null,
      "editability": "native_required",
      "fallback_chain": ["native_penpot_text"],
      "reason_codes": [],
      "qa_checks": ["native text remains readable in preview"],
      "bbox": [58, 52, 940, 70],
      "z": 30,
      "style_ref": "typography.title",
      "text_role": "title",
      "font_size_px": 48,
      "role_floor_px": 40,
      "reading_order": 1,
      "text": "Comp 先变成临时 DESIGN.md"
    },
    {
      "id": "extraction-machine",
      "type": "illustration",
      "planned_route": "generated_image",
      "actual_route": null,
      "editability": "visual_only_allowed",
      "fallback_chain": ["generated_image", "native_penpot_shape", "hybrid_overlay"],
      "reason_codes": [],
      "qa_checks": ["fallback preserves the extraction-machine identity and richness floor"],
      "bbox": [96, 294, 1248, 286],
      "z": 12,
      "source": "generated-asset | native-vector-fallback",
      "visual_anchor_type": "illustration",
      "recognizable_subject": "extraction machine",
      "subject_cues": ["intake tray", "four processing chambers", "output stack"],
      "illustration_job": "make the transformation and fidelity-loss points tangible",
      "non_card_visual_area": {"bbox": [96, 294, 1248, 286], "content_area_ratio": 0.41},
      "component_recipe": "wide machine frame, central core, four chambers, cyan tubes, glow nodes",
      "density_target": "at least 4 chambers, 6 route nodes, 8 rail segments, 1 dominant focal object",
      "fallback_minimum": "must still read as an extraction machine, not a row of boxes"
    }
  ],
  "depth_layers": ["background-grid", "ambient-rails", "main-panels", "illustration", "native-text", "state-badges"],
  "must_not_flatten": ["illustration", "route hierarchy", "title scale"],
  "fidelity_checks": [
    "primary visual memory remains visible within 3 seconds",
    "native text is readable",
    "illustration is not generic dashboard filler",
    "slide does not become a primitive rectangle diagram"
  ]
}
```

Required fields:

- `bbox`: concrete target position and size in 1440x810 coordinates.
- `z`: depth order, not just parent-child order.
- `component_recipe`: what geometry must be created, not just a mood description.
- `density_target`: minimum visual complexity for the region.
- `fallback_minimum`: what a native fallback must preserve if assets fail.
- `fidelity_checks`: slide-specific visual tests.
- `planned_route`, `actual_route`, `editability`, `fallback_chain`, `reason_codes`, and `qa_checks`: object-level delivery contract from `references/production-contract.md`.
- Every native text region must also declare `text_role`, `font_size_px`, `role_floor_px`, and `reading_order`, plus `small_text_exception` when `12px` nonessential metadata is used. If several regions belong to one sentence or argument, declare their shared `reading_unit_id`; splitting them must not remove the words that express their relationship.
- Every non-sparse slide must declare one `dominant_visual`, an allowed `visual_anchor_type`, `illustration_job`, and `non_card_visual_area`, plus at least one meaningful supporting region, an evidence/artifact or contextual-detail layer, and a depth strategy. Raw element counts are not the goal; the goal is enough internal structure to preserve the comp's visual memory.
- Allowed anchor types are `illustration`, `chart`, `diagram`, `artifact`, `photo`, and `expressive-typography`. Card grids, rails, ledgers, status panels, and dashboard frames are support geometry, not visual-anchor types.
- An `illustration` anchor must declare a concrete `recognizable_subject` and at least three `subject_cues`. Those cues must remain recognizable after a native fallback and in the actual exported preview.
- `richness_floor` must name what cannot disappear during Penpot translation: centerpiece identity, internal substructure, routes, annotations, artifact texture, depth, or supporting evidence.

If a slide relies on an image asset and the asset cannot enter Penpot, update the scene graph before building. Do not proceed with the old asset-dependent contract.

For a cover, the scene graph must include these three separate objects:

```json
{
  "cover_background": {
    "type": "image-fill",
    "bbox": [0, 0, 1440, 810],
    "planned_route": "gpt_image_2_generated_background",
    "actual_route": null,
    "editability": "visual_only_allowed",
    "fallback_chain": [],
    "qa_checks": ["text-free asset", "subject recognizable", "16:9 crop works", "title-safe zone remains calm"]
  },
  "cover_overlay": {
    "type": "native-shape-group",
    "enabled": true,
    "mode": "single-hue-alpha-gradient",
    "layers": [
      {
        "id": "title-mask",
        "color": "#17324D",
        "direction": "left-to-right",
        "opacity_stops": [[0.0, 0.90], [0.58, 0.55], [1.0, 0.10]],
        "coverage": "full"
      },
      {
        "id": "lower-mask",
        "optional": true,
        "color": "#000000",
        "direction": "top-to-bottom",
        "opacity_stops": [[0.0, 0.0], [1.0, 0.60]],
        "coverage": "lower-40-percent"
      }
    ],
    "planned_route": "native_penpot_shape",
    "actual_route": null,
    "qa_checks": ["sits above background and below text", "single-hue only", "no decorative multi-color gradient", "supports 4.5:1 text contrast"]
  },
  "cover_text": {
    "type": "native-text-group",
    "planned_route": "native_penpot_text",
    "actual_route": null,
    "editability": "native_required",
    "required_roles": ["cover-title", "cover-subtitle", "cover-metadata"],
    "role_floors_px": {"cover-title": 56, "cover-subtitle": 24, "cover-metadata": 16},
    "qa_checks": ["inside title-safe zone", "editable", "not baked into image", "contrast target passes"]
  }
}
```

### 6. Illustration And Asset Policy

Default to Penpot-native reconstruction for content slides when it can satisfy the same subject and preview-quality contract. The required cover background remains the fixed image-generation exception:

- Native text.
- Native rectangles, lines, panels, rings, rails, flow nodes, badges, and layer stacks as construction material, not as automatic proof of an illustration.
- Simple vector-like diagrams made from Penpot shapes.

Illustrations must be planned like a human PPT maker would plan them, not like a quota of pasted images. For every slide, write an `illustration_decision`:

```json
{
  "slide": "03",
  "needs_illustration": true,
  "visual_anchor_type": "illustration",
  "recognizable_subject": "translation machine",
  "subject_cues": ["input document", "processing chambers", "verified output stack"],
  "illustration_job": "turn an abstract workflow into one recognizable transformation scene",
  "non_card_visual_area": {"content_area_ratio": 0.38},
  "rhetorical_job": "make the pipeline feel tangible, not decorate the page",
  "information_job": "show the concrete transformation stages and where fidelity can be lost",
  "claim_supported": "a deck is improved by three translations, not by direct prompt-to-shape generation",
  "evidence_payload": ["stage count", "handoff artifacts", "risk points"],
  "best_form": "abstract process machine built from native shapes plus one small generated texture panel",
  "placement": "right 42% of canvas, vertically centered, clear of title and page rail",
  "visual_weight": "secondary-to-title, primary within content region",
  "crop_or_mask": "wide rounded panel, no text inside raster",
  "source": "generate-local-asset | native-shape | reuse-comp-region | omit",
  "reason": "..."
}
```

Use an illustration when it has a clear rhetorical job:

- clarifies an abstract process;
- makes a contrast emotionally legible;
- provides evidence or artifact texture;
- adds new information the text does not already say;
- supports a specific claim, diagnosis, or proof point;
- anchors the slide's visual memory.

Do not use an illustration when it only fills blank space, repeats the title, creates fake dashboards, or competes with the main hierarchy. A pretty image with no information or proof value is a failed illustration. A polished card grid, rail, ledger, or status panel is not an illustration merely because it is large or visually dominant.

For a visually rich five-slide deck, at least two content slides must use a recognizable subject as an illustration anchor. Record a deck-level exception only when charts, artifacts, photos, or domain-faithful diagrams are more truthful than figurative illustration; the exception must name the substitute anchors and why they carry stronger evidence.

When a slide uses generated explanatory imagery, chart redraws, unfamiliar entities, scientific/cultural objects, or embedded labels, read `references/illustration-contract.md` and create an `illustration_brief` before prompting. Keep in-image Chinese labels short and concrete; keep explanatory sentences as native Penpot text outside the image.

Use local generated image assets only when all of these are true:

- The comp region truly needs a raster visual, photo, screenshot-like insert, or complex illustration.
- The generated asset is crisp, no-text or text-safe, relevant, and visually stronger than native shapes.
- The asset has a specific target bbox and layer purpose.
- The asset has an `information_job`, `claim_supported`, and `evidence_payload`, not only a style description.
- The asset will not make the deck look like a blurry pasted screenshot.
- The asset follows `deck-design.md` illustration rules: crop, color temperature, subject type, density, and visual weight.

If the asset fails this gate, classify it as:

- `native-shape`: rebuild with Penpot geometry.
- `drop-with-reason`: omit because it harms quality.

If the asset cannot be uploaded into Penpot, do not automatically choose `native-shape`. First ask:

- Did the comp depend on this asset for its primary visual memory?
- Can native Penpot geometry preserve the same rhetorical job, depth, density, and focal weight?
- Does the fallback satisfy the slide's `fallback_minimum` in `comp-to-penpot-scene-graph.json`?

If not, stop the build and report the blocker. A weak native fallback is not a valid completion.

Do not treat `imageFillCount > 0` as success by itself. For V2 stable decks, `imageFillCount = 0` can be valid if the native design is stronger.

### 7. Build Editable Penpot Deck

Use `penpot-workflow`.

Required gate:

- Verify active Penpot MCP/file context and update `capability-report.json` with observed evidence.
- Read the current page before modifying.
- If no file exists and tools cannot create one, stop and ask the user to open/create a blank Penpot file and connect MCP.
- Do not build the deck until visual comp evidence, `deck-design.md`, slide contracts, and `comp-to-penpot-scene-graph.json` exist, unless the user explicitly asks for a no-image dry run.

Build rules:

- One Penpot board per slide.
- Use `1440x810` unless the user requests another aspect/size.
- Use the V2 stable dark/cyan design system by default.
- Apply `deck-design.md` tokens before placing slide-specific content.
- On the cover, place layers in this order: full-bleed generated background, declared native single-hue mask layer(s), native cover text/metadata. Verify the image fill really covers all four board edges after crop.
- Keep cover copy inside the brief's title-safe zone and outside a card. Do not rasterize title, subtitle, author/date, or logo with the background.
- Use native text for all important copy.
- Apply the role floors from `presentation_distance_scale` before solving layout. On `1440x810`, body copy defaults to `24px` and has a `22px` hard floor; supporting copy is at least `20px`; meaningful labels/stage names/axis labels are at least `16px`; captions, sources, footers, and page metadata are at least `14px`.
- Permit `12px` only for explicitly nonessential metadata with a `small_text_exception`; it cannot carry a claim, category, stage, status, relationship, or required source.
- If a text region does not fit at its role floor, recompose the region, reduce nonessential copy, or split the slide. Do not lower `font_size_px` below `role_floor_px`.
- Place the canonical visible copy from `slide-content-script.json` before decorative microcopy.
- Keep each reading unit visually continuous. Do not create one card per phrase, one badge per clause, or a label cloud when ordinary prose or a clearly related diagram reads better.
- Reconstruct the full composition around that reading unit: dominant visual, support regions, evidence/artifact detail, depth layers, scale contrast, and visual routes from `composition-richness-contract.json`.
- A simplified native fallback is invalid if it preserves readable text but loses the comp's centerpiece, internal detail, depth, or evidence layer below the declared `richness_floor`.
- Use named layers matching the scene graph.
- Reuse components/tokens for shared rails, cards, badges, dividers, and page numbers.
- Preserve slide role and hierarchy over pixel-perfect comp imitation.
- Place illustrations according to the slide's `illustration_decision`, not as generic right-side image blocks.
- Preserve each illustration anchor's `recognizable_subject`, all required `subject_cues`, and meaningful `non_card_visual_area`; do not let supporting chrome consume the subject.
- Build each major region from its scene-graph `component_recipe`; do not replace rich comp regions with generic rectangles unless the fallback minimum still passes.
- Track every intentional deviation from the comp in `penpot-build-report.json`.
- Resolve every object's `actual_route` during build. When it differs from `planned_route`, add a stable reason code, verify the fallback minimum, and append the route change to `deck-run-manifest.json.fallbacks`.
- Update `deck-run-manifest.json` after board creation, preview export, verification, and delivery. Keep `last_successful_stage` and `resume_from` current.
- Do not use unsupported intermediate font weights such as `650`; prefer `400` and `700`.
- Avoid pixel line heights that can make text disappear in export; use default or proportional line-height.
- If using image fills, upload through `penpot.uploadMediaData` where possible and record mappings.

### 8. Quality Gate

Read `references/content-and-gates.md` and record all 17 gates in `quality-gates-report.json`. A failed required gate blocks delivery. Before calling the deck done, also verify:

- Every visible fact, number, and conclusion has an evidence reference or an explicit uncertainty marker.
- Each slide meets its declared density target without shrinking typography to hide overflow, and every native text node satisfies its declared `role_floor_px`.
- Each slide uses an intentional reading form; a semantic component grammar is required only when it makes the relationships clearer.
- Plain-text readability: when visible copy is extracted in reading order, it still forms a complete and understandable expression.
- Relational clarity: viewers do not need to invent the missing cause, contrast, sequence, qualification, or conclusion between text fragments.
- Fragmentation audit: sentence fragments appear only as genuine labels, categories, states, steps, or metadata, not as decorative substitutes for prose.
- Composition audit: every non-sparse slide has a memorable dominant composition, meaningful support, deliberate depth, and enough internal detail to avoid title + paragraph + simple image results.
- Dual-axis verdict: record readability and compositional richness separately. The slide fails if either axis fails.
- Typography sub-verdict: record the minimum actual size for each `text_role`, all `small_text_exception` entries, and any role-floor violation. Coherent copy that is too small still fails.
- Visual-anchor sub-verdict: record `visual_anchor_type`, `recognizable_subject`, surviving `subject_cues`, and `non_card_visual_area`. A busy page with only generic UI chrome still fails.
- Every slide board exists on the current Penpot page/root.
- Required text is native and visible in exported previews.
- No obvious overlap, clipping, or off-board content.
- Visual rhythm is not a generic repeated template.
- `deck-design.md` compliance: colors, type scale, spacing, radii, components, and forbidden drift.
- Title system compliance: every non-cover slide uses the same page-start grammar unless the scene graph explicitly documents an intentional exception.
- Scene graph compliance: required bboxes, depth layers, component recipes, density targets, and fallback minimums are implemented.
- The deck still resembles the V2 stable design language: dark editorial surface, cyan accents, large type, clean native geometry.
- Illustration naturalness: each image or illustrated region has a rhetorical job, information job, claim supported, recognizable subject when applicable, at least three surviving subject cues, correct scale, intentional crop, meaningful non-card area, and a clean relationship to nearby text.
- Illustration coverage: a visually rich five-slide deck has recognizable subjects on at least two content slides, or a documented deck-level exception with stronger chart/artifact/photo/diagram anchors.
- Cover production: `cover_background`, `cover_overlay`, and `cover_text` routes are all resolved; the background is full bleed and text-free; the overlay state is explicit; native title/subtitle remain in the safe zone and meet the declared contrast and role floors.
- Generated illustration labels, data, reference cues, and crop are correct; regenerate failed assets instead of hiding errors with unrelated overlays.
- Charts are redrawn from extracted semantics/data, not visually skinned screenshots. Axis, values, units, category order, and uncertainty remain exact.
- If image assets are used, they improve quality and have mappings in `penpot-image-upload-report.json`.
- Export preview is nonblank.
- Run a comp-vs-Penpot fidelity audit for every slide:
  - Export the Penpot slide preview.
  - Compare it against the generated comp.
  - Identify lost visual memory, lost depth, flattened components, weak illustration fallback, repeated skeletons, and title/spacing drift.
  - Record the result in `fidelity-audit-report.md`.
- Run a visual audit using the `ui-state-auditor` method:
  - What should the viewer notice first?
  - Are object identities clear?
  - Are accents and status signals owned by the right object?
  - Are spacing, scale, crop, and text fit acceptable?
  - Is the deck drifting into AI-slop?
- Run a fine-detail visual audit for every exported slide, not only a deck-level impression:
  - title and subtitle: same title system, no accidental drift, no awkward line break;
- text geometry: no clipped glyphs, no cramped line-height, no overlong line, no button/tag overflow;
  - presentation distance: body, supporting copy, meaningful labels, and captions meet their role floors in the actual Penpot text properties;
  - reading continuity: related text is grouped and ordered; unrelated microcopy does not interrupt the main expression;
  - alignment: repeated elements share baselines, edges, gutters, and visual centers;
  - state signals: pass/fail, selected, disabled, source, and destination colors belong to the right object;
  - image crop: no accidental editor-handle look, no meaningless crop, no image fighting the title;
  - detail density: centerpiece regions have enough internal structure to match their scene-graph density target;
  - comp delta: name the most important visual memory lost from the comp and either fix it or record a justified exception.

Passing structural checks is not enough. A deck with correct board count, native text, and no off-board elements can still fail if it is visually flat or far from the comp.

If the audit says the generated-asset version is worse than the native V2 style, revert to the V2 native system. If the native fallback is worse than the comp and also fails the scene graph fallback minimum, block completion and report the reason.

After all gates, re-probe preview/PDF evidence and apply `references/production-contract.md` status caps. A passed visual audit may produce `verified`, but only existing promised deliverables plus all profile-required evidence may produce `final`. A failed required gate produces `blocked`.

### 9. Deliver

Primary delivery:

```text
Penpot editable source + PDF
```

Optional delivery:

```text
PPTX compatibility file
```

Only create PPTX when required. Do not spend effort on image-only PPTX when PDF already satisfies presentation delivery.

Delivery language must include the bounded status from `deck-run-manifest.json`, its status cap, evidence references, fallbacks, and caveats. Do not replace this with "done", "completed", or "production-ready" unless the manifest status is `final`.

## Common Mistakes

- Mistake: forcing PPTX because the user said "PPT".
  Fix: default to Penpot + PDF unless Office editing is explicitly required.

- Mistake: treating generated slide images as final slides.
  Fix: use raster comps as visual direction; rebuild editable native Penpot source.

- Mistake: generating comps before the argument and evidence are settled.
  Fix: create the evidence table, compare at least two storylines, and lock per-slide claims first.

- Mistake: drawing every diagram from primitive rectangles.
  Fix: choose a semantic component archetype first, then adapt its geometry and hierarchy to the deck theme.

- Mistake: treating generated assets as a required proof of quality.
  Fix: content-slide image assets are optional and must pass the asset quality gate; the fixed cover background is the explicit exception.

- Mistake: asking `gpt-image-2` to generate the finished cover with the title already inside it.
  Fix: generate only the text-free background, upload it full bleed, add a native solid or single-hue alpha mask, then typeset all canonical cover copy in Penpot.

- Mistake: silently using a native panel cover when the cover image route is unavailable.
  Fix: record the cover-specific capability reason code and block, unless the user explicitly approves a different cover route.

- Mistake: pasting blurry AI-generated screenshots or dashboards into every slide.
  Fix: prefer native Penpot shapes unless the asset clearly improves the slide.

- Mistake: entering Penpot reconstruction directly from prompts and comps.
  Fix: first use visual capability to write `deck-design.md`, then reconstruct from that design system.

- Mistake: treating illustrations as decoration or a required image count.
  Fix: every illustration needs an `illustration_decision` plus an `illustration_brief` when generated imagery is involved.

- Mistake: counting a large card grid, rail, status ladder, or ledger as the slide illustration.
  Fix: declare an allowed `visual_anchor_type`; an illustration needs a concrete `recognizable_subject`, at least three `subject_cues`, an `illustration_job`, and meaningful `non_card_visual_area`.

- Mistake: fitting dense content by shrinking body rows and meaningful labels to dashboard-sized text.
  Fix: enforce role-aware presentation-distance floors and recompose, rewrite, or split the slide when text does not fit.

- Mistake: beautifying a chart screenshot directly.
  Fix: extract chart semantics and exact data, then redesign the chart from those facts.

- Mistake: patching broken generated-image labels with disconnected external text.
  Fix: use short 2-5 character labels in the image, inspect them, and regenerate when they are wrong.

- Mistake: writing `deck-design.md` and assuming Penpot reconstruction will improve automatically.
  Fix: write `comp-to-penpot-scene-graph.json` with bboxes, depth layers, component recipes, density targets, fallback minimums, and fidelity checks.

- Mistake: media upload fails, so the agent silently replaces the asset with simple native boxes.
  Fix: re-plan the scene graph fallback and block completion if the fallback cannot preserve the slide's visual memory.

- Mistake: passing QA because boards exist and no layers are off-canvas.
  Fix: run comp-vs-Penpot fidelity audit. Structure checks are necessary but not sufficient.

- Mistake: overfitting comp fidelity and losing the deck's design quality.
  Fix: preserve role, hierarchy, and V2 visual system first.

- Mistake: using one repeated left-text/right-image layout for every slide.
  Fix: use slide roles and varied visual grammar.

- Mistake: turning every sentence into a collection of short labels, chips, and equal-weight cards.
  Fix: restore the slide's complete expression from `slide-content-script.json`, make semantic relationships explicit, and use labels only where they name a real object, state, step, or category.

- Mistake: forcing every page into a conclusion headline plus three supporting points.
  Fix: choose the reading form that fits the content. A coherent paragraph, comparison, process, image-caption pair, or chart interpretation can be the primary page structure.

- Mistake: interpreting coherent copy as permission to simplify the whole page.
  Fix: keep the complete expression as the reading spine, then restore a dominant visual, supporting evidence/artifacts, layered depth, routes, scale contrast, and the comp's internal detail.

- Mistake: finishing an ordinary content slide as title + paragraph + one rectangular image because it passes the plain-text test.
  Fix: require the `composition-richness-contract.json` fields and block delivery unless a real `sparse_exception_reason` applies.

- Mistake: skipping visual audit because layer counts look correct.
  Fix: export previews and judge actual geometry, hierarchy, and taste.

## Output Summary Contract

When finishing, report:

- Selected production profile.
- Capability report summary and unavailable/unknown capabilities.
- `deck-run-manifest.json` status, status cap, last successful stage, and resume point.
- Penpot file/page name.
- Created or updated boards.
- Visual comp generation summary.
- Evidence table, storyline choice, and density targets.
- Plain-language slide scripts, reading forms, and any fragmentation risks corrected.
- Composition richness contracts, dual-axis verdicts, and any sparse exceptions.
- Theme profile and semantic visual plan.
- Temporary `deck-design.md` summary.
- Whether local assets were used or deliberately skipped.
- Illustration decisions summary.
- `comp-to-penpot-scene-graph.json` summary.
- Scene graph/layout contract summary.
- Layer/component summary.
- Fidelity audit summary.
- Visual audit summary.
- 17-gate quality report summary.
- PDF export status.
- Object-route fallbacks and reason codes.
- Whether PPTX was intentionally skipped.
- Known limitations.
