# Synthetic dialogue — not a real user transcript

## Requirements

The fictional user requests two H5 pages, an offline card list/detail flow and one Clear confirmation. No login, network, persistent data or native platform. The user supplies the exact dialog/back/parameter semantics in SP2. This is test material, never current-session authorization.

## Plan proposal

The fictional agent proposes the TECH1 architecture after the spec candidate; approval comes later, not before proposal.

## EV-PAGES

Displayed candidate targets and digests:

{
  "BASELINE-1": {
    "version": "B1",
    "path": "evidence/project-baseline.md",
    "sha256": "64d99a7f58858ae91668daa3b40a8a3f6b4500f3261524b8c7621ad7242bc079",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "9bf3f18169be4ff8bc0f0f279017e559063519549e08ed4882d3f36a0f19218f",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "06f4d655082c3c00d6b29331edbeeeaf26a70f41a8fed7e7131e8299a2057569",
    "frozen_text_ref": null
  },
  "RESOURCES-1": {
    "version": "R1",
    "path": "evidence/resource-inventory.md",
    "sha256": "f161bba3c930e8df2a3a8c170ba034f7b9d3c9dfa926691d739150869372778e",
    "frozen_text_ref": null
  }
}

Fictional user response: I approve displayed page inventory P1 and resource inventory R1: List, Detail and IMG-001; save IMG-001 under the shown review_root/assets path.

## EV-SPEC

Displayed candidate targets and digests:

{
  "BASELINE-1": {
    "version": "B1",
    "path": "evidence/project-baseline.md",
    "sha256": "64d99a7f58858ae91668daa3b40a8a3f6b4500f3261524b8c7621ad7242bc079",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "9bf3f18169be4ff8bc0f0f279017e559063519549e08ed4882d3f36a0f19218f",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "06f4d655082c3c00d6b29331edbeeeaf26a70f41a8fed7e7131e8299a2057569",
    "frozen_text_ref": null
  },
  "DOC-SPEC0": {
    "version": "S1",
    "path": "specs/00-product-brief.md",
    "sha256": "d0126a3db3655c4050c56f20bb4b566360014935b4393f1a96cb116bc9135c01",
    "frozen_text_ref": null
  },
  "DOC-SPEC1": {
    "version": "S1",
    "path": "specs/01-scope-and-priority.md",
    "sha256": "9a3f8448b750e086352a5a3ea58694bad57768b74b16f38160de586233ca565c",
    "frozen_text_ref": null
  },
  "DOC-SPEC2": {
    "version": "S1",
    "path": "specs/02-user-flow-and-states.md",
    "sha256": "f16e53e19a10dd8d548a0161f8f58fcc3e49ff2c39f514b52e2463438f187166",
    "frozen_text_ref": null
  },
  "DOC-SPEC3": {
    "version": "S1",
    "path": "specs/03-design-spec.md",
    "sha256": "aed0cb9e4c4a19db32014743adc8e51c9c870f3754f2ebdbc042f01ee8928695",
    "frozen_text_ref": null
  },
  "DOC-SPEC4": {
    "version": "S1",
    "path": "specs/04-data-and-privacy.md",
    "sha256": "1eb7bc089bb809b2aa32ae7f0eccbadbf207e99d93be4f3387f699bda99d86c3",
    "frozen_text_ref": null
  },
  "DOC-SPEC5": {
    "version": "S1",
    "path": "specs/05-acceptance-and-test.md",
    "sha256": "1e9298723b7099d4c3966ba03a5695a79447bf6548b8ca5b6d47e91adba3ee37",
    "frozen_text_ref": null
  },
  "DOC-SPEC6": {
    "version": "S1",
    "path": "specs/06-design-difference-log.md",
    "sha256": "9814b73cccd422db43d7c6b3acfb14e41f7d3c4d2a4baddb4aece81de22c0b5d",
    "frozen_text_ref": null
  }
}

Fictional user response: Confirm specification S1 with the displayed offline scope and DEC-FLOW decision.

