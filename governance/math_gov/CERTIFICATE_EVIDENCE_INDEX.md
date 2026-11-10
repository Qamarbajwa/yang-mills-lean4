# MATHEMATICAL CERTIFICATE EVIDENCE INDEX & DOWNGRADE RECORD

**Date:** 2026-11-10  
**Status:** `AUDITED_AND_CALIBRATED`  
**Governing Standard:** Master Directive Phase C Step 10, Rule H14, Rule H15  

---

## 1. Inventory of Mathematical Certificates

| Certificate Identifier | Mathematical Scope | Verification Mechanism | Code / Test Anchor | Directed-Rounding / Precision | Verification Status |
|---|---|---|---|---|---|
| **CERT-YM011-DYADIC** | Dyadic Free Energy Partition | Exact Rational (`Fraction`) | `tests/test_ym_011_dyadic_free_energy.py` | Exact $\mathbb{Q}$ | `VERIFIED_EXACT_RATIONAL` |
| **CERT-YM011-PLAQUETTE** | Plaquette Expectation Bounds | Exact Rational (`Fraction`) | `tests/test_ym_011_plaquette_exp.py` | Exact $\mathbb{Q}$ | `VERIFIED_EXACT_RATIONAL` |
| **CERT-YM011-TORON** | Quartic Toron & Brascamp-Lieb | Exact Rational (`Fraction`) | `tests/test_ym_011_toron_quartic_and_brascamp_lieb.py` | Exact $\mathbb{Q}$ | `VERIFIED_EXACT_RATIONAL` |
| **CERT-YM013-CHOLESKY** | SDP Dual Slack Matrix Positivity | Outward Interval $LDL^T$ | `src/ymmg/loop_bootstrap.py` | Directed Interval Cholesky | `VERIFIED_LOCAL_LDL_T` |
| **CERT-YM016-SOURCE-JET** | Source-Jet Jet-Factor Bounds | Exact Rational (`Fraction`) | `tests/test_source_jet_finite_certificates.py` | Exact $\mathbb{Q}$ | `VERIFIED_EXACT_RATIONAL` |
| **CERT-YM016-TERMINAL** | Terminal Sector Finite Certificate | Exact Rational (`Fraction`) | `tests/test_terminal_sector_finite_certificate.py` | Exact $\mathbb{Q}$ | `VERIFIED_EXACT_RATIONAL` |
| **CERT-MATHGOV-10STEP** | Candidate 10-Step Plan Enclosure | Illustrative Model JSON | `governance/math_gov/examples/ten_tasks.json` | N/A (Symbolic / Structural) | **`REPORTED_UNVERIFIED`** |

---

## 2. Formal Downgrade of Candidate "10-Step Interval Certificate"

1. **Audit Finding:**
   - In the candidate MATH-GOV v0.6 package (`ten_tasks.json` and `five_of_ten.json`), 10 sequential tasks and steps are specified with structural dependencies, obligations, and illustrative status markers.
   - However, executable floating-point directed-rounding interval arithmetic code (e.g. `mpmath.iv` or hardware-level IEEE 754 outward rounding modes) is **not bundled** for these 10 candidate tasks in the candidate archive.
2. **Mandatory Epistemic Action (Directive Step 10):**
   - The status of the candidate 10-step sequence is formally downgraded from any claim of `CERTIFIED` to:
     **`REPORTED_UNVERIFIED`**
   - The historical record of the 10-task structure in `examples/ten_tasks.json` is preserved without deletion for architectural review.
