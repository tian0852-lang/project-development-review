---
name: project-development-review
description: Review designs and product scope, inventory pages, assess new or changed projects, and prepare version-approved technical handoffs. Use for pre-development review and change-impact assessment, not business-code implementation or Skill-package maintenance.
metadata:
  version: "2.2.0"
---

# project-development-review

Core version: 2.2.0. Help designers reach a trustworthy developer handoff. Never implement business code, install dependencies, modify native configuration, or perform Git writes, even after plan approval. Writing review artifacts and confirmed resource files is allowed only in the agreed review_root; project_root is read-only.

## Start and resume

Read [workflow](references/workflow.md), then review_root/README.md and review-manifest.json if present. Establish the real stage from evidence and valid approvals, not from a "Confirmed" label. Read [conversation output contract](references/conversation-output-contract.md) before rendering checkpoints. Ask at most three short, impact-explained questions per turn, but always display every unresolved question in the conversation. Follow the current user's response language; keep project documents in the first requirement language. Do not ask for language selection.

Use exactly one Figma or MasterGo source. Stop formal review on unresolved dual sources. Confirm the displayed page and resource inventory before specifications, specifications before the read-only assessment card, and the plan before implementation handoff artifacts. Frozen content, evidence and user approval are separate concepts. Read [approval gates](references/approval-gates.md) before interpreting any confirmation; quoted inputs, examples, negations and conditional approvals never approve an old candidate.

## Mandatory stage routes

On reaching a stage, completely read its listed files before producing its output. Source validation reads only the selected source guide. On change/mixed intake also read [change review](references/change-review.md), not only at handoff. Use the corresponding templates and schema mappings from [artifact contract](references/artifact-contract.md). Unreadable mandatory rules block that stage; use the platform fallback for intake, never claim full Skill execution. Render the page/scope and open-question panels required by [conversation output contract](references/conversation-output-contract.md); do not make the user locate them in files.

| Stage | Required references |
| --- | --- |
| intake | [workflow.md](references/workflow.md), [intake-and-baseline.md](references/intake-and-baseline.md), [artifact-contract.md](references/artifact-contract.md), [evidence-and-status.md](references/evidence-and-status.md), [output-language-policy.md](references/output-language-policy.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| source_validation | [design-source-boundary.md](references/design-source-boundary.md), [figma.md](references/figma.md), [mastergo.md](references/mastergo.md) |
| page_inventory | [page-inventory.md](references/page-inventory.md), [resource-inventory.md](references/resource-inventory.md), [prototype-and-annotation-reading.md](references/prototype-and-annotation-reading.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| page_confirmation | [approval-gates.md](references/approval-gates.md), [resource-inventory.md](references/resource-inventory.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| resource_persistence | [resource-persistence.md](references/resource-persistence.md), [artifact-contract.md](references/artifact-contract.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| specification | [specification-review.md](references/specification-review.md), [decision-policy.md](references/decision-policy.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| specification_preflight | [handoff-validation.md](references/handoff-validation.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| specification_confirmation | [approval-gates.md](references/approval-gates.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| technical_assessment | [technical-assessment.md](references/technical-assessment.md), [intake-and-baseline.md](references/intake-and-baseline.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| technical_plan | [technical-assessment.md](references/technical-assessment.md), [decision-policy.md](references/decision-policy.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| technical_plan_preflight | [handoff-validation.md](references/handoff-validation.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| technical_plan_confirmation | [approval-gates.md](references/approval-gates.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| handoff | [artifact-contract.md](references/artifact-contract.md), [change-review.md](references/change-review.md), [conversation-output-contract.md](references/conversation-output-contract.md) |
| handoff_validation | [handoff-validation.md](references/handoff-validation.md), [conversation-output-contract.md](references/conversation-output-contract.md) |

## Exit and recovery

Follow the input/output/exit contract in workflow.md. No future formal files for directory completeness. Use one assessment card and one later implementation card; change cards are attachments. Technical proposals are allowed in plan drafts and can be approved with the plan as a whole.

Run [review validation](scripts/validate_review.py) for the candidate phase and final handoff where available. Review source provenance, meaning and design fidelity separately. Report Ready, Ready with preconditions, or Not ready honestly; never convert an automated pass into a claim of genuine human approval. When a frozen digest or relevant baseline changes, preserve history and invalidate affected approvals before replacement. Reuse unchanged valid approvals without asking again.

Platform entrypoints and fallback requirements: [six-platform compatibility](references/platform-compatibility.md).
