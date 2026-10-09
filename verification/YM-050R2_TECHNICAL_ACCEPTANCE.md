# YM-050R2 bounded technical acceptance

Decision: TECHNICAL_ACCEPTANCE_GRANTED. Date: 2026-10-09.
Accepted baseline revision 51 / 6d1e46fc1a9f974c3855320fe775c9e26c9dfe13. Frozen candidate 6328f403af0e32fe80c5d4241213f0c472704d58.

## Authority Separation and Provenance (IND1_DISTINCT_PROCESS_ACCEPTOR)

Execution authorities are strictly separated under IND1_DISTINCT_PROCESS_ACCEPTOR:
- WRITER: `00ffe8a3-c73a-4096-b0e7-53138b34c21a`
- REVIEWER (E4): `e436ee6a-4330-473e-addc-0f07fbe873a4` (Fresh Blind YM-050R2 Mathematical & Governance Verifier, verdict: `INTEGRITY_PASS`)
- ACCEPTOR: `799643cd-211f-480c-97ce-cf79fbc53153` (Distinct process under `IND1_DISTINCT_PROCESS_ACCEPTOR`)

Acceptor directly inspected candidate `6328f403af0e32fe80c5d4241213f0c472704d58` on disk, read the entire review receipt `verification/raw/YM-050R2_E4_RAW_20261009.md`, and independently verified its byte SHA-256 digest:
`eaf7af7a89fdc43383da6ce2bbcd550ea4fb0b2824abda64597100feed00137c`.
The reviewer verdict is `INTEGRITY_PASS` without unresolved defects. Writer, reviewer, and acceptor operated in strictly distinct execution contexts.

---

## Independent Verification & Analysis

Acceptor conducted independent mathematical, code, and governance inspections across all candidate artifacts directly on disk:

1. **Exact Upstream Artifacts, Locators, and Digests:**
   Verified upstream repository `https://github.com/openai/math.git` at immutable commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 380–418), `research/YM_CONSTRUCTION_DEFECT_CORRECTION_LEDGER.md` (CDC-050R2), and `research/YM_CROSS_DOMAIN_TRANSFER_REGISTRY.md` (XFER-YM-O3-FAMILY215). Direct inspection confirms the repair of the erroneous `math/` repository prefix (which returned HTTP 404) to `lean/docs/215.md` (HTTP 200). All four primary artifacts, byte lengths, roles, and SHA-256 digests are verified:
   - Scope description: `lean/docs/215.md` (LEN 1,031 bytes, SHA-256 `41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30`). Role: Documentation describing scope of preprint `preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf`; contains zero Lean code or theorem declarations.
   - Comparator challenge: `lean/ComparatorChallenges/ClassicalON.lean` (LEN 1,961 bytes, SHA-256 `c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696`). Role: Formal challenge specification. Namespace: `OAI.ClassicalON`. Exact declarations: `Site := ℤ × ℤ`, `PositiveNeighbor (x y : Site) : Prop`, `structure LatticeGraph`, `Spin`, `Configuration`, `sphereProbability`, `referenceLaw`, `interaction`, `partition`, `correlation`, `siteDistance`, `ExponentialDecay`, and `theorem main : ExponentialDecay := by sorry`.
   - Challenge manifest: `lean/ComparatorChallenges/ClassicalON.json` (LEN 308 bytes, SHA-256 `47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252`). Role: Manifest specifying `challenge_module`: `ComparatorChallenges.ClassicalON`, `solution_module`: `OAI.Probability.ClassicalON.Main`, `theorem_names`: `["OAI.ClassicalON.main"]`, and permitted axioms `["propext", "Quot.sound", "Classical.choice"]`.
   - Candidate solution module: `lean/OAI/Probability/ClassicalON/Main.lean` (LEN 2,050 bytes, SHA-256 `0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a`). Role: Solution proof module. Imports `OAI.Probability.ClassicalON.BlockReduction` and contains proof script text `theorem main : ExponentialDecay := by ...` without top-level `sorry`.

2. **Boundary Condition & Model Repair:**
   Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 391–395) and `tests/test_source_jet_finite_certificates.py` (Test 10). The formalized model specifies classical 2D $O(n)$ ($n \ge 3$) spin correlation decay on finite square-lattice subgraphs with **FREE boundary conditions** (`structure LatticeGraph`), strictly refuting the prior periodic boundary assertion. Furthermore, `lean/docs/215.md` explicitly specifies:
   > *"For each interaction bound $\beta>0$, constants $A$ and $m>0$ work for every finite square-lattice subgraph with free boundary and nonnegative edge strengths at most $\beta$: the correlation between sites $x,y$ is at most $Ae^{-m|x-y|}$. The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included."*
   The infinite-volume limit and $O(4)$ spectral gap claim are explicitly disclaimed upstream.

