# Presentation Distance And Illustration Pressure Test

Use this regression test whenever typography, density, visual-anchor, illustration, scene-graph, native-only fallback, or quality-gate rules change.

## Scenario

Create a five-slide `1440x810` presentation under a fast native-only route. The content is information-rich and the available Penpot primitives make cards, rails, ledgers, and dashboard panels faster to build than recognizable illustrations. The pressure is to fit all planned copy by shrinking labels and explanatory text while counting generic UI-like geometry as the dominant visual.

## RED Baseline

The 2026-07-19 engineering-v1 smoke passed all required structural gates but exposed both failures:

- the Typography Gate accepted a `12px` minimum even though many body rows and meaningful labels were too small at presentation viewing distance;
- five dominant visuals were described as a control rail, asymmetric split, pipeline, status ladder, and acceptance ledger;
- the deck contained 117 native text layers and no raster images, but no contract field required a recognizable native illustration subject;
- `dominant_visual` and high element counts allowed card/rail/status chrome to stand in for an illustration;
- the native-only fallback preserved editability but did not preserve an illustration-quality floor.

The failure was not clipping or missing content. It was role-blind typography and a visual-anchor contract that could be satisfied by polished interface chrome.

## PASS Criteria

- For a `1440x810` deck, explanatory body copy uses `24px` by default and never falls below `22px`.
- Supporting copy uses at least `20px`; meaningful labels, stage names, and axis labels use at least `16px`; captions, sources, footers, and page metadata use at least `14px`.
- `12px` text is permitted only for explicitly nonessential metadata with a recorded exception and must not carry a claim, step, category, status, or relationship.
- Overflow or density pressure is resolved by rewriting, regrouping, or recomposing content, never by shrinking below the role floor.
- Every native text node declares `text_role`, planned font size, and the applicable role floor so the Typography Gate can verify the actual result.
- Every non-sparse slide declares `visual_anchor_type`, `illustration_job`, and `non_card_visual_area` in addition to `dominant_visual`.
- Allowed visual-anchor types are `illustration`, `chart`, `diagram`, `artifact`, `photo`, or `expressive-typography`; generic card grids, rails, ledgers, and status panels are supporting structures, not anchor types.
- Every slide whose anchor type is `illustration` declares a concrete `recognizable_subject` and at least three `subject_cues` that survive reconstruction.
- A visually rich five-slide deck contains recognizable subjects on at least two content slides unless a recorded deck-level exception explains why charts, artifacts, or photos are more truthful.
- A native-only route passes the Illustration Evidence Gate only when its recognizable subjects remain legible in exported previews; editability and element count alone are insufficient.
- Typography and illustration-anchor results are recorded separately so one cannot compensate for the other.

## Failure Signals

- A `12px` minimum is reported as a typography pass without role-level exceptions.
- Body copy or meaningful labels are shrunk to preserve a dense layout.
- A card grid, progress rail, status ladder, acceptance ledger, or dashboard frame is named as the illustration.
- `dominant_visual` describes geometry but not a subject the audience can identify.
- A native-only fallback reports success because it contains many editable shapes even though the visual memory is generic UI chrome.
- Decorative icons or isolated symbols are counted as recognizable illustrations without three subject cues.

## GREEN Observation

The 2026-07-19 implementation added the missing role and anchor fields to the active skill and references. A static contract probe that initially failed on all seven terms (`presentation-distance`, `role_floor_px`, `visual_anchor_type`, `recognizable_subject`, `subject_cues`, `illustration_job`, and `non_card_visual_area`) passed after the update.

The comparable Penpot v2 smoke preserved the original page and created `Smoke - Engineering V1 Contract v2 - Readable Illustrated` with five new `1440x810` boards. Live inspection found `119` native text layers, `303` editable shapes, zero raster images, zero role-floor violations, zero text overflow, and zero containment violations. Role minima were `22px` for body, `20px` for supporting copy, `16px` for meaningful labels, and `14px` for footer/metadata.

Exported previews confirmed two recognizable native illustration subjects: a document verification scanner on slide 01 and a design production engine with a missing instrument module on slide 02. Each retained three declared subject cues and occupied a meaningful non-card content region. Slides 03-05 used diagram or artifact anchors without claiming that their rails, ladders, or ledgers were illustrations. The regression is closed at `verified`; PDF unavailability still prevents a `final` delivery claim.
