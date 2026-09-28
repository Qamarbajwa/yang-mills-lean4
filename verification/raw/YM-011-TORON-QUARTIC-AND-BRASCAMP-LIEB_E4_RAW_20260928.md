# Independent Adversarial E4 Mathematical & Governance Audit Report: `YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB`

- **Task ID:** `YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB` (Periodic-Torus Uniform Plaquette Bound Audit, Toron Quartic Commutator Variety, Brascamp–Lieb Applicability, and Stratified Laplace Resolution of Fixed-Volume $O_L(1/\beta)$)
- **Reviewer Role:** Fresh, Blind, Independent Research Subagent (`E4` Adversarial Mathematical & Governance Auditor)
- **Reviewer Conversation ID:** `e0458aff-ded7-42e2-b0e6-657daff42dbe`
- **Audited Candidate Commit SHA:** `de11450f23497fc444571e6bdcba92a962535170`
- **Baseline Commit SHA Verified:** `9aec40b170415ba94fee65cb8d27df76ecd4aeaf` (`BASELINE_LINEAGE_VERIFIED`, `transition_class = SAME`)
- **Audited `SCIENTIFIC_TREE_HASH`:** `0ad88e618086d4278b7dcf8141baed940d23f7ec1ccc33f9b86670aac072c399` (`102` canonical scientific files in `SCIENTIFIC_FINGERPRINT_MANIFEST`)
- **Regression Test Verification:** `356 passed in 5.54s` (`$env:PYTHONPATH="."; python -m pytest -q`)
- **Global Project Invariants:** `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`
- **Final Audit Verdict:** **`INTEGRITY_PASS_WITH_LIMITATIONS`**

---

## 1. First-Principles Verification of the 11 Mandatory Review Items (Section 20)

### Item 1: Quartic Zero-Set Characterization (`YM-011-TORON-Q1`) — **VERIFIED**
1. **Exact Zero Locus:** For $Q(X_1, \dots, X_d) = \sum_{1 \le \mu < \nu \le d} \|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2$ on $\mathfrak{su}(N)^d$, since $\|[X_\mu, X_\nu]\|_{\mathrm{HS}}^2 = \operatorname{Tr}([X_\mu, X_\nu]^\dagger [X_\mu, X_\nu]) \ge 0$, $Q(X) = 0$ if and only if $[X_\mu, X_\nu] = 0$ for all $1 \le \mu < \nu \le d$.
2. **Falsification of Global Coercivity $Q(X) \ge c\|X\|_{\mathrm{HS}}^4$:** Explicitly falsified along any non-zero Cartan tuple $(H_1, \dots, H_d) \in \mathfrak{t}_{\max}^d \setminus \{0\}$, where $[H_\mu, H_\nu] = 0 \implies Q(H) = 0$ while $\|H\|_{\mathrm{HS}}^4 > 0$.
3. **Simultaneous Diagonalizability & Dimensions:** Every commuting tuple $(X_1, \dots, X_d) \in \mathfrak{C}_d(\mathfrak{su}(N))$ of skew-Hermitian matrices is simultaneously unitarily diagonalizable by $g \in SU(N)$ into $\mathfrak{t}_{\max}^d$. The adjoint sweep map $\Psi : (SU(N)/T_{\max}) \times \mathfrak{t}_{\max}^d \to \mathfrak{C}_d(\mathfrak{su}(N))$ is surjective and an $S_N$-covering ($|S_N| = N!$) over the dense open regular stratum $\mathfrak{C}_d^{\mathrm{reg}}(\mathfrak{su}(N))$. This yields:
   - $\dim_{\mathbb{R}} \mathfrak{C}_d(\mathfrak{su}(N)) = \dim(SU(N)/T_{\max}) + d\dim \mathfrak{t}_{\max} = N(N - 1) + d(N - 1) = (d + N)(N - 1)$;
   - $\dim_{\mathbb{R}}\!\left(\mathfrak{C}_d(\mathfrak{su}(N))/\operatorname{Ad}(SU(N))\right) = \dim_{\mathbb{R}}(\mathfrak{t}_{\max}^d / S_N) = d(N - 1)$;
   - $\operatorname{codim}_{\mathfrak{su}(N)^d} \mathfrak{C}_d(\mathfrak{su}(N)) = d(N^2 - 1) - (d + N)(N - 1) = (d - 1)N(N - 1)$.
