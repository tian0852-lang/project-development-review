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

# {{project_name}} — project-baseline

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- section:work-units -->
## Work units

| Work unit ID | New / change | Target platform | Current or proposed path | Evidence |
| --- | --- | --- | --- | --- |
| {{unit_id}} | {{operation}} | {{platform}} | {{path}} | {{evidence_id}} |

<!-- section:repository-evidence -->
## Repository evidence

Project root: {{project_root_or_null_reason}}
README/revision: {{visible_readme_paths_and_revision_or_limitations}}
Baseline ID/version: {{baseline_id_and_version}}
Readable implementation and platform facts: {{observations}}
External dependencies: {{external_ids}}

<!-- section:missing-history -->
## Missing history

{{existing_specs_cards_tests_or_explicit_absence_and_current_baseline_alternative}}
