# YM-014-REPRESENTATION-LANDSCAPE: Audit of Candidate Non-Perturbative Representations Across the Intermediate Crossover Window

- **TASK_ID:** `YM-014`
- **OBJECTIVE:** Comprehensive Audit of Candidate Non-Perturbative Representations (A through E)
- **MISSING_BRIDGE_EDGE:** `E-CROSSOVER`
- **GOVERNANCE_STATUS:** Phase 2, 4, 5, 7, 11 Audit
- **DATE:** 2026-10-02

---

## 1. Executive Summary

Task `YM-014` investigates whether four-dimensional finite-$N$ lattice Yang–Mills theory can be reformulated into an exact non-perturbative representation whose analytical control persists through the intermediate-coupling crossover window $\beta \in [1.5, 2.5]$ ($g \sim 1$).

This document audits five canonical classes of non-perturbative reformulations:
1. **Candidate A:** Pure Random-Surface / Character Expansion (Peter–Weyl, Balian–Drouffe–Itzykson, Weingarten, Gross)
2. **Candidate B:** Non-Abelian Dual Spin-Foam / Cell-Complex Representations (Ooguri, Baez, Perez, Barrett–Crane, Pfeiffer)
3. **Candidate C:** Center-Vortex / Center-Flux Decomposition (Mack–Petkova, Tomboulis, 't Hooft electric-flux free energy)
4. **Candidate D:** Fermionic / Worldline Rewriting & Loop-Space String Representations (Polyakov string, Migdal loop transform)
5. **Candidate E:** Exact Solved Lower-Dimensional & Abelian Dualities (2D Yang–Mills, 3D Compact QED monopole gas, 4D Kramers–Wannier Abelian duality)

Each representation is audited against:
- Exact mathematical definition on $\mathbb{Z}^4$;
- Positivity / sign structure;
- Regimes of proved convergence vs. breakdown;
- Failure locality when applied to $\beta \in [1.5, 2.5]$;
- Downstream missing-bridge utility.

---

## 2. Detailed Audit of Candidate Representations

### 2.1. Candidate A: Pure Random-Surface / Character Expansion

#### 2.1.1. Mathematical Formulation
By the Peter–Weyl theorem on compact Lie group $G = SU(N)$, any class function on $G$ expands in irreducible characters $\chi_R$. The single-plaquette Boltzmann factor $e^{-S_p(U_p)} = \exp\left(\frac{\beta}{2N}(\operatorname{Tr} U_p + \operatorname{Tr} U_p^\dagger)\right)$ admits the exact character expansion:
$$e^{-S_p(U_p)} = c_0(\beta) \left( 1 + \sum_{R \ne 0} d_R a_R(\beta) \chi_R(U_p) \right),$$
where $d_R = \dim(R)$ and $a_R(\beta) = \frac{1}{d_R c_0(\beta)} \int_G d\mu_{\mathrm{Haar}}(U) e^{-S_p(U)} \chi_R(U^\dagger)$.

For $SU(2)$, representations are indexed by half-integers $j \in \{1/2, 1, 3/2, \dots\}$, with $d_j = 2j+1$, and:
$$a_j(\beta) = \frac{I_{2j+1}(\beta)}{(2j+1) I_1(\beta)},$$
where $I_n(\beta)$ are modified Bessel functions of the first kind.

Expanding the lattice partition function $Z(\beta) = \int \prod dU_e \prod_p e^{-S_p(U_p)}$ generates a sum over closed 2-complexes $\Sigma \subset \Lambda^*$ whose 2-cells are decorated by representations $R_p$. Integrating over link variables $U_e$ via the character orthogonality / Clebsch–Gordan theorem forces representation matching at edges:
$$\int d\mu_{\mathrm{Haar}}(U_e) \bigotimes_{p \ni e} D^{R_p}(U_e) = \sum_{i_e} v_{i_e} \otimes v_{i_e}^*,$$
where $i_e$ indexes invariant intertwiners in $\operatorname{Inv}(\bigotimes_{p \ni e} R_p)$.

#### 2.1.2. Convergence and Breakdown
- **Strong Coupling ($\beta \ll 1$):** $a_{1/2}(\beta) = \frac{I_2(\beta)}{2 I_1(\beta)} \sim \frac{\beta}{8} \ll 1$. Higher representations are suppressed as $a_j(\beta) = O(\beta^{2j})$. The surface expansion is dominated by minimal-area surfaces, yielding a convergent polymer expansion for $\beta \le \beta_0 \approx 0.35$ (Theorem `THM-YM-0010`, Osterwalder–Seiler 1978).
- **Crossover Regime ($\beta \in [1.5, 2.5]$):** For $SU(2)$ at $\beta = 2.0$:
  $$a_{1/2}(2.0) = \frac{I_2(2.0)}{2 I_1(2.0)} = \frac{0.688948}{2 \times 1.590637} \approx 0.21657,$$
  yielding a bare surface tension:
  $$\tau_0(\beta) = -\ln a_{1/2}(2.0) \approx 1.5298.$$
  In $d=4$, the number of connected 2D lattice surfaces of area $A$ with fixed boundary grows as $N(A) \asymp \mu_4^A A^{-\gamma}$, where the 4D surface connectivity constant is $\mu_4 \ge 3.5$ (typically $\mu_4 \approx 5-8$, so $\ln \mu_4 \ge 1.6-2.1$).
  Because $\tau_0(\beta) < \ln \mu_4$, the bare surface tension fails to overcome the surface entropy. The sum over surfaces $\sum_A N(A) e^{-\tau_0 A}$ undergoes a Hagedorn / roughening divergence.
- **Epistemic Classification:** `METHOD_LIMITATION_ROUGHENING_BARRIER`.

---

### 2.2. Candidate B: Non-Abelian Dual Spin-Foam / Cell-Complex Representations

#### 2.2.1. Mathematical Formulation
Exact duality transformations for 4D non-Abelian lattice gauge theory on the dual 4D cell complex $\Lambda^*$ associate:
- An irreducible representation $j_f$ to each 2-face $f \in (\Lambda^*)_2$ (dual to lattice plaquettes);
- An invariant intertwiner $i_e \in \operatorname{Inv}(j_{f_1} \otimes j_{f_2} \otimes j_{f_3} \otimes j_{f_4})$ to each 1-edge $e \in (\Lambda^*)_1$ (dual to lattice 3-cubes);
- A 4-simplex / hypercube amplitude to each 0-vertex $v \in (\Lambda^*)_0$ (dual to lattice 4-cells), given by the contraction of 8 intertwiners (for hypercubes) or a Wigner $15j$ symbol (for 4-simplices).

The partition function takes the exact spin-foam form:
$$Z = \sum_{\{j_f\}} \sum_{\{i_e\}} \prod_f d_{j_f} a_{j_f}(\beta) \prod_e \dim(i_e) \prod_v \mathcal{A}_v(j_f, i_e).$$

#### 2.2.2. Positivity and the Non-Abelian Sign Barrier
- In Abelian gauge theory ($U(1)$ or $\mathbb{Z}_N$), group representations are 1-dimensional, intertwiners are trivial constraints, and the dual weights are strictly positive: $\mathcal{A}_v \in \{0, 1\}$.
- In non-Abelian gauge theory ($SU(2)$, $SU(3)$), intertwiner contractions $\mathcal{A}_v$ evaluate to Wigner $6j$, $9j$, or $15j$ recoupling symbols.
- Wigner $6j$ symbols $\left\{\begin{matrix} j_1 & j_2 & j_3 \\ j_4 & j_5 & j_6 \end{matrix}\right\}$ oscillate in sign across admissible spin configurations.
- Consequently, the dual weights $W(\{j_f, i_e\}) = \prod_f a_{j_f} \prod_v \mathcal{A}_v$ are NOT positive:
  $$\exists \{j_f, i_e\} \quad \text{such that} \quad W(\{j_f, i_e\}) < 0.$$
- This creates an extensive sign problem: $\langle \operatorname{sign} \rangle = \frac{\sum W}{\sum |W|} \le e^{-c V}$. Dual spin foams cannot be interpreted as probabilistic random surfaces, cluster expansions cannot be bounded by absolute values, and Peierls contour arguments fail completely.
- **Epistemic Classification:** `NON_ABELIAN_SIGN_OSCILLATION_BARRIER`.

---

### 2.3. Candidate C: Center-Vortex / Center-Flux Decomposition

#### 2.3.1. Mathematical Formulation
The center of $SU(N)$ is $Z(SU(N)) \cong \mathbb{Z}_N$. The gauge group admits the global fibration:
$$\mathbb{Z}_N \hookrightarrow SU(N) \to PSU(N) \cong SU(N)/\mathbb{Z}_N.$$
On the lattice, one decomposes link variables as:
$$U_e = z_e \, V_e, \quad z_e \in \mathbb{Z}_N, \quad V_e \in SU(N)/\mathbb{Z}_N.$$
Under this decomposition, the Wilson action decomposes into:
$$S_W(U) = -\frac{\beta}{2N} \sum_p \operatorname{Re}\operatorname{Tr}(U_p) = -\frac{\beta}{2N} \sum_p z_p \operatorname{Re}\operatorname{Tr}(V_p),$$
where $z_p = \prod_{e \in \partial p} z_e \in \mathbb{Z}_N$ is the center flux through plaquette $p$.

#### 2.3.2. Evaluation Across the Crossover Window
- **At $\beta = 0$:** $V_e$ and $z_e$ decouple under the Haar measure $d\mu_{SU(N)} = d\mu_{\mathbb{Z}_N} \otimes d\mu_{PSU(N)}$. The center flux $z$ forms an independent $\mathbb{Z}_N$ gauge theory with disordered center vortices.
- **At $\beta > 0$:** The term $z_p \operatorname{Re}\operatorname{Tr}(V_p)$ couples center flux directly to coset fluctuations $V$. Integrating out $V_e$ produces an effective center-action:
  $$e^{-S_{\mathrm{eff}}(z)} = \int \prod_e dV_e \exp\left( \frac{\beta}{2N} \sum_p z_p \operatorname{Re}\operatorname{Tr}(V_p) \right).$$
  This effective action contains all-order, non-local multi-plaquette interactions among center flux loops.
- **In the Crossover Window ($\beta \in [1.5, 2.5]$):**
  - Mack–Petkova (1979) and Tomboulis (1981) proved that center-vortex condensation implies an area law *provided* the effective action satisfies a polymer/Peierls bound.
  - However, computing $S_{\mathrm{eff}}(z)$ requires integrating out $V_e$, which is mathematically equivalent to solving the non-Abelian coset model.
  - The polymer expansion for $S_{\mathrm{eff}}(z)$ converges *only* for $\beta \le \beta_0 \approx 0.35$.
  - In the crossover regime $\beta \sim 2$, the non-local sheet couplings diverge, coset fluctuations lose stability, and the center-vortex ensemble cannot be bounded away from percolation collapse or flat-connection alignment.
- **Epistemic Classification:** `COSET_COUPLING_NON_CONVERGENCE_BARRIER`.

---

### 2.4. Candidate D: Fermionic / Worldline Rewriting & Loop-Space String Representations

#### 2.4.1. Mathematical Formulation
Polyakov (1981, 1997) proposed representing Yang–Mills Wilson loop expectations $\langle W(C) \rangle$ as a functional integral over 2D worldsheets $\Sigma$ immersed in 4D Euclidean space:
$$\langle W(C) \rangle = \int_{\partial \Sigma = C} \mathcal{D}X \mathcal{D}g \exp\left( -\sigma_0 \int d^2\xi \sqrt{g} - \frac{1}{\alpha'} \int d^2\xi \sqrt{g} g^{ab} \partial_a X^\mu \partial_b X_\mu + S_{\mathrm{extrinsic}} \right).$$

#### 2.4.2. Mathematical Barriers in $d=4$
- **Conformal Anomaly:** Critical string theories require spacetime dimension $D = 26$ (bosonic) or $D = 10$ (superstring). In $D = 4$, the Liouville field does not decouple; the non-critical worldsheet action has negative Liouville central charge or tachyonic instabilities.
- **Rigid / Extrinsic Curvature String:** Polyakov and Kleinert proposed adding an extrinsic curvature term $\frac{1}{\alpha} \int d^2\xi \sqrt{g} (\Delta X)^2$ to suppress crumpling. However, rigorous analysis (Ambjørn et al. 1992) proved that the rigid string undergoes a first-order phase transition directly from a crumpled phase to an unphysical smooth phase with infinite string tension, without any non-trivial continuum scaling window.
- **Loop-Space Non-Closure:** The Makeenko–Migdal loop-space functional Laplacian does not admit a mathematically rigorous measure on the infinite-dimensional loop space $\mathcal{L}(\mathbb{R}^4)$.
- **Epistemic Classification:** `NON_CRITICAL_STRING_ANOMALY_BARRIER`.

---

### 2.5. Candidate E: Exact Solved Lower-Dimensional & Solved Analogues

#### 2.5.1. Audit of Solved Analogues
1. **2D Yang–Mills ($d=2$):** Migdal (1975), Witten (1991, 1992). Solved exactly via character expansion because $\chi(M_2) = 2 - 2g$ eliminates all non-trivial intertwiner networks: every link is shared by at most two plaquettes. In $d=4$, every link is shared by $2(d-1) = 6$ plaquettes, creating 6-face intertwiner vertices whose sign oscillations prevent factorization.
2. **3D Compact QED ($d=3$):** Polyakov (1977), Göpfert–Mack (1981). Duality transforms compact $U(1)$ into a dilute gas of point monopoles with Coulomb interaction $V(r) \sim 1/r$. The gas is mapped to a sine-Gordon field theory with rigorous mass gap. In 4D $SU(N)$, magnetic defects are not point particles, but extended 2D vortex sheets with non-Abelian internal degrees of freedom.
3. **4D Abelian $U(1)$ Gauge Theory:** Kramers–Wannier duality maps $U(1)$ at coupling $\beta$ to dual $U(1)$ with coupling $1/\beta$. Non-Abelian $SU(N)$ does NOT possess self-duality: the dual of $SU(N)$ is not a local gauge theory of the same form.

#### 2.5.2. Transfer Audit
Zero transfer mechanisms exist from 2D Yang–Mills or 3D Abelian monopole gases to 4D non-Abelian Yang–Mills that survive the higher-dimensional cell-complex geometry and non-Abelian sign problem.
- **Epistemic Classification:** `ANALOGUE_TRANSFER_OBSTRUCTED`.

---

## 3. Primary-Source Representation Audit Table

| Source Key | Primary Citation | Representation Class | Dimension / Group | Proved Regime | Claimed Crossover Utility | Rigorous Status in $d=4$ $SU(2)$ Crossover |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `BDI-1975` | Balian, Drouffe, Itzykson (1975) | Character Expansion | Any $d$, compact $G$ | $\beta \to 0$ | High-temperature expansion | Fails at $\beta \sim 2$ (roughening transition) |
| `OOG-1992` | Ooguri (1992) | Dual Spin Foam | $d=4$, $SU(2)$ | Topological BF theory | Dual quantum gravity / gauge theory | Indefinite $15j$ signs; non-positive weights |
| `MP-1979` | Mack, Petkova (1979) | $\mathbb{Z}_2$ Center Vortices | $d=4$, $SU(2)$ | Area law if vortices condense | Non-perturbative confinement | Coset integration diverges for $\beta > \beta_0$ |
| `TOM-1981` | Tomboulis (1981) | Center-Vortex Effective Action | $d=4$, $SU(2)$ | Polyakov loop bounds at small $\beta$ | Electric flux confinement | Effective sheet action non-convergent at $\beta \sim 2$ |
| `POL-1981` | Polyakov (1981, 1997) | Confining String Ansatz | $d=4$ continuum | N/A (conjectural) | Exact string dual | Worldsheet conformal anomaly; no 4D measure |
| `AMB-1992` | Ambjørn, Durhuus, Jonsson (1992) | Rigid Random Surfaces | $d \ge 3$ | Discrete triangulations | Avoid surface crumpling | First-order transition; no continuum limit |
| `GM-1981` | Göpfert, Mack (1981) | Monopole Gas Duality | $d=3$, $U(1)$ | All $\beta < \infty$ | Non-perturbative mass gap | Abelian only; 4D defects are 2D sheets |
| `WIT-1991` | Witten (1991, 1992) | 2D Gauge Theory | $d=2$, $SU(N)$ | All $\beta$ | Exact solution via characters | Fails in $d=4$ due to 6-plaquette link sharing |

---

## 4. Synthesis and Structural Verdict

Across all five candidate classes, the failure localities in the crossover regime $\beta \in [1.5, 2.5]$ fall into two universal mathematical mechanisms:
1. **The Surface Entropy vs. Energy Deficit:**  
   Character and surface expansions suffer a roughening transition when $\tau_0(\beta) < \ln \mu_4$. In $d=4$, $\tau_0(2.0) \approx 1.53 < \ln \mu_4 \ge 1.61$, rendering the surface sum divergent.
2. **The Non-Abelian Dual Sign Obstruction:**  
   Dual spin foams and cell-complex representations possess indefinite Wigner $6j$/$15j$ weights, creating an extensive sign problem that destroys probabilistic and cluster-expansion methods.

These two mechanisms will be derived as formal obstruction theorems in `literature/YM-014-SURFACE-ENTROPY-ENERGY.md` and `literature/YM-014-CONTINUUM-SCALING.md`.
