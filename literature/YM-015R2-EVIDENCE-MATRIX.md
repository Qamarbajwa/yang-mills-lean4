# YM-015R2-EVIDENCE-MATRIX — Authoritative Evidence, Lemma Status, and Traceability Matrix

- **Document Identifier:** `YM-015R2-EVIDENCE-MATRIX`
- **Task Association:** `YM-015R2 — Exact RP Status Repair and Nonperturbative Flowed-Continuum Bridge`
- **Governance Classification:** Post-Reconciliation Source-to-Evidence Verification and Epistemic Status Matrix
- **Authoritative Baseline:** State Revision 32
- **Status:** `COMPLETE_RECONCILED_MAPPING`

---

## 1. Executive Summary

This matrix establishes the authoritative epistemic classification for all theorems, lemmas, witnesses, and architectural routes audited during Task `YM-015R2`. Every claim is tied to its primary literature source, mathematical status, temporal locality classification, failure locality, code implementation, and downstream impact.

---

## 2. Authoritative 10-Column Source-Evidence Matrix

| Theorem / Lemma ID | Formal Mathematical Statement | Primary Literature Source & Citation | Project Reconstructed Derivation | Verification Mechanism | Code Implementation & Unit Test | Epistemic Classification | Temporal Locality | Downstream Dependency | Missing-Bridge Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`YM-015-L3`** | Reflection positivity status for 4D gradient flow with support buffer $\delta$ | Osterwalder & Seiler, Ann. Phys. 110 (1978); Lüscher (2010) | `YM-015R2-RP-STATUS-AMENDMENT.md` | Heat kernel leakage proves $F_t \notin \mathcal{A}_+$; but $\langle \Theta F F \rangle < 0$ unproved (no counterexample) | `src/ymmg/uv_continuum.py`; `test_ym_015r2` | **`EXACT_RP_UNRESOLVED_FOR_FINITE_4D_FLOW_TIME`** | `EXPONENTIALLY_TIME_NONLOCAL` | Standard half-space inheritance fails as a proof method | `OPEN_AND_UNRESOLVED` |
| **`RP-DEFECT-BOUND`** | Heuristic bound $\Delta_{\mathrm{RP}} \lesssim e^{-\delta^2/(4t)}$ | Conjectural extrapolation from scalar heat kernel | `YM-015R2-RP-STATUS-AMENDMENT.md` (Sec 4) | Conflates linear heat kernel tail with nonlinear Wilson measure expectation | N/A (Excised from theorem proofs) | **`CONJECTURAL_ERROR_MODEL`** | N/A | Removed from proof-level reasoning | `EXCISED_FROM_THEOREMS` |
| **`ROUTE-C`** | Two-stage limit ($a \to 0$ at $t > 0$, then $t \downarrow 0$) | M. Lüscher & P. Weisz, JHEP 02 (2011) 051 | `YM-015R2-OBSERVABLE-ROUTE-MATRIX.md` (Sec 3) | Preserves $Z \equiv 1$ and $H_4$ at $t > 0$; requires fixed-$t$ object and $t \to 0$ limit | `src/ymmg/uv_continuum.py` | **`CANDIDATE_LOCALITY_RECOVERY_ARCHITECTURE`** | `EXPONENTIALLY_TIME_NONLOCAL` ($t > 0$) $\to$ `STRICT_LOCAL` ($t = 0$) | Prerequisite for physical OS reconstruction | `OPEN_CANDIDATE_PATHWAY` |
| **`YM-015F-L1`** | Uniform Smeared Schwinger Bound at fixed $t \ge t_{\min} > 0$ | M. Lüscher (2010); T. Bałaban, CMP 109, 116 (1987) | `YM-015R2-FLOWED-CONTINUUM-TARGET.md` (Sec 2) | Peierls large-field suppression $e^{-c\beta/a^4}$ beats $a^{-4k}$; small-field contractivity | `src/ymmg/uv_continuum.py` | **`PARTIAL_PROGRESS — CONDITIONAL_ON_BALABAN_OBSERVABLE_FLOW`** | `EXPONENTIALLY_TIME_NONLOCAL` | Prerequisite for multilinear compactness (L2) | `PARTIAL_UNIFORM_BOUND_ONLY` |
| **`YM-015F-L2`** | Subsequential multilinear continuum distribution extraction | Banach–Alaoglu Theorem; Grothendieck–Schwartz Kernel Theorem | `YM-015R2-FLOWED-CONTINUUM-TARGET.md` (Sec 3) | Weak-* compactness in projective tensor dual $(\mathcal{H}_\pi^{(k)})^*$ and $\mathcal{D}'$ | `src/ymmg/uv_continuum.py` | **`SUBSEQUENTIAL_MULTILINEAR_DISTRIBUTION_EXTRACTION`** | `EXPONENTIALLY_TIME_NONLOCAL` | Foundation for flowed correlation limits | `PRECOMPACT_FLOWED_LIMIT` |
| **`YM-015-SPF1/2`** | Spatial gradient flow exact slice autonomy and reflection positivity | Morningstar & Peardon (1999); Lüscher (1977, 2010) | `YM-015R2-SPATIAL-FLOW-ANALYSIS.md` (Sec 3 & 4) | Purely spatial flow decouples time slices; $F_t \in \mathcal{A}_+$ strictly for $x_4 > 0$ | `src/ymmg/spatial_flow.py`; `test_ym_015r2` | **`SPATIAL_FLOW_RP_COMPATIBILITY_PROVED`** | **`STRICT_TIME_SLICE_LOCAL`** | Satisfies Criterion A for exact OS2 | `PROVED_FOR_SPATIAL_FLOW` |
| **`YM-015-L4`** | Continuous Euclidean translation covariance | H. D. Kirk (2026, Lemma 7); distribution theory | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 5) | Discrete lattice translation + fractional shift $O(a)$ vanishing | `src/ymmg/uv_continuum.py` | **`CONFIRMED_CONDITIONALLY_ON_L1`** | N/A | Axiom OS1 translation invariance | `CONFIRMED_CONDITIONALLY` |
| **`YM-015-L5`** | Vanishing hypercubic anisotropy and continuous $SO(4)$ restoration | T. Bałaban, CMP 116 (1988); K. Symanzik, NPB 226 (1983) 187 | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 6) | $H_4 \to SO(4)$ representation theory valid; $O(a^2)$ scaling is Symanzik perturbative | `src/ymmg/uv_continuum.py` | **`PERTURBATIVE_SUPPORT_ONLY`** | N/A | Axiom OS1 continuous rotational covariance | `UNPROVED_NONPERTURBATIVELY` |
| **`YM-015-W1`** | Strict nontriviality witness for flowed 2-point function | M. Lüscher, JHEP 08 (2010) 071, Sec 4 | `YM-015R-CONTINUUM-RECONCILIATION.md` (Sec 7) | $\operatorname{Var}_a > 0$ at finite $a$; continuum uniform lower bound unproved nonperturbatively | `src/ymmg/uv_continuum.py` | **`FINITE_CUTOFF_NONDEGENERACY_ONLY`** | N/A | Excludes empty trivial lattice theory | `PARTIAL_FINITE_CUTOFF_ONLY` |

---

## 3. Precursor and Successor Status

1. **Precursors Satisfied:**
   - `YM-011` (UV Scale-Transfer and Observables Mollification) $\to$ `SATISFIED_WITH_REGULATED_SCOPE`.
   - `YM-014R` (External-Evidence Reconciliation and Obstruction-Theorem Repair) $\to$ `SATISFIED`.
   - `YM-015R` (Continuum-Construction Stress Test) $\to$ `SATISFIED`.
2. **Current Missing-Bridge Status:**
   - `E-UV-FREE-CONT` is **`OPEN_AND_UNSOLVED`**.
   - Sub-edge `E-UV-FLOWED` is **`PARTIAL_PROGRESS`** (Precompact multilinear limit conditional on Bałaban observable insertion).
   - Sub-edge `E-UV-LOCAL-OS` is **`OPEN_AND_UNSOLVED`** (Requires downstream $t \downarrow 0$ local limit under Criterion B or spatial flow under Criterion A).
3. **Successor Task Blocking:**
   - `YM-016` (`E-CROSSOVER` / Thermodynamic Limit) is strictly **`BLOCKED`** pending full non-perturbative closure of `E-UV-FREE-CONT`.
