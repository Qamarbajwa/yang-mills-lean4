# INDEPENDENT ADVERSARIAL MATHEMATICAL & GOVERNANCE AUDIT REPORT — `YM-011-TREE-GAUGE`

- **Task ID:** `YM-011-TREE-GAUGE` (Maximal-Tree Gauge Fixing and Zero-Mode Separation)
- **Candidate Commit SHA:** `099c883a67f07bb3576abe77cd19fce8978df651`
- **Closed-World Scientific Tree Hash (`SCIENTIFIC_TREE_HASH`):** `d7eca47e7fc9b469ac88992a63e3c2362839f1bb1a577a30d3e0932516988f55`
- **Reviewer Role:** Fresh Blind Independent Adversarial Verifier Subagent (`e5f0407a-dab8-42b8-9446-5945533293cf`)
- **Audit Scope:** First-principles mathematical verification and governance inspection of `literature/YM-011-TREE-GAUGE-ANALYSIS.md`, `src/ymmg/tree_gauge.py`, `tests/test_ym_011_tree_gauge.py`, `NEGATIVE_EVIDENCE_REGISTER.md`, `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml`, `src/ymmg/ros.py`, and `governance/PROJECT_STATE.yaml`.
- **Repository Test Execution:** `8/8` task unit/regression tests in `tests/test_ym_011_tree_gauge.py` PASSED; `344/344` full repository tests PASSED (`python -B -m pytest -p no:cacheprovider`).

---

## 1. Item-by-Item First-Principles Adversarial Audit (Section 15 Mandate)

### Item 1: Tree-Gauge Existence & Uniqueness (`YM-011-TREE-T1`) — **PASS**
- **Mathematical Audit:** On any connected finite oriented graph $G = (V, E_+)$ with root $x_0 = (0,\dots,0)$ and canonical lexicographical comb spanning tree $T \subset E_+$ ($e = (x, \mu, x + \hat{\mu}) \in T \iff 0 \le x_\mu \le L-2$ and $x_{\mu+1} = \dots = x_d = 0$), every vertex $x \in V$ has a unique path $\gamma_T(x_0 \to x)$ in $T$ of Manhattan length $\sum_{\mu=1}^d x_\mu$. Defining $g_{U, g_0}(x) := g_0 W_T(x_0 \to x)[U]$, every tree edge $e = (u \to v) \in T$ satisfies $W_T(x_0 \to v)[U] = W_T(x_0 \to u)[U] U_e$, which yields:
  $$(g_{U, g_0} \cdot U)_e = g_0 W_T(x_0 \to u) U_e \left(g_0 W_T(x_0 \to u) U_e\right)^{-1} = I_N \qquad \forall e \in T.$$
  If $g, \tilde{g} \in \mathcal{G}_{x_0} = \{g \in SU(N)^V : g(x_0) = I_N\}$ both fix $U|_T \equiv I_N$, then $h(x) := \tilde{g}(x)g(x)^{-1}$ satisfies $h(u) I_N h(v)^{-1} = I_N \implies h(u) = h(v)$ along every tree edge $e = (u \to v) \in T$. Connectedness of $T$ and $h(x_0) = I_N$ force $h(x) = I_N \;\forall x \in V$, proving uniqueness of $g_{U, I_N}$ in $\mathcal{G}_{x_0}$.
- **Implementation & Test Verification:** Verified in `compute_tree_gauge_transform` (`src/ymmg/tree_gauge.py:237-273`) and `test_02_maximal_tree_gauge_existence_uniqueness_and_wilson_invariance` (`tests/test_ym_011_tree_gauge.py:61-105`) to machine precision ($10^{-14}$).

### Item 2: Residual Gauge Group — **PASS**
- **Mathematical Audit:** When the root gauge $g(x_0) = g_0 \in SU(N)$ is not fixed, preserving $\widetilde{U}_e = I_N$ on $e = (u \to v) \in T$ requires $h(u) = h(v)$ across all $e \in T$, so the slice stabilizer in $\mathcal{G} = SU(N)^V$ is the global diagonal subgroup $\mathcal{G}_{\mathrm{res}} = \Delta(SU(N)) = \{(g_0, \dots, g_0) : g_0 \in SU(N)\} \cong SU(N)$. Its action on any co-tree edge $e = (u \to v) \in E_{\mathrm{co-tree}}$ is simultaneous adjoint conjugation:
  $$(g_0 \cdot \widetilde{U})_e = g_0 \widetilde{U}_e g_0^{-1} = \operatorname{Ad}_{g_0}(\widetilde{U}_e),$$
  where $\widetilde{U}_e = H(C_T(e))[U]$ is the fundamental-cycle holonomy rooted at $x_0$. Since the center $Z(SU(N)) \cong \mathbb{Z}_N$ acts trivially on $\Sigma_T$, the effective residual gauge group is $\operatorname{Ad}(SU(N)) \cong SU(N)/\mathbb{Z}_N = PSU(N)$.

