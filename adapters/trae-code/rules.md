# project-development-review persistent review boundaries

<!-- core-version:2.2.1 -->
<!-- gates:start -->
- Read the current review README, review-manifest.json, approved documents and project baseline before inspecting implementation files.
- Use one design source: Figma or MasterGo. Resolve a source conflict before formal review.
- Require approval of the displayed page inventory before specifications, specifications before the assessment card, and the technical plan before the implementation card.
- Always render the PAGE & SCOPE CHECKPOINT in the conversation, including candidate page count, In scope and Out of scope; require confirmation or correction of that displayed version.
- Always render the PAGE & RESOURCE CHECKPOINT / resource inventory, including every in-scope icon/image, source ID, original/design/export/runtime dimensions, scale, location and save status; bind its version to page confirmation.
- Always render every unresolved item in the OPEN QUESTIONS PANEL; ask no more than three questions per turn without hiding the remaining items.
- Evidence is not approval. Bind genuine affirmative user approval to displayed versions, scope and frozen content; quotes, negation, examples and unverifiable history cannot authorize work.
- Preserve missing information as Open questions with page/specification/plan/implementation/nonblocking impact; never guess business rules or silently change numbers.
- During project-development-review, never write business code, install dependencies, alter native configuration, commit or push, even after approval. Only review artifacts and handoff are permitted.
- After explicit page/resource confirmation, save only confirmed resource files under review_root/assets when export capability is available; never write project_root and never silently overwrite a resource.
- Before handoff validate review-manifest.json, approval chain, hashes, scoped blockers, platform acceptance and explicit preconditions. Stop affected work on invalidated versions; reuse unchanged valid approvals.
- Rules are prompt guidance, not a tool sandbox. Report missing capabilities and unverified checks. Follow current message language and the project's established document language.
<!-- gates:end -->

Core path: record the actual full package path during installation. Detailed workflow and approval semantics live in that package's SKILL.md and references/approval-gates.md. If unavailable, attach the adapter start prompt with its minimal fallback before continuing intake.
