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

# {{project_name}} — 01-scope-and-priority

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:included-scope -->
## Included scope

| Item ID | Requirement | Priority | Platforms | Evidence IDs | Decision IDs | Acceptance IDs |
| --- | --- | --- | --- | --- | --- | --- |
| {{spec_item_id}} | {{requirement}} | {{priority}} | {{platforms}} | {{evidence}} | {{decisions}} | {{acceptance}} |

<!-- section:exclusions -->
## Exclusions

{{explicit_excluded_item_ids_reason_and_user_decision_reference}}

<!-- section:scope-confirmation-checkpoint -->
## Scope confirmation checkpoint

In scope item IDs: {{in_scope_item_ids}}

Out of scope item IDs and reasons: {{out_of_scope_item_ids_and_reasons}}

Target platforms: {{target_platforms}}

User-facing confirmation text/reference and specification version: {{scope_confirmation_event_reference}}
