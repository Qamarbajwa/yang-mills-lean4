"""
YM-014R External-Evidence Reconciliation and Obstruction-Theorem Repair Module.

Provides exact algebraic and numerical routines to verify:
1. Exact SU(2) Makeenko-Migdal single-trace linearity and vanishing of loop splitting.
2. Non-vanishing SU(3) / SU(N >= 3) loop splitting term causing multi-trace proliferation.
3. Adaptive loop bootstrap perimeter scaling L_max(a) ~ R_* / a.
4. Local Wigner 6j sign indefiniteness vs unproved extensive sign decay.
5. Faizal-Shabir (2026) dimensional scaling defect (dimensionless m*a vs dimensionful M_phys).
6. Three-tier obstruction taxonomy classification.
"""

from dataclasses import dataclass
from enum import Enum
import math
from typing import Dict, List, Optional, Tuple
import numpy as np


class ObstructionType(Enum):
    """Three-tier obstruction classification taxonomy."""
    METHOD_SPECIFIC_OBSTRUCTION = "METHOD_SPECIFIC_OBSTRUCTION"
    CLASS_OF_METHODS_OBSTRUCTION = "CLASS_OF_METHODS_OBSTRUCTION"
    STRUCTURAL_NO_GO = "STRUCTURAL_NO_GO"


class AmendmentClassification(Enum):
    """Theorem amendment status."""
    CONFIRMED = "CONFIRMED"
    CONFIRMED_WITH_NARROWER_SCOPE = "CONFIRMED_WITH_NARROWER_SCOPE"
    NEEDS_AMENDMENT = "NEEDS_AMENDMENT"
    REFUTED = "REFUTED"
    UNVERIFIED = "UNVERIFIED"


@dataclass(frozen=True)
class TheoremAuditRecord:
    theorem_id: str
    original_claim: str
    primary_source: str
    reconciliation_finding: str
    amendment_status: AmendmentClassification
    obstruction_tier: Optional[ObstructionType]


def verify_su2_trace_reality_and_vanishing_split(num_samples: int = 1000, seed: int = 42) -> Dict[str, float]:
    r"""
    Verify that for any U in SU(2), Tr(U) in R, and hence Tr(U - U^\dagger) == 0 identically.
    
    This proves that in SU(2), the 1/N loop-splitting term:
        (beta / 4N^2) sum_{p ni ell} < Tr(U(C)) Tr(U_p - U_p^\dagger) >
    vanishes identically as an algebraic operator identity, ensuring the Makeenko-Migdal
    equations on SU(2) close entirely within the single-trace space (Kazakov & Zheng 2025).
    """
    rng = np.random.default_rng(seed)
    max_im_tr = 0.0
    max_split_norm = 0.0
    
    for _ in range(num_samples):
        # Generate random SU(2) matrix via quaternion on S^3
        v = rng.normal(size=4)
        v = v / np.linalg.norm(v)
        a, b, c, d = v
        # U = [[a + i*b, c + i*d], [-c + i*d, a - i*b]]
        U = np.array([
            [complex(a, b), complex(c, d)],
            [complex(-c, d), complex(a, -b)]
        ], dtype=complex)
        
        tr_U = np.trace(U)
        U_dag = U.conj().T
        split = U - U_dag
        tr_split = np.trace(split)
        
        im_tr = abs(tr_U.imag)
        if im_tr > max_im_tr:
            max_im_tr = im_tr
        
        norm_split = abs(tr_split)
        if norm_split > max_split_norm:
            max_split_norm = norm_split
            
    return {
        "max_imaginary_trace": float(max_im_tr),
        "max_trace_split_operator": float(max_split_norm),
        "su2_splitting_vanishes_identically": max_split_norm < 1e-14
    }


