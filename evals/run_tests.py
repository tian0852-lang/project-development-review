#!/usr/bin/env python3
"""Exercise shipped synthetic fixtures and independent invalid-state mutations."""
import copy
import hashlib
import json
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parent
sys.path.insert(0,str(PACKAGE/'scripts'))
from validate_review import validate
from validate_package import validate as validate_package

def digest_tree(root):
    return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}

def update_summary(root,m):
    # Presentation-only sync; deliberately never recompute an approved target hash.
    data={'stage':m['stage'],'versions':m['versions'],'active_cards':m['active_cards'],
          'decision_states':{k:{f:v[f] for f in ('question','status','blocking_level','affected_item_ids','user_decision','approval_event_ids','precondition_id')} for k,v in m['decisions'].items()}}
    for artifact in m['artifacts'].values():
        if artifact['role'] not in ('review_readme','decisions','validation_report'): continue
        path=root/artifact['path']
        if path.is_file():
            text=path.read_text()
            text=re.sub(r'<!-- review-summary\n.*?\n-->',
                        '<!-- review-summary\n'+json.dumps(data,indent=2)+'\n-->',text,flags=re.S)
            path.write_text(text)

def mutate(root,m,op):
    kind=op['op']
    if kind in ('set','delete'):
        parts=op['path'].lstrip('/').split('/')
        cursor=m
        for key in parts[:-1]: cursor=cursor[key]
        if kind=='set': cursor[parts[-1]]=copy.deepcopy(op['value'])
        else: del cursor[parts[-1]]
    elif kind=='append_file':
        path=root/op['path']; path.write_text(path.read_text()+op['value'])
    elif kind=='remove_file':
        (root/op['path']).unlink()  # Only the exact generated temporary fixture path.
    else: raise ValueError(kind)

