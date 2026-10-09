# YM-051R2 bounded technical acceptance

Decision: TECHNICAL_ACCEPTANCE_GRANTED. Date: 2026-10-09.
Accepted baseline revision 54 / c6859211542a1c1e2983a9ffc5681425d44aa3f8. Frozen candidate 15c8c13dc9f51728d34cccc80942ff4710030dee.

## Authority Separation and Provenance (IND1_DISTINCT_PROCESS_ACCEPTOR)

Execution authorities are strictly separated under IND1_DISTINCT_PROCESS_ACCEPTOR:
- WRITER: `00ffe8a3-c73a-4096-b0e7-53138b34c21a`
- REVIEWER (E4): `fa7b8aa6-896f-4836-961b-8f7844561345` (Fresh Blind YM-051R2 Mathematical & Governance Verifier, verdict: `INTEGRITY_PASS`)
- ACCEPTOR: `4629eec4-50b0-4559-a271-14dfcc2347cf` (Distinct process under `IND1_DISTINCT_PROCESS_ACCEPTOR`)

Acceptor directly inspected candidate commit `15c8c13dc9f51728d34cccc80942ff4710030dee` on disk, read the entire review receipt `verification/raw/YM-051R2_E4_RAW_20261009.md`, and independently verified its byte SHA-256 digest:
`0470e24a1d1a1d16fa6a15e344efcd31b107f95a0e9e55c05b9b93a9b3712552`.
The reviewer verdict is `INTEGRITY_PASS` across all 10 mandatory review criteria without unresolved defects. Writer, reviewer, and acceptor operated in strictly distinct execution contexts.

---

## Independent Verification & Analysis

Acceptor conducted independent mathematical, code, and governance inspections across all candidate artifacts directly on disk:

1. **Candidate Commit SHA & Git Cleanliness:**
   - Audited candidate commit SHA: `15c8c13dc9f51728d34cccc80942ff4710030dee`.
   - Baseline commit SHA: `c6859211542a1c1e2983a9ffc5681425d44aa3f8`.
   - Lineage verified: `15c8c13` is the immediate child of `c685921` (which closed out YM-051R at state revision 54 following acceptance `774d69d`).
   - Candidate `15c8c13` modifies exactly 7 canonical files (+631 lines, -417 lines).
   - Working tree clean (untracked receipt `verification/raw/YM-051R2_E4_RAW_20261009.md` present for closeout).

2. **E4 Independent Review Receipt Verification:**
   - Receipt path: `verification/raw/YM-051R2_E4_RAW_20261009.md`.
   - Verified SHA-256 digest: `0470e24a1d1a1d16fa6a15e344efcd31b107f95a0e9e55c05b9b93a9b3712552` (exact byte match).
   - Reviewer Conversation ID: `fa7b8aa6-896f-4836-961b-8f7844561345`.
   - Reviewer verdict: `INTEGRITY_PASS` across all 10 mandatory review criteria.

3. **Reconciliation of Lie Algebra Conventions and Determinants:**
   - Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (Section YM-051R2, lines 616–648).
   - Audited the explicit dictionary reconciling:
     - **Hermitian generator convention (Bałaban CMP 109, R-I (1.81)):** Basis $T_a = \frac{1}{2}\sigma_a$, $[T_a, T_b] = i\epsilon_{abc}T_c$, Hermitian fluctuation $B^\prime$ with $\operatorname{Tr}((B^\prime)^2) \ge 0$, group link $\exp(i B^\prime)$ with anti-Hermitian exponent $i B^\prime$.
     - **Anti-Hermitian generator convention (Lie Theory / Quaternions):** Basis $\tilde{T}_a = i T_a = \frac{i}{2}\sigma_a$, $[\tilde{T}_a, \tilde{T}_b] = -\epsilon_{abc}\tilde{T}_c$, Lie algebra element $X = i B^\prime \in \mathfrak{su}(2)$ with $\operatorname{Tr}(X^2) \le 0$, pure imaginary quaternions $\operatorname{Im}(\mathbb{H})$ with $X^2 = -\|X\|^2 \le 0$, group exponential $\exp(X)$ without explicit $i$.
     - **Orientation vs. Volume Density:** Directional derivative matrix $D_{V_0}$ along tree $T_0$ has signed determinant $\det(D_{V_0}) = +1$ (orientation-preserving isomorphism), while integration volume density scales by absolute Jacobian $|\det(D_{V_0})| = 1$. Both are explicitly distinguished and asserted.

