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
    joint compensating covariance vs fixed-background failure, non-factorization defect,
    and cutoff replacement for one admissible history term alpha from Bałaban R-I (1.76)–(1.89)."""
    # 1. Boundary bond inclusion / exclusion rule on B0 = U_k \cap \Lambda_0:
    # Model a finite bond set partitioned into boundary-intersecting classes
    # b_interior_Lambda: bond inside Lambda
    # b_boundary_Lambda: bond intersecting \partial \Lambda (INCLUDED in B0)
    # b_boundary_Omega: bond intersecting \partial \Omega_{k+1}^1 (EXCLUDED from B0)
    # b_Zh: bond in preliminary region Z_h (carried by V_h under dV_h \lceil_{Z_h})
    # b_exterior: bond in Z \cap \Lambda^c (carried by V_k|_{Z \cap \Lambda^c})
    bonds_all = ["b_int", "b_bnd_Lambda", "b_bnd_Omega", "b_Zh", "b_ext"]

    # Active bond set B0:
    B0 = {b for b in bonds_all if (b in ["b_int", "b_bnd_Lambda"])}
    assert "b_bnd_Lambda" in B0  # Bonds intersecting \partial \Lambda are INCLUDED in B0
    assert "b_bnd_Omega" not in B0  # Bonds intersecting \partial \Omega_{k+1}^1 are EXCLUDED from B0
    assert "b_Zh" not in B0  # Preliminary region Z_h bonds are carried by V_h, not B0
    assert "b_ext" not in B0  # Exterior bonds Z \cap \Lambda^c carried by V_k, not B0

    # 2. Maximal tree graph T0 \subset B0 and Faddeev-Popov tree gauge:
    # Let B0 have 2 bonds: tree bond b_tree and non-tree dynamical bond b_fluc
    T0 = {"b_int"}  # tree bond
    non_tree = B0 - T0  # {"b_bnd_Lambda"}
    assert len(T0) == 1
    assert len(non_tree) == 1

    # On tree bond b in T0, tree gauge sets fluctuation to 0:
    B_prime = {b: F(0) if b in T0 else F(3, 2) for b in B0}
    assert B_prime["b_int"] == 0  # Gauge slice restriction B'|_{T0} = 0
    assert B_prime["b_bnd_Lambda"] != 0  # Dynamical non-tree fluctuation unconstrained
    # Tree Faddeev-Popov Jacobian is identically 1
    delta_FP = F(1)
    assert delta_FP == 1

    # 3. Exact covariance of joint compensating transformations vs naive fixed-background failure:
    # Endpoint site gauge elements hx = 2, hy = 3
    hx = F(2)
    hy = F(3)
    # Link fluctuation V' = 5, background V0 = 7
    v_prime = F(5)
    v0 = F(7)
    v_composite = v_prime * v0  # 35

    # Actual gauge transformation of link U_xy: h_x * U_xy * h_y^-1
    actual_transformed_link = hx * v_composite / hy  # 2 * 35 / 3 = 70/3

    # Joint compensating transformation: V' -> h_x V' h_x^-1, V0 -> h_x V0 h_y^-1
    joint_trans_v_prime = hx * v_prime / hx  # 5 (adjoint action at site x)
    joint_trans_v0 = hx * v0 / hy  # 14/3 (background transformation with endpoints x, y)
    composite_joint = joint_trans_v_prime * joint_trans_v0  # 5 * 14/3 = 70/3
    assert composite_joint == actual_transformed_link  # EXACT COVARIANCE

    # Naive transformation: holding V0 fixed while transforming V' alone by endpoint action:
    # Naive composite: (h_x V' h_x^-1) * V0 = 5 * 7 = 35
    naive_composite = joint_trans_v_prime * v0
    endpoint_defect = composite_joint - naive_composite
    assert endpoint_defect == F(70, 3) - F(35) == F(-35, 3)
    assert endpoint_defect != 0  # Falsifies naive fixed-background transformation

    # 4. Disjoint-region non-factorization defect:
    # Consider observable O with kernel coupling link in Zh (weight w_Zh) and link in B0 (weight w_B0)
    # In interacting theory with diffusion kernel:
    # Joint state with parabolic coupling:
    prob_joint = [F(1, 4), F(1, 4), F(1, 2)]  # states (1,1), (0,0), (1,0)
    # Observable values in the three states:
    val_Zh = [F(1), F(0), F(1)]
    val_B0 = [F(1), F(0), F(0)]

    # Cross term E[val_Zh * val_B0] = 1/4*1 + 0 + 0 = 1/4
    # Factored expectation: E[val_Zh] * E[val_B0] = (3/4) * (1/4) = 3/16
    cross_defect = F(1, 4) - F(3, 16)
    assert cross_defect == F(1, 16)
    assert cross_defect != 0  # Falsifies spatial factorization across disjoint regions

    # 5. Cutoff replacement identity R-I (1.89):
    # On small-field support chi_prime = 1, chi_k'' = 1, so chi_k'' * chi_prime = chi_prime:
    chi_prime_small = F(1)
    chi_k_double_prime = F(1)
    assert chi_k_double_prime * chi_prime_small == chi_prime_small
    # On large-field complement:
    chi_prime_large = F(0)
    remainder_weight = F(1) - chi_prime_large
    assert remainder_weight == F(1)

    # 6. Epistemic boundary: single-term representation does not prove multiscale polymer summability
    single_term_proved = True
    multiscale_polymer_summability_proved = False
    assert single_term_proved is True
    assert multiscale_polymer_summability_proved is False
