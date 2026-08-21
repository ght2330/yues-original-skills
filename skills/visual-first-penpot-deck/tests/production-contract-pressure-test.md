# Production Contract Pressure Test

## Scenario

Ask the skill to plan a five-slide `standard` deck when Penpot is available, image generation is unavailable, PDF export is unknown, and fonts have not been inventoried. Request the selected production profile, required artifacts, capability evidence, fallback routes, and strongest claimable delivery status.

## RED Baseline

The 2026-07-19 baseline produced a sensible Penpot-native fallback and avoided claiming that the deck was complete, but the response remained prose-driven:

- `standard-quality` was inferred without a defined production-profile contract;
- capability checks were listed, but no versioned `capability-report.json` was required;
- existing build and QA reports were listed independently, with no single run manifest or resume point;
- the strongest status was free text rather than a bounded delivery status with evidence requirements;
- required artifacts were not reduced according to the selected profile.

The failure was not unsafe visual guidance. It was the absence of a machine-checkable production envelope around an otherwise strong design workflow.

## PASS Criteria

The updated skill must require all of the following:

- an explicit `fast | standard | premium` profile selected before artifact planning;
- a profile matrix that scales internal artifacts and verification effort without weakening the promised deliverable;
- `capability-report.json` before build, with checked capabilities, unavailable capabilities, and allowed fallbacks;
- `deck-run-manifest.json` as the single stage/status/resume record for the run;
- object-level planned and actual delivery routes when a visual or editable object can downgrade;
- a bounded status vocabulary: `planned | built | previewed | verified | final | blocked`;
- a status cap that prevents `verified` or `final` when required preview, export, font, or visual evidence is missing;
- explicit reason codes and caveats for every blocked capability or fallback;
- no duplicate PPT IR or second design methodology layered over the existing reading-unit, composition, scene-graph, and 17-gate system.

## Failure Signals

- Calling `Quality medium` or `standard-quality` a production profile without applying an artifact matrix.
- Listing capability checks only in prose.
- Claiming `final` because Penpot construction succeeded while PDF or required visual evidence is unavailable.
- Silently replacing native/editable content with raster output.
- Creating parallel `PPT IR`, `Style Contract`, `Delivery Plan`, and QA files that duplicate current artifacts.

## GREEN Observation

The 2026-07-19 forward test used the same request in a fresh context. It selected the formal `standard` profile, required `capability-report.json` and `deck-run-manifest.json`, used stable capability and route reason codes, kept canonical copy on native Penpot routes, omitted fake image-generation artifacts, and capped both current and maximum status at `planned`. The response also distinguished a native-only fallback from comp fidelity instead of claiming that missing visual comps had been verified.

The live Penpot smoke then exercised the failure path: three read-only probes, including a minimal connection ping, timed out. The run must remain `blocked` until the user connects a Penpot file; no Penpot boards, previews, font evidence, PDF, or completion claim may be fabricated.
