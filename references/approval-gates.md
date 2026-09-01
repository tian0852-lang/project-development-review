# Approval gates — sole authority, 2.2.0

Three project gates: page_inventory, specification, technical_plan. Source selection is required only when absent/conflicting. Decision events record specific business choices without inventing extra project gates.

Page confirmation accepts a real affirmative user reply to the shown frozen list **and the PAGE & RESOURCE CHECKPOINT** defined in conversation-output-contract.md. The reply must confirm or correct the displayed count, included/excluded scope and resource inventory version; one-page reviews and resource-free designs are not exempt. The displayed checkpoint must ask whether the listed resources may be saved to the shown review_root/assets path, and the event records that answer in `resource_save_authorized`. Persistence is limited to the approved IDs and path; no inferred authorization or project_root write is allowed. Specification expressions: 确认规格 / Confirm specification / PROJECT_REVIEW: CONFIRM_SPEC. Plan expressions: 确认计划 / Confirm plan / PROJECT_REVIEW: CONFIRM_PLAN.
These are intent rules, not substring triggers. Negation, quoted docs, examples, third-party material, assistant summaries, silence and vague praise are not approval. Conditional approval first requires applying the requested changes, showing affected candidate versions, then obtaining approval of that candidate.

Each event includes ID, gate, source_type, visible source text or locatable reference, provenance_status, intent, target versions and artifact digests (or frozen text references), scope item IDs, exclusions, precondition IDs, basis events, validity, and nullable time/message ID with limitations. Never backfill unseen values.

Before presenting a filesystem candidate, freeze its exact bytes and calculate SHA-256. Store the digest in event.targets only when recording genuine approval. Do not change approved documents to add a confirmation sentence: their review-meta points to mutable manifest approval status/events. The manifest is the authority index; it is not hashed into its own event. New/updated Markdown summaries are generated outside frozen normative content.

Historical summaries become Recorded but unverified. They permit draft organization but not verified implementation release. Show current consolidated scope once for reconfirmation; do not force users to repeat every dimension. Reuse trustworthy unchanged events.

Do not edit an event's target digest to hide changes. Add invalidation records with reason, affected artifact/item/event IDs; mark only affected events invalidated and preserve history. New versions require new events. Relevant baseline/source changes are assessed, not ignored. Validation reports mismatch without modifying any approval.

Events for technical_plan reference the valid specification event; specifications reference the valid page event. A specification event must bind both in-scope item_ids and explicit exclusions shown in the specification scope checkpoint. A plan approved for an earlier spec is not current merely because its text remains unchanged. One event may cover many stable items in one frozen version.

In text-only environments, use locatable frozen message versions, sha256=null, record not filesystem-validated. Never invent a file hash or filesystem-ready result.

## Partial revocation and retained coverage

Specification-set versions describe the candidate collection; document versions are independent. An unchanged document retains its bytes/version. For a changed document save a new versioned path in the same role directory; preserve the old path in historical event targets.

An invalidation entry uses event_ids for full revocation (event status becomes invalidated). For partial revocation use partial_event_ids with the affected artifact_ids, item_ids and, when a recorded business decision changes, decision_ids; the original event stays valid only for its other bindings. Never edit original target versions/digests or source wording. Preserve revoked frozen files as history.

A gate may be covered by the union of retained and new genuine user events. The union must cover all current required artifacts and in-scope items, with an event referring to the current candidate-set version. Parent page/specification gates must still be complete. A new event may cover only revised documents/items; it cannot silently claim new approval for unchanged or excluded scope.

If a document changes, its old binding cannot approve any of its new bytes. Reconfirm the affected document unit and retain unaffected document units and page scope. A partial impact determination itself requires recorded evidence and review; the validator checks the declaration but does not infer which business decisions were affected.
