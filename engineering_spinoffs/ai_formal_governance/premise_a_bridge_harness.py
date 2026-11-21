"""
AI Formal Governance Sandbox: Zero-Trust Premise A -> Verdict Harness
======================================================================
Neuro-Symbolic compliance verification framework inspired by Lean 4 
"Bridge vs. Train" formal architecture.

Author: Qamar Munawer
Affiliation: Brandenburg University of Technology Cottbus-Senftenberg
Methodology: ai is being used as a tool
Epistemic Status: Practical engineering toolkit based on deterministic formal verification.
"""

import json
import hashlib
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional
from enum import Enum

class VerdictStatus(str, Enum):
    PROVEN_COMPLIANT = "PROVEN_COMPLIANT"
    PROVEN_VIOLATION = "PROVEN_VIOLATION"
    REJECTED_EPISTEMIC_VIOLATION = "REJECTED_EPISTEMIC_VIOLATION"
    INSUFFICIENT_PREMISE = "INSUFFICIENT_PREMISE"

@dataclass(frozen=True)
class MunicipalPremiseA:
    """
    Immutable Train: Structured architectural and municipal inputs extracted from BIM/CAD.
    """
    project_id: str
    plot_area_sqm: float
    total_built_up_area_sqm: float
    max_allowable_far: float
    occupancy_count: int
    egress_width_meters: float
    beam_span_meters: float
    beam_depth_meters: float
    front_setback_meters: float
    rear_setback_meters: float
    side_setback_meters: float

    def compute_sha256(self) -> str:
        serialized = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class ScientificPremiseA:
    """
    Immutable Train: Structured inputs for scientific and mathematical proofs.
    """
    claim_id: str
    finite_metric_name: str
    finite_metric_value: float
    finite_metric_floor: float
    lean4_certified: bool
    axioms_used: List[str]
    open_horizon_lock_active: bool
    claims_millennium_settled: bool

    def compute_sha256(self) -> str:
        serialized = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


class ZeroTrustMunicipalBridge:
    """
    Zero-Axiom Symbolic Municipal Code Compliance Bridge.
    Enforces deterministic statutory rules without LLM natural language ambiguity.
    """
    MIN_EGRESS_PER_PERSON_M = 0.005
    MIN_BASE_EGRESS_M = 1.20
    MAX_SPAN_TO_DEPTH_RATIO = 20.0
    MIN_FRONT_SETBACK_M = 3.0
    MIN_REAR_SETBACK_M = 3.0
    MIN_SIDE_SETBACK_M = 2.0

    @classmethod
    def verify(cls, premise: MunicipalPremiseA) -> Dict[str, Any]:
        violations = []
        
        # Rule 1: Floor Area Ratio (FAR)
        if premise.plot_area_sqm <= 0:
            return {
                "verdict": VerdictStatus.INSUFFICIENT_PREMISE,
                "reason": "Plot area must be strictly positive.",
                "premise_hash": premise.compute_sha256()
            }
        
        actual_far = premise.total_built_up_area_sqm / premise.plot_area_sqm
        if actual_far > premise.max_allowable_far + 1e-6:
            violations.append(f"FAR violation: actual {actual_far:.3f} exceeds maximum {premise.max_allowable_far:.3f}")
            
        # Rule 2: Fire Egress Width
        required_egress = max(cls.MIN_BASE_EGRESS_M, premise.occupancy_count * cls.MIN_EGRESS_PER_PERSON_M)
        if premise.egress_width_meters < required_egress - 1e-6:
            violations.append(f"Egress width violation: provided {premise.egress_width_meters:.2f} m < required {required_egress:.2f} m")
            
        # Rule 3: Structural Span-to-Depth Ratio
        if premise.beam_depth_meters <= 0:
            violations.append("Beam depth must be strictly positive.")
        else:
            span_ratio = premise.beam_span_meters / premise.beam_depth_meters
            if span_ratio > cls.MAX_SPAN_TO_DEPTH_RATIO + 1e-6:
                violations.append(f"Structural deflection violation: span/depth ratio {span_ratio:.2f} exceeds limit {cls.MAX_SPAN_TO_DEPTH_RATIO:.2f}")
                
        # Rule 4: Mandatory Boundary Setbacks
        if premise.front_setback_meters < cls.MIN_FRONT_SETBACK_M - 1e-6:
            violations.append(f"Front setback violation: {premise.front_setback_meters:.2f} m < {cls.MIN_FRONT_SETBACK_M:.2f} m")
        if premise.rear_setback_meters < cls.MIN_REAR_SETBACK_M - 1e-6:
            violations.append(f"Rear setback violation: {premise.rear_setback_meters:.2f} m < {cls.MIN_REAR_SETBACK_M:.2f} m")
        if premise.side_setback_meters < cls.MIN_SIDE_SETBACK_M - 1e-6:
            violations.append(f"Side setback violation: {premise.side_setback_meters:.2f} m < {cls.MIN_SIDE_SETBACK_M:.2f} m")

        if len(violations) == 0:
            return {
                "verdict": VerdictStatus.PROVEN_COMPLIANT,
                "premise_hash": premise.compute_sha256(),
                "actual_far": actual_far,
                "required_egress_m": required_egress,
                "span_to_depth": premise.beam_span_meters / premise.beam_depth_meters,
                "violations": []
            }
        else:
            return {
                "verdict": VerdictStatus.PROVEN_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "actual_far": actual_far,
                "violations": violations
            }