3. **Supersession of Inaccurate Declaration Claims:**
   Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 396–400) and `research/YM_CONSTRUCTION_DEFECT_CORRECTION_LEDGER.md` (CDC-050R2). Formally supersedes the phantom declaration name `lattice_spin_decay_2d` (which does not exist upstream). Establishes that the comparator challenge theorem is `OAI.ClassicalON.main : ExponentialDecay := by sorry` in `ClassicalON.lean`, and candidate solution theorem is `OAI.ClassicalON.main` in `Main.lean`.

4. **Proof Status Evaluation (`UNVERIFIED_UPSTREAM_PROOF_CODE`):**
   Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 401–405) and `research/YM_CONSTRUCTION_DEFECT_CORRECTION_LEDGER.md` (CDC-050R2). Clarified that the presence of `sorry` in `lean/ComparatorChallenges/ClassicalON.lean` is a benchmark challenge placeholder, not proof of absent solution code. Demonstrates that candidate solution module `Main.lean` contains proof text without `sorry`, but because governance prohibits running untrusted downloaded code and no local kernel-check build receipt is verified at commit `fd4aeeb2...`, the proof status is properly classified as **`UNVERIFIED_UPSTREAM_PROOF_CODE`**.

5. **Inspected Scope vs. Nonexistence Theorem:**
   Inspected `research/YM_015F_R_OPERATION_SOURCE_AUDIT_039.md` (lines 406–413). Confirms that direct inspection across the 4 primary artifacts yields a search-negative finding (zero declarations for continuum QFT construction, Osterwalder–Schrader axioms OS0–OS4, non-Gaussianity, or 4D Yang–Mills theory), which is carefully distinguished from an unproved universal assertion of repo-wide nonexistence across all files in `openai/math`.

6. **Negative Evidence Register Integrity:**
   Inspected `NEGATIVE_EVIDENCE_REGISTER.md`:
   - Verified registration of `## YM-050R2: OpenAI Family 215 primary-source provenance and proof status repair` (`NEG-YM-050R2-FAMILY215-PROVENANCE`), classified as `[METHOD_SPECIFIC_OBSTRUCTION]` / `[UNVERIFIED_CANDIDATE_PREPRINT]`.
   - Verified historical amendment note under `## YM-050: OpenAI Family 215 unverified candidate and criticality mismatch` (`NEG-YM-050-FAMILY215`) at item 6:
     `6. **[CHALLENGED_AND_SUPERSEDED IN YM-050R2]:** The path math/lean/docs/215.md, periodic boundary condition, and declaration head lattice_spin_decay_2d cited in this historical entry are superseded by exact upstream commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, path lean/docs/215.md, free-boundary condition, comparator OAI.ClassicalON.main : ExponentialDecay := by sorry, and candidate solution module lean/OAI/Probability/ClassicalON/Main.lean (see entry NEG-YM-050R2-FAMILY215-PROVENANCE).`
   - Git diff between candidate `6328f403af0e32fe80c5d4241213f0c472704d58` and baseline `6d1e46fc1a9f974c3855320fe775c9e26c9dfe13` confirms strictly additive changes (+14 lines, 0 deletions); zero historical negative evidence was deleted or weakened.

7. **Deterministic Certificates & Full Test Suite:**
   - Inspected `tests/test_source_jet_finite_certificates.py`: all 10 tests pass deterministically (including Test 10 `test_family215_primary_source_provenance_and_scope_certificate`, verifying commit length, falsifying `math/lean` prefix, confirming `FREE_BOUNDARY_FINITE_SUBGRAPHS`, falsifying `lattice_spin_decay_2d`, and asserting zero continuum/OS/YM declarations).
   - Inspected `tests/test_governance_v406r3_adoption.py`: all 18 tests pass; Test 14 whitelist contains `bea824858bad92b6d092520f89e19d532cd9b6ed28fef4d743183e63f0a0e9d2` at line 260.
   - Closed-world scientific tree hash computed via `compute_closed_world_scientific_tree_hash(Path('.'))` over exactly 158 canonical files evaluates to:
     `bea824858bad92b6d092520f89e19d532cd9b6ed28fef4d743183e63f0a0e9d2`.
   - Executed full test suite (`python -m pytest`): **440 passed in 6.23s** with zero failures, zero errors, zero warnings (exit code 0).

---

## Confirmation of 12 Hard Gates (PROJECT_BOUND_READINESS_RULE.yaml)

