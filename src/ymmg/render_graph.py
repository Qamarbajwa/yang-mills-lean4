"""Regenerate Mermaid graph from the same governed node/edge input being validated."""
import argparse
import json
from pathlib import Path
try:
    from src.ymmg.math_step_engine import index_graph
except ImportError:
    try:
        from .math_step_engine import index_graph
    except (ImportError, ValueError):
        from math_step_engine import index_graph

def render(case):
    index,edges,errors=index_graph(case)
    if errors: raise ValueError('; '.join(errors))
    lines=['flowchart LR']
    aliases={ident:f'N{i}' for i,ident in enumerate(sorted(index))}
    for key in sorted(index):
        k=index[key]['kind']
        name=(key+' ('+k+')').replace('"','').replace('<','').replace('>','')
        lines.append(f'    {aliases[key]}["{name}"]')
    for source,target,kind,group in sorted(edges,key=str):
        label=kind if group is None else kind+':'+group
        lines.append(f'    {aliases[source]} -->|"{label}"| {aliases[target]}')
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--output');a=p.parse_args()
    txt=render(json.loads(Path(a.case).read_text()))
    if a.output: Path(a.output).write_text(txt)
    else:print(txt)

if __name__=='__main__': main()
