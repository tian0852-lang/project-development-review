<!-- review-meta
{
  "artifact_id": "IMPLEMENT-1",
  "review_id": "REVIEW-change-ready",
  "version": "1",
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
    "PLAN-1": "T1"
  },
  "approval_status_ref": "#/artifacts/IMPLEMENT-1/approval_status",
  "approval_event_ids_ref": "#/artifacts/IMPLEMENT-1/approval_event_ids"
}
-->

# Offline Cards (synthetic) — implementation_card

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:approved-version-references -->
## Approved version references

Reuse S1, T1, EV-SPEC and EV-PLAN with the indexed frozen hashes. Do not regenerate or reconfirm the same unchanged plan.

<!-- section:baseline-verification -->
## Baseline verification

Downstream verifies baseline and digests. Stop affected work if the repository, business scope or proposed implementation deviates; return for impact review.

<!-- section:permitted-work -->
## Permitted work

TECH1 only, H5 only, exact indexed plan file scope. This Skill hands off and performs no development.

<!-- section:blocked-work -->
## Blocked work

TECH1: No current condition. All out-of-scope login/network/native/Git actions remain unauthorized by this review.