### Item 3: Edge and Cycle Counts (`YM-011-TREE-T2`) — **PASS**
- **Mathematical Audit:**
  - Summing comb-tree edges by direction $\mu \in \{1, \dots, d\}$ gives $|T| = \sum_{\mu=1}^d L^{\mu-1}(L-1) = L^d - 1 = |V| - 1$.
  - Cycle rank / co-tree edge counts:
    - $\Lambda_{\mathrm{free}}(L, d)$: $|E_{\mathrm{co-tree}}| = |E_+| - |V| + 1 = d(L-1)L^{d-1} - L^d + 1$, giving $(L-1)^2$ ($d=2$), $(2L+1)(L-1)^2$ ($d=3$), and $(3L^2+2L+1)(L-1)^2$ ($d=4$).
    - $\Lambda_{\mathrm{per}}(L, d)$: $|E_{\mathrm{co-tree}}| = dL^d - L^d + 1 = (d-1)L^d + 1$, partitioned into $d(L-1)L^{d-1} - L^d + 1$ interior co-tree edges and $dL^{d-1}$ boundary-wrapping co-tree edges.
  - Alternating cell-count sums confirm $\chi(\Lambda_{\mathrm{free}}) = \sum_{k=0}^d (-1)^k \binom{d}{k}(L-1)^k L^{d-k} = (L - (L-1))^d = 1$ and $\chi(\Lambda_{\mathrm{per}}) = \sum_{k=0}^d (-1)^k \binom{d}{k} L^d = 0$.
- **Implementation & Test Verification:** Verified in `build_lattice_graph` (`src/ymmg/tree_gauge.py:159-235`) and `test_01_combinatorial_edge_tree_cotree_and_cycle_rank_counts` (`tests/test_ym_011_tree_gauge.py:35-59`).

### Item 4: Plaquette-Coordinate Claims Across $d = 2, 3, 4$ — **PASS**
- **Mathematical Audit:**
  - **$d = 2$ Free Boundary:** $|E_{\mathrm{co-tree}}| = |P_+| = (L-1)^2$. In comb tree gauge, all vertical links and bottom-spine horizontal links equal $I_N$, so $U_{p_{x_1, x_2}} = \widetilde{U}_{((x_1, x_2), \hat{1})} \widetilde{U}_{((x_1, x_2+1), \hat{1})}^{-1}$ inverts triangularly via $\widetilde{U}_{((x_1, x_2), \hat{1})} = U_{p_{x_1, x_2-1}}^{-1} \cdots U_{p_{x_1, 0}}^{-1}$ with unit Haar Jacobian $J = 1$.
  - **$d \ge 3$ Free Boundary:** Since $\chi(\Lambda_{\mathrm{free}}) = |V| - |E_+| + |P_+| - |C_3| + |C_4| = 1$, the excess of plaquettes over co-tree links is $|P_+| - |E_{\mathrm{co-tree}}| = |C_3| - |C_4| > 0$ (equal to $(L-1)^3$ in $d=3$ and $(3L+1)(L-1)^3 = 3L^4 - 8L^3 + 6L^2 - 1$ in $d=4$). Because $H_1(\Lambda_{\mathrm{free}}) = 0$, the map is injective, forming a constrained embedding onto the Bianchi subvariety.
  - **Periodic Torus $\Lambda_{\mathrm{per}}(L, d)$:** Neither injective (the $d(N-1)$-dimensional commuting toron family $\mathcal{Z}_{\mathrm{per}}$ maps to $U_p \equiv I_N$) nor surjective (constrained by surface and 3-cube Bianchi identities).
- **Implementation & Test Verification:** Verified in `reconstruct_d2_free_from_plaquettes`, `audit_plaquette_coordinate_map`, `test_03`, and `test_04`.

