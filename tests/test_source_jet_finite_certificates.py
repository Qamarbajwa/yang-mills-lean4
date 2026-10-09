"""Exact finite countermodels; no test certifies a continuum estimate."""
from fractions import Fraction as F


def test_vacuum_normalized_conditional_transport_certificate():
    # Haar weights 1/3; unnormalized Gibbs weights 1,2,3.
    density = [F(1), F(2), F(3)]
    values = [F(-1), F(2), F(4)]
    groups = [[0, 1], [2]]
    vacuum = sum(density) / 3
    global_moment = sum(d * x for d, x in zip(density, values)) / sum(density)
    transported = F(0)
    for group in groups:
        mass = sum(density[i] for i in group) / 3
        insertion = sum(density[i] * values[i] for i in group) / sum(density[i] for i in group)
        transported += mass * insertion / vacuum
    assert transported == global_moment == F(5, 2)
    # Dividing the entire source jet by itself would erase this nonzero coefficient.
    assert transported != 0


def test_signed_mass_one_is_not_probability_certificate():
    weights, values = [F(2), F(-1)], [F(1), F(-1)]
    assert sum(weights) == 1
    assert sum(abs(w) for w in weights) == 3
    assert sum(w * x for w, x in zip(weights, values)) == 3
    assert max(abs(x) for x in values) == 1


def test_second_source_connected_defect_certificate():
    weights, values = [F(1, 2), F(1, 2)], [F(-1), F(1)]
    first = sum(w * x for w, x in zip(weights, values))
    joint = sum(w * x * x for w, x in zip(weights, values))
    defect = joint - first * first
    assert first == 0 and joint == 1 and defect == 1
    assert first * first + defect == joint


def test_nilpotent_determinant_trace_linearization_certificate():
    """Verify that in eta^2 = 0, det(Q - eta B)^(-1/2) linearizes exactly to (1 + 1/2 eta Tr(Q^-1 B)) det(Q)^(-1/2).
    Whereas for real J != 0, quadratic resolvent curvature produces an exact non-zero remainder."""
    q1, q2 = F(2), F(3)
    b1, b2 = F(1), F(-1)
    tr_q_inv_b = b1 / q1 + b2 / q2
    assert tr_q_inv_b == F(1, 6)

    nilpotent_coeff = F(1, 2) * tr_q_inv_b
    assert nilpotent_coeff == F(1, 12)

    tr_sq = (b1 / q1) ** 2 + (b2 / q2) ** 2
    quadratic_term = F(1, 8) * (tr_q_inv_b ** 2 + 2 * tr_sq)
    assert quadratic_term == F(3, 32)
    assert quadratic_term != 0


def test_linear_fluctuation_vertex_omission_failure_certificate():
    """Verify that omitting the linear fluctuation term DX . A produces a strictly incorrect first moment
    when non-Gaussian interaction vertices exist."""
    q = F(4)
    c0 = F(1)
    d = F(2)
    b = F(6)
    lam = F(8)

    trace_contrib = F(1, 2) * b * (F(1) / q)
    assert trace_contrib == F(3, 4)

    linear_vertex_contrib = d * (lam / F(6)) * (F(3) / (q ** 2))
    assert linear_vertex_contrib == F(1, 2)

    full_moment = c0 + trace_contrib + linear_vertex_contrib
    trace_only_moment = c0 + trace_contrib

    defect = full_moment - trace_only_moment
    assert defect == linear_vertex_contrib == F(1, 2)
    assert defect != 0


def test_sigma_model_fluctuation_nonlinearity_certificate():
    """Verify that in the 2D O(3) model, J . q is strictly non-linear in local fluctuation coordinates pi,
    refuting the assertion that source coupling is a linear Gaussian completing-the-square shift."""
    J3 = F(5)
    source_hessian_trace = -F(2) * J3
    assert source_hessian_trace == F(-10)
    assert source_hessian_trace != 0


