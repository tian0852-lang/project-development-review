# Workflow — core 2.2.0

The stage keys below are normative. At each stage, read the listed references completely before generating its artifacts. Only advance after the exit evidence is available. Never bulk-create future handoff documents for directory completeness.

| Stage | Required reads (in references/) | Permitted output | Exit evidence |
| --- | --- | --- | --- |
| intake | intake-and-baseline.md, artifact-contract.md, evidence-and-status.md, output-language-policy.md, conversation-output-contract.md | README, manifest, baseline, decisions | Goal, mode, roots, language and limitations recorded |
| source_validation | design-source-boundary.md, selected figma.md or mastergo.md | design-source | One selected source, precise review scope |
| page_inventory | page-inventory.md, resource-inventory.md, prototype-and-annotation-reading.md, conversation-output-contract.md | page-inventory and resource-inventory drafts plus PAGE & RESOURCE CHECKPOINT | Candidates, resource rows, count, in/out scope and evidence rendered in chat |
| page_confirmation | approval-gates.md, resource-inventory.md, conversation-output-contract.md | Frozen page/resource candidates and confirmation event | Explicit approval of shown count/list/resource set/scope version |
| resource_persistence | resource-persistence.md, artifact-contract.md, conversation-output-contract.md | Saved-resource records or explicit unavailable/precondition report | Confirmed resources are saved under review_root/assets immediately after the checkpoint when capability and rights allow; conflicts and limits are recorded |
| specification | specification-review.md, decision-policy.md, conversation-output-contract.md | Seven specs and decision register | Scoped business questions resolved/excluded and OPEN QUESTIONS PANEL rendered |
| specification_preflight | handoff-validation.md, conversation-output-contract.md | Validation results, candidate summary | Complete seven specs, target platforms, no scope blockers and scope checkpoint shown |
| specification_confirmation | approval-gates.md, conversation-output-contract.md | Specification event | Valid event bound to frozen version/content and included/excluded scope |
| technical_assessment | technical-assessment.md, intake-and-baseline.md, conversation-output-contract.md | One technical-assessment-task-card | Approved spec and baseline available; open questions shown |
| technical_plan | technical-assessment.md, decision-policy.md, conversation-output-contract.md | Plan draft with technical proposals | Files, state, validation and conditions assessable; open questions shown |
| technical_plan_preflight | handoff-validation.md, conversation-output-contract.md | Validation results, candidate summary | No scoped page/spec/plan blockers and open questions rendered |
| technical_plan_confirmation | approval-gates.md, conversation-output-contract.md | Plan event | Valid plan approval with exact scope/content and open questions shown |
| handoff | artifact-contract.md, change-review.md when applicable, conversation-output-contract.md | Implementation card, approval record, handoff | Same approved versions, resource set and unique card IDs |
| handoff_validation | handoff-validation.md, conversation-output-contract.md | Final validation-report | Ready / Ready with preconditions / Not ready; final questions visible |

For change/mixed mode, read change-review.md during intake and maintain request/impact artifacts through specification. Generate the change attachment only after affected specifications are approved. It is not another authority.

Recover at the earliest affected stage, not at intake by default. Keep history and unaffected approvals. A content hash mismatch is not repaired by rehashing an old event. Diagnose impact, invalidate affected event IDs, present a new candidate and seek necessary approval. A later declared stage never proves earlier approval.

Use artifact-contract.md for exact paths, evidence-and-status.md for data meanings, and approval-gates.md as the only confirmation authority.
