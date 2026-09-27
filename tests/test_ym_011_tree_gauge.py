"""
Deterministic Unit & Regression Tests for Task YM-011-TREE-GAUGE
(Maximal-Tree Gauge Fixing, Bianchi Constraints, and Zero-Mode Separation).
"""

import itertools
import math
from pathlib import Path
import numpy as np
import pytest
from scipy.linalg import expm

from src.ymmg.tree_gauge import (
    audit_plaquette_coordinate_map,
    analyze_periodic_toron_zero_modes,
    build_lattice_graph,
    compute_tree_gauge_hessian_spectrum,
    compute_tree_gauge_transform,
    evaluate_fixed_volume_equipartition_bound,
    evaluate_plaquette_holonomy,
    reconstruct_d2_free_from_plaquettes,
    verify_non_abelian_bianchi_cube_identity,
)

ROOT = Path(__file__).resolve().parent.parent


def _random_su_n(rng: np.random.Generator, N: int) -> np.ndarray:
    H = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    A = H - H.conj().T
    A -= (np.trace(A) / float(N)) * np.eye(N, dtype=complex)
    return expm(A)


def test_01_combinatorial_edge_tree_cotree_and_cycle_rank_counts():
    """
    Verifies |T| = |V| - 1, |E_cotree| = |E_+| - |V| + 1 (cycle rank),
    and Euler characteristic chi = 1 (free boundary) vs chi = 0 (periodic torus)
    across d = 2, 3, 4.
    """
    for d, L in [(2, 3), (2, 4), (3, 3), (4, 2)]:
        g_free = build_lattice_graph(L=L, d=d, periodic=False)
        assert g_free.num_vertices == L ** d
        assert g_free.num_edges == d * (L - 1) * (L ** (d - 1))
        assert g_free.num_tree_edges == (L ** d) - 1
        assert g_free.num_cotree_edges == g_free.num_edges - g_free.num_vertices + 1
        assert g_free.cycle_rank == g_free.num_cotree_edges
        assert g_free.num_plaquettes == math.comb(d, 2) * ((L - 1) ** 2) * (L ** (d - 2))
        assert g_free.euler_characteristic == 1

        g_per = build_lattice_graph(L=L, d=d, periodic=True)
        assert g_per.num_vertices == L ** d
        assert g_per.num_edges == d * (L ** d)
        assert g_per.num_tree_edges == (L ** d) - 1
        assert g_per.num_cotree_edges == (d - 1) * (L ** d) + 1
        assert g_per.cycle_rank == g_per.num_cotree_edges
        assert g_per.num_plaquettes == math.comb(d, 2) * (L ** d)
        assert g_per.euler_characteristic == 0


def test_02_maximal_tree_gauge_existence_uniqueness_and_wilson_invariance():
    """
    Verifies explicit recursive tree-gauge fixing (U_e = I_N for all e in T),
    uniqueness after fixing root gauge g(x_0) = I_N, residual global adjoint conjugation
    when root gauge is varied, and exact invariance of all plaquette traces.
    """
    rng = np.random.default_rng(20260927)
    for d, periodic in [(2, False), (3, False), (3, True), (4, False)]:
        L = 2
        N = 3
        graph = build_lattice_graph(L=L, d=d, periodic=periodic)
        U = {e: _random_su_n(rng, N) for e in graph.edges_pos}

        g_1, U_fixed_1 = compute_tree_gauge_transform(graph, U)
        eye = np.eye(N, dtype=complex)

        # 1. Root gauge fixed to I_N
        assert np.allclose(g_1[graph.root], eye, atol=1e-14)

        # 2. Every tree edge is set to I_N
        for te in graph.tree_edges:
            assert np.allclose(U_fixed_1[te], eye, atol=1e-14)

        # 3. Uniqueness: applying tree-gauge transform again to U_fixed_1 yields g = I_N everywhere
        g_again, U_fixed_again = compute_tree_gauge_transform(graph, U_fixed_1)
        for v in graph.vertices:
            assert np.allclose(g_again[v], eye, atol=1e-14)
        for e in graph.edges_pos:
            assert np.allclose(U_fixed_again[e], U_fixed_1[e], atol=1e-14)

        # 4. Residual global conjugation: setting g(x_0) = g_0 conjugates every co-tree link by g_0
        g_0 = _random_su_n(rng, N)
        _, U_fixed_g0 = compute_tree_gauge_transform(graph, U, g_root=g_0)
        for te in graph.tree_edges:
            assert np.allclose(U_fixed_g0[te], eye, atol=1e-14)
        for ce in graph.cotree_edges:
            expected_ce = g_0 @ U_fixed_1[ce] @ g_0.conj().T
            assert np.allclose(U_fixed_g0[ce], expected_ce, atol=1e-14)

        # 5. Exact preservation of all plaquette Wilson traces
        for p in graph.plaquettes_pos:
            hol_orig = evaluate_plaquette_holonomy(graph, U, p)
            hol_fixed = evaluate_plaquette_holonomy(graph, U_fixed_1, p)
            assert np.isclose(np.trace(hol_orig), np.trace(hol_fixed), atol=1e-14)


