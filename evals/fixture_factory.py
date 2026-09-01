"""Build fictional validator input as a file map. Never touches real projects or approvals."""
import copy
import hashlib
import json
import posixpath
from pathlib import Path

PACKAGE=Path(__file__).resolve().parents[1]
CT=json.loads((PACKAGE/'schemas/review-manifest.schema.json').read_text())['x-contract']

def build_fixture(name='new-ready',mode='new',conditional=False,stage='handoff_validation'):
    m=json.loads((PACKAGE/'templates/review-manifest.json').read_text())
    asset_text='<svg xmlns="http://www.w3.org/2000/svg" width="160" height="90" viewBox="0 0 160 90"><rect width="160" height="90" fill="#d9e7ff"/><circle cx="80" cy="45" r="18" fill="#316ee8"/></svg>\n'
    persistence_reached=CT['stages'].index(stage) >= CT['stages'].index('resource_persistence')
    m.update(fixture=True,project_id='DEMO-OFFLINE-CARDS',project_name='Offline Cards (synthetic)',
             review_id='REVIEW-'+name,mode=mode,review_root='.',project_root=None if mode=='new' else '/synthetic/fixture-repository',
             document_language='en',stage=stage,target_platforms=['H5'])
    m['design_source']={'selected':'Figma','link':'https://www.figma.com/design/SYNTHETIC-NOT-A-REAL-FILE/offline-cards',
                        'scope_ids':['frame-list','frame-detail'],'evidence_ids':['E-DESIGN']}
    m['versions']={'pages':'P1','specification':'S1','plan':'T1','resources':'R1'}
    m['resource_inventory']={'required':True,'artifact_id':'RESOURCES-1','version':'R1','resource_ids':['IMG-001'],
                             'historical_inventory':'Not applicable: synthetic new baseline.' if mode=='new' else 'Not available in the fictional old review; current baseline is established from evidence.',
                             'save_root':'assets/','confirmation_event_ids':['EV-PAGES'],'persistence_status':'Complete' if persistence_reached else 'Not started'}
    m['baseline']={'id':'BASELINE-1','version':'B1','repository_exists':mode!='new',
                  'readme_paths':[] if mode=='new' else ['/synthetic/fixture-repository/README.md'],
                  'revision':None,'work_units':[{'id':'WU1','operation':'new' if mode=='new' else 'change',
                                              'target':'H5','path':'.' if mode!='mixed' else 'existing-web/'}],
                  'limitations':['Synthetic fixture only; no real repository or client is asserted.']}
    if mode=='mixed':
        m['baseline']['work_units'].append({'id':'WU2','operation':'new','target':'H5','path':'independent-web/'})
    def evidence(kind,location,scope,**more):
        return {'kind':kind,'location':location,'readable_scope':scope,'limitations':['Fictional test evidence, not a live tool response.'],
                'author':None,'time':None,**more}
    m['evidence']={
        'E-DESIGN':evidence('design_observation','evidence/synthetic-design.md#frames','Two 390 x 844 frames; static text and boxes.',design_source='Figma'),
        'E-USER':evidence('user_provided','evidence/synthetic-transcript.md#requirements','Offline flow, no login/network, state and privacy rules.'),
        'E-TECH':evidence('inference','evidence/synthetic-transcript.md#plan-proposal','Proposed vanilla browser files, pending plan approval until EV-PLAN.')
    }
    m['resources']={'IMG-001':{'type':'Image','page_ids':['frame-list','frame-detail'],'source_node_ids':['frame-list-hero'],
                               'usage':'Offline card illustration','variant':'default','original_dimensions':'unknown',
                               'design_dimensions':'160x90','export_runtime_dimensions':'160x90','scale':'1x','format':'SVG',
                               'crop_fit':'contain, centered','location':'evidence/synthetic-design.md#frames','accessibility':'synthetic source available to fixture generator',
                               'rights':'Synthetic fixture; no external rights','evidence_ids':['E-DESIGN'],'decision_ids':[],
                               'acceptance_ids':['AC1'],'approval_status':'Approved','save_status':'Saved' if persistence_reached else 'Pending',
                               'saved_path':'assets/IMG-001/1x/hero.svg' if persistence_reached else None,
                               'sha256':hashlib.sha256(asset_text.encode()).hexdigest() if persistence_reached else None}}
    if mode!='new':
        m['evidence']['E-CODE']=evidence('repository_observation','evidence/synthetic-baseline.md','Fictional old web file inventory and tests, not real source access.')
    if conditional:
        m['evidence']['E-ASSET']=evidence('user_provided','evidence/synthetic-transcript.md#font-condition','Demo font choice/licensing fixed; transfer is an implementation condition.')

    roles=list(CT['roles'])
    if mode=='new': roles=[r for r in roles if not r.startswith('change_')]
    ids={r:('DOC-'+r.upper().replace('_','-')) for r in roles}
    ids.update({'baseline':'BASELINE-1','pages':'PAGES-1','resource_inventory':'RESOURCES-1','assessment_card':'ASSESS-1','plan':'PLAN-1',
                'implementation_card':'IMPLEMENT-1'})
    for role in roles:
        path,_,_=CT['roles'][role]
        version= 'P1' if role=='pages' else 'R1' if role=='resource_inventory' else 'S1' if role.startswith('spec') else 'T1' if role=='plan' else 'B1' if role=='baseline' else '1'
        m['artifacts'][ids[role]]={'role':role,'path':path.replace('<change-id>','CH1'),'version':version,'completion':'complete',
                                 'approval_status':'Draft','approval_event_ids':[],'evidence_ids':['E-USER'],
                                 'item_ids':[],'depends_on':{}}
    for role in ('baseline','design_source','pages','resource_inventory'):
        m['artifacts'][ids[role]]['approval_status']='Approved'
        m['artifacts'][ids[role]]['approval_event_ids']=['EV-PAGES']
    for role in ['spec'+str(i) for i in range(7)]+['assessment_card','change_impact','change_resource_diff','change_attachment']:
        if role in ids and ids[role] in m['artifacts']:
            m['artifacts'][ids[role]]['approval_status']='Approved'; m['artifacts'][ids[role]]['approval_event_ids']=['EV-SPEC']
    for role in ('plan','implementation_card','approval_record','handoff'):
        m['artifacts'][ids[role]]['approval_status']='Approved'; m['artifacts'][ids[role]]['approval_event_ids']=['EV-PLAN']
    for role in ('assessment_card','plan','implementation_card','approval_record','handoff','change_attachment'):
        if role not in roles: continue
        dependencies=['baseline']+['spec'+str(i) for i in range(7)]
        if role=='plan': dependencies+=['assessment_card']
        if role in ('implementation_card','approval_record','handoff'): dependencies+=['plan']
        m['artifacts'][ids[role]]['depends_on']={ids[r]:m['artifacts'][ids[r]]['version'] for r in dependencies}
    if 'change_resource_diff' in roles:
        m['artifacts'][ids['change_resource_diff']]['depends_on']={ids['resource_inventory']:'R1'}
    def item(iid,kind,role,summary,events,evidence_ids,deps=()):
        m['items'][iid]={'kind':kind,'artifact_id':ids[role],'summary':summary,'scope':'in',
                         'evidence_ids':evidence_ids,'decision_ids':[],'acceptance_ids':[] if kind=='page' else ['AC1'],
                         'dependencies':list(deps),'platforms':[] if kind=='page' else ['H5'],
                         'approval_status':'Approved','approval_event_ids':events}
        m['artifacts'][ids[role]]['item_ids'].append(iid)
    item('PG1','page','pages','Card list','EV-PAGES'.split(),['E-DESIGN'])
    item('PG2','page','pages','Card detail','EV-PAGES'.split(),['E-DESIGN'])
    summaries=['Help a visitor inspect offline cards','Two pages and one dialog; no login/network','Open detail and preserve list selection on return',
               'Static frame layout and supplied text','Fictional in-memory data only','Browser steps cover list, detail, return and cancel/confirm',
               'No unresolved accepted deviation']
    for i,text in enumerate(summaries):
        item('SP'+str(i),'specification','spec'+str(i),text,['EV-SPEC'],['E-USER','E-DESIGN'])
    item('TECH1','technical','plan','Implement approved offline H5 flow in proposed vanilla files',['EV-PLAN'],['E-TECH','E-USER'],['SP'+str(i) for i in range(7)])
    m['artifacts'][ids['implementation_card']]['item_ids']=['TECH1']
    m['acceptance']['AC1']={'item_ids':['SP'+str(i) for i in range(7)]+['TECH1'],'platforms':['H5'],
                           'steps':['Open fixture card list at 390 x 844','Choose card A and open detail','Return to list; retain selected card',
                                    'Open Clear confirmation; cancel, then confirm','Reload and inspect browser network/storage'],
                           'expected_result':'Two frames, correct titles; return retains A; cancel retains selection; confirm clears it; reload clears memory; no external requests or persistent personal data.',
                           'environment':'Desktop Chromium with viewport 390 x 844; no backend; keyboard Escape and visible Back tested.',
                           'evidence_required':'Screenshots and manual interaction recording, browser network/storage observation; planned, not yet executed.'}
    def decision(question,affected,value):
        return {'question':question,'facts':['Synthetic user supplied the scope.'],'evidence_ids':['E-USER'],
                'affected_item_ids':affected,'options':['Use stated scope','Exclude flow'],'recommendation':None,
                'rationale':'The user decides product behavior.','blocking_level':'specification','status':'resolved',
                'owner':None,'user_decision':value,'approval_event_ids':['EV-SPEC'],'precondition_id':None}
    m['decisions']['DEC-FLOW']=decision('Should cancel preserve selection?', ['SP2'],'Cancel preserves selection; confirm clears it.')
    m['items']['SP2']['decision_ids']=['DEC-FLOW']
    if conditional:
        m['preconditions']['PRE-FONT']={'description':'Receive the already approved Demo Sans font file and verify its approved license.',
                'blocks_item_ids':['TECH1'],'blocks_actions':['Integrate or validate final typography'],
                'resolution_test':'Authorized owner supplies the fixed font file and matching license; verify access before typography implementation.',
                'status':'pending','changes_approved_solution':False,'evidence_ids':['E-ASSET'],'dependency_ids':['EXT-FONT']}
        m['external_dependencies']['EXT-FONT']={'kind':'asset','location':'/synthetic/team-assets/DemoSans.woff2','accessibility':'not_checked',
                'evidence_ids':['E-ASSET'],'required_by_item_ids':['TECH1'],'precondition_id':'PRE-FONT'}
    if mode!='new':
        m['decisions']['DEC-CHANGE']=decision('Approve assessed change scope and existing behavior to preserve?', ['SP2','TECH1'],'Preserve old list return behavior and add only the confirmed clear dialog.')
        m['changes']['CH1']={'request_artifact_id':ids['change_request'],'impact_artifact_id':ids['change_impact'],
                'resource_diff_artifact_id':ids['change_resource_diff'],
                'attachment_artifact_id':ids['change_attachment'],'classification':'Cross-page','scan':{
                    'shared_components':'Existing ListRow used on list only; retain its public input.',
                    'design_tokens':'Reuse existing spacing and color constants; no token change.',
                    'navigation':'List/detail back route remains; dialog does not add a route.',
                    'shared_state':'Selection survives detail/back; confirm clear empties it.',
                    'data_models':'Card ID/title shape unchanged; no persistence.',
                    'permissions':'No permissions introduced; no authentication.',
                    'project_configuration':'Existing browser entry retained; no SDK/dependency changes.',
                    'tests':'Add cancel/confirm regression and preserve existing return test.'},
                'decision_ids':['DEC-CHANGE'],'baseline_refs':['E-CODE','E-USER'],'affected_item_ids':['SP2','TECH1']}
    m['active_cards']={'assessment_id':ids['assessment_card'],'implementation_id':ids['implementation_card']}
    m['validation']={'report_artifact_id':ids['validation_report'],
                     'declared_readiness':'Ready with preconditions' if conditional else 'Ready',
                     'manual_checks':[{'id':x,'status':'passed','evidence_ref':'evidence/synthetic-audit.md',
                                      'limitations':['Synthetic attestation for validator testing only; not a real human review.']}
                                      for x in ['confirmation_provenance','semantic_consistency','design_fidelity']+(['impact_sufficiency'] if mode!='new' else [])]}
    scope_spec=['SP'+str(i) for i in range(7)]
    def event(gate,text,scope,rolelist,basis):
        return {'gate':gate,'source_type':'user_message','source':{'text':text,'reference':'evidence/synthetic-transcript.md',
                'message_id':None,'time':None,'limitations':['Fictional transcript; no real message ID or time.']},
                'intent':'affirmative','provenance_status':'Verified','target_versions':copy.deepcopy(m['versions']),
                'resource_inventory_version':'R1' if gate=='page_inventory' else None,
                'resource_ids':['IMG-001'] if gate=='page_inventory' else [],
                'resource_save_authorized':gate=='page_inventory',
                'targets':{ids[r]:{'version':m['artifacts'][ids[r]]['version'],'path':m['artifacts'][ids[r]]['path'],
                                  'sha256':None,'frozen_text_ref':None} for r in rolelist},
                'item_ids':scope,'exclusions':[],'precondition_ids':['PRE-FONT'] if conditional and gate=='technical_plan' else [],
                'decision_values':{d:v['user_decision'] for d,v in m['decisions'].items()} if gate=='specification' else {},
                'basis_event_ids':basis,'status':'valid'}
    specification_roles=['baseline','design_source','pages']+['spec'+str(i) for i in range(7)]
    if mode!='new': specification_roles+=['change_impact','change_resource_diff']
    m['confirmation_events']={
        'EV-PAGES':event('page_inventory','I approve displayed page inventory P1 and resource inventory R1: List, Detail and IMG-001; save IMG-001 under the shown review_root/assets path.',['PG1','PG2'],['baseline','design_source','pages','resource_inventory'],[]),
        'EV-SPEC':event('specification','Confirm specification S1 with the displayed offline scope and DEC-FLOW decision.',scope_spec,specification_roles,['EV-PAGES']),
        'EV-PLAN':event('technical_plan','Confirm plan T1 and the displayed file scope'+(' with PRE-FONT as a precondition.' if conditional else '.'),['TECH1'],['baseline','assessment_card','plan'],['EV-SPEC'])
    }
    if mode!='new': m['confirmation_events']['EV-SPEC']['source']['text']+=' Approve DEC-CHANGE as stated in the impact report.'
    if stage=='intake':
        keep={'review_readme','baseline'}
        m['artifacts']={k:v for k,v in m['artifacts'].items() if v['role'] in keep}
        for v in m['artifacts'].values(): v.update(approval_status='Draft',approval_event_ids=[],evidence_ids=['E-USER'],item_ids=[],depends_on={})
        m.update(items={},decisions={},acceptance={},confirmation_events={},changes={},preconditions={},external_dependencies={})
        m['design_source']={'selected':None,'link':None,'scope_ids':[],'evidence_ids':[]}
        m['evidence']={'E-USER':m['evidence']['E-USER']}
        m['versions']={'pages':None,'specification':None,'plan':None,'resources':None}
        m['resource_inventory'].update(required=False,artifact_id=None,version=None,resource_ids=[],confirmation_event_ids=[],persistence_status='Not started')
        m['resources']={}
        m['active_cards']={'assessment_id':None,'implementation_id':None}
        m['validation']={'report_artifact_id':None,'declared_readiness':'Not ready','manual_checks':[]}
    if stage=='technical_plan':
        removed={'implementation_card','approval_record','handoff','validation_report'}
        m['artifacts']={k:v for k,v in m['artifacts'].items() if v['role'] not in removed}
        m['confirmation_events'].pop('EV-PLAN')
        m['items']['TECH1'].update(approval_status='Draft',approval_event_ids=[])
        m['artifacts'][ids['plan']].update(approval_status='Draft',approval_event_ids=[],completion='draft')
        m['active_cards']['implementation_id']=None
        m['validation']={'report_artifact_id':None,'declared_readiness':'Not ready','manual_checks':[]}
    files={
        'evidence/synthetic-design.md':'# Synthetic design evidence\n\nNot a live Figma response. Fixture section contains direct child frames frame-list (List, 390 x 844) and frame-detail (Detail, 390 x 844); no other pages. Static screenshots are simulated by this fixture description, not claimed as real screenshots. Prototype behavior is user-provided in the synthetic transcript.\n',
        'evidence/synthetic-baseline.md':'# Synthetic repository baseline\n\nNot a real repository scan. Fictional README declares a browser-only offline cards app. Existing index.html, src/app.js, src/styles.css and tests/manual.md exist in the simulated baseline. Old review specifications, task cards and approval records do not exist. Existing return selection is an observation, not product approval. No backend, shared package or native configuration is present in this synthetic tree.\n',
        'evidence/synthetic-audit.md':'# Synthetic audit attestations\n\nFor fixture testing only. This is not a real reviewer signature. The fictional source dialogue covers the exact shown P1/S1/T1 candidates. The fictional design describes two static frames; interactions come from the fictional user, not guessed prototype data. The seven specifications, plan and acceptance describe the same offline flow. The change fixture scan covers all eight named areas. Client execution and design connector access have not occurred.\n'
    }
    if persistence_reached:
        files['assets/IMG-001/1x/hero.svg']=asset_text
    if conditional:
        files['evidence/synthetic-audit.md']+='The font fixture freezes Demo Sans selection/license while delivery is a stated pending prerequisite; no automatic substitute font is approved.\n'
    bodies={
        'review_readme':['Current phase and machine state are indexed in [manifest](review-manifest.json). No implementation has been performed.','Only follow the current-stage next action; final outputs hand off to a separately authorized developer.','Decision states are synchronized below; see the decision register.'],
        'baseline':['Work units: '+json.dumps(m['baseline']['work_units'])+' Mode '+mode+'.','No repository exists for new mode. For change/mixed see synthetic-baseline.md; the external root is fictional, not a claim of local access.','Old specifications/task cards/approvals: Not applicable in new mode; absent in the simulated change baseline. Build a current baseline; never invent historical approval.'],
        'design_source':['Figma only. Exact candidate IDs frame-list and frame-detail; original simulated evidence in synthetic-design.md.','Static frames readable in the fixture model; prototype and authorship unavailable. No other design tool is evidence.','User interaction evidence comes from synthetic-transcript.md, not static geometry.'],
        'pages':['PG1: List, frame-list, 390 x 844, parent Section Demo, included page. PG2: Detail, frame-detail, 390 x 844, parent Section Demo, included page. Background rectangle is excluded non-page. Count: 2.','Frozen candidate P1 is presented with both IDs and explicit inclusion. Approval state resolves from the manifest.'],
        'resource_inventory':['R1: IMG-001 is a synthetic SVG image mapped to the two approved pages; the fixture explicitly records which dimensions are simulated evidence.','Resource set is approved only for this fixture. Its synthetic binary is saved only after the page/resource checkpoint, under the review root with dimensions, rights and save status recorded.','PAGE & RESOURCE CHECKPOINT: P1 pages and R1 resources are shown together; corrections create new candidate versions.','IMG-001: '+('EV-PAGES authorizes assets/IMG-001/1x/hero.svg; recorded SHA-256 matches the generated synthetic file.' if persistence_reached else 'EV-PAGES authorizes the pending post-confirmation save; no saved path or digest is claimed before persistence runs.')],
        'decisions':['The machine summary below is authoritative for statuses; narrative must agree.','DEC-FLOW: Cancel preserves selection; confirm clears it. Evidence E-USER, affected SP2, no silent default. '+('DEC-CHANGE approves the reviewed Cross-page change impact.' if mode!='new' else 'No change decision is required in new mode.'),'No unresolved decision is hidden from the conversation; synthetic entries are fixture evidence only.'],
        'spec0':['SP0: Visitors who want to inspect example cards without an account.','SP0: Let a visitor choose a card, inspect it and return without losing selection. Success: complete AC1 unaided.','Not applicable: no future backend/login promise is part of this exercise.'],
        'spec1':['SP1: H5 only; two pages, one primary list/detail flow and one clear confirmation dialog. Core priority: correct state and return behavior.','SP1: No login, network request, permissions, deep navigation, complex animation or persistence. Native platforms excluded.','SP1 scope confirmation: included pages, resource IMG-001 and H5 are explicit; all other platforms and features are out of scope.'],
        'spec2':['SP2 / INT1: frame-list, Open button, click, user-provided NAVIGATE intent, frame-detail, no animation, E-USER, readable as user instruction; see approval pointers. Prototype data unavailable.','SP2: Source List; Open chosen card -> Detail; parameter cardId must match the static list. Visible Back or browser Back returns to List with selected ID retained. Invalid ID shows a local error with Back, no network.','SP2 / DIALOG1: Clear button opens confirmation. Title Clear selection? Body This only clears the current choice. Cancel keeps it; Clear empties it. Overlay, close button and Escape cancel. Browser Back dismisses the dialog first and stays on List. No secret default action.','SP2: Initial no choice; chosen card; detail; dialog; empty after confirm; invalid-ID error/recovery. Waiting/network success/failure Not applicable because no asynchronous request is in scope.'],
        'spec3':['SP3: Match the two simulated 390 x 844 frames and labels List, Open, Detail, Back, Clear. Design tokens not observed: use existing browser defaults for this fixture only as explicitly approved user scope, not extracted token claims.','SP3: Use approved IMG-001 at 160 x 90 with contain/center behavior from R1. '+('Demo Sans fixed by E-ASSET; PRE-FONT blocks typography until file/license access is verified. No substitute may silently change the approved layout.' if conditional else 'Use system browser font; no additional external icons, images or fonts.')],
        'spec4':['SP4: Two fictional cards A/Example A and B/Example B. Only in-memory selectedId; no real personal data.','SP4: No API, logs with personal information, tokens, secrets, uploads or persistent storage. Reload resets selection. Never include real sample data.'],
        'spec5':['SP5: H5 in desktop Chromium at 390 x 844; keyboard and browser Back included. iOS/Android native Not applicable because outside scope.','SP5 / AC1: Select A, inspect Detail, Back retains A, open Clear, cancel retains A, confirm clears, reload resets, invalid ID recovers with Back. Check console/network/storage for no external calls or persistence. Evidence required: screenshot + recording; actual execution deferred to developer.'],
        'spec6':['SP6: No known accepted design deviation in the fictional baseline.','SP6: New difference must record ID, evidence, acceptance impact, owner only if known, disposition and user decision. Unknown authors remain null.'],
        'assessment_card':['This is the sole read-only technical assessment card. Specification S1 and EV-SPEC authorize analysis only, not code.','Read the indexed approved specs, baseline and external project README before necessary structural/source inspection. No source access in this synthetic fixture.','Propose exact file actions, component responsibilities, state/parameter/return/dialog behavior, dependencies, configuration, risks, platform verification and conditions. Plan can propose new architecture for one overall approval.'],
        'plan':['TECH1: '+('Create index.html (entry), src/app.js (ListView, DetailView, ConfirmDialog and selection/router state), src/styles.css (approved layout), tests/review-scenarios.md (AC1 manual steps).' if mode=='new' else 'Modify existing src/app.js (add Clear dialog, preserve List/Detail back behavior); reuse index.html and src/styles.css; extend tests/manual.md with cancel/confirm regression. '+('Create independent-web/index.html, independent-web/src/app.js and independent-web/src/styles.css for the new independent H5 work unit.' if mode=='mixed' else ''))+' These are planned paths, not written business code.',
                'TECH1: '+('Initialize a plain static H5 directory and document browser loading; no package manager, new SDK or native configuration. Choose no build dependency for this approved fictional exercise.' if mode=='new' else 'Retain existing static browser entry and no-dependency configuration; no replacement SDK or native changes. Mixed new work unit also uses plain static initialization.'),
                'TECH1: App owns selectedId and route; List/Detail receive callbacks; ConfirmDialog owns only visibility. cardId passes as an allowlisted ID; Back retains selection; invalid ID enters error. Cancel/overlay/close/Escape preserve selection; confirm clears it; browser Back closes dialog first. No eval() or external evaluation.',
                'TECH1: Use AC1 on H5, including browser Back and keyboard. Risk: route/state desynchronization; verify selection across repeated round trips and reload. Existing return tests remain required in change mode. No user-facing feature beyond S1.',
                'TECH1: '+('PRE-FONT blocks typography integration and validation. Do not start that affected action until the fixed file/license passes access check; unaffected scaffold/state work can proceed under downstream authority.' if conditional else 'Not applicable: no pending external asset/dependency prerequisite in this synthetic approved plan.')],
        'implementation_card':['Reuse S1, T1, EV-SPEC and EV-PLAN with the indexed frozen hashes. Do not regenerate or reconfirm the same unchanged plan.','Downstream verifies baseline and digests. Stop affected work if the repository, business scope or proposed implementation deviates; return for impact review.','TECH1 only, H5 only, exact indexed plan file scope. This Skill hands off and performs no development.','TECH1: '+('Typography blocked by PRE-FONT until resolution evidence; other authorized steps may proceed.' if conditional else 'No current condition. All out-of-scope login/network/native/Git actions remain unauthorized by this review.')],
        'approval_record':['EV-PAGES, EV-SPEC and EV-PLAN refer to synthetic-transcript.md and frozen target bytes in manifest. These are fixture approvals only.','Only PG1/PG2, SP0–SP6 and TECH1. Exclusions: login/network/native ports. '+('PRE-FONT is retained.' if conditional else 'No implementation preconditions.')],
        'handoff':['Synthetic expected status: '+m['validation']['declared_readiness']+'. Not a real client readiness certification.','Use manifest active assessment/implementation pointers and exact approved versions, not another same-named package.','Downstream checks hashes and baseline, clears affected conditions, implements only approved work under separate authority, and reports AC1 evidence. Changed scope returns for targeted review; no identical-plan loop.'],
        'validation_report':['Automated result must come from a validator run; this is the expected complete fixture output, not a record of client execution.','Synthetic attestations in evidence/synthetic-audit.md exercise required provenance/meaning/design/impact checks.','No real client, design connector, browser test or human signature.','Not applicable for the valid fixture: validator-negative variants document specific repairs.'],
        'change_request':['CH1: Add one clear-selection confirmation to an existing simulated H5 list/detail flow; preserve return state.','Old formal review docs do not exist. Current factual baseline: E-CODE and synthetic-baseline.md, fictional README/file/test inventory, E-DESIGN and E-USER. Do not invent old approvals.'],
        'change_impact':['CH1: Cross-page because shared selectedId crosses List and Detail; it is not Local merely because the screenshot marks one button.','All eight areas: '+json.dumps(m.get('changes',{}).get('CH1',{}).get('scan',{})), 'DEC-CHANGE records user approval of assessed scope/impact. Unknown impact cannot be made known by approval alone.'],
        'change_resource_diff':['Previous review has no formal resource inventory; establish that limitation instead of inventing historical asset approval. Current candidate is R1.','IMG-001: previous evidence/path unavailable; current evidence E-DESIGN and current location are recorded; status New for the current baseline; affects SP3 and AC1; DEC-CHANGE supplies the reviewed change decision; reconfirmation required.','Resource impact remains Cross-page because IMG-001 is used by both approved pages. The eight-area scan and DEC-CHANGE are recorded in CH1; no filename-only comparison or unknown-to-known shortcut is used.'],
        'change_attachment':['CH1 is supplementary scope/impact evidence only. No independent assessment or implementation authority.','Reference S1, CH1 impact report, ASSESS-1; after plan approval the standard IMPLEMENT-1 pointer supplies implementation scope. Do not create a second active implementation card.']
    }
    for artifact in m['artifacts'].values():
        evidence_ids = set(artifact['evidence_ids'])
        for iid in artifact['item_ids']:
            evidence_ids.update(m['items'][iid]['evidence_ids'])
        if artifact['role'] in ('design_source','pages'):
            evidence_ids.add('E-DESIGN')
        artifact['evidence_ids'] = sorted(evidence_ids)
    def summary():
        return {'stage':m['stage'],'versions':m['versions'],'active_cards':m['active_cards'],
                'decision_states':{k:{f:v[f] for f in CT['decision_summary_fields']} for k,v in m['decisions'].items()}}
    for aid,a in m['artifacts'].items():
        meta={'artifact_id':aid,'review_id':m['review_id'],'version':a['version'],
              'manifest':posixpath.relpath('review-manifest.json',posixpath.dirname(a['path']) or '.'),
              'design_source':m['design_source']['selected'],'scope_ids':m['design_source']['scope_ids'],
              'evidence_ids':a['evidence_ids'],'readability_limits':['Synthetic fixture evidence only.'],
              'item_ids':a['item_ids'],'depends_on':a['depends_on'],
              'approval_status_ref':'#/artifacts/'+aid+'/approval_status','approval_event_ids_ref':'#/artifacts/'+aid+'/approval_event_ids'}
        text='<!-- review-meta\n'+json.dumps(meta,indent=2)+'\n-->\n\n# '+m['project_name']+' — '+a['role']+'\n\n'
        text+='Approval status and events: resolve metadata pointers in review-manifest.json. This file is a synthetic frozen candidate, not a real user-approved business document.\n\n'
        if a['role'] in CT['summary_roles']:
            text+='<!-- review-summary\n'+json.dumps(summary(),indent=2)+'\n-->\n\n'
        for section,body in zip(CT['template_sections'][CT['roles'][a['role']][1]],bodies[a['role']]):
            text+='<!-- section:'+section.lower().replace(' ','-')+' -->\n## '+section+'\n\n'+body+'\n\n'
        files[a['path']]=text.rstrip()+'\n'
    for event in m['confirmation_events'].values():
        for target in event['targets'].values():
            target['sha256']=hashlib.sha256(files[target['path']].encode()).hexdigest()
    transcript='# Synthetic dialogue — not a real user transcript\n\n## Requirements\n\nThe fictional user requests two H5 pages, an offline card list/detail flow and one Clear confirmation. No login, network, persistent data or native platform. The user supplies the exact dialog/back/parameter semantics in SP2. This is test material, never current-session authorization.\n\n## Plan proposal\n\nThe fictional agent proposes the TECH1 architecture after the spec candidate; approval comes later, not before proposal.\n\n'
    if conditional: transcript+='## Font condition\n\nThe fictional user fixed Demo Sans and its license; the file transfer remains PRE-FONT. Do not substitute a different font or call typography immediately ready.\n\n'
    for eid,event in m['confirmation_events'].items():
        transcript+='## '+eid+'\n\nDisplayed candidate targets and digests:\n\n'+json.dumps(event['targets'],indent=2)+'\n\nFictional user response: '+event['source']['text']+'\n\n'
    files['evidence/synthetic-transcript.md']=transcript
    files['review-manifest.json']=json.dumps(m,indent=2)+'\n'
    return files

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description='Print a synthetic file map; does not write files.')
    p.add_argument('name'); p.add_argument('--mode',default='new'); p.add_argument('--conditional',action='store_true'); p.add_argument('--stage',default='handoff_validation')
    args=p.parse_args()
    print(json.dumps(build_fixture(args.name,args.mode,args.conditional,args.stage)))
