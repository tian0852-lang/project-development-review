# TraeWork adapter — 2.2.0

## Complete package and persistent layer

Current CN documentation describes local upload via Plugin Market → Skills → Upload Skill, accepting a zip or .skill with SKILL.md at archive root. It also documents project `.trae/skills/` and a slash picker or natural-language invocation. These are documented capabilities, not a test of your installed build or a promise about other regional clients. [Official TraeWork Skills](https://docs.trae.cn/work_skills)

For a file-based project use the complete `.trae/skills/project-development-review/` only when that workspace recognizes it; otherwise supply an explicit package folder such as `docs/skill-packages/project-development-review/`. Record its actual path/version and local/cloud context. Do not assume Codex scanning or dollar commands.

Merge [rules.md](rules.md) into enabled project Rules (or persistent project instructions where available). Use [start-review-prompt.md](start-review-prompt.md), even when a Skill is selected, to establish staged reads and the manifest. Do not overwrite existing rules.

## Degraded operation

If native loading fails, attach the full package materials plus the start prompt. It contains a standalone minimal fallback and a mandatory template/reference list. Without those materials, collect inputs only; do not claim all rules ran. With no local file capability, return text-only document/manifest drafts. Re-run filesystem and provenance checks after export.

Documentation checked 2026-08-31; local import, persistent-rule behavior, slash picker and design connector: not run.