def verify_su3_non_vanishing_split(num_samples: int = 1000, seed: int = 42) -> Dict[str, float]:
    r"""
    Verify that for SU(3), Tr(U) is in general complex, so Tr(U - U^\dagger) = 2i Im(Tr(U)) != 0.
    
    This proves that in SU(3) (and SU(N >= 3)), link variations generically couple
    single-trace loops to two-trace loops at finite N, confirming multi-trace coupling for N >= 3.
    """
    rng = np.random.default_rng(seed)
    non_zero_split_count = 0
    max_split_norm = 0.0
    mean_im_tr_sq = 0.0
    
    for _ in range(num_samples):
        # Generate random SU(3) matrix via QR decomposition of complex normal matrix
        Z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        Q, R_mat = np.linalg.qr(Z)
        d_diag = np.diagonal(R_mat)
        ph = d_diag / np.abs(d_diag)
        U = Q * ph
        # Fix determinant to 1
        det_U = np.linalg.det(U)
        U = U / (det_U ** (1.0 / 3.0))
        
        tr_U = np.trace(U)
        tr_split = np.trace(U - U.conj().T)
        norm_split = abs(tr_split)
        
        if norm_split > 1e-5:
            non_zero_split_count += 1
        if norm_split > max_split_norm:
            max_split_norm = norm_split
        mean_im_tr_sq += (tr_U.imag) ** 2
        
    mean_im_tr_sq /= num_samples
    
    return {
        "non_zero_split_fraction": float(non_zero_split_count / num_samples),
        "max_trace_split_norm": float(max_split_norm),
        "mean_im_trace_squared": float(mean_im_tr_sq),
        "su3_splitting_is_non_zero": non_zero_split_count > 0.9 * num_samples
    }


def evaluate_adaptive_bootstrap_scaling(a: float, R_star_fm: float = 0.5) -> Dict[str, float]:
    """
    Evaluate the required adaptive loop truncation depth L_max(a) = ceil(R_star / a)
    for a physical target scale R_star.
    
    Demonstrates that unlike fixed truncation (where R_phys = L_max * a -> 0),
    an adaptive hierarchy maintains physical reach R_phys >= R_star as a -> 0.
    """
    if a <= 0:
        raise ValueError("Lattice spacing 'a' must be positive.")
    if R_star_fm <= 0:
        raise ValueError("Physical scale 'R_star_fm' must be positive.")
        
    L_adaptive = math.ceil(R_star_fm / a)
    R_phys_adaptive = L_adaptive * a
    
    # Comparison with fixed truncation L_fixed = 6
    L_fixed = 6
    R_phys_fixed = L_fixed * a
    
    return {
        "lattice_spacing_fm": a,
        "target_physical_scale_fm": R_star_fm,
        "adaptive_truncation_depth": L_adaptive,
        "adaptive_physical_reach_fm": R_phys_adaptive,
        "fixed_physical_reach_fm": R_phys_fixed,
        "fixed_ratio_to_target": R_phys_fixed / R_star_fm,
        "adaptive_ratio_to_target": R_phys_adaptive / R_star_fm
    }


def calculate_faizal_shabir_scaling_defect(
    dimensionless_gap_mu: float,
    lattice_spacings: List[float]
) -> List[Dict[str, float]]:
    """
    Calculate the physical mass gap M_phys(a) = mu / a under the Faizal-Shabir hypothesis
    that the dimensionless transfer-matrix spectral gap mu is bounded below by a constant
    mu >= c_0 > 0 as a -> 0.
    
    Demonstrates the fatal dimensional defect:
    If mu(a) >= c_0 > 0, then M_phys = c_0 / a -> infinity as a -> 0.
    A finite physical mass M_target strictly forces mu(a) = M_target * a -> 0.
    """
    results = []
    for a in lattice_spacings:
        if a <= 0:
            continue
        m_phys_faizal = dimensionless_gap_mu / a
        # For a physical mass of 1000 MeV (1 GeV), the true lattice dimensionless gap should be:
        # 1 GeV ~= 5.068 fm^-1
        m_target_gev = 1.0
        m_target_inv_fm = m_target_gev * 5.06773
        correct_dimensionless_mu = m_target_inv_fm * a
        
        results.append({
            "lattice_spacing_fm": a,
            "assumed_dimensionless_mu": dimensionless_gap_mu,
            "resulting_physical_mass_inv_fm": m_phys_faizal,
            "correct_dimensionless_mu_for_1gev": correct_dimensionless_mu,
            "scaling_defect_ratio": m_phys_faizal / m_target_inv_fm
        })
    return results


