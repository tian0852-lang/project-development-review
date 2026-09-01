# Evidence and status

Use two independent axes, never one mutually exclusive list.

Evidence kinds: design_observation, repository_observation, user_provided, inference, unreadable. An evidence record includes ID, selected source where relevant, exact node/file/message location, readable scope, limitations, and only actually visible author/time. A screenshot or recording must be attributable to the selected source. Existing code is evidence, not approved product behavior.

Approval states: Draft, Pending confirmation, Approved, Out of scope, Invalidated. Approved artifacts/items reference valid confirmation_events; they must not merely cite evidence. An inferred proposal can become approved through a genuine confirmation covering its stable item ID. Static structure cannot establish resend, navigation parameters, return retention or dialog results.

Keep stable page/specification/technical item IDs with evidence_ids, decision_ids, acceptance_ids, dependencies, platforms and scope. A technical item points to at least one in-scope specification item. Acceptance IDs point back to the covered item IDs. Out-of-scope items cannot reappear as implementation dependencies.

Markdown review-meta blocks contain ID, version, review ID, design source/scope, evidence/limitations, item IDs, dependencies and references to approval status/event IDs in the manifest. Resolve those approval references when presenting the document. Do not duplicate mutable approved state in frozen text.

Only record visible source text, timestamps, owners and message IDs. Null plus a limitation is better than invented precision. Human evidence review remains necessary even when a validator accepts reference structure.
