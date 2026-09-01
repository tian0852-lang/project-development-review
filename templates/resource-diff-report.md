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
  "item_ids": [],
  "depends_on": {
    "{{resource_inventory_artifact_id}}": "{{resource_inventory_version}}"
  },
  "approval_status_ref": "#/artifacts/{{artifact_id}}/approval_status",
  "approval_event_ids_ref": "#/artifacts/{{artifact_id}}/approval_event_ids"
}
-->

# {{project_name}} — resource-diff-report

Approval status and event references: resolve review-meta pointers in review-manifest.json.

<!-- section:resource-baseline -->
## Resource baseline

Previous review ID / inventory version: {{previous_review_and_inventory_version}}
Current inventory version: {{current_inventory_version}}
Historical limitations: {{historical_limitations}}

<!-- section:resource-differences -->
## Resource differences

| Resource ID | Previous evidence / path | Current evidence / path | Status | Page / component impact | Dimension / format change | Decision ID | Reconfirmation required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{resource_id}} | {{previous_reference}} | {{current_reference}} | {{unchanged_new_modified_removed_moved_unknown}} | {{impact}} | {{change}} | {{decision_id}} | {{yes_or_no_and_reason}} |

<!-- section:resource-impact-decision -->
## Resource impact decision

{{cross_page_global_scan_and_user_decision_references}}
