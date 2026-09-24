# Portable Autonomous Scientific Repair & Acceptance-Authority Amendment (v1.1)

- **AMENDMENT_ID:** `GOV-AMEND-AUTONOMOUS-REPAIR-v1.1`
- **APPLICABILITY:** Project-Neutral Scientific Research Operating Systems (`Yang–Mills`, `Riemann Hypothesis`, `Navier–Stokes`, `Cosmic Seasons`, and related repositories)
- **ORIGIN_TASK:** `YM-GOV-014`
- **EFFECTIVE_DATE:** 2026-09-24

---

## 1. Operating Principle

**The human owner determines research direction and authorizes consequential external actions. The autonomous research system identifies, repairs, verifies, and records bounded scientific work.**

Routine mathematical, computational, or epistemic defects discovered during audit must **never** park a task in `AWAITING_HUMAN_OWNER_ACCEPTANCE`. Instead, scientific defects must automatically trigger bounded autonomous repair (`REPAIR_REQUIRED -> BOUNDED_REPAIR -> REVERIFICATION -> INDEPENDENT_SCIENTIFIC_REVIEW`).

---

## 2. Canonical State Definitions

### 2.1 Routine Scientific Task States

$$\texttt{CANDIDATE} \longrightarrow \texttt{INDEPENDENT\_SCIENTIFIC\_REVIEW} \longrightarrow \begin{cases} \texttt{SCIENTIFICALLY\_ACCEPTED} \\ \texttt{REPAIR\_REQUIRED} \\ \texttt{REVIEW\_HOLD} \end{cases}$$

If `REPAIR_REQUIRED` occurs:

$$\texttt{REPAIR\_REQUIRED} \longrightarrow \texttt{BOUNDED\_REPAIR} \longrightarrow \texttt{REVERIFICATION} \longrightarrow \texttt{INDEPENDENT\_SCIENTIFIC\_REVIEW}$$

1. **`SCIENTIFICALLY_ACCEPTED`** (including `SCIENTIFICALLY_ACCEPTED (WITH_REGULATED_SCOPE)`):
   - Assigned when an independent scientific review returns `INTEGRITY_PASS` (or `INTEGRITY_PASS_WITH_LIMITATIONS` where all limitations are explicitly reflected in the claim's governed scope), `candidate_sha == reviewed_sha` (or only declared non-scientific metadata changed post-review), and zero disqualifying defects remain.
   - Does not require human-owner sign-off for bounded internal research increments.

2. **`REPAIR_REQUIRED`**:
   - Assigned automatically whenever an audit or verification pass identifies any mathematical conflation, scope promotion, unit fabrication, circularity, or unproven transfer.
   - Prohibits routing to human-owner acceptance; mandates immediate transition to `BOUNDED_REPAIR`.

3. **`REVIEW_HOLD`** (or `SCIENTIFIC_REVIEW_HOLD`):
   - Assigned when a downstream task depends on an upstream bridge, lemma, or theorem that has not yet been established, or when an overclaimed global synthesis is quarantined pending foundational prerequisite reconstruction.

4. **`HUMAN_OWNER_DECISION_REQUIRED`**:
   - Reserved **exclusively** for the six consequential owner-authority actions:
     1. Changing the project mission or target problem;
     2. Claiming `GOAL_COMPLETE` or a solution to a major prize/target problem (e.g., Clay Millennium Problem);
     3. External publication, submission, or public release;
     4. Destructive deletion of historical records or quarantine history;
     5. Modifying another repository (`Riemann`, `Navier–Stokes`, `Cosmic Seasons`, etc.);
     6. Unbounded expenditure of external resources or credentials.

---

## 3. Candidate-Bound Review Invariant

An independent scientific review is valid for `SCIENTIFICALLY_ACCEPTED` **if and only if**:
1. `review_verdict` $\in \{\texttt{INTEGRITY\_PASS}, \texttt{INTEGRITY\_PASS\_WITH\_LIMITATIONS}\}$ (with all limitations reflected in claim status);
2. `candidate_sha == reviewed_sha` (or post-review changes are strictly restricted to declared non-scientific provenance/administrative metadata);
3. No disqualifying finding (`MATHEMATICAL_CONFLATION`, `SCOPE_PROMOTION`, `UNIT_FABRICATION`, `CIRCULARITY`, `UNPROVEN_TRANSFER`) is present.

---

## 4. Portable Cross-Project Adoption Checklist

When adopting this amendment into `Riemann`, `Navier–Stokes`, `Cosmic Seasons`, or any new scientific research repository (to be executed only within that repository's authorized session):

- [ ] **Step 1 (Copy Amendment):** Copy `PORTABLE_AUTONOMOUS_REPAIR_AMENDMENT_v1.1.md` into the target repository's `governance/` directory.
- [ ] **Step 2 (State Machine Update):** Register `SCIENTIFICALLY_ACCEPTED`, `REPAIR_REQUIRED`, `BOUNDED_REPAIR`, `REVERIFICATION`, `REVIEW_HOLD`, and `HUMAN_OWNER_DECISION_REQUIRED` in the repository's governance validator.
- [ ] **Step 3 (Deprecate Routine Owner Gating):** Replace any occurrence of `AWAITING_HUMAN_OWNER_ACCEPTANCE` on defective or routine tasks with `REPAIR_REQUIRED` (if actionable) or `REVIEW_HOLD` (if blocked by upstream dependencies).
- [ ] **Step 4 (Enforce Candidate-Bound SHA Check):** Add automated unit test asserting that acceptance fails whenever `candidate_sha != reviewed_sha` or when disqualifying audit findings exist.
- [ ] **Step 5 (Enforce Global Completion Gate):** Add automated unit test asserting that `GOAL_COMPLETE = false` whenever any required proof-dependency edge or sub-goal is not `PROVED`.
