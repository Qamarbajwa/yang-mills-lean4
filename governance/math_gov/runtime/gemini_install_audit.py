#!/usr/bin/env python3
"""Read-only inspection of Gemini project's *claimed* MATH-GOV installation.

This can detect missing files/settings and compute local byte hashes. It cannot
authenticate owner approvals, hook execution, event capture, mathematical truth,
repo rights, isolated Lean, or live policy gates. ALWAYS release_authorized False.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

AUTHORITIES = ('governance/GOVERNANCE.md', 'governance/PROJECT_DIRECTION.md', 'governance/PROJECT_STATE.yaml')

def digest(path:Path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1_048_576),b''):h.update(b)
    return h.hexdigest()

def audit(root:Path,mode:str='unknown'):
    result={'verdict':'NOT_INSTALLED_OR_NOT_AUTHENTICATED','mode':mode,'project_root':str(root),
            'release_authorized':False,'independent_acceptance':False,
            'evidence_level':'LOCAL_FILE_OBSERVATIONS_ONLY','files':{},'checks':{},'missing':[],
            'unsupported':['live host authorization','independent reviewer and acceptor identity','actual Lean verification','full event completeness','OS permission isolation','Gemini hook execution']}
    if not root.is_dir():
        result['missing'].append('project directory inaccessible')
        return result
    for rel in AUTHORITIES:
        path=root / rel
        if path.is_symlink():
            result['missing'].append(f'symlink authority requires trusted resolution: {rel}')
        elif path.is_file():
            result['files'][rel]={'sha256':digest(path),'bytes':path.stat().st_size}
        else:result['missing'].append(rel)
    if mode == 'cli':
        instruction=root/'GEMINI.md'
        result['checks']['GEMINI.md_present']=instruction.is_file()
        if instruction.is_file():result['files']['GEMINI.md']={'sha256':digest(instruction),'bytes':instruction.stat().st_size}
        else:result['missing'].append('GEMINI.md')
        settings=root/'.gemini/settings.json'
        result['checks']['CLI_settings_present']=settings.is_file()
        if settings.is_file():
            result['files']['.gemini/settings.json']={'sha256':digest(settings),'bytes':settings.stat().st_size}
            try:
                config=json.loads(settings.read_text(encoding='utf-8'))
                hooks=config.get('hooks',{})
                before=hooks.get('BeforeTool',[]) if isinstance(hooks,dict) else []
                enabled=config.get('hooksConfig',{}).get('enabled',True) if isinstance(config.get('hooksConfig',{}),dict) else None
                has_before=isinstance(before,list) and any(isinstance(item,dict) and item.get('hooks') for item in before)
                result['checks']['BeforeTool_declared']=bool(has_before)
                result['checks']['hooks_not_explicitly_disabled']=enabled is True
                if not has_before:result['missing'].append('BeforeTool configuration absent')
                if enabled is not True:result['missing'].append('hooks disabled or uncertain')
            except (ValueError,TypeError,UnicodeError,AttributeError) as ex:
                result['checks']['CLI_settings_parse']='INVALID'
                result['missing'].append('Gemini settings malformed')
        else:result['missing'].append('.gemini/settings.json')
    elif mode=='adk':
        result['missing'].append('ADK external callback and tool-grant attestations unavailable to local scanner')
    else:
        result['missing'].append('host mode not confirmed as CLI/ADK; chat cannot enforce filesystem changes')
    try:
        p=subprocess.run(['git','-C',str(root),'rev-parse','HEAD'],capture_output=True,text=True,timeout=3)
        result['checks']['git_commit']=p.stdout.strip() if p.returncode == 0 else 'UNKNOWN'
    except (FileNotFoundError,subprocess.TimeoutExpired):
        result['checks']['git_commit']='UNKNOWN'
    result['checks']['authority_count_observed']=len([x for x in AUTHORITIES if x in result['files']])
    if not result['missing']:
        result['verdict']='CANDIDATE_FILES_PRESENT_EXTERNAL_VERIFICATION_REQUIRED'
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('project',type=Path);p.add_argument('--mode',choices=['cli','adk','chat','unknown'],default='unknown');args=p.parse_args()
    ans=audit(args.project,args.mode)
    print(json.dumps(ans,indent=2,ensure_ascii=False))
    sys.exit(0 if ans['verdict']=='CANDIDATE_FILES_PRESENT_EXTERNAL_VERIFICATION_REQUIRED' else 2)
