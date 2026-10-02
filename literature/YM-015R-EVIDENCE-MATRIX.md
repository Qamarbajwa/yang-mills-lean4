# YM-015R-EVIDENCE-MATRIX — Authoritative Post-Reconciliation Evidence & Traceability Matrix

- **Document Identifier:** `YM-015R-EVIDENCE-MATRIX`
- **Task Association:** `YM-015R — Post-Acceptance Stress Test and Scientific Repair`
- **Governance Classification:** Source-to-Evidence Verification and Theorem Amendment Matrix
- **Authoritative Baseline:** State Revision 31
- **Status:** `COMPLETE_RECONCILED_MAPPING`

---

## 1. Executive Summary

This matrix establishes the authoritative, post-reconciliation epistemic classification for all theorems, lemmas, witnesses, and architectural routes audited during Task `YM-015R`. Every claim is tied to its primary literature source, mathematical status, failure locality, code implementation, and downstream impact.

---

## 2. Authoritative 10-Column Source-Evidence Matrix

| Theorem / Lemma ID | Formal Mathematical Statement | Primary Literature Source & Citation | Project Reconstructed Derivation | Verification Mechanism | Code Implementation & Unit Test | Epistemic Classification | Scope Limitation | Downstream Dependency | Missing-Bridge Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`YM-015-L1`** | Cutoff-independent smeared moment bounds: $\|S_k^a(f_1, \dots, f_k)\| \le C_k \prod \|f_i\|_{H^3}$ | M. Lüscher, JHEP 08 (2010) 071; M. Struwe, Calc. Var. PDE 2 (1994) 123 | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 2) | Hölder inequality + Sobolev embedding; operator bound $\le C/t^2$ is perturbative | `src/ymmg/uv_continuum.py::evaluate_uniform_schwinger_bound`; `test_02` | **`DOWNGRADED_TO_PERTURBATIVE_AND_SMALL_FIELD`** | Conditional on non-perturbative flow contractivity; unproved on rough configurations | Prerequisite for multilinear compactness (L2) | `PARTIAL_UNIFORM_BOUND_ONLY` |
| **`YM-015-L2`** | Subsequential continuum multilinear distribution extraction: $S_k \in \mathcal{D}'((\mathbb{T}^4)^k)$ | Banach–Alaoglu Theorem; Grothendieck–Schwartz Kernel Theorem | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 3) | Weak-* compactness on projective tensor dual $(\mathcal{H}_\pi^{(k)})^*$ and nuclear space $\mathcal{D}'$ | `src/ymmg/uv_continuum.py`; `test_02` | **`SUBSEQUENTIAL_MULTILINEAR_DISTRIBUTION_EXTRACTION`** | Yields multilinear distributions, NOT a physical Schwinger system (OS2/OS4 open) | Foundation for flowed correlation limits | `PARTIAL_PRECOMPACTNESS_ONLY` |
| **`YM-015-L3`** | Reflection positivity inheritance under support-buffer condition: $\delta > \sqrt{8t}$ | Osterwalder & Seiler, Ann. Phys. 110 (1978); Lüscher (2010) | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 4) | Heat-kernel infinite tails $K_t \propto e^{-r^2/(4t)} > 0$ violate $A \in \mathcal{A}_+$ for all finite $\delta$ | `src/ymmg/uv_continuum.py::verify_reflection_positivity_support_buffer`; `test_05` | **`REFUTED_FOR_EXACT_RP_AT_FINITE_FLOW_TIME`** | Exact OS2 fails at $t > 0$; defect $\Delta_{\mathrm{RP}} \sim O(e^{-\delta^2/(4t)}) > 0$ | GNS Hilbert space reconstruction fails at $t > 0$ | **`OPEN_AND_UNRESOLVED`** |
| **`YM-015-L4`** | Continuous Euclidean translation covariance: $S_k(\tau_h f_1 \dots) = S_k(f_1 \dots)$ | H. D. Kirk (2026, Lemma 7); standard distribution theory | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 5) | Discrete lattice translation invariance + fractional shift $O(a)$ vanishing | `src/ymmg/uv_continuum.py::evaluate_translation_continuity`; `test_03` | **`CONFIRMED_CONDITIONALLY_ON_L1`** | Fixed $V < \infty$, UV basin; conditioned on functional continuity | Axiom OS1 translation invariance | `CONFIRMED_CONDITIONALLY` |
| **`YM-015-L5`** | Vanishing hypercubic anisotropy and continuous $SO(4)$ restoration: $S_k(R f_1 \dots) = S_k(f_1 \dots)$ | T. Bałaban, CMP 116 (1988); K. Symanzik, NPB 226 (1983) 187 | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 6) | $H_4 \to SO(4)$ representation theory is valid; $O(a^2)$ scaling is Symanzik perturbative | `src/ymmg/uv_continuum.py::evaluate_hypercubic_anisotropy_scaling`; `test_04` | **`PERTURBATIVE_SUPPORT_ONLY`** | Perturbative expectation only; non-perturbative spacing-uniform bound unproved | Axiom OS1 continuous rotational covariance | `UNPROVED_NONPERTURBATIVELY` |
| **`YM-015-W1`** | Strict nontriviality of 2-point connected Schwinger function: $S_2^c(t, t)(f \otimes f) > 0$ | M. Lüscher, JHEP 08 (2010) 071, Sec 4 | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 7) | Variance is non-zero at finite $a$; continuum lower bound relies on unproved remainder control | `src/ymmg/uv_continuum.py::evaluate_nontriviality_witness`; `test_06` | **`FINITE_CUTOFF_NONDEGENERACY_ONLY`** | Proved at finite $a > 0$; continuum uniform lower bound unproved non-perturbatively | Excludes trivial empty lattice theory | `PARTIAL_FINITE_CUTOFF_ONLY` |
| **`ROUTE-A`** | Spatial-only gradient flow | M. Lüscher (2010); Symanzik (1983) | `YM-015R-LOCALITY-REPLACEMENT-ANALYSIS.md` (Sec 2) | Smooths spatial links only; preserves $\mathcal{A}_+$ identically | `src/ymmg/uv_continuum.py` | `ARCHITECTURAL_ALTERNATIVE` | Explicitly breaks $SO(4) \to SO(3)$; temporal contact singularities persist | Alternative for spatial gap | `BACKUP_CANDIDATE` |
| **`ROUTE-B`** | Zero-flow-time local bare observables | T. Bałaban, CMP 99–122 (1984–1989) | `YM-015R-LOCALITY-REPLACEMENT-ANALYSIS.md` (Sec 2) | Bare local operators strictly in $\mathcal{A}_+$ | `src/ymmg/uv_continuum.py` | `ARCHITECTURALLY_BLOCKED` | Severe $a^{-4}$ UV divergences, operator mixing, contact divergences | Constructive program | `CONSTRUCTIVELY_BLOCKED` |
| **`ROUTE-C`** | Two-stage limit ($a \to 0$ at $t > 0$, followed by $t \downarrow 0$) | M. Lüscher & P. Weisz, JHEP 02 (2011) 051 | `YM-015R-LOCALITY-REPLACEMENT-ANALYSIS.md` (Sec 2 & 4) | At $t > 0$, $Z \equiv 1$; exact OS2 recovered as $t \downarrow 0$ since defect $\to 0$ | `src/ymmg/uv_continuum.py` | **`PRIMARY_RECOMMENDED_ARCHITECTURE`** | Requires OPE subtractions as $t \downarrow 0$ | Resolves OS2 without breaking $SO(4)$ | **`PRIMARY_PATHWAY`** |
| **`ROUTE-D`** | Half-space Dirichlet cylinder flow | Standard parabolic boundary-value theory | `YM-015R-LOCALITY-REPLACEMENT-ANALYSIS.md` (Sec 2) | Dirichlet condition on $\Sigma_0$ isolates $\Lambda_+$ | `src/ymmg/uv_continuum.py` | `ARCHITECTURALLY_BLOCKED` | Breaks translation invariance in $x_4$; boundary divergences on $\Sigma_0$ | None | `STRUCTURALLY_FLAWED` |

---

## 3. Precursor and Successor Status

1. **Precursors Satisfied:**
   - `YM-011` (UV Scale-Transfer and Observables Mollification) $\to$ `SATISFIED_WITH_REGULATED_SCOPE`.
   - `YM-014R` (External-Evidence Reconciliation and Obstruction-Theorem Repair) $\to$ `SATISFIED`.
2. **Current Missing-Bridge Status:**
   - `E-UV-FREE-CONT` is **`OPEN_AND_UNRESOLVED`** for the physical Osterwalder–Schrader field theory.
   - It is partially bridged only as **`PRECOMPACT_FLOWED_MULTILINEAR_LIMIT_WITH_UNRESOLVED_RP_AND_SO4`**.
3. **Successor Task Blocking:**
   - `YM-016` (`E-CROSSOVER`) is **`BLOCKED_PENDING_YM-015R`** and must not proceed until the continuum object upon which the crossover operates is unambiguously specified under Route C.
