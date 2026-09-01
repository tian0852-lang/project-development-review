# Conversation output contract — core 2.2.0

This contract defines how the review state must be rendered in the current conversation. It does not add a fourth project gate. A document-only reference is insufficient when a decision or confirmation is due.

## Required panels

At every response after intake, render an `OPEN QUESTIONS PANEL` before asking for user input. Include **all** unresolved decisions, not only the questions selected for this turn:

| Decision ID | Question | Known facts / evidence limits | Affected item IDs | Impact / blocking level | Options | Suggested option and rationale | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Ask for answers to no more than three highest-priority questions in the current turn. The remaining unresolved entries must stay visible with their IDs and status. Never tell the user to search a document instead of showing the pending decision summary. After an answer, restate which IDs, scope items and candidate version the answer changes before updating the manifest.

## Page and resource checkpoint

During `page_inventory` and `page_confirmation`, render a `PAGE & RESOURCE CHECKPOINT` directly in the conversation, even when only one page or no binary resource is detected. It must show:

- candidate page count and included count;
- every candidate's name, exact source ID, size, parent, page/non-page classification and evidence/limits;
- state artboards versus distinct runtime pages;
- `In scope` items (pages and known feature items);
- `Out of scope` items and the reason/evidence;
- unresolved page/scope decisions and their blocking levels;
- every in-scope icon, image, font or illustration grouped by page, with stable Resource ID, source node/layer, original/design/export/runtime dimensions, scale, format, location, rights/accessibility, evidence limits and save status;
- resource additions/removals/modifications for change or mixed mode, including the historical inventory limitation when no prior list exists;
- the review_root/assets save root and any conflict, export or rights precondition;
- the frozen candidate version and the exact response needed to confirm or edit it.

The page gate is not satisfied by a file that merely says `Confirmed`. The user must affirm or correct the displayed count, included/excluded list and resource set/version. A correction creates new candidate versions; it is not approval of the previous version. Resource confirmation is a sub-checkpoint of the page gate, not a fourth project gate.

## Specification scope checkpoint

Before specification confirmation, render a `SPECIFICATION SCOPE CHECKPOINT` with the approved page IDs, in-scope item IDs, explicit exclusions, target platforms, open questions that affect the scope, and the candidate specification version. The specification confirmation event must bind both included and excluded IDs. Do not create the assessment card until this displayed scope is affirmed.

## Rendering order and fallback

Use this order: stage/read summary → required checkpoint panel(s) → all pending questions → permitted artifacts → one concise next decision. The panels are required in text-only fallback output as well. If filesystem or native Skill access is unavailable, label the delivery as `Text-only delivery / not filesystem-validated`; do not hide the panels behind a path that the user cannot read.
