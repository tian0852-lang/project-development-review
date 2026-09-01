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

# {{project_name}} — technical-assessment-task-card

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:read-only-authority -->
## Read-only authority

This card authorizes read-only technical analysis and plan drafting only. It does not authorize code, dependency, native configuration or Git writes.

<!-- section:required-reads -->
## Required reads

{{approved_spec_event_id_spec_version_artifact_ids_baseline_and_README_paths_then_source_scope}}

<!-- section:expected-plan -->
## Expected plan

{{required_file_actions_components_state_data_navigation_dialogs_initialization_risks_acceptance_and_preconditions}}
