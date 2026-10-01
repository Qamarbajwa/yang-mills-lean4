# YM-014-RANDOM-SURFACE-DUALITY-TARGET: Target Specification for Non-Perturbative Representations Across the Intermediate Crossover Window

- **TASK_ID:** `YM-014`
- **OBJECTIVE:** Random-Surface / Duality Crossover Representation Analysis
- **MISSING_BRIDGE_EDGE:** `E-CROSSOVER` (Intermediate Coupling Crossover Window $g_k \sim 1$)
- **GOVERNANCE_STATUS:** Target Specification (Phase 1)
- **DATE:** 2026-10-02

---

## 1. Context and Problem Statement

Previous project tasks established two distinct, rigorous structural barriers spanning the intermediate coupling crossover window $g_k \sim 1$ ($\beta \in (\beta_0, \beta_{\mathrm{UV}}^*)$):
1. **The Series Expansion / Flow Continuation Barrier (`YM-012`):**  
   Neither small-field Gaussian expansions ($\kappa_{\mathrm{BF}} \ge 1$) nor large-field polymer expansions converge inside the crossover window ($\Delta\beta \ge 2N - 1 > 0$ in $d=4$, Theorem `YM-012-T1`, `YM-012-T2`). Furthermore, gradient flow mollification accumulates $\Omega(1)$ total variation measure error per scale step (`NEG-YM-012-CROSSOVER-1`).
2. **The Finite-Perimeter Truncation Barrier (`YM-013`):**  
   Lattice Schwinger–Dyson / Makeenko–Migdal loop equations cannot self-close at finite trace degree without planar large-$N$ factorization (Theorem `YM-013-T1`), Mandelstam trace reduction forces exponential loop perimeter explosion $|AB| = |A| + |B|$ (Theorem `YM-013-T2`), and at any fixed perimeter cutoff $L_{\max} < \infty$, the physical reach $R_{\max}(a) = L_{\max} a \to 0$ decouples from the non-perturbative physical scale $R_{\mathrm{cross}} \approx 0.5\text{ fm}$ in the continuum limit $a \to 0$ (Theorem `YM-013-T4`).

Task `YM-014` investigates whether four-dimensional finite-$N$ lattice Yang–Mills theory can be reformulated into a non-perturbative **random-surface, dual spin-foam, center-vortex, or character-expansion representation** whose estimates remain mathematically valid and uniform throughout the intermediate coupling regime $g \sim 1$, thereby circumventing both previous barriers.

---

## 2. The 16 Formal Target Specification Fields

Before evaluating any candidate representation, we define the minimum mathematically sufficient statement that would constitute genuine progress beyond `YM-012` and `YM-013`.

