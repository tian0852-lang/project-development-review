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
    "{{pages_artifact_id}}": "{{pages_artifact_version}}"
  },
  "approval_status_ref": "#/artifacts/{{artifact_id}}/approval_status",
  "approval_event_ids_ref": "#/artifacts/{{artifact_id}}/approval_event_ids"
}
-->

# {{project_name}} — resource-inventory

Approval status and event references: resolve review-meta pointers in review-manifest.json; do not rewrite frozen text to update approval.

<!-- section:resource-scope-and-evidence -->
## Resource scope and evidence

Resource inventory version: {{resource_inventory_version}}
Selected design source and exact scope: {{selected_design_source_and_scope}}
Inventory limitations: {{inventory_limitations}}
Historical inventory status: {{historical_inventory_status}}

<!-- section:resource-items -->
## Resource items

| Resource ID | Type | Page ID | Source node / layer | Usage / variant | Original size | Design size | Export / runtime size | Scale | Format | Crop / fit | Location | Rights / access | Evidence IDs | Approval | Save status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{resource_id}} | {{icon_or_image_or_other}} | {{page_id}} | {{source_node_id}} | {{usage_and_variant}} | {{original_dimensions}} | {{design_dimensions}} | {{export_runtime_dimensions}} | {{scale}} | {{format}} | {{crop_fit_or_not_applicable}} | {{actual_location}} | {{rights_accessibility}} | {{evidence_ids}} | {{approval_status}} | {{save_status}} |

<!-- section:page-resource-checkpoint -->
## PAGE & RESOURCE CHECKPOINT

- Candidate page count: {{candidate_page_count}}
- Included page count: {{included_page_count}}
- Resource version: {{resource_inventory_version}}
- Included resources: {{included_resource_ids}}
- Excluded resources and reasons: {{excluded_resource_ids_and_reasons}}
- Save root: {{review_root_assets_path}}
- Open resource decisions and blocking levels: {{open_resource_decision_ids}}
- Evidence and readability limits: {{evidence_and_limits_summary}}

{{request_explicit_confirmation_or_correction_of_pages_resources_scales_dimensions_and_exclusions}}

<!-- section:save-record -->
## Save record

| Resource ID | Approved event | Saved path | SHA-256 | Save status | Conflict / precondition |
| --- | --- | --- | --- | --- | --- |
| {{resource_id}} | {{confirmation_event_id}} | {{saved_path_or_null}} | {{sha256_or_null}} | {{save_status}} | {{conflict_or_precondition}} |
