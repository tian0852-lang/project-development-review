# Decisions and preconditions

Render every unresolved decision in the conversation using [conversation-output-contract.md](conversation-output-contract.md). The three-question-per-turn limit controls which entries request an answer now; it never permits hiding the remaining entries in a document.

A decision has ID, question, facts, evidence_ids, affected_item_ids, options, recommendation, rationale, blocking_level, owner when known, status, user_decision and approval_event_ids.

blocking_level: page_scope, specification, plan, implementation, nonblocking, out_of_scope. Explain the effect and affected IDs. An unresolved decision outside approved scope does not block the whole package; an unknown fact affecting approved scope does. Exclusions require explicit resolution/approval, not silent removal.

Preserve user business numbers exactly. Contradictory durations or agreement/button rules need user judgment. Technical plan drafts may propose new architecture, components, SDKs or file changes and be approved once as a plan; do not require all proposals to be approved before drafting.

Ready with preconditions requires valid spec and plan approvals, no page/spec/plan blockers and conditions which do not change the approved solution. Each pending implementation condition specifies blocked item IDs/actions and a verifiable resolution test. An unavailable known font file can be such a condition; undecided font family/license/layout is a plan blocker. External assets are not absent merely because not copied: record location, accessibility and evidence. An alternative font cannot be silently substituted.

Unknown impact must be investigated or affected scope explicitly excluded. A bare user agreement does not make unknown facts known.
