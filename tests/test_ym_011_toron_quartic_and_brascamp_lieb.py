"""
Deterministic regression test suite for YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB:
Periodic-Torus Uniform Plaquette Bound Audit, Quartic Commutator Variety,
Levi-Stratum Power Counting, Brascamp-Lieb Applicability, Exact Schwinger-Dyson
Link Identities, Dyadic Partition-Ratio Concavity Bound, and P1/P2/P3 Guardrails.
"""

from __future__ import annotations

import math
from pathlib import Path
import numpy as np
import pytest

from src.ymmg.toron_brascamp_lieb import (
    audit_brascamp_lieb_applicability,
    audit_commuting_variety_and_levi_strata,
    build_su_n_generators,
    evaluate_dyadic_partition_ratio_bound_and_quartic_model,
    evaluate_periodic_plaquette_hierarchy_guardrail,
    evaluate_quartic_commutator_functional,
    verify_exact_schwinger_dyson_link_identities,
)
from src.ymmg.ros import (
    verify_baseline_lineage_transition,
    verify_full_git_object_exists,
)

ROOT = Path(__file__).resolve().parents[1]


def test_01_quartic_commutator_zero_set_and_commuting_variety_dimensions():
    """
    Verifies Theorem YM-011-TORON-Q1:
    - Q(X_1, ..., X_d) = 0 iff [X_mu, X_nu] = 0 for all mu < nu.
    - Global coercivity Q(X) >= c ||X||^4 is strictly FALSE along non-zero Cartan tuples.
    - Commuting variety dimension is (d + N)(N - 1), quotient dimension is d(N - 1),
      and transverse codimension is (d - 1)N(N - 1).
    """
    # 1. Non-zero Cartan tuple in su(3)^4 has ||X|| > 0 but Q(X) == 0
    h1 = np.diag([1j * 1.2, 1j * (-0.5), 1j * (-0.7)])
    h2 = np.diag([1j * (-0.8), 1j * 1.5, 1j * (-0.7)])
    h3 = np.diag([1j * 0.3, 1j * 0.4, 1j * (-0.7)])
    h4 = np.diag([1j * (-2.1), 1j * 1.1, 1j * 1.0])
    res_comm = evaluate_quartic_commutator_functional([h1, h2, h3, h4], N=3)
    norm_sq = sum(float(np.real(np.trace(h.conj().T @ h))) for h in (h1, h2, h3, h4))
    assert norm_sq > 10.0
    assert res_comm["Q_value"] == pytest.approx(0.0, abs=1e-15)
    assert res_comm["H_4_value"] == pytest.approx(0.0, abs=1e-15)
    assert res_comm["is_commuting_zero_set"] is True

    # 2. Non-commuting su(3) generators have strictly positive Q(X) > 0
    gens = build_su_n_generators(3)
    res_noncomm = evaluate_quartic_commutator_functional([gens[0], gens[1], gens[2], gens[3]], N=3)
    assert res_noncomm["Q_value"] > 0.1
    assert res_noncomm["is_commuting_zero_set"] is False

    # 3. Verify dimensions across d in {2, 3, 4} and N in {2, 3, 4}
    for d in (2, 3, 4):
        for N in (2, 3, 4):
            audit = audit_commuting_variety_and_levi_strata(L=2, d=d, N=N)
            assert audit.commuting_variety_dim == (d + N) * (N - 1)
            assert audit.commuting_quotient_dim == d * (N - 1)
            assert audit.transverse_codim == (d - 1) * N * (N - 1)
            assert audit.commuting_variety_dim + audit.transverse_codim == d * (N * N - 1)


def test_02_levi_stratum_dimension_partition_and_harmonic_exponents():
    """
    Verifies for all d in {2, 3, 4} and N in {2, 3, 4, 5} that every Levi stratum
    L_{(n_1, ..., n_k)} satisfies the exact tangent space partition:
        d(k - 1) + (N^2 - S) + (d - 1)(N^2 - S) + d(S - k) = d(N^2 - 1)
    and the exact harmonic exponent identity:
        alpha_harm(n_1, ..., n_k) = alpha_harm^reg + (1/4) sum_{r=1}^k (n_r - 1)[d - (d - 2)n_r].
    """
    for d in (2, 3, 4):
        for N in (2, 3, 4, 5):
            audit = audit_commuting_variety_and_levi_strata(L=2, d=d, N=N)
            for rec in audit.levi_strata:
                assert (
                    rec.levi_center_flat_modes
                    + rec.off_block_conjugation_zero_modes
                    + rec.off_block_quadratic_modes
                    + rec.in_block_quartic_modes
                    == d * (N * N - 1)
                )
                expected_shift = 0.25 * sum(
                    (nr - 1) * (d - (d - 2) * nr) for nr in rec.partition
                )
                assert math.isclose(
                    rec.alpha_harm_exponent - audit.regular_alpha_harm,
                    expected_shift,
                    abs_tol=1e-12,
                )


