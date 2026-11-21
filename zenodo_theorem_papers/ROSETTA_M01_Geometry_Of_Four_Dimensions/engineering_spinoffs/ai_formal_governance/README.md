# AI Formal Governance Sandbox: Zero-Trust Premise A -> Verdict Harness

**Neuro-Symbolic Automated Compliance Engine**  
**Author:** Qamar Munawer  
**Affiliation:** Brandenburg University of Technology Cottbus-Senftenberg  
**Methodology Note:** ai is being used as a tool  
**Epistemic Status:** `status: verified-finite deterministic formal governance`

---

## 1. Motivation and Problem Statement

When generative AI and LLM agents are deployed to review legal documents, municipal building plans (Development Control Regulations / FAR / fire escape compliance), or scientific research papers, standard language generation introduces dangerous failure modes:
1. **Hallucinated Waivers:** Inventing non-existent regulatory exemptions.
2. **Ignored Statutory Limits:** Approving plans with inadequate fire exit widths or excessive building heights.
3. **Overclaimed Mathematical Proofs:** Declaring open Millennium Problems solved when only finite approximations were tested.

This toolkit implements the **Bridge vs. Train** architecture derived from our formal Lean 4 verification research.

---

## 2. Architecture: The Bridge vs. Train Pattern

```
┌──────────────────────────────────────┐
│       THE TRAIN (Premise A)          │
│ - Strictly typed, immutable inputs   │
│ - Extracted from CAD/BIM or data     │
│ - Cryptographically hashed (SHA-256) │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│     THE BRIDGE (Symbolic Kernel)     │
│ - Zero-Axiom Deterministic Rules     │
│ - No probabilistic natural language  │
│ - Direct mathematical inequality chk │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       THE VERDICT (Audit Trail)      │
│ - PROVEN_COMPLIANT                   │
│ - PROVEN_VIOLATION                   │
│ - REJECTED_EPISTEMIC_VIOLATION       │
└──────────────────────────────────────┘
```

---

## 3. Implemented Bridges

1. **ZeroTrustMunicipalBridge:**
   - **Floor Area Ratio (FAR):** Verifies that built-up area does not exceed statutory zoning limits.
   - **Fire Egress Width:** Enforces minimum exit widths based on occupant load ($W \ge \max(1.20 \text{ m}, N \times 0.005 \text{ m})$).
   - **Structural Span-to-Depth Ratio:** Verifies deflection safety limits ($L/d \le 20.0$).
   - **Boundary Setbacks:** Checks mandatory front, rear, and side clearances.

2. **ZeroTrustScientificBridge:**
   - **Epistemic Integrity Lock:** Strictly rejects any claim that an open Millennium Problem is unconditionally settled.
   - **Standard Axioms Enforcer:** Guarantees that formal proofs rely only on standard Lean 4 axioms (`propext`, `Classical.choice`, `Quot.sound`) with zero custom axioms.
   - **Finite Metric Coercivity:** Checks whether verified finite spectral gaps or bounds exceed their non-zero positive floor.

---

## 4. Usage

Run the benchmark and export the audit receipt:
```bash
python engineering_spinoffs/ai_formal_governance/premise_a_bridge_harness.py
```

Run automated unit tests:
```bash
python -m unittest engineering_spinoffs/ai_formal_governance/test_ai_formal_governance.py
```
