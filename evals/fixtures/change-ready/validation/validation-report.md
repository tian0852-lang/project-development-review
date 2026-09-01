<!-- review-meta
{
  "artifact_id": "DOC-VALIDATION-REPORT",
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
  "depends_on": {},
  "approval_status_ref": "#/artifacts/DOC-VALIDATION-REPORT/approval_status",
  "approval_event_ids_ref": "#/artifacts/DOC-VALIDATION-REPORT/approval_event_ids"
}
-->

# Offline Cards (synthetic) — validation_report

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

<!-- section:automatic-passed -->
## Automatic passed

Automated result must come from a validator run; this is the expected complete fixture output, not a record of client execution.

<!-- section:manual-verified -->
## Manual verified

Synthetic attestations in evidence/synthetic-audit.md exercise required provenance/meaning/design/impact checks.

<!-- section:unverified -->
## Unverified

No real client, design connector, browser test or human signature.

<!-- section:repair-path -->
## Repair path

Not applicable for the valid fixture: validator-negative variants document specific repairs.
