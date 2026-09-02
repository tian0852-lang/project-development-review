# Claude Code adapter — 2.2.1

The documented local project path is `.claude/skills/project-development-review/SKILL.md`; copy the complete package beside it, not SKILL.md alone. The documented personal path is `~/.claude/skills/project-development-review/SKILL.md`. The directory name exposes `/project-development-review`. Same-name personal Skills can shadow project Skills, so verify the resolved version. [Official Skills documentation](https://code.claude.com/docs/en/skills)

Merge [CLAUDE.md.template](CLAUDE.md.template) into the applicable project CLAUDE.md. Keep [invocation.md](invocation.md) as the start request and fallback. Project Skill and persistent review rules have different jobs; the Skill must still stop at handoff.

If Skills or slash invocation are disabled/unavailable, attach the required package references/templates and review documents, retain CLAUDE.md, and paste the invocation prompt. Record an explicit full package path or readable attachment resource; `docs/skill-packages/project-development-review/` is a manual convention, not a native path. Missing full rules limits progress to intake/page drafts. No file capability means text-only, not validated delivery.

Do not claim automatic matching is unconditional. Prompt rules cannot enforce a filesystem sandbox. Check the active workspace settings and permissions during team verification.

Official paths and slash behavior checked 2026-08-31; actual local installation/invocation and rule behavior for this v2 package: not run.