### Item 5: Bianchi Constraints (`NEG-YM-011-TREE-1`) — **PASS**
- **Mathematical Audit:** Around any elementary 3-cube $c \in C_3$, the product of the 6 base-point-transported face holonomies `L1 @ L2 @ L3 @ L4 @ L5 @ L6` telescopes identically via pairwise edge cancellations ($U_e U_e^{-1} = I_N$) to $\prod_{f=1}^6 \widehat{U}_{p_f(c)} = I_N$ for arbitrary non-Abelian $SU(N)$ links. Consequently, the $|C_3| - |C_4|$ dependent plaquettes in $P_+ \setminus P_{\mathrm{sel}}$ are non-local products of the $|E_{\mathrm{co-tree}}|$ spanning plaquettes, preventing single-plaquette factorization of $S_W$ in $d \ge 3$. Registered in `NEGATIVE_EVIDENCE_REGISTER.md` (`NEG-YM-011-TREE-1`, lines 120–128) and verified numerically to $< 10^{-14}$ in `test_04`.

### Item 6: Measure & Jacobian — **PASS**
- **Mathematical Audit:** Under $\Phi_T(g, \widetilde{U}) = g^{-1} \cdot \widetilde{U}$, conditioning on $g \in \mathcal{G}_{x_0}$ maps each co-tree link $\widetilde{U}_e \mapsto g(u)^{-1} \widetilde{U}_e g(v)$ by left and right group translations, preserving $\prod_{e \in E_{\mathrm{co-tree}}} d\mu_{\mathrm{Haar}}(\widetilde{U}_e)$ by bi-invariance of Haar measure on $SU(N)$. Peeling tree leaves from maximum tree depth $k = |V|-1$ down to $k = 1$ maps $g(x_k) \mapsto U_{e_k} = g(p(x_k))^{-1} g(x_k)$ with $g(p(x_k))$ fixed by shallower vertices, yielding $d\mu_{\mathrm{Haar}}(U_{e_k}) = d\mu_{\mathrm{Haar}}(g(x_k))$ by Fubini's theorem and left-translation invariance. Thus $J_{\mathrm{tree}} \equiv 1$ and $\Delta_{\mathrm{FP}} \equiv 1$.

### Item 7: Free-Boundary Zero Set & Hessian (`YM-011-TREE-T3`) — **PASS**
- **Mathematical Audit:** On $\Lambda_{\mathrm{free}}(L, d)$, $H(\widetilde{U}) = 0 \iff U_p = I_N \;\forall p \in P_+ \iff \widetilde{U}_e = H(C_T(e)) = I_N \;\forall e \in E_{\mathrm{co-tree}}$ because every fundamental cycle $C_T(e)$ bounds a 2-chain of plaquettes in the contractible complex. Expanding $\widetilde{U}_e = \exp(\sum_a A_e^a T^a)$ ($\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$) gives $H(\exp(A)) = \frac{1}{4N}\sum_{a=1}^{N^2-1} \langle A^a, \mathcal{H}_{\mathrm{tree}}(L, d) A^a \rangle + O(\|A\|^3)$ with $\mathcal{H}_{\mathrm{tree}}(L, d) = (d_\Lambda|_{\Sigma_T})^T (d_\Lambda|_{\Sigma_T})$. Since $H^1(\Lambda_{\mathrm{free}}; \mathbb{R}) = 0$ and $T_{\mathrm{free}}$ spans $V_{\mathrm{free}}$, $\ker(d_\Lambda|_{\Sigma_T}) = \{0\}$, so $\ker D^2 H|_{\Sigma_{T_{\mathrm{free}}}}(I_N) = \{0\}$ and $\operatorname{rank} D^2 H|_{\Sigma_{T_{\mathrm{free}}}}(I_N) = D_{\mathrm{free}} = (N^2-1)(d(L-1)L^{d-1} - L^d + 1)$.

