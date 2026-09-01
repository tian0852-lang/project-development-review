# Changelog

## 2.2.0 — 2026-09-01

- Added page-level resource inventory and a mandatory PAGE & RESOURCE CHECKPOINT for icons, images, dimensions, scales, formats, rights and accessibility.
- Added historical resource baseline comparison for change/mixed reviews, including Unchanged/New/Modified/Removed/Moved/Unknown classifications.
- Added confirmed-resource persistence immediately after the page/resource checkpoint, limited to review_root/assets, with Resource ID and explicit 1x/2x/3x directories, conflict detection and save records.
- Extended manifest/schema, version bindings, validators, adapters, fixtures and evaluation guidance for resource evidence, confirmation and persistence. Saved resources now require explicit event authorization, a traversal-free path, an existing file and a matching SHA-256.
- Required a linked resource-diff report for change/mixed reviews and added generated positive fixtures plus targeted failure mutations.

## 2.1.0 — 2026-09-01

- Added a mandatory in-conversation PAGE & SCOPE CHECKPOINT for candidate count, included scope and exclusions.
- Added an OPEN QUESTIONS PANEL that renders every unresolved decision while limiting only the requested answers to three per turn.
- Bound specification confirmation to the displayed included/excluded scope and synchronized the page/scope fields in templates and adapter fallbacks.
- Updated all six adapters, stage routes, schema contract, validators and evaluation guidance to core 2.1.0.
- Moved maintainer handoff, migration and source-sample analysis documents outside the runtime package into the parent maintenance directory.

## 2.0.0 — 2026-08-31

- Kept machine/display name project-development-review; delivered in a separate v2 directory.
- Replaced optional reference browsing with mandatory stage routes and a phase artifact contract.
- Separated evidence classification from approval status; added stable evidence/item/decision/acceptance IDs.
- Added review-manifest.json, JSON Schema and language-neutral Markdown metadata/summary blocks.
- Bound approval to authentic source, displayed candidate/version/scope and real frozen SHA-256; added full/partial invalidation and retained approval reuse.
- Split assessment and implementation cards, removing identical-plan confirmation loops.
- Added new/change/mixed baseline reasoning and change-impact attachments with no independent authority.
- Classified scoped blockers, excluded questions and explicit fixed-solution implementation prerequisites.
- Updated six adapters with persistent boundaries, required file routes and a versioned minimal fallback; declared text-only limitations.
- Added standard-library package/review validators, synthetic full/partial-stage fixtures, targeted mutations and retained/new behavior scenarios.
- Added migration guide, maintainer handoff, source-sample root-cause analysis and verification reporting.
- Preserved v1 packages, installed copy, original reviews and the business project. No install, dependency update, publish, commit or push.

## Compatibility notes

The old single task-card, language and confirmation entrypoints route to canonical v2 rules. The output review layout changes deliberately from business-project docs/ to an independent review_root. v1 Confirmed is not automatically v2 Approved. The migration guide is maintained outside the runtime package under the parent `maintenance/` directory.

No client runtime certification is implied. Cursor's historical Commands documentation now redirects to Skills guidance; the legacy command artifact remains available but must be checked in the target build. [Platform details](references/platform-compatibility.md)
