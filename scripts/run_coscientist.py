#!/usr/bin/env python3
"""
Yang-Mills Research Co-Scientist Discovery & Formal Verification CLI
====================================================================
Runs a governed Co-Scientist discovery cycle targeting Yang-Mills IR
crossover obstructions (NEG-YM-101 / Lemmas YM-059F, YM-060F, YM-101F):
1. Generates distinct mathematical pathways + adversarial falsification control.
2. Enforces fail-closed ResearchGateKernel stage transitions & quarantine.
3. Evaluates blinded A/B + B/A Elo tournaments.
4. Breeds cross-mechanism hybrid candidate (with full state/Elo reset).
5. Runs independent verification bridge (Exact Rational + Dream-RSI + Chrysalis + Live Lean 4.35).
6. Prints Pareto rankings and proof obligations while preserving OPEN_AND_UNSOLVED truth.

Usage:
    python scripts/run_coscientist.py
    python scripts/run_coscientist.py --no-lean
"""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.ymmg.coscientist import YangMillsCoScientistOrchestrator


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Yang-Mills Research Co-Scientist Discovery Cycle")
    parser.add_argument("--no-lean", action="store_true", help="Skip live Lean 4.35 kernel check (sub-lemma proofs will remain unverified)")
    parser.add_argument("--json", action="store_true", help="Output structured JSON report")
    args = parser.parse_args()

    orch = YangMillsCoScientistOrchestrator(root_dir=ROOT)
    enable_lean = not args.no_lean
    res = orch.run_discovery_cycle(
        enable_lean=enable_lean,
        require_lean_for_proof=True,
        include_adversarial_flawed=True,
    )

    if args.json:
        payload = {
            "goal": res["goal"].goal_id,
            "clay_problem": res["clay_problem"],
            "meta_report": {
                "run_id": res["meta_report"].run_id,
                "total_hypotheses": res["meta_report"].total_hypotheses,
                "pareto_top_ids": res["meta_report"].pareto_top_ids,
                "quarantined_ids": res["meta_report"].quarantined_ids,
                "verified_claims_ids": res["meta_report"].verified_claims_ids,
                "recurring_failures": res["meta_report"].recurring_failures,
                "next_proof_obligations": res["meta_report"].next_proof_obligations,
                "epistemic_status": res["meta_report"].epistemic_status,
                "summary": res["meta_report"].summary,
            },
            "hypotheses": [
                {
                    "id": h.hypothesis_id,
                    "family": h.mechanism_family,
                    "proposal_state": h.proposal_state,
                    "formal_state": h.formal_state,
                    "elo": round(h.elo, 2),
                }
                for h in sorted(res["hypotheses"].values(), key=lambda x: x.elo, reverse=True)
            ],
        }
        print(json.dumps(payload, indent=2))
        return 0

    meta = res["meta_report"]
    print("=" * 80)
    print("  YANG-MILLS RESEARCH CO-SCIENTIST OS — DISCOVERY & VERIFICATION REPORT")
    print("=" * 80)
    print(f"  Goal ID          : {res['goal'].goal_id}")
    print(f"  Target Barrier   : {res['goal'].target_obstruction}")
    print(f"  Clay Status      : {res['clay_problem']} (Honest Epistemic Guard Active)")
    print(f"  Total Candidates : {meta.total_hypotheses}")
    print("-" * 80)
    print("  HYPOTHESIS LEADERBOARD & FORMAL VERIFICATION STATUS:")
    for h in sorted(res["hypotheses"].values(), key=lambda x: x.elo, reverse=True):
        vrep = res["verification_reports"].get(h.hypothesis_id)
        lean_info = f" | Lean: {vrep.lean_status}" if vrep else ""
        print(
            f"  - {h.hypothesis_id:<36} | Stage: {h.proposal_state:<14} "
            f"| Elo: {h.elo:>6.1f} | Formal: {h.formal_state:<14}{lean_info}"
        )
    print("-" * 80)
    print(f"  Quarantined      : {', '.join(meta.quarantined_ids) or 'None'}")
    print(f"  Pareto Top 3     : {', '.join(meta.pareto_top_ids)}")
    print(f"  Sub-Lemmas Proved: {', '.join(meta.verified_claims_ids) or 'None'}")
    print("  Next Proof Obligations:")
    for ob in meta.next_proof_obligations:
        print(f"    * {ob}")
    print("=" * 80)
    print(f"  Summary: {meta.summary}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
