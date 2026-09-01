<!-- review-meta
{
  "artifact_id": "DOC-SPEC2",
  "review_id": "REVIEW-change-ready",
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
    "SP2"
  ],
  "depends_on": {},
  "approval_status_ref": "#/artifacts/DOC-SPEC2/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-SPEC2/approval_event_ids"
}
-->

# Offline Cards (synthetic) — spec2

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:interaction-evidence -->
## Interaction evidence

SP2 / INT1: frame-list, Open button, click, user-provided NAVIGATE intent, frame-detail, no animation, E-USER, readable as user instruction; see approval pointers. Prototype data unavailable.

<!-- section:navigation -->
## Navigation

SP2: Source List; Open chosen card -> Detail; parameter cardId must match the static list. Visible Back or browser Back returns to List with selected ID retained. Invalid ID shows a local error with Back, no network.

<!-- section:dialogs -->
## Dialogs

SP2 / DIALOG1: Clear button opens confirmation. Title Clear selection? Body This only clears the current choice. Cancel keeps it; Clear empties it. Overlay, close button and Escape cancel. Browser Back dismisses the dialog first and stays on List. No secret default action.

<!-- section:states-and-recovery -->
## States and recovery

SP2: Initial no choice; chosen card; detail; dialog; empty after confirm; invalid-ID error/recovery. Waiting/network success/failure Not applicable because no asynchronous request is in scope.