def test_03_d2_free_boundary_exact_triangular_plaquette_reconstruction():
    """
    Verifies that in d = 2 free boundary, the (L - 1)^2 co-tree links biject
    triangularly onto the (L - 1)^2 plaquette holonomies with exact inverse reconstruction.
    """
    rng = np.random.default_rng(101)
    L = 4
    N = 3
    graph = build_lattice_graph(L=L, d=2, periodic=False)
    assert graph.num_cotree_edges == (L - 1) ** 2 == graph.num_plaquettes

    # Generate arbitrary random SU(3) plaquette holonomies
    target_plaquettes = {p: _random_su_n(rng, N) for p in graph.plaquettes_pos}
    U_recon = reconstruct_d2_free_from_plaquettes(L=L, plaquette_holonomies=target_plaquettes, N=N)

    # Verify all tree edges are I_N and every reconstructed plaquette matches target_plaquettes
    for te in graph.tree_edges:
        assert np.allclose(U_recon[te], np.eye(N, dtype=complex), atol=1e-14)
    for p in graph.plaquettes_pos:
        hol = evaluate_plaquette_holonomy(graph, U_recon, p)
        assert np.allclose(hol, target_plaquettes[p], atol=1e-14)


def test_04_non_abelian_bianchi_cube_identity_and_failure_of_d3_d4_bijection():
    """
    Verifies the exact 6-face non-Abelian Bianchi identity around a 3-cube in SU(2) and SU(3)
    and confirms that co-tree links do NOT biject onto all plaquettes in d >= 3 or on periodic tori.
    """
    rng = np.random.default_rng(303)
    for N in (2, 3):
        links = {}
        for pt in itertools.product((0, 1), repeat=3):
            for ax in range(3):
                if pt[ax] == 0:
                    links[(pt, ax)] = _random_su_n(rng, N)
        err = verify_non_abelian_bianchi_cube_identity(links)
        assert err < 1e-14

    # Audit map classifications
    a_d2_free = audit_plaquette_coordinate_map(L=3, d=2, periodic=False, N=3)
    assert a_d2_free.is_global_bijection is True
    assert a_d2_free.decouples_wilson_action is True
    assert a_d2_free.plaquette_minus_cotree == 0

    for d, periodic in [(2, True), (3, False), (3, True), (4, False), (4, True)]:
        audit = audit_plaquette_coordinate_map(L=2, d=d, periodic=periodic, N=3)
        assert audit.is_global_bijection is False
        assert audit.decouples_wilson_action is False
        if not periodic and d >= 3:
            assert audit.plaquette_minus_cotree > 0
            assert audit.map_classification == "CONSTRAINED_EMBEDDING_WITH_BIANCHI_SYZYGIES"
        if periodic:
            assert audit.global_homology_rank_b1 == d
            assert audit.map_classification == "NON_BIJECTIVE_GLOBAL_CYCLE_DEFICIT_AND_BIANCHI_CONSTRAINTS"


