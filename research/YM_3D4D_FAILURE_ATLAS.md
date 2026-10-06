# YM 3D4D FAILURE ATLAS

Status: CANDIDATE RESEARCH MAP / NO RESULTS PROMOTED. Access date: 2026-10-04.

YM-3D4D-FAILURE-MAP-001: source theorem, proof dependency chain, dimension-dependent exponents, first failing lemma, missing gain, repair mechanism, and DAG compatibility. Entries require source-level verification; no failure implies a structural no-go.

Policy: governance/YM_AUTONOMOUS_DISCOVERY_ARCHITECTURE.md. Primary dependency remains YM-015F. E-UV-FLOWED PARTIAL_PROGRESS; E-UV-LOCAL-OS, E-UV-FREE-CONT OPEN_AND_UNSOLVED; P3 and E-CROSSOVER OPEN; YM-016 BLOCKED; STRUCTURAL_NO_GO_COUNT = 0.

## Source bindings and access limits

- **S1:** Chandra, Chevyrev, Hairer, Shen, *Stochastic quantisation of Yang–Mills–Higgs in 3D*, Invent. Math. 237 (2024), 541–696, [publisher full text](https://link.springer.com/article/10.1007/s00222-024-01264-2), [author record](https://arxiv.org/abs/2201.03487). Access: publisher HTML opening, abstract and introduction through equation (1.7) inspected; subsequent targeted opens failed. No PDF downloaded or line-by-line proof reconstruction completed. Verified locators: abstract; introduction, trivial-bundle assumption; (1.4), (1.7). Later theorem numbers are not represented as directly inspected here.
- **S2:** Cao, Chatterjee, *A State Space for 3D Euclidean Yang–Mills Theories*, CMP 405, article 3 (2024), [publisher](https://link.springer.com/article/10.1007/s00220-023-04870-y). Access: full HTML available; introduction through Theorem 1.6 and surrounding discussion inspected. Verified locators: §1.1 group restriction, §1.5 state space, Lemma 1.4, Theorem 1.6, Remark 1.7, Conjecture 1.8. Proof §3 not reconstructed.
- **S3:** Chevyrev, Shen, *Uniqueness of Gauge Covariant Renormalisation of Stochastic 3D Yang–Mills–Higgs*, ARMA 250, article 11 (2026), published 13 January 2026, [publisher](https://link.springer.com/article/10.1007/s00205-025-02163-3), [preprint](https://arxiv.org/abs/2503.03060). Access: publisher HTML introduction through §1.1 inspected; search returned main Theorem 1.6 but its complete quantifiers and proof were not inspected. Verified locators: (1.1), introduction (1.2), §1.1 mollifier scaling. Search snippets are discovery aids only.

The source record supports a local stochastic dynamic and conditional state-space compactness, not a solved 3D continuum measure or mass gap. S3 explicitly leaves invariant-measure existence and 3D lattice Langevin scaling-limit identification open. This audit found a newer uniqueness result; it does not establish an exhaustive ranking of all 2026 literature.

## FA-001: local stochastic flow / singular SPDE / regularity structures

**Source theorem and scope (SOURCE_SUPPORTED):** S1 abstract supplies a renormalised local-in-time stochastic YMH flow and a gauge-orbit Markov process allowing explosion. Dimension is three, on a torus and trivial bundles. The proof dependency skeleton to audit is DeTurck parabolicisation → enhanced noise/model convergence → renormalised fixed point → state-space continuity → gauge covariance in law → orbit dynamic. This is a skeleton, not a verified lemma-by-lemma dependency chain.

**Critical estimate (ALGEBRAICALLY_VERIFIED scaling diagnostic; not a source theorem):** parabolic scaling gives white-noise homogeneity below −(d+2)/2 and stochastic heat-convolution homogeneity

\[
\alpha=(2-d)/2-\kappa,\qquad \kappa>0.
\]

The YM coordinate equation contains a quadratic derivative term and a cubic term. In formal model homogeneities, heat integration gives respectively 2α+1 and 3α+2. Their improvements over α are α+1 and 2α+2. These labels concern renormalised model terms; they do not assert that ordinary multiplication of distributions exists.

| Quantity | d=3 | d=4 |
|---|---|---|
| Linear α | −1/2−κ | −1−κ |
| Quadratic derivative output 2α+1 | −2κ | −1−2κ |
| Quadratic improvement | 1/2−κ | −κ |
| Cubic output 3α+2 | 1/2−3κ | −1−3κ |
| Cubic improvement | 1−2κ | −2κ |

**First diagnosed failure:** strict positive improvement required by the usual locally subcritical recursive expansion disappears at d=4. At κ=0 both margins are zero; below the endpoint both are negative. This is the first failure of this *power-counting test*, not an identified first failing numbered lemma in S1. That stronger requested reconstruction remains PENDING_SOURCE_PROOF_AUDIT. A naive unrenormalised product test already fails in d=3 and therefore cannot be used as the d=3→4 separator.

**Classification:** METHOD_SPECIFIC_OBSTRUCTION for direct use of this subcritical construction. No structural no-go and no claim about all critical-SPDE methods.

**Missing gain:** if a corrected bound adds regularity δ₂ to the quadratic output and δ₃ to the cubic output, strict improvement requires δ₂>κ and δ₃>2κ at d=4. The endpoint has infimum missing positive power zero, not a fixed half derivative. Recovering the entire d=3 margin would require δ₂=1/2 and δ₃=1. These are distinct targets. Endpoint logarithmic control might replace a power gain only after a new contraction/model-convergence theorem is proved.

**Bounded missing 4D estimate:** construct a gauge-compatible renormalised bilinear derivative operator with an endpoint norm and a scale-uniform convergence/iteration bound, then do the corresponding cubic bound. Do not infer convergence from the homogeneity table. Ward identities, curvature/Bianchi cancellations, and asymptotic-freedom damping are candidate hypotheses, currently HEURISTIC; none was verified here as supplying δ.

**DAG compatibility:** exploratory support for E-UV-FLOWED and representation search only. A successful stochastic endpoint estimate still needs measure existence, lattice matching, gauge-invariant observable bounds, positivity and local OS bridges. It does not close YM-015F.

## FA-002: state-space compactness / energy / concentration

**Source theorem (SOURCE_SUPPORTED):** S2 Theorem 1.6 says that tight action values at every positive heat-flow time imply a weakly convergent subsequence of orbit-valued laws. Its introduction names Uhlenbeck compactness, heat-flow properties and Sobolev embedding as proof ingredients. Establishing that actual YM approximants meet the action-tightness premise remains Conjecture 1.8. The group restriction in §1.1 must be retained.

**Independent scaling diagnostic (ALGEBRAICALLY_VERIFIED):** for a rescaled smooth connection Aλ(x)=λA(λx), curvature is Fλ=λ²F(λx), and ∫|Fλ|²=λ^(4−d)∫|F|² on the corresponding rescaled domain. Thus the energy exponent is 1 in d=3 and 0 in d=4. Local concentration at shrinking scales is energetically marginal in four dimensions. This computation is not a substitute for the exact compactness proof or a bubbling theorem.

**First failing lemma:** UNKNOWN_PENDING_PROOF_AUDIT of S2 §3. The action-scaling margin vanishes, but this alone neither proves Theorem 1.6 false in d=4 nor identifies where additional positive flow time could repair compactness.

**Classification:** METHOD_SPECIFIC_OBSTRUCTION candidate, with failure itself unverified. **Missing gain:** no numerical δ can yet be assigned to S2's actual compactness estimate. A proposed local anti-concentration hypothesis is uniform integrability of curvature energy in balls, sup_n sup_x ∫B_r(x)|F_n(t)|²→0 as r→0 at each fixed t>0, with suitable probability control; sufficiency for the required orbit topology must be proved. Candidate repairs: concentration-compactness, gauge-covariant norms, flow-time smoothing. **DAG:** informs continuum tightness; cannot replace the missing nonperturbative insertion bound.

## FA-003: counterterm uniqueness / gauge covariance

**Source-supported result:** S3 strengthens the intrinsic uniqueness of gauge-covariant mass renormalisation. Introduction (1.2) detects a different limiting renormalisation through regularised Wilson-loop expectations separated by order t^(10/9), replaceable by an exponent greater than one. This is a short-time detection exponent, not a spectral gap or a d-dependent power-counting margin. Its proof uses stochastic and flowed-observable expansions.

**3D value:** detection exponent 10/9 in the introductory formulation. **4D value:** UNKNOWN; dimensional substitution into 10/9 is invalid. **Critical estimate / first failure / missing gain:** PENDING complete Theorem 1.6 and §1.3/proof audit; local construction FA-001 is already a prerequisite. **Classification:** METHOD_SPECIFIC_OBSTRUCTION of a proposed transfer, not a proved obstruction. **Repair:** gauge-invariant defect detection is a concrete mechanism to examine in the defect-correction ledger. **DAG:** possible observable/counterterm diagnostic; uniqueness cannot provide existence, invariant measure or nonperturbative lattice matching.

## Coverage registry: required categories not silently promoted

| Category | Entry / source theorem | 3D value | 4D value | First failure / missing gain | Mechanism / DAG compatibility |
|---|---|---|---|---|---|
| Stochastic quantisation | FA-001 / S1 local flow | α<−1/2 | α<−1 | scaling diagnostic above; numbered lemma pending | Gauge cancellations; exploratory UV support |
| Singular SPDE | FA-001 | margins 1/2−κ, 1−2κ | −κ, −2κ | strict improvement lost; δ₂>κ, δ₃>2κ | Endpoint/log norms; no closure |
| Regularity structures | FA-001 | positive recursive margins | critical endpoint | source rule/model theorem audit pending | Critical model convergence; no closure |
| Paracontrolled methods | PENDING_SOURCE_SELECTION | UNKNOWN | UNKNOWN | UNKNOWN; no obstruction assigned | Compensated products; UV exploratory |
| Energy estimates | FA-002 diagnostic / S2 | action exponent 1 | 0 | actual estimate pending; δ unknown | Local anti-concentration; tightness |
| Compactness | FA-002 / S2 Thm. 1.6 | conditional tightness | no transferred theorem | §3 first lemma pending; δ unknown | Gauge-covariant compactness; tightness |
| Concentration/bubbling | FA-002 diagnostic only | subcritical energy scaling | energy critical | bubbling source theorem pending | Concentration-compactness; tightness |
| RG contraction | PENDING_SOURCE_SELECTION | UNKNOWN | UNKNOWN | no validated 3D comparison; δ unknown | RG damping; main YM-015F dependency retained |
| Mass-scale generation | PENDING_SOURCE_SELECTION | UNKNOWN | UNKNOWN | no verified theorem; δ unknown | Massive-basin stability; YM-016 blocked |
| Spectral estimates | PENDING_SOURCE_SELECTION | UNKNOWN | UNKNOWN | no verified physical gap; δ unknown | Transfer-matrix norms; downstream only |

For pending rows, no failure classification is awarded until an actual approach is analysed. UNKNOWN is not negative evidence. The completed algebra is explicitly separated from source theorem claims. The next task is to inspect S1's state-space definition, admissible exponents, regularity-structure rule and first model/fixed-point lemma, bind exact locators, and replace the diagnostic with an actual proof-local failure map. No XFER is promoted and STRUCTURAL_NO_GO_COUNT remains zero.


## FA-001 numbered locator / stage037
Primary author manuscript now inspected at Lemma5.17 (pp69-70) and downstream fixed-point use (p73). Its displayed minimum-degree criterion has 3D margin1/2-2kappa. The separate physical-homogeneity derivative-branch diagnostic gives4D margin-2kappa; this does not yet reconcile the printed attaining tree, reduced source degrees or full CH16 hypotheses. Detailed audit: YM_3D4D_NUMBERED_LEMMA_AUDIT_037.md. First failing numbered lemma of the whole proof remains UNESTABLISHED; no4D impossibility or structural no-go follows.


## FA-001 cited theorem hypotheses / stage038
Theorem2.15 of Chandra-Hairer arxiv1612.08138v5, printed18-19, directly inspected: complete/subcritical rule, alltree/subtree strict tests and compatible Gaussian approximation conditions. Detailed audit YM_3D4D_BPHZ_HYPOTHESIS_AUDIT_038.md. One numerical minimum-degree margin cannot discharge the full quantified theorem. First failing numbered lemma and actual4D replacement remain unestablished.


## FA-001 attaining trees and slack dictionary / stage039
Visually inspected printed70 drawings; independent fulltext pp63-64 gives later heat-gain2 counting, while p59 assigns2-kappa. Detailed two-assignment audit YM_3D4D_TREE_SLACK_AUDIT_039.md. Both displayed3D margins are positive for smallkappa; both4D diagnostics lose strictmargin. A globalreset/regrading/modelnorm dictionary and earliest numbered failure remain unresolved. No authortheorem falsification or structural no-go.


## FA-001 numbered symmetry filter / YM-045
Source YMH Lemma4.5 p54 -> Lemma5.5 p60, decoration definition(4.3)p53 and parity set(5.9)p60. Under invariant kernel/noise law the odd-decoration/noise exclusion has a dimension-independent algebraic core; actual4D existence is unproved. Own044 pruned comparison has even-noise/even-derivative unary-root binary chains:3D a=(1/2-3kappa)q-2+kappa, negative q2/4;4D a=-2-(3q-1)kappa, unbounded below. Fixed root gain cannot repair this comparison; assumed per-noise gain requires gamma>3kappa (gamma>0 at kappa0) to make this chain sector finite. Parity passes are necessary only, not nonzero-character or author-membership claims. METHOD_SPECIFIC_OBSTRUCTION; candidate repair search: quantified gauge cancellations or improved analytic degrees plus full completed-rule/model correspondence. YM-015F receives no estimate from parity alone. Earliest numbered4Dfailure remains UNESTABLISHED, structural no-go0. Detailed proof and limits in TREE_SLACK_AUDIT_039.


## FA-001 numbered counting/linearity gate / YM-046
YMH Lemma5.11(5.12) pp63-64 -> Lemma5.12 p65/footnote15. Own necessary-count reconstruction recovers only(n,p,t,q)=(2,1,0,2),(4,1,0,4) negative3D patterns for0<kappa<1/14; patterns are not tree counts. Stipulated dimensional heat2 comparison changes order coefficient(4-D)/2 from1/2 to0. Even-order linear necessary-count witnesses have4D degree-2-n*kappa; cubic external witnesses are marginal at kappa0. Therefore source proof-local n>=6 positivity does not follow after this formal substitution. No actual4D symbols/nonzero characters or earliest global failure proved. Missing diagnostic order gain requires delta>kappa (delta>0 at kappa0), grading-specific, not an analytical estimate. Candidate repairs: order-dependent gauge cancellations/improved model norms, with full completed-rule/subtree correspondence. METHOD_SPECIFIC_OBSTRUCTION; source3Dlemma not falsified; structural no-go0.


## FA-001 marked symmetry compatibility / YM-047
Numbered Definition4.4/Lemma4.5 -> Lemma5.5 remains conditional on kernel/noise invariance. Own first-jet invariance requires L1J0+L0J1=L1, not merely L0J0=L0. Odd marked coefficients need not vanish: positive Gaussian exponential insertion has L0(G)=0,L1(G)=1 and source covariance s->-s. Actual flowed-observable parity/source transformation and marked BPHZ/model correspondence remain unverified. No dimension-dependent positive gain supplied; earliest global4Dfailure still UNESTABLISHED. Transfer to YM-015F is a mark-completeness gate, not a uniform estimate. METHOD_SPECIFIC_OBSTRUCTION for vacuum-filter reuse without marked hypotheses; structural no-go0. Detailed support/jet proof in SOURCE_JET_REDUCTION.


## FA-001 full source-coefficient filter / YM-048
Numbered YMH Lemma4.5 p54 ->5.5 p60 ->5.12 p65 supplies a vacuum symmetry premise, not a marked BPHZ theorem. Own invariant-probability finite-jet theorem yields epsilon_S=eta as the necessary condition for a nonzero marked coefficient, including after the correct source-denominator convolution. For sign-odd Gaussian marks and tau=G^q, the condition is q+|S| even, so odd-q coefficients may survive odd source subsets. No Gaussian moment is identified with a source BPHZ character or tree. Actual source signs, kernel/model covariance, completed-rule membership, and dimensional analytic gain remain OPEN; 3D/4D parity algebra is dimension independent, hence no positive missing margin is supplied. Earliest global4Dfailure UNESTABLISHED; METHOD_SPECIFIC_OBSTRUCTION only for unconditional reuse of the vacuum filter; structural no-go0. Source-counting family046 stays scoped to its vacuum hypotheses. Detailed own proof in SOURCE_JET_REDUCTION; compatibility with YM-015F requires actual mark and terminal-adjoint reconstruction.
