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

# {{project_name}} — page-inventory

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:candidate-pages -->
## Candidate pages

Included count: {{count}}
| Page item ID | Name | Source node ID | Size | Parent | Page / non-page | Included | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{page_item_id}} | {{name}} | {{node}} | {{size}} | {{parent}} | {{type}} | {{scope}} | {{evidence_id}} |

<!-- section:confirmation-candidate -->
## Confirmation candidate

Version: {{pages_version}}
### PAGE & SCOPE CHECKPOINT (render this block in the conversation)

- Candidate page count: {{candidate_page_count}}
- Included count: {{included_count}}
- In scope: {{in_scope_page_and_feature_ids}}
- Out of scope: {{out_of_scope_page_and_feature_ids_with_reason}}
- State artboards versus runtime pages: {{state_artboard_classification}}
- Open page/scope decisions: {{open_page_scope_decision_ids_and_blocking_levels}}
- Evidence and readability limits: {{evidence_and_limits_summary}}
- Page resource inventory: {{resource_inventory_artifact_id_and_version}}
- Resource scope and save status: {{included_excluded_resource_ids_and_open_resource_conditions}}

{{request_explicit_confirmation_or_correction_of_count_pages_resources_and_inclusions_exclusions}}
