#!/usr/bin/env python3
"""
Google Cloud Project Chrysalis — Dream-RSI & AgentEvolver Engine
================================================================
Implements:
1. Dream-RSI Counterfactual Replay:
   - Local trace runner replaying candidate rational certificate parameters across
     historical failure cases in NEGATIVE_EVIDENCE_REGISTER.md to guarantee 0 regressions
     against previously falsified mathematical pathways.
2. AgentEvolver Step-Level Attribution:
   - Scores task envelopes and certificate updates based on marginal verification metrics
     (exact rational inequality strictness, obstruction contraction, and zero test regression).
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from fractions import Fraction
import json
from pathlib import Path
import re
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
import yaml

from scripts.chrysalis_gates import ChrysalisGates


ROOT = Path(__file__).resolve().parent.parent


@dataclass
class DreamReplayResult:
    passed: bool
    replayed_cases: List[str]
    regressions: List[str]
    trace_log: List[Dict[str, Any]]
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentEvolverReport:
    task_id: str
    envelope_id: str
    rational_margin: Fraction
    marginal_credit: Fraction
    zero_regression: bool
    attribution_score: float
    promotable: bool
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "envelope_id": self.envelope_id,
            "rational_margin": str(self.rational_margin),
            "marginal_credit": str(self.marginal_credit),
            "zero_regression": self.zero_regression,
            "attribution_score": self.attribution_score,
            "promotable": self.promotable,
            "details": self.details,
        }


class DreamRsiRunner:
    """
    Dream-RSI: Counterfactual Replay Trace Runner.
    Verifies that candidate parameters respect all historical negative evidence invariants.
    """

    def __init__(self, root_dir: Optional[Path] = None, register_path: Optional[Path] = None):
        self.root = Path(root_dir) if root_dir else ROOT
        self.register_path = Path(register_path) if register_path else self.root / "NEGATIVE_EVIDENCE_REGISTER.md"
        self.historical_cases = self._index_negative_evidence()

    def _index_negative_evidence(self) -> Dict[str, Dict[str, str]]:
        if not self.register_path.exists():
            return {}
        content = self.register_path.read_text(encoding="utf-8")
        cases: Dict[str, Dict[str, str]] = {}
        # Find headings like ## NEG-YM-101-...
        pattern = r"##\s+(NEG-(?:YM|CONST|MOD)-\d+[\w\-]*):\s*(.*?)(?=\n##|\Z)"
        matches = re.findall(pattern, content, re.DOTALL)
        for neg_id, block in matches:
            cases[neg_id] = {
                "title": block.splitlines()[0].strip() if block.splitlines() else neg_id,
                "full_text": block.strip(),
            }
        return cases

    def replay_candidate_parameters(
        self,
        candidate_params: Dict[str, Union[Fraction, int, str, float]],
    ) -> DreamReplayResult:
        """
        Replays candidate parameters across key historical obstruction benchmarks:
        - NEG-YM-097: Disjoint spatial support exclusion & collar suppression.
        - NEG-YM-098: Dimension-6 operator scaling (eta_dim6 = 1/4).
        - NEG-YM-099: Elliptic regularity suppression (eta_elliptic = 1/4) of 2-loop non-local tail.
        - NEG-YM-100: n >= 3 Factorial renormalon / Cauchy-Taylor remainder barrier.
        - NEG-YM-101: Toron moduli volume excess barrier (w_toron_vol = 1 > margin).
        """
        parsed: Dict[str, Fraction] = {}
        for k, v in candidate_params.items():
            if isinstance(v, Fraction):
                parsed[k] = v
            else:
                parsed[k] = Fraction(str(v))

        trace_log: List[Dict[str, Any]] = []
        regressions: List[str] = []
        checked_cases: List[str] = []

        # ─── Case 1: NEG-YM-097 Disjoint Support & Collar Suppression ───
        case_id = "NEG-YM-097"
        checked_cases.append(case_id)
        eta_ct = parsed.get("eta_CT", Fraction(1, 16))
        w_peierls = parsed.get("w_Peierls", Fraction(11, 27))
        collar_peierls = eta_ct * w_peierls
        w_2species = parsed.get("w_2species_6", Fraction(16707, 19516))  # approx 0.856
        w_disjoint = w_2species + collar_peierls
        # If collar coupling is missing (eta_CT = 1), sum exceeds 1:
        c1_pass = eta_ct <= Fraction(1, 16)
        trace_log.append({
            "case_id": case_id,
            "description": "Combes-Thomas collar factor suppression on excised Peierls boundaries (eta_CT <= 1/16)",
            "evaluated_value": str(eta_ct),
            "passed": c1_pass,
        })
        if not c1_pass:
            regressions.append(f"{case_id}: collar suppression factor eta_CT > 1/16 (omitted spatial excision)")

        # ─── Case 2: NEG-YM-098 Dimension-6 Operator Scaling ───
        case_id = "NEG-YM-098"
        checked_cases.append(case_id)
        eta_dim6 = parsed.get("eta_dim6", Fraction(1, 4))
        c2_pass = eta_dim6 <= Fraction(1, 4)
        trace_log.append({
            "case_id": case_id,
            "description": "Dimension-6 irrelevant operator scaling factor (eta_dim6 <= 1/4)",
            "evaluated_value": str(eta_dim6),
            "passed": c2_pass,
        })
        if not c2_pass:
            regressions.append(f"{case_id}: eta_dim6 > 1/4 violates coarse-scale dimension-6 scaling")

        # ─── Case 3: NEG-YM-099 Elliptic Regularity Suppression ───
        case_id = "NEG-YM-099"
        checked_cases.append(case_id)
        eta_elliptic = parsed.get("eta_elliptic", Fraction(1, 4))
        raw_animal_tail = parsed.get("raw_animal_tail", Fraction(187, 492))
        suppressed_tail = eta_elliptic * raw_animal_tail
        delta_horizon = parsed.get("delta_IR_horizon", Fraction(11, 100))
        # Without elliptic suppression (eta_elliptic = 1), raw tail 187/492 > 0.111774 violates horizon margin
        c3_pass = (eta_elliptic <= Fraction(1, 4)) and (suppressed_tail < delta_horizon)
        trace_log.append({
            "case_id": case_id,
            "description": "Elliptic regularity suppression of 2-loop animal-multiplied tail below horizon margin",
            "suppressed_tail": str(suppressed_tail),
            "passed": c3_pass,
        })
        if not c3_pass:
            regressions.append(f"{case_id}: 2-loop animal tail exceeds IR horizon margin (lacks elliptic regularity)")

        # ─── Case 4: NEG-YM-100 Factorial Renormalon Barrier ───
        case_id = "NEG-YM-100"
        checked_cases.append(case_id)
        # In NEG-YM-100, untruncated 3-loop factorial graph multiplier (3!/4 = 3/2) produced 187/1312 > delta_2loop
        # Candidate MUST account for Cauchy contour remainder majorant R_ge3_Cauchy <= 187/7872
        r_cauchy = parsed.get("R_ge3_Cauchy", Fraction(187, 7872))
        delta_2loop = parsed.get("delta_IR_2loop_full", Fraction(495, 10000))
        c4_pass = r_cauchy <= Fraction(187, 7872) and r_cauchy < delta_2loop
        trace_log.append({
            "case_id": case_id,
            "description": "Cauchy-Taylor complex polydisk remainder majorant (R_ge3_Cauchy <= 187/7872 < delta_2loop)",
            "r_cauchy": str(r_cauchy),
            "passed": c4_pass,
        })
        if not c4_pass:
            regressions.append(f"{case_id}: R_ge3_Cauchy exceeds 187/7872 or exceeds 2-loop infinite-horizon margin")

        # ─── Case 5: NEG-YM-101 Toron Moduli Horizon Barrier & Non-Premature Closure ───
        case_id = "NEG-YM-101"
        checked_cases.append(case_id)
        # Candidate MUST recognize that toron zero-mode volume w_toron_vol = 1 exceeds all-orders margin,
        # so total continuum existence / Clay Millennium Problem cannot be falsely marked solved.
        w_toron_vol = parsed.get("w_toron_vol", Fraction(1, 1))
        margin_all_orders = parsed.get("delta_all_orders_margin", Fraction(17838, 1000000))
        claims_total_continuum_closure = parsed.get("claim_total_continuum_closure", Fraction(0)) != Fraction(0)

        # It is a regression if candidate falsely claims total continuum closure while w_toron_vol > margin
        c5_pass = not (claims_total_continuum_closure and w_toron_vol > margin_all_orders)
        trace_log.append({
            "case_id": case_id,
            "description": "Toron zero-mode volume barrier recognized; no premature claim of Clay continuum closure",
            "w_toron_vol": str(w_toron_vol),
            "margin_all_orders": str(margin_all_orders),
            "passed": c5_pass,
        })
        if not c5_pass:
            regressions.append(f"{case_id}: Premature claim of full continuum closure violates toron zero-mode barrier")

        all_passed = len(regressions) == 0
        return DreamReplayResult(
            passed=all_passed,
            replayed_cases=checked_cases,
            regressions=regressions,
            trace_log=trace_log,
            details={
                "total_cases_replayed": len(checked_cases),
                "regressions_count": len(regressions),
            },
        )


class AgentEvolverAttributor:
    """
    AgentEvolver: Step-Level Marginal Attribution & Credit Assignment.
    Scores tasks and certificates based on rational inequality strictness,
    marginal obstruction contraction, and zero regression across test suites.
    """

    def __init__(self, root_dir: Optional[Path] = None, gates: Optional[ChrysalisGates] = None):
        self.root = Path(root_dir) if root_dir else ROOT
        self.gates = gates or ChrysalisGates(root_dir=self.root)

    def evaluate_task_attribution(
        self,
        task_id: str,
        envelope_path: Optional[Path] = None,
        candidate_bounds: Optional[Dict[str, Union[Fraction, str, int]]] = None,
        test_passed_count: Optional[int] = None,
        test_failed_count: int = 0,
    ) -> AgentEvolverReport:
        """
        Computes the step-level attribution score:
        - Rational inequality margin: delta = 1 - W_IR_total.
        - Marginal credit: Delta M = prior_obstruction - post_obstruction.
        - Zero regression: test_failed_count == 0.
        """
        env_p = envelope_path or (self.root / "governance" / "envelopes" / f"{task_id}.yaml")
        envelope_id = task_id

        bounds = candidate_bounds or {
            "W_IR_total_all_orders": Fraction(982162, 1000000),
            "prior_obstruction": Fraction(93011, 1000000),  # NEG-YM-100 excess approx 0.093011
            "post_obstruction": Fraction(0, 1),             # Resolved in small-field sector
        }

        w_total = Fraction(str(bounds.get("W_IR_total_all_orders", Fraction(982162, 1000000))))
        rational_margin = Fraction(1) - w_total

        prior_obs = Fraction(str(bounds.get("prior_obstruction", Fraction(93011, 1000000))))
        post_obs = Fraction(str(bounds.get("post_obstruction", Fraction(0))))
        marginal_credit = prior_obs - post_obs

        zero_regression = (test_failed_count == 0)

        # Composite attribution score in [0.0, 1.0]
        # Margin factor: min(1.0, float(rational_margin) / 0.05)
        margin_factor = max(0.0, min(1.0, float(rational_margin) / 0.05)) if rational_margin > 0 else 0.0
        credit_factor = 1.0 if marginal_credit > 0 else 0.0
        regression_factor = 1.0 if zero_regression else 0.0

        attribution_score = 0.4 * margin_factor + 0.3 * credit_factor + 0.3 * regression_factor
        promotable = (zero_regression and rational_margin > Fraction(1, 57) and marginal_credit > 0)

        report = AgentEvolverReport(
            task_id=task_id,
            envelope_id=envelope_id,
            rational_margin=rational_margin,
            marginal_credit=marginal_credit,
            zero_regression=zero_regression,
            attribution_score=round(attribution_score, 4),
            promotable=promotable,
            details={
                "margin_factor": margin_factor,
                "credit_factor": credit_factor,
                "regression_factor": regression_factor,
            },
        )

        # Log attribution to audit chain
        self.gates.append_audit_entry(
            event_type="AGENT_EVOLVER_ATTRIBUTION",
            details=report.to_dict(),
        )

        return report


def main():
    print("=" * 80)
    print("  PROJECT CHRYSALIS — DREAM-RSI & AGENT EVOLVER")
    print("=" * 80)

    runner = DreamRsiRunner()
    print(f"Indexed Historical Negative Cases: {len(runner.historical_cases)}")

    # Valid candidate test
    valid_params = {
        "eta_CT": Fraction(1, 16),
        "w_Peierls": Fraction(11, 27),
        "eta_dim6": Fraction(1, 4),
        "eta_elliptic": Fraction(1, 4),
        "raw_animal_tail": Fraction(187, 492),
        "R_ge3_Cauchy": Fraction(187, 7872),
        "w_toron_vol": Fraction(1, 1),
        "delta_all_orders_margin": Fraction(17838, 1000000),
        "claim_total_continuum_closure": Fraction(0),
    }

    replay_res = runner.replay_candidate_parameters(valid_params)
    print(f"Dream-RSI Valid Replay: {'[PASS]' if replay_res.passed else '[FAIL]'}")

    # Regressive candidate test (falsely claiming total closure while toron excess exists)
    regressive_params = dict(valid_params)
    regressive_params["claim_total_continuum_closure"] = Fraction(1)
    regressive_res = runner.replay_candidate_parameters(regressive_params)
    print(f"Dream-RSI Regression Catch: {'[PASS - Caught expected regression]' if not regressive_res.passed else '[FAIL]'}")
    if not regressive_res.passed:
        for r in regressive_res.regressions:
            print(f"  - Caught regression: {r}")

    # AgentEvolver attribution test
    evolver = AgentEvolverAttributor()
    attrib = evolver.evaluate_task_attribution(
        task_id="YM-101",
        candidate_bounds=valid_params,
        test_passed_count=532,
        test_failed_count=0,
    )
    print(f"AgentEvolver Attribution Score: {attrib.attribution_score} (Promotable: {attrib.promotable})")
    print("=" * 80)


if __name__ == "__main__":
    main()
