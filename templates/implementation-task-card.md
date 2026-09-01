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

# {{project_name}} — implementation-task-card

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:approved-version-references -->
## Approved version references

{{spec_version_plan_version_valid_event_ids_targets_and_active_card_ids_from_manifest}}

Approved resource inventory and save records: {{resource_inventory_version_resource_ids_and_review_root_assets_paths}}

<!-- section:baseline-verification -->
## Baseline verification

{{baseline_id_version_read_order_and_pre_execution_verification}}

<!-- section:permitted-work -->
## Permitted work

Use the already approved plan. Do not regenerate or request approval for the same unchanged plan. {{approved_technical_item_ids_and_unblocked_actions}}

<!-- section:blocked-work -->
## Blocked work

{{preconditions_blocked_actions_exclusions_and_affected_scope_stop_rule_if_baseline_or_plan_deviation}}
This review Skill only hands off; downstream implementation requires the user's development authorization.
