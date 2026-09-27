"""
YM-011-TREE-GAUGE: Maximal-Tree Gauge Fixing and Zero-Mode Separation
=====================================================================

Rigorous finite-lattice constructions, maximal spanning-tree gauge fixing,
co-tree cycle-rank and Bianchi constraint audits, free-boundary vs. periodic-torus
zero-mode separation, and Hessian diagnostics for SU(N) lattice Yang-Mills theory.

Epistemic & Governance Guardrails:
1. Separate Free-Boundary Hypercubic Box Lambda_free(L, d) and Periodic Torus Lambda_per(L, d).
2. Prove maximal-tree gauge fixing from first principles via explicit recursive tree
   parallel transport g_U(x) = g_0 W_T(x_0 -> x)[U], with exact unit Haar Jacobian (J = 1)
   and absence of Faddeev-Popov determinants.
3. Distinguish co-tree edge count |E_cotree| = |E_+| - |V| + 1 from plaquette count |P_+|.
   In d >= 3, plaquette holonomies satisfy non-Abelian 3-cube Bianchi identities and are NOT
   freely independent coordinates.
4. On Free Boundary Lambda_free(L, d):
   - Flat moduli space M_0 = {[I_N]} is a unique isolated point on Sigma_T.
   - Hessian D^2 H|_{Sigma_T}(I_N) has kernel {0} and full rank (N^2 - 1)|E_cotree|.
   - Ordinary finite-dimensional Laplace asymptotics proves Claim A (fixed-volume O(1/beta))
     with leading coefficient C_free(L, d, N) = (N^2 - 1)|E_cotree| / (2 |P_+|) -> (N^2 - 1)/d.
   - However, lambda_min(H_tree(L, d)) -> 0 as L -> infty, so Claim B (volume-uniform O(1/beta))
     is proved ONLY in d = 2 free boundary (exact single-plaquette factorization) and remains
     NOT_ESTABLISHED in d >= 3 by tree gauge alone.
5. On Periodic Torus Lambda_per(L, d):
   - Zero-action configurations on Sigma_T are isomorphic to commuting d-tuples
     Z_per = {(U_1, ..., U_d) in SU(N)^d : [U_mu, U_nu] = I_N}.
   - Moduli space M_flat(T^d, SU(N)) = (T_max)^d / S_N has dimension d(N - 1).
   - At central torons U_cent = (z_1 I_N, ..., z_d I_N), the stabilizer in Ad(SU(N)) jumps
     by N(N - 1) and the Hessian kernel in Sigma_T jumps from (d + N)(N - 1) to d(N^2 - 1),
     exhibiting (d - 1)N(N - 1) transverse quartic commutator zero modes.
   - Ordinary Laplace asymptotics does NOT apply on the periodic torus.
6. Numerical Hessian eigenvalue computations are classified strictly as NUMERICAL_DIAGNOSTIC_ONLY.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import math
from typing import Dict, List, Optional, Tuple
import numpy as np


Vertex = Tuple[int, ...]
# Directed edge: (tail_vertex, axis_mu_0_indexed, head_vertex)
Edge = Tuple[Vertex, int, Vertex]
# Oriented plaquette: (base_vertex, mu_0_indexed, nu_0_indexed) with mu < nu
Plaquette = Tuple[Vertex, int, int]


@dataclass(frozen=True)
class LatticeGraph:
    """Explicit combinatorial structure of a finite d-dimensional lattice."""
    L: int
    d: int
    periodic: bool
    root: Vertex
    vertices: Tuple[Vertex, ...]
    edges_pos: Tuple[Edge, ...]
    tree_edges: Tuple[Edge, ...]
    cotree_edges: Tuple[Edge, ...]
    plaquettes_pos: Tuple[Plaquette, ...]
    num_3_cubes: int
    num_4_cubes: int
    tree_parent_map: Dict[Vertex, Tuple[Vertex, Edge]]

    @property
    def num_vertices(self) -> int:
        return len(self.vertices)

    @property
    def num_edges(self) -> int:
        return len(self.edges_pos)

    @property
    def num_tree_edges(self) -> int:
        return len(self.tree_edges)

    @property
    def num_cotree_edges(self) -> int:
        return len(self.cotree_edges)

    @property
    def cycle_rank(self) -> int:
        return self.num_edges - self.num_vertices + 1

    @property
    def num_plaquettes(self) -> int:
        return len(self.plaquettes_pos)

    @property
    def euler_characteristic(self) -> int:
        return (
            self.num_vertices
            - self.num_edges
            + self.num_plaquettes
            - self.num_3_cubes
            + self.num_4_cubes
        )


@dataclass(frozen=True)
class PlaquetteCoordinateAudit:
    """Audit of the co-tree link to plaquette holonomy map."""
    L: int
    d: int
    periodic: bool
    N: int
    num_vertices: int
    num_edges: int
    num_tree_edges: int
    num_cotree_edges: int
    num_plaquettes: int
    plaquette_minus_cotree: int
    num_independent_bianchi_constraints: int
    global_homology_rank_b1: int
    map_classification: str
    is_global_bijection: bool
    decouples_wilson_action: bool
    haar_jacobian_on_selected_cotree_subset: str
    rank_d1: int = 0
    cochain_constraint_count_scope: str = "LINEARIZED_COCHAIN_RANK_COUNT"
    non_abelian_constraint_scope: str = "NON_ABELIAN_GLOBAL_CONSTRAINT_VARIETY"


@dataclass(frozen=True)
class ToronZeroModeDecomposition:
    """Exact decomposition of flat moduli and Hessian zero modes on the periodic torus."""
    d: int
    N: int
    lie_algebra_dim: int
    cartan_rank: int
    flat_moduli_dim: int
    generic_adjoint_orbit_dim: int
    regular_toron_hessian_nullity: int
    central_toron_hessian_nullity: int
    stabilizer_dim_regular: int
    stabilizer_dim_central: int
    stabilizer_dim_jump: int
    quartic_commutator_zero_modes: int
    num_central_toron_sectors: int
    moduli_space_notation: str


@dataclass(frozen=True)
class HessianDiagnosticResult:
    """Spectral diagnostic of the tree-gauge scalar curl-curl Hessian operator."""
    L: int
    d: int
    periodic: bool
    matrix_size: int
    numerical_rank: int
    numerical_nullity: int
    expected_nullity_per_color: int
    smallest_positive_eigenvalue: float
    largest_eigenvalue: float
    analytical_d2_free_lambda_min: Optional[float]
    epistemic_status: str = "NUMERICAL_DIAGNOSTIC_ONLY"


def build_lattice_graph(L: int, d: int, periodic: bool = False) -> LatticeGraph:
    """
    Constructs either the contractible free-boundary hypercubic box Lambda_free(L, d)
    or the periodic torus Lambda_per(L, d) = (Z / L Z)^d, together with the canonical
    lexicographical comb maximal spanning tree T rooted at x_0 = (0, ..., 0).

    Comb spanning tree rule:
    An interior edge e = (x, mu, x + e_mu) with 0 <= x_mu <= L - 2 belongs to T
    if and only if x_{mu+1} = x_{mu+2} = ... = x_{d-1} = 0 (in 0-indexed axes).
    """
    if L < 2:
        raise ValueError("Lattice linear size L must be >= 2.")
    if d < 2 or d > 4:
        raise ValueError("Dimension d must be in {2, 3, 4}.")

    vertices: Tuple[Vertex, ...] = tuple(itertools.product(range(L), repeat=d))
    root: Vertex = tuple(0 for _ in range(d))

    edges_pos: List[Edge] = []
    tree_edges: List[Edge] = []
    cotree_edges: List[Edge] = []
    tree_parent_map: Dict[Vertex, Tuple[Vertex, Edge]] = {}

    for x in vertices:
        for mu in range(d):
            if not periodic and x[mu] == L - 1:
                continue
            y_list = list(x)
            y_list[mu] = (x[mu] + 1) % L if periodic else (x[mu] + 1)
            y: Vertex = tuple(y_list)
            edge: Edge = (x, mu, y)
            edges_pos.append(edge)

            # Comb tree membership: non-wrapping step (0 <= x[mu] <= L - 2)
            # and all higher-index coordinates x[mu+1:] == 0
            is_non_wrapping = (x[mu] < L - 1)
            higher_coords_zero = all(x[nu] == 0 for nu in range(mu + 1, d))
            if is_non_wrapping and higher_coords_zero:
                tree_edges.append(edge)
                tree_parent_map[y] = (x, edge)
            else:
                cotree_edges.append(edge)

    plaquettes_pos: List[Plaquette] = []
    for x in vertices:
        for mu in range(d):
            for nu in range(mu + 1, d):
                if not periodic and (x[mu] == L - 1 or x[nu] == L - 1):
                    continue
                plaquettes_pos.append((x, mu, nu))

    if periodic:
        num_3_cubes = math.comb(d, 3) * (L ** d) if d >= 3 else 0
        num_4_cubes = math.comb(d, 4) * (L ** d) if d >= 4 else 0
    else:
        num_3_cubes = math.comb(d, 3) * ((L - 1) ** 3) * (L ** (d - 3)) if d >= 3 else 0
        num_4_cubes = math.comb(d, 4) * ((L - 1) ** 4) * (L ** (d - 4)) if d >= 4 else 0

    graph = LatticeGraph(
        L=L,
        d=d,
        periodic=periodic,
        root=root,
        vertices=vertices,
        edges_pos=tuple(edges_pos),
        tree_edges=tuple(tree_edges),
        cotree_edges=tuple(cotree_edges),
        plaquettes_pos=tuple(plaquettes_pos),
        num_3_cubes=num_3_cubes,
        num_4_cubes=num_4_cubes,
        tree_parent_map=tree_parent_map,
    )

    assert graph.num_tree_edges == graph.num_vertices - 1
    assert graph.num_cotree_edges == graph.cycle_rank
    return graph


def compute_tree_gauge_transform(
    graph: LatticeGraph,
    U: Dict[Edge, np.ndarray],
    g_root: Optional[np.ndarray] = None,
) -> Tuple[Dict[Vertex, np.ndarray], Dict[Edge, np.ndarray]]:
    """
    Constructs the explicit recursive maximal-tree gauge transformation g_U: V -> SU(N)
    from first principles such that (g_U . U)(e) = g_U(u) U(e) g_U(v)^{-1} = I_N
    for all e = (u, mu, v) in T.

    Recursive rule along the directed comb tree T rooted at x_0:
        g_U(x_0) = g_root (defaults to I_N)
        g_U(child) = g_U(parent) @ U(parent -> child)
    """
    sample_mat = next(iter(U.values()))
    N = sample_mat.shape[0]
    eye = np.eye(N, dtype=complex)
    root_mat = eye.copy() if g_root is None else g_root.copy()

    g_U: Dict[Vertex, np.ndarray] = {graph.root: root_mat}

    # Resolve vertices in lexicographical / increasing tree depth order:
    # In the comb tree, parent of y = (y_0, ..., y_mu, 0, ..., 0) with y_mu > 0
    # has y_mu - 1, which strictly precedes y in sum(y_k).
    sorted_vertices = sorted(graph.vertices, key=lambda v: sum(v))
    for v in sorted_vertices:
        if v == graph.root:
            continue
        parent_v, tree_edge = graph.tree_parent_map[v]
        g_U[v] = g_U[parent_v] @ U[tree_edge]

    U_fixed: Dict[Edge, np.ndarray] = {}
    for edge in graph.edges_pos:
        u, _, v = edge
        U_fixed[edge] = g_U[u] @ U[edge] @ g_U[v].conj().T

    return g_U, U_fixed


def evaluate_plaquette_holonomy(
    graph: LatticeGraph,
    U: Dict[Edge, np.ndarray],
    plaq: Plaquette,
) -> np.ndarray:
    """
    Computes U_p = U(x, mu) U(x + e_mu, nu) U(x + e_nu, mu)^dagger U(x, nu)^dagger.
    """
    x, mu, nu = plaq
    L = graph.L

    def shift(v: Vertex, axis: int) -> Vertex:
        lst = list(v)
        lst[axis] = (v[axis] + 1) % L if graph.periodic else (v[axis] + 1)
        return tuple(lst)

    x_mu = shift(x, mu)
    x_nu = shift(x, nu)
    x_munu = shift(x_mu, nu)

    e1: Edge = (x, mu, x_mu)
    e2: Edge = (x_mu, nu, x_munu)
    e3: Edge = (x_nu, mu, x_munu)
    e4: Edge = (x, nu, x_nu)

    return U[e1] @ U[e2] @ U[e3].conj().T @ U[e4].conj().T


def reconstruct_d2_free_from_plaquettes(
    L: int,
    plaquette_holonomies: Dict[Plaquette, np.ndarray],
    N: int,
) -> Dict[Edge, np.ndarray]:
    """
    Executes the exact triangular reconstruction of all tree-gauge link variables
    on the 2D free-boundary lattice Lambda_free(L, 2) from the (L-1)^2 plaquette holonomies.

    In comb tree gauge on d=2:
    - All vertical links ((x1, x2), 1, (x1, x2+1)) are in T -> U = I_N.
    - Bottom horizontal spine ((x1, 0), 0, (x1+1, 0)) is in T -> U = I_N.
    - Plaquette p=(x1, x2, 0, 1) has U_p = U_horiz(x1, x2) U_horiz(x1, x2+1)^dagger,
      so U_horiz(x1, x2+1) = U_p^dagger @ U_horiz(x1, x2).
    """
    graph = build_lattice_graph(L=L, d=2, periodic=False)
    eye = np.eye(N, dtype=complex)
    U_reconstructed: Dict[Edge, np.ndarray] = {}

    # Set all tree edges to I_N
    for e in graph.tree_edges:
        U_reconstructed[e] = eye.copy()

    # Reconstruct horizontal co-tree links row by row (x2 = 1 .. L-1)
    for x1 in range(L - 1):
        prev_u = eye.copy()  # U((x1, 0), 0, (x1+1, 0)) = I_N
        for x2 in range(L - 1):
            p: Plaquette = ((x1, x2), 0, 1)
            u_p = plaquette_holonomies[p]
            curr_u = u_p.conj().T @ prev_u
            edge_top: Edge = ((x1, x2 + 1), 0, (x1 + 1, x2 + 1))
            U_reconstructed[edge_top] = curr_u
            prev_u = curr_u

    return U_reconstructed


def audit_plaquette_coordinate_map(
    L: int,
    d: int,
    periodic: bool,
    N: int = 3,
) -> PlaquetteCoordinateAudit:
    """
    Audits whether the map {co-tree links} <-> {plaquette holonomies} is a bijection,
    a constrained embedding, or neither, across dimensions d=2,3,4 and boundary conditions.
    """
    graph = build_lattice_graph(L=L, d=d, periodic=periodic)
    diff = graph.num_plaquettes - graph.num_cotree_edges

    if not periodic:
        b1 = 0
        if d == 2:
            indep_bianchi = 0
            classification = "GLOBAL_TRIANGULAR_BIJECTION_WITH_UNIT_JACOBIAN"
            is_bijection = True
            decouples = True
        else:
            indep_bianchi = graph.num_3_cubes - graph.num_4_cubes
            assert diff == indep_bianchi
            classification = "CONSTRAINED_EMBEDDING_WITH_BIANCHI_SYZYGIES"
            is_bijection = False
            decouples = False
    else:
        b1 = d
        if d == 2:
            indep_bianchi = 1  # Product of all L^2 plaquettes equals commutator [W_1, W_2]
        elif d == 3:
            indep_bianchi = (L ** 3) - 1 + 3
        else:
            indep_bianchi = 3 * (L ** 4) + 3
        classification = "NON_BIJECTIVE_GLOBAL_CYCLE_DEFICIT_AND_BIANCHI_CONSTRAINTS"
        is_bijection = False
        decouples = False

    rank_d1 = graph.num_edges - graph.num_vertices + 1 - b1
    assert rank_d1 == graph.num_cotree_edges - b1
    assert indep_bianchi == graph.num_plaquettes - rank_d1
    assert indep_bianchi == graph.num_plaquettes - graph.num_cotree_edges + b1

    return PlaquetteCoordinateAudit(
        L=L,
        d=d,
        periodic=periodic,
        N=N,
        num_vertices=graph.num_vertices,
        num_edges=graph.num_edges,
        num_tree_edges=graph.num_tree_edges,
        num_cotree_edges=graph.num_cotree_edges,
        num_plaquettes=graph.num_plaquettes,
        plaquette_minus_cotree=diff,
        num_independent_bianchi_constraints=indep_bianchi,
        global_homology_rank_b1=b1,
        map_classification=classification,
        is_global_bijection=is_bijection,
        decouples_wilson_action=decouples,
        haar_jacobian_on_selected_cotree_subset="UNIT_HAAR_JACOBIAN_ON_TRIANGULAR_SPANNING_SUBSET_ONLY",
        rank_d1=rank_d1,
        cochain_constraint_count_scope="LINEARIZED_COCHAIN_RANK_COUNT",
        non_abelian_constraint_scope="NON_ABELIAN_GLOBAL_CONSTRAINT_VARIETY",
    )


def verify_non_abelian_bianchi_cube_identity(
    link_dict_3cube: Dict[Tuple[Tuple[int, int, int], int], np.ndarray],
) -> float:
    """
    Verifies the exact non-Abelian lattice Bianchi identity on a single 3-cube [0,1]^3.

    Let u_i = U(0 -> e_i) for i in {0, 1, 2}.
    When each of the 6 faces of the 3-cube is parallel-transported to the origin (0,0,0),
     define:
        P_{12}(0) = U(0,0) U(e1,1) U(e2,0)^{-1} U(0,1)^{-1}
        P_{23}(0) = U(0,1) U(e2,2) U(e3,1)^{-1} U(0,2)^{-1}
        P_{31}(0) = U(0,2) U(e3,0) U(e1,2)^{-1} U(0,0)^{-1}
        P_{12}(e3) transported by U(0,2): U(0,2) U(e3,0) U(e1+e3,1) U(e2+e3,0)^{-1} U(e3,1)^{-1} U(0,2)^{-1}
        P_{23}(e1) transported by U(0,0): U(0,0) U(e1,1) U(e1+e2,2) U(e1+e3,1)^{-1} U(e1,2)^{-1} U(0,0)^{-1}
        P_{31}(e2) transported by U(0,1): U(0,1) U(e2,2) U(e2+e3,0) U(e1+e2,2)^{-1} U(e2,0)^{-1} U(0,1)^{-1}

    Then the exact non-Abelian telescoping identity holds:
        P_{12}(0) @ P_{23}(e1) @ P_{12}(e3)^{-1} @ P_{23}(0)^{-1} @ P_{31}(e2)^{-1} @ P_{31}(0)^{-1}
    (in the proper cyclic boundary ordering of the 6 faces of the 3-cube) = I_N!
    """
    def u(pt: Tuple[int, int, int], axis: int) -> np.ndarray:
        return link_dict_3cube[(pt, axis)]

    # Define the 6 base-point-transported face loops around the 3-cube:
    # Face 1 (bottom z=0, +xy): 0 -> x -> xy -> y -> 0
    F_z0 = u((0, 0, 0), 0) @ u((1, 0, 0), 1) @ u((0, 1, 0), 0).conj().T @ u((0, 0, 0), 1).conj().T
    # Face 2 (right x=1, +yz, transported via 0->x->xy):
    # Let's write the 3-cube boundary as a single self-cancelling path of 6 plaquette lassos from 0:
    # Lasso 1: Face(z=0) = 0 -> x -> xy -> y -> 0
    L1 = F_z0
    # Lasso 2: (0 -> y) + Face(y=1: y -> xy -> xyz -> yz -> y) + (y -> 0)
    L2 = (
        u((0, 0, 0), 1)
        @ u((0, 1, 0), 0)
        @ u((1, 1, 0), 2)
        @ u((0, 1, 1), 0).conj().T
        @ u((0, 1, 0), 2).conj().T
        @ u((0, 0, 0), 1).conj().T
    )
    #Notice L1 @ L2 = 0 -> x -> xy -> xyz -> yz -> y -> 0!
    # Lasso 3: (0 -> y -> yz) + Face(x=0: yz -> z -> 0 -> y -> yz)^inv = 0 -> y -> yz -> z -> 0
    L3 = (
        u((0, 0, 0), 1)
        @ u((0, 1, 0), 2)
        @ u((0, 0, 1), 1).conj().T
        @ u((0, 0, 0), 2).conj().T
    )
    # Now L1 @ L2 @ L3 = 0 -> x -> xy -> xyz -> yz -> z -> 0!
    # Lasso 4: (0 -> z) + Face(z=1: z -> yz -> xyz -> xz -> z) + (z -> 0)
    L4 = (
        u((0, 0, 0), 2)
        @ u((0, 0, 1), 1)
        @ u((0, 1, 1), 0)
        @ u((1, 0, 1), 1).conj().T
        @ u((0, 0, 1), 0).conj().T
        @ u((0, 0, 0), 2).conj().T
    )
    # Now L1 @ L2 @ L3 @ L4 = 0 -> x -> xy -> xyz -> xz -> z -> 0!
    # Lasso 5: (0 -> x -> xy) + Face(x=1: xy -> x -> xz -> xyz -> xy) + (xy -> x -> 0)
    # Wait: current path is 0 -> x -> xy -> xyz -> xz -> z -> 0.
    # Multiply on left by Lasso 5 = 0 -> z -> xz -> x -> 0:
    L5 = (
        u((0, 0, 0), 2)
        @ u((0, 0, 1), 0)
        @ u((1, 0, 0), 2).conj().T
        @ u((0, 0, 0), 0).conj().T
    )
    # Now L1 @ L2 @ L3 @ L4 @ L5 = 0 -> x -> xy -> xyz -> xz -> x -> 0!
    # Finally Lasso 6 = (0 -> x) + (x -> xz -> xyz -> xy -> x) + (x -> 0):
    L6 = (
        u((0, 0, 0), 0)
        @ u((1, 0, 0), 2)
        @ u((1, 0, 1), 1)
        @ u((1, 1, 0), 2).conj().T
        @ u((1, 0, 0), 1).conj().T
        @ u((0, 0, 0), 0).conj().T
    )
    product_6_faces = L1 @ L2 @ L3 @ L4 @ L5 @ L6
    N = product_6_faces.shape[0]
    return float(np.linalg.norm(product_6_faces - np.eye(N, dtype=complex), ord="fro"))


def compute_tree_gauge_hessian_spectrum(
    L: int,
    d: int,
    periodic: bool = False,
) -> HessianDiagnosticResult:
    """
    Constructs the exact restricted exterior-derivative (lattice curl) matrix
    M = d_Lambda|_{Sigma_T} : R^{E_cotree} -> R^{P_+} and its symmetric Hessian
    H_tree = M^T M : R^{E_cotree} -> R^{E_cotree}, and computes its spectrum.

    Note: All numerical eigenvalue results carry status NUMERICAL_DIAGNOSTIC_ONLY.
    """
    graph = build_lattice_graph(L=L, d=d, periodic=periodic)
    cotree_index: Dict[Edge, int] = {e: idx for idx, e in enumerate(graph.cotree_edges)}

    num_p = graph.num_plaquettes
    num_c = graph.num_cotree_edges
    M = np.zeros((num_p, num_c), dtype=float)

    def shift(v: Vertex, axis: int) -> Vertex:
        lst = list(v)
        lst[axis] = (v[axis] + 1) % L if periodic else (v[axis] + 1)
        return tuple(lst)

    for p_idx, (x, mu, nu) in enumerate(graph.plaquettes_pos):
        x_mu = shift(x, mu)
        x_nu = shift(x, nu)
        x_munu = shift(x_mu, nu)

        e1: Edge = (x, mu, x_mu)
        e2: Edge = (x_mu, nu, x_munu)
        e3: Edge = (x_nu, mu, x_munu)
        e4: Edge = (x, nu, x_nu)

        if e1 in cotree_index:
            M[p_idx, cotree_index[e1]] += 1.0
        if e2 in cotree_index:
            M[p_idx, cotree_index[e2]] += 1.0
        if e3 in cotree_index:
            M[p_idx, cotree_index[e3]] -= 1.0
        if e4 in cotree_index:
            M[p_idx, cotree_index[e4]] -= 1.0

    H_tree = M.T @ M
    eigvals = np.linalg.eigvalsh(H_tree)
    tol = 1e-10
    pos_eigvals = eigvals[eigvals > tol]
    nullity = int(np.sum(np.abs(eigvals) <= tol))
    rank = int(len(pos_eigvals))
    lambda_min_pos = float(np.min(pos_eigvals)) if len(pos_eigvals) > 0 else 0.0
    lambda_max = float(np.max(eigvals)) if len(eigvals) > 0 else 0.0

    expected_nullity = d if periodic else 0
    analytical_d2 = (
        float(4.0 * (math.sin(math.pi / (2.0 * (2 * L - 1))) ** 2))
        if (d == 2 and not periodic)
        else None
    )

    return HessianDiagnosticResult(
        L=L,
        d=d,
        periodic=periodic,
        matrix_size=num_c,
        numerical_rank=rank,
        numerical_nullity=nullity,
        expected_nullity_per_color=expected_nullity,
        smallest_positive_eigenvalue=lambda_min_pos,
        largest_eigenvalue=lambda_max,
        analytical_d2_free_lambda_min=analytical_d2,
        epistemic_status="NUMERICAL_DIAGNOSTIC_ONLY",
    )


def analyze_periodic_toron_zero_modes(d: int, N: int) -> ToronZeroModeDecomposition:
    """
    Computes the exact algebraic and geometric dimensions of the periodic flat-connection
    moduli space M_flat(T^d, SU(N)) = (T_max)^d / S_N and its Hessian zero-mode strata
    inside the root-fixed tree-gauge slice Sigma_{T_per}.
    """
    if d < 2:
        raise ValueError("Dimension d must be >= 2.")
    if N < 2:
        raise ValueError("SU(N) rank parameter N must be >= 2.")

    lie_dim = N * N - 1
    cartan_rank = N - 1
    flat_moduli_dim = d * cartan_rank
    generic_orbit_dim = lie_dim - cartan_rank  # N(N - 1)
    reg_nullity = flat_moduli_dim + generic_orbit_dim  # (d + N)(N - 1)
    cent_nullity = d * lie_dim  # d(N^2 - 1)
    stab_reg = cartan_rank  # dim T_max = N - 1
    stab_cent = lie_dim     # dim SU(N) = N^2 - 1
    stab_jump = stab_cent - stab_reg  # N(N - 1)
    quartic_modes = cent_nullity - reg_nullity  # (d - 1) N (N - 1)
    assert quartic_modes == (d - 1) * N * (N - 1)

    return ToronZeroModeDecomposition(
        d=d,
        N=N,
        lie_algebra_dim=lie_dim,
        cartan_rank=cartan_rank,
        flat_moduli_dim=flat_moduli_dim,
        generic_adjoint_orbit_dim=generic_orbit_dim,
        regular_toron_hessian_nullity=reg_nullity,
        central_toron_hessian_nullity=cent_nullity,
        stabilizer_dim_regular=stab_reg,
        stabilizer_dim_central=stab_cent,
        stabilizer_dim_jump=stab_jump,
        quartic_commutator_zero_modes=quartic_modes,
        num_central_toron_sectors=N ** d,
        moduli_space_notation=f"(T_max)^{d} / S_{N} where T_max = U(1)^{N-1} subset SU({N})",
    )


def evaluate_fixed_volume_equipartition_bound(
    L: int,
    d: int,
    N: int,
    periodic: bool = False,
    claim_scope: str = "CLAIM_A_FIXED_VOLUME_FREE_BOUNDARY",
) -> Dict[str, object]:
    """
    Evaluates the weak-coupling equipartition coefficient for e_plaq(beta, Lambda)
    and enforces strict scope and boundary-condition guardrails.
    """
    if periodic and claim_scope in (
        "CLAIM_A_ORDINARY_LAPLACE_ISOLATED_MINIMUM",
        "CLAIM_B_VOLUME_UNIFORM",
        "CLAIM_C_CONTINUUM_UNIFORM",
    ):
        raise ValueError(
            "Periodic torus retains global toron moduli (T_max)^d / S_N, jumping Ad(SU(N)) "
            "stabilizers, and (d-1)N(N-1) quartic commutator zero modes; ordinary Laplace "
            "asymptotics around an isolated minimum is invalid on the periodic torus."
        )

    if not periodic and d >= 3 and claim_scope in (
        "CLAIM_B_VOLUME_UNIFORM",
        "CLAIM_C_CONTINUUM_UNIFORM",
    ):
        raise ValueError(
            f"In d={d} >= 3, tree-gauge Hessian smallest eigenvalue lambda_min(H_tree(L, d)) -> 0 "
            "as L -> infty and non-Abelian Bianchi cube relations couple plaquettes; fixed-volume "
            "Laplace asymptotics (Claim A) cannot be promoted to volume-uniform (Claim B) or "
            "continuum-uniform (Claim C) without multiscale RG or Brascamp-Lieb control."
        )

    if claim_scope == "CLAIM_C_CONTINUUM_UNIFORM":
        raise ValueError(
            "Claim C (continuum-useful uniform estimate) is NOT established in YM-011-TREE-GAUGE."
        )

    graph = build_lattice_graph(L=L, d=d, periodic=periodic)
    dof_cotree = (N * N - 1) * graph.num_cotree_edges
    c_free = dof_cotree / (2.0 * graph.num_plaquettes)
    thermodynamic_limit_c = (N * N - 1) / float(d)

    return {
        "L": L,
        "d": d,
        "N": N,
        "periodic": periodic,
        "claim_scope": claim_scope,
        "cotree_dof": dof_cotree,
        "num_plaquettes": graph.num_plaquettes,
        "leading_coefficient_C": c_free,
        "thermodynamic_limit_coefficient": thermodynamic_limit_c,
        "volume_uniform_proved": (not periodic and d == 2),
    }