4. **Transverse Coercivity via Lagrange's Identity:** For $H \in \mathfrak{t}_{\max}^d \cap \mathfrak{C}_d^{\mathrm{reg}}$ and $Y^\perp \in N_H \mathfrak{C}_d(\mathfrak{su}(N))$ satisfying the orthogonality condition $\sum_{\mu=1}^d \alpha(H_\mu) Y_{\mu,\alpha}^\perp = 0$ on each root space $\alpha \in \Phi_+$, Lagrange's identity gives $\sum_{\mu < \nu} \|[H_\mu, Y_\nu^\perp] - [H_\nu, Y_\mu^\perp]\|_{\mathrm{HS}}^2 = \sum_{\alpha \in \Phi_+} (\sum_{\mu=1}^d \alpha(H_\mu)^2) \sum_{\nu=1}^d |Y_{\nu,\alpha}^\perp|^2 \ge \delta_{\mathrm{sing}}(H)^2 \|Y^\perp\|_{\mathrm{HS}}^2$.

### Item 2: Toron Stratification (`L_{(n_1, \dots, n_k)}`) — **VERIFIED**
For every partition $(n_1, \dots, n_k) \vdash N$ ($\sum_{r=1}^k n_r = N$) with $S = \sum_{r=1}^k n_r^2 \in [N, N^2]$ and stabilizer $L_{(n_1, \dots, n_k)} = S(U(n_1) \times \cdots \times U(n_k))$ ($\dim L = S - 1$), the harmonic tangent space $\mathfrak{su}(N)^d$ of dimension $d(N^2 - 1)$ splits into four orthogonal subspaces:
1. **Levi-center flat directions ($\beta^0$):** $d(k - 1)$
2. **Global conjugation zero modes ($\beta^0$):** $\dim(SU(N)/L_{(n_1,\dots,n_k)}) = (N^2 - 1) - (S - 1) = N^2 - S$
3. **Off-block transverse positive quadratic modes ($\beta^{-1/2}$):** $d(N^2 - S) - (N^2 - S) = (d - 1)(N^2 - S)$
4. **In-block semisimple quartic commutator modes ($\beta^{-1/4}$):** $d \sum_{r=1}^k (n_r^2 - 1) = d(S - k)$

The dimension partition holds identically across all strata (regular $k=N, S=N$; singular non-central $1 < k < N$; central $k=1, S=N^2$):
$$d(k - 1) + (N^2 - S) + (d - 1)(N^2 - S) + d(S - k) = d(S - 1) + d(N^2 - S) = d(N^2 - 1).$$

### Item 3: Quartic Power Counting & Exponent Reduction — **VERIFIED**
Integrating $(d-1)(N^2-S)$ quadratic modes ($\beta^{-1/2}$ each), $d(S-k)$ quartic modes ($\beta^{-1/4}$ each), and $d(k-1) + (N^2-S)$ compact flat/conjugation modes ($\beta^0$ each) yields the exact harmonic exponent:
$$\alpha_{\mathrm{harm}}(n_1, \dots, n_k) = \frac{d-1}{2}(N^2 - S) + \frac{d}{4}(S - k) = \frac{(d-1)N(N-1)}{2} + \frac{1}{4}\sum_{r=1}^k (n_r - 1)\big[d - (d - 2)n_r\big].$$
- Because $-\partial_\beta \ln(\beta^{-1/4}) = \frac{1}{4\beta} < \frac{1}{2\beta}$ (quartic mode) and $-\partial_\beta \ln(\beta^0) = 0 < \frac{1}{2\beta}$ (flat/conjugation mode), replacing quadratic modes by quartic and flat modes **strictly decreases** the weak-coupling $1/\beta$ equipartition coefficient rather than inflating it.
- Across dimensions: $d = 2$ is regular-toron dominated ($\alpha_{\mathrm{harm}}^{\min} = \frac{N(N-1)}{2}$); $d = 3$ is regular-dominated for $N=2$ ($\alpha_{\mathrm{harm}}^{\min} = 2$), marginally resonant at $N=3$ ($\alpha_{\mathrm{harm}}^{\min} = 6$), and central-dominated for $N \ge 4$ ($\alpha_{\mathrm{harm}}^{\min} = \frac{3}{4}(N^2-1)$); $d = 4$ is central-dominated for all $N \ge 2$ (with marginal resonance at $n_r = 2$), giving $\alpha_{\mathrm{harm}}^{\min}(4, N) = N^2 - 1$.

### Item 4: Brascamp–Lieb Hypotheses & Applicability — **VERIFIED**
All 11 required hypothesis fields (`measure`, `coordinate_chart`, `potential_V`, `domain`, `hessian_of_V`, `convexity_region`, `lower_hessian_bound`, `boundary_conditions`, `zero_modes_removed`, `constants`, `volume_dependence`) are audited in Section 4 of `literature/YM-011-TORON-QUARTIC-AND-BRASCAMP-LIEB-ANALYSIS.md` and `audit_brascamp_lieb_applicability()` in `src/ymmg/toron_brascamp_lieb.py`.
- `GLOBAL_BRASCAMP_LIEB = NOT_APPLICABLE`: Confirmed due to non-convexity of $H(U)$ on compact $SU(N)$ outside small fields and vanishing transverse Hessian on $\mathcal{M}_{\mathrm{flat}}$ ($\sup \|(\operatorname{Hess} V)^{-1}\|_{\mathrm{op}} = +\infty$).
- `LOCAL_BRASCAMP_LIEB = CONDITIONAL`: Confirmed; conditional on excising singular torons ($\delta_{\mathrm{sing}}(T)^2 \to 0$), controlling the $O(L^{-2})$ infrared Laplacian modes, and establishing a volume-uniform Peierls / large-field tail bound $\mu_{\mathrm{per},\beta}(\mathcal{G}_\epsilon^c) \le C e^{-c\beta}$.

