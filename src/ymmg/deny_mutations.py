#!/usr/bin/env python3
"""Gemini CLI preliminary read-only hook, not a security sandbox.

ALL unknown or write-capable tools are blocked. Allowed read-only names are limited
and are version-dependent; verify names in your actual host. Malformed input is
blocked via exit code 2. Do not grant access to secrets through a readable tool.
Agent/admin may be able to disable project hooks: use external OS/repo ACL as well.
"""
import json, sys

READ_ONLY = {'read_file', 'glob', 'grep', 'list_directory'}

def decide(payload):
    if not isinstance(payload,dict): return False,'Malformed hook payload'
    name=payload.get('tool_name')
    args=payload.get('tool_input')
    if not isinstance(name,str) or not isinstance(args,dict):
        return False,'Missing tool name or tool arguments'
    if name in READ_ONLY:
        return True,'ALLOW_ADVISORY_READ_ONLY'
    return False,f'READ_ONLY_ADOPTION: {name} is not explicitly permitted'

if __name__ == '__main__':
    try:
        incoming=json.load(sys.stdin)
        ok,reason=decide(incoming)
        if ok:
            sys.stdout.write('{}\n')
            sys.exit(0)
        print(reason,file=sys.stderr)
        sys.exit(2)
    except SystemExit:
        raise
    except Exception as err:
        print(f'READ_ONLY_ADOPTION_BLOCKED: {type(err).__name__}',file=sys.stderr)
        sys.exit(2)