def test_05_free_boundary_hessian_strict_positivity_and_volume_degeneration():
    """
    Verifies that on the contractible free-boundary lattice, the tree-gauge Hessian H_tree
    has nullity 0 (full rank |E_cotree|), matches the exact analytical formula in d=2,
    and degenerates (lambda_min -> 0) as L increases.
    """
    prev_lmin = float("inf")
    for L in (2, 3, 4, 5):
        res_d2 = compute_tree_gauge_hessian_spectrum(L=L, d=2, periodic=False)
        assert res_d2.numerical_nullity == 0
        assert res_d2.numerical_rank == res_d2.matrix_size == (L - 1) ** 2
        assert res_d2.epistemic_status == "NUMERICAL_DIAGNOSTIC_ONLY"
        expected_lmin = 4.0 * (math.sin(math.pi / (2.0 * (2 * L - 1))) ** 2)
        assert math.isclose(res_d2.smallest_positive_eigenvalue, expected_lmin, rel_tol=1e-12)
        assert res_d2.smallest_positive_eigenvalue < prev_lmin
        prev_lmin = res_d2.smallest_positive_eigenvalue

    res_d3 = compute_tree_gauge_hessian_spectrum(L=3, d=3, periodic=False)
    assert res_d3.numerical_nullity == 0
    assert res_d3.numerical_rank == 28

    res_d4 = compute_tree_gauge_hessian_spectrum(L=2, d=4, periodic=False)
    assert res_d4.numerical_nullity == 0
    assert res_d4.numerical_rank == 17


def test_06_periodic_torus_zero_modes_commuting_holonomies_and_quartic_strata():
    """
    Verifies that on the periodic torus:
    1. Scalar tree-gauge Hessian has nullity d (hence d(N^2 - 1) for su(N) at U = I_N).
    2. Commuting global wrapping holonomies [U_mu, U_nu] = I_N give exact zero Wilson action H = 0
       on Sigma_{T_per}, whereas non-commuting wrapping holonomies give H > 0 on corner plaquettes.
    3. Stabilizer dimension jumps by N(N - 1) and releases (d - 1)N(N - 1) quartic commutator modes.
    """
    for d in (2, 3, 4):
        L = 2
        res_per = compute_tree_gauge_hessian_spectrum(L=L, d=d, periodic=True)
        assert res_per.numerical_nullity == d
        assert res_per.numerical_rank == res_per.matrix_size - d

        for N in (2, 3):
            decomp = analyze_periodic_toron_zero_modes(d=d, N=N)
            assert decomp.flat_moduli_dim == d * (N - 1)
            assert decomp.generic_adjoint_orbit_dim == N * (N - 1)
            assert decomp.regular_toron_hessian_nullity == (d + N) * (N - 1)
            assert decomp.central_toron_hessian_nullity == d * (N * N - 1)
            assert decomp.stabilizer_dim_jump == N * (N - 1)
            assert decomp.quartic_commutator_zero_modes == (d - 1) * N * (N - 1)
            assert decomp.num_central_toron_sectors == N ** d

    # Construct an explicit periodic configuration in tree gauge with wrapping matrices U_mu
    graph = build_lattice_graph(L=2, d=3, periodic=True)
    N = 2
    eye = np.eye(N, dtype=complex)

    # Commuting diagonal torons: U_mu = exp(i theta_mu sigma_3)
    comm_mats = [
        np.diag([np.exp(0.3j), np.exp(-0.3j)]),
        np.diag([np.exp(-0.7j), np.exp(0.7j)]),
        np.diag([np.exp(1.1j), np.exp(-1.1j)]),
    ]
    U_comm = {}
    for e in graph.edges_pos:
        x, mu, _ = e
        U_comm[e] = comm_mats[mu] if x[mu] == graph.L - 1 else eye.copy()

    # Verify all tree edges are I_2 and all plaquettes have h_p = 0
    for te in graph.tree_edges:
        assert np.allclose(U_comm[te], eye, atol=1e-14)
    for p in graph.plaquettes_pos:
        hol = evaluate_plaquette_holonomy(graph, U_comm, p)
        assert np.allclose(hol, eye, atol=1e-14)

    # Non-commuting wrapping matrices: [U_0, U_1] != I_2 -> corner plaquette has h_p > 0
    rng = np.random.default_rng(777)
    noncomm_mats = [_random_su_n(rng, N) for _ in range(3)]
    U_noncomm = {}
    for e in graph.edges_pos:
        x, mu, _ = e
        U_noncomm[e] = noncomm_mats[mu] if x[mu] == graph.L - 1 else eye.copy()
    corner_p = ((1, 1, 0), 0, 1)
    hol_corner = evaluate_plaquette_holonomy(graph, U_noncomm, corner_p)
    h_corner = 1.0 - (1.0 / N) * np.real(np.trace(hol_corner))
    assert h_corner > 1e-3