def test_03_dominant_stratum_and_logarithmic_resonance_across_d_and_N():
    """
    Verifies the stratum competition across (d, N):
    - d = 2: regular toron strictly dominates for all N >= 2 (m_0 > m_4).
    - d = 3, N = 2: regular toron dominates (alpha_harm = 2.0 < 2.25).
    - d = 3, N = 3: exact marginal resonance between regular (1,1,1) and central (3) at alpha_harm = 6.0.
    - d = 4, N = 2: exact marginal resonance between regular (1,1) and central (2) at alpha_harm = 3.0.
    - d = 4, N = 3: central toron (3) strictly dominates with alpha_harm = 8.0 < 9.0,
      while subregular Levi (2,1) resonates with regular (1,1,1) at 9.0.
    """
    for N in (2, 3, 4):
        a_d2 = audit_commuting_variety_and_levi_strata(L=2, d=2, N=N)
        assert a_d2.dominant_stratum_type == "REGULAR_TORON_GAUSSIAN_DOMINATED"
        assert math.isclose(a_d2.dominant_alpha_harm, 0.5 * N * (N - 1))

    a_32 = audit_commuting_variety_and_levi_strata(L=2, d=3, N=2)
    assert a_32.dominant_stratum_type == "REGULAR_TORON_GAUSSIAN_DOMINATED"
    assert math.isclose(a_32.dominant_alpha_harm, 2.0)

    a_33 = audit_commuting_variety_and_levi_strata(L=2, d=3, N=3)
    assert a_33.dominant_stratum_type == "MARGINAL_RESONANCE_REGULAR_AND_CENTRAL"
    assert a_33.has_logarithmic_resonance is True
    assert math.isclose(a_33.dominant_alpha_harm, 6.0)

    a_42 = audit_commuting_variety_and_levi_strata(L=2, d=4, N=2)
    assert a_42.dominant_stratum_type == "MARGINAL_RESONANCE_REGULAR_AND_CENTRAL"
    assert a_42.has_logarithmic_resonance is True
    assert math.isclose(a_42.dominant_alpha_harm, 3.0)

    a_43 = audit_commuting_variety_and_levi_strata(L=2, d=4, N=3)
    assert a_43.dominant_stratum_type == "CENTRAL_TORON_QUARTIC_DOMINATED"
    assert math.isclose(a_43.regular_alpha_harm, 9.0)
    assert math.isclose(a_43.central_alpha_harm, 8.0)
    assert math.isclose(a_43.dominant_alpha_harm, 8.0)


def test_04_fixed_volume_periodic_equipartition_coefficient_and_toron_reduction():
    """
    Verifies Theorem YM-011-TORON-T2 in d = 4:
        C_per(L, 4, N) = (N^2 - 1)(3 L^4 - 1) / (12 L^4) < (N^2 - 1) / 4,
    confirming that toron flat and quartic zero modes strictly reduce the O(1/beta)
    coefficient relative to (N^2 - 1)/4 rather than increasing it.
    """
    for L in (2, 3, 4):
        for N in (2, 3, 4):
            audit = audit_commuting_variety_and_levi_strata(L=L, d=4, N=N)
            expected_c_per = ((N * N - 1) * (3 * (L ** 4) - 1)) / (12.0 * (L ** 4))
            assert math.isclose(audit.fixed_volume_c_per_coefficient, expected_c_per, rel_tol=1e-12)
            assert audit.fixed_volume_c_per_coefficient < audit.free_boundary_thermodynamic_limit
            assert math.isclose(
                audit.toron_finite_volume_shift,
                -(N * N - 1) / (12.0 * (L ** 4)),
                rel_tol=1e-12,
            )


def test_05_brascamp_lieb_11_field_audit_and_global_non_applicability():
    """
    Verifies all 11 mandatory Brascamp-Lieb fields and confirms that
    GLOBAL_BRASCAMP_LIEB == 'NOT_APPLICABLE' and LOCAL_BRASCAMP_LIEB == 'CONDITIONAL'.
    """
    bl = audit_brascamp_lieb_applicability(L=4, d=4, N=3, periodic=True)
    assert bl.global_brascamp_lieb_status == "NOT_APPLICABLE"
    assert bl.local_brascamp_lieb_status == "CONDITIONAL"
    for attr in (
        "measure",
        "coordinate_chart",
        "potential_V",
        "domain",
        "hessian_of_V",
        "convexity_region",
        "lower_hessian_bound",
        "boundary_conditions",
        "zero_modes_removed",
        "constants",
        "volume_dependence",
    ):
        val = getattr(bl, attr)
        assert isinstance(val, str) and len(val) > 10


