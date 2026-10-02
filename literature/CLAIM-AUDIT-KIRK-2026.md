# CLAIM-AUDIT-KIRK-2026 — Formal Mathematical Audit of Harold D. Kirk (Version 4, August 2026)

- **Audit Identifier:** `CLAIM-AUDIT-KIRK-2026`
- **Task Association:** `YM-015 — E-UV-FREE-CONT`
- **Audited Work:** Harold D. Kirk, *"Yang-Mills Existence, Mass Gap and Nontriviality for Fixed Compact Simple Gauge Groups via Karcher Blocking and Exact Haar-Pivot Matching,"* Version 4, 2 August 2026.
- **Precursor Papers Inspected:**
  1. H. D. Kirk, *"On the restoration of O(4) invariance in Karcher-blocked lattice gauge theories,"* Preprint (2025).
  2. H. D. Kirk, *"Curvature-jet observables and uniform bounds on the 4D lattice torus,"* Preprint (2025).
  3. H. D. Kirk, *"Exact Haar-pivot matching for nonlinear group-valued block spins,"* Preprint (2026).
- **Epistemic Classification:** `[EXTERNAL_CLAIM_AUDIT]`
- **Audit Date:** 2026-10-02

---

## 1. Executive Summary

In August 2026, Harold D. Kirk posted Version 4 of an ambitious monograph claiming a complete constructive proof of four-dimensional $SU(N)$ Yang–Mills existence, continuous $SO(4)$ rotational covariance, Osterwalder–Schrader reflection positivity, and a positive mass gap via a novel framework combining **Karcher Riemannian center-of-mass blocking**, **exact Haar-pivot matching**, and **curvature-jet observables**.

Under project governance, this work is treated strictly as an **unverified external claim**, not established mathematics.
This audit deconstructs the 10 load-bearing lemmas directly relevant to Task `YM-015` (UV continuum field construction and $SO(4)$ restoration in finite volume), checking:
- Exact quantifiers;
- Circular assumptions;
- Lattice-spacing uniformity;
- Volume dependence;
- Chart coverage and injectivity radius singularities;
- Large-field / exceptional configuration control;
- Reflection positivity support boundaries.

---

## 2. Granular Lemma-by-Lemma Deconstruction

| Lemma ID & Topic | Paper Assertion | Independent Mathematical Evaluation | Flaw / Obstruction / Condition of Validity | Surviving Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Lemma 1: Karcher Blocking Right Inverse** | Claims a global smooth right inverse $\mathcal{K}^{-1}: SU(N)^{E_1} \to SU(N)^{E_0}$ such that $\mathcal{K}(\mathcal{K}^{-1}(V)) = V$ everywhere on the gauge manifold. | **FLAWED ON LARGE FIELDS** | The Karcher Riemannian mean on $SU(N)$ has a unique smooth minimizer only within the injectivity radius $r_{\mathrm{inj}} = \pi/\sqrt{2N}$. On large-field configurations with eigenvalues near $-1$, the Karcher mean hits cut loci and caustic branching. Global smoothness fails without a Bałaban-style small/large-field partition of unity. | Valid strictly on small-field subset $\mathcal{D}_{\mathrm{small}}$ |
| **Lemma 2: Exact Haar-Pivot Matching** | Assumes the Jacobian of the Karcher blocking map is identically 1 plus negligible corrections without an inductive polymer expansion. | **UNJUSTIFIED / INCOMPLETE** | The differential of the group exponential map introduces non-trivial curvature Jacobians $\det(\sin(\operatorname{ad}_X)/\operatorname{ad}_X)$. At finite coupling, these generate non-local interactions that require cluster expansion control. | Not importable without polymer bounds |
| **Lemma 3: Curvature-Jet Observables** | Defines unsmeared observables $J^{(k)}(x) = \nabla^{k-2} F(x)$ and claims uniform $L^2$ bounds on discrete lattices. | **FLAWED (POWER DIVERGENCE)** | Unsmeared lattice finite differences $\nabla_\mu$ diverge as $a \to 0$ without explicit subtractive counterterms or gradient-flow mollification. Pointwise curvature jets are not uniformly bounded in the continuum limit. | Invalid as unsmeared point operators; requires flow mollification |
| **Lemma 4: Tightness & Precompactness** | Assumes weak-* compactness in $\mathcal{D}'(\mathbb{T}^4)$ for smeared observables. | **VALID UNDER MOLLIFICATION** | Proved in `YM-015-L1` and `YM-015-L2` using Banach–Alaoglu on $H^{-3}(\mathbb{T}^4)$ for gradient-flowed observables. | Valid for flow-mollified observables; invalid for bare curvature jets |
| **Lemma 5: Uniform Locality Across Scales** | Assumes effective action maintains exponential decay uniformly without large-field cluster expansion. | **INCOMPLETE** | Same obstruction as YM-012/YM-004: large-field fluctuations at $g \sim 1$ violate naive exponential locality unless guarded by Kotecký–Preiss polymer bounds. | Limited to small-field regime |
| **Lemma 6: Asymptotic Freedom Scaling** | Uses 2-loop beta function running of $g_0(a)$. | **VALID (STANDARD)** | Standard 2-loop perturbative asymptotic freedom in 4D $SU(N)$ (Gross–Wilczek, Politzer). | Fully valid in UV basin |
| **Lemma 7: Translation Covariance** | Proves continuous translation covariance via fractional lattice shift estimates $\tau_h - I \sim O(|h|)$. | **VALID** | Independent verification confirms that discrete lattice invariance plus fractional shift Sobolev estimates $|\tau_h f - f\|_{H^s} \le |h| \|f\|_{H^{s+1}}$ rigorously proves continuous translation covariance (Theorem `YM-015-L4`). | **INDEPENDENTLY CONFIRMED & IMPORTED** |
| **Lemma 8: Hypercubic Anisotropy Suppression** | Derives $O(a^2)$ suppression of non-$SO(4)$ operators under $H_4$ symmetry. | **VALID (UV BASIN)** | The lowest-dimension gauge-invariant hypercubic anisotropic operator has mass dimension 6. Under RG scaling in the UV basin, dimension-6 operators contract by $O(a^2)$ (Theorem `YM-015-L5`). | **INDEPENDENTLY CONFIRMED & IMPORTED** |
| **Lemma 9: Continuous $SO(4)$ Restoration** | Concludes $SO(4)$ covariance of continuum correlators from $O(a^2)$ suppression. | **VALID (FINITE $V$)** | Valid for fixed physical volume $L_{\mathrm{phys}} < \infty$ and positive flow time $t_{\mathrm{phys}} > 0$. | **INDEPENDENTLY CONFIRMED & IMPORTED** |
| **Lemma 10: Reflection Positivity Inheritance** | Claims reflection positivity without a support-buffer restriction. | **FATAL OMISSION** | 4D block averaging or 4D flow diffuses links across the time reflection plane $x_4 = 0$, violating $A \in \mathcal{A}_+$. Reflection positivity holds only if test functions satisfy the support buffer $\delta > R_{\mathrm{diff}}$ (Theorem `YM-015-L3`). | Valid ONLY with support buffer $\delta > \sqrt{8t}$ |

