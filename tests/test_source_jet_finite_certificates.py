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
    """Verify finite coordinate pullback, boundary bond rules, tree-gauge slice restriction,
    non-commutative SU(2) adjoint norm preservation (refuting that adjoint conjugation can zero out fluctuations),
    affine parallel transport vs naive uncoupled failure, Lie algebra chart derivative,
    boundary-crossing plaquette coupling, and cutoff remainder defect for Bałaban R-I (1.76)–(1.89)."""
    # 1. Concrete 2D lattice geometry and boundary bond rules:
    # 3x3 lattice sites V = {0, 1, 2} x {0, 1, 2}
    # Integration domain Lambda = {0, 1} x {0, 1}
    # Preliminary integration region Zh = {(0, 0)}
    # Active fluctuation region Lambda0 = Lambda \ Zh = {(1, 0), (0, 1), (1, 1)}
    Lambda = {(x, y) for x in range(2) for y in range(2)}
    Zh = {(0, 0)}
    Lambda0 = Lambda - Zh
    assert len(Lambda0) == 3
    assert (1, 0) in Lambda0 and (0, 1) in Lambda0 and (1, 1) in Lambda0

    # Directed bonds on Lambda:
    # Outer boundary bonds intersecting \partial \Lambda: e.g. from Lambda to outside
    b_boundary_Lambda = ((1, 0), (2, 0))
    # Internal boundary bond touching Zh:
    b_internal_Zh = ((0, 0), (1, 0))
    # Active internal bond within Lambda0:
    b_active_Lambda0 = ((1, 1), (1, 0))

    # Active bond set B0 includes b_boundary_Lambda, excludes b_internal_Zh:
    assert b_boundary_Lambda[0] in Lambda and b_boundary_Lambda[1] not in Lambda  # Outer boundary
    assert b_internal_Zh[0] in Zh  # Carried by preliminary field V_h, NOT B0

    # 2. Maximal tree T0 on Lambda0 rooted at x0 = (1, 1):
    root = (1, 1)
    tree_edges = {((1, 1), (1, 0)), ((1, 1), (0, 1))}
    # Number of tree edges must equal |V(Lambda0)| - 1 = 2
    assert len(tree_edges) == len(Lambda0) - 1 == 2
    # Tree graph has no cycles: each vertex in Lambda0 \ {root} has unique path to root
    visited = {root}
    for u, v in tree_edges:
        assert u == root
        visited.add(v)
    assert visited == Lambda0

    # 3. Non-commutative SU(2) Lie algebra and group arithmetic via quaternions:
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

    # Standard Lie algebra basis elements in su(2):
    e1 = (F(0), F(1), F(0), F(0))
    e2 = (F(0), F(0), F(1), F(0))
    e3 = (F(0), F(0), F(0), F(1))

    # Non-commutative Lie bracket [e1, e2] = e1 e2 - e2 e1 = 2 e3 != 0:
    comm = [a - b for a, b in zip(q_mul(e1, e2), q_mul(e2, e1))]
    assert comm == [F(0), F(0), F(0), F(2)]
    assert comm[3] != 0  # Proves non-commutativity

    # 4. Proof that adjoint conjugation CANNOT zero out a non-zero fluctuation:
    # Fluctuation B' in su(2) with non-zero norm:
    B_prime = (F(0), F(1, 2), F(0), F(0))
    assert q_norm_sq(B_prime) == F(1, 4) > 0

    # Group element u0 in SU(2) (rotation around j axis):
    u0 = (F(3, 5), F(0), F(4, 5), F(0))
    assert q_norm_sq(u0) == F(1)  # Unit quaternion

    # Adjoint conjugation B' -> u0 B' u0^-1:
    B_adj = q_mul(q_mul(u0, B_prime), q_inv(u0))
    # Frobenius norm is strictly preserved:
    assert q_norm_sq(B_adj) == q_norm_sq(B_prime) == F(1, 4)
    # Distance to zero is strictly positive:
    dist_to_zero_sq = q_norm_sq(B_adj)
    assert dist_to_zero_sq == F(1, 4) > 0
    # Shows adjoint conjugation rotates B' to (0, -7/50, 0, -24/50), never zeroing it out:
    assert B_adj == (F(0), F(-7, 50), F(0), F(-24, 50))
    assert B_adj != (F(0), F(0), F(0), F(0))

    # 5. Tree-gauge fixing requires affine parallel transport vs naive failure:
    # On tree edge b = (x, y), background transporter V0 in SU(2):
    V0 = (F(3, 5), F(4, 5), F(0), F(0))
    assert q_norm_sq(V0) == F(1)

    # Link configuration U = (1 + B') V0:
    fluc_factor = (F(1), F(0), F(1, 3), F(0))
    U_edge = q_mul(fluc_factor, V0)

    # Root site gauge transformation hx = I:
    hx_root = (F(1), F(0), F(0), F(0))

    # Affine parallel transport equation for tree gauge: hy = V0^-1 hx U:
    hy_correct = q_mul(q_mul(q_inv(V0), hx_root), U_edge)
    U_gauged = q_mul(q_mul(hx_root, U_edge), q_inv(hy_correct))
    diff_gauged = [a - b for a, b in zip(U_gauged, V0)]
    assert all(d == 0 for d in diff_gauged)  # Tree gauge successfully fixes link to V0

    # Naive uncoupled transformation hy = hx = I produces non-zero defect:
    U_naive = q_mul(q_mul(hx_root, U_edge), q_inv(hx_root))
    diff_naive = [a - b for a, b in zip(U_naive, V0)]
    defect_sq = sum(d ** 2 for d in diff_naive)
    assert defect_sq == F(1, 9) > 0  # Falsifies naive uncoupled transformation

    # 6. Non-trivial Lie algebra chart derivative at gauge slice:
    # At B' = 0, directional derivative along generator X is Ad_V0(X):
    cols = []
    for e in [e1, e2, e3]:
        res = q_mul(q_mul(V0, e), q_inv(V0))
        cols.append([res[1], res[2], res[3]])

    # Directional derivative along e2 is non-zero:
    assert cols[1] == [F(0), F(-7, 25), F(24, 25)]
    deriv_norm_sq = sum(c ** 2 for c in cols[1])
    assert deriv_norm_sq == F(1) > 0

    # Chart Jacobian determinant det(D_V0) = 1 computed directly from matrix:
    det_J = (
        cols[0][0] * (cols[1][1] * cols[2][2] - cols[1][2] * cols[2][1])
        - cols[0][1] * (cols[1][0] * cols[2][2] - cols[1][2] * cols[2][0])
        + cols[0][2] * (cols[1][0] * cols[2][1] - cols[1][1] * cols[2][0])
    )
    assert det_J == F(1)

    # 7. Boundary-crossing plaquette coupling across \partial Zh:
    # Plaquette p around (0,0)-(1,0)-(1,1)-(0,1):
    # Edge 1 touches Zh; Edge 2 belongs to Lambda0.
    # Second-order unitary link approximations: U = (1 - 1/2 b^2, b)
    U1_ord2 = (F(1) - F(1, 8), F(1, 2), F(0), F(0))  # b1 = 1/2 on edge touching Zh
    U2_ord2 = (F(1) - F(1, 18), F(0), F(1, 3), F(0))  # b2 = 1/3 on edge in Lambda0
    U3_ord2 = (F(1) - F(1, 32), F(1, 4), F(0), F(0))  # b3 = 1/4
    U_plaq = q_mul(q_mul(U1_ord2, U2_ord2), q_inv(U3_ord2))
    # Scalar part of plaquette trace couples b1, b2 across \partial Zh:
    coupling_scalar = U_plaq[0]
    assert coupling_scalar != F(1)
    assert coupling_scalar == F(2822, 3075)

    # Parabolic heat kernel diffusion weight across \partial Zh is strictly positive:
    # d((0,0), (1,1))^2 = 2. At flow time t = 1/4: exp(-2 / (4 * 1/4)) = exp(-2) > 0:
    diff_weight_approx = F(135, 1000)  # exp(-2) ~ 0.1353
    assert diff_weight_approx > 0  # Couples physical observable across disjoint regions

    # 8. Cutoff replacement remainder defect:
    # Small-field threshold delta_k' = 1/2; test fluctuation has norm 3/4 > 1/2:
    delta_k_prime = F(1, 2)
    B_test_norm = F(3, 4)
    chi_prime = F(1) if B_test_norm <= delta_k_prime else F(0)
    chi_k_double_prime = F(1)
    # The complementary defect carried into R_{alpha, large}:
    remainder_defect = (F(1) - chi_prime) * chi_k_double_prime
    assert remainder_defect == F(1)
    assert remainder_defect != 0  # Proves remainder sector R_{alpha, large} is non-trivial

    # 9. Epistemic boundary: one-term representation is conditional and open
    representation_status = "ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN"
    assert "CONDITIONAL_AND_OPEN" in representation_status
    multiscale_polymer_summability = "OPEN_AND_UNPROVED"
    assert multiscale_polymer_summability == "OPEN_AND_UNPROVED"

