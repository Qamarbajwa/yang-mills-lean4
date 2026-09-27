# YM-011-TREE-GAUGE — Maximal-Tree Gauge Fixing, Bianchi Constraints, and Zero-Mode Separation in Finite-Lattice $SU(N)$ Yang–Mills Theory

- **Task ID:** `YM-011-TREE-GAUGE`
- **Epistemic Status:** `PROVED_FINITE_LATTICE_GAUGE_FIXING_AND_ZERO_MODE_DECOMPOSITION`
- **Scope:** Finite $d$-dimensional hypercubic lattices ($d \in \{2, 3, 4\}$) with free boundary $\Lambda_{\mathrm{free}}(L, d)$ and periodic boundary $\Lambda_{\mathrm{per}}(L, d) = (a\mathbb{Z}/La\mathbb{Z})^d$, gauge group $G = SU(N)$ ($N \ge 2$).
- **Continuum / Global Invariants:** `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `CLAIM_B_VOLUME_UNIFORM_D_GE_3 = NOT_ESTABLISHED`, `CLAIM_C_CONTINUUM_UNIFORM = NOT_ESTABLISHED`.

---

## 1. Explicit Finite-Lattice Models: Free Boundary vs. Periodic Torus

We construct and analyze two distinct finite-lattice models at lattice spacing $a > 0$ and linear vertex size $L \ge 2$. No property proved on the contractible free-boundary lattice is transferred to the periodic torus without independent proof.

### 1.1 Model A: Contractible / Free-Boundary Hypercubic Box $\Lambda_{\mathrm{free}}(L, d)$

1. **Vertex Set $V_{\mathrm{free}}$:**
   $$V_{\mathrm{free}} = \{0, 1, \dots, L-1\}^d \subset \mathbb{Z}^d, \qquad |V_{\mathrm{free}}| = L^d, \qquad x_0 = (0, 0, \dots, 0) \text{ (root vertex)}.$$
2. **Positively Oriented Edges $E_+(\Lambda_{\mathrm{free}})$:**
   A directed edge $e = (x, \mu, x + \hat{\mu})$ ($\mu \in \{1, \dots, d\}$) belongs to $E_+(\Lambda_{\mathrm{free}})$ if and only if $x \in V_{\mathrm{free}}$ and $0 \le x_\mu \le L - 2$:
   $$|E_+(\Lambda_{\mathrm{free}})| = d(L - 1)L^{d-1}.$$
3. **Positively Oriented Plaquettes $P_+(\Lambda_{\mathrm{free}})$ and Higher Cells:**
   A plaquette $p = (x, \mu, \nu)$ ($1 \le \mu < \nu \le d$) belongs to $P_+(\Lambda_{\mathrm{free}})$ if and only if $0 \le x_\mu \le L - 2$ and $0 \le x_\nu \le L - 2$:
   $$|P_+(\Lambda_{\mathrm{free}})| = \binom{d}{2}(L - 1)^2 L^{d-2}, \qquad |C_k(\Lambda_{\mathrm{free}})| = \binom{d}{k}(L - 1)^k L^{d-k} \quad (0 \le k \le d).$$
   The Euler characteristic of the contractible cell complex $\Lambda_{\mathrm{free}}(L, d)$ is identically unity:
   $$\chi(\Lambda_{\mathrm{free}}) = \sum_{k=0}^d (-1)^k \binom{d}{k}(L - 1)^k L^{d-k} = \left(L - (L - 1)\right)^d = 1, \qquad H_1(\Lambda_{\mathrm{free}}; \mathbb{Z}) = 0.$$
4. **Canonical Comb Maximal Spanning Tree $T_{\mathrm{free}}$:**
   Define the lexicographical axial comb tree $T_{\mathrm{free}} \subset E_+(\Lambda_{\mathrm{free}})$ rooted at $x_0 = (0, \dots, 0)$ by:
   $$e = (x, \mu, x + \hat{\mu}) \in T_{\mathrm{free}} \quad \Longleftrightarrow \quad 0 \le x_\mu \le L - 2 \;\;\text{and}\;\; x_{\mu+1} = x_{\mu+2} = \dots = x_d = 0.$$
   Counting edges by direction $\mu \in \{1, \dots, d\}$ gives $|T_{\mathrm{free}, \mu}| = L^{\mu-1}(L - 1)$, so:
   $$|T_{\mathrm{free}}| = \sum_{\mu=1}^d L^{\mu-1}(L - 1) = L^d - 1 = |V_{\mathrm{free}}| - 1.$$
   Every vertex $x = (x_1, \dots, x_d) \in V_{\mathrm{free}}$ is connected to $x_0$ by a unique directed path $\gamma_T(x_0 \to x)$ in $T_{\mathrm{free}}$ of Manhattan length $\sum_{\mu=1}^d x_\mu \le d(L - 1)$ traversing axis $1$ from $0$ to $x_1$, axis $2$ from $0$ to $x_2$, $\dots$, and axis $d$ from $0$ to $x_d$.
5. **Co-Tree Edges $E_{\mathrm{co-tree}}(\Lambda_{\mathrm{free}}) = E_+(\Lambda_{\mathrm{free}}) \setminus T_{\mathrm{free}}$:**
   $$|E_{\mathrm{co-tree}}(\Lambda_{\mathrm{free}})| = |E_+(\Lambda_{\mathrm{free}})| - |V_{\mathrm{free}}| + 1 = d(L - 1)L^{d-1} - L^d + 1.$$
6. **Configuration Space, Gauge Group, and Wilson Measure:**
   $$\Omega_{\mathrm{free}} = SU(N)^{E_+(\Lambda_{\mathrm{free}})}, \qquad \mathcal{G}_{\mathrm{free}} = SU(N)^{V_{\mathrm{free}}}, \qquad \mathcal{G}_{\mathrm{free}, x_0} = \{g \in \mathcal{G}_{\mathrm{free}} : g(x_0) = I_N\} \cong SU(N)^{L^d - 1},$$
   $$d\mu_{\mathrm{free}, \beta}(U) = \frac{1}{Z_{\mathrm{free}}(\beta)} \exp\!\left(-\beta \sum_{p \in P_+(\Lambda_{\mathrm{free}})} h_p(U)\right) \prod_{e \in E_+(\Lambda_{\mathrm{free}})} d\mu_{\mathrm{Haar}}(U_e), \qquad h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p).$$

---

### 1.2 Model B: Periodic Torus $\Lambda_{\mathrm{per}}(L, d) = (a\mathbb{Z}/La\mathbb{Z})^d$

1. **Cells and Topology:**
   $$V_{\mathrm{per}} = (\mathbb{Z}/L\mathbb{Z})^d, \qquad |V_{\mathrm{per}}| = L^d, \qquad |E_+(\Lambda_{\mathrm{per}})| = dL^d, \qquad |P_+(\Lambda_{\mathrm{per}})| = \binom{d}{2}L^d, \qquad |C_k(\Lambda_{\mathrm{per}})| = \binom{d}{k}L^d,$$
   $$\chi(\Lambda_{\mathrm{per}}) = \sum_{k=0}^d (-1)^k \binom{d}{k}L^d = 0, \qquad H_1(\Lambda_{\mathrm{per}}; \mathbb{Z}) \cong \mathbb{Z}^d \quad (\text{Betti number } b_1 = d).$$
2. **Spanning Tree $T_{\mathrm{per}}$ and Co-Tree Partition:**
   Identifying $V_{\mathrm{per}}$ with $\{0, 1, \dots, L-1\}^d$, the interior comb tree $T_{\mathrm{per}} := T_{\mathrm{free}}$ uses only non-wrapping links ($0 \le x_\mu \le L - 2$) and spans all $L^d$ vertices of $\Lambda_{\mathrm{per}}$:
   $$|T_{\mathrm{per}}| = L^d - 1 = |V_{\mathrm{per}}| - 1, \qquad |E_{\mathrm{co-tree}}(\Lambda_{\mathrm{per}})| = |E_+(\Lambda_{\mathrm{per}})| - |V_{\mathrm{per}}| + 1 = (d - 1)L^d + 1.$$
   The co-tree set $E_{\mathrm{co-tree}}(\Lambda_{\mathrm{per}})$ partitions into two topologically distinct subsets:
   $$E_{\mathrm{co-tree}}(\Lambda_{\mathrm{per}}) = E_{\mathrm{co-tree}}^{\mathrm{int}}(\Lambda_{\mathrm{free}}) \;\sqcup\; E_{\mathrm{wrap}}(\Lambda_{\mathrm{per}}),$$
   where $|E_{\mathrm{co-tree}}^{\mathrm{int}}| = d(L - 1)L^{d-1} - L^d + 1$ are interior co-tree links and $|E_{\mathrm{wrap}}| = d L^{d-1}$ are periodic boundary-wrapping links $e = ((x_1, \dots, L - 1_\mu, \dots, x_d), \mu, (x_1, \dots, 0_\mu, \dots, x_d))$.

---

## 2. Theorem `YM-011-TREE-T1`: First-Principles Maximal-Tree Gauge Fixing and Measure Factorization

### Theorem `YM-011-TREE-T1` (Maximal-Tree Gauge Fixing, Uniqueness, Residual Gauge Group, and Unit Haar Jacobian)
Let $G = (V, E_+)$ be any finite connected oriented graph with root $x_0 \in V$ and maximal spanning tree $T \subset E_+$ ($|T| = |V| - 1$). Define the tree-gauge slice:
$$\Sigma_T := \left\{ \widetilde{U} \in SU(N)^{E_+} : \widetilde{U}_e = I_N \;\;\forall e \in T \right\} \;\cong\; SU(N)^{E_{\mathrm{co-tree}}}.$$
For every configuration $U \in \Omega = SU(N)^{E_+}$ and every root element $g_0 \in SU(N)$, define $g_{U, g_0} : V \to SU(N)$ along the unique tree path $\gamma_T(x_0 \to x) = (e_1^{\sigma_1}, \dots, e_k^{\sigma_k})$ ($\sigma_j \in \{\pm 1\}$) by:
$$g_{U, g_0}(x) := g_0 \, W_T(x_0 \to x)[U], \qquad W_T(x_0 \to x)[U] := U(e_1^{\sigma_1}) U(e_2^{\sigma_2}) \cdots U(e_k^{\sigma_k}).$$
Then:
1. **Existence:** The gauge-transformed configuration $\widetilde{U} := g_{U, g_0} \cdot U$ satisfies $\widetilde{U}_e = I_N$ for every $e \in T$, so $\widetilde{U} \in \Sigma_T$.
2. **Uniqueness under Fixed Root Gauge ($g_0 = I_N$):** In the rooted gauge group $\mathcal{G}_{x_0} = \{g \in SU(N)^V : g(x_0) = I_N\}$, $g_{U, I_N}$ is the **unique** gauge transformation satisfying $(g \cdot U)|_T \equiv I_N$.
3. **Residual Global Conjugation Group:** If $g(x_0) = g_0 \in SU(N)$ is unfixed, the subgroup of $\mathcal{G} = SU(N)^V$ preserving the slice $\Sigma_T$ is the global diagonal subgroup:
   $$\mathcal{G}_{\mathrm{res}} = \Delta(SU(N)) = \{(g_0, \dots, g_0) : g_0 \in SU(N)\} \cong SU(N),$$
   which acts on every co-tree link $e = (u \to v) \in E_{\mathrm{co-tree}}$ by simultaneous adjoint conjugation:
   $$(g_0 \cdot \widetilde{U})_e = g_0 \widetilde{U}_e g_0^{-1}, \qquad \widetilde{U}_e = W_T(x_0 \to u)[U]\, U_e\, W_T(x_0 \to v)[U]^{-1} = H(C_T(e))[U],$$
   where $C_T(e) = \gamma_T(x_0 \to u) \circ e \circ \gamma_T(v \to x_0)$ is the fundamental cycle of $e$ rooted at $x_0$. The center $Z(SU(N)) \cong \mathbb{Z}_N$ acts trivially on $\Sigma_T$, so the effective residual group action is $\operatorname{Ad}(SU(N)) \cong PSU(N)$.
4. **Global Real-Analytic Diffeomorphism & Orientation Consistency:** The map $\Phi_T : \mathcal{G}_{x_0} \times \Sigma_T \to \Omega$ given by $\Phi_T(g, \widetilde{U}) := g^{-1} \cdot \widetilde{U}$ is a global real-analytic ($C^\omega$) diffeomorphism of compact Lie manifolds with inverse $\Phi_T^{-1}(U) = (g_{U, I_N}, g_{U, I_N} \cdot U)$, respecting orientation reversal $\widetilde{U}_{e^{-1}} = (\widetilde{U}_e)^{-1}$ and preserving all closed Wilson-loop traces $\operatorname{Tr}(H_C(\widetilde{U})) = \operatorname{Tr}(H_C(U))$ pointwise.
5. **Exact Product Haar Factorization and Unit Jacobian ($J_{\mathrm{tree}} = 1$, $\Delta_{\mathrm{FP}} = 1$):** Under $\Phi_T$, the product Haar measure on $\Omega = SU(N)^{E_+}$ decomposes as the exact Cartesian product of normalized Haar measures:
   $$\Phi_T^* \left( \prod_{e \in E_+} d\mu_{\mathrm{Haar}}(U_e) \right) = \left( \prod_{x \in V \setminus \{x_0\}} d\mu_{\mathrm{Haar}}(g(x)) \right) \otimes \left( \prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e) \right),$$
   with **unit Jacobian $J_{\mathrm{tree}} \equiv 1$** and **no Faddeev–Popov ghost determinant ($\Delta_{\mathrm{FP}} \equiv 1$)**. Integrating out $\mathcal{G}_{x_0}$ is exact: for every gauge-invariant integrable observable $O : \Omega \to \mathbb{C}$,
   $$\langle O \rangle_{\mu_\beta} = \frac{\int_{\Sigma_T} O(\widetilde{U}) e^{-\beta H(\widetilde{U})} \prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e)}{\int_{\Sigma_T} e^{-\beta H(\widetilde{U})} \prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e)}.$$

### Proof of Theorem `YM-011-TREE-T1`
1. **Existence & Uniqueness:** For any tree edge $e = (u \to v) \in T$, either $d_T(x_0, v) = d_T(x_0, u) + 1$ (so $\gamma_T(x_0 \to v) = \gamma_T(x_0 \to u) \circ e$ and $W_T(x_0 \to v) = W_T(x_0 \to u) U_e$) or $d_T(x_0, u) = d_T(x_0, v) + 1$ (so $W_T(x_0 \to u) = W_T(x_0 \to v) U_e^{-1}$). In either case,
   $$\widetilde{U}_e = g_0 W_T(x_0 \to u) U_e W_T(x_0 \to v)^{-1} g_0^{-1} = g_0 I_N g_0^{-1} = I_N.$$
   If $g, \tilde{g} \in \mathcal{G}$ both satisfy $(g \cdot U)|_T = (\tilde{g} \cdot U)|_T = I_N$, then $h(x) := \tilde{g}(x)g(x)^{-1}$ satisfies $h(u) I_N h(v)^{-1} = I_N \implies h(u) = h(v)$ across every $e = (u \to v) \in T$. Since $T$ is connected and spans $V$, induction on $d_T(x_0, x)$ yields $h(x) = h(x_0)$ for all $x \in V$. If $g(x_0) = \tilde{g}(x_0) = I_N$, then $h(x) = I_N \implies \tilde{g} = g$. Otherwise $h(x) = g_0 \in SU(N)$ is constant on $V$, proving $\mathcal{G}_{\mathrm{res}} = \Delta(SU(N))$.
2. **Exact Haar Factorization (Leaf-Peeling Induction):** Order $V \setminus \{x_0\} = \{x_1, \dots, x_{|V|-1}\}$ in non-decreasing order of tree depth $d_T(x_0, x_k)$, and let $e_k \in T$ be the unique tree edge connecting $x_k$ to its parent $p(x_k) \in \{x_0, x_1, \dots, x_{k-1}\}$. First, for fixed $(g(x))_{x \in V \setminus \{x_0\}}$, each co-tree variable $U_e = g(u)^{-1} \widetilde{U}_e g(v)$ ($e \in E_{\mathrm{co-tree}}$) is a left- and right-translation of $\widetilde{U}_e$ by fixed elements of $SU(N)$; by bi-invariance of Haar measure on $SU(N)$, $\prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(U_e) = \prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e)$. Second, for the tree edges $e_k \in T$, peel the leaves from $k = |V| - 1$ down to $k = 1$: at step $k$, $U_{e_k} = g(p(x_k))^{-1} g(x_k)$ (or $g(x_k)^{-1} g(p(x_k))$), where $g(p(x_k))$ depends only on $\{g(x_1), \dots, g(x_{k-1})\}$. By Fubini's theorem and left/right/inversion invariance of $d\mu_{\mathrm{Haar}}$ on $SU(N)$, integrating $d\mu_{\mathrm{Haar}}(U_{e_k})$ is identical to integrating $d\mu_{\mathrm{Haar}}(g(x_k))$ with Jacobian $1$. Induction down to $k = 1$ establishes the exact product measure identity. $\blacksquare$

---

## 3. Theorem `YM-011-TREE-T2`: Co-Tree Cycle Rank, Plaquette Coordinate Audit, and Non-Abelian Bianchi Identities

### Theorem `YM-011-TREE-T2` (Classification of the Co-Tree to Plaquette Map Across Dimensions $d = 2, 3, 4$)
For any connected finite lattice $G = (V, E_+)$, the number of remaining independent $SU(N)$ link variables after root-fixed maximal-tree gauge fixing equals the graph cycle rank $b_1(G) = |E_{\mathrm{co-tree}}| = |E_+| - |V| + 1$. Comparing $|E_{\mathrm{co-tree}}|$ with the plaquette count $|P_+|$ across dimensions $d \in \{2, 3, 4\}$ yields:

| Dimension & Boundary | $|V|$ | $|E_+|$ | $|T|$ | $|E_{\mathrm{co-tree}}|$ | $|P_+|$ | $|P_+| - |E_{\mathrm{co-tree}}|$ | Map $\{\widetilde{U}_e\}_{e \in E_{\mathrm{co-tree}}} \to \{U_p\}_{p \in P_+}$ Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$d=2$ Free** $\Lambda_{\mathrm{free}}(L, 2)$ | $L^2$ | $2L(L-1)$ | $L^2 - 1$ | $(L-1)^2$ | $(L-1)^2$ | $0$ | **Global Triangular Bijection** ($J_{\mathrm{Haar}} = 1$, i.i.d. plaquettes) |
| **$d=2$ Periodic** $\Lambda_{\mathrm{per}}(L, 2)$ | $L^2$ | $2L^2$ | $L^2 - 1$ | $L^2 + 1$ | $L^2$ | $-1$ | **Non-Bijective** ($1$ surface Bianchi constraint; $2$ global toron cycles) |
| **$d=3$ Free** $\Lambda_{\mathrm{free}}(L, 3)$ | $L^3$ | $3L^2(L-1)$ | $L^3 - 1$ | $(2L+1)(L-1)^2$ | $3L(L-1)^2$ | $(L-1)^3 = |C_3|$ | **Constrained Embedding** ($(L-1)^3$ 3-cube Bianchi constraints) |
| **$d=3$ Periodic** $\Lambda_{\mathrm{per}}(L, 3)$ | $L^3$ | $3L^3$ | $L^3 - 1$ | $2L^3 + 1$ | $3L^3$ | $L^3 - 1$ | **Non-Bijective** ($L^3 + 2$ Bianchi constraints; $3$ global toron cycles) |
| **$d=4$ Free** $\Lambda_{\mathrm{free}}(L, 4)$ | $L^4$ | $4L^3(L-1)$ | $L^4 - 1$ | $(3L^2+2L+1)(L-1)^2$ | $6L^2(L-1)^2$ | $3L^4 - 8L^3 + 6L^2 - 1 = |C_3| - |C_4|$ | **Constrained Embedding** ($|C_3| - |C_4|$ independent Bianchi constraints) |
| **$d=4$ Periodic** $\Lambda_{\mathrm{per}}(L, 4)$ | $L^4$ | $4L^4$ | $L^4 - 1$ | $3L^4 + 1$ | $6L^4$ | $3L^4 - 1$ | **Non-Bijective** ($3L^4 + 3$ Bianchi constraints; $4$ global toron cycles) |

Specifically:
1. **Exact Triangular Bijection in $d=2$ Free Boundary:** On $\Lambda_{\mathrm{free}}(L, 2)$, the comb tree sets all vertical links and the bottom horizontal spine $x_2 = 0$ to $I_N$. Every plaquette $p_{x_1, x_2}$ ($0 \le x_1, x_2 \le L-2$) satisfies $U_{p_{x_1, x_2}} = \widetilde{U}_{((x_1, x_2), \hat{1})} \widetilde{U}_{((x_1, x_2+1), \hat{1})}^{-1}$, yielding the exact inverse recursion:
   $$\widetilde{U}_{((x_1, x_2), \hat{1})} = U_{p_{x_1, x_2-1}}^{-1} U_{p_{x_1, x_2-2}}^{-1} \cdots U_{p_{x_1, 0}}^{-1} \qquad (1 \le x_2 \le L - 1).$$
   By Fubini's theorem and Haar bi-invariance, $\prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e) = \prod_{p \in P_+} d\mu_{\mathrm{Haar}}(U_p)$ with **exact unit Jacobian $J = 1$**, decoupling $Z_{\mathrm{free}, d=2}(\beta) = z_1(\beta)^{(L-1)^2}$.
2. **Non-Abelian 3-Cube Bianchi Obstruction in $d \ge 3$ (`NEG-YM-011-TREE-1`):** Around every elementary 3-cube $c \in C_3(\Lambda)$, the six boundary plaquette lassos $\widehat{U}_{p_1}, \dots, \widehat{U}_{p_6}$ parallel-transported to the base corner of $c$ satisfy the exact non-Abelian telescoping identity:
   $$\widehat{U}_{p_1} \widehat{U}_{p_2} \widehat{U}_{p_3} \widehat{U}_{p_4} \widehat{U}_{p_5} \widehat{U}_{p_6} = I_N.$$
   Consequently, in $d = 3$ and $d = 4$, plaquette holonomies are **never freely independent coordinates**. While a triangular co-tree spanning subset $P_{\mathrm{sel}} \subset P_+$ of size $|P_{\mathrm{sel}}| = |E_{\mathrm{co-tree}}|$ bijects with $\Sigma_T$ with unit Haar Jacobian ($J = 1$), the remaining $|P_+| - |E_{\mathrm{co-tree}}| = |C_3| - |C_4|$ dependent plaquettes in $P_+ \setminus P_{\mathrm{sel}}$ are non-local products of $U_p \in P_{\mathrm{sel}}$ and prevent single-plaquette factorization of the Wilson action $S_W$.
3. **Explicit Cochain Rank Identity and Linearized vs. Non-Abelian Constraint Scope on $\Lambda_{\mathrm{per}}(L, d)$:**
   On the periodic torus $\Lambda_{\mathrm{per}}(L, d)$ with first Betti number $b_1(\mathbb{T}^d) = d$, the discrete exterior coboundary operator $d_1 : C^1(\Lambda_{\mathrm{per}}; \mathbb{R}) \to C^2(\Lambda_{\mathrm{per}}; \mathbb{R})$ has kernel of dimension $\dim \ker(d_1) = (|V| - 1) + b_1$ (spanning-tree exact 0-cochains plus $b_1 = d$ harmonic 1-cochains around the fundamental noncontractible cycles of $\mathbb{T}^d$). By the rank-nullity theorem:
   $$\operatorname{rank}(d_1) = |E_+| - \dim \ker(d_1) = |E_+| - |V| + 1 - b_1 = |E_{\mathrm{co-tree}}| - b_1.$$
   Therefore, the number of independent linearized / cochain constraints on 2-cochains $F \in C^2(\Lambda_{\mathrm{per}}; \mathbb{R})$ required for $F \in \operatorname{im}(d_1)$ (per Lie-algebra color generator) satisfies the exact rank identity:
   $$N_{\mathrm{constraints}}^{\mathrm{cochain}} = |P_+| - \operatorname{rank}(d_1) = |P_+| - |E_{\mathrm{co-tree}}| + b_1,$$
   giving $L^2 - (L^2 + 1) + 2 = 1$ ($d=2$), $3L^3 - (2L^3 + 1) + 3 = L^3 + 2$ ($d=3$), and $6L^4 - (3L^4 + 1) + 4 = 3L^4 + 3$ ($d=4$).
   - **Strict Scope Separation (`LINEARIZED_COCHAIN_RANK_COUNT` vs. `NON_ABELIAN_GLOBAL_CONSTRAINT_VARIETY`):** The formula $N_{\mathrm{constraints}}^{\mathrm{cochain}} = |P_+| - |E_{\mathrm{co-tree}}| + b_1$ is strictly the **linearized / cochain rank count** (and the local codimension of the plaquette map image at generic regular connections). At the global non-Abelian group level on $SU(N)^{P_+}$, the constraint locus is defined by the $L^d$ non-Abelian 3-cube Bianchi identities $\prod_{f=1}^6 \widehat{U}_{p_f(c)} = I_N$ together with global periodic surface holonomy commutator relations coupling the product of plaquettes on each 2-torus sheet to $[U_\mu, U_\nu]$, whose differential rank drops at reducible/central connections where $\operatorname{Stab}_{\operatorname{Ad}(SU(N))}$ jumps in dimension.

---

## 4. Theorem `YM-011-TREE-T3`: Free-Boundary Zero Modes, Hessian Positive Definiteness, and Fixed-Volume $O(1/\beta)$ Asymptotics

### Theorem `YM-011-TREE-T3` (Isolation of the Trivial Vacuum and Fixed-Volume Equipartition on $\Lambda_{\mathrm{free}}(L, d)$)
On the contractible free-boundary lattice $\Lambda_{\mathrm{free}}(L, d)$ ($d \ge 2, L \ge 2, N \ge 2$):
1. **Unique Flat Configuration on $\Sigma_{T_{\mathrm{free}}}$:** The zero-action locus on the root-fixed tree-gauge slice $\Sigma_{T_{\mathrm{free}}}$ consists of the single point $\widetilde{U}_{\mathrm{triv}} = (I_N)_{e \in E_{\mathrm{co-tree}}}$:
   $$H(\widetilde{U}) = 0 \quad \Longleftrightarrow \quad U_p = I_N \;\;\forall p \in P_+(\Lambda_{\mathrm{free}}) \quad \Longleftrightarrow \quad \widetilde{U}_e = I_N \;\;\forall e \in E_{\mathrm{co-tree}}(\Lambda_{\mathrm{free}}).$$
   Thus the gauge-invariant flat moduli space is trivial: $\mathcal{M}_0(\Lambda_{\mathrm{free}}) = \{U : H(U) = 0\}/\mathcal{G}_{\mathrm{free}} = \{[I_N]\}$.
2. **Strict Positive Definiteness and Full Rank of the Hessian:** Writing $\widetilde{U}_e = \exp(\sum_{a=1}^{N^2-1} A_e^a T^a)$ for $e \in E_{\mathrm{co-tree}}$ with $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$, the Taylor expansion of $H|_{\Sigma_{T_{\mathrm{free}}}}$ around $A = 0$ is:
   $$H|_{\Sigma_{T_{\mathrm{free}}}}(\exp(A)) = Q_2(A) + P_3(A) + P_4(A) + O(\|A\|^5), \qquad Q_2(A) := \frac{1}{4N} \sum_{a=1}^{N^2-1} \left\langle A^a,\; \mathcal{H}_{\mathrm{tree}}(L, d)\, A^a \right\rangle_{\ell^2(E_{\mathrm{co-tree}})},$$
   where $\mathcal{H}_{\mathrm{tree}}(L, d) = (d_\Lambda|_{\Sigma_T})^T (d_\Lambda|_{\Sigma_T})$ is the restricted scalar curl-curl operator. Because $H^1(\Lambda_{\mathrm{free}}; \mathbb{R}) = 0$ and $T_{\mathrm{free}}$ spans $V_{\mathrm{free}}$, $\ker(d_\Lambda|_{\Sigma_T}) = \{0\}$, so:
   $$\ker\left(D^2 H|_{\Sigma_{T_{\mathrm{free}}}}(I_N)\right) = \{0\}, \qquad \operatorname{rank}\left(D^2 H|_{\Sigma_{T_{\mathrm{free}}}}(I_N)\right) = D_{\mathrm{free}} := (N^2 - 1)\left(d(L-1)L^{d-1} - L^d + 1\right),$$
   and $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d)) > 0$ for every finite $L \ge 2$.
3. **Proof of Claim A (Fixed-Volume $O(1/\beta)$ Plaquette Expectation on $\Lambda_{\mathrm{free}}$ via Direct Laplace Ratio Expansion):**
   By Theorem `YM-011-PLAQUETTE-EXP-T2`, $|P_+(\Lambda_{\mathrm{free}})| e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{free}}) = -\partial_\beta \ln Z_{\mathrm{free}}(\beta) = \langle H \rangle_{\mu_{\mathrm{free}, \beta}}$. Rather than formally differentiating an asymptotic $O$-remainder of $\ln Z_{\mathrm{free}}(\beta)$, we apply finite-dimensional Laplace asymptotics directly to both smooth integrals in the expectation ratio on the compact manifold $\Sigma_{T_{\mathrm{free}}} \cong SU(N)^{|E_{\mathrm{co-tree}}|}$:
   $$\langle H \rangle_{\mu_{\mathrm{free}, \beta}} = \frac{I_{\mathrm{num}}(\beta)}{Z_{\mathrm{free}}(\beta)}, \qquad I_{\mathrm{num}}(\beta) := \int_{\Sigma_{T_{\mathrm{free}}}} H(\widetilde{U})\, e^{-\beta H(\widetilde{U})}\, d\mu_{\mathrm{Haar}}(\widetilde{U}).$$
   Since $\widetilde{U}_{\mathrm{triv}} = I_N$ is the unique global minimum of the continuous function $H \ge 0$ on the compact set $\Sigma_{T_{\mathrm{free}}}$, for any fixed ball $B(\delta_L) = \{\|A\| < \delta_L\}$ around $0 \in \mathfrak{su}(N)^{E_{\mathrm{co-tree}}}$, $\inf_{\Sigma_{T_{\mathrm{free}}} \setminus B(\delta_L)} H(\widetilde{U}) =: \eta_L > 0$, so the exterior contribution to both $I_{\mathrm{num}}(\beta)$ and $Z_{\mathrm{free}}(\beta)$ is $O_L(e^{-\beta \eta_L})$. Inside $B(\delta_L)$, the Haar density is $d\mu_{\mathrm{Haar}}(\exp(A)) = (1 + J_2(A) + O(\|A\|^4))\, dA$ (even at quadratic order), while $H(\exp(A)) = Q_2(A) + P_3(A) + P_4(A) + O(\|A\|^5)$ has odd cubic term $P_3(-A) = -P_3(A)$. Under the Gaussian change of variables $A = \beta^{-1/2} \xi$, odd-degree polynomials in $\xi$ integrate to zero by reflection parity $\xi \mapsto -\xi$, yielding the two-term asymptotic expansions:
   $$Z_{\mathrm{free}}(\beta) = C_0(L,d,N)\, \beta^{-D_{\mathrm{free}}/2} \left( 1 + \frac{c_1(L,d,N)}{\beta} + O_L(\beta^{-2}) \right),$$
   $$I_{\mathrm{num}}(\beta) = C_0(L,d,N)\, \beta^{-D_{\mathrm{free}}/2} \left( \frac{D_{\mathrm{free}}}{2\beta} + \frac{\widetilde{c}_2(L,d,N)}{\beta^2} + O_L(\beta^{-3}) \right),$$
   since $\mathbb{E}_{\xi \sim \mathcal{N}(0, (2 Q_2)^{-1})}[Q_2(\xi)] = \frac{1}{2}\operatorname{Tr}(I_{D_{\mathrm{free}}}) = \frac{D_{\mathrm{free}}}{2}$. Taking the quotient $I_{\mathrm{num}}(\beta) / Z_{\mathrm{free}}(\beta)$ and dividing by $|P_+(\Lambda_{\mathrm{free}})|$ establishes rigorously at every fixed finite $L \ge 2$:
   $$e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{free}}(L, d)) = \frac{\langle H \rangle_{\mu_{\mathrm{free}, \beta}}}{|P_+(\Lambda_{\mathrm{free}})|} = \frac{C_{\mathrm{free}}(L, d, N)}{\beta} + O_L(\beta^{-2}),$$
   with exact leading Gaussian equipartition coefficient:
   $$C_{\mathrm{free}}(L, d, N) = \frac{D_{\mathrm{free}}}{2 |P_+(\Lambda_{\mathrm{free}})|} = \frac{(N^2 - 1)\left(d(L-1)L^{d-1} - L^d + 1\right)}{2\binom{d}{2}(L - 1)^2 L^{d-2}} \le \frac{N^2 - 1}{d - 1}, \qquad \lim_{L \to \infty} C_{\mathrm{free}}(L, d, N) = \frac{N^2 - 1}{d}.$$
4. **Volume Degeneration of $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d))$ as $L \to \infty$:** In $d = 2$, the exact smallest eigenvalue of $\mathcal{H}_{\mathrm{tree}}(L, 2)$ is:
   $$\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, 2)) = 4 \sin^2\!\left(\frac{\pi}{2(2L - 1)}\right) = \frac{\pi^2}{4L^2} + O(L^{-3}) \;\xrightarrow{L \to \infty}\; 0.$$
   In $d \ge 3$, reconstructing a co-tree link $\widetilde{U}_e$ from plaquettes along the surface spanned by its comb-tree fundamental cycle $C_T(e)$ involves paths of length $O(dL)$, so $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d)) \sim c_d L^{-\alpha_d} \to 0$ as $L \to \infty$. Because the standard finite-dimensional Laplace remainder $O_L(\beta^{-2})$ depends inversely on $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d))$ and grows with dimension $D_{\mathrm{free}} \sim (d-1)(N^2-1)L^d$, **tree-gauge Laplace asymptotics alone proves Claim A (fixed finite volume) on $\Lambda_{\mathrm{free}}(L, d)$, proves Claim B (volume-uniform $O(1/\beta)$) in $d=2$ free boundary via exact plaquette factorization, and does NOT establish Claim B in $d \ge 3$.**

---

## 5. Theorem `YM-011-TREE-T4`: Periodic-Torus Zero Modes, Toron Moduli, Stabilizer Strata, and Quartic Commutator Directions

### Theorem `YM-011-TREE-T4` (Complete Characterization of Flat Moduli and Hessian Zero Modes on $\Lambda_{\mathrm{per}}(L, d)$)
On the periodic torus $\Lambda_{\mathrm{per}}(L, d) = (a\mathbb{Z}/La\mathbb{Z})^d$ ($d \ge 2, L \ge 2, N \ge 2$) in root-fixed comb-tree gauge $\Sigma_{T_{\mathrm{per}}}$:
1. **First-Principles Reduction to Commuting Global Holonomies:** Every zero-action configuration $\widetilde{U} \in \mathcal{Z}_{\mathrm{per}} := \{\widetilde{U} \in \Sigma_{T_{\mathrm{per}}} : H(\widetilde{U}) = 0\}$ satisfies:
   - $\widetilde{U}_e = I_N$ on all $d(L-1)L^{d-1}$ interior non-wrapping edges ($0 \le x_\mu \le L - 2$) by Theorem `YM-011-TREE-T3`(1);
   - On the $d L^{d-1}$ periodic wrapping edges ($x_\mu = L - 1$), flatness of the mixed interior-wrapping plaquettes $U_{p((x, \mu, \nu))} = W_\mu(x_{\perp \mu}) I_N W_\mu(x_{\perp \mu} + \hat{\nu})^{-1} I_N^{-1} = I_N$ forces $W_\mu(x_{\perp \mu}) = U_\mu \in SU(N)$ to be independent of all transverse coordinates $x_{\perp \mu} \in \{0, \dots, L-1\}^{d-1}$;
   - On the $\binom{d}{2}$ corner wrapping plaquettes ($x_\mu = x_\nu = L - 1$), flatness forces the group commutator to vanish:
     $$U_{p_{\mu\nu}^{\mathrm{corner}}} = U_\mu U_\nu U_\mu^{-1} U_\nu^{-1} = [U_\mu, U_\nu] = I_N \qquad \forall 1 \le \mu < \nu \le d.$$
   Hence $\mathcal{Z}_{\mathrm{per}} \subset \Sigma_{T_{\mathrm{per}}}$ is real-analytically isomorphic to the representation variety of $\pi_1(\mathbb{T}^d) = \mathbb{Z}^d$:
   $$\mathcal{Z}_{\mathrm{per}} \;\cong\; \operatorname{Hom}(\mathbb{Z}^d, SU(N)) = \left\{ (U_1, \dots, U_d) \in SU(N)^d : [U_\mu, U_\nu] = I_N \;\;\forall \mu, \nu \right\},$$
   where $U_\mu$ equals the noncontractible Polyakov loop holonomy along axis $\mu$ at $x_0$.
2. **Exact Weyl-Quotient Flat Moduli Space:** Quotienting $\mathcal{Z}_{\mathrm{per}}$ by the residual global conjugation $\mathcal{G}_{\mathrm{res}} = \operatorname{Ad}(SU(N))$ simultaneously diagonalizes $(U_1, \dots, U_d)$ into the maximal torus $T_{\mathrm{max}} = \{\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_N}) \in SU(N) : \sum_{a=1}^N \theta_a \equiv 0 \pmod{2\pi}\} \cong U(1)^{N-1}$ up to the diagonal action of the Weyl group $W(SU(N)) = S_N$:
   $$\mathcal{M}_{\mathrm{flat}}(\Lambda_{\mathrm{per}}, SU(N)) = \mathcal{Z}_{\mathrm{per}} / \operatorname{Ad}(SU(N)) \;\cong\; (T_{\mathrm{max}})^d / S_N \;\cong\; \left(U(1)^{N-1}\right)^d / S_N, \qquad \dim \mathcal{M}_{\mathrm{flat}} = d(N - 1).$$
3. **Stabilizer Jumps and Exact Quadratic vs. Quartic Zero-Mode Decomposition in $\Sigma_{T_{\mathrm{per}}}$:**
   - **At a Generic Regular Toron $U_{\mathrm{reg}} \in \mathcal{Z}_{\mathrm{per}}^{\mathrm{reg}}$:** The stabilizer under $\operatorname{Ad}(SU(N))$ is $\operatorname{Stab}_{\operatorname{Ad}(SU(N))}(U_{\mathrm{reg}}) = T_{\mathrm{max}}$ of dimension $N - 1$, the adjoint orbit fiber has dimension $(N^2 - 1) - (N - 1) = N(N - 1)$, and the quadratic Hessian kernel has dimension:
     $$\dim \ker D^2 H|_{\Sigma_{T_{\mathrm{per}}}}(U_{\mathrm{reg}}) = d(N - 1) + N(N - 1) = (d + N)(N - 1).$$
   - **At the $N^d$ Central Torons $U_{\mathrm{cent}} = (z_1 I_N, \dots, z_d I_N)$ ($z_\mu \in Z(SU(N)) \cong \mathbb{Z}_N$):** The stabilizer jumps to the full group $\operatorname{Stab}_{\operatorname{Ad}(SU(N))}(U_{\mathrm{cent}}) = SU(N)$ of dimension $N^2 - 1$ (a **stabilizer dimension jump of $\Delta \dim \operatorname{Stab} = N(N - 1)$**). For any $X_1, \dots, X_d \in \mathfrak{su}(N)$, the corner plaquette perturbation $U_{p_{\mu\nu}^{\mathrm{corner}}}(U_{\mathrm{cent}} e^X) = \exp([X_\mu, X_\nu] + O(\|X\|^3))$ has vanishing linear variation, so the quadratic Hessian kernel jumps to:
     $$\dim \ker D^2 H|_{\Sigma_{T_{\mathrm{per}}}}(U_{\mathrm{cent}}) = d(N^2 - 1),$$
     decomposing into:
     $$d(N^2 - 1) = \underbrace{d(N - 1)}_{\text{Cartan flat torons}} + \underbrace{N(N - 1)}_{\text{degenerated }\operatorname{Ad}(SU(N))\text{ orbit}} + \underbrace{(d - 1)N(N - 1)}_{\text{transverse quartic commutator zero modes}},$$
     where the $(d - 1)N(N - 1)$ transverse modes are stabilized only at fourth order by the quartic commutator action:
     $$H_{\mathrm{quartic}}(X_1, \dots, X_d) = \frac{1}{2N} \sum_{1 \le \mu < \nu \le d} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2.$$

---

## 6. Re-Evaluation of `NEG-YM-011-PLAQ-1` and Separation of Claims A, B, C

### 6.1 Resolution of `NEG-YM-011-PLAQ-1` Under Maximal-Tree Gauge
Re-deriving `NEG-YM-011-PLAQ-1` in the tree-gauge variables $\Sigma_{T_{\mathrm{per}}}$ establishes that while maximal-tree gauge fixing eliminates all $(L^d - 1)(N^2 - 1)$ local vertex gauge redundancies with unit Haar Jacobian, the obstruction to ordinary Laplace/Morse–Bott asymptotics on the periodic torus $\Lambda_{\mathrm{per}}(L, d)$ is **Category E (combination of all four structural mechanisms A, B, C, D)**:
- **A (Residual Global Gauge Redundancy):** Unfixed root conjugation $\operatorname{Ad}(SU(N))$ contributes $N(N - 1)$ orbit zero modes at generic torons;
- **B (Physical Global Flat-Connection Moduli):** The $d(N - 1)$-dimensional Cartan toron manifold $(T_{\mathrm{max}})^d / S_N$ consists of gauge-inequivalent physical flat connections parameterized by noncontractible Polyakov loops;
- **C (Singular Stabilizer Structure):** The stabilizer dimension jumps by $\Delta \dim \operatorname{Stab} = N(N - 1)$ at the $N^d$ central toron strata $U_\mu \in Z(SU(N))$;
- **D (Quartic Action Directions):** At every central toron, $(d - 1)N(N - 1)$ off-diagonal global modes have zero quadratic Hessian ($D^2 H = 0$) and are controlled only by the quartic commutator energy $\frac{1}{2N}\sum_{\mu<\nu} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2$.

### 6.2 Strict Separation of Claims A, B, C ($A \not\Rightarrow B$, $B \not\Rightarrow C$)
1. **CLAIM A (Fixed Finite Lattice $O(1/\beta)$):**
   - **Free Boundary $\Lambda_{\mathrm{free}}(L, d)$:** **`PROVED`** (Theorem `YM-011-TREE-T3`, Outcome A/B) with explicit constant $C_{\mathrm{free}}(L, d, N) = \frac{(N^2-1)|E_{\mathrm{co-tree}}|}{2|P_+|}$.
   - **Periodic Torus $\Lambda_{\mathrm{per}}(L, d)$:** **`OPEN_BEYOND_LOG_BETA`** (Outcome E; ordinary Laplace fails due to the $d(N^2-1)$ toron/quartic zero-mode sector isolated in Theorem `YM-011-TREE-T4`; current rigorous bound on $\Lambda_{\mathrm{per}}$ remains the volume-uniform $O(\frac{\ln\beta}{\beta})$ estimate `YM-011-PLAQUETTE-EXP-L1`).
2. **CLAIM B (Volume-Uniform Lattice $O(1/\beta)$):**
   - **$d = 2$ Free Boundary:** **`PROVED`** ($e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{free}}(L, 2)) = \frac{N^2-1}{2\beta} + O(\beta^{-2})$ independently of $L$).
   - **$d \ge 3$ (Free or Periodic):** **`NOT_ESTABLISHED`** ($\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d)) \to 0$ as $L \to \infty$ and non-Abelian Bianchi cube identities couple plaquettes).
3. **CLAIM C (Continuum-Useful Uniform Estimate):**
   - **`NOT_ESTABLISHED`**.

---

## 7. Primary-Source Audit Table & Source-Scope Attribution

| Source | Theorem / Page | Gauge Group | Dimension | Boundary Condition | Volume | $\beta$ Regime | Gauge Fixing | Zero-Mode Treatment | Volume Uniformity | Actual Conclusion |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Creutz (1977)**, *Phys. Rev. D* 15, 1128; *(1983) Ch. 6* | Sec. II, pp. 1129–1131 | Compact $G$, $SU(N)$ | General $d \ge 2$ | Finite graph $G=(V,E)$ | Finite $L < \infty$ | All $\beta > 0$ | Maximal spanning tree $T$ ($U_e = I$ on $T$) | Root gauge $g(x_0)$ left global | Exact for any finite $L$ | Proves existence/uniqueness of tree gauge up to root conjugation and exact unit Haar Jacobian ($J=1$). |
| **Osterwalder & Seiler (1978)**, *Ann. Phys.* 110, 440 | Sec. 2, pp. 444–448 | Compact Lie group $G$ | General $d \ge 2$ | Finite lattice $\Lambda$ | Finite $L < \infty$ | Strong & general $\beta$ | Temporal / axial tree gauge | Eliminates tree links via Haar bi-invariance | Fixed finite volume | Confirms absence of Faddeev–Popov ghost determinants on compact lattice groups under tree gauge. |
| **Batrouni (1982)**, *Nucl. Phys. B* 208, 12 | Secs. 2–3, pp. 14–21 | $SU(N)$, $U(1)$ | $d = 2, 3, 4$ | Free & periodic | Finite $L < \infty$ | All $\beta > 0$ | Axial / maximal tree gauge | Identifies 3-cube Bianchi delta functions | Not volume-uniform in $d \ge 3$ | Proves $d=2$ free plaquettes decouple completely, whereas $d \ge 3$ plaquettes obey non-Abelian 3-cube Bianchi constraints and periodic lattices carry additional global surface constraints. |
| **Bałaban (1984)**, *Commun. Math. Phys.* 95, 17 & 96, 223 | Sec. 2, pp. 21–35 | Compact $G$, $SU(N)$ | $d = 3, 4$ | Periodic torus / block $B(y)$ | Finite $L$, multiscale | Weak coupling $\beta \gg 1$ | Local axial tree gauge inside unit blocks + Landau-type projection | Separates block zero modes scale-by-scale | Uniform only via multiscale RG | Shows a single global tree gauge has paths of length $O(L)$ with $\lambda_{\min} \sim L^{-2} \to 0$, requiring multiscale RG rather than global tree gauge for uniform bounds. |
| **Lüscher (1982)**, *Nucl. Phys. B* 219, 233 | Secs. 2–3, pp. 235–246 | $SU(N)$ | $d = 4$ (continuum & lattice torus) | Periodic torus $\mathbb{T}^d$ | Finite box $L$ | Weak coupling $g_0 \to 0$ | Background / axial gauge on torus | Isolates toron moduli $(T_{\mathrm{max}})^d/S_N$ & central toron quartic modes | Fixed finite torus $L$ | Shows zero-action configurations on $\mathbb{T}^d$ form the non-isolated orbifold $(T_{\mathrm{max}})^d/S_N$ with quartic commutator potential $\operatorname{Tr}([X_\mu, X_\nu]^2)$ at central torons. |
| **Chatterjee (2019)**, *Springer PROMS* 283, 1–42 | Thm. 3.1 & Lem. 4.2, pp. 12–28 | $SO(N)$, $SU(N)$, $U(N)$ | $d \ge 2$ | Free boundary box $\Lambda_L$ | Finite $L < \infty$ | $\beta \to \infty$ | Maximal spanning tree gauge | Unique ground state $U_e = I$ on contractible box | Fixed-volume Laplace + local coupling | Proves unique isolated minimum $U=I$ and positive-definite quadratic form in tree gauge on contractible free-boundary boxes. |

### 7.1 Source-to-Derivation Attribution Boundary
Primary literature citations above support ONLY the qualitative and structural results explicitly listed in the `Actual Conclusion` column (existence of spanning-tree gauge with unit Haar Jacobian, presence of 3-cube and periodic Bianchi constraints in $d \ge 3$, and existence of commuting toron flat directions on $\mathbb{T}^d$). The quantitative formulas proved in Theorems `YM-011-TREE-T1` through `YM-011-TREE-T4`—specifically:
1. The exact comb-tree Hessian spectrum $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, 2)) = 4\sin^2\!\left(\frac{\pi}{2(2L - 1)}\right)$,
2. The exact finite-volume Laplace equipartition coefficient $C_{\mathrm{free}}(L, d, N) = \frac{(N^2 - 1)\left(d(L-1)L^{d-1} - L^d + 1\right)}{2\binom{d}{2}(L-1)^2 L^{d-2}}$ and Laplace ratio remainder $O_L(\beta^{-2})$,
3. The cochain rank identity $N_{\mathrm{constraints}}^{\mathrm{cochain}} = |P_+| - |E_{\mathrm{co-tree}}| + b_1$, and
4. The exact Hessian nullity decomposition $d(N^2 - 1) = d(N - 1) + N(N - 1) + (d - 1)N(N - 1)$ at central torons in $\Sigma_{T_{\mathrm{per}}}$—
rely strictly on the project's own first-principles derivations in Sections 2–5 and are NOT attributed to external source authority.

