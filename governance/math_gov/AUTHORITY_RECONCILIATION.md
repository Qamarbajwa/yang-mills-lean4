# AUTHORITY RECONCILIATION & STRICT THREE-AUTHORITY CONFORMANCE

**Date:** 2026-11-10  
**Status:** `CONFORMANT_WITH_CANONICAL_THREE_AUTHORITY_MODEL`  
**Governing Standard:** Universal Governance Minimal (UGM) v4.1.0-r3, Section 0  

---

## 1. The Strict Three-Authority Model

Under the constitution of this research workspace, project-level active authority is restricted strictly and exhaustively to exactly three files:

1. **`governance/GOVERNANCE.md`:** Procedural and operational rules governing all research tasks, verification requirements, and role separations.
2. **`governance/PROJECT_DIRECTION.md`:** Strategic scientific purpose, approved mathematical problems, and material research boundaries.
3. **`governance/PROJECT_STATE.yaml`:** Live epistemic state machine, active revision counters, closed/open edge statuses, and referee verification gates.

**Fundamental Invariant:** All other files—including evidence ledgers, task envelopes, test scripts, Python modules, prompts, transcripts, and external governance adoption candidates—are **supporting artifacts**, never a fourth active authority.

---

## 2. Rejection of Undeclared "Supreme Mathematical Constitution"

In candidate MATH-GOV materials, phrases such as "Supreme Mathematical Constitution" or "Self-Executing Universal Governance" have been suggested. This document establishes:

1. **No Fourth Authority:**
   - Candidate MATH-GOV v0.6 files located in `governance/math_gov/` are **subordinate domain-specific overlays** and **reference templates**.
   - They possess **zero independent legal authority** to override, alter, weaken, or replace the canonical three authorities.
2. **Subordination Hierarchy:**
   - Canonical `governance/GOVERNANCE.md` takes absolute precedence.
   - Any conflict between MATH-GOV candidate proposals and Canonical UGM rules resolves in favor of Canonical UGM (`BLOCKED_CONFLICT`), requiring explicit human project owner intervention.
3. **Non-Authoritative Status of Candidate Templates:**
   - Files stored in `governance/math_gov/reference_templates/` (such as candidate `GOVERNANCE.md`, `PROJECT_DIRECTION.md`, and `PROJECT_STATE.yaml`) are frozen reference archetypes. They are not loaded by runtime governance tools as active authority.