### Item 5: Signs in Schwinger–Dyson Identities (`YM-011-TORON-SD1`) — **VERIFIED**
Re-derived from first principles for $\{T^a\}_{a=1}^{N^2-1} \subset \mathfrak{su}(N)$ with $\operatorname{Tr}(T^a T^b) = -\frac{1}{2}\delta^{ab}$ and $\sum_a (T^a)^2 = -\frac{N^2-1}{2N} I_N$:
1. **Casimir divergence:** $\sum_{a=1}^{N^2-1} \partial_\ell^a F_{\ell, p_0}^a(U) = \frac{1}{2N}\operatorname{Tr}\!\big((\sum_a (T^a)^2)(U_{p_0} + U_{p_0}^\dagger)\big) = -\frac{N^2-1}{2N^2}\operatorname{Re}\operatorname{Tr}(U_{p_0})$.
2. **$1/N$ loop-splitting sign:** With $\Delta_p = U_p - U_p^\dagger = 2i\operatorname{Im}(U_p)$, the completeness relation $\sum_a \operatorname{Tr}(T^a \Delta_{p_0})\operatorname{Tr}(T^a \Delta_p) = -\frac{1}{2}\operatorname{Tr}(\Delta_{p_0}\Delta_p) + \frac{1}{2N}\operatorname{Tr}(\Delta_{p_0})\operatorname{Tr}(\Delta_p)$ yields $\frac{1}{2N}(2i\operatorname{Im}\operatorname{Tr} U_{p_0})(2i\operatorname{Im}\operatorname{Tr} U_p) = -\frac{2}{N}(\operatorname{Im}\operatorname{Tr} U_{p_0})(\operatorname{Im}\operatorname{Tr} U_p)$.
3. **Non-closure:** Confirmed `SCHWINGER_DYSON_CLOSURE = PARTIAL / NOT_SELF_CLOSING` because the $2d - 3$ neighboring 6-link domino loop mergers $\operatorname{Re}\operatorname{Tr}(U_{p_0} U_p^\dagger)$ and 8-link figure-eight loops $\operatorname{Re}\operatorname{Tr}(U_{p_0} U_p)$ have indefinite sign.

### Item 6: Reflection-Positivity & Character-Expansion Assumptions — **VERIFIED**
- `REFLECTION_POSITIVITY_ROUTE = PARTIAL`: Link/site reflection positivity holds on $\Lambda_{\mathrm{per}}(2L, d)$, but chessboard dissemination of $h_p(U)$ reproduces the homogeneous periodic product $\langle \prod_x h_{p_x} \rangle_{\mu_{\mathrm{per},\beta}}^{1/|\Lambda|}$, which remains coupled across 3-cubes by non-Abelian Bianchi constraints in $d \ge 3$.
- `CHARACTER_EXPANSION_STATUS = PARTIAL`: Heat-kernel / character coefficients $c_r(\beta) > 0$ hold for all $\beta > 0$, but strong-coupling character truncation is restricted to $\beta \le \beta_0 \ll 1$ and is never misused at weak coupling $\beta \gg 1$.

### Item 7: Fixed-$L$ versus Uniform Constants (`P1` vs `P2` vs `P3`) — **VERIFIED**
- `P1` (`FIXED_VOLUME_PERIODIC_O_1_OVER_BETA = PROVED`) is strictly separated from `P2` (`VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA = OPEN`, blocked by `YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`) and `P3` (`CONTINUUM_UNIFORM_CONTROL = OPEN`).
- `evaluate_periodic_plaquette_hierarchy_guardrail` in `src/ymmg/toron_brascamp_lieb.py` fails closed with `ValueError` whenever `P2` or `P3` is queried as proved.

