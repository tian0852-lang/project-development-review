<!-- review-meta
{
  "artifact_id": "{{artifact_id}}",
  "review_id": "{{review_id}}",
  "version": "{{artifact_version}}",
  "manifest": "{{relative_manifest_path}}",
  "design_source": "{{selected_design_source}}",
  "scope_ids": [
    "{{scope_id}}"
  ],
  "evidence_ids": [
    "{{evidence_id}}"
  ],
  "readability_limits": [
    "{{readability_limit}}"
  ],
  "item_ids": [
    "{{item_id}}"
  ],
  "depends_on": {
    "{{dependency_artifact_id}}": "{{dependency_version}}"
  },
  "approval_status_ref": "#/artifacts/{{artifact_id}}/approval_status",
  "approval_event_ids_ref": "#/artifacts/{{artifact_id}}/approval_event_ids"
}
-->

# {{project_name}} — 02-user-flow-and-states

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:interaction-evidence -->
## Interaction evidence

| Item ID | Source page / node | Control | Trigger | Action | Destination | Transition | Evidence | Readability / limits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{item_id}} | {{page_and_node}} | {{control}} | {{trigger}} | {{action}} | {{destination}} | {{transition}} | {{evidence_id}} | {{limits}} |

<!-- section:navigation -->
## Navigation

{{source_trigger_destination_parameters_return_and_retained_state_per_item_with_decision_and_acceptance_ids}}

<!-- section:dialogs -->
## Dialogs

{{trigger_type_title_body_buttons_each_outcome_overlay_back_close_and_confirm_cancel_state_effect_per_item_or_not_applicable_with_reason}}

<!-- section:states-and-recovery -->
## States and recovery

{{normal_waiting_success_failure_recovery_main_flow_and_acceptance_ids_no_invented_states}}
