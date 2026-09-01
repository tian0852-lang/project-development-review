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

# {{project_name}} — 03-design-spec

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:visual-requirements -->
## Visual requirements

{{stable_item_ids_layout_components_copy_tokens_evidence_decisions_acceptance_and_limits}}

<!-- section:resources -->
## Resources

Use the approved page resource inventory for page-level identity, dimensions and persistence status. This table remains for external dependencies and rights/precondition references; do not treat it as a substitute for `evidence/resource-inventory.md`.

| External dependency ID | Resource | Actual location | Accessibility | Rights / limits | Precondition or plan decision |
| --- | --- | --- | --- | --- | --- |
| {{external_id}} | {{resource}} | {{location}} | {{accessibility}} | {{limits}} | {{condition_or_decision_id}} |