def test_07_regression_guardrails_against_overclaiming_and_conflation():
    """
    Regression tests enforcing strict separation of Claims A, B, C and rejecting:
    - ordinary Laplace isolated-minimum claims on the periodic torus;
    - promoting fixed-volume (Claim A) to volume-uniform (Claim B) in d >= 3;
    - claiming continuum-uniform (Claim C).
    """
    # Valid Claim A on d=4 free boundary
    res_a = evaluate_fixed_volume_equipartition_bound(
        L=2, d=4, N=3, periodic=False, claim_scope="CLAIM_A_FIXED_VOLUME_FREE_BOUNDARY"
    )
    assert res_a["cotree_dof"] == 8 * 17
    assert res_a["num_plaquettes"] == 24
    assert math.isclose(res_a["leading_coefficient_C"], (8 * 17) / 48.0)
    assert res_a["volume_uniform_proved"] is False

    # Valid Claim B ONLY on d=2 free boundary
    res_b_d2 = evaluate_fixed_volume_equipartition_bound(
        L=4, d=2, N=3, periodic=False, claim_scope="CLAIM_B_VOLUME_UNIFORM"
    )
    assert res_b_d2["volume_uniform_proved"] is True
    assert math.isclose(res_b_d2["leading_coefficient_C"], 4.0)

    # Reject Claim B on d=3 and d=4 free boundary
    with pytest.raises(ValueError, match="cannot be promoted to volume-uniform"):
        evaluate_fixed_volume_equipartition_bound(
            L=3, d=3, N=3, periodic=False, claim_scope="CLAIM_B_VOLUME_UNIFORM"
        )
    with pytest.raises(ValueError, match="cannot be promoted to volume-uniform"):
        evaluate_fixed_volume_equipartition_bound(
            L=2, d=4, N=3, periodic=False, claim_scope="CLAIM_B_VOLUME_UNIFORM"
        )

    # Reject ordinary Laplace isolated-minimum claim on periodic torus
    with pytest.raises(ValueError, match="Periodic torus retains global toron moduli"):
        evaluate_fixed_volume_equipartition_bound(
            L=2, d=4, N=3, periodic=True, claim_scope="CLAIM_A_ORDINARY_LAPLACE_ISOLATED_MINIMUM"
        )

    # Reject Claim C everywhere
    with pytest.raises(ValueError):
        evaluate_fixed_volume_equipartition_bound(
            L=3, d=2, N=3, periodic=False, claim_scope="CLAIM_C_CONTINUUM_UNIFORM"
        )


