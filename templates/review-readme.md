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

# {{project_name}} — review-readme

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- review-summary
{
  "stage": "{{stage}}",
  "versions": {
    "pages": "{{pages_version}}",
    "specification": "{{spec_version}}",
    "plan": "{{plan_version}}",
    "resources": "{{resources_version}}"
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

<!-- section:current-stage -->
## Current stage

{{review_id}} — stage {{stage}}. Source of truth: review-manifest.json. Root paths and external dependencies must be distinguished.

<!-- section:next-action -->
## Next action

{{next_step_and_required_user_decision}}

<!-- section:decision-summary -->
## Decision summary

{{render_manifest_decisions_with_ids_status_blocking_level_affected_scope_and_approval_refs}}
