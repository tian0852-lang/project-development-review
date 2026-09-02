# Artifact contract — 2.2.1

review-manifest.json is the single machine index. The schema defines exact keys/enums; x-contract defines stage keys, required roles, templates and metadata. Specifications remain the normative text at indexed versions.

## Roots and paths
review_root is the delivery root ('.' means the supplied root for portability); project_root is external and nullable. They must differ. Artifact paths are unique, relative and contained in review_root; use role paths in x-contract, or versioned filenames in the same role directory. Replace <change-id> in change paths. Confirmed resource files are relative to `assets/<resource-id>/<scale>/`, where scale is an explicit value such as `1x`, `2x` or `3x`, and never project_root. External dependencies must declare location/accessibility/evidence. Links outside the review must be labeled external and registered; never silently point to another review.

## Stage requirements
Intake creates README, manifest and baseline. Source adds design-source; inventory adds pages and the required resource inventory when enabled. After page/resource confirmation, resource persistence writes only authorized files or records access/rights/conflict conditions. Specification then adds decisions and all seven specs. From specification_preflight all seven are complete. Only valid spec approval unlocks assessment_card; technical_plan adds plan. Only valid plan approval unlocks implementation_card, approval_record and handoff. Final handoff_validation adds validation_report. Early missing future artifacts are not failures; premature authority-bearing cards are.
Change/mixed adds request at intake, impact and resource-diff report at specification, and an attachment after affected-spec approval. active_cards contains one assessment ID and one implementation ID; the latter remains null before plan approval.

## Markdown metadata
Every indexed Markdown artifact starts with a review-meta JSON HTML comment. Fields are listed in x-contract.metadata_fields. The manifest path is relative to that file; approval_status_ref and approval_event_ids_ref use JSON pointers such as '#/artifacts/SPEC-00/approval_status'. Resolve them for presentation, so approved text remains immutable while approval state can change in the index.
Version, review ID, source/scope, evidence, item IDs and dependencies must agree with the manifest. Real content may translate headings, but retain section marker IDs (<!-- section:... -->) from templates for language-neutral validation. Every spec/technical item appears in its artifact text and metadata.

README, decision-register and validation-report carry a review-summary JSON comment containing stage, versions, decision_states and active_cards synchronized from the manifest. decision_states uses x-contract.decision_summary_fields: question, status, blocking_level, affected_item_ids, user_decision, approval_event_ids and precondition_id. Other prose summaries require human consistency review. Normative frozen documents have no mutable summary block.

## Completion and authority
All in-scope spec/technical items have stable IDs, evidence, decision/acceptance links and approval events. Technical items depend on spec items. An Approved record without a valid covering event is invalid. No auto-transfer from v1 Confirmed.
Each document evidence index includes its items' evidence IDs. IDs must be nonblank and JSON-pointer-safe, without slash or tilde; use stable labels rather than editable titles.
Completed output has real content or 'Not applicable' with a reason. Templates may have placeholders, delivered complete documents may not.
versions.specification is the frozen specification-set version, not a requirement to renumber every unchanged spec file. Pages and plan have their own candidate versions; individual artifact.version values identify exact document bytes.
Text-only environments supply full Markdown and manifest drafts, frozen message references and null hashes; label Text-only delivery / not filesystem-validated.

## Schema and validator
The standard-library validator implements only local $ref, type, required, properties, additionalProperties, enum, const, pattern, minLength, minItems, uniqueItems, items and anyOf from this schema. It is not a general JSON Schema engine. Semantic checks layer on top; neither layer proves genuine user intent.

## Role and template index

The rows are mirrored by x-contract.roles; do not maintain a second path scheme. Versioned names are allowed within the same role directory.

| Role | Default review-relative path | Template | First required stage |
| --- | --- | --- | --- |
| review_readme | `README.md` | [review-readme.md](../templates/review-readme.md) | intake |
| baseline | `evidence/project-baseline.md` | [project-baseline.md](../templates/project-baseline.md) | intake |
| design_source | `evidence/design-source.md` | [design-source.md](../templates/design-source.md) | source_validation |
| pages | `evidence/page-inventory.md` | [page-inventory.md](../templates/page-inventory.md) | page_inventory |
| resource_inventory | `evidence/resource-inventory.md` | [resource-inventory.md](../templates/resource-inventory.md) | page_inventory |
| decisions | `decisions/decision-register.md` | [decision-register.md](../templates/decision-register.md) | specification |
| spec0 | `specs/00-product-brief.md` | [00-product-brief.md](../templates/00-product-brief.md) | specification |
| spec1 | `specs/01-scope-and-priority.md` | [01-scope-and-priority.md](../templates/01-scope-and-priority.md) | specification |
| spec2 | `specs/02-user-flow-and-states.md` | [02-user-flow-and-states.md](../templates/02-user-flow-and-states.md) | specification |
| spec3 | `specs/03-design-spec.md` | [03-design-spec.md](../templates/03-design-spec.md) | specification |
| spec4 | `specs/04-data-and-privacy.md` | [04-data-and-privacy.md](../templates/04-data-and-privacy.md) | specification |
| spec5 | `specs/05-acceptance-and-test.md` | [05-acceptance-and-test.md](../templates/05-acceptance-and-test.md) | specification |
| spec6 | `specs/06-design-difference-log.md` | [06-design-difference-log.md](../templates/06-design-difference-log.md) | specification |
| assessment_card | `technical/technical-assessment-task-card.md` | [technical-assessment-task-card.md](../templates/technical-assessment-task-card.md) | technical_assessment |
| plan | `technical/technical-implementation-plan.md` | [technical-implementation-plan.md](../templates/technical-implementation-plan.md) | technical_plan |
| implementation_card | `handoff/implementation-task-card.md` | [implementation-task-card.md](../templates/implementation-task-card.md) | handoff |
| approval_record | `handoff/implementation-approval-record.md` | [implementation-approval-record.md](../templates/implementation-approval-record.md) | handoff |
| handoff | `handoff/developer-handoff.md` | [developer-handoff.md](../templates/developer-handoff.md) | handoff |
| validation_report | `validation/validation-report.md` | [validation-report.md](../templates/validation-report.md) | handoff_validation |
| change_request | `changes/<change-id>/change-request.md` | [change-request.md](../templates/change-request.md) | intake |
| change_impact | `changes/<change-id>/change-impact-report.md` | [change-impact-report.md](../templates/change-impact-report.md) | specification |
| change_resource_diff | `changes/<change-id>/resource-diff-report.md` | [resource-diff-report.md](../templates/resource-diff-report.md) | specification |
| change_attachment | `changes/<change-id>/change-task-card.md` | [change-task-card.md](../templates/change-task-card.md) | technical_assessment |

Use [manifest template](../templates/review-manifest.json) and [JSON Schema](../schemas/review-manifest.schema.json) for exact object shapes. Arrays and ID maps may be empty at an early phase where their items are not yet known; completed final artifacts must meet the role and stable-item contract.
