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

# {{project_name}} — change-impact-report

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:impact-classification -->
## Impact classification

{{Local_Cross_page_Global_Unknown_evidence_and_affected_item_ids}}

<!-- section:cross-page-and-global-scan -->
## Cross-page and global scan

{{shared_components_design_tokens_navigation_shared_state_data_models_permissions_project_configuration_tests_findings}}

<!-- section:user-decisions -->
## User decisions

{{decision_ids_approved_scope_resolution_unknowns_or_explicit_exclusion_event_ids}}
