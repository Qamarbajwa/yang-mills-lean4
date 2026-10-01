"""Unit tests for Task YM-014: Random-Surface / Duality Crossover Representation Analysis.

Validates Theorems YM-014-T1 through YM-014-T4, bare surface tension,
roughening thresholds, Wigner 6j sign oscillation, and continuum scaling diagnostics.
"""

import math
import pytest
from pathlib import Path

from ymmg.random_surface_duality import (
    bessel_character_ratio_su2,
    bare_surface_tension_su2,
    roughening_gap,
    is_surface_roughened,
    critical_roughening_beta,
    wigner_6j_symbol,
    evaluate_dual_sign_configurations,
    average_sign_ratio,
    asymptotic_lattice_spacing_su2,
    physical_string_tension,
    evaluate_crossover_surface_duality_landscape,
)

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / "literature"
GOV_DIR = ROOT / "governance"


def test_01_bessel_character_expansion_su2():
    """Verify Bessel character expansion ratios a_j(beta) on SU(2)."""
    # Small beta expansion: a_{1/2}(beta) ~ beta / 8
    for beta in [0.01, 0.05, 0.1]:
        a_half = bessel_character_ratio_su2(0.5, beta)
        expected = beta / 8.0
        assert math.isclose(a_half, expected, rel_tol=0.02)

    # Intermediate coupling beta = 2.0
    a_half_2 = bessel_character_ratio_su2(0.5, 2.0)
    assert math.isclose(a_half_2, 0.216564, rel_tol=1e-4)

    a_one_2 = bessel_character_ratio_su2(1.0, 2.0)
    assert math.isclose(a_one_2, 0.04458, rel_tol=1e-3)
    assert a_one_2 < a_half_2

    # Higher spin suppression
    a_threehalf_2 = bessel_character_ratio_su2(1.5, 2.0)
    assert a_threehalf_2 < a_one_2


def test_02_bare_surface_tension_monotonicity():
    """Verify bare surface tension tau_0(beta) = -ln a_{1/2}(beta) and monotonicity."""
    tau_1 = bare_surface_tension_su2(1.0)
    tau_15 = bare_surface_tension_su2(1.5)
    tau_2 = bare_surface_tension_su2(2.0)
    tau_25 = bare_surface_tension_su2(2.5)

    assert math.isclose(tau_1, 2.1195, rel_tol=1e-3)
    assert math.isclose(tau_15, 1.7598, rel_tol=1e-3)
    assert math.isclose(tau_2, 1.5299, rel_tol=1e-3)
    assert math.isclose(tau_25, 1.3720, rel_tol=1e-3)

    # Monotonic decrease as coupling weakens
    assert tau_1 > tau_15 > tau_2 > tau_25


def test_03_roughening_entropy_energy_barrier_t1():
    """Verify Theorem YM-014-T1: bare surface tension drops below surface entropy in crossover."""
    mu_4_physical = 6.0
    ln_mu_4 = math.log(mu_4_physical)  # ~ 1.7918

    # At strong coupling beta = 1.0, tau_0 > ln mu_4 (convergent)
    assert roughening_gap(1.0, mu_4=mu_4_physical) > 0.0
    assert not is_surface_roughened(1.0, mu_4=mu_4_physical)

    # At crossover beta = 2.0, tau_0 < ln mu_4 (divergent roughening)
    gap_2 = roughening_gap(2.0, mu_4=mu_4_physical)
    assert gap_2 < 0.0
    assert is_surface_roughened(2.0, mu_4=mu_4_physical)

    # Critical roughening beta for mu_4 = 6.0
    beta_c = critical_roughening_beta(mu_4=mu_4_physical)
    assert 1.40 < beta_c < 1.50
    assert math.isclose(bare_surface_tension_su2(beta_c), ln_mu_4, rel_tol=1e-4)

    # Even for conservative lower bound mu_4 = 5.0 (ln mu_4 ~= 1.6094)
    beta_c_50 = critical_roughening_beta(mu_4=5.0)
    assert 1.75 < beta_c_50 < 1.85
    assert is_surface_roughened(2.0, mu_4=5.0)