---

## 3. Detailed Technical Critique of Kirk's Framework

### 3.1 The Karcher Mean Injectivity Radius Hazard
The Riemannian center of mass (Karcher mean) of a collection of group elements $\{U_1, \dots, U_m\} \subset SU(N)$ is the unique minimizer of the Riemannian energy:
$$\mathcal{E}(V) = \frac{1}{2m} \sum_{i=1}^m d_G^2(U_i, V),$$
where $d_G(U, V) = \|\log(U^\dagger V)\|_{\mathrm{HS}}$.
By the classic theorem of Karcher (1977) and Kendall (1990):
The minimizer $V$ exists and is unique **if and only if** all points $U_i$ lie inside a geodesic ball of radius:
$$r < \frac{1}{2} r_{\mathrm{inj}}(G) = \frac{\pi}{2\sqrt{2N}}.$$
On a lattice gauge configuration, links $U(e)$ fluctuate over the entire group $SU(N)$. For configurations where eigenvalues of $U_i$ are widely separated (large-field sector), the Karcher energy $\mathcal{E}(V)$ possesses multiple local minima, saddles, and cut loci.
Kirk's assertion of a single, smooth, everywhere-differentiable blocking map $\mathcal{K}$ fails on the large-field measure space. To make this rigorous, one must partition the measure into small-field and large-field regions $\chi_{\mathrm{small}} + \chi_{\mathrm{large}} = 1$ with exponential Peierls bounds $\exp(-\kappa |Y|/g^2)$, exactly as Bałaban did in CMP 99 and CMP 122.

### 3.2 Reflection Positivity and Hyperplane Slicing
Kirk asserts that because the bare Wilson lattice action is reflection positive, the Karcher-blocked continuum theory automatically satisfies OS2.
This ignores the basic spatial extent of the blocking kernel:
A blocked cell centered at $x_4 = a/2$ has links spanning both $x_4 > 0$ and $x_4 < 0$. If an operator contains blocked links at the boundary, it is not an element of the positive-time algebra $\mathcal{A}_+$.
Reflection positivity is salvaged **only** by introducing the support buffer $\delta > R_{\mathrm{block}}$ proved in Theorem `YM-015-L3`.

---

## 4. Final Claim Audit Verdict & Imported Lemmas

1. **Global Claim Acceptance:** **`NOT_ACCEPTED / PROOF_UNSOUND_AS_STATED`**. The paper's claimed global solution to the Clay Millennium Problem is rejected due to unhandled cut-locus singularities in the Karcher mean on large fields, absence of large-field cluster expansion convergence, and unbuffered reflection positivity violations.
2. **Surviving Independently Reconstructible Lemmas (Imported into YM-015):**
   - **`KIRK-LEMMA-7` (Fractional Displacement Translation Covariance):** Confirmed and incorporated into Theorem `YM-015-L4`.
   - **`KIRK-LEMMA-8` (Dimension-6 Hypercubic Anisotropy Suppression):** Confirmed and incorporated into Theorem `YM-015-L5`.
   - **`KIRK-LEMMA-9` ($SO(4)$ Rotational Restoration in Finite Volume):** Confirmed and incorporated into Theorem `YM-015-L5`.
3. **Repository Epistemic Impact:**
   - `CLAY_PROBLEM = OPEN_AND_UNSOLVED`
   - `goal_complete = false`
   - `P3 = OPEN`
   - `E-CROSSOVER = OPEN`