def test_06_exact_schwinger_dyson_link_identities_and_partial_closure():
    """
    Verifies Theorem YM-011-TORON-SD1 (exact Casimir divergence and loop-merger / 1/N
    loop-splitting contraction identities) across SU(2), SU(3), and SU(4).
    """
    for N in (2, 3, 4):
        sd = verify_exact_schwinger_dyson_link_identities(N=N, d=4, seed=100 + N)
        assert sd["lhs_discrepancy"] < 1e-14
        assert sd["rhs_discrepancy"] < 1e-14
        assert sd["closure_status"] == "PARTIAL / NOT_SELF_CLOSING"
        assert "domino" in sd["uncontrolled_correlations"]


def test_07_dyadic_partition_ratio_concavity_inequality_and_quartic_model():
    """
    Verifies Theorem YM-011-TORON-T1 (<H>_beta <= (2/beta) ln(Z(beta/2)/Z(beta)))
    on mixed quadratic + quartic models and confirms zero ln(beta)/beta term.
    """
    for n_q, n_4 in ((10, 0), (8, 4), (0, 6), (14, 18)):
        res = evaluate_dyadic_partition_ratio_bound_and_quartic_model(
            n_quad=n_q, n_quartic=n_4, beta=50.0
        )
        assert res["has_log_beta_over_beta_term"] is False
        assert res["dyadic_upper_bound"] >= res["exact_mean_energy"]
        assert math.isclose(res["ratio_bound_over_exact"], 2.0 * math.log(2.0), rel_tol=1e-12)


def test_08_hierarchy_guardrails_p1_proved_p2_and_p3_open():
    """
    Enforces strict hierarchy P3 => P2 => P1:
    - P1_FIXED_VOLUME_PERIODIC is PROVED;
    - P2_VOLUME_UNIFORM_PERIODIC fails closed (OPEN);
    - P3_CONTINUUM_UNIFORM_CONTROL fails closed (OPEN).
    """
    res_p1 = evaluate_periodic_plaquette_hierarchy_guardrail(
        claim_level="P1_FIXED_VOLUME_PERIODIC", L=2, d=4, N=3
    )
    assert res_p1["status"] == "PROVED"
    assert res_p1["log_beta_in_plaquette_expectation"] is False
    assert res_p1["volume_uniform_proved"] is False

    with pytest.raises(ValueError, match="P2_VOLUME_UNIFORM_PERIODIC is OPEN"):
        evaluate_periodic_plaquette_hierarchy_guardrail(
            claim_level="P2_VOLUME_UNIFORM_PERIODIC", L=2, d=4, N=3
        )

    with pytest.raises(ValueError, match="P3_CONTINUUM_UNIFORM_CONTROL is OPEN"):
        evaluate_periodic_plaquette_hierarchy_guardrail(
            claim_level="P3_CONTINUUM_UNIFORM_CONTROL", L=2, d=4, N=3
        )


def test_09_literature_and_negative_evidence_artifacts_integrity():
    """
    Verifies that literature/YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB-ANALYSIS.md
    and NEGATIVE_EVIDENCE_REGISTER.md contain all required theorems, dispositions,
    and negative evidence records.
    """
    lit_path = ROOT / "literature" / "YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB-ANALYSIS.md"
    assert lit_path.exists()
    lit_text = lit_path.read_text(encoding="utf-8")
    for token in (
        "YM-011-TORON-Q1",
        "YM-011-TORON-SD1",
        "YM-011-TORON-T1",
        "YM-011-TORON-T2",
        "GLOBAL_BRASCAMP_LIEB: NOT_APPLICABLE",
        "FIXED_VOLUME_PERIODIC_O_1_OVER_BETA",
        "VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA",
        "GOAL_COMPLETE = FALSE",
        "CLAY_PROBLEM = OPEN_AND_UNSOLVED",
    ):
        assert token in lit_text

    neg_path = ROOT / "NEGATIVE_EVIDENCE_REGISTER.md"
    neg_text = neg_path.read_text(encoding="utf-8")
    assert "NEG-YM-011-TORON-1" in neg_text


def test_10_baseline_lineage_transition_from_tree_gauge_r1():
    """
    Verifies that the baseline SHA 9aec40b170415ba94fee65cb8d27df76ecd4aeaf
    exists in Git as a commit and passes verify_baseline_lineage_transition(..., transition_class='SAME').
    """
    baseline_sha = "9aec40b170415ba94fee65cb8d27df76ecd4aeaf"
    assert verify_full_git_object_exists(baseline_sha, repo_root=ROOT) == "commit"
    res = verify_baseline_lineage_transition(
        prior_closeout_sha=baseline_sha,
        next_baseline_sha=baseline_sha,
        transition_class="SAME",
        repo_root=ROOT,
    )
    assert res["status"] == "BASELINE_LINEAGE_VERIFIED"