### Item 8: Periodic Toron Moduli (`YM-011-TREE-T4`) — **PASS**
- **Mathematical Audit:** On $\Lambda_{\mathrm{per}}(L, d)$ in comb tree gauge $\Sigma_{T_{\mathrm{per}}}$, $H(\widetilde{U}) = 0$ forces:
  1. All interior links ($0 \le x_\mu \le L-2$) to $\widetilde{U}_e = I_N$ by `YM-011-TREE-T3`(1);
  2. Mixed interior-wrapping plaquettes ($x_\mu = L-1, 0 \le x_\nu \le L-2$) to satisfy $W_\mu(x_{\perp \mu}) I_N W_\mu(x_{\perp \mu} + \hat{\nu})^{-1} I_N^{-1} = I_N \implies W_\mu(x_{\perp \mu}) = U_\mu \in SU(N)$ independent of $x_{\perp \mu}$;
  3. Corner wrapping plaquettes ($x_\mu = x_\nu = L-1$) to satisfy $U_\mu U_\nu U_\mu^{-1} U_\nu^{-1} = [U_\mu, U_\nu] = I_N$.
  Thus $\mathcal{Z}_{\mathrm{per}} \cong \operatorname{Hom}(\mathbb{Z}^d, SU(N)) = \{(U_1, \dots, U_d) \in SU(N)^d : [U_\mu, U_\nu] = I_N\}$, and quotienting by $\mathcal{G}_{\mathrm{res}} = \operatorname{Ad}(SU(N))$ simultaneously diagonalizes $(U_1, \dots, U_d)$ into $(T_{\mathrm{max}})^d$ up to simultaneous Weyl permutations $W(SU(N)) = S_N$, proving $\mathcal{M}_{\mathrm{flat}}(\Lambda_{\mathrm{per}}, SU(N)) \cong (T_{\mathrm{max}})^d / S_N$ of dimension $d(N - 1)$.

### Item 9: Stabilizer Strata — **PASS**
- **Mathematical Audit:** Under $\operatorname{Ad}(SU(N))$, the stabilizer at a generic regular toron $U_{\mathrm{reg}} \in \mathcal{Z}_{\mathrm{per}}^{\mathrm{reg}}$ is the maximal torus $T_{\mathrm{max}}$ of dimension $N - 1$ (adjoint orbit dimension $(N^2-1)-(N-1) = N(N-1)$). At the $N^d$ central torons $U_{\mathrm{cent}} = (z_1 I_N, \dots, z_d I_N) \in Z(SU(N))^d$, the stabilizer jumps to the full group $SU(N)$ of dimension $N^2 - 1$, yielding an exact stabilizer dimension jump of $\Delta \dim \operatorname{Stab} = (N^2 - 1) - (N - 1) = N(N - 1)$.

### Item 10: Quartic Zero Modes — **PASS**
- **Mathematical Audit:** At a regular toron $U_{\mathrm{reg}}$, the quadratic Hessian kernel in $\Sigma_{T_{\mathrm{per}}}$ has dimension $d(N - 1) + N(N - 1) = (d + N)(N - 1)$. At a central toron $U_{\mathrm{cent}} \in Z(SU(N))^d$, central phases cancel on all plaquettes and the corner plaquette perturbation $U_{p_{\mu\nu}^{\mathrm{corner}}}(U_{\mathrm{cent}} e^X) = \exp([X_\mu, X_\nu] + O(\|X\|^3))$ has zero linear variation for all $X_1, \dots, X_d \in \mathfrak{su}(N)$, so the Hessian nullity jumps to $d(N^2 - 1)$. This releases:
  $$d(N^2 - 1) - (d + N)(N - 1) = (d - 1)N(N - 1)$$
  transverse off-diagonal modes stabilized only at fourth order by the quartic commutator energy:
  $$H_{\mathrm{quartic}}(X_1, \dots, X_d) = \frac{1}{2N} \sum_{1 \le \mu < \nu \le d} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2.$$

### Item 11: Boundary-Condition Dependence & `NEG-YM-011-PLAQ-1` — **PASS**
- **Audit:** Verified in `literature/YM-011-TREE-GAUGE-ANALYSIS.md` Section 6.1 and `NEGATIVE_EVIDENCE_REGISTER.md` (`NEG-YM-011-PLAQ-1` Post-Tree-Gauge Re-Evaluation, lines 94–98). The periodic-torus obstruction in tree gauge is rigorously classified as **Category E (combination of A: residual global $\operatorname{Ad}(SU(N))$ conjugation, B: $d(N-1)$ physical flat Cartan moduli $(T_{\mathrm{max}})^d/S_N$, C: stabilizer jump $\Delta \dim \operatorname{Stab} = N(N-1)$ at $N^d$ central torons, and D: $(d-1)N(N-1)$ quartic commutator zero modes)**, whereas $\Lambda_{\mathrm{free}}(L, d)$ avoids torons because $H_1(\Lambda_{\mathrm{free}}) = 0$.

