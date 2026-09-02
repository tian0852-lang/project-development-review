#!/usr/bin/env python3
"""Read-only package checks. Stdlib only; not a general YAML or JSON Schema validator."""
import argparse
import json
import re
import sys
from pathlib import Path
from contract import PACKAGE, schema, check_shape, comment_json, markdown_links, link_errors

ADAPTERS = {
    'chatgpt': ('rules.md','invocation.md'),
    'codex': ('AGENTS.md.template','invocation.md'),
    'trae-work': ('rules.md','start-review-prompt.md'),
    'trae-code': ('rules.md','agent-prompt.md'),
    'cursor': ('rules.mdc','invocation.md'),
    'claude-code': ('CLAUDE.md.template','invocation.md'),
}
ALIASES = {
    'references/confirmation-gates.md': 'approval-gates.md',
    'references/language-policy.md': 'output-language-policy.md',
    'references/required-inputs.md': 'intake-and-baseline.md',
    'references/recommendation-policy.md': 'decision-policy.md',
    'templates/task-card.md': 'implementation-task-card.md',
    'templates/project-readme.md': 'review-readme.md',
    'templates/project-structure.md': 'artifact-contract.md',
}

def validate(root=PACKAGE):
    root = Path(root).resolve()
    errors, checks = [], []
    def fail(code, message):
        errors.append({'code':code,'message':message})
    def read(relative):
        try: return (root/relative).read_text(encoding='utf-8')
        except OSError:
            fail('MISSING_FILE',relative); return ''
    try:
        s=json.loads(read('schemas/review-manifest.schema.json'))
        ct=s['x-contract']
    except (ValueError, KeyError):
        return {'passed':False,'errors':errors or [{'code':'CONTRACT','message':'Unreadable schema contract'}]}
    version=read('VERSION').strip()
    if version!='2.2.1' or ct.get('version')!=version or s['properties']['schema_version'].get('const')!=version:
        fail('VERSION','VERSION/schema/core contract mismatch')
    required=['SKILL.md','README.md','README.zh-CN.md','CHANGELOG.md',
              'agents/openai.yaml','templates/review-manifest.json',
              'evals/README.md','evals/run_tests.py','evals/regenerate_fixtures.py','evals/update_expected_results.py',
              'evals/expected-results/verification-report.md','scripts/validate_review.py','scripts/contract.py',
              'references/platform-compatibility.md','references/resource-inventory.md','references/resource-persistence.md',
              'templates/resource-inventory.md','templates/resource-diff-report.md','adapters/fallback-contract.md']
    for relative in required:
        if not (root/relative).is_file(): fail('MISSING_FILE',relative)
    skill=read('SKILL.md')
    if not skill.startswith('---\n') or not re.search(r'^name: project-development-review$',skill,re.M):
        fail('SKILL_METADATA','Machine name or frontmatter missing')
    if not re.search(r'^description: .+',skill,re.M) or f'version: "{version}"' not in skill:
        fail('SKILL_METADATA','Description/version missing')
    if len(skill.splitlines())>160: fail('ENTRY_SIZE','SKILL.md must remain a short router (<=160 lines)')
    if 'display_name: "project-development-review"' not in read('agents/openai.yaml'):
        fail('DISPLAY_NAME','Agent display name mismatch')
    # Stage reads are mandatory links; source guides are mutually selected at runtime.
    for stage, names in ct['stage_routes'].items():
        lines=[line for line in skill.splitlines() if line.startswith('| '+stage+' |')]
        if len(lines)!=1:
            fail('STAGE_ROUTE',f'{stage}: one mandatory route row required'); continue
        for name in names:
            if f'(references/{name})' not in lines[0]: fail('STAGE_ROUTE',f'{stage}: missing linked read {name}')
            if not (root/'references'/name).is_file(): fail('MISSING_REFERENCE',name)
    if 'change-review.md' not in skill or 'during intake' not in read('references/workflow.md'):
        fail('CHANGE_ROUTE','Change/mixed must route impact rules during intake')
    stages=ct['stages']
    if not (stages.index('page_confirmation') < stages.index('resource_persistence') < stages.index('specification')):
        fail('RESOURCE_STAGE','Confirmed resources must be persisted or dispositioned before specification review.')
    for role, (_, template, stage) in ct['roles'].items():
        if stage not in ct['stages']: fail('ROLE_STAGE',role)
        text=read('templates/'+template)
        try:
            meta=comment_json(text,'review-meta')
            if set(ct['metadata_fields'])-set(meta): fail('TEMPLATE_META',template)
            if role in ct['summary_roles']: comment_json(text,'review-summary')
        except (ValueError,TypeError) as exc: fail('TEMPLATE_META',f'{template}: {exc}')
        for section in ct['template_sections'].get(template,[]):
            if '<!-- section:'+section.lower().replace(' ','-')+' -->' not in text:
                fail('TEMPLATE_SECTION',f'{template}: {section}')
        if not ct['template_sections'].get(template): fail('TEMPLATE_CONTRACT',template)
    try:
        tmpl=json.loads(read('templates/review-manifest.json'))
        missing=set(s['required'])-set(tmpl)
        if missing: fail('MANIFEST_TEMPLATE',str(sorted(missing)))
        if tmpl.get('schema_version')!=version: fail('VERSION','Manifest template')
    except ValueError: fail('MANIFEST_TEMPLATE','Invalid JSON')
    for relative,target in ALIASES.items():
        text=read(relative)
        if 'This file is a compatibility alias, not an active alternate contract.' not in text or target not in text or version not in text:
            fail('ALIAS',relative)
        if len(text.splitlines())>15: fail('ALIAS','Alias must route, not duplicate rules: '+relative)
    def block(text,name):
        match=re.search(r'<!-- '+name+r':start -->.*?<!-- '+name+r':end -->',text,re.S)
        return match.group(0) if match else ''
    base_rules=block(read('adapters/codex/AGENTS.md.template'),'gates')
    base_fallback=block(read('adapters/fallback-contract.md'),'fallback')
    for term in ['review-manifest.json','Figma or MasterGo','page inventory','resource inventory','Evidence is not approval',
                 'Open questions','never write business code','review_root/assets','never silently overwrite','Before handoff validate']:
        if term not in base_rules: fail('RULE_BOUNDARY',term)
    for term in ['Text-only delivery / not filesystem-validated','Recorded but unverified',
                 'Implementation pointer stays null','minimal safety fallback']:
        if term not in base_fallback: fail('FALLBACK_BOUNDARY',term)
    for name,(rule,prompt) in ADAPTERS.items():
        install=read(f'adapters/{name}/INSTALL.md')
        rt=read(f'adapters/{name}/{rule}'); pt=read(f'adapters/{name}/{prompt}')
        if version not in install or 'not run' not in install:
            fail('ADAPTER_EVIDENCE',name+': version and runtime caveat required')
        if block(rt,'gates')!=base_rules or f'core-version:{version}' not in rt:
            fail('ADAPTER_RULE_DRIFT',name)
        if block(pt,'fallback')!=base_fallback or f'core-version:{version}' not in pt:
            fail('ADAPTER_FALLBACK_DRIFT',name)
        for term in ['SKILL.md','review-manifest.json','workflow.md','approval-gates.md','conversation-output-contract.md',
                     'templates/review-manifest.json','technical-assessment-task-card.md','implementation-task-card.md']:
            if term not in pt: fail('ADAPTER_ROUTE',name+': '+term)
    cursor=read('adapters/cursor/rules.mdc')
    if not re.search(r'^alwaysApply: true$',cursor,re.M): fail('CURSOR_GATES','alwaysApply must be true')
    for p in ['adapters/cursor/commands/project-development-review.md','adapters/chatgpt/fallback-prompt.md']:
        if block(read(p),'fallback')!=base_fallback: fail('FALLBACK_DRIFT',p)
    # All package-contained Markdown links. Negative tests mutate temporary copies, not stored links.
    md_files=[p for p in root.rglob('*') if p.is_file() and p.suffix in ('.md','.mdc','.template')]
    for path in md_files:
        text=path.read_text(encoding='utf-8')
        for problem in link_errors(root,path,text):
            fail('LINK',str(path.relative_to(root))+': '+problem)
    # Reachability of canonical rules from the execution entry.
    seen=set(); todo=[root/'SKILL.md']
    while todo:
        path=todo.pop()
        if path in seen or not path.is_file(): continue
        seen.add(path)
        for _,target in markdown_links(path.read_text(encoding='utf-8')):
            if re.match(r'^[a-z]+:',target): continue
            target=(path.parent/target.split('#')[0]).resolve()
            if target.is_relative_to(root) and target.suffix=='.md': todo.append(target)
    canonical={root/'references'/n for names in ct['stage_routes'].values() for n in names}
    canonical.add(root/'references/change-review.md')
    for path in canonical-seen: fail('UNREACHABLE',str(path.relative_to(root)))
    for path in (root/'scripts').glob('*.py'):
        try: compile(path.read_text(),str(path),'exec')
        except SyntaxError as exc: fail('PYTHON_SYNTAX',str(exc))
    if not errors:
        checks=['Required files and names','Version consistency','Mandatory routes and reference reachability',
                'Template metadata and sections','Manifest template keys','Compatibility aliases',
                'Six persistent-rule and fallback contracts','Markdown local links','Python source syntax']
    return {'passed':not errors,'version':version,'markdown_files_checked':len(md_files),
            'automatic_passed':checks,'errors':errors,
            'not_proven':['Client discovery/runtime behavior','Natural-language correctness',
                          'Genuine user approval','External URL availability','General YAML/JSON Schema compliance']}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('package_root',nargs='?',default=str(PACKAGE))
    result=validate(p.parse_args().package_root)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['passed'] else 1)
