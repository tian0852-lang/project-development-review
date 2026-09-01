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

# {{project_name}} — design-source

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:selected-source -->
## Selected source

Tool: {{Figma_or_MasterGo}}
Link: {{design_link}}
Exact scope: {{node_or_artboard_ids}}
Other supplied source excluded: {{excluded_source_or_not_applicable_reason}}

<!-- section:readable-capabilities -->
## Readable capabilities

{{actual_tool_calls_returned_fields_screenshot_location_readable_range_and_limitations}}

<!-- section:supplementary-evidence -->
## Supplementary evidence

| Evidence ID | Kind | Location / exact node | Readable scope | Limitations | Visible author / time |
| --- | --- | --- | --- | --- | --- |
| {{evidence_id}} | {{kind}} | {{location}} | {{scope}} | {{limits}} | {{visible_values_or_null}} |
