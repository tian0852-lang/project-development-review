<!-- review-meta
{
  "artifact_id": "DOC-CHANGE-IMPACT",
  "review_id": "REVIEW-change-ready",
  "version": "1",
  "manifest": "../../review-manifest.json",
  "design_source": "Figma",
  "scope_ids": [
    "frame-list",
    "frame-detail"
  ],
  "evidence_ids": [
    "E-USER"
  ],
  "readability_limits": [
    "Synthetic fixture evidence only."
  ],
  "item_ids": [],
  "depends_on": {},
  "approval_status_ref": "#/artifacts/DOC-CHANGE-IMPACT/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-CHANGE-IMPACT/approval_event_ids"
}
-->

# Offline Cards (synthetic) — change_impact

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:impact-classification -->
## Impact classification

CH1: Cross-page because shared selectedId crosses List and Detail; it is not Local merely because the screenshot marks one button.

<!-- section:cross-page-and-global-scan -->
## Cross-page and global scan

All eight areas: {"shared_components": "Existing ListRow used on list only; retain its public input.", "design_tokens": "Reuse existing spacing and color constants; no token change.", "navigation": "List/detail back route remains; dialog does not add a route.", "shared_state": "Selection survives detail/back; confirm clear empties it.", "data_models": "Card ID/title shape unchanged; no persistence.", "permissions": "No permissions introduced; no authentication.", "project_configuration": "Existing browser entry retained; no SDK/dependency changes.", "tests": "Add cancel/confirm regression and preserve existing return test."}

<!-- section:user-decisions -->
## User decisions

DEC-CHANGE records user approval of assessed scope/impact. Unknown impact cannot be made known by approval alone.
