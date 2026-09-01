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
    "sha256": "620e124fbec0ef36dbeb4497ae4ea995a56ffb4b2d852e1e4fa629fca033388c",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "712b38367c93a7b422a4a63697afe9560c7d5e858c5b5271eb242bcaadf98845",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "49e578483cfa97bc1cbeeaa161c5ae3b27e7f7c4c2651b282bbff14d3f87a473",
    "frozen_text_ref": null
  },
  "RESOURCES-1": {
    "version": "R1",
    "path": "evidence/resource-inventory.md",
    "sha256": "44b2e7ac232771931e81a998bcd52b01da9743ec685ed9abf1c37e4ac5277351",
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
    "sha256": "620e124fbec0ef36dbeb4497ae4ea995a56ffb4b2d852e1e4fa629fca033388c",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "712b38367c93a7b422a4a63697afe9560c7d5e858c5b5271eb242bcaadf98845",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "49e578483cfa97bc1cbeeaa161c5ae3b27e7f7c4c2651b282bbff14d3f87a473",
    "frozen_text_ref": null
  },
  "DOC-SPEC0": {
    "version": "S1",
    "path": "specs/00-product-brief.md",
    "sha256": "d1195fd291e2a44f33c5bcfc54366499f63f41ba073f323bbdc56b7d573e8689",
    "frozen_text_ref": null
  },
  "DOC-SPEC1": {
    "version": "S1",
    "path": "specs/01-scope-and-priority.md",
    "sha256": "6bdb30f3e30bf982162aa304ba950b9dbc75d26c17f20aa4f25d8af9a7e0573e",
    "frozen_text_ref": null
  },
  "DOC-SPEC2": {
    "version": "S1",
    "path": "specs/02-user-flow-and-states.md",
    "sha256": "9fbb393b16ada49876707ae238ab3142ae1661a037e358e80b380c3d1c71a4c8",
    "frozen_text_ref": null
  },
  "DOC-SPEC3": {
    "version": "S1",
    "path": "specs/03-design-spec.md",
    "sha256": "4ee96f581a2f09f53884f559f59d14e0e3ffbade7950a1f72b2ebb7627986888",
    "frozen_text_ref": null
  },
  "DOC-SPEC4": {
    "version": "S1",
    "path": "specs/04-data-and-privacy.md",
    "sha256": "d66fc5b7a45c283e1e33e47f39c5eab378ba9de0e7b05d55f56760e6c4eb7f99",
    "frozen_text_ref": null
  },
  "DOC-SPEC5": {
    "version": "S1",
    "path": "specs/05-acceptance-and-test.md",
    "sha256": "3497f2c87f87890361cf61069e3d0a40b70aa4ef1e491d68d47e2d3a2222f037",
    "frozen_text_ref": null
  },
  "DOC-SPEC6": {
    "version": "S1",
    "path": "specs/06-design-difference-log.md",
    "sha256": "ae059f5b021f976a05553787208f1e093f590a1a233282fba4cd456c1b85ba6b",
    "frozen_text_ref": null
  },
  "DOC-CHANGE-IMPACT": {
    "version": "1",
    "path": "changes/CH1/change-impact-report.md",
    "sha256": "62aaf82031979f97e471d6102c82dc56dac1b7780a371f99aeee145e32df774d",
    "frozen_text_ref": null
  },
  "DOC-CHANGE-RESOURCE-DIFF": {
    "version": "1",
    "path": "changes/CH1/resource-diff-report.md",
    "sha256": "519c246951744ceccd88eeb64aced29d3d74bf130578af5cb2c7c74d5a65efb1",
    "frozen_text_ref": null
  }
}

Fictional user response: Confirm specification S1 with the displayed offline scope and DEC-FLOW decision. Approve DEC-CHANGE as stated in the impact report.

## EV-PLAN

Displayed candidate targets and digests:

{
  "BASELINE-1": {
    "version": "B1",
    "path": "evidence/project-baseline.md",
    "sha256": "620e124fbec0ef36dbeb4497ae4ea995a56ffb4b2d852e1e4fa629fca033388c",
    "frozen_text_ref": null
  },
  "ASSESS-1": {
    "version": "1",
    "path": "technical/technical-assessment-task-card.md",
    "sha256": "a009fa872d4ede70b8f869c433aff662ff0474b0fdcd253f1e10641a22d4ba68",
    "frozen_text_ref": null
  },
  "PLAN-1": {
    "version": "T1",
    "path": "technical/technical-implementation-plan.md",
    "sha256": "f9ce063b4077a201c48cfc25b423ee8656d7d25c5d573bd18ff7ef1923002d23",
    "frozen_text_ref": null
  }
}

Fictional user response: Confirm plan T1 and the displayed file scope.

