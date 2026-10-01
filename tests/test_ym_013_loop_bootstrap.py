"""Tests for Task YM-013: Certified Finite-N Loop-Bootstrap Crossover Bounds.

Verifies:
- Canonical loop dictionary up to perimeter 6.
- Theorem YM-013-T1: Multi-trace proliferation tracking.
- Theorem YM-013-T2: Mandelstam perimeter explosion in SU(2).
- Theorem YM-013-T3: Certified Level-4 and Level-6 SDP bounds in the crossover window.
- Independent deterministic interval Cholesky dual certificate verifier.
- Theorem YM-013-T4: Continuum finite-perimeter truncation barrier.
- Epistemic invariants and obstruction status.
"""

from __future__ import annotations

import pytest
from ymmg.loop_bootstrap import (
    CANONICAL_LOOPS,
    su2_mandelstam_concatenation,
    compute_multi_trace_composite_perimeter,
    compute_su2_level4_bounds,
    compute_su2_level6_bounds,
    verify_interval_cholesky_psd,
    generate_and_verify_plaquette_certificate,
    compute_continuum_perimeter_ratio,
)


def test_01_canonical_loop_dictionary():
    """Verify canonical loop classes on Z^4."""
    assert "empty" in CANONICAL_LOOPS
    assert "plaquette" in CANONICAL_LOOPS
    assert "domino" in CANONICAL_LOOPS
    assert "chair" in CANONICAL_LOOPS
    assert "twist" in CANONICAL_LOOPS

    assert CANONICAL_LOOPS["empty"].perimeter == 0
    assert CANONICAL_LOOPS["plaquette"].perimeter == 4
    assert CANONICAL_LOOPS["domino"].perimeter == 6
    assert CANONICAL_LOOPS["chair"].perimeter == 6
    assert CANONICAL_LOOPS["twist"].perimeter == 6

    assert CANONICAL_LOOPS["plaquette"].is_planar is True
    assert CANONICAL_LOOPS["domino"].is_planar is True
    assert CANONICAL_LOOPS["chair"].is_planar is False


def test_02_mandelstam_perimeter_explosion():
    """Verify Theorem YM-013-T2: Mandelstam perimeter explosion |AB| = |A| + |B|."""
    # Concatenation of two plaquettes (4 + 4 = 8)
    p_comp = su2_mandelstam_concatenation(4, 4)
    assert p_comp == 8

    # Concatenation of plaquette and domino (4 + 6 = 10)
    assert su2_mandelstam_concatenation(4, 6) == 10

    # Multi-trace product of 4 plaquettes requires loop of perimeter 16
    multi_perim = compute_multi_trace_composite_perimeter([4, 4, 4, 4])
    assert multi_perim == 16


def test_03_level4_analytical_bounds():
    """Verify Level-4 analytical bounds on SU(2) plaquette expectation w_p."""
    with pytest.raises(ValueError):
        compute_su2_level4_bounds(0.0)

    # At beta = 2.0 (crossover center), level-4 relaxation is broad
    w_min, w_max = compute_su2_level4_bounds(2.0)
    assert w_min == -1.0
    assert w_max == 1.0

    # At strong coupling beta = 0.5
    w_min_05, w_max_05 = compute_su2_level4_bounds(0.5)
    assert -1.0 <= w_min_05 <= 1.0
    assert -1.0 <= w_max_05 <= 1.0


def test_04_level6_certified_bounds():
    """Verify Level-6 tightened bounds on SU(2) plaquette expectation w_p."""
    w_min, w_max = compute_su2_level6_bounds(2.0)
    assert w_min >= 0.0
    assert w_max <= 1.0
    assert w_min < w_max
    # Verify that the enclosure is non-trivial (strictly narrower than [-1, 1])
    assert (w_max - w_min) < 2.0


def test_05_interval_cholesky_verification():
    """Verify deterministic interval Cholesky PSD verification."""
    # Strictly positive definite matrix
    spd_matrix = [
        [4.0, 1.0, 0.5],
        [1.0, 3.0, 0.2],
        [0.5, 0.2, 2.0],
    ]
    is_psd, pivots = verify_interval_cholesky_psd(spd_matrix)
    assert is_psd is True
    assert all(p > 0.0 for p in pivots)

    # Indefinite matrix
    indef_matrix = [
        [1.0, 2.0],
        [2.0, 1.0],
    ]
    is_psd_indef, pivots_indef = verify_interval_cholesky_psd(indef_matrix)
    assert is_psd_indef is False
    assert any(p < 0.0 for p in pivots_indef)


def test_06_dual_certificate_generator():
    """Verify dual certificate generator and deterministic check at crossover couplings."""
    for beta in [1.5, 2.0, 2.5]:
        cert_lower = generate_and_verify_plaquette_certificate(beta, "LOWER")
        assert cert_lower.is_certified is True
        assert cert_lower.bound_type == "LOWER"
        assert all(p > 0.0 for p in cert_lower.pivots)

        cert_upper = generate_and_verify_plaquette_certificate(beta, "UPPER")
        assert cert_upper.is_certified is True
        assert cert_upper.bound_type == "UPPER"
        assert cert_lower.bound_value <= cert_upper.bound_value


def test_07_continuum_truncation_barrier():
    """Verify Theorem YM-013-T4: Vanishing physical perimeter ratio in continuum limit."""
    l_max = 6
    r_cross = 0.5  # fm

    with pytest.raises(ValueError):
        compute_continuum_perimeter_ratio(l_max, -0.1)

    with pytest.raises(ValueError):
        compute_continuum_perimeter_ratio(l_max, 0.1, -0.5)

    # On coarse lattice a = 0.1 fm: R_max = 0.6 fm, ratio > 1
    ratio_coarse = compute_continuum_perimeter_ratio(l_max, 0.1, r_cross)
    assert ratio_coarse == pytest.approx(1.2)

    # As a -> 0: a = 0.01 fm ==> ratio = 0.12; a = 0.001 fm ==> ratio = 0.012
    ratio_fine = compute_continuum_perimeter_ratio(l_max, 0.01, r_cross)
    assert ratio_fine == pytest.approx(0.12)

    ratio_ultra = compute_continuum_perimeter_ratio(l_max, 0.001, r_cross)
    assert ratio_ultra == pytest.approx(0.012)
    assert ratio_ultra < ratio_fine < ratio_coarse


def test_08_epistemic_invariants_and_obstruction_preservation():
    """Verify epistemic invariants: goal_complete is false, clay_problem is OPEN, E-CROSSOVER is OPEN."""
    from pathlib import Path
    import yaml

    repo_root = Path(__file__).resolve().parent.parent
    proj_state_path = repo_root / "governance" / "PROJECT_STATE.yaml"
    assert proj_state_path.exists()
    state = yaml.safe_load(proj_state_path.read_text(encoding="utf-8"))

    assert state["goal_complete"] is False
    assert state["clay_problem"] == "OPEN_AND_UNSOLVED"

    # Verify that NEGATIVE_EVIDENCE_REGISTER.md contains NEG-YM-013 findings
    neg_reg = (repo_root / "NEGATIVE_EVIDENCE_REGISTER.md").read_text(encoding="utf-8")
    assert "NEG-YM-013-BOOTSTRAP-1" in neg_reg
    assert "NEG-YM-013-BOOTSTRAP-2" in neg_reg

