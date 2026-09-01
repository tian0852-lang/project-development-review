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

# {{project_name}} — technical-implementation-plan

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:file-changes -->
## File changes

| Technical item ID | Real / proposed path | Create / modify / reuse / replace | Responsibility | Spec dependency IDs | Acceptance IDs |
| --- | --- | --- | --- | --- | --- |
| {{technical_item_id}} | {{path}} | {{action}} | {{responsibility}} | {{spec_ids}} | {{acceptance_ids}} |

<!-- section:initialization-and-configuration -->
## Initialization and configuration

{{new_project_bootstrap_project_configuration_dependencies_resources_and_native_settings_to_be_changed_by_downstream_only_or_not_applicable_reason}}

Resource delivery: {{approved_resource_ids_save_paths_scale_folders_and_conflicts_or_preconditions}}

<!-- section:state-and-interaction -->
## State and interaction

{{state_data_navigation_parameters_return_retention_dialog_results_and_no_eval_local_logic}}

<!-- section:risks-and-validation -->
## Risks and validation

{{compatibility_regression_technical_options_recommended_selection_and_each_platform_validation}}

<!-- section:implementation-preconditions -->
## Implementation preconditions

{{condition_ids_blocked_item_ids_actions_resolution_tests_and_whether_solution_changes}}
