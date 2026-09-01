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

# {{project_name}} — validation-report

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- review-summary
{
  "stage": "{{stage}}",
  "versions": {
    "pages": "{{pages_version}}",
    "specification": "{{spec_version}}",
    "plan": "{{plan_version}}"
  },
  "decision_states": {
    "{{decision_id}}": {
      "status": "{{status}}",
      "blocking_level": "{{blocking_level}}",
      "affected_item_ids": [
        "{{item_id}}"
      ],
      "question": "{{question}}",
      "user_decision": "{{user_decision_or_null}}",
      "approval_event_ids": [
        "{{approval_event_id}}"
      ],
      "precondition_id": "{{precondition_id_or_null}}"
    }
  },
  "active_cards": {
    "assessment_id": "{{assessment_id_or_null}}",
    "implementation_id": "{{implementation_id_or_null}}"
  }
}
-->

<!-- section:automatic-passed -->
## Automatic passed

{{automatic_check_results_and_tool_command_stage}}

<!-- section:manual-verified -->
## Manual verified

{{recorded_human_check_ids_actual_evidence_reviewer_when_visible_and_limits}}

<!-- section:unverified -->
## Unverified

{{unverified_provenance_semantics_design_connections_client_runtime_and_text_only_limitations}}

<!-- section:repair-path -->
## Repair path

{{smallest_repair_path_without_fabricating_approval_or_rehashing_old_events}}