### Item 12: $O(1/\beta)$ Claim Scope (Claims A, B, C) — **PASS**
- **Audit:**
  - **Claim A (Fixed finite lattice $O(1/\beta)$):** Proved on $\Lambda_{\mathrm{free}}(L, d)$ via compact finite-dimensional Laplace asymptotics around the isolated nondegenerate minimum $\widetilde{U} = I_N$, yielding $e_{\mathrm{plaq}}(\beta, \Lambda_{\mathrm{free}}(L, d)) = C_{\mathrm{free}}(L, d, N)/\beta + O_L(\beta^{-2})$ with $C_{\mathrm{free}}(L, d, N) = \frac{(N^2-1)|E_{\mathrm{co-tree}}|}{2|P_+|} \to \frac{N^2-1}{d}$ as $L \to \infty$. On $\Lambda_{\mathrm{per}}(L, d)$, ordinary Laplace fails (`OPEN_BEYOND_LOG_BETA`).
  - **Claim B (Volume-uniform lattice $O(1/\beta)$):** Proved **ONLY** in $d = 2$ free boundary ($C_{\mathrm{free}}(L, 2, N) = \frac{N^2-1}{2}$ independent of $L$ via exact plaquette factorization) and strictly withheld as `NOT_ESTABLISHED` in $d \ge 3$.
  - **Claim C (Continuum-useful uniform estimate):** Strictly `NOT_ESTABLISHED`.
  - Enforced programmatically in `evaluate_fixed_volume_equipartition_bound` (`src/ymmg/tree_gauge.py:596-650`) and tested in `test_07`.

### Item 13: Volume Dependence — **PASS**
- **Mathematical Audit:** On $\Lambda_{\mathrm{free}}(L, 2)$, $\mathcal{H}_{\mathrm{tree}}(L, 2)$ decouples into $L - 1$ columns, each isomorphic to the $(L-1) \times (L-1)$ 1D discrete Laplacian with Dirichlet bottom boundary ($u_0 = 0$) and free/Neumann top boundary ($u_L = u_{L-1}$), whose exact spectrum is $4\sin^2\!\left(\frac{(2k-1)\pi}{2(2L-1)}\right)$ ($k=1,\dots,L-1$). Thus:
  $$\lambda_{\min}\!\left(\mathcal{H}_{\mathrm{tree}}(L, 2)\right) = 4 \sin^2\!\left(\frac{\pi}{2(2L - 1)}\right) = \frac{\pi^2}{4L^2} + O(L^{-3}) \xrightarrow{L \to \infty} 0,$$
  and similarly $\lambda_{\min}(\mathcal{H}_{\mathrm{tree}}(L, d)) \to 0$ as $L \to \infty$ in $d \ge 3$ due to $O(dL)$ comb-tree fundamental-cycle paths. This proves why fixed-volume Laplace asymptotics cannot be promoted to volume-uniform bounds in $d \ge 3$.

### Item 14: Source-to-Claim Correspondence & Governance Invariants — **PASS**
- **Audit:**
  - The 11-column Primary-Source Audit Table (`literature/YM-011-TREE-GAUGE-ANALYSIS.md` Section 7, lines 178–185) accurately records `Source`, `Theorem / Page`, `Gauge Group`, `Dimension`, `Boundary Condition`, `Volume`, `$\beta$ Regime`, `Gauge Fixing`, `Zero-Mode Treatment`, `Volume Uniformity`, and `Actual Conclusion` for Creutz (1977/1983), Osterwalder & Seiler (1978), Batrouni (1982), Bałaban (1984), Lüscher (1982), and Chatterjee (2019).
  - Numerical Hessian spectra in `HessianDiagnosticResult` carry explicit `epistemic_status = "NUMERICAL_DIAGNOSTIC_ONLY"`.
  - `literature/YM-011-TREE-GAUGE-ANALYSIS.md` is bound in `governance/SCIENTIFIC_ARTIFACT_CLASSIFICATION.yaml` and `src/ymmg/ros.py`, matching `SCIENTIFIC_TREE_HASH = d7eca47e7fc9b469ac88992a63e3c2362839f1bb1a577a30d3e0932516988f55`.
  - Global invariants remain intact: `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, and `YM-006` through `YM-010 = SCIENTIFIC_REVIEW_HOLD`.

---

## 2. Final Audit Verdict

**`INTEGRITY_PASS`**