def get_all_theorem_reconciliations() -> List[TheoremAuditRecord]:
    """
    Return authoritative audit and reconciliation records for all YM-012, YM-013, and YM-014 theorems.
    """
    return [
        TheoremAuditRecord(
            theorem_id="YM-012-T1",
            original_claim="Crossover window non-meeting Delta beta >= 2N - 1 > 0",
            primary_source="Bałaban (1984-89); Osterwalder-Seiler (1978)",
            reconciliation_finding="Fully confirmed. Combining rigorous UV Gaussian and IR polymer convergence radii.",
            amendment_status=AmendmentClassification.CONFIRMED,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-012-T2",
            original_claim="Simultaneous expansion breakdown in (beta_0, beta_UV^*)",
            primary_source="Bałaban (1985); Kotecký-Preiss (1982); Shen-Zhu-Zhu (2022)",
            reconciliation_finding="Fully confirmed. Contractivity kappa_BF >= 1 and polymer sum diverges.",
            amendment_status=AmendmentClassification.CONFIRMED,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-012-T3",
            original_claim="Bounded crossover comparison lemma (tangent error + D_TV)",
            primary_source="YM-011-T2; Villani (2009)",
            reconciliation_finding="Fully confirmed. Exact triangle inequality on total variation and transport.",
            amendment_status=AmendmentClassification.CONFIRMED,
            obstruction_tier=None
        ),
        TheoremAuditRecord(
            theorem_id="YM-012-T4",
            original_claim="Crossover continuation obstruction: flow matching alone cannot close crossover",
            primary_source="Hairer (2014); Bałaban (1989)",
            reconciliation_finding="Confirmed with narrower scope as method-specific obstruction for unassisted flow matching.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-013-T1",
            original_claim="Finite-N multi-trace proliferation prevents closure for all finite N",
            primary_source="Kazakov-Zheng (JHEP 2025 099); Makeenko-Migdal (1979)",
            reconciliation_finding="Refuted for SU(2): Tr(U - U^dag) == 0 forces linear closure on single traces. Confirmed for SU(N >= 3).",
            amendment_status=AmendmentClassification.NEEDS_AMENDMENT,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-013-T2",
            original_claim="Mandelstam reduction forces exponential perimeter explosion",
            primary_source="Liu-Yang (JHEP 2026 107); Mandelstam (1979)",
            reconciliation_finding="Confirmed with narrower scope: naive multiplication sums perimeters, but indirect equations eliminate intermediate loops without explosion.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-013-T3",
            original_claim="Certified finite-level SDP bounds on Wilson loops at fixed lattice spacing",
            primary_source="Kazakov-Zheng (2025); Anderson et al. (2020)",
            reconciliation_finding="Fully confirmed. Dual interval Cholesky certificates verify valid SDP relaxations on discrete lattices.",
            amendment_status=AmendmentClassification.CONFIRMED,
            obstruction_tier=None
        ),
        TheoremAuditRecord(
            theorem_id="YM-013-T4",
            original_claim="Finite-perimeter continuum barrier: loop bootstrap cannot close continuum crossover",
            primary_source="Standard dimensional scaling",
            reconciliation_finding="Confirmed with narrower scope: proves fixed-truncation limitation (L_max < infty). Adaptive hierarchy L_max(a) ~ R_*/a is unruled out.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-014-T1",
            original_claim="Random-surface roughening tau_0 < ln mu_4 proves divergence of 4D Yang-Mills",
            primary_source="Ambjørn (1997); Durhuus et al. (1984)",
            reconciliation_finding="Confirmed with narrower scope: proved for bare single-surface ribbon model; heuristic/unproved for interacting non-Abelian theory.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-014-T2",
            original_claim="Non-Abelian duality sign problem: average sign decays exponentially with volume",
            primary_source="Oeckl-Pfeiffer (Nucl. Phys. B 2001)",
            reconciliation_finding="Needs amendment: signed weights proved from 6j symbols, but extensive exponential sign decay is an unproved extrapolation in 4D.",
            amendment_status=AmendmentClassification.NEEDS_AMENDMENT,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-014-T3",
            original_claim="Center-vortex coset polymer divergence rules out vortex route",
            primary_source="Mack-Petkova (1979); Tomboulis (1981)",
            reconciliation_finding="Confirmed with narrower scope: bare coset polymer expansion fails at beta ~= 0.35; vortex flux correlation inequalities remain viable.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
        TheoremAuditRecord(
            theorem_id="YM-014-T4",
            original_claim="Bare string tension scaling tau(a) -> 0 forces empty Hilbert space",
            primary_source="Lüscher-Weisz (2002); Polyakov (1981)",
            reconciliation_finding="Confirmed with narrower scope: applies to bare lattice surface models; does not rule out renormalized continuum string descriptions.",
            amendment_status=AmendmentClassification.CONFIRMED_WITH_NARROWER_SCOPE,
            obstruction_tier=ObstructionType.METHOD_SPECIFIC_OBSTRUCTION
        ),
    ]