def test_08_literature_and_negative_evidence_artifacts_integrity():
    """
    Verifies that literature/YM-011-TREE-GAUGE-ANALYSIS.md and NEGATIVE_EVIDENCE_REGISTER.md
    contain all required theorems, primary-source audit records, and negative evidence entries.
    """
    lit_path = ROOT / "literature" / "YM-011-TREE-GAUGE-ANALYSIS.md"
    assert lit_path.exists()
    lit_text = lit_path.read_text(encoding="utf-8")
    for token in (
        "YM-011-TREE-T1",
        "YM-011-TREE-T2",
        "YM-011-TREE-T3",
        "YM-011-TREE-T4",
        "(T_{\\mathrm{max}})^d / S_N",
        "(d - 1)N(N - 1)",
        "GOAL_COMPLETE = FALSE",
        "CLAY_PROBLEM = OPEN_AND_UNSOLVED",
    ):
        assert token in lit_text

    neg_path = ROOT / "NEGATIVE_EVIDENCE_REGISTER.md"
    neg_text = neg_path.read_text(encoding="utf-8")
    assert "NEG-YM-011-PLAQ-1" in neg_text
    assert "Post-Tree-Gauge Re-Evaluation (`YM-011-TREE-GAUGE`)" in neg_text
    assert "NEG-YM-011-TREE-1" in neg_text


def test_09_cochain_rank_identity_and_linearized_scope():
    """
    Verifies the explicit periodic and free-boundary cochain rank identity (YM-011-TREE-GAUGE-R1):
        rank(d_1) = |E_+| - |V| + 1 - b_1 = |E_co-tree| - b_1
        N_constraints^cochain = |P_+| - rank(d_1) = |P_+| - |E_co-tree| + b_1
    giving 1 (d=2), L^3 + 2 (d=3), and 3L^4 + 3 (d=4) on Lambda_per(L, d),
    and strictly labels the count as LINEARIZED_COCHAIN_RANK_COUNT vs
    NON_ABELIAN_GLOBAL_CONSTRAINT_VARIETY.
    """
    for d, L, expected_per_constraints in ((2, 3, 1), (3, 3, 29), (4, 2, 51)):
        audit_per = audit_plaquette_coordinate_map(L=L, d=d, periodic=True, N=3)
        assert audit_per.global_homology_rank_b1 == d
        assert audit_per.rank_d1 == audit_per.num_edges - audit_per.num_vertices + 1 - d
        assert audit_per.rank_d1 == audit_per.num_cotree_edges - d
        assert audit_per.num_independent_bianchi_constraints == audit_per.num_plaquettes - audit_per.rank_d1
        assert audit_per.num_independent_bianchi_constraints == (
            audit_per.num_plaquettes - audit_per.num_cotree_edges + d
        )
        assert audit_per.num_independent_bianchi_constraints == expected_per_constraints
        assert audit_per.cochain_constraint_count_scope == "LINEARIZED_COCHAIN_RANK_COUNT"
        assert audit_per.non_abelian_constraint_scope == "NON_ABELIAN_GLOBAL_CONSTRAINT_VARIETY"

        audit_free = audit_plaquette_coordinate_map(L=L, d=d, periodic=False, N=3)
        assert audit_free.global_homology_rank_b1 == 0
        assert audit_free.rank_d1 == audit_free.num_cotree_edges
        assert audit_free.num_independent_bianchi_constraints == (
            audit_free.num_plaquettes - audit_free.num_cotree_edges
        )