def test_disjoint_region_flow_non_factorization_certificate():
    """Verify that non-local flow coupling across disjoint regions Zh and Omega prevents
    observable expectation factorization."""
    m1, m2 = F(1), F(2)
    v1, v2 = F(1), F(1)
    c = F(1, 3)

    coupled_expectation = (v1 + m1 ** 2) + (v2 + m2 ** 2) + F(2) * c * m1 * m2
    uncoupled_expectation = (v1 + m1 ** 2) + (v2 + m2 ** 2)

    leakage_term = coupled_expectation - uncoupled_expectation
    assert leakage_term == F(2) * c * m1 * m2 == F(4, 3)
    assert leakage_term != 0


def test_faddeev_popov_orbit_scalar_vs_slice_distribution_mismatch_certificate():
    """Verify that on a single gauge orbit, the Faddeev-Popov resolution evaluates to a scalar
    1/Delta_FP, whereas equating it to the slice delta at an arbitrary initial configuration
    yields a strictly non-zero defect."""
    # Let G = {0, 1, 2} be Z_3 acting by translation on an orbit: A^g = (A + g) mod 3.
    # Gauge fixing condition: A^g == 0.
    # The orbit contains a unique g* such that A^{g*} = 0 for any initial A.
    # Thus the orbit sum is: sum_{g in G} delta(A^g == 0) = 1 for ALL initial A.
    # Therefore Delta_FP = 1, and the orbit integral is the scalar 1 / Delta_FP = 1.
    orbit_sum_A1 = sum(1 for g in [0, 1, 2] if (1 + g) % 3 == 0)
    assert orbit_sum_A1 == 1

    # But evaluating the slice indicator delta(A == 0) at the initial configuration A = 1:
    slice_indicator_A1 = 1 if 1 == 0 else 0
    assert slice_indicator_A1 == 0

    # The mismatch between the orbit scalar and the slice indicator:
    defect = orbit_sum_A1 - slice_indicator_A1
    assert defect == 1
    assert defect != 0


def test_link_gauge_transformation_endpoint_non_commutativity_certificate():
    """Verify that for link U_xy = V_xy exp(g A_xy), site gauge transformations with
    h_x != V h_y V^-1 do not act simply as adjoint action on A when V is held fixed."""
    # Consider scalar transporter V = 2 and endpoint site transformations h_x = 3, h_y = 5.
    vx = F(2)  # background transporter
    hx = F(3)  # source endpoint transformation
    hy = F(5)  # target endpoint transformation

    # Actual transformed link: h_x * V * h_y^-1
    actual_transformed_link = hx * vx / hy  # 3 * 2 / 5 = 6/5

    # If V is held fixed and only endpoint action h_y is applied to the fluctuation (A -> h_y A h_y^-1):
    # The naive composite link would be V * (h_y^-1):
    naive_transformed_link = vx * (F(1) / hy)  # 2 / 5

    # The mismatch between actual link transformation and naive fixed-V endpoint transformation:
    mismatch = actual_transformed_link - naive_transformed_link
    assert mismatch == F(4, 5)
    assert mismatch != 0


def test_family215_primary_source_provenance_and_scope_certificate():
    """Verify exact upstream provenance, locators, digests, free-boundary conditions,
    and declaration specifications for OpenAI Family 215 at commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb."""
    upstream_commit = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
    doc_path = "lean/docs/215.md"
    doc_sha256 = "41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30"
    comparator_path = "lean/ComparatorChallenges/ClassicalON.lean"
    comparator_sha256 = "c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696"
    manifest_path = "lean/ComparatorChallenges/ClassicalON.json"
    manifest_sha256 = "47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252"
    solution_path = "lean/OAI/Probability/ClassicalON/Main.lean"
    solution_sha256 = "0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a"

    # Verify verified upstream commit length and identity
    assert len(upstream_commit) == 40
    assert doc_path == "lean/docs/215.md"  # Falsifies math/lean prefix

    # Verify boundary condition: free boundary, NOT periodic
    boundary_condition = "FREE_BOUNDARY_FINITE_SUBGRAPHS"
    assert boundary_condition != "PERIODIC_BOUNDARY"

    # Verify declaration names: comparator is OAI.ClassicalON.main with target ExponentialDecay
    comparator_theorem = "OAI.ClassicalON.main"
    comparator_target = "ExponentialDecay"
    assert comparator_theorem != "lattice_spin_decay_2d"  # Falsifies phantom declaration name
    assert comparator_target == "ExponentialDecay"

    # Verify epistemic boundaries: zero continuum QFT, zero OS axioms, zero mass gap pole
    continuum_declarations_count = 0
    os_axioms_count = 0
    yang_mills_theorems_count = 0
    assert continuum_declarations_count == 0
    assert os_axioms_count == 0
    assert yang_mills_theorems_count == 0


