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

# {{project_name}} — decision-register

Approval status and event references: resolve review-meta pointers in the manifest; do not rewrite frozen text to update approval.

<!-- review-summary
{
  "stage": "{{stage}}",
  "versions": {
    "pages": "{{pages_version}}",
    "specification": "{{spec_version}}",
    "plan": "{{plan_version}}"
  },
  "decision_states": {
    "{{decision_id}}": {
      "status": "{{status}}",
      "blocking_level": "{{blocking_level}}",
      "affected_item_ids": [
        "{{item_id}}"
      ],
      "question": "{{question}}",
      "user_decision": "{{user_decision_or_null}}",
      "approval_event_ids": [
        "{{approval_event_id}}"
      ],
      "precondition_id": "{{precondition_id_or_null}}"
    }
  },
  "active_cards": {
    "assessment_id": "{{assessment_id_or_null}}",
    "implementation_id": "{{implementation_id_or_null}}"
  }
}
-->

<!-- section:decision-summary -->
## Decision summary

{{render_all_decision_ids_status_blocking_level_affected_items_and_event_references_from_manifest}}

<!-- section:open-questions-panel -->
## OPEN QUESTIONS PANEL (render all unresolved entries in the conversation)

{{render_all_unresolved_questions_with_facts_evidence_limits_impact_options_recommendation_and_status;_ask_at_most_three_this_turn_but_do_not_hide_the_rest}}

<!-- section:decision-details -->
## Decision details

| Decision ID | Question | Facts / evidence | Affected scope | Options | Recommendation / rationale | Blocking level / reason | Owner | User decision | Event |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{decision_id}} | {{question}} | {{facts}} | {{affected_ids}} | {{options}} | {{recommendation}} | {{blocking}} | {{owner_or_null}} | {{decision_or_unresolved}} | {{event_or_none}} |
