# Verification report — project-development-review 2.2.1

Date: 2026-09-01. Environment: macOS, Python 3.14.6; standard-library validators. Scope: the new Skill package and fictional fixtures only. This is a package-maintenance report, not approval of any business project.

## Measured results

| Verification class | Result | Evidence / qualification |
| --- | --- | --- |
| Package structure, name, version, stage routes, template fields, compatibility aliases and six adapters | Passed | [Package output](package-validation.json) |
| Local Markdown-style links, including target headings where present | Passed across 259 .md/.mdc/.template files | Same package run; web URLs are not asserted by this checker |
| Validator regression suite | 68 test methods passed, 0 failures, 0 errors | [Full test output](validator-tests.txt); includes 60 delta cases, 6 valid-state subcases and 6 package-defect subcases |
| Synthetic positive/negative states | Passed as declared | [Fixture results](fixture-results.json), [delta definitions](../fixtures/mutation-cases.json) |
| Read-only comparison of old packages, installed copy, login project and original review samples | Prior preservation result retained; not repeated by this v2.2 rerun | [Preservation report](preservation-report.json); no input package or business project was edited in this rerun |
| Skill creator quick_validate.py | Blocked before validation | ModuleNotFoundError: No module named 'yaml'; no dependency installed |
| Original three-sample root-cause review | Read-only document analysis completed | Parent maintenance/root-cause-analysis.zh-CN.md; no original chat provenance reconstructed |
| Agent conversational behavior | Not run | 40 written scenarios (23 core behavior + 17 retained categories), not 40 successful model runs; B19-B23 cover page-resource panels, diffs and persistence |
| Actual client install/invocation/persistent-rule behavior | Not run on all six clients | Documentation review is not runtime verification |
| Live Figma/MasterGo connector and prototype reading | Not run | No selected-source tool session or business review was initiated |
| Independent human verification of real approval sources | Not run | Fixture audit records are fictional; no real user approvals claimed |

## What the automated checks demonstrated

The suite rejects missing current specs, broken paths/anchors, unsafe artifact traversal, version/event mismatch, changed approved bytes without a version bump, cyclic dependencies, premature spec/plan drafts and task cards, invalid or unverifiable approval declarations, missing platform acceptance, undeclared resource conditions, empty required values and evidence-index omissions. Resource checks additionally reject traversal hidden below `assets/`, paths outside `assets/<resource-id>/<scale>/`, absent saved files, digest mismatches, missing save authorization and missing change/mixed resource-diff reports.

It distinguishes scoped page/spec/plan blockers from out-of-scope or nonblocking questions. It separates a fixed font solution awaiting delivery from an undecided font solution. It checks change/mixed impact records, scan categories and unique standard-card pointers; a change card is not implementation authority.

Unchanged approvals are reused without file writes. Partial revocation preserves unaffected document/item bindings and page approval; a new event can approve the revised unit while retaining old frozen bytes. These are structural/event-declaration tests, not proof of authentic human intent.

## Synthetic fixture outcomes

| Fixture | Requested phase | Result |
| --- | --- | --- |
| new-ready | handoff_validation | Ready |
| change-ready | handoff_validation | Ready |
| mixed-ready | handoff_validation | Ready |
| conditional-ready | handoff_validation | Ready with preconditions; typography action blocked |
| intake-valid | intake | Phase passed; Not ready |
| plan-proposal-valid | technical_plan | Phase passed; Not ready |

All fixtures require --fixture. They include fictional design responses, repository observations, user messages and audit attestations. Running them without --fixture is rejected. They cannot be used as current user approval or evidence that a real design/project was accessed.

## Defects found and corrected during implementation

- The initial alias check accepted an alias whose body was changed into an independent contract because its title still contained "compatibility alias". The check now verifies the canonical routing statement; its negative test passes.
- Markdown link validation was extended to anchors, with a negative anchor case.
- Document evidence indexes now must include the evidence referenced by owned items; fixture metadata and templates were aligned.
- Mutable Markdown decision summaries now include question, decision text/event references and precondition pointer, not just status.
- A merely early stage label could previously leave an active spec/plan draft before its prerequisite gate; explicit artifact-level gate checks and tests now reject it.
- Specification collection version was separated from individual document versions so unchanged document approvals can be retained.
- Partial revocation and reapproval were tested without rewriting the original approval or its frozen source bytes.
- The first v2.2 path check accepted only a string prefix. It now resolves paths without traversal, requires the Resource ID and explicit `1x`/`2x`/`3x` directory shape, verifies saved-file existence and SHA-256, and requires explicit save authorization.
- The resource-diff template initially was not exercised by change/mixed fixtures. It is now a required linked change artifact, frozen with the specification decision in those synthetic cases.

## Source preservation and observed relocation

The earlier preservation run recorded a legacy v1 package at an external local path. At that run's final check it was found at a differently nested external local path whose parent folder name contained a trailing space.

The earlier report recorded matching fingerprints and no assistant move/rename. This v2.2 rerun did not repeat those external-input hashes; it edited only the target package and its generated synthetic test evidence. Exact local paths are intentionally omitted from this distributable package.

## Limits and interpretation

- The checker implements only the JSON Schema subset documented in artifact-contract.md, plus explicit cross-field checks. It is not a general JSON Schema validator or general YAML parser.
- Genuine current user intent, natural-language contradiction, source fidelity, impact sufficiency and correct approval-scoping still require evidence review. A manually asserted Verified field is not cryptographic proof.
- Automatic confirmation tests operate on declared intent/provenance states. They do not constitute an LLM test of a negated or quoted sentence.
- Prompt Rules and CLAUDE.md are not permission sandboxes, and do not make every client tool mode physically read-only.
- External resource access is not rechecked by default. --check-external checks existence of declared available local resources only; network/permission/license facts require actual evidence.
- Local link checking covers common inline/reference Markdown links and headings, not every Markdown extension.
- Text-only output cannot attest to saved files, real file digests or filesystem validation.
- Original sample approval provenance remains unknowable from final documents alone; no claim is made that the users never confirmed.

## Next verification before team rollout

With separate installation authorization, choose a disposable workspace, verify the resolved Skill version/path, merge its persistent boundary layer, and run the applicable client scenario. Record the loaded files, real prompt sequence, candidate versions, tool capabilities and before/after business-tree state. Test unavailable Skill and unavailable filesystem paths too.

Use the official-document caveats in [platform compatibility](../../references/platform-compatibility.md). No install, upload, distribution, publication, Git commit/push, dependency install or business implementation was performed by this maintenance task.
