# Evaluation guide — 2.2.1

## Four independent result classes

1. Static package checks: files, versions, local links, route/template fields and adapter drift.
2. Validator tests: fixed synthetic snapshots plus deliberately corrupted states. Assertions require the intended error code, not merely any failure.
3. Agent behavior scenarios: actual conversational execution and side-effect observation; scenarios being written or mentally reviewed does not mean run.
4. Real client/design connector validation: versioned installation, discovery, persistent rules, selected-source tool returns. No such run was performed by this upgrade.

## Run

```sh
python3 -B scripts/validate_package.py
python3 -B evals/run_tests.py
python3 -B scripts/validate_review.py evals/fixtures/new-ready --fixture
python3 -B scripts/validate_review.py evals/fixtures/conditional-ready --fixture
```

Run from package root. Python 3.9+ and the standard library suffice. Tests copy inputs into narrowly named temporary directories under evals and clean only those generated test directories. Validators themselves are read-only. No dependency installation, business code or external service required.

[Mutation inputs](fixtures/mutation-cases.json) contain positive and negative delta cases. The runner modifies temporary copies, never shipped fixtures. [Fixture factory](fixture_factory.py) emits fictional file maps and does not write files or mint production approval. Maintainers may run `python3 -B evals/regenerate_fixtures.py` to update only the six named synthetic fixture directories, then `python3 -B evals/update_expected_results.py` to refresh generated validator evidence. Never point either maintenance step at a real review or use generated digests to overwrite an old approval.

## Shipped fixtures

| Fixture | Expected phase result | Purpose |
| --- | --- | --- |
| new-ready | Ready | Seven complete specs, page/resource confirmation and both standard cards |
| change-ready | Ready | First formal review of existing implementation without fake old approval; resource baseline is synthetic |
| mixed-ready | Ready | New independent work plus existing change and all impact areas |
| conditional-ready | Ready with preconditions | Fixed resource choice, delivery condition with blocked actions |
| intake-valid | Phase passed / Not ready | Missing future artifacts is legitimate |
| plan-proposal-valid | Phase passed / Not ready | New technical proposal before plan approval |

All are synthetic, with explicit fixture flag and simulated evidence/transcript/audit. A fixture Ready tests validator classification, not real project readiness. --fixture refuses nonfixture input; without it fixture input is rejected. None of these samples contains copied personal information from the login reviews.

## Behavior coverage

- [B01: Dual-source conflict](scenarios/B01.md)
- [B02: MasterGo unenumerable parent](scenarios/B02.md)
- [B03: Static evidence is not interaction approval](scenarios/B03.md)
- [B04: Page gate](scenarios/B04.md)
- [B05: Distinct cards and gates](scenarios/B05.md)
- [B06: Real affirmative approval intent](scenarios/B06.md)
- [B07: Historical summary only](scenarios/B07.md)
- [B08: Do not repair business numbers](scenarios/B08.md)
- [B09: Scoped blockers](scenarios/B09.md)
- [B10: Technical proposals are drafts](scenarios/B10.md)
- [B11: Reuse and selective invalidation](scenarios/B11.md)
- [B12: Corrupt or missing artifact](scenarios/B12.md)
- [B13: Mode and baseline reasoning](scenarios/B13.md)
- [B14: Platform acceptance coverage](scenarios/B14.md)
- [B15: Resource conditions versus undecided solution](scenarios/B15.md)
- [B16: Trae minimum fallback](scenarios/B16.md)
- [B17: Complete synthetic delivery](scenarios/B17.md)
- [B18: Original sample read-only regression](scenarios/B18.md)
- [B19: Conversation page and scope checkpoint](scenarios/B19.md)
- [B20: Complete open-question panel](scenarios/B20.md)
- [B21: Page resource inventory and confirmation](scenarios/B21.md)
- [B22: Existing-project resource delta](scenarios/B22.md)
- [B23: Confirmed resource persistence and scale folders](scenarios/B23.md)

## Retained v1 categories

- [L01: MasterGo complete static review](scenarios/L01.md)
- [L02: Figma complete review](scenarios/L02.md)
- [L03: Screenshot only](scenarios/L03.md)
- [L04: Two sources](scenarios/L04.md)
- [L05: Early development](scenarios/L05.md)
- [L06: Early code change](scenarios/L06.md)
- [L07: Automatic language](scenarios/L07.md)
- [L08: Figma parent children](scenarios/L08.md)
- [L09: MasterGo multi-select](scenarios/L09.md)
- [L10: MasterGo parent unreadable](scenarios/L10.md)
- [L11: Structured recommendation](scenarios/L11.md)
- [L12: Existing project local change](scenarios/L12.md)
- [L13: Figma overlay](scenarios/L13.md)
- [L14: MasterGo prototype not returned](scenarios/L14.md)
- [L15: Annotation author unknown](scenarios/L15.md)
- [L16: Cursor entry and persistent rules](scenarios/L16.md)
- [L17: Claude project skill and invocation](scenarios/L17.md)

Record behavior runs with host/version/model, actual read routes, user-turn sequence, artifact/hash evidence and pass/fail/not-run. Do not load all stages before testing staged disclosure. Test fallback by deliberately removing access to mandatory rules, then by removing filesystem tools.

Current measured outcomes: [verification report](expected-results/verification-report.md). Original sample analysis is maintained outside the runtime package under the parent `maintenance/root-cause-analysis.zh-CN.md`; raw samples are not migrated or used as each other's answer keys.
