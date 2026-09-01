<!-- review-meta
{
  "artifact_id": "DOC-APPROVAL-RECORD",
  "review_id": "REVIEW-change-ready",
  "version": "1",
  "manifest": "../review-manifest.json",
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
  "approval_status_ref": "#/artifacts/DOC-APPROVAL-RECORD/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-APPROVAL-RECORD/approval_event_ids"
}
-->

# Offline Cards (synthetic) — approval_record

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- section:approval-event-references -->
## Approval event references

EV-PAGES, EV-SPEC and EV-PLAN refer to synthetic-transcript.md and frozen target bytes in manifest. These are fixture approvals only.

<!-- section:scope-and-exclusions -->
## Scope and exclusions

Only PG1/PG2, SP0–SP6 and TECH1. Exclusions: login/network/native ports. No implementation preconditions.
