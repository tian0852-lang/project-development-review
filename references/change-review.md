# Change and mixed reviews

Read during intake when this round modifies existing implementation, including mixed new/change projects. Create changes/<change-id>/change-request.md and change-impact-report.md; add resource-diff-report.md when the review package has a resource inventory or the change touches design assets. Record real old specs/cards/code/tests and the historical resource inventory; record absent old docs or inventories explicitly instead of fabricating them.

Scan shared components, design tokens, navigation, shared state, data models, permissions, project configuration and tests, plus resource identity, dimensions, formats, page usage, rights and save paths. Classify Local / Cross-page / Global / Unknown with evidence. A small screenshot does not prove Local. Resolve unknowns or exclude affected scope with a recorded decision.

Sequence: identify → build resource baseline/diff when applicable → assess scope/impact → user decisions → confirm the page/resource set → persist confirmed resources or record scoped preconditions → confirm affected specifications → assessment card and change attachment → update plan → confirm plan → implementation card.
change-task-card.md is an attachment only, generated after affected-spec approval. It references change ID, affected spec version, impact report and the standard assessment card (later implementation card via manifest). It grants no independent assessment/implementation authority.

manifest.active_cards contains one assessment ID and one implementation ID (null before plan approval). Changes point to attachment IDs. Keep unaffected old approvals/history; reapprove only impacted content after proper invalidation.