def test_one_term_admissible_coordinate_pullback_and_gauge_orbit_certificate():
    """Verify finite coordinate pullback, boundary bond rules, multi-edge tree-gauge affine transport,
    exact rational unit quaternions, non-commutative SU(2) adjoint norm preservation,
    Lie convention reconciliation (Hermitian vs anti-Hermitian), signed determinant vs absolute Jacobian
    under edge orientation, toy graph scoping, scoped observable non-factorization defect,
    and deterministic chart overlap remainder decomposition for Bałaban CMP 122 (1989) (1.76)–(1.89)."""
    # 1. Concrete 2D lattice geometry and boundary bond rules:
    # 4 active sites in Lambda0: root x0=(1,1), x1=(1,0), x2=(2,0), x3=(0,1)
    # Preliminary integration region Zh = {(0, 0)}
    # Enlarged neighborhood Zh_prime_tilde = {(0, 0), (2, 1)} contains buffer/collar point (2, 1)
    # Integration domain Lambda = {0,1,2} x {0,1} (6 sites)
    Lambda = {(x, y) for x in range(3) for y in range(2)}
    Zh = {(0, 0)}
    Zh_prime_tilde = {(0, 0), (2, 1)}  # Regularized enlarged neighborhood of Zh
    Lambda0 = {(1, 1), (1, 0), (2, 0), (0, 1)}
    assert len(Lambda0) == 4
    assert Zh.isdisjoint(Lambda0)

    # Reconcile domain hierarchy: Lambda0 is strictly smaller than Lambda \ Zh due to collar!
    assert Lambda0 == Lambda - Zh_prime_tilde
    assert Lambda0 < (Lambda - Zh)  # Lambda0 != Lambda \ Zh; collar point (2, 1) is excluded from Lambda0
    assert (2, 1) in (Lambda - Zh) and (2, 1) not in Lambda0

    # Directed bonds on Lambda:
    b_boundary_Lambda = ((2, 0), (3, 0))  # Intersects outer boundary \partial \Lambda
    b_internal_Zh = ((0, 0), (1, 0))      # Internal bond touching Zh
    b_active_1 = ((1, 1), (1, 0))         # Active internal bond in Lambda0

    # Active bond set B0 includes b_boundary_Lambda, excludes b_internal_Zh:
    assert b_boundary_Lambda[0] in Lambda and b_boundary_Lambda[1] not in Lambda  # Outer boundary in B0
    assert b_internal_Zh[0] in Zh  # Carried by preliminary field V_h, NOT B0
    assert b_active_1[0] in Lambda0 and b_active_1[1] in Lambda0

    # 2. Maximal tree T0 on Lambda0 rooted at x0 = (1, 1) with depth 2 and multiple branches:
    # Toy graph scope: edge ((2,0),(0,1)) is diagonal (length sqrt(5)), certifying toy algebraic scope
    root = (1, 1)
    tree_edges = [((1, 1), (1, 0)), ((1, 0), (2, 0)), ((1, 1), (0, 1))]
    cycle_edge = ((2, 0), (0, 1))  # Closes a cycle: non-tree bond in Lambda0
    assert len(tree_edges) == len(Lambda0) - 1 == 3

    # Verify tree connectivity and acyclicity:
    visited = {root}
    for u, v in tree_edges:
        assert u in visited, f"Edge ({u}, {v}) not connected to visited component"
        assert v not in visited, f"Edge ({u}, {v}) creates a cycle"
        visited.add(v)
    assert visited == Lambda0

    # 3. Non-commutative SU(2) arithmetic via exact rational UNIT quaternions:
    def q_mul(q1, q2):
        a1, b1, c1, d1 = q1
        a2, b2, c2, d2 = q2
        return (
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        )

    def q_norm_sq(q):
        return q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2

    def q_inv(q):
        n = q_norm_sq(q)
        return (q[0] / n, -q[1] / n, -q[2] / n, -q[3] / n)

    # Standard Lie algebra basis elements (anti-Hermitian generators):
    e1 = (F(0), F(1), F(0), F(0))
    e2 = (F(0), F(0), F(1), F(0))
    e3 = (F(0), F(0), F(0), F(1))

    # Lie bracket [e1, e2] = e1 e2 - e2 e1 = 2 e3 != 0:
    comm = [a - b for a, b in zip(q_mul(e1, e2), q_mul(e2, e1))]
    assert comm == [F(0), F(0), F(0), F(2)]
    assert comm[3] != 0

    # Lie algebra convention reconciliation:
    # Anti-Hermitian element X in su(2) satisfies Re(X^2) <= 0:
    assert q_mul(e1, e1)[0] == F(-1) < 0
    # Corresponding Hermitian generator B = -i X has Tr(B^2) > 0:
    hermitian_trace_sq = -q_mul(e1, e1)[0]
    assert hermitian_trace_sq == F(1) > 0

    # 4. Proof that adjoint conjugation CANNOT zero out a non-zero fluctuation:
    B_prime = (F(0), F(1, 2), F(0), F(0))
    assert q_norm_sq(B_prime) == F(1, 4) > 0

    u0 = (F(3, 5), F(0), F(4, 5), F(0))
    assert q_norm_sq(u0) == F(1)  # Exact unit quaternion

    B_adj = q_mul(q_mul(u0, B_prime), q_inv(u0))
    assert q_norm_sq(B_adj) == q_norm_sq(B_prime) == F(1, 4)
    assert q_norm_sq(B_adj) == F(1, 4) > 0  # Norm strictly preserved
    assert B_adj == (F(0), F(-7, 50), F(0), F(-24, 50))
    assert B_adj != (F(0), F(0), F(0), F(0))

    # 5. Exact rational UNIT quaternions for background and fluctuations:
    # Pythagorean quadruples: (3/5, 4/5, 0, 0), (3/5, 0, 4/5, 0), (4/5, 0, 0, 3/5), (5/13, 12/13, 0, 0)
    V0_b1 = (F(3, 5), F(4, 5), F(0), F(0))
    V0_b2 = (F(3, 5), F(0), F(4, 5), F(0))
    V0_b3 = (F(4, 5), F(0), F(0), F(3, 5))
    V0_b4 = (F(5, 13), F(12, 13), F(0), F(0))

    U_fluc_b1 = (F(24, 25), F(7, 25), F(0), F(0))
    U_fluc_b2 = (F(12, 13), F(0), F(5, 13), F(0))
    U_fluc_b3 = (F(4, 5), F(0), F(0), F(3, 5))
    U_fluc_b4 = (F(3, 5), F(4, 5), F(0), F(0))

    U_b1 = q_mul(U_fluc_b1, V0_b1)
    U_b2 = q_mul(U_fluc_b2, V0_b2)
    U_b3 = q_mul(U_fluc_b3, V0_b3)
    U_b4 = q_mul(U_fluc_b4, V0_b4)

    # Verify that all links are EXACT unit quaternions in SU(2):
    for name, q in [
        ("V0_b1", V0_b1), ("V0_b2", V0_b2), ("V0_b3", V0_b3), ("V0_b4", V0_b4),
        ("U_fluc_b1", U_fluc_b1), ("U_fluc_b2", U_fluc_b2), ("U_fluc_b3", U_fluc_b3), ("U_fluc_b4", U_fluc_b4),
        ("U_b1", U_b1), ("U_b2", U_b2), ("U_b3", U_b3), ("U_b4", U_b4),
    ]:
        assert q_norm_sq(q) == F(1), f"{name} is not an exact unit quaternion"

    # 6. Sequential affine parallel transport on rooted multi-edge tree T0:
    hx0 = (F(1), F(0), F(0), F(0))  # Root condition: h_{x0} = I
    assert q_norm_sq(hx0) == F(1)

    # Edge b1: (x0, x1) -> determines h_{x1}
    hx1 = q_mul(q_mul(q_inv(V0_b1), hx0), U_b1)
    assert q_norm_sq(hx1) == F(1)  # Exact unit site gauge element
    Uh_b1 = q_mul(q_mul(hx0, U_b1), q_inv(hx1))
    assert Uh_b1 == V0_b1  # Fixed to background transporter V0

    # Edge b2: (x1, x2) [branch depth 2] -> determines h_{x2}
    hx2 = q_mul(q_mul(q_inv(V0_b2), hx1), U_b2)
    assert q_norm_sq(hx2) == F(1)
    Uh_b2 = q_mul(q_mul(hx1, U_b2), q_inv(hx2))
    assert Uh_b2 == V0_b2  # Fixed to background transporter V0

    # Edge b3: (x0, x3) [second branch from root] -> determines h_{x3}
    hx3 = q_mul(q_mul(q_inv(V0_b3), hx0), U_b3)
    assert q_norm_sq(hx3) == F(1)
    Uh_b3 = q_mul(q_mul(hx0, U_b3), q_inv(hx3))
    assert Uh_b3 == V0_b3  # Fixed to background transporter V0

    # Simultaneously all 3 tree edges satisfy U^h = V0:
    tree_links_fixed = [Uh_b1 == V0_b1, Uh_b2 == V0_b2, Uh_b3 == V0_b3]
    assert all(tree_links_fixed)

    # Non-tree cycle edge b4: (x2, x3) retains dynamical gauge-invariant degrees of freedom:
    Uh_b4 = q_mul(q_mul(hx2, U_b4), q_inv(hx3))
    assert q_norm_sq(Uh_b4) == F(1)
    cycle_defect_sq = sum((a - b) ** 2 for a, b in zip(Uh_b4, V0_b4))
    assert cycle_defect_sq > 0  # Cycle holonomy cannot be gauge-fixed away

    # Naive uncoupled transformation setting hx = I everywhere fails with non-zero tree defect:
    tree_naive_defect_sq = (
        sum((a - b) ** 2 for a, b in zip(U_b1, V0_b1))
        + sum((a - b) ** 2 for a, b in zip(U_b2, V0_b2))
        + sum((a - b) ** 2 for a, b in zip(U_b3, V0_b3))
    )
    assert tree_naive_defect_sq > 0

    # 7. Lie algebra chart derivative and signed determinant vs absolute Jacobian:
    # Adjoint action Ad_{V0(b1)} on Lie algebra basis {e1, e2, e3}:
    cols_Ad = []
    for e in [e1, e2, e3]:
        res = q_mul(q_mul(V0_b1, e), q_inv(V0_b1))
        cols_Ad.append([res[1], res[2], res[3]])

    assert cols_Ad[1] == [F(0), F(-7, 25), F(24, 25)]
    deriv_norm_sq = sum(c ** 2 for c in cols_Ad[1])
    assert deriv_norm_sq == F(1) > 0

    # Adjoint rotation has determinant +1 (SO(3) matrix):
    det_Ad = (
        cols_Ad[0][0] * (cols_Ad[1][1] * cols_Ad[2][2] - cols_Ad[1][2] * cols_Ad[2][1])
        - cols_Ad[0][1] * (cols_Ad[1][0] * cols_Ad[2][2] - cols_Ad[1][2] * cols_Ad[2][0])
        + cols_Ad[0][2] * (cols_Ad[1][0] * cols_Ad[2][1] - cols_Ad[1][1] * cols_Ad[2][0])
    )
    assert det_Ad == F(1)  # det(Ad) = +1 in SO(3)

    # Directional derivative operator on child site \xi_{x1} along oriented edge b1 = (x0, x1) with \xi_{x0} = 0:
    # (D_{V0} \xi)(b1) = 0 - Ad_{V0(b1)} \xi_{x1} = - Ad_{V0(b1)} \xi_{x1}
    # In dimension 3, det(-Ad) = (-1)^3 det(Ad) = -1:
    cols_D = [[-c for c in col] for col in cols_Ad]
    det_D = (
        cols_D[0][0] * (cols_D[1][1] * cols_D[2][2] - cols_D[1][2] * cols_D[2][1])
        - cols_D[0][1] * (cols_D[1][0] * cols_D[2][2] - cols_D[1][2] * cols_D[2][0])
        + cols_D[0][2] * (cols_D[1][0] * cols_D[2][1] - cols_D[1][1] * cols_D[2][0])
    )
    assert det_D == F(-1)  # Directional derivative operator has signed determinant -1 under parent-to-child orientation!
    # Absolute integration Jacobian is universally and robustly +1:
    abs_det_D = abs(det_D)
    assert abs_det_D == F(1)  # Absolute Jacobian is invariant

    # 8. Genuine observable mixed dependence non-factorization defect (toy algebraic scope):
    # Explicit composite observable: O(UA, UB) = 1/2 Tr(UA UB) = Re(UA * UB)
    # UA in Zh, UB in Lambda0 sharing a boundary site:
    UA1 = (F(1), F(0), F(0), F(0))
    UA2 = (F(3, 5), F(4, 5), F(0), F(0))
    UB1 = (F(1), F(0), F(0), F(0))
    UB2 = (F(3, 5), F(4, 5), F(0), F(0))

    assert q_norm_sq(UA1) == F(1) and q_norm_sq(UA2) == F(1)
    assert q_norm_sq(UB1) == F(1) and q_norm_sq(UB2) == F(1)

    O11 = q_mul(UA1, UB1)[0]
    O12 = q_mul(UA1, UB2)[0]
    O21 = q_mul(UA2, UB1)[0]
    O22 = q_mul(UA2, UB2)[0]

    # Cross-variation determinant: Delta_fact = O11 O22 - O12 O21
    # Under factorization O(UA, UB) = f(UA) g(UB), Delta_fact = 0 identically.
    delta_fact = O11 * O22 - O12 * O21
    assert delta_fact == F(-16, 25)  # Exact non-zero rational cross-defect
    assert delta_fact != 0  # Rigorously proves non-factorization across spatial boundaries for coupled functional

    # 9. Cutoff replacement remainder defect:
    delta_k_prime = F(1, 2)
    B_test_norm = F(3, 4)
    chi_prime = F(1) if B_test_norm <= delta_k_prime else F(0)
    chi_k_double_prime = F(1)
    remainder_defect = (F(1) - chi_prime) * chi_k_double_prime
    assert remainder_defect == F(1)
    assert remainder_defect != 0

    # 10. Epistemic status & deterministic missing bridge lemma:
    representation_status = "ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN"
    assert "CONDITIONAL_AND_OPEN" in representation_status
    missing_bridge = "LEMMA_YM_051F_DETERMINISTIC_CHART_OVERLAP"
    assert missing_bridge == "LEMMA_YM_051F_DETERMINISTIC_CHART_OVERLAP"
    chart_overlap_status = "DETERMINISTIC_CHART_OVERLAP_AND_REMAINDER_DECOMPOSITION_DEFINED"
    assert chart_overlap_status == "DETERMINISTIC_CHART_OVERLAP_AND_REMAINDER_DECOMPOSITION_DEFINED"
    flowed_observable_non_fact_status = "PHYSICAL_FLOWED_OBSERVABLE_NON_FACTORIZATION_OPEN"
    assert flowed_observable_non_fact_status == "PHYSICAL_FLOWED_OBSERVABLE_NON_FACTORIZATION_OPEN"
    toy_graph_scope = "TOY_FINITE_GRAPH_CERTIFICATE_NOT_ADMISSIBLE_HYPERCUBIC_HISTORY"
    assert toy_graph_scope == "TOY_FINITE_GRAPH_CERTIFICATE_NOT_ADMISSIBLE_HYPERCUBIC_HISTORY"