def test_10_baseline_lineage_transition_and_sha_drift_guardrail():
    """
    Verifies the YM-011-TREE-GAUGE-R1 regression protection against baseline SHA drift:
    1. True Git governance closeout SHA `88cc4f9de1b96204e30743c4679131871732bbc7` exists in Git
       and passes `verify_baseline_lineage_transition(..., transition_class='SAME')`.
    2. Historical prose typo SHA `88cc4f93282b09a71ce169352e057ba6e1b643a6` does NOT exist in Git
       and fails closed under `verify_full_git_object_exists` and `SAME` transition.
    3. Reconciling `88cc4f93282b09a71ce169352e057ba6e1b643a6` -> `88cc4f9de1b96204e30743c4679131871732bbc7`
       succeeds ONLY when `transition_class='SUPERSEDED_BY_AMEND'` and the explicit reconciliation
       record `verification/YM-011-TREE-GAUGE-R1_PROVENANCE_RECONCILIATION.md` is supplied.
    4. Unexplained baseline SHA differences and `SEMANTIC_REVIEW_REQUIRED` transitions fail closed.
    """
    from ymmg.ros import (
        ConstitutionalIntegrityError,
        verify_baseline_lineage_transition,
        verify_full_git_object_exists,
    )

    true_gov_closeout_sha = "88cc4f9de1b96204e30743c4679131871732bbc7"
    typo_prose_sha = "88cc4f93282b09a71ce169352e057ba6e1b643a6"
    tree_gauge_candidate_sha = "099c883a67f07bb3576abe77cd19fce8978df651"

    # 1. True SHA exists in Git as a commit; typo SHA does not exist in Git
    assert verify_full_git_object_exists(true_gov_closeout_sha, repo_root=ROOT) == "commit"
    assert verify_full_git_object_exists(tree_gauge_candidate_sha, repo_root=ROOT) == "commit"
    with pytest.raises(ConstitutionalIntegrityError, match="does not exist in the Git object database"):
        verify_full_git_object_exists(typo_prose_sha, repo_root=ROOT)

    # 2. Abbreviated SHA fails closed
    with pytest.raises(ConstitutionalIntegrityError, match="40-character"):
        verify_full_git_object_exists("88cc4f9", repo_root=ROOT)

    # 3. Exact SAME transition on the true Git commit passes
    res_same = verify_baseline_lineage_transition(
        prior_closeout_sha=true_gov_closeout_sha,
        next_baseline_sha=true_gov_closeout_sha,
        transition_class="SAME",
        repo_root=ROOT,
    )
    assert res_same["status"] == "BASELINE_LINEAGE_VERIFIED"

    # 4. Unexplained drift under SAME fails closed
    with pytest.raises(ConstitutionalIntegrityError):
        verify_baseline_lineage_transition(
            prior_closeout_sha=typo_prose_sha,
            next_baseline_sha=true_gov_closeout_sha,
            transition_class="SAME",
            repo_root=ROOT,
            verify_git_existence=False,
        )

    # 5. Reconciled transition with explicit provenance reconciliation record passes
    res_reconciled = verify_baseline_lineage_transition(
        prior_closeout_sha=typo_prose_sha,
        next_baseline_sha=true_gov_closeout_sha,
        transition_class="SUPERSEDED_BY_AMEND",
        reconciliation_record_path="verification/YM-011-TREE-GAUGE-R1_PROVENANCE_RECONCILIATION.md",
        repo_root=ROOT,
    )
    assert res_reconciled["status"] == "BASELINE_LINEAGE_VERIFIED"

    # 6. Missing reconciliation record fails closed
    with pytest.raises(ConstitutionalIntegrityError, match="requires an explicit reconciliation_record_path"):
        verify_baseline_lineage_transition(
            prior_closeout_sha=typo_prose_sha,
            next_baseline_sha=true_gov_closeout_sha,
            transition_class="SUPERSEDED_BY_AMEND",
            reconciliation_record_path=None,
            repo_root=ROOT,
        )

    # 7. SEMANTIC_REVIEW_REQUIRED always fails closed
    with pytest.raises(ConstitutionalIntegrityError, match="SEMANTIC_REVIEW_REQUIRED"):
        verify_baseline_lineage_transition(
            prior_closeout_sha=true_gov_closeout_sha,
            next_baseline_sha=tree_gauge_candidate_sha,
            transition_class="SEMANTIC_REVIEW_REQUIRED",
            repo_root=ROOT,
        )

    # 8. Extract and validate EVERY 40-character hex SHA in the provenance reconciliation record
    import re
    rec_path = ROOT / "verification" / "YM-011-TREE-GAUGE-R1_PROVENANCE_RECONCILIATION.md"
    rec_text = rec_path.read_text(encoding="utf-8")
    all_40_hex = set(re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", rec_text))
    assert typo_prose_sha in all_40_hex
    valid_commit_shas = all_40_hex - {typo_prose_sha}
    assert len(valid_commit_shas) >= 8
    for sha in sorted(valid_commit_shas):
        assert verify_full_git_object_exists(sha, repo_root=ROOT, require_commit_type=True) == "commit"
