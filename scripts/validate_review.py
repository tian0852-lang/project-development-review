#!/usr/bin/env python3
"""Read-only phased review validator. Stdlib only; never creates approvals or hashes in files."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from contract import schema, check_shape, contained, comment_json, summary, link_errors


def validate(review_root, stage=None, fixture=False, check_external=False):
    root = Path(review_root).resolve()
    errors, passed, manual, unverified = [], [], [], []
    def fail(code, message):
        errors.append({'code': code, 'message': message})
    def report(candidate='Not ready', conditions=None):
        return {'validation_mode': 'synthetic fixture' if fixture else 'review',
                'review_root': str(root), 'stage': stage, 'phase_passed': not errors,
                'readiness': candidate if not errors else 'Not ready',
                'candidate_readiness': candidate, 'automatic_passed': passed,
                'manual_verified': manual, 'unverified': unverified, 'errors': errors,
                'implementation_preconditions': conditions or [],
                'repair_path': [e['message'] for e in errors],
                'limits': ['Checks do not prove genuine user intent or natural-language truth.',
                           'Manual verified lists recorded attestations, not tool-certified human approval.',
                           'No files or confirmation events were modified.']}
    try:
        m = json.loads((root / 'review-manifest.json').read_text(encoding='utf-8'))
        s = schema()
    except (OSError, ValueError) as exc:
        fail('MANIFEST_READ', str(exc)); return report()
    for e in check_shape(m, s, s):
        fail('SCHEMA', e)
    if errors:
        return report()
    ct = s['x-contract']; stages = ct['stages']
    resource_cfg = m.get('resource_inventory', {'required': False, 'artifact_id': None, 'version': None, 'resource_ids': [], 'confirmation_event_ids': [], 'save_root': 'assets/', 'persistence_status': 'Not started'})
    stage = stage or m['stage']
    if stage not in stages:
        fail('STAGE', 'Unknown requested stage'); return report()
    rank = stages.index(stage)
    if rank == stages.index('handoff_validation') and m['stage'] != stage:
        fail('STAGE_MISMATCH', 'Final handoff stage must agree with the manifest, not only the CLI flag.')
    if re.search(r'\{\{.*?\}\}', json.dumps(m), re.S):
        fail('PLACEHOLDER', 'Actual review manifest must not contain template placeholders.')
    if m['fixture'] and not fixture:
        fail('FIXTURE_NOT_PRODUCTION', 'Synthetic examples require --fixture and are not real user approvals.')
    if fixture and not m['fixture']:
        fail('FIXTURE_FLAG', 'Do not use --fixture to bypass checks for real reviews.')
    if m['delivery_mode'] == 'text_only':
        fail('TEXT_ONLY', 'Text-only delivery / not filesystem-validated; collect frozen text versions and export before filesystem handoff.')
        unverified.append('No file hash or filesystem delivery is attested for text-only output.')
        return report()
    if m['review_root'] != '.' and Path(m['review_root']).resolve() != root:
        fail('ROOT', 'review_root does not match the supplied directory; update portable roots explicitly.')
    if m['project_root'] and Path(m['project_root']).resolve() == root:
        fail('ROOT', 'review_root and project_root must be distinct.')
    if m['baseline']['repository_exists'] and not m['project_root']:
        fail('BASELINE', 'Existing repository requires a real external project_root.')
    operations = {u['operation'] for u in m['baseline']['work_units']}
    expected_ops = {'new': {'new'}, 'change': {'change'}, 'mixed': {'new', 'change'}}
    if operations != expected_ops[m['mode']]:
        fail('MODE', 'Baseline work units must substantiate new/change/mixed mode; repository presence alone is insufficient.')
    a, items, ev, decisions, events = (m[k] for k in ('artifacts', 'items', 'evidence', 'decisions', 'confirmation_events'))
    resources = m.get('resources', {})
    if resource_cfg.get('required') and rank >= stages.index('specification'):
        if resource_cfg.get('persistence_status') == 'Not started':
            fail('RESOURCE_PERSISTENCE', 'Finish the post-confirmation resource save attempt or record its scoped limitation before specification review.')
        if any(r.get('save_status') == 'Pending' for r in resources.values()):
            fail('RESOURCE_PERSISTENCE', 'A resource save remains Pending after the persistence checkpoint.')
    for name in ('artifacts','items','evidence','decisions','acceptance','confirmation_events','preconditions','external_dependencies','resources','changes'):
        if any(not key.strip() or '/' in key or '~' in key for key in m[name]):
            fail('ID_FORMAT', f'{name}: IDs must be nonblank and safe for plain JSON pointers (no slash or tilde)')
    def acyclic(graph, label):
        active, done = set(), set()
        def visit(node):
            if node in active:
                fail('CYCLE', f'{label}: cyclic dependency at {node}'); return
            if node in done: return
            active.add(node)
            for dep in graph.get(node, []):
                if dep in graph: visit(dep)
            active.remove(node); done.add(node)
        for node in graph: visit(node)
    acyclic({k:list(v['depends_on']) for k,v in a.items()}, 'artifacts')
    acyclic({k:v['dependencies'] for k,v in items.items()}, 'items')
    acyclic({k:v['basis_event_ids'] for k,v in events.items()}, 'approval events')
    roles, texts, paths = {}, {}, {}
    def refs(ids, collection, where):
        for i in ids:
            if i not in collection:
                fail('REFERENCE', f'{where}: unknown ID {i}')
    ext_locations = [d['location'] for d in m['external_dependencies'].values()]
    if resource_cfg.get('required'):
        rid = resource_cfg.get('artifact_id')
        if not rid or rid not in a or a[rid].get('role') != 'resource_inventory':
            fail('RESOURCE_ARTIFACT','Required resource inventory artifact is missing or has the wrong role.')
        if resource_cfg.get('version') != m['versions'].get('resources'):
            fail('RESOURCE_VERSION','Resource inventory version must match versions.resources.')
        try:
            save_root = contained(root, resource_cfg.get('save_root',''))
            if not save_root.is_relative_to((root / 'assets').resolve()):
                raise ValueError('outside assets')
        except (TypeError, ValueError):
            fail('RESOURCE_ROOT','Resource save root must be a traversal-free relative path under review_root/assets/.')
        refs(resource_cfg.get('confirmation_event_ids',[]), events, 'resource_inventory.confirmation_event_ids')
        if set(resource_cfg.get('resource_ids',[])) != set(resources):
            fail('RESOURCE_REFERENCE','resource_inventory.resource_ids must exactly index current resource records, including exclusions.')
        for resource_id in resource_cfg.get('resource_ids',[]):
            if resource_id not in resources:
                fail('RESOURCE_REFERENCE',f'{resource_id}: resource inventory points to an unknown resource.')
    saved_locations = {}
    for resource_id, resource in resources.items():
        refs(resource.get('evidence_ids',[]), ev, resource_id)
        refs(resource.get('decision_ids',[]), decisions, resource_id)
        refs(resource.get('acceptance_ids',[]), m['acceptance'], resource_id)
        unknown_pages = set(resource.get('page_ids',[])) - set(m['design_source'].get('scope_ids',[]))
        if unknown_pages:
            fail('RESOURCE_PAGE_REFERENCE',f'{resource_id}: resource page IDs are outside the selected design scope: {sorted(unknown_pages)}')
        saved_path = resource.get('saved_path')
        resolved_saved = None
        if saved_path:
            try:
                resolved_saved = contained(root, saved_path)
                parts = Path(saved_path).parts
                if (not resolved_saved.is_relative_to((root / 'assets').resolve()) or len(parts) != 4
                        or parts[0] != 'assets' or parts[1] != resource_id or parts[2] != resource.get('scale')
                        or not Path(parts[3]).suffix):
                    raise ValueError('wrong resource path shape')
            except (TypeError, ValueError):
                fail('RESOURCE_PATH',f'{resource_id}: saved_path must be assets/<resource-id>/<scale>/<filename.ext> without traversal.')
            else:
                prior = saved_locations.get(resolved_saved)
                if prior and prior != resource_id:
                    fail('RESOURCE_PATH_COLLISION',f'{resource_id}: saved_path collides with {prior}; never overwrite silently.')
                saved_locations[resolved_saved] = resource_id
        if resource.get('save_status') == 'Saved' and not resource.get('saved_path'):
            fail('RESOURCE_SAVE_RECORD',f'{resource_id}: Saved resources require saved_path.')
        if resource.get('save_status') == 'Saved' and not resource.get('sha256'):
            fail('RESOURCE_SAVE_RECORD',f'{resource_id}: Saved resources require a recorded SHA-256.')
        if resource.get('save_status') == 'Saved' and resolved_saved is not None:
            if not resolved_saved.is_file():
                fail('RESOURCE_FILE_MISSING',f'{resource_id}: Saved resource file does not exist at the recorded review-root path.')
            elif resource.get('sha256') and hashlib.sha256(resolved_saved.read_bytes()).hexdigest() != resource['sha256']:
                fail('RESOURCE_HASH',f'{resource_id}: saved file bytes do not match the recorded SHA-256.')
    for aid, artifact in a.items():
        role = artifact['role']; roles.setdefault(role, []).append(aid)
        refs(artifact['evidence_ids'], ev, aid); refs(artifact['item_ids'], items, aid)
        refs(artifact['approval_event_ids'], events, aid)
        for dep, version in artifact['depends_on'].items():
            if dep not in a or a[dep]['version'] != version:
                fail('DEPENDENCY_VERSION', f'{aid}: missing or changed dependency {dep}@{version}')
        try:
            path = contained(root, artifact['path'])
            if path in paths.values():
                fail('PATH_COLLISION', f'{aid}: duplicate artifact path')
            paths[aid] = path
            expected = ct['roles'][role][0]
            if '<change-id>' not in expected and Path(artifact['path']).parent != Path(expected).parent:
                fail('ARTIFACT_PATH', f'{aid}: role belongs in {Path(expected).parent}')
            text = path.read_text(encoding='utf-8'); texts[aid] = text
            for problem in link_errors(root, path, text, ext_locations):
                fail('LINK', problem)
            meta = comment_json(text, 'review-meta')
            for key in ct['metadata_fields']:
                if key not in meta:
                    fail('METADATA', f'{aid}: missing {key}')
            match = {'artifact_id': aid, 'review_id': m['review_id'], 'version': artifact['version'],
                     'design_source': m['design_source']['selected'], 'scope_ids': m['design_source']['scope_ids'],
                     'evidence_ids': artifact['evidence_ids'], 'item_ids': artifact['item_ids'],
                     'depends_on': artifact['depends_on'],
                     'approval_status_ref': f'#/artifacts/{aid}/approval_status',
                     'approval_event_ids_ref': f'#/artifacts/{aid}/approval_event_ids'}
            for key, value in match.items():
                if meta.get(key) != value:
                    fail('METADATA', f'{aid}: {key} disagrees with manifest')
            if not isinstance(meta.get('readability_limits'), list):
                fail('METADATA', f'{aid}: readability_limits must be an array')
            if (path.parent / meta.get('manifest', '')).resolve() != root / 'review-manifest.json':
                fail('MANIFEST_POINTER', f'{aid}: manifest pointer resolves elsewhere')
            if role in ct['summary_roles'] and comment_json(text, 'review-summary') != summary(m):
                fail('SUMMARY', f'{aid}: stage/decision/version summary is stale')
            if artifact['completion'] == 'complete':
                if re.search(r'\{\{.*?\}\}', text, re.S):
                    fail('PLACEHOLDER', f'{aid}: completed output contains placeholders')
                for section in ct['template_sections'][ct['roles'][role][1]]:
                    marker = '<!-- section:' + section.lower().replace(' ', '-') + ' -->'
                    if marker not in text:
                        fail('SECTION', f'{aid}: missing section marker {section}')
                        continue
                    body = text.split(marker, 1)[1].split('<!-- section:', 1)[0]
                    body = re.sub(r'^#+[^\n]*', '', body, flags=re.M).strip()
                    if not body or body.lower().strip(' .:-') == 'not applicable':
                        fail('EMPTY_SECTION', f'{aid}: {section} requires content or a reason for Not applicable')
                for row in re.sub(r'```.*?```', '', text, flags=re.S).splitlines():
                    if row.strip().startswith('|') and row.strip().endswith('|'):
                        cells = [c.strip() for c in row.strip()[1:-1].split('|')]
                        if any(not cell for cell in cells):
                            fail('EMPTY_TABLE_CELL', f'{aid}: required table cells need content, null with a limitation, or Not applicable with a reason')
                for iid in artifact['item_ids']:
                    if iid not in re.sub(r'<!--.*?-->', '', text, flags=re.S):
                        fail('ITEM_TEXT', f'{aid}: item {iid} is absent from normative text')
        except (OSError, ValueError, TypeError) as exc:
            fail('ARTIFACT_READ', f'{aid}: {exc}')
    for role, contract in ct['roles'].items():
        if role.startswith('change_'):
            continue
        if len(roles.get(role, [])) > 1:
            fail('DUPLICATE_ROLE', f'{role}: exactly one active artifact permitted; retain historical paths in events')
        if rank >= stages.index(contract[2]) and not roles.get(role):
            fail('MISSING_ARTIFACT', f'{stage}: required role {role} is missing')
    if rank >= stages.index('source_validation') or roles.get('pages'):
        source = m['design_source']
        if not source['selected'] or not source['link'] or not source['scope_ids']:
            fail('DESIGN_SOURCE', 'Select one source and record exact design link/scope before formal review.')
        if not source['evidence_ids']:
            fail('SOURCE_EVIDENCE', 'Source context needs indexed evidence with actual readability limits.')
        refs(source['evidence_ids'], ev, 'design_source')
    for eid, evidence in ev.items():
        if evidence.get('design_source') and evidence['design_source'] != m['design_source']['selected']:
            fail('DUAL_SOURCE', f'{eid}: design evidence from another source is not allowed')
        if evidence['kind'] == 'design_observation' and not evidence.get('design_source'):
            fail('EVIDENCE_SOURCE', f'{eid}: design observation requires selected-source attribution')
    if rank >= stages.index('specification_preflight'):
        if not m['target_platforms']:
            fail('PLATFORMS', 'Product target platforms must be set before specification confirmation.')
        for role in ['baseline', 'design_source', 'pages', 'decisions'] + ['spec'+str(i) for i in range(7)]:
            for aid in roles.get(role, []):
                if a[aid]['completion'] != 'complete':
                    fail('INCOMPLETE', f'{aid}: complete content required at specification preflight')
    if rank >= stages.index('technical_plan_preflight'):
        for aid in roles.get('plan', []):
            if a[aid]['completion'] != 'complete':
                fail('INCOMPLETE', 'Technical plan must be complete before approval.')
    # Specification-set version is independent of its documents' versions.
    for role, key in [('pages', 'pages'), ('resource_inventory', 'resources'), ('plan', 'plan')]:
        for aid in roles.get(role, []):
            if a[aid]['version'] != m['versions'][key]:
                fail('VERSION', f'{aid}: version differs from versions.{key}')
    # Invalid events are kept as history; only valid events can provide authority.
    invalid_events = set()
    invalidation_ids = set()
    partial_targets, partial_items, partial_decisions = {}, {}, {}
    for entry in m['invalidations']:
        refs(entry['event_ids'], events, entry['id']); refs(entry['replacement_event_ids'], events, entry['id'])
        refs(entry['artifact_ids'], a, entry['id']); refs(entry['item_ids'], items, entry['id'])
        invalidation_ids.update(entry['event_ids'])
        refs(entry.get('partial_event_ids', []), events, entry['id'])
        refs(entry.get('decision_ids', []), decisions, entry['id'])
        for eid in entry.get('partial_event_ids', []):
            partial_targets.setdefault(eid, set()).update(entry['artifact_ids'])
            partial_items.setdefault(eid, set()).update(entry['item_ids'])
            partial_decisions.setdefault(eid, set()).update(entry.get('decision_ids', []))
            if eid in events and events[eid]['status'] != 'valid':
                fail('INVALIDATION', f'{eid}: partial revocation retains an otherwise valid historical event')
        for eid in entry['event_ids']:
            if eid in events and events[eid]['status'] != 'invalidated':
                fail('INVALIDATION', f'{eid}: invalidation log and event status disagree')
    for eid, event in events.items():
        refs(event['item_ids'] + event['exclusions'], items, eid)
        refs(event['precondition_ids'], m['preconditions'], eid)
        refs(event['basis_event_ids'], events, eid)
        refs(event['decision_values'], decisions, eid)
        if resource_cfg.get('required') and event['gate'] == 'page_inventory':
            if event.get('resource_inventory_version') != resource_cfg.get('version'):
                fail('RESOURCE_EVENT_VERSION', f'{eid}: page confirmation must bind the current resource inventory version.')
            if set(event.get('resource_ids', [])) != set(resource_cfg.get('resource_ids', [])):
                fail('RESOURCE_EVENT_SCOPE', f'{eid}: page confirmation resource IDs differ from the displayed inventory.')
        if event['status'] == 'invalidated':
            invalid_events.add(eid)
            if eid not in invalidation_ids:
                fail('INVALIDATION', f'{eid}: invalidated event needs an append-only reason record')
            continue
        src = event['source']
        if event['gate'] != 'decision' and (not event['targets'] or not event['item_ids']):
            fail('EVENT_SCOPE', f'{eid}: a project gate must bind a displayed object and nonempty item scope')
            invalid_events.add(eid)
        if (event['intent'] != 'affirmative' or event['provenance_status'] != 'Verified'
                or event['source_type'] == 'historical_summary' or not (src['text'] or src['reference'])):
            invalid_events.add(eid)
            unverified.append(f'{eid}: not a verified affirmative user confirmation')
        if set(event['item_ids']) & set(event['exclusions']):
            fail('EVENT_SCOPE', f'{eid}: an item is both approved and excluded')
        for aid, target in event['targets'].items():
            if aid in partial_targets.get(eid, set()):
                try:
                    archived = contained(root, target['path'])
                    if hashlib.sha256(archived.read_bytes()).hexdigest() != target['sha256']:
                        fail('HISTORY_HASH', f'{eid}: preserve the original frozen target {aid} at its old path')
                except (OSError, ValueError):
                    fail('HISTORY_MISSING', f'{eid}: revoked frozen target is not preserved')
                continue
            if aid not in a:
                fail('EVENT_TARGET', f'{eid}: unknown target {aid}'); invalid_events.add(eid); continue
            if target['version'] != a[aid]['version'] or target['path'] != a[aid]['path']:
                fail('EVENT_VERSION', f'{eid}: target {aid} changed; assess impact and invalidate affected approval')
                invalid_events.add(eid)
            if aid in paths and paths[aid].is_file():
                actual = hashlib.sha256(paths[aid].read_bytes()).hexdigest()
                if target['sha256'] != actual:
                    fail('HASH_MISMATCH', f'{eid}: frozen bytes of {aid} changed; do not overwrite the old digest')
                    invalid_events.add(eid)
        for did, value in event['decision_values'].items():
            if did in partial_decisions.get(eid, set()): continue
            if did in decisions and decisions[did]['user_decision'] != value:
                fail('DECISION_VALUE', f'{eid}: decision {did} changed without new approval')
                invalid_events.add(eid)
    def event_ok(eid, gate=None, aid=None, iid=None, did=None):
        return (eid in events and eid not in invalid_events and events[eid]['status'] == 'valid'
                and (gate is None or events[eid]['gate'] == gate)
                and aid not in partial_targets.get(eid, set())
                and iid not in partial_items.get(eid, set())
                and did not in partial_decisions.get(eid, set()))
    # Validate parent-event chains and current candidate versions; decision events have no project gate.
    gate_keys = {'page_inventory': 'pages', 'specification': 'specification', 'technical_plan': 'plan'}
    gate_roles = {'page_inventory': ['baseline','design_source','pages'] + (['resource_inventory'] if resource_cfg.get('required') else []),
                  'specification': ['baseline','design_source','pages']+['spec'+str(i) for i in range(7)],
                  'technical_plan': ['baseline','assessment_card','plan']}
    for gate in gate_keys:
        for eid, event in events.items():
            if event['gate'] != gate or not event_ok(eid):
                continue
            required_keys = ['pages'] + (['resources'] if gate == 'page_inventory' else []) + (['specification'] if gate != 'page_inventory' else []) + (['plan'] if gate == 'technical_plan' else [])
            if eid not in partial_targets and any(event['target_versions'][k] != m['versions'][k] or not m['versions'][k] for k in required_keys):
                fail('APPROVAL_VERSION', f'{eid}: confirmation refers to a different candidate version'); invalid_events.add(eid)
            parent = {'specification':'page_inventory','technical_plan':'specification'}.get(gate)
            if parent and not any(event_ok(p, parent) for p in event['basis_event_ids']):
                fail('APPROVAL_CHAIN', f'{eid}: no current valid {parent} event'); invalid_events.add(eid)
    gates = {gate: [eid for eid in events if event_ok(eid, gate)] for gate in gate_keys}
    complete_gates = {}
    for gate in gate_keys:
        covered = {aid for eid in gates[gate] for aid in events[eid]['targets'] if event_ok(eid, aid=aid)}
        required = {aid for role in gate_roles[gate] for aid in roles.get(role, [])}
        current_anchor = any(events[eid]['target_versions'][gate_keys[gate]] == m['versions'][gate_keys[gate]]
                             for eid in gates[gate])
        parent = {'specification':'page_inventory','technical_plan':'specification'}.get(gate)
        complete_gates[gate] = (all(roles.get(r) for r in gate_roles[gate]) and required <= covered
                                and current_anchor and (not parent or complete_gates[parent]))
    need_gates = []
    if rank >= stages.index('resource_persistence'): need_gates.append('page_inventory')
    if rank >= stages.index('technical_assessment'): need_gates.append('specification')
    if rank >= stages.index('handoff'): need_gates.append('technical_plan')
    for gate in need_gates:
        if not complete_gates[gate]: fail('APPROVAL_REQUIRED', f'{stage}: verified complete {gate} approval coverage required')
        for role in gate_roles[gate]:
            for aid in roles.get(role, []):
                if a[aid]['approval_status'] != 'Approved':
                    fail('ARTIFACT_STATUS', f'{aid}: gate requires Approved state, not an observation or Draft')
    if resource_cfg.get('required') and rank >= stages.index('resource_persistence'):
        valid_resource_events = [eid for eid in resource_cfg.get('confirmation_event_ids', [])
                                 if event_ok(eid, 'page_inventory')]
        if not valid_resource_events:
            fail('RESOURCE_APPROVAL', 'Current resource inventory has no valid page/resource confirmation event.')
        for resource_id, resource in resources.items():
            covered = any(resource_id in events[eid].get('resource_ids', [])
                          and resource_cfg.get('artifact_id') in events[eid].get('targets', {})
                          for eid in valid_resource_events)
            if resource['approval_status'] in ('Approved', 'Out of scope') and not covered:
                fail('RESOURCE_APPROVAL', f'{resource_id}: approved/excluded resource is not bound by the current checkpoint event.')
            if resource['approval_status'] not in ('Approved', 'Out of scope'):
                fail('RESOURCE_APPROVAL', f'{resource_id}: resource remains {resource["approval_status"]} after the checkpoint.')
            if resource['save_status'] == 'Saved' and not any(events[eid].get('resource_save_authorized') for eid in valid_resource_events):
                fail('RESOURCE_SAVE_AUTH', f'{resource_id}: Saved state lacks explicit resource-save authorization in the checkpoint event.')
    if rank >= stages.index('specification_preflight'):
        for role in ['pages'] + ['spec'+str(i) for i in range(7)]:
            for aid in roles.get(role, []):
                if not a[aid]['item_ids']:
                    fail('EMPTY_SCOPE', f'{aid}: document needs stable items, including justified not-applicable items')
    if rank >= stages.index('technical_plan_preflight'):
        for aid in roles.get('plan', []):
            if not a[aid]['item_ids']: fail('EMPTY_SCOPE', 'Plan has no traceable technical scope')
    for role, gate in [('assessment_card','specification'),('change_attachment','specification'),('implementation_card','technical_plan'),('approval_record','technical_plan'),('handoff','technical_plan')]:
        if roles.get(role) and not complete_gates[gate]:
            fail('PREMATURE_ARTIFACT', f'{role} cannot exist as formal output before {gate} approval')
    for role, gate in [('spec'+str(i), 'page_inventory') for i in range(7)] + [('plan','specification')]:
        if roles.get(role) and not complete_gates[gate]:
            fail('PREMATURE_ARTIFACT', f'{role} cannot be an active draft before complete {gate} approval')
    for aid, artifact in a.items():
        if artifact['approval_status'] == 'Approved':
            refs_ok = [eid for eid in artifact['approval_event_ids'] if event_ok(eid)]
            direct = any(aid in events[eid]['targets'] and event_ok(eid, aid=aid) for eid in refs_ok)
            downstream = artifact['role'] in ('assessment_card','change_attachment','implementation_card','approval_record','handoff')
            downstream_gate = 'specification' if artifact['role'] in ('assessment_card','change_attachment') else 'technical_plan'
            downstream = downstream and complete_gates[downstream_gate] and any(event_ok(eid, downstream_gate) for eid in refs_ok)
            if not refs_ok or not (direct or downstream):
                fail('ARTIFACT_APPROVAL', f'{aid}: Approved has no covering valid event')
    approved_scope = set()
    for iid, item in items.items():
        refs([item['artifact_id']], a, iid); refs(item['evidence_ids'], ev, iid)
        refs(item['decision_ids'], decisions, iid); refs(item['acceptance_ids'], m['acceptance'], iid)
        refs(item['dependencies'], items, iid); refs(item['approval_event_ids'], events, iid)
        if item['artifact_id'] in a and iid not in a[item['artifact_id']]['item_ids']:
            fail('ITEM_OWNER', f'{iid}: missing from owning artifact')
        if item['artifact_id'] in a and not set(item['evidence_ids']) <= set(a[item['artifact_id']]['evidence_ids']):
            fail('EVIDENCE_INDEX', f'{iid}: owning document evidence index omits item evidence')
        if item['scope'] == 'out':
            if item['approval_status'] not in ('Out of scope','Invalidated'):
                fail('EXCLUSION', f'{iid}: excluded item must not be implemented')
            continue
        if item['kind'] != 'page':
            if not item['evidence_ids'] or not item['acceptance_ids']:
                fail('TRACEABILITY', f'{iid}: implementable item requires evidence and acceptance IDs')
            if not set(item['platforms']) <= set(m['target_platforms']) or not item['platforms']:
                fail('PLATFORM_SCOPE', f'{iid}: platform outside approved product targets or missing')
        if item['kind'] == 'technical' and not any(d in items and items[d]['kind']=='specification' for d in item['dependencies']):
            fail('TECHNICAL_DEPENDENCY', f'{iid}: technical item needs a specification dependency')
        for dep in item['dependencies']:
            if dep in items and items[dep]['scope'] == 'out':
                fail('EXCLUDED_DEPENDENCY', f'{iid}: depends on excluded {dep}')
        if item['approval_status'] == 'Approved':
            gate = {'page':'page_inventory','specification':'specification','technical':'technical_plan'}[item['kind']]
            if not any(event_ok(eid, gate, item['artifact_id'], iid) and iid in events[eid]['item_ids'] and item['artifact_id'] in events[eid]['targets'] for eid in item['approval_event_ids']):
                fail('ITEM_APPROVAL', f'{iid}: no matching valid event covering item and frozen document')
            else: approved_scope.add(iid)
        required_kind = (item['kind']=='page' and 'page_inventory' in need_gates or item['kind']=='specification' and 'specification' in need_gates or item['kind']=='technical' and 'technical_plan' in need_gates)
        if required_kind and iid not in approved_scope:
            fail('UNAPPROVED_SCOPE', f'{iid}: required scope remains unapproved')
    for accept_id, accept in m['acceptance'].items():
        refs(accept['item_ids'], items, accept_id)
        if not set(accept['platforms']) <= set(m['target_platforms']):
            fail('ACCEPTANCE_PLATFORM', f'{accept_id}: acceptance introduces out-of-scope platform')
    if rank >= stages.index('specification_preflight'):
        for iid, item in items.items():
            if item['scope']=='in' and item['kind']!='page':
                covered = set()
                for acc in item['acceptance_ids']:
                    if acc in m['acceptance'] and iid in m['acceptance'][acc]['item_ids']:
                        covered.update(m['acceptance'][acc]['platforms'])
                if not set(item['platforms']) <= covered:
                    fail('ACCEPTANCE_COVERAGE', f'{iid}: missing platform-specific acceptance')
        all_platforms = {p for acc in m['acceptance'].values() for p in acc['platforms']}
        if not set(m['target_platforms']) <= all_platforms:
            fail('ACCEPTANCE_COVERAGE', 'Not every target platform has an acceptance plan.')
    active_items = {i for i,v in items.items() if v['scope']=='in'}
    for did, decision in decisions.items():
        refs(decision['evidence_ids'], ev, did); refs(decision['affected_item_ids'], items, did)
        refs(decision['approval_event_ids'], events, did)
        if decision['precondition_id'] is not None:
            refs([decision['precondition_id']], m['preconditions'], did)
        affected = not decision['affected_item_ids'] or bool(active_items & set(decision['affected_item_ids']))
        if decision['status'] != 'unresolved':
            if not decision['user_decision'] or not any(event_ok(eid, did=did) and events[eid]['decision_values'].get(did)==decision['user_decision'] for eid in decision['approval_event_ids']):
                fail('DECISION_APPROVAL', f'{did}: resolved/excluded decision lacks a verified user decision event')
        elif affected:
            level = decision['blocking_level']
            thresholds = {'page_scope':'page_confirmation','specification':'specification_preflight','plan':'technical_plan_preflight'}
            if level in thresholds and rank >= stages.index(thresholds[level]):
                fail('BLOCKING_DECISION', f'{did}: unresolved {level} question affects current scope')
            if level == 'out_of_scope' and decision['affected_item_ids']:
                fail('FALSE_EXCLUSION', f'{did}: out-of-scope decision still affects included items')
            if level == 'implementation' and rank >= stages.index('technical_plan_preflight') and decision['precondition_id'] not in m['preconditions']:
                fail('PRECONDITION_REQUIRED', f'{did}: implementation blocker needs explicit condition')
    pending = []
    for pid, condition in m['preconditions'].items():
        refs(condition['blocks_item_ids'], items, pid); refs(condition['evidence_ids'], ev, pid)
        refs(condition['dependency_ids'], m['external_dependencies'], pid)
        relevant = bool(set(condition['blocks_item_ids']) & active_items)
        if condition['status']=='pending' and relevant:
            pending.append({'id':pid,**condition})
            if condition['changes_approved_solution'] and rank >= stages.index('technical_plan_preflight'):
                fail('SOLUTION_UNDECIDED', f'{pid}: condition changes the approved solution; resolve plan first')
            if rank >= stages.index('handoff') and not any(pid in events[eid]['precondition_ids'] for eid in gates['technical_plan']):
                fail('CONDITION_APPROVAL', f'{pid}: pending condition absent from approved plan event')
    for xid, dependency in m['external_dependencies'].items():
        refs(dependency['evidence_ids'], ev, xid); refs(dependency['required_by_item_ids'], items, xid)
        if dependency['precondition_id'] is not None:
            refs([dependency['precondition_id']], m['preconditions'], xid)
        relevant = bool(set(dependency['required_by_item_ids']) & active_items)
        if relevant and dependency['accessibility'] != 'available' and rank >= stages.index('technical_plan_preflight'):
            if not any(p['id']==dependency['precondition_id'] for p in pending):
                fail('EXTERNAL_UNRESOLVED', f'{xid}: unavailable dependency needs explicit approved-solution condition')
        if dependency['accessibility']=='available' and not dependency['evidence_ids']:
            fail('EXTERNAL_EVIDENCE', f'{xid}: available resource requires access-check evidence')
        if check_external and dependency['accessibility']=='available' and not re.match(r'^https?://',dependency['location']):
            if not Path(dependency['location']).exists():
                fail('EXTERNAL_ACCESS', f'{xid}: declared available local path does not exist')
    if m['external_dependencies'] and not check_external:
        unverified.append('External access not rechecked by this run; recorded evidence/conditions used.')
    if m['mode'] in ('change','mixed'):
        if not m['changes']: fail('CHANGE_REQUIRED','Change/mixed mode requires change records.')
        for cid, change in m['changes'].items():
            refs(change['decision_ids'], decisions, cid); refs(change['affected_item_ids'], items, cid)
            refs(change['baseline_refs'], ev, cid)
            if rank >= stages.index('specification') and resource_cfg.get('required'):
                aid = change.get('resource_diff_artifact_id')
                if not aid or aid not in a or a[aid]['role'] != 'change_resource_diff':
                    fail('CHANGE_ARTIFACT', f'{cid}: change/mixed review requires a resource-diff report linked to the current inventory.')
                elif Path(a[aid]['path']).parent != Path('changes') / cid:
                    fail('CHANGE_PATH', f'{cid}: resource-diff report belongs in its own change directory.')
            for field, role, threshold in [('request_artifact_id','change_request','intake'),('impact_artifact_id','change_impact','specification'),('attachment_artifact_id','change_attachment','technical_assessment')]:
                if rank < stages.index(threshold): continue
                aid=change[field]
                if aid not in a or a[aid]['role']!=role:
                    fail('CHANGE_ARTIFACT',f'{cid}: missing {role}')
                elif Path(a[aid]['path']).parent != Path('changes') / cid:
                    fail('CHANGE_PATH',f'{cid}: attachment belongs in its own change directory')
            if rank >= stages.index('specification_preflight'):
                if set(ct['scan_areas']) - set(change['scan']): fail('IMPACT_SCAN',f'{cid}: global scan is incomplete')
                if change['classification']=='Unknown' and set(change['affected_item_ids']) & active_items:
                    fail('UNKNOWN_IMPACT',f'{cid}: investigate unknown impact or exclude affected scope')
                if not change['decision_ids'] or any(d not in decisions or decisions[d]['status']=='unresolved' for d in change['decision_ids']):
                    fail('CHANGE_DECISION',f'{cid}: scope/impact requires user decision records')
    elif m['changes']:
        fail('MODE', 'Change records need change or mixed mode.')
    for field, role, threshold in [('assessment_id','assessment_card','technical_assessment'),('implementation_id','implementation_card','handoff')]:
        aid=m['active_cards'][field]
        if aid is not None and (aid not in a or a[aid]['role']!=role):
            fail('ACTIVE_CARD',f'{field}: pointer must reference the sole standard {role}')
        if rank>=stages.index(threshold) and aid not in roles.get(role,[]):
            fail('ACTIVE_CARD',f'{field}: active pointer required')
        if aid and not complete_gates['specification' if role=='assessment_card' else 'technical_plan']:
            fail('PREMATURE_POINTER',f'{field}: cannot point to an unapproved authority')
    # Handoff documents must bind the same plan/spec/baseline, not a freshly requested plan.
    for role in ('assessment_card','plan','implementation_card','approval_record','handoff','change_attachment'):
        for aid in roles.get(role,[]):
            required_roles=['baseline']+['spec'+str(i) for i in range(7)]
            if role=='plan': required_roles+=['assessment_card']
            if role in ('implementation_card','approval_record','handoff'): required_roles+=['plan']
            for rr in required_roles:
                if any(d not in a[aid]['depends_on'] for d in roles.get(rr,[])):
                    fail('HANDOFF_REFERENCE',f'{aid}: missing current dependency {rr}')
            if role=='implementation_card' and set(a[aid]['item_ids']) != {i for i,v in items.items() if v['kind']=='technical' and v['scope']=='in'}:
                fail('HANDOFF_SCOPE',f'{aid}: implementation card must list exactly current in-scope technical items')
    if rank>=stages.index('handoff'):
        required_manual={'confirmation_provenance','semantic_consistency','design_fidelity'}
        if m['mode']!='new': required_manual.add('impact_sufficiency')
        for check in m['validation']['manual_checks']:
            if check['status']=='passed' and check['evidence_ref']:
                location=check['evidence_ref'].split('#',1)[0]
                try: readable=contained(root,location).is_file()
                except ValueError: readable=False
                if readable:
                    manual.append(check); required_manual.discard(check['id'])
        for name in sorted(required_manual):
            fail('MANUAL_UNVERIFIED',f'{name}: record actual evidence review; scripts cannot supply it')
            unverified.append(name)
        for aid in a:
            if a[aid]['completion']!='complete': fail('INCOMPLETE',f'{aid}: final active artifacts must be complete')
    if rank==stages.index('handoff_validation'):
        if m['validation']['report_artifact_id'] not in roles.get('validation_report',[]):
            fail('VALIDATION_REFERENCE','Manifest must index the actual validation report.')
    if not errors:
        passed.extend(['Schema subset and phase artifacts','Contained links and metadata','ID/version/dependency consistency',
                       'Recorded approval chains and frozen SHA-256','Scoped blockers and platform acceptance','Active cards and conditions'])
    candidate = ('Ready with preconditions' if pending else 'Ready') if not errors and rank==stages.index('handoff_validation') else 'Not ready'
    if rank==stages.index('handoff_validation') and not errors and m['validation']['declared_readiness']!=candidate:
        fail('READINESS_MISMATCH',f'Declared readiness differs from {candidate}; synchronize summary without changing frozen documents.')
    if rank<stages.index('handoff_validation'):
        unverified.append('Preflight only; final handoff validation has not been completed by this invocation.')
    return report(candidate,pending)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('review_root'); parser.add_argument('--stage')
    parser.add_argument('--fixture',action='store_true',help='Explicit synthetic-fixture run; not production approval')
    parser.add_argument('--check-external',action='store_true',help='Read-only existence check for declared available local external resources')
    args=parser.parse_args()
    result=validate(args.review_root,args.stage,args.fixture,args.check_external)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['phase_passed'] else 1


if __name__=='__main__':
    sys.exit(main())
