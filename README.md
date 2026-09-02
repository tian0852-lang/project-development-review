# project-development-review

English | [简体中文](README.zh-CN.md)

## Skill overview

`project-development-review` is a pre-development review Skill for designers, product managers and AI development collaborators.

Before Vibe Coding begins, it turns design files, product goals, page scope, interaction rules, page resources, data boundaries and acceptance requirements into evidence-backed, versioned and approval-traceable specifications, a technical implementation plan and a developer handoff package.

Current version: `2.2.1`

## Quick start

After installing the matching platform adapter, send the following message to start a review.

```text
Please use the Figma MCP or MasterGo MCP to connect to the design document and start a project review.

Project name: …
Project goal: …
Design source: Figma or MasterGo (choose one)
Design link: …
Current screenshot: …
Target platform: …
Project repository: …
```

Each review may use only one design source. Before starting the review, select the artboards to be reviewed in the design tool and keep that selection until the review ends. The Skill first validates the design source, inventories pages and resources, and asks you to confirm the scope before drafting specifications.

## Supported platforms

ChatGPT, Codex, TraeWork, TraeCode, Cursor and Claude Code.

Each platform uses the same core contract with a platform adapter, persistent rules and a fallback prompt. Installation entrypoints and native Skill capabilities differ by client, so follow and verify the matching adapter instructions.

## Core capabilities

- Review new projects, scoped changes to existing projects and mixed projects.
- Use exactly one design source per review: Figma or MasterGo.
- Inventory and confirm page count, names, nodes, dimensions and current scope before specification review.
- Inventory icons, images, fonts, dimensions, formats, scales and usage locations with the pages.
- Identify unchanged, new, modified, removed, moved and unknown resources in previously reviewed projects.
- After user authorization, save confirmed resources under `review_root/assets/<resource-id>/<scale>/`.
- Review navigation, parameters, return behavior, retained state, dialogs and recovery paths.
- Render page scope, included and excluded work, and every open question directly in the conversation.
- Keep design evidence, user-provided facts, technical proposals and user approval distinct.
- Produce a read-only technical assessment and plan only after specification approval.
- Produce the implementation task card and developer handoff only after plan approval.

## Resource management

The resource inventory records:

- Resource ID;
- page usage and design nodes;
- icon or image purpose;
- original, design, export and runtime dimensions;
- export scales such as 1x, 2x and 3x;
- format, crop and fit behavior;
- source, accessibility and usage rights;
- approval status, save status, path and SHA-256.

Resources may be saved only in the review directory, never in the business project. The Skill rejects path traversal, unauthorized saves, digest mismatches and silent overwrites.

## Review deliverables

Review materials are stored in a separate `review_root` and include:

- project and repository baseline;
- design-source record;
- page inventory;
- page resource inventory;
- decisions and open questions;
- seven product and design specifications;
- technical assessment task card;
- technical implementation plan;
- implementation task card;
- approval record;
- developer handoff;
- final validation report;
- change-impact and resource-difference reports when applicable.

## Capability boundaries

This Skill is limited to pre-development review, specification approval, technical planning and developer handoff.

Even after plan approval, it does not:

- write or modify business code;
- install or upgrade dependencies;
- change native project configuration;
- commit or push Git changes;
- decide product rules for the user;
- guess design tokens, navigation parameters, return rules or dialog outcomes;
- convert prototype links directly into runnable logic;
- treat unverified historical confirmation as current development authorization.

Its goal is to replace “developing by guessing from screenshots” with a trustworthy handoff based on evidence, specifications, resources, versions and explicit user approval.

## Platform setup

Use [SKILL.md](SKILL.md) as the execution entry, then choose one [platform adapter](references/platform-compatibility.md): [ChatGPT](adapters/chatgpt/INSTALL.md), [Codex](adapters/codex/INSTALL.md), [TraeWork](adapters/trae-work/INSTALL.md), [TraeCode](adapters/trae-code/INSTALL.md), [Cursor](adapters/cursor/INSTALL.md), or [Claude Code](adapters/claude-code/INSTALL.md). Read the full installation guide; do not copy only SKILL.md. Merge persistent rules instead of replacing existing instructions.

This package has not been installed, published or runtime-certified on those six clients. Start later in a disposable team test workspace with explicit installation permission. An unavailable native Skill never removes review gates. Missing mandatory materials restrict progress to intake/page drafts; no file tools means text-only, not filesystem-validated.

## Local validation

Python 3.9+; standard library only. From this package directory:

```sh
python3 -B scripts/validate_package.py
python3 -B scripts/validate_review.py /absolute/path/to/review --stage specification_preflight
python3 -B scripts/validate_review.py /absolute/path/to/review --stage handoff_validation
python3 -B evals/run_tests.py
```

Scripts do not create approval or update hashes. Exit 0 means that requested phase's checks passed, not that a draft is Ready. Add --check-external for read-only existence checks of declared available local dependencies; network resource access still requires evidence. Synthetic examples require --fixture and are never production approval.

The JSON Schema checker supports the documented subset, not arbitrary JSON Schema. Automated structure/hash checks, recorded human evidence review, agent behavior tests and actual client/connector tests are different result classes. See [eval guide](evals/README.md) and [verification report](evals/expected-results/verification-report.md).

## Maintenance and migration

Maintenance-only documents are kept outside this runtime package under the parent `项目评审skill v2.0/maintenance/` directory: `v1-to-v2.md`, `PROJECT_HANDOFF.zh-CN.md`, and `root-cause-analysis.zh-CN.md`. Never bulk-convert v1 Confirmed to v2 Approved. Do not overwrite existing installations or historical sample reviews.

Internal execution files are English. Responses follow the current user's message; review documents retain the first requirement language unless explicitly translated. README language links do not change a project's document language.
