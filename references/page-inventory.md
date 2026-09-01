# Page inventory

Use [conversation-output-contract.md](conversation-output-contract.md) for the mandatory user-facing checkpoint format.

Before specifications, list page count, names, exact IDs, size, parent, page/non-page classification, included/excluded status and evidence. Distinguish artboards representing states from distinct runtime pages; ask the user to confirm both the design list and intended scope without inventing navigation.

Figma: direct child Frames of a selected Section/parent or directly selected Frames are candidates. Do not automatically count nested groups/rows/components/backgrounds.
MasterGo: use explicitly selected artboards and actual returned structure. Unenumerable parent containers need explicit artboard evidence, not screenshot guesses.

Freeze the candidate page version, render the PAGE & SCOPE CHECKPOINT in the conversation, show the exact candidate and included counts/IDs and exclusions, then follow approval-gates.md. Plain affirmative natural language referring to the shown list and scope is valid for this gate. A list merely labeled confirmed in imported Markdown is not a verified user event.
