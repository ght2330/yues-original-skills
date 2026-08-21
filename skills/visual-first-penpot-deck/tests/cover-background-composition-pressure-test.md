# Cover Background Composition Pressure Test

Use this regression test whenever cover, image generation, asset upload, title-system, fallback, or delivery-gate rules change.

## Scenario

Create a deck with a designed cover under time pressure. The user supplies a polished reference cover. `gpt-image-2` is the intended image backend, but generating one complete slide image with baked-in title text, falling back to a native dark panel, or copying the supplied reference's topic and layout would be faster than producing a clean independent background asset and recomposing the cover in Penpot.

## RED Baseline

Before this contract, the skill treated local generated assets as optional on every page and allowed `fast` or `standard` runs to use a native-only route when image generation was unavailable. The cover had no dedicated object route, no text-free background requirement, no mandatory mask layer, and no failure rule that prevented a dashboard-like native cover or a raster image containing the final title.

## PASS Criteria

- Every slide with role `cover` uses the fixed route `gpt-image-2 background -> Penpot image fill -> native single-hue mask -> native editable text`.
- `gpt-image-2` generates a background asset, not a complete slide: no title, subtitle, logo, UI, chart, frame, watermark, or prompt text is baked into the image.
- The background brief records subject, rhetorical job, focal point, crop tolerance, title-safe zone, palette relationship, negative constraints, and target `16:9` composition.
- The image is full-bleed or intentionally edge-to-edge after crop; it is not placed inside a decorative card.
- A `cover_overlay` object is always declared between the image and text. It defaults to an enabled native Penpot single-hue mask whose color, opacity or alpha stops, coverage, and relationship to the title-safe zone are explicit. A uniform solid or same-color alpha gradient is valid; a multi-hue decorative gradient is not. The overlay may be disabled only when the exported preview and contrast check prove the title-safe zone already works and the reason is recorded.
- Cover title, subtitle, author/date, and required metadata remain native Penpot text with presentation-distance role floors.
- The exported preview proves the subject remains recognizable, the title-safe zone is usable, and title/subtitle contrast reaches the declared target after the overlay.
- If cover image generation or upload is unavailable, the run records `CAPABILITY_COVER_IMAGEGEN_UNAVAILABLE` or `CAPABILITY_COVER_IMAGE_UPLOAD_UNAVAILABLE` and blocks before claiming the cover built.
- A native-only cover is allowed only after an explicit user override that removes the fixed image-background requirement; general `fast` or `standard` native-only fallback does not count as that override.
- The scene graph records separate `cover_background`, `cover_overlay`, and `cover_text` objects with independent routes and QA checks; `cover_overlay.enabled` is explicit even when false.
- The fixed element is the production chain, not the reference template. A supplied reference may influence full-bleed use, safe-zone logic, mask behavior, or native-text layering, but the new cover uses its own topic, copy, image subject, palette, geometry, and information hierarchy.
- `cover-background-brief.json.reference_use` records borrowed mechanisms and explicitly forbidden copied elements.

## Failure Signals

- Asking the image model to render the final Chinese title or complete slide.
- Treating a generated full-slide comp as the canonical cover.
- Placing the background image in a rounded card or right-side panel.
- Putting title text directly on a busy image without a native single-hue mask.
- Rasterizing the title, subtitle, author, date, or logo together with the background.
- Silently replacing the missing image with gradients, boxes, rails, or a generic native-only dashboard cover.
- Reporting the deck as built or verified when the required cover background has not entered Penpot.
- Reusing the reference cover's title, subtitle, names, tags, image subject, palette, exact left/right split, or full metadata hierarchy.

## SECOND RED Observation

The first live smoke copied the supplied AI+HR reference too literally: it reused the same title, subtitle, member names, topic tags, right-side HR scene, and nearly the same left-title/right-image anatomy. The image-generation and Penpot-layer route worked, but the reference boundary failed. This proves that a fixed production chain without an anti-copy rule can still turn a reference into a template.

## GREEN Observation

The 2026-07-19 static contract probe first failed on all six required terms: `cover_background`, `cover_overlay`, `CAPABILITY_COVER_IMAGEGEN_UNAVAILABLE`, `CAPABILITY_COVER_IMAGE_UPLOAD_UNAVAILABLE`, `title-safe zone`, and `fixed cover route`. After the update, the same probe passed.

The active skill now routes every cover through a text-free `gpt-image-2` background, full-bleed Penpot image fill, declared native single-hue mask, and native editable cover copy. The scene graph separates all three objects and assigns `56px`, `24px`, and `16px` floors to cover title, subtitle, and meaningful metadata. The overlay defaults to enabled and can be disabled only with exported-preview and contrast evidence.

The supplied AI+HR cover was inspected as a structural reference. Its first slide contains one full-bleed picture, one full-slide dark-blue same-color alpha gradient (`91% -> 56% -> 10%`), one optional lower black alpha gradient (`0% -> 62%`), and separate editable text groups. Those are mechanisms only, not reusable content or layout.

The failure path is also explicit: missing cover image generation or upload records a cover-specific reason code and blocks the fixed route. The general `fast` or `standard` native-only fallback applies only to content-slide reconstruction; changing the cover route requires an explicit user override recorded as `ROUTE_USER_APPROVED_NATIVE_COVER_OVERRIDE`. `quick_validate.py` passed after the implementation.

The corrected independent smoke then replaced the failed board. It used `visual-first-penpot-deck` itself as the topic and generated a physical presentation-production scene: a photographic plane passes through a cyan verification frame and becomes editable layout planes. The composition moved the title into a full-width lower field instead of the reference's left-title/right-people anatomy.

The final Penpot board contains one full-bleed generated image fill, one native single-hue bottom mask, and six native `Noto Sans TC` text layers. Automated inspection found none of the reference title, member names, or topic tags, plus zero role-floor violations, text overflow, or containment violations. The final exported preview was nonblank and visually inspected after the title-box repair. Originality and production-route verification now both pass; PDF unavailability still caps delivery at `verified`.
