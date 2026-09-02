# Platform compatibility — core 2.2.1

Documentation review date: 2026-08-31. Every v2 client installation, invocation, automatic match and connector end-to-end test is **not run**. Documented support is not runtime certification. No installation or publication occurred.

| Platform | Complete package / entry | Persistent layer | Non-native fallback |
| --- | --- | --- | --- |
| ChatGPT | [Upload and invocation](../adapters/chatgpt/INSTALL.md) | Attached/project instructions | Explicit prompt plus supplied core materials |
| Codex | [Repository or personal Skill](../adapters/codex/INSTALL.md) | AGENTS.md | Explicit readable folder plus prompt |
| TraeWork | [Local upload or verified project path](../adapters/trae-work/INSTALL.md) | Enabled Rules/project instructions | Staged start prompt and minimum fallback |
| TraeCode | [Enabled .agents or .trae Skill](../adapters/trae-code/INSTALL.md) | Rules/Custom Agent instructions | Staged agent prompt and minimum fallback |
| Cursor | [Always rule plus discovered entry](../adapters/cursor/INSTALL.md) | Always-applied .mdc | Prompt + Rule; legacy command needs build verification |
| Claude Code | [Project Skill with explicit slash](../adapters/claude-code/INSTALL.md) | CLAUDE.md | Prompt + rules + attached documents |

Each adapter installation guide contains primary official citations and exact path caveats. Record actual client/build, OS, region, permissions, package path/version, loaded files and test transcript. Tool write restrictions should be configured separately by an authorized owner; this package does not install a permission system.

Read [minimal fallback](../adapters/fallback-contract.md). Without mandatory core materials do intake/page drafts only. With them but no files, produce Text-only delivery / not filesystem-validated; do not assert file hashes, saved documents or Ready. A client feature with the same name is not evidence of equivalent behavior.

Figma/MasterGo connectors are separate from Skill discovery. Inspect real selected-source tool returns before making readability claims or attempting resource export. A PAGE & RESOURCE CHECKPOINT can be produced from metadata/text-only evidence, but binary saving is claimed only when the selected connector and filesystem actually expose it. No tool dependency for both sources is auto-installed.
