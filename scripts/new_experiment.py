from pathlib import Path
from datetime import datetime, timezone
import argparse, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments" / "records"
OUT.mkdir(parents=True, exist_ok=True)

def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "experiment"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--program", required=True,
                    choices=["FOUNDATIONS","RG","LATTICE","SPDE","BOOTSTRAP","ANALOGUES","BRIDGE"])
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    path = OUT / f"EXP-{stamp}-{slugify(args.title)}.md"

    body = f'''# {args.title}

- Experiment ID: `EXP-{stamp}`
- Program: `{args.program}`
- Created UTC: `{now.isoformat()}`
- Status: `PROPOSED`

## Question

## Baseline

## Hypothesis

## Prediction before execution

## Inputs / parameters

## Method

## Commands actually executed

## Raw evidence

## Observations

## What did not pass / was not checked

## Conclusion

## Claim type
`NUMERICAL_OBSERVATION | MACHINE_VERIFIED_RESULT | INFERENCE | HYPOTHESIS | REJECTED`

## Reproduction instructions

## Downstream impact
'''
    path.write_text(body, encoding="utf-8")
    print(path.relative_to(ROOT))

if __name__ == "__main__":
    main()
