# Derived Independent Verification Summary — `YM-011-PLAQUETTE-EXP-R2`

- **REVIEW_ID:** `EVD-YM-011-PLAQUETTE-EXP-R2-E4`
- **REVIEWER_SUBAGENT_ID:** `95e6eb5a-6c28-4db1-8190-8f708e90ccab` (`fresh-blind-research-subagent-YM-011-PLAQUETTE-EXP-R2`)
- **CANDIDATE_SHA:** `9ed117fe58a39540134fb2fb2bac3691d747b884`
- **REVIEWED_SHA:** `9ed117fe58a39540134fb2fb2bac3691d747b884`
- **SCIENTIFIC_TREE_HASH:** `18c319312f7afcd3fc4e93afa898de78b5c88500c4eee1fa04bdd08b2c08b77d`
- **RAW_RECEIPT_PATH:** `verification/raw/YM-011-PLAQUETTE-EXP-R2_E4_RAW_20260925.md`
- **VERDICT:** `INTEGRITY_PASS`

## Summary of Verified Mathematical Dispositions
1. **`YM-011-PLAQUETTE-EXP-R2` (`Group-Specific Plaquette-Energy Range, Proof of Odd-N Minimizer, and Expectation-Positivity Audit`):** `SCIENTIFICALLY_ACCEPTED` via `REPAIR_REQUIRED -> BOUNDED_REPAIR -> REVERIFICATION -> INDEPENDENT_SCIENTIFIC_REVIEW -> SCIENTIFICALLY_ACCEPTED`.
2. **Sharp Group-Theoretic Ranges & Odd-$N$ Variational Proof:**
   - Variational optimization of $q_N(U) = \frac{1}{N}\sum_{j=1}^N \cos\theta_j$ subject to $\sum \theta_j \equiv 0 \pmod{2\pi}$ rigorously established via shifted coordinates $\theta_j = \pi - \phi_j$, concavity of $\cos$ on $[-\pi/2, \pi/2]$, Jensen's inequality, and admissibility of $e^{i\pi(N-1)/N} I_N \in SU(N)$ for odd $N$.
   - $SU(2): h_{\max} = 2.0$ (attained at $-I_2$).
   - $SU(3): h_{\max} = 1 + \cos(\pi/3) = 1.5$ (attained at $e^{i 2\pi/3} I_3$).
   - $SU(4): h_{\max} = 2.0$ (attained at $-I_4$).
   - $SU(5): h_{\max} = 1 + \cos(\pi/5) \approx 1.809017$ (attained at $e^{i 4\pi/5} I_5$).
3. **Three-Range Architectural Separation:**
   - `CONFIGURATION_RANGE(N) = [0, h_max(N)]`
   - `EXPECTATION_RANGE(N) = [0, h_max(N)]`: Enforces that expectation values cannot exceed configuration supremum. Specifically, $e_{\mathrm{plaq}} = 2.0$ is recognized and tested as impossible for $SU(3)$ under any probability measure.
   - `UNIVERSAL_ALL_N_RANGE = [0, 2]`: Universal coarse bound for all $N \ge 2$.
4. **Lie-Laplacian Positivity Derivation & Epistemic Classification:**
   - First-principles derivation via integration by parts: $\langle \Delta_\ell S_W \rangle_{\mu_\beta} = \sum_{a=1}^{N^2-1} \langle (\partial_\ell^a S_W)^2 \rangle_{\mu_\beta} \ge 0 \implies \sum_{p \ni \ell} \langle \operatorname{Re}\operatorname{Tr} U_p \rangle \ge 0$.
   - Classification: `PROVED_FOR_WILSON_GIBBS_MEASURE` for summed plaquettes touching link $\ell$; `PROVED_ONLY_AFTER_ADDITIONAL_SYMMETRY` for single plaquettes; `FALSE` as a configuration-wise bound.
   - Fully decoupled from Theorems $T1, T2$ and Lemma $L1$.
5. **Verified Theorems:**
   - **`YM-011-PLAQUETTE-EXP-T1`:** $\langle |\Delta_{\mathrm{tan}}(C_1)| \rangle_{\mu_0} \le 4(d-1)\sqrt{N} \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0)$ on isotropic periodic $\Lambda_0$ ($C(d,N) = 4(d-1)\sqrt{N}$, and $C_{\mathrm{sharp}}(d,2) = 4(d-1)$ for $SU(2)$), valid for any $e_p \in [0, h_{\max}(N)]$.
   - **`YM-011-PLAQUETTE-EXP-T2`:** Exact derivative identity $-\partial_\beta \ln Z_{\Lambda_0}(\beta) = |P_+| e_{\mathrm{plaq}}(\beta, \Lambda_0)$ and variance monotonicity $-\partial_\beta e_{\mathrm{plaq}} = \operatorname{Var}(H)/|P_+| \ge 0$.
   - **`YM-011-PLAQUETTE-EXP-L1`:** Volume-uniform bound $e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0,\pi]} (8r^2 + \frac{2}{(d-1)\beta}\ln(1/v_N(r))) = O(\frac{\ln\beta}{\beta})$.
6. **Preserved Negative Evidence Disclosures:**
   - `NEG-YM-011-PLAQ-1`: Toron singular strata obstructing naive Morse–Bott Laplace asymptotics.
   - `NEG-YM-011-PLAQ-2`: False $[0, 1]$ configuration range and root-cause disclosure of initial review miss.
   - `NEG-YM-011-PLAQ-3`: Group-specific plaquette admissibility inconsistency and verification separation.
7. **Authorized Next Task:** `YM-011-TREE-GAUGE` (`Maximal Spanning-Tree Gauge Fixing and Co-Tree Plaquette Coordinate Map`).
8. **Global Invariants:** `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `YM-006` through `YM-010 = SCIENTIFIC_REVIEW_HOLD`, original `YM-011` continuum proposal `NOT AUTHORIZED`.
