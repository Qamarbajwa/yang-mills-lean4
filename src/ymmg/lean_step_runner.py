"""Lean step-verification adapter for a TRUSTED, externally sandboxed host.

IMPORTANT: Running Lean code executes build macros and plugins; this Python file is
NOT a sandbox. Use in a container/VM with no secrets, network or write access to
protected repositories. Do not call untrusted JSON tool outputs 'verified'.

If Lean/Lake is unavailable, returns LEAN_UNAVAILABLE. No simulated Lean passes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

SAFE_ID = re.compile(r'\A[A-Za-z_][A-Za-z0-9_\.]*\Z')
ALLOWED_AXIOMS = {'propext','Classical.choice','Quot.sound'}


def sha(raw): return hashlib.sha256(raw).hexdigest()


def failed(reason, extra=None):
    out={'verdict':reason,'lean_kernel_check_passed':False,
         'proof_complete':False,'semantics_independently_audited':False,
         'release_authorized':False}
    if extra: out.update(extra)
    return out


def extract_axioms(raw, theorem):
    # Printed diagnostics are informational and cannot authenticate an untrusted execution.
    # These formats are matched against Lean's standard #print axioms output.
    regex = r"['\"]?" + re.escape(theorem) + r"['\"]?"
    clean=re.search(r'(?:^|\n)(?:[^\n]*?\s)?'+regex+r' does not depend on any axioms',raw)
    if clean: return []
    line=re.search(r'(?:^|\n)(?:[^\n]*?\s)?'+regex+r' depends on axioms:\s*\[([^\]]*)\]',raw)
    if line: return [x.strip() for x in line.group(1).split(',') if x.strip()]
    return None


def check_step(project_root, relative_source, theorem, expected_statement,
               expected_file_sha256, timeout=120):
    """Compile a frozen Lean file and generate a checking wrapper.

    - Expected statement is supplied by an independently pinned review contract,
      NOT generated from the worker's theorem declaration.
    - A source SHA-256 is compared before and after execution.
    - Does not grant mathematical acceptance or independence from compiler/library.
    - Source must be reviewed before it is ever run; server must sandbox the toolchain.
    """
    try:
        root=Path(project_root).resolve(strict=True)
        rel=Path(relative_source)
        if rel.is_absolute() or '..' in rel.parts or rel.suffix!='.lean':
            return failed('SOURCE_PATH_DENIED')
        candidate=root/rel
        if candidate.is_symlink() or not candidate.is_file() or candidate.resolve().is_relative_to(root) is False:
            return failed('SOURCE_PATH_DENIED')
        if not SAFE_ID.fullmatch(theorem or ''):
            return failed('INVALID_THEOREM_NAME')
        if not isinstance(expected_statement,str) or not expected_statement.strip():
            return failed('MISSING_APPROVED_FORMAL_STATEMENT')
        if re.fullmatch(r'[0-9a-f]{64}',expected_file_sha256 or '') is None:
            return failed('INVALID_PINNED_SOURCE_DIGEST')
        src=candidate.read_bytes()
        if sha(src)!=expected_file_sha256:
            return failed('STALE_OR_CHANGED_SOURCE',{'observed_sha256':sha(src)})
        # Project and dependency locks required; loose scripts are insufficient for formal acceptance.
        toolchain=root/'lean-toolchain'; manifest=root/'lake-manifest.json'
        if not toolchain.is_file() or not manifest.is_file() or not (root/'lakefile.toml').is_file() and not (root/'lakefile.lean').is_file():
            return failed('UNPINNED_LEAN_PROJECT')
        if not shutil.which('lake'):
            return failed('LEAN_UNAVAILABLE',{'detail':'lake executable not installed or not on PATH'})
        # Append the independent statement obligation and axiom query to the exact source.
        # The source may have a namespace; theorem is expected to be fully qualified.
        wrapper=(src.decode('utf-8')+f'\n\nexample : ({expected_statement}) := by\n  exact {theorem}\n'+
                 f'\n#print axioms {theorem}\n')
        # Keep temporary file outside project; LEAN_PATH is resolved via lake env and cwd.
        with tempfile.TemporaryDirectory(prefix='mathgov_lean_') as d:
            temp=Path(d)/'Check.lean'; temp.write_bytes(wrapper.encode('utf-8'))
            try:
                run=subprocess.run(['lake','env','lean',str(temp)],cwd=root,
                                   capture_output=True,text=True,timeout=timeout,
                                   env=None,check=False)
            except subprocess.TimeoutExpired:
                return failed('LEAN_TIMEOUT')
        if candidate.read_bytes()!=src: return failed('SOURCE_MUTATED_DURING_LEAN_RUN')
        # Never claim a pass just because a command exited zero: require exact axiom report.
        stdout=run.stdout or ''; stderr=run.stderr or ''; combined=stdout+'\n'+stderr
        details={'source_sha256':sha(src),'lean_tool_stdout_sha256':sha(stdout.encode()),
                 'lean_tool_stderr_sha256':sha(stderr.encode()),'returncode':run.returncode,
                 'toolchain_pin_sha256':sha(toolchain.read_bytes()),
                 'manifest_sha256':sha(manifest.read_bytes()),
                 'theorem':theorem,'formal_statement_sha256':sha(expected_statement.encode())}
        if run.returncode!=0 or re.search(r'(^|\n)[^\n]*(error:|warning:)',combined):
            return failed('LEAN_COMPILATION_OR_WARNING',details)
        axioms=extract_axioms(combined,theorem)
        if axioms is None: return failed('AXIOM_REPORT_MISSING',details)
        details['axioms']=axioms
        disallowed=sorted(set(axioms)-ALLOWED_AXIOMS)
        if disallowed: return failed('DISALLOWED_AXIOMS',dict(details,disallowed_axioms=disallowed))
        # This only asserts a local, non-authenticated Lean-process result in an assumed trusted host.
        # Independent runner and meaning audit are separate mandatory gates.
        return {'verdict':'LOCAL_LEAN_STEP_CHECK_PASS_PENDING_INDEPENDENT_RECHECK',
                'lean_kernel_check_passed':True,'proof_complete':False,
                'semantics_independently_audited':False,'release_authorized':False,**details}
    except (OSError,ValueError,UnicodeError,TypeError) as e:
        return failed('LEAN_RUNNER_ERROR',{'detail':type(e).__name__+': '+str(e)[:300]})


def main():
    p=argparse.ArgumentParser(description='Local Lean preflight; must be run by a trusted sandbox host')
    p.add_argument('project_root'); p.add_argument('source'); p.add_argument('theorem')
    p.add_argument('--statement-file',required=True,help='Approved goal file owned outside worker source')
    p.add_argument('--source-sha256',required=True)
    p.add_argument('--timeout',type=int,default=120)
    args=p.parse_args()
    try:
        statement=Path(args.statement_file).read_text(encoding='utf-8').strip()
        result=check_step(args.project_root,args.source,args.theorem,statement,args.source_sha256,args.timeout)
    except (OSError,ValueError) as e: result=failed('STATEMENT_FILE_UNAVAILABLE',{'detail':str(e)})
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