class RegressionTests(unittest.TestCase):
    def fixture_result(self,name):
        root=HERE/'fixtures'/name
        before=digest_tree(root)
        result=validate(root,fixture=True)
        self.assertEqual(before,digest_tree(root),'Validator must be read-only')
        return result

    def test_shipped_valid_states(self):
        expected={'new-ready':'Ready','change-ready':'Ready','mixed-ready':'Ready',
                  'conditional-ready':'Ready with preconditions','intake-valid':'Not ready',
                  'plan-proposal-valid':'Not ready'}
        for name,readiness in expected.items():
            with self.subTest(name=name):
                result=self.fixture_result(name)
                self.assertTrue(result['phase_passed'],result['errors'])
                self.assertEqual(readiness,result['readiness'])

    def test_fixture_never_production_approval(self):
        result=validate(HERE/'fixtures/new-ready')
        self.assertIn('FIXTURE_NOT_PRODUCTION',{e['code'] for e in result['errors']})

    def test_unchanged_approval_reused_without_writes(self):
        root=HERE/'fixtures/new-ready'; before=digest_tree(root)
        first=validate(root,fixture=True); second=validate(root,fixture=True)
        self.assertEqual(first,second); self.assertEqual(before,digest_tree(root))
        self.assertEqual('Ready',second['readiness'])

    def test_partial_invalidation_retains_unaffected_items(self):
        with tempfile.TemporaryDirectory(prefix='.review-test-',dir=HERE) as temp:
            root=Path(temp)/'review'; shutil.copytree(HERE/'fixtures/plan-proposal-valid',root)
            m=json.loads((root/'review-manifest.json').read_text())
            # Revoke only the visual specification unit. Other spec items retain the same source event.
            m['invalidations'].append({'id':'INV1','reason':'Visual item requires revision.',
                'event_ids':[],'partial_event_ids':['EV-SPEC'],'artifact_ids':['DOC-SPEC3'],
                'item_ids':['SP3'],'replacement_event_ids':[]})
            m['items']['SP3'].update(approval_status='Invalidated',approval_event_ids=[])
            m['artifacts']['DOC-SPEC3'].update(approval_status='Invalidated',approval_event_ids=[])
            m['stage']='specification'
            # Remove active downstream references; stored originals remain untouched as historical files.
            m['artifacts'].pop('ASSESS-1'); m['artifacts'].pop('PLAN-1')
            m['items'].pop('TECH1')
            m['acceptance']['AC1']['item_ids'].remove('TECH1')
            m['active_cards']={'assessment_id':None,'implementation_id':None}
            update_summary(root,m)
            (root/'review-manifest.json').write_text(json.dumps(m,indent=2))
            result=validate(root,fixture=True)
            self.assertTrue(result['phase_passed'],result['errors'])
            self.assertEqual('Approved',m['items']['SP2']['approval_status'])
            self.assertEqual('valid',m['confirmation_events']['EV-PAGES']['status'])
            self.assertEqual('Not ready',result['readiness'])

    def test_manual_attestation_not_invented_by_validator(self):
        with tempfile.TemporaryDirectory(prefix='.review-test-',dir=HERE) as temp:
            root=Path(temp)/'review'; shutil.copytree(HERE/'fixtures/new-ready',root)
            m=json.loads((root/'review-manifest.json').read_text())
            m['validation']['manual_checks'][0].update(status='not_verified',evidence_ref=None)
            (root/'review-manifest.json').write_text(json.dumps(m))
            before=digest_tree(root)
            result=validate(root,fixture=True)
            self.assertEqual('Not ready',result['readiness'])
            self.assertEqual(before,digest_tree(root))
            self.assertIn('confirmation_provenance',result['unverified'])

    def test_changed_spec_reapproved_with_retained_coverage(self):
        with tempfile.TemporaryDirectory(prefix='.review-test-',dir=HERE) as temp:
            root=Path(temp)/'review'; shutil.copytree(HERE/'fixtures/plan-proposal-valid',root)
            m=json.loads((root/'review-manifest.json').read_text())
            old_event=copy.deepcopy(m['confirmation_events']['EV-SPEC'])
            m['stage']='technical_assessment'
            m['versions'].update(specification='S2',plan=None)
            m['artifacts'].pop('PLAN-1'); m['items'].pop('TECH1')
            m['acceptance']['AC1']['item_ids'].remove('TECH1')
            m['invalidations'].append({'id':'INV1','reason':'Only visual SP3 document unit revised.',
                'event_ids':[],'partial_event_ids':['EV-SPEC'],'artifact_ids':['DOC-SPEC3'],
                'item_ids':['SP3'],'replacement_event_ids':['EV-SPEC2']})
            spec=m['artifacts']['DOC-SPEC3']
            old_path=root/spec['path']
            spec.update(version='S2',path='specs/03-design-spec.v2.md',approval_event_ids=['EV-SPEC2'])
            def rewrite_meta(path,aid,artifact,new_path):
                text=path.read_text()
                meta=json.loads(re.search(r'<!-- review-meta\n(.*?)\n-->',text,re.S).group(1))
                meta.update(version=artifact['version'],depends_on=artifact['depends_on'])
                text=re.sub(r'<!-- review-meta\n.*?\n-->','<!-- review-meta\n'+json.dumps(meta,indent=2)+'\n-->',text,flags=re.S)
                new_path.write_text(text)
            rewrite_meta(old_path,'DOC-SPEC3',spec,root/spec['path'])
            m['items']['SP3']['approval_event_ids']=['EV-SPEC2']
            new_event=copy.deepcopy(old_event)
            new_event.update(target_versions=copy.deepcopy(m['versions']),item_ids=['SP3'],decision_values={},
                targets={'DOC-SPEC3':{'version':'S2','path':spec['path'],'frozen_text_ref':None,
                                     'sha256':hashlib.sha256((root/spec['path']).read_bytes()).hexdigest()}})
            new_event['source']['text']='Confirm specification S2: revised SP3 unit only; retain unchanged scope.'
            m['confirmation_events']['EV-SPEC2']=new_event
            assessment=m['artifacts']['ASSESS-1']
            assessment['depends_on']['DOC-SPEC3']='S2'
            prior_path=root/assessment['path']
            assessment.update(version='2',path='technical/technical-assessment-task-card.v2.md',approval_event_ids=['EV-SPEC2'])
            rewrite_meta(prior_path,'ASSESS-1',assessment,root/assessment['path'])
            update_summary(root,m); (root/'review-manifest.json').write_text(json.dumps(m,indent=2))
            result=validate(root,fixture=True)
            self.assertTrue(result['phase_passed'],result['errors'])
            self.assertEqual(old_event,m['confirmation_events']['EV-SPEC'],'Old event must not be rewritten')
            self.assertEqual(old_event['targets']['DOC-SPEC3']['sha256'],hashlib.sha256(old_path.read_bytes()).hexdigest())
            self.assertEqual(['EV-SPEC'],m['items']['SP2']['approval_event_ids'])

    def test_package_static(self):
        result=validate_package(PACKAGE)
        self.assertTrue(result['passed'],result['errors'])

    def test_package_defects_detected(self):
        mutations=[
            ('adapters/cursor/rules.mdc','alwaysApply: true','alwaysApply: false','CURSOR_GATES'),
            ('SKILL.md','(references/decision-policy.md)','(references/missing-policy.md)','STAGE_ROUTE'),
            ('templates/02-user-flow-and-states.md','<!-- section:dialogs -->','<!-- section:omitted -->','TEMPLATE_SECTION'),
            ('references/confirmation-gates.md','compatibility alias','independent contract','ALIAS'),
            ('adapters/trae-work/start-review-prompt.md','Implementation pointer stays null','Implementation pointer is free','ADAPTER_FALLBACK_DRIFT'),
            ('VERSION','2.2.1','1.0','VERSION'),
        ]
        for path,old,new,code in mutations:
            with self.subTest(path=path), tempfile.TemporaryDirectory(prefix='.package-test-',dir=HERE) as temp:
                root=Path(temp)/'project-development-review'
                shutil.copytree(PACKAGE,root,ignore=shutil.ignore_patterns('.package-test-*','.review-test-*','__pycache__'))
                p=root/path; p.write_text(p.read_text().replace(old,new))
                result=validate_package(root)
                self.assertIn(code,{e['code'] for e in result['errors']},result)

