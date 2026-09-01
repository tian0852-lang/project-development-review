<!-- review-meta
{
  "artifact_id": "DOC-DECISIONS",
  "review_id": "REVIEW-mixed-ready",
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
  "depends_on": {},
  "approval_status_ref": "#/artifacts/DOC-DECISIONS/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-DECISIONS/approval_event_ids"
}
-->

# Offline Cards (synthetic) — decisions

Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.

<!-- review-summary
{
  "stage": "handoff_validation",
  "versions": {
    "pages": "P1",
    "specification": "S1",
    "plan": "T1",
    "resources": "R1"
  },
  "active_cards": {
    "assessment_id": "ASSESS-1",
    "implementation_id": "IMPLEMENT-1"
  },
  "decision_states": {
    "DEC-FLOW": {
      "question": "Should cancel preserve selection?",
      "status": "resolved",
      "blocking_level": "specification",
      "affected_item_ids": [
        "SP2"
      ],
      "user_decision": "Cancel preserves selection; confirm clears it.",
      "approval_event_ids": [
        "EV-SPEC"
      ],
      "precondition_id": null
    },
    "DEC-CHANGE": {
      "question": "Approve assessed change scope and existing behavior to preserve?",
      "status": "resolved",
      "blocking_level": "specification",
      "affected_item_ids": [
        "SP2",
        "TECH1"
      ],
      "user_decision": "Preserve old list return behavior and add only the confirmed clear dialog.",
      "approval_event_ids": [
        "EV-SPEC"
      ],
      "precondition_id": null
    }
  }
}
-->

<!-- section:decision-summary -->
## Decision summary

The machine summary below is authoritative for statuses; narrative must agree.

<!-- section:decision-details -->
## Decision details

DEC-FLOW: Cancel preserves selection; confirm clears it. Evidence E-USER, affected SP2, no silent default. DEC-CHANGE approves the reviewed Cross-page change impact.

<!-- section:open-questions-panel -->
## Open questions panel

No unresolved decision is hidden from the conversation; synthetic entries are fixture evidence only.
