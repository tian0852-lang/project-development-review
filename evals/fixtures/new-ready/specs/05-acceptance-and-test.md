<!-- review-meta
{
  "artifact_id": "DOC-SPEC5",
  "review_id": "REVIEW-new-ready",
  "version": "S1",
  "manifest": "../review-manifest.json",
  "design_source": "Figma",
  "scope_ids": [
    "frame-list",
    "frame-detail"
  ],
  "evidence_ids": [
    "E-DESIGN",
    "E-USER"
  ],
  "readability_limits": [
    "Synthetic fixture evidence only."
  ],
  "item_ids": [
    "SP5"
  ],
  "depends_on": {},
  "approval_status_ref": "#/artifacts/DOC-SPEC5/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-SPEC5/approval_event_ids"
}
-->

# Offline Cards (synthetic) — spec5

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:platform-coverage -->
## Platform coverage

SP5: H5 in desktop Chromium at 390 x 844; keyboard and browser Back included. iOS/Android native Not applicable because outside scope.

<!-- section:acceptance-cases -->
## Acceptance cases

SP5 / AC1: Select A, inspect Detail, Back retains A, open Clear, cancel retains A, confirm clears, reload resets, invalid ID recovers with Back. Check console/network/storage for no external calls or persistence. Evidence required: screenshot + recording; actual execution deferred to developer.
