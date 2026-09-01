# Handoff validation

Use scripts/validate_review.py at preflight and final handoff. It reads and reports only. Stage requirements come from artifact-contract.md and schemas/review-manifest.schema.json; do not demand future artifacts early.

Automatic checks include shape, files, paths, relative links, IDs, versions, hashes, dependencies, metadata summaries, selected-source consistency, page/resource confirmation, resource paths/scales/conflicts, platform acceptance, exclusions, scoped blockers, conditions and change records. No placeholder is allowed in real completed output.

Review humans/agents must separately verify provenance of genuine user messages, semantic consistency, design fidelity and impact sufficiency. A structured "Verified" field is a recorded attestation, not cryptographic proof that a human approved. Report automatic_passed, manual_verified (recorded evidence), and unverified separately. Never present string matching as behavioral model testing.

Ready: valid current approval chain, frozen page/resource scope and no implementation blocker.
Ready with preconditions: valid approvals, no page/spec/plan blockers, remaining explicit implementation prerequisites do not change the solution; enumerate blocked actions and permitted unaffected work.
Not ready: missing current artifacts, unverified/invalid approvals, content mismatch, conflicting scope or unresolved page/spec/plan blocker. State the smallest repair path.
Preflight-only success is not a final Ready result. Text-only delivery is always labeled Text-only delivery / not filesystem-validated.

Write validation/validation-report.md after collecting the report, index it, then run handoff_validation again. Do not modify frozen approved content just to update state summaries.