4. **Exact Rational Unit Quaternions in SU(2):**
   - Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 649–659) and `tests/test_source_jet_finite_certificates.py` (lines 270–294).
   - In $SU(2) \cong \mathbb{H}_1$, group elements must satisfy $\|q\|^2 = q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1$.
   - All group link variables and site gauge transformations are constructed from Pythagorean quadruples in $\mathbb{Q}$:
     - Background transporters: $V_0(b_1) = (3/5, 4/5, 0, 0)$, $V_0(b_2) = (3/5, 0, 4/5, 0)$, $V_0(b_3) = (4/5, 0, 0, 3/5)$, $V_0(b_4) = (5/13, 12/13, 0, 0)$ (all $\|q\|^2 = 1$).
     - Fluctuation factors: $U_{\mathrm{fluc}}(b_1) = (24/25, 7/25, 0, 0)$, $U_{\mathrm{fluc}}(b_2) = (12/13, 0, 5/13, 0)$, $U_{\mathrm{fluc}}(b_3) = (4/5, 0, 0, 3/5)$, $U_{\mathrm{fluc}}(b_4) = (3/5, 4/5, 0, 0)$ (all $\|q\|^2 = 1$).
     - Physical links $U(b) = U_{\mathrm{fluc}}(b) V_0(b)$ have $\|U(b)\|^2 = \|U_{\mathrm{fluc}}(b)\|^2 \|V_0(b)\|^2 = 1 \cdot 1 = 1$.
   - All non-unit approximations (such as $10/9$, $65/64$) are completely excised.

5. **Multi-Edge Rooted Tree $T_0$ Affine Transport:**
   - Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 660–680) and `tests/test_source_jet_finite_certificates.py` (lines 207–221, 295–334).
   - Rooted tree $T_0$ has 3 edges with depth 2 and multiple branches: branch 1 $b_1 = (x_0, x_1)$, depth-2 continuation $b_2 = (x_1, x_2)$, branch 2 $b_3 = (x_0, x_3)$ with root $x_0 = (1, 1)$, $h_{x_0} = (1, 0, 0, 0) = I$.
   - Sequential affine parallel transport:
     $h_{x_1} = V_0(b_1)^{-1} h_{x_0} U(b_1)$, $h_{x_2} = V_0(b_2)^{-1} h_{x_1} U(b_2)$, $h_{x_3} = V_0(b_3)^{-1} h_{x_0} U(b_3)$.
   - All site gauge transformations have exact unit norm $\|h_x\|^2 = 1$.
   - Simultaneously, all 3 tree links are fixed: $U^h(b_1) = V_0(b_1)$, $U^h(b_2) = V_0(b_2)$, $U^h(b_3) = V_0(b_3)$.
   - Non-tree cycle edge $b_4 = (x_2, x_3)$ transforms as $U^h(b_4) = h_{x_2} U(b_4) h_{x_3}^{-1}$ with strictly positive holonomy defect $\|U^h(b_4) - V_0(b_4)\|^2 = 38536388 / 34328125 > 0$, rigorously proving that dynamical gauge-invariant degrees of freedom are preserved.
   - Naive uncoupled transformation setting $h_x = I$ everywhere leaves non-zero tree defect $\sum_{b \in T_0} \|U(b) - V_0(b)\|^2 > 0$, proving affine coupling is mandatory.

6. **Observable Mixed Dependence Non-Factorization Defect:**
   - Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 681–693) and `tests/test_source_jet_finite_certificates.py` (lines 356–375).
   - Audited the explicit composite gauge-invariant observable $\mathcal{O}(U_A, U_B) = \frac{1}{2} \operatorname{Tr}(U_A U_B) = \operatorname{Re}(U_A U_B) = (U_A U_B)_0$ coupling preliminary region $Z_h$ and active region $\Lambda_0$ across boundary $\partial Z_h$.
   - The cross-variation non-factorization determinant evaluates to:
     $$\Delta_{\mathrm{fact}} = \mathcal{O}_{11}\mathcal{O}_{22} - \mathcal{O}_{12}\mathcal{O}_{21} = 1 \cdot \left(-\frac{7}{25}\right) - \left(\frac{3}{5}\right)\left(\frac{3}{5}\right) = -\frac{16}{25} \ne 0.$$
   - Non-zero cross-defect rigorously disproves spatial factorization across $\partial Z_h$, replacing scalar heuristic constants.
   - Discrete lattice Wilson gradient flow mixed derivatives $\frac{\partial^2 S_{\mathrm{flowed}}}{\partial U(b_1) \partial U(b_2)} \ne 0$ are verified as the physical lattice mechanism.

