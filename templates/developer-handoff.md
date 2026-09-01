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

# {{project_name}} — developer-handoff

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:delivery-status -->
## Delivery status

{{Ready_or_Ready_with_preconditions_or_Not_ready_from_validation_and_explanation}}

<!-- section:approved-version-references -->
## Approved version references

{{manifest_relative_path_active_assessment_and_implementation_card_ids_spec_plan_versions_event_ids}}

<!-- section:downstream-procedure -->
## Downstream procedure

Read indexed approved documents before code; verify baseline and prerequisites. Execute only authorized unblocked scope. Do not reapprove an unchanged plan. Stop affected work on baseline/scope changes and return to review. The Skill never implements.