| Gate | Name | Requirement | Finding | Status |
|---|---|---|---|---|
| 1 | `candidate_frozen` | Exact candidate commit SHA is frozen in Git and recorded in state | Candidate SHA is `6328f403af0e32fe80c5d4241213f0c472704d58` (child of baseline `6d1e46fc1a9f974c3855320fe775c9e26c9dfe13`). Clean working tree. | **PASS** |
| 2 | `candidate_bound_review` | Review is strictly bound to candidate SHA | Review receipt `verification/raw/YM-050R2_E4_RAW_20261009.md` explicitly binds SHA `6328f403af0e32fe80c5d4241213f0c472704d58`; SHA-256 digest `eaf7af7a89fdc43383da6ce2bbcd550ea4fb0b2824abda64597100feed00137c` verified. | **PASS** |
| 3 | `scientific_review_pass` | Review verdict is `INTEGRITY_PASS` | Review verdict is `INTEGRITY_PASS` across all 10 mandatory review criteria. | **PASS** |
| 4 | `negative_evidence_preserved` | Negative evidence registered; zero historical deletions | `NEG-YM-050R2-FAMILY215-PROVENANCE` registered; `NEG-YM-050-FAMILY215` amended; Git diff confirms +14 lines, 0 deletions. | **PASS** |
| 5 | `dependencies_satisfied` | All precursor tasks completed and accepted | Precursor tasks `YM-050`, `YM-050R`, `YM-049`, and `YM-015F-JET-002A` completed and accepted in `PROJECT_STATE.yaml`. | **PASS** |
| 6 | `scientific_tree_identity` | Tree hash matches verified canonical hash | Closed-world hash matches `bea824858bad92b6d092520f89e19d532cd9b6ed28fef4d743183e63f0a0e9d2` (158 canonical files); present on Test 14 whitelist. | **PASS** |
| 7 | `state_revision_freshness` | State revision increments monotonically | Current state revision is 51; next state revision will be 52. | **PASS** |
| 8 | `no_unresolved_mandatory_blocker` | Zero unresolved mandatory blockers within bounded scope | Zero mandatory blockers exist within the bounded YM-050R2 repair scope. | **PASS** |
| 9 | `goal_complete_false_invariant` | `goal_complete` remains `false` | `goal_complete: false` verified in `PROJECT_STATE.yaml`; invariant preserved. | **PASS** |
| 10 | `clay_problem_unsolved_invariant` | `clay_problem` remains `OPEN_AND_UNSOLVED` | `clay_problem: OPEN_AND_UNSOLVED` verified in `PROJECT_STATE.yaml`; invariant preserved. | **PASS** |
| 11 | `scientific_acceptance_authority_separation` | Writer != Reviewer != Acceptor (`IND1_DISTINCT_PROCESS_ACCEPTOR`) | Writer (`00ffe8a3...`) != Reviewer E4 (`e436ee6a...`) != Acceptor (`799643cd...`). Distinct processes confirmed. | **PASS** |
| 12 | `regression_protection_for_consequential_defects` | Durable regression tests protect against defects | Test 10 in `tests/test_source_jet_finite_certificates.py` and full suite (440 tests) pass deterministically. | **PASS** |

---

## Scope, Limitations, and Authorization

Bounded technical acceptance is granted for the YM-050R2 primary-source provenance, free-boundary repair, locator correction, and proof status classification of OpenAI Family 215.

Constitutional and epistemic invariants remain strictly intact:
- `goal_complete` = `false`
- `clay_problem` = `OPEN_AND_UNSOLVED`
- `P3` = `OPEN`
- `E-CROSSOVER` = `OPEN`
- `E-UV-FLOWED` = `PARTIAL_PROGRESS`
- `YM-016` = `BLOCKED`
- `STRUCTURAL_NO_GO_COUNT` = `0`

No continuum QFT construction, Osterwalder–Schrader axioms, non-Gaussianity, or 4D Yang–Mills theorems are claimed or imported. The transfer candidate remains classified as `UNVERIFIED_CANDIDATE_PREPRINT` and `METHOD_SPECIFIC_OBSTRUCTION`. Allowed transfer conclusion is strictly `None`; zero DAG edges close.

Root alone is authorized to bind unchanged candidate `6328f403af0e32fe80c5d4241213f0c472704d58`, E4 receipt digest `eaf7af7a89fdc43383da6ce2bbcd550ea4fb0b2824abda64597100feed00137c`, save this technical acceptance receipt to `verification/YM-050R2_TECHNICAL_ACCEPTANCE.md`, and advance `PROJECT_STATE.yaml` revision from 51 to 52. Acceptor operated strictly read-only per governance separation.

---

## Final Decision

**FINAL DECISION: TECHNICAL_ACCEPTANCE_GRANTED**  
**Acceptor Conversation ID:** `799643cd-211f-480c-97ce-cf79fbc53153`  
**Execution Authority Separation:** `IND1_DISTINCT_PROCESS_ACCEPTOR`
