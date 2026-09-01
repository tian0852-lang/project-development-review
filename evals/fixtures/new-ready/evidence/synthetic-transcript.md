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
    "sha256": "0070a3f21f2b4285d696ef3b2379214e345318dbb5d0375de507d9856c7c2485",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "bdccdd634fd622cc4e702b7b47fab9b1e425c309f3cdec31c8f81c656b535e95",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "f0f7606bebb92acd80451c06c0df2794bf3e474b01eef796fad3ec181fac155f",
    "frozen_text_ref": null
  },
  "RESOURCES-1": {
    "version": "R1",
    "path": "evidence/resource-inventory.md",
    "sha256": "11f96120ccfe53f3c22edc0e10469f624d6f9741b404a546134a2899091c3f6f",
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
    "sha256": "0070a3f21f2b4285d696ef3b2379214e345318dbb5d0375de507d9856c7c2485",
    "frozen_text_ref": null
  },
  "DOC-DESIGN-SOURCE": {
    "version": "1",
    "path": "evidence/design-source.md",
    "sha256": "bdccdd634fd622cc4e702b7b47fab9b1e425c309f3cdec31c8f81c656b535e95",
    "frozen_text_ref": null
  },
  "PAGES-1": {
    "version": "P1",
    "path": "evidence/page-inventory.md",
    "sha256": "f0f7606bebb92acd80451c06c0df2794bf3e474b01eef796fad3ec181fac155f",
    "frozen_text_ref": null
  },
  "DOC-SPEC0": {
    "version": "S1",
    "path": "specs/00-product-brief.md",
    "sha256": "12d1eee3663d0b75b878fbb719ca8692dae04f7532f4f78125f26f95d5288860",
    "frozen_text_ref": null
  },
  "DOC-SPEC1": {
    "version": "S1",
    "path": "specs/01-scope-and-priority.md",
    "sha256": "19a9dd71dbb2fb20567fcb4837812515051d65a29dd384df8e6f9c61d5977648",
    "frozen_text_ref": null
  },
  "DOC-SPEC2": {
    "version": "S1",
    "path": "specs/02-user-flow-and-states.md",
    "sha256": "a6fa5ad6c31098cd03733ad50110645c0480dfd9b149f0711021a515bb562ae7",
    "frozen_text_ref": null
  },
  "DOC-SPEC3": {
    "version": "S1",
    "path": "specs/03-design-spec.md",
    "sha256": "18bd0b8008bdb042f1c119a22a9b4bbf225abc611c10840db3dfa2f3b3f75cb6",
    "frozen_text_ref": null
  },
  "DOC-SPEC4": {
    "version": "S1",
    "path": "specs/04-data-and-privacy.md",
    "sha256": "268145be3bf4447fd2aee14a00d6a6e433880d9691e6691667e0178511f9513e",
    "frozen_text_ref": null
  },
  "DOC-SPEC5": {
    "version": "S1",
    "path": "specs/05-acceptance-and-test.md",
    "sha256": "4e13342bd65e0d9a9b5bd22933a495bc0360c4edab6f5c3d917798c9e02dbb6b",
    "frozen_text_ref": null
  },
  "DOC-SPEC6": {
    "version": "S1",
    "path": "specs/06-design-difference-log.md",
    "sha256": "5a0ab42abb8771cdf6a4d76d2b32c2ddb5a36234b58a8f0b7e2f1791e69fb860",
    "frozen_text_ref": null
  }
}

Fictional user response: Confirm specification S1 with the displayed offline scope and DEC-FLOW decision.

## EV-PLAN

Displayed candidate targets and digests:

{
  "BASELINE-1": {
    "version": "B1",
    "path": "evidence/project-baseline.md",
    "sha256": "0070a3f21f2b4285d696ef3b2379214e345318dbb5d0375de507d9856c7c2485",
    "frozen_text_ref": null
  },
  "ASSESS-1": {
    "version": "1",
    "path": "technical/technical-assessment-task-card.md",
    "sha256": "31e5c553528da1512ad926de1e0d38eef0a7d290a0bca07f0b67040b99a17e35",
    "frozen_text_ref": null
  },
  "PLAN-1": {
    "version": "T1",
    "path": "technical/technical-implementation-plan.md",
    "sha256": "6186606455be3bba86df46dd5bb773f00a3efa9115a412747f5f42cb592e58ee",
    "frozen_text_ref": null
  }
}

Fictional user response: Confirm plan T1 and the displayed file scope.

