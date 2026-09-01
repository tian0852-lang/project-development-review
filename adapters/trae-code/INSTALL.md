# TraeCode adapter — 2.2.0

Prefer the reusable complete `.agents/skills/project-development-review/` package when Settings → Skills and Commands → Import settings has the .agents Skill directory enabled. Current CN documentation also supports `.trae/skills/project-development-review/` and local Skill/zip import. A same-name .trae Skill takes priority: inspect version/path, do not silently mix copies. Natural-language invocation is documented; do not assume a universal slash or dollar command. [Official TraeCode Skills](https://docs.trae.cn/ide_skills)

Merge [rules.md](rules.md) into enabled project Rules and use [agent-prompt.md](agent-prompt.md) as the Custom Agent/start request. The prompt routes mandatory references, stage artifacts and manifest before assessment. Record actual package location and read capability; an explicit `docs/skill-packages/project-development-review/` folder is a manual alternative, not native scanning.

If native loading is unavailable, attach the required references/templates, review documents and the same prompt. Its minimal fallback permits intake/page drafts while missing materials are requested. Text-only output must not claim filesystem validation. Keep business code read-only.

Documentation checked 2026-08-31; installation, Custom Agent, Rules and connector runtime: not run. Verify region/build settings during team acceptance.
