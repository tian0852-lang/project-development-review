<!-- review-meta
{
  "artifact_id": "PLAN-1",
  "review_id": "REVIEW-mixed-ready",
  "version": "T1",
  "manifest": "../review-manifest.json",
  "design_source": "Figma",
  "scope_ids": [
    "frame-list",
    "frame-detail"
  ],
  "evidence_ids": [
    "E-TECH",
    "E-USER"
  ],
  "readability_limits": [
    "Synthetic fixture evidence only."
  ],
  "item_ids": [
    "TECH1"
  ],
  "depends_on": {
    "BASELINE-1": "B1",
    "DOC-SPEC0": "S1",
    "DOC-SPEC1": "S1",
    "DOC-SPEC2": "S1",
    "DOC-SPEC3": "S1",
    "DOC-SPEC4": "S1",
    "DOC-SPEC5": "S1",
    "DOC-SPEC6": "S1",
    "ASSESS-1": "1"
  },
  "approval_status_ref": "#/artifacts/PLAN-1/approval_status",
  "approval_event_ids_ref": "#/artifacts/PLAN-1/approval_event_ids"
}
-->

# Offline Cards (synthetic) — plan

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:file-changes -->
## File changes

TECH1: Modify existing src/app.js (add Clear dialog, preserve List/Detail back behavior); reuse index.html and src/styles.css; extend tests/manual.md with cancel/confirm regression. Create independent-web/index.html, independent-web/src/app.js and independent-web/src/styles.css for the new independent H5 work unit. These are planned paths, not written business code.

<!-- section:initialization-and-configuration -->
## Initialization and configuration

TECH1: Retain existing static browser entry and no-dependency configuration; no replacement SDK or native changes. Mixed new work unit also uses plain static initialization.

<!-- section:state-and-interaction -->
## State and interaction

TECH1: App owns selectedId and route; List/Detail receive callbacks; ConfirmDialog owns only visibility. cardId passes as an allowlisted ID; Back retains selection; invalid ID enters error. Cancel/overlay/close/Escape preserve selection; confirm clears it; browser Back closes dialog first. No eval() or external evaluation.

<!-- section:risks-and-validation -->
## Risks and validation

TECH1: Use AC1 on H5, including browser Back and keyboard. Risk: route/state desynchronization; verify selection across repeated round trips and reload. Existing return tests remain required in change mode. No user-facing feature beyond S1.

<!-- section:implementation-preconditions -->
## Implementation preconditions

TECH1: Not applicable: no pending external asset/dependency prerequisite in this synthetic approved plan.