def test_04_wigner_6j_sign_oscillation_t2():
    """Verify Theorem YM-014-T2: Wigner 6j symbols have indefinite signs on dual cell complex."""
    sign_data = evaluate_dual_sign_configurations()

    assert sign_data["has_negative_weights"] is True
    assert sign_data["has_positive_weights"] is True
    assert sign_data["is_strictly_nonnegative"] is False
    assert sign_data["sign_oscillation_present"] is True

    # Check explicit cases
    val_neg1 = wigner_6j_symbol(1.0, 1.0, 1.0, 0.5, 0.5, 0.5)
    assert math.isclose(val_neg1, -1.0 / 3.0, rel_tol=1e-6)

    val_neg2 = wigner_6j_symbol(1.0, 1.0, 1.0, 0.5, 0.5, 1.5)
    assert math.isclose(val_neg2, -1.0 / 6.0, rel_tol=1e-6)

    val_pos = wigner_6j_symbol(0.5, 0.5, 1.0, 0.5, 0.5, 1.0)
    assert math.isclose(val_pos, 1.0 / 6.0, rel_tol=1e-6)


def test_05_average_sign_decay_t2():
    """Verify exponential decay of the average sign ratio <sign> <= exp(-c_sign * V)."""
    c_sign = 0.05
    for l in [4, 8, 12, 16]:
        v = l**4
        sign_ratio = average_sign_ratio(c_sign, v)
        expected = math.exp(-c_sign * v)
        assert math.isclose(sign_ratio, expected)

    # In thermodynamic volume 16^4 = 65536, sign is utterly vanished
    v_large = 16**4
    assert average_sign_ratio(c_sign, v_large) < 1e-100


def test_06_continuum_scaling_defect_t4():
    """Verify Theorem YM-014-T4: continuum scaling defect and rough phase collapse."""
    # Lattice spacing decreases as beta increases
    a_2 = asymptotic_lattice_spacing_su2(2.0)
    a_3 = asymptotic_lattice_spacing_su2(3.0)
    a_4 = asymptotic_lattice_spacing_su2(4.0)
    assert a_2 > a_3 > a_4 > 0.0

    # Constant bare tension implies divergent continuum string tension
    sigma_2 = physical_string_tension(2.0, bare_tau=1.0)
    sigma_3 = physical_string_tension(3.0, bare_tau=1.0)
    sigma_4 = physical_string_tension(4.0, bare_tau=1.0)
    assert sigma_4 > sigma_3 > sigma_2

    # Constant physical string tension implies vanishing bare tension
    sigma_phys = 1.0  # (Lambda_YM)^2
    tau_lat_4 = sigma_phys * (a_4**2)
    tau_lat_2 = sigma_phys * (a_2**2)
    assert tau_lat_4 < tau_lat_2
    assert tau_lat_4 < math.log(3.5)  # Far below roughening threshold


def test_07_comprehensive_landscape_diagnostic():
    """Verify complete landscape diagnostic evaluation."""
    report = evaluate_crossover_surface_duality_landscape()

    assert report["crossover_roughened_at_beta_2"] is True
    assert report["governance_disposition"] == "OBSTRUCTION_FORMALIZED_E_CROSSOVER_OPEN"
    assert report["next_objective"] == "YM-015"
    assert "YM-014-T1" in report["theorems"]
    assert "YM-014-T2" in report["theorems"]
    assert "YM-014-T3" in report["theorems"]
    assert "YM-014-T4" in report["theorems"]


def test_08_governance_invariants_and_negative_evidence():
    """Verify project governance invariants and negative evidence registration."""
    neg_reg = ROOT / "NEGATIVE_EVIDENCE_REGISTER.md"
    assert neg_reg.exists()
    content = neg_reg.read_text(encoding="utf-8")

    # Target file exists
    target_path = LIT_DIR / "YM-014-RANDOM-SURFACE-DUALITY-TARGET.md"
    assert target_path.exists()
    target_text = target_path.read_text(encoding="utf-8")
    assert "YM-014-TARGET" in target_text
    assert "goal_complete = false" in target_text
    assert "clay_problem = OPEN_AND_UNSOLVED" in target_text
    assert "E-CROSSOVER = OPEN" in target_text
