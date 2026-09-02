# Resource persistence — core 2.2.1

Read after a valid page/resource confirmation and before final handoff. Persistence is limited to confirmed design resources in `review_root/assets/`; `project_root` remains read-only. This step never installs dependencies, changes code/configuration or writes Git state.

## Authorization and capability

The page/resource confirmation event must identify the approved resource IDs, candidate version, save root, exclusions and whether the user authorizes saving. After a valid event authorizes saving, attempt persistence before specification review. Do not save a Draft, unresolved resource, excluded item or an asset with unresolved rights that blocks the approved solution. If the client or connector cannot export/download the binary, return `Approved but not saved` or `Unavailable` with the actual limitation and a verifiable precondition.

## Directory and naming contract

Use a stable resource directory followed by a scale directory so same-named files cannot overwrite one another:

```text
assets/<resource-id>/<scale>/<variant>.<ext>
```

Examples:

```text
assets/ICON-001/1x/search.svg
assets/ICON-001/2x/search.png
assets/IMG-001/1x/hero.jpg
assets/IMG-001/2x/hero.jpg
```

When needed, include semantic variant and dimensions in the basename, for example `IMG-001__hero__320x180__2x.jpg`. Use `1x`, `2x`, `3x` (not an implicit filename suffix) and preserve the source format unless the confirmed specification states an export format.

Never silently overwrite an existing `resource-id + scale + variant + format`. Detect a conflict, retain the existing file, record both paths and request a new Resource ID, replacement decision or explicit deduplication. If content digests match, reuse is allowed only with all page references recorded.

## Save record

For every saved or failed row record Resource ID, source URL/node, source and saved dimensions, scale, format, saved path, SHA-256 when filesystem-readable, accessibility, rights, save status and confirmation event ID. A design display size does not by itself determine an export size; retain the distinction.

## Readiness impact

- `Saved`: resource file is in the approved review root and the save record is consistent.
- `Approved but not saved`: identity and use are approved, but export/access is an implementation precondition; downstream cannot start affected work until resolved.
- `Conflict`, `Blocked by rights` or `Unavailable`: block the affected specification/plan when the resource changes layout, licensing or the approved solution; otherwise record a scoped precondition.

With no filesystem capability, label the delivery `Text-only delivery / not filesystem-validated`; never claim a path, hash or save operation that was not observed.
