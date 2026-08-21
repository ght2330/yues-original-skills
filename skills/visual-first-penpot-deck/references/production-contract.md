# Production Contract

Use this contract before artifact planning. It scales process overhead, records actual environment capabilities, and bounds delivery claims without weakening the promised deck.

## Production Profiles

Choose exactly one profile and record it in `deck-run-manifest.json`.

| Profile | Use when | Required process |
|---|---|---|
| `fast` | Low-risk personal deck, smoke test, or at most six slides | Compact brief, slide scripts, composition contract, theme, scene graph, capability report, Penpot build report, all-slide previews, concise 17-gate report |
| `standard` | Normal user-facing deck | Evidence table, two storyline options, full scripts and composition contracts, semantic plan, comps or an approved native-only route, deck design, scene graph, build report, all-slide previews, fidelity/visual audit, 17-gate report, PDF attempt |
| `premium` | Board, investor, research, consulting, regulated, or source-heavy deck | Standard artifacts plus explicit storyline and blueprint approval, complete asset manifests, required comps, per-slide fidelity evidence, independent review when available, successful promised exports, and no unresolved required-gate caveat |

Profiles scale evidence, approvals, and recovery detail. They do not permit unreadable text, unsupported claims, silent raster fallback, missing accessibility, or a weaker promised deliverable.

Conditional artifacts remain conditional. A fast deck with claims or numbers still needs traceable evidence. A standard deck may use a native-only route for content slides when image generation is unavailable and the fallback is recorded. A deck with a cover is the exception: its fixed `gpt-image-2` background route remains required across profiles unless the user explicitly approves a different cover route. A premium deck blocks before build when required comp or delivery evidence cannot be produced.

## Capability Report

Write `capability-report.json` before Penpot build. Re-probe export capabilities after the first board exists.

```json
{
  "schema_version": "1.0",
  "profile": "standard",
  "checked_at": "ISO-8601 timestamp",
  "capabilities": {
    "penpot_context": {"status": "available | unavailable | unknown", "evidence": []},
    "image_generation": {"status": "available | unavailable | unknown", "evidence": []},
    "gpt_image_2_cover_background": {"status": "available | unavailable | unknown | not-required", "evidence": []},
    "media_upload": {"status": "available | unavailable | unknown", "evidence": []},
    "cover_image_upload": {"status": "available | unavailable | unknown | not-required", "evidence": []},
    "required_fonts": {"status": "available | unavailable | unknown", "evidence": []},
    "preview_export": {"status": "available | unavailable | unknown", "evidence": []},
    "pdf_export": {"status": "available | unavailable | unknown", "evidence": []}
  },
  "allowed_fallbacks": [],
  "blockers": [],
  "reason_codes": []
}
```

Evidence must name an observed file, page, tool result, exported artifact, or preview. Mentioning a capability in this skill is not evidence that it exists.

## Delivery Routes

Do not create a separate delivery-plan artifact. Add these fields to each object or region in `comp-to-penpot-scene-graph.json`:

```json
{
  "planned_route": "native_penpot_text",
  "actual_route": null,
  "editability": "native_required | native_preferred | visual_only_allowed",
  "fallback_chain": ["native_penpot_text"],
  "reason_codes": [],
  "qa_checks": ["native text remains readable in preview"]
}
```

Allowed route vocabulary:

- `native_penpot_text`
- `native_penpot_shape`
- `native_penpot_chart`
- `uploaded_raster`
- `generated_image`
- `hybrid_overlay`

Canonical text, conclusions, labels, page chrome, and evidence citations are `native_required`. Never silently replace them with raster content. When `actual_route` differs from `planned_route`, record the reason and verify the fallback minimum before continuing.

## Run Manifest

Use one `deck-run-manifest.json` as the run ledger. Existing reports remain evidence artifacts; do not duplicate their content in a second planning system.

```json
{
  "schema_version": "1.0",
  "run_id": "...",
  "profile": "standard",
  "status": "planned",
  "status_cap": "planned",
  "capability_report_ref": "capability-report.json",
  "artifact_refs": {},
  "stages": {
    "briefed": false,
    "planned": false,
    "comped": false,
    "built": false,
    "previewed": false,
    "verified": false,
    "delivered": false
  },
  "fallbacks": [],
  "warnings": [],
  "errors": [],
  "last_successful_stage": null,
  "resume_from": null,
  "evidence": []
}
```

Update the manifest after every completed or failed stage. `resume_from` names the first incomplete stage. Use references rather than copying full report bodies into the manifest.

## Delivery Status

Use only:

- `planned`: production contracts exist; Penpot build has not completed.
- `built`: all required Penpot boards exist; previews are not yet fully checked.
- `previewed`: every required slide has a nonblank current preview.
- `verified`: all profile-required gates pass, but a promised delivery artifact may still be unavailable.
- `final`: all promised deliverables exist and all profile-required evidence passes.
- `blocked`: a required capability, route, gate, or deliverable failed.

Apply the strongest matching status cap:

| Missing or failed evidence | Maximum status |
|---|---|
| Real Penpot context unavailable | `planned` or `blocked` |
| Required font check unknown or failed | `built` |
| Any required slide preview missing or blank | `built` |
| Any required quality gate failed | `blocked` |
| Promised PDF unavailable after successful visual verification | `verified` with caveat |
| Premium comp evidence unavailable | `blocked` |
| Native-required object silently downgraded | `blocked` |
| Required cover `gpt-image-2` background unavailable | `planned` or `blocked` |
| Required cover image cannot enter Penpot | `planned` or `blocked` |

Image generation unavailability alone does not block `fast` or `standard` content-slide reconstruction. Record `CAPABILITY_IMAGEGEN_UNAVAILABLE`, choose a native-only content route, remove comp-fidelity claims, and still pass the reading, composition, scene-graph, preview, and 17-gate checks. The fixed cover route is not covered by this fallback: when a cover exists, missing `gpt-image-2` or cover upload evidence blocks the cover unless the user explicitly approves another route. Premium still requires its declared comp evidence.

## Reason Codes

Use stable reason codes in capability, route, run, and quality records:

- `CAPABILITY_PENPOT_UNAVAILABLE`
- `CAPABILITY_IMAGEGEN_UNAVAILABLE`
- `CAPABILITY_MEDIA_UPLOAD_UNAVAILABLE`
- `CAPABILITY_COVER_IMAGEGEN_UNAVAILABLE`
- `CAPABILITY_COVER_IMAGE_UPLOAD_UNAVAILABLE`
- `CAPABILITY_FONT_UNVERIFIED`
- `CAPABILITY_PREVIEW_EXPORT_UNAVAILABLE`
- `CAPABILITY_PDF_EXPORT_UNAVAILABLE`
- `ROUTE_NATIVE_REQUIRED_DOWNGRADE_BLOCKED`
- `ROUTE_APPROVED_NATIVE_FALLBACK`
- `ROUTE_USER_APPROVED_NATIVE_COVER_OVERRIDE`
- `QA_REQUIRED_GATE_FAILED`
- `DELIVERY_ARTIFACT_MISSING`

Free-form explanation may accompany a code, but must not replace it.