def make_case(case):
    def test(self):
        with tempfile.TemporaryDirectory(prefix='.review-test-',dir=HERE) as temp:
            root=Path(temp)/'review'
            shutil.copytree(HERE/'fixtures'/case['fixture'],root)
            m=json.loads((root/'review-manifest.json').read_text())
            for op in case['operations']: mutate(root,m,op)
            if case.get('sync_summary'): update_summary(root,m)
            (root/'review-manifest.json').write_text(json.dumps(m,indent=2))
            before=digest_tree(root)
            result=validate(root,fixture=True)
            self.assertEqual(before,digest_tree(root),'Check must not silently fix input')
            if case['expect_code']:
                self.assertFalse(result['phase_passed'],case['id'])
                self.assertIn(case['expect_code'],{e['code'] for e in result['errors']},result)
                if case.get('expect_message'):
                    self.assertTrue(any(e['code']==case['expect_code'] and case['expect_message'] in e['message']
                                        for e in result['errors']),result)
                self.assertEqual('Not ready',result['readiness'])
            else:
                self.assertTrue(result['phase_passed'],result['errors'])
                self.assertEqual(case['expect_readiness'],result['readiness'])
    return test

CASES=json.loads((HERE/'fixtures/mutation-cases.json').read_text())
for case in CASES:
    setattr(RegressionTests,'test_mutation_'+case['id'].replace('-','_'),make_case(case))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print(json.dumps({'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
                      'mutation_cases':len(CASES),'behavior_model_runs':0,'real_client_runs':0}))
    sys.exit(0 if result.wasSuccessful() else 1)
