# Resource inventory — core 2.2.1

Read after page candidates are known and before page/resource confirmation. This inventory is evidence, not an automatic approval. Keep one selected design source; screenshots, recordings and user text supplement it but never introduce a second source.

## Required resource coverage

Inventory every in-scope page resource that can affect implementation or acceptance, especially icons, images, fonts and illustrations. A resource row has a stable `Resource ID` and links to the page, source node/layer, evidence, decision and acceptance IDs. Record what is observed, what is user-provided and what is unreadable; never infer a binary asset or runtime rule from a screenshot alone.

For icons record semantic use, page/control location, source ID, variant/state, design and runtime size, stroke/fill/tint behavior, format and accessibility. For images record purpose, source ID, original dimensions, design display dimensions, export/runtime dimensions, aspect ratio, crop/fit/position, density/scale, format, fallback and rights.

Always distinguish page/Frame dimensions, original file dimensions, design display dimensions, export dimensions and runtime dimensions. Unknown values remain `Open question` with evidence limits.

## Resource status dimensions

Do not merge these dimensions:

- Evidence: `Observed`, `User provided`, `Repository observed`, `Inferred`, `Unreadable`.
- Approval: `Draft`, `Pending confirmation`, `Approved`, `Out of scope`, `Invalidated`.
- Persistence: `Not requested`, `Pending`, `Saved`, `Unavailable`, `Conflict`, `Blocked by rights`.

An asset documented in an old review is not automatically present, accessible, saved or approved. If the historical review has no inventory, record that absence and establish a current baseline without inventing history.

## Page and resource checkpoint

Render `PAGE & RESOURCE CHECKPOINT` in the conversation. Show the page count and every page row, then every resource row grouped by page. Include resource version, included/excluded resources, source IDs, icon/image dimensions, evidence limits, save root and unresolved decisions. Ask no more than three answers in one turn, while keeping all unresolved resource decisions visible in the OPEN QUESTIONS PANEL.

The page confirmation event remains one of the three project gates; it must bind both the displayed page candidate version and resource inventory version. Resource confirmation is a required sub-checkpoint, not a fourth project gate. A correction creates new candidate versions and invalidates only affected approvals.

## Change and mixed reviews

Load the previous `resource-inventory` when available and compare it with the current source, repository and accessible files. Classify each resource as `Unchanged`, `New`, `Modified`, `Removed`, `Moved` or `Unknown`. Compare stable IDs and source node IDs first, then content digest, path, dimensions, ratio, format and page usage. Do not use a filename alone.

Scan shared components, tokens, navigation, shared state, data models, permissions, project configuration and tests for changed resources. A dimension or icon variant change may be `Cross-page` or `Global`; uncertainty remains `Unknown` until evidence or explicit exclusion is recorded. Reconfirm only affected specification and plan items; retain valid unaffected approvals.

## Source limitations

Figma prototype connections express interaction intent, not export permission. MasterGo inventory and export fields depend on actual tool returns. If the selected source cannot provide a file, record its actual location/accessibility and continue with a text-only inventory; do not claim the resource was saved.
