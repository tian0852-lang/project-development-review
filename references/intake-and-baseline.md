# Intake and baseline

Record project ID/name/goal, review ID, first project document language, review_root, nullable project_root, existing README paths, target platforms, current implementation facts and baseline limitations.

Collect progressively, with at most three short questions per turn; explain the effect of each missing input. Required coverage across intake and later review: project name; one-sentence goal; target users/scenarios; core user task; included features; explicit exclusions; target platforms; selected source/link/exact nodes/current screenshots; fields/buttons/business and interaction rules; normal/waiting/success/failure/recovery states; real/mock data and privacy; acceptance focus/target validation environment; repository and README location. Do not demand all answers before page inventory if missing items do not affect page scope. Do not invent absent inputs to fill a template.

Choose mode from this round's goal:

- new: create an independent module/platform; a repository may already exist.
- change: modify existing implementation.
- mixed: both new units and modifications.
Record each work unit and intended new/change operation. Repository existence alone does not decide mode.

Keep review_root separate from project_root. Do not create or edit a business README or source tree. Inspect project README and existing specs before source, then only the files/structure needed for assessment. Read-only repo facts are not product approval. A nonexistent repository uses project_root=null and a proposed initialization plan, never a fictional existing tree.

Record baseline ID/version, observable repository revision when available, relevant files/README evidence and their limitations. Do not invent a commit, run result or platform minimum. Preserve distinction between a present iOS tree and proposed independent Android creation. A relevant baseline change after approval must be assessed against the frozen baseline artifact; affected approvals expire.

No old specs? Record their absence, build a current baseline from readable code/README and design evidence, then confirm affected scope. This does not require manufacturing historical approvals.