class ZeroTrustScientificBridge:
    """
    Epistemic Scientific Verification Bridge.
    Enforces honest boundaries between certified finite mathematics and open infinite horizons.
    """
    STANDARD_LEAN4_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}

    @classmethod
    def verify(cls, premise: ScientificPremiseA) -> Dict[str, Any]:
        # Epistemic Rule 1: No claim of an open Millennium Problem being settled is permitted.
        if premise.claims_millennium_settled:
            return {
                "verdict": VerdictStatus.REJECTED_EPISTEMIC_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "reason": "Epistemic lock violation: Clay Millennium Problems remain strictly OPEN. Claims of unconditional settlement are rejected."
            }
            
        # Epistemic Rule 2: Open horizon lock must be explicitly active.
        if not premise.open_horizon_lock_active:
            return {
                "verdict": VerdictStatus.REJECTED_EPISTEMIC_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "reason": "Epistemic lock violation: open_horizon_lock must be set to True."
            }
            
        # Verification Rule 3: Finite metric floor
        if premise.finite_metric_value < premise.finite_metric_floor:
            return {
                "verdict": VerdictStatus.PROVEN_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "reason": f"Finite metric {premise.finite_metric_name} = {premise.finite_metric_value} below floor {premise.finite_metric_floor}."
            }
            
        # Verification Rule 4: Lean 4 certification and standard axioms
        if not premise.lean4_certified:
            return {
                "verdict": VerdictStatus.PROVEN_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "reason": "Lean 4 kernel certificate is required."
            }
            
        custom_axioms = set(premise.axioms_used) - cls.STANDARD_LEAN4_AXIOMS
        if len(custom_axioms) > 0:
            return {
                "verdict": VerdictStatus.PROVEN_VIOLATION,
                "premise_hash": premise.compute_sha256(),
                "reason": f"Non-standard custom axioms detected: {list(custom_axioms)}"
            }

        return {
            "verdict": VerdictStatus.PROVEN_COMPLIANT,
            "premise_hash": premise.compute_sha256(),
            "claim_id": premise.claim_id,
            "finite_metric": premise.finite_metric_name,
            "metric_margin": premise.finite_metric_value - premise.finite_metric_floor,
            "axioms_verified": list(premise.axioms_used),
            "epistemic_status": "verified-finite"
        }


def run_governance_benchmark(output_path: str = "ai_formal_governance_receipt.json") -> Dict[str, Any]:
    """
    Executes governance test cases and exports audit receipts.
    """
    # Test case 1: Valid compliant building plan
    valid_building = MunicipalPremiseA(
        project_id="BTU_CAMPUS_AUDITORIUM_01",
        plot_area_sqm=2500.0,
        total_built_up_area_sqm=3750.0, # FAR = 1.50
        max_allowable_far=2.00,
        occupancy_count=400,
        egress_width_meters=2.40,        # required: max(1.20, 400*0.005=2.00) -> 2.40 >= 2.00
        beam_span_meters=12.0,
        beam_depth_meters=0.80,          # ratio: 12/0.8 = 15.0 <= 20.0
        front_setback_meters=5.0,
        rear_setback_meters=4.0,
        side_setback_meters=3.0
    )
    res_bldg = ZeroTrustMunicipalBridge.verify(valid_building)
    
    # Test case 2: Valid honest scientific claim
    valid_science = ScientificPremiseA(
        claim_id="YM_T02_COVOLUME_TARE",
        finite_metric_name="cavity_tare_energy",
        finite_metric_value=65.4505,
        finite_metric_floor=0.0,
        lean4_certified=True,
        axioms_used=["propext", "Classical.choice", "Quot.sound"],
        open_horizon_lock_active=True,
        claims_millennium_settled=False
    )
    res_sci = ZeroTrustScientificBridge.verify(valid_science)
    
    receipt = {
        "benchmark_name": "AI Formal Governance Premise A -> Verdict Sandbox",
        "author": "Qamar Munawer",
        "affiliation": "Brandenburg University of Technology Cottbus-Senftenberg",
        "methodology": "ai is being used as a tool",
        "epistemic_status": "verified-finite deterministic formal governance",
        "municipal_verification": res_bldg,
        "scientific_verification": res_sci,
        "overall_status": "PASS" if (
            res_bldg["verdict"] == VerdictStatus.PROVEN_COMPLIANT and 
            res_sci["verdict"] == VerdictStatus.PROVEN_COMPLIANT
        ) else "FAIL"
    }
    
    with open(output_path, "w") as f:
        json.dump(receipt, f, indent=2)
        
    return receipt


if __name__ == "__main__":
    import sys
    out_file = sys.argv[1] if len(sys.argv) > 1 else "ai_formal_governance_receipt.json"
    res = run_governance_benchmark(out_file)
    print("=" * 60)
    print("AI Formal Governance Sandbox Results:")
    print(f"Overall Status: {res['overall_status']}")
    print(f"Municipal Verdict: {res['municipal_verification']['verdict']}")
    print(f"Scientific Verdict: {res['scientific_verification']['verdict']}")
    print(f"Receipt written to: {out_file}")
    print("=" * 60)