### Item 8: Partition-Function Differentiation & Resonant $\ln\beta$ Terms — **VERIFIED**
Differentiating $\ln Z_{\mathrm{per}}(\beta) = \ln C_0(L) - \alpha_L \ln \beta + k_L \ln(\ln \beta) + O_L(1/\ln\beta)$ with respect to $\beta$ yields:
$$-\partial_\beta \ln Z_{\mathrm{per}}(\beta) = \frac{\alpha_L}{\beta} - \frac{k_L}{\beta \ln \beta} + o_L\!\left(\frac{1}{\beta \ln \beta}\right) = O_L\!\left(\frac{1}{\beta}\right).$$
Thus any resonant $(\ln \beta)^{k_L}$ factor in $Z_{\mathrm{per}}(\beta)$ produces a subleading $-\frac{k_L}{\beta \ln \beta} = o_L(1/\beta)$ correction, **never** $\frac{\ln \beta}{\beta}$.

### Item 9: Sublevel-Set & Dyadic Partition-Ratio Argument (`YM-011-TORON-T1` & `YM-011-TORON-T2`) — **VERIFIED**
- By log-partition convexity $\partial_t^2 \ln Z_\Lambda(t) = \operatorname{Var}_{\mu_t}(H) \ge 0$, $t \mapsto \langle H \rangle_{\mu_t}$ is non-increasing on $(0, \infty)$, so $\frac{\beta}{2}\langle H \rangle_{\mu_\beta} \le \int_{\beta/2}^{\beta} \langle H \rangle_{\mu_t}\, dt = \ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)}$, proving Theorem `YM-011-TORON-T1`:
  $$e_{\mathrm{plaq}}(\beta, \Lambda) \le \frac{2}{|P_+|\,\beta} \ln \frac{Z_\Lambda(\beta/2)}{Z_\Lambda(\beta)} \qquad \forall \beta > 0.$$
- In the dyadic ratio $Z_{\mathrm{per}}(\beta/2)/Z_{\mathrm{per}}(\beta) = 2^{\alpha_L}(1 - \frac{\ln 2}{\ln \beta})^{k_L}(1 + o_L(1)) \to 2^{\alpha_L}$, both $\beta^{-\alpha_L}$ and $(\ln \beta)^{k_L}$ cancel directly without requiring derivative asymptotics.

### Item 10: Literature Theorem Mapping & Bałaban Comparison — **VERIFIED**
- Section 8.1 accurately contrasts single-step periodic torus plaquette bounds with Bałaban's multiscale small-field / large-field polymer RG machinery (`CMP 95, 96, 98, 109, 116, 119, 122`).
- Section 8.2 provides the complete 12-column Primary-Source Audit Table across all 7 primary sources.

### Item 11: Claimed $O_L(1/\beta)$ Coefficient & Project Invariants — **VERIFIED**
- In $d = 4$, with $|P_+| = 6L^4$, $|E_{\mathrm{co-tree}}| - 4 = 3(L^4 - 1)$, and $\alpha_{\mathrm{harm}}^{\min}(4, N) = N^2 - 1$,
  $$\alpha_L(4, N) = \frac{3}{2}(N^2 - 1)(L^4 - 1) + (N^2 - 1) = \frac{(N^2 - 1)(3L^4 - 1)}{2},$$
  $$C_{\mathrm{per}}(L, 4, N) = \frac{\alpha_L(4, N)}{6L^4} = \frac{(N^2 - 1)(3L^4 - 1)}{12 L^4} = \frac{N^2 - 1}{4}\left(1 - \frac{1}{3L^4}\right) < \frac{N^2 - 1}{4}.$$
- `NEGATIVE_EVIDENCE_REGISTER.md` properly records `NEG-YM-011-TORON-1`.
- `GOAL_COMPLETE = FALSE`, `CLAY_PROBLEM = OPEN_AND_UNSOLVED`, and `356 passed` tests are confirmed.

---

## 2. Final Audit Verdict

**`INTEGRITY_PASS_WITH_LIMITATIONS`**
- **Approved Scope (`PROVED`):** Theorem `YM-011-TORON-Q1` (quartic commutator zero-locus geometry), Theorem `YM-011-TORON-SD1` (exact finite-$N$ link Schwinger–Dyson identity), Theorem `YM-011-TORON-T1` (universal dyadic partition-ratio concavity bound), and Theorem `YM-011-TORON-T2` (`P1: FIXED_VOLUME_PERIODIC_O_1_OVER_BETA = PROVED`).
- **Enforced Limitations (`OPEN` / `PARTIAL`):** `GLOBAL_BRASCAMP_LIEB = NOT_APPLICABLE`, `LOCAL_BRASCAMP_LIEB = CONDITIONAL`, `SCHWINGER_DYSON_CLOSURE = PARTIAL`, `REFLECTION_POSITIVITY_ROUTE = PARTIAL`, `CHARACTER_EXPANSION_STATUS = PARTIAL`, `P2: VOLUME_UNIFORM_PERIODIC_O_1_OVER_BETA = OPEN` (`YM-011-DYADIC-FREE-ENERGY-UNIFORMITY`), and `P3: CONTINUUM_UNIFORM_CONTROL = OPEN`.
