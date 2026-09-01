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

# {{project_name}} — 05-acceptance-and-test

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:platform-coverage -->
## Platform coverage

{{each_target_platform_with_environment_and_acceptance_ids_including_nonapplicable_reason_if_excluded}}

<!-- section:acceptance-cases -->
## Acceptance cases

| Acceptance ID | Item IDs | Platforms | Steps | Expected result | Environment | Required evidence |
| --- | --- | --- | --- | --- | --- | --- |
| {{acceptance_id}} | {{item_ids}} | {{platforms}} | {{steps}} | {{expected}} | {{environment}} | {{evidence}} |