| Field # | Attribute | Formal Specification |
| :--- | :--- | :--- |
| **F01** | **Theorem Identifier** | `YM-014-TARGET` |
| **F02** | **Gauge Group** | Primary: $G = SU(2)$; Secondary: $G = SU(3)$ and general $SU(N)$ ($N \ge 3$) analyzed on separate branches. |
| **F03** | **Spacetime Dimension** | $d = 4$ Euclidean spacetime on hypercubic lattice $\mathbb{Z}^4$ (or dual 2-complex). |
| **F04** | **Lattice Geometry & Boundary Conditions** | Hypercubic periodic torus $\Lambda_{\mathrm{per}}(L_{\mathrm{vol}}, 4)$ ($L_{\mathrm{vol}} \ge 4$), twisted torus $\Lambda_{\mathrm{twist}}$, or $\mathbb{Z}^4$ thermodynamic limit. |
| **F05** | **Coupling Interval** | $\beta \in I_{\mathrm{cross}} = [1.5, 2.5]$ for $SU(2)$, strictly intersecting the YM-012 crossover window $(\beta_0, \beta_{\mathrm{UV}}^*) \approx (0.35, 4.0)$ and centered at $g_0 \approx 1$ ($\beta = 4/g_0^2 = 2.0$). |
| **F06** | **Finite vs. Infinite Volume** | All representation weights and bounds must admit a rigorous, volume-uniform thermodynamic limit $\Lambda \uparrow \mathbb{Z}^4$. |
| **F07** | **Exact Transformed Variables** | Discrete surface configurations $\Sigma \subset \Lambda^*$ with representation labels $j_p \in \frac{1}{2}\mathbb{Z}_+$, center flux cocycles $z \in Z(G)^{\Lambda}$, or dual intertwiners $i_\ell \in \operatorname{Inv}(\bigotimes j_p)$. |
| **F08** | **Positivity / Sign Structure** | The transformed weights $W(\Sigma)$ must either be strictly non-negative ($W(\Sigma) \ge 0$) or possess a rigorously bounded sign oscillation ratio $\sum |W(\Sigma)| / |\sum W(\Sigma)| \le C < \infty$ uniformly in volume. |
| **F09** | **Surface / Flux Weights** | Explicit local or quasilocal weights $W(\Sigma) = \prod_{p \in \Sigma} w(j_p, \beta) \prod_{\ell} c(i_\ell)$ with decay rate exceeding the surface entropy: $\tau(\beta) > \ln \mu_4$. |
| **F10** | **Lattice Spacing Dependence** | As $a \to 0$, the representation must scale consistently with asymptotic freedom: the physical string tension $\sigma_{\mathrm{phys}} = \tau(\beta(a))/a^2$ must remain finite and non-zero ($0 < \sigma_{\mathrm{phys}} < \infty$). |
| **F11** | **Observable Correspondence** | Exact, non-heuristic map from gauge-invariant observables (Wilson loop $W(C)$, 't Hooft loop $B(C)$, twisted partition function ratio $Z(\text{twist})/Z(0)$) to surface/flux ensemble expectations. |
| **F12** | **Required Uniform Constants** | The effective surface tension $\tau_{\mathrm{eff}}(\beta)$, mass gap $m_{\mathrm{lat}}(\beta)$, or flux free energy $F_{\mathrm{el}}(\beta, L)/L^2$ must be bounded away from zero uniformly in lattice volume $L \to \infty$. |
| **F13** | **Downstream DAG Edge Unlocked** | Edge $E\text{-}CROSSOVER\text{-}WINDOW$ ($\text{Node } N\text{-}UV\text{-}RG\text{-}BOUNDS \to N\text{-}INT\text{-}CROSSOVER$) or $E\text{-}NONPERT\text{-}CONSTR$ ($\text{Node } N\text{-}INT\text{-}CROSSOVER \to N\text{-}EFF\text{-}NONPERT$). |
| **F14** | **Bypass of YM-012 Barrier** | Must not rely on perturbative expansions around $\beta = \infty$ (Gaussian small-field contractivity) or polymer expansions around $\beta = 0$ that diverge inside $I_{\mathrm{cross}}$. |
| **F15** | **Bypass of YM-013 Barrier** | Must not be restricted to finite loop perimeters $L_{\max} < \infty$; must allow surfaces of arbitrary physical area $A_{\mathrm{phys}} = n a^2$ as $a \to 0$. |
| **F16** | **Explicit Non-Claims** | Must NOT claim continuum Wightman construction, continuum reflection positivity, or solution of the Clay Millennium Problem without closing the entire downstream DAG. |

---

## 3. Strict Prohibitions and Epistemic Invariants

Any candidate claiming to satisfy `YM-014-TARGET` must strictly enforce:

1. **No Conflation of Abelian Duality with Non-Abelian Gauge Theory:**
   Kramers–Wannier duality for 4D Abelian $U(1)$ lattice gauge theory (which maps $\beta \mapsto 1/\beta$) does NOT apply to non-Abelian $SU(N)$ gauge theories. Importing Abelian duality without an explicit non-Abelian transfer theorem is prohibited.
2. **No Heuristic Center Projection or Uncontrolled Gauge Fixing:**
   Center-vortex condensation arguments relying on maximal center gauge fixing (plagued by Gribov copies and unproved Faddeev–Popov determinants) are heuristic and cannot serve as mathematical proof.
3. **No Hidden Expansion Non-Convergence:**
   A representation that formally writes $\langle W(C) \rangle = \sum_{\Sigma} W(\Sigma)$ is vacuous if the sum over surfaces diverges due to surface entropy ($\tau(\beta) < \ln \mu$).
4. **Preservation of Constitutional Invariants:**
   - `goal_complete = false`
   - `clay_problem = OPEN_AND_UNSOLVED`
   - `P3 = OPEN`
   - `E-CROSSOVER = OPEN`