7. **Concrete Actual-History Audit and Dependency Ordering:**
   - Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 694–722), `research/YM_CONSTRUCTION_DEFECT_CORRECTION_LEDGER.md` (CDC-051R2, lines 101–123), and `research/YM_CROSS_DOMAIN_TRANSFER_REGISTRY.md` (lines 251–263).
   - Audited ONE concrete admissible history $\alpha$ from Bałaban R-I (1.76): exterior domain $Z \cap \Lambda^c$, preliminary region $Z_h$, active region $\Lambda_0 = \Lambda \setminus Z_h$, external bonds $\mathbb{B}_0$, background transporter $V_0 = M_{\mathbb{B}_k^\prime}(U_0)$, and rooted gauge group $\mathcal{G}_{\Lambda_0}$ with root condition $h_{x_0} = I$.
   - Formulated the explicit missing bridge lemma:
     **LEMMA `YM-051F-ACTUAL-CHART-SUMMABILITY` (Small-Field Chart Stability and Remainder Activity Bound)**, establishing that tree-gauge orbit chart exit is bounded by $\mathcal{O}(e^{-c_k / g_k^2})$ and remainder activity satisfies $\|\mathcal{R}_{\alpha, \mathrm{large}}\| \le C_k e^{-M / g_k^2} \|\mathcal{O}\|_\infty$.
   - Corrected dependency ordering: multiscale polymer activity summability is conditionally dependent on this chart stability lemma and is NOT the immediate next dependency-satisfied obligation.
   - Reclassified as `CONDITIONAL_AND_OPEN` (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN`). Zero DAG edges close.

8. **Negative Evidence Register Integrity:**
   - Inspected `NEGATIVE_EVIDENCE_REGISTER.md` (lines 529–541): entry `NEG-YM-051R2-UNIT-QUATERNION-AND-OBSERVABLE-DEFECT` registered under `[METHOD_SPECIFIC_OBSTRUCTION]`.
   - Git diff confirms strictly additive changes (+14 lines, 0 deletions); zero historical negative evidence entries were deleted, modified, or weakened.

9. **Closed-World Scientific Tree Hash & Test 14 Whitelist:**
   - Inspected `tests/test_governance_v406r3_adoption.py`: line 263 explicitly whitelists `c9f53ceeb0d5b99357f8eb65aa371c5464ff9558b9fa68ce7cf5a8048e6f4fbc`.
   - Independently computed `compute_closed_world_scientific_tree_hash(Path('.'))` over exactly 158 canonical files:
     `c9f53ceeb0d5b99357f8eb65aa371c5464ff9558b9fa68ce7cf5a8048e6f4fbc` (exact match).

10. **Full Deterministic Test Suite Execution:**
    - Executed full test suite (`python -m pytest`): **441 passed in 7.01s** with zero failures, zero errors, zero warnings (exit code 0).

---

## Confirmation of 12 Hard Gates (PROJECT_BOUND_READINESS_RULE.yaml)

| Gate | Name | Requirement | Finding | Status |
|---|---|---|---|---|
| 1 | `candidate_frozen` | Exact candidate commit SHA is frozen in Git and recorded in state | Candidate SHA is `15c8c13dc9f51728d34cccc80942ff4710030dee` (child of baseline `c6859211542a1c1e2983a9ffc5681425d44aa3f8`). Clean working tree (untracked review receipt). | **PASS** |
| 2 | `candidate_bound_review` | Review is strictly bound to candidate SHA | Review receipt `verification/raw/YM-051R2_E4_RAW_20261009.md` explicitly binds SHA `15c8c13dc9f51728d34cccc80942ff4710030dee`; verified SHA-256 digest `0470e24a1d1a1d16fa6a15e344efcd31b107f95a0e9e55c05b9b93a9b3712552`. | **PASS** |
| 3 | `scientific_review_pass` | Review verdict is `INTEGRITY_PASS` | Review verdict is `INTEGRITY_PASS` across all 10 mandatory review criteria. | **PASS** |
| 4 | `negative_evidence_preserved` | Negative evidence registered; zero historical deletions | `NEG-YM-051R2-UNIT-QUATERNION-AND-OBSERVABLE-DEFECT` registered; Git diff confirms +14 lines, 0 deletions. | **PASS** |
| 5 | `dependencies_satisfied` | All precursor tasks completed and accepted | Precursor tasks `YM-051R`, `YM-051`, `YM-050R2`, `YM-050R`, `YM-050`, `YM-049`, and `YM-015F-JET-002A` completed and accepted in `governance/PROJECT_STATE.yaml`. | **PASS** |
| 6 | `scientific_tree_identity` | Tree hash matches verified canonical hash | Closed-world hash matches `c9f53ceeb0d5b99357f8eb65aa371c5464ff9558b9fa68ce7cf5a8048e6f4fbc` (158 canonical files); present on Test 14 whitelist. | **PASS** |
| 7 | `state_revision_freshness` | State revision increments monotonically | Current state revision is 54; next state revision will be 55. | **PASS** |
| 8 | `no_unresolved_mandatory_blocker` | Zero unresolved mandatory blockers within bounded scope | Zero mandatory blockers exist within the bounded repair scope (only non-mandatory `NO_REMOTE` in `governance/PROJECT_STATE.yaml`). | **PASS** |
| 9 | `goal_complete_false_invariant` | `goal_complete` remains `false` | `goal_complete: false` verified in `governance/PROJECT_STATE.yaml`; invariant preserved. | **PASS** |
| 10 | `clay_problem_unsolved_invariant` | `clay_problem` remains `OPEN_AND_UNSOLVED` | `clay_problem: OPEN_AND_UNSOLVED` verified in `governance/PROJECT_STATE.yaml`; invariant preserved. | **PASS** |
| 11 | `scientific_acceptance_authority_separation` | Writer != Reviewer != Acceptor (`IND1_DISTINCT_PROCESS_ACCEPTOR`) | Writer (`00ffe8a3...`) != Reviewer E4 (`fa7b8aa6...`) != Acceptor (`4629eec4...`). Distinct processes confirmed. | **PASS** |
| 12 | `regression_protection_for_consequential_defects` | Durable regression tests protect against defects | Test 11 in `tests/test_source_jet_finite_certificates.py` (exact SU(2) unit quaternion certificates, multi-edge tree transport, observable non-factorization defect, Lie convention reconciliation, and signed vs absolute determinants) and full suite (441 tests) pass deterministically. | **PASS** |

---

## Scope, Limitations, and Authorization

Bounded technical acceptance is granted for the YM-051R2 repair of SU(2) unit rational quaternion certificates via Pythagorean quadruples, multi-edge rooted tree affine transport and non-tree cycle holonomy defect, observable mixed dependence non-factorization cross-defect, reconciliation of Hermitian vs anti-Hermitian generator conventions and signed determinant vs absolute Jacobian, concrete actual-history audit and dependency ordering with Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY`, and negative evidence preservation.

Constitutional and epistemic invariants remain strictly intact:
- `goal_complete` = `false`
- `clay_problem` = `OPEN_AND_UNSOLVED`
- `P3` = `OPEN`
- `E-CROSSOVER` = `OPEN`
- `E-UV-FLOWED` = `PARTIAL_PROGRESS`
- `YM-016` = `BLOCKED`
- `STRUCTURAL_NO_GO_COUNT` = `0`

No continuum QFT construction, uniform summability over polymer histories, or spectral gap promotion is claimed or imported. The transfer candidate remains classified as `CONDITIONAL_AND_OPEN` (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN`) and `METHOD_SPECIFIC_OBSTRUCTION`. Scope limitation is recorded as `ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_TREE_GAUGE_CONDITIONAL_AND_OPEN_MULTISCALE_SUMMABILITY_OPEN`; zero DAG edges close.

Root alone is authorized to bind unchanged candidate `15c8c13dc9f51728d34cccc80942ff4710030dee`, E4 receipt digest `0470e24a1d1a1d16fa6a15e344efcd31b107f95a0e9e55c05b9b93a9b3712552`, persist this technical acceptance receipt to `verification/YM-051R2_TECHNICAL_ACCEPTANCE.md`, and advance `governance/PROJECT_STATE.yaml` revision from 54 to 55. Acceptor operated strictly read-only per governance separation.

---

## Final Decision

**FINAL DECISION: TECHNICAL_ACCEPTANCE_GRANTED**  
**Acceptor Conversation ID:** `4629eec4-50b0-4559-a271-14dfcc2347cf`  
**Execution Authority Separation:** `IND1_DISTINCT_PROCESS_ACCEPTOR`
