# Cursor adapter — 2.2.0

## Persistent rule and explicit entry

Merge [rules.mdc](rules.mdc) into `.cursor/rules/project-development-review-gates.mdc`, keeping `alwaysApply: true`. This supplies ongoing Agent guidance, not a permission sandbox. [Official Rules](https://cursor.com/docs/rules)

Retain [commands/project-development-review.md](commands/project-development-review.md) for builds that discover `.cursor/commands/project-development-review.md`; verify `/project-development-review` appears before relying on it. The former commands documentation now redirects to Skills/migration guidance, so this legacy path is not advertised as runtime-tested on all current builds. [Official migration guidance](https://cursor.com/help/customization/skills)

Current Skills documentation lists project `.cursor/skills/` and `.agents/skills/`. Optional current-build setup: put the complete package in one of those under `project-development-review/`, then verify the selected entry's path/version. Do not require native scanning for the command/fallback to work. [Official Skills](https://cursor.com/docs/skills)

## Responsibilities and fallback

Rule: persistent safety boundaries. Command or Skill: starts the complete staged workflow. Preserve existing project rules and avoid duplicate same-name entries.

Record an explicit full package path (native path or `docs/skill-packages/project-development-review/`). If command discovery fails, paste [invocation.md](invocation.md) with the rule and required package materials. It works as a read-only review prompt without native Skills. Missing core files means intake/page drafts only, not full execution.

Documentation checked 2026-08-31; actual v2 command discovery, installation and enforcement: not run.
