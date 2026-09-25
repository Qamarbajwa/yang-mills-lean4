# Derived Independent Verification Summary — `YM-011-PLAQUETTE-EXP-R1`

- **REVIEW_ID:** `EVD-YM-011-PLAQUETTE-EXP-R1-E4`
- **REVIEWER_SUBAGENT_ID:** `09be6d81-b52b-43f9-b0a4-b8d22fc5c846` (`fresh-blind-research-subagent-YM-011-PLAQUETTE-EXP-R1`)
- **CANDIDATE_SHA:** `5553891059c6501c022e716016feac38c475cc4a`
- **REVIEWED_SHA:** `5553891059c6501c022e716016feac38c475cc4a`
- **SCIENTIFIC_TREE_HASH:** `0e96fcdacf45c4f63721e644ad81810b7fc360df5abc90ffa2391fbe07712326`
- **RAW_RECEIPT_PATH:** `verification/raw/YM-011-PLAQUETTE-EXP-R1_E4_RAW_20260925.md`
- **VERDICT:** `INTEGRITY_PASS`

## Summary of Verified Mathematical Dispositions
1. **`YM-011-PLAQUETTE-EXP-R1` (`Repaired Plaquette-Energy Range [0, 2] and Expectation Reduction`):** `SCIENTIFICALLY_ACCEPTED` via `REPAIR_REQUIRED -> BOUNDED_REPAIR -> REVERIFICATION -> INDEPENDENT_SCIENTIFIC_REVIEW -> SCIENTIFICALLY_ACCEPTED`.
2. **Repaired Plaquette Energy Range $[0, 2]$:**
   - For all $SU(N)$ ($N \ge 2$), $h_p(U) = 1 - \frac{1}{N}\operatorname{Re}\operatorname{Tr}(U_p) \in [0, 2]$ and $e_{\mathrm{plaq}}(\beta, \Lambda_0) \in [0, 2]$.
   - For even $N$: $-I_N \in SU(N) \implies \max h_p = 2.0$ (e.g. $U_p = -I_2$ in $SU(2)$).
   - For odd $N$: $-I_N \notin SU(N) \implies \max h_p = 1 + \cos(\pi/N) < 2.0$ (e.g. $1.5$ in $SU(3)$).
3. **Verified Theorems:**
   - **`YM-011-PLAQUETTE-EXP-T1`:** Unconditional expectation reduction $\langle |\Delta_{\mathrm{tan}}(C_1)| \rangle_{\mu_0} \le 4(d-1)\sqrt{N} \, |C_1|_{\Lambda_1} \, e_{\mathrm{plaq}}(\beta, \Lambda_0)$ on the isotropic periodic torus $\Lambda_0 = (a\mathbb{Z}/2La\mathbb{Z})^d$ ($C(d,N) = 4(d-1)\sqrt{N}$, and $C_{\mathrm{sharp}}(d,2) = 4(d-1)$ for $SU(2)$), proved strictly invariant under the range repair (depending solely on $\|U_p - I_N\|_{\mathrm{HS}}^2 = 2N h_p(U)$ and Cauchy–Schwarz on $L^2$).
   - **`YM-011-PLAQUETTE-EXP-T2`:** Exact partition-function derivative identity $-\partial_\beta \ln Z_{\Lambda_0}(\beta) = \langle H \rangle_{\mu_0} = |P_+(\Lambda_0)| e_{\mathrm{plaq}}(\beta, \Lambda_0)$ with $e_{\mathrm{plaq}}(\beta, \Lambda_0) \in [0, 2]$; Lie-Laplacian positivity contextualized as an expectation property under unperturbed translation invariance rather than a configuration-wise algebraic range.
   - **`YM-011-PLAQUETTE-EXP-L1`:** Elementary volume-uniform entropy–energy bound $e_{\mathrm{plaq}}(\beta, \Lambda_0) \le \inf_{r \in (0,\pi]} (8r^2 + \frac{2}{(d-1)\beta}\ln(1/v_N(r))) = O(\frac{\ln\beta}{\beta})$.
4. **Preserved Negative Results:**
   - `NEG-YM-011-PLAQ-1`: Toron singular strata $\mathcal{M}_{\mathrm{flat}} \cong T^d / S_N$ and jumping stabilizer dimension obstructing naive Morse–Bott Laplace asymptotics on the un-gauge-fixed periodic torus.
   - `NEG-YM-011-PLAQ-2`: False configuration-wise range $[0, 1]$, counterexamples $U_p = \pm I_N$, and root cause disclosure of previous review miss.
5. **Authorized Next Task:** `YM-011-TREE-GAUGE` (`Maximal Spanning-Tree Gauge Fixing and Co-Tree Plaquette Coordinate Map`).
6. **Global Invariants:** `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, `YM-006` through `YM-010 = SCIENTIFIC_REVIEW_HOLD`, original `YM-011` continuum proposal `NOT AUTHORIZED`.
