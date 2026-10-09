# Construction, defect, correction ledger

CDC-001 / YM-015F-JET-002: put the exact normalized Gibbs source jet and an approximate RG source jet in the same finite algebra. Define D=P-P*. Require semantic equality of the represented observable. Relevant, marginal, irrelevant, gauge, nonlocal, symmetry, and observable labels require explicit projections; none have been constructed for YM here. For each component record scaling dimension, symmetry, gauge behavior, locality, positivity, norm, coupling, volume, and cutoff dependence. Model-specific entries remain OPEN.

Conditional lemma CDC-002 (pending independent review). In a normed space suppose D-L(C)=E, ||E||<=eta||D||, ||C||<=K||D||, and ||N(C)||<=B||C||^2, with nonnegative constants. The triangle inequality gives ||D'|| <= (eta+BK^2||D||)||D|| for D'=D-L(C)-N(C). If eta<1 and ||D||<=epsilon with eta+BK^2 epsilon<1, this contracts that step. Iteration requires uniform constants and validity at every step. No right inverse, uniform K, quadratic B, or invariant YM norm ball is supplied.

FALSIFY: a scalar marginal mode L=0, N=0, D nonzero leaves D'=D for every correction. A schematic decomposition cannot imply strict contraction. METHOD_SPECIFIC_OBSTRUCTION for this abstract scheme; no Yang-Mills no-go theorem.

Next bounded task: identify coefficient projections and linearized integration in one actual RG scale. The exact source-jet integration inequality J3 in YM_015F_SOURCE_JET_REDUCTION.md is conditional on input integrability. Strict q<1 remains OPEN. Audit marginal subtractions and logarithmic gains next.

Policy: governance/YM_AUTONOMOUS_DISCOVERY_ARCHITECTURE.md. E-UV-FLOWED PARTIAL_PROGRESS; other continuum, local OS, crossover and physical-gap edges remain open. STRUCTURAL_NO_GO_COUNT=0.


## CDC-048: terminal adjoint criterion at an integrated-equivalence step

Own conditional theorem, not an extracted Bałaban identity. For finite M let E_k be real/complex normed spaces, T_k:E_k->E_(k+1) bounded linear source-independent maps, and lambda_M a continuous terminal linear functional. Define lambda_k=lambda_(k+1) T_k backwards. For each finite nilpotent-source coefficient S let v_(k+1,S)=T_k v_(k,S), and choose approximations tilde_v_(k,S) with tilde_v_(0,S)=v_(0,S). Put D_(k,S)=T_k tilde_v_(k,S)-tilde_v_(k+1,S). Then

    lambda_0(v_(0,S)) = lambda_M(tilde_v_(M,S))
                         + sum_(k=0)^(M-1) lambda_(k+1)(D_(k,S)).

Proof: lambda_k(tilde_v_(k,S))-lambda_(k+1)(tilde_v_(k+1,S))=lambda_(k+1)(D_(k,S)); sum and telescope. Equivalently the final vector error is the sum of each D propagated through all later T maps. This proof needs no positivity and makes no assertion that such bounded operators exist in the actual source representation. Infinite histories/limits require separate absolute convergence or other justified passage to limits. Source-dependent operators require full subset-convolution jets instead; they are outside this fixed-map theorem.

For positive jet weights r_S=product_(i in S)r_i define ||D_k||_r=sum_S r_S ||D_(k,S)||_(E_(k+1)). Finite sums and duality give

    sum_S r_S |lambda_0(v_(0,S))-lambda_M(tilde_v_(M,S))|
       <= sum_k ||lambda_(k+1)||_* ||D_k||_r.

A sufficient cutoff-uniform terminal estimate is a uniform bound on the approximate terminal jet plus this weighted residual sum, with physical vacuum normalization already in lambda_M or otherwise explicitly retained. Neither boundedness of each fixed-cutoff operator nor a finite M proves a uniform bound when M grows. No uniform dual norms, source residuals, physical denominator bounds, strict RG contraction or flow tails are supplied. The criterion may test just the specified terminal insertion family; equality against every coarse test would be the stronger measure identity. A defect annihilated by that exact backward functional does not affect that target, but its vacuum integral vanishing alone does not establish this annihilation.

Positive finite countermodel to vacuum-only substitution: E0=R^2,E1=R, lambda1=id, T=(1,1), A=(2,0). For vacuum v0=(1/2,1/2), Tv0=Av0=1. For marked v1=(1/2,-1/2), Tv1=0 but Av1=1. Both maps take nonnegative vectors to nonnegative scalars; agreement on this vacuum vector does not give lambda1 A=lambda1 T on marked inputs. A does not conserve mass on arbitrary inputs. Thus a specific equal-vacuum-integral representation cannot be silently substituted for the whole marked operator. This is METHOD_SPECIFIC_OBSTRUCTION only; it does not refute R-I's vacuum formulas or any physical YM theorem.

The source-bound trigger is R-I printed193 last paragraphs and194 before(1.76), separately audited in YM_015F_R_OPERATION_SOURCE_AUDIT_039.md: eliminated domains are term dependent. Reconstruction must identify the actual backward functional or preserve the original insertion before elimination, with all retained T/zeta objects, rejected/n=0 sectors, Jacobians, normalization and terminal integration. The fixed-vacuum denominator convention does not remove these obligations. Current theorem status PROVED_WITHIN_STATED_HYPOTHESES pending independent review; actual operator/adjoint identification and cutoff-uniform estimates OPEN. No scientific edge closes.


## CDC-049: existence and stability of a target adjoint are separate gates

Own finite-dimensional theorem. Let T:F^n->F^m be linear, F=R or C, and ell:F^n->F linear (no conjugation in functional composition). A functional lambda:F^m->F satisfying lambda T=ell exists if and only if ker T is contained in ker ell. Necessity follows by applying lambda T to a kernel vector. For sufficiency define lambda(Tv)=ell(v) on image T; the kernel condition makes this well defined. Extend it linearly to a complement. Equivalently ell is in the row space of T. This is an exact finite criterion for recovering this target from unmarked reduced data for every input vector, not a statement that a target matched on one vacuum vector has such a lift. Existence alone supplies no uniform bound on lambda.

With chosen norms, every lift satisfies ||lambda||_* >= |ell(v)|/||Tv|| for each v with Tv!=0. An identified kernel vector with ell(v)!=0 disproves only descent through that particular T. It does not forbid retaining additional source coefficients, changing representation or constructing the physical observable by another method. No claim is made for infinite-dimensional algebraic extensions or their continuity; actual integral operators require their own domain and analytic estimates.

Positive norm-amplification family: for0<epsilon<=1 put

    T_epsilon = (1/2)*[[1+epsilon,1-epsilon],[1-epsilon,1+epsilon]],
    ell=(1,-1),  u=(1/2,1/2),  d=(1,-1).

T is positive and column stochastic, T u=u and T d=epsilon*d. The unique lift is lambda_epsilon=(1/epsilon,-1/epsilon). In l1 vector norms its dual l-infinity norm is1/epsilon, by the displayed ratio applied to d. Vacuum normalization and l1 forward contraction are therefore compatible with arbitrarily large backward adjoint norms. At epsilon=0, d is a kernel witness and no lift of ell exists. This is not a physical cutoff trajectory, actual RG map or no-go theorem.

Crucial distinction for the selected source route: retaining the marked density before reduction does not require inverting T. For any finite column-stochastic T and coefficient vector v_S, the terminal row of ones satisfies 1_m*T*v_S=1_n*v_S, including signed/complex marked vectors. Nonnegative entries give ||T*v_S||_1<=||v_S||_1. These identities transport already defined source coefficients; they do not prove cutoff-uniform input norms. A coarse adjoint applied to unmarked T*v and a forward pushforward T*v_S are different representations. The exploding lambda example is no obstruction to correctly carrying v_S and integrating its mass. Actual gauge factors, constraints, rejected/n=0 histories, physical normalization and terminal row still require matching; individual signed activities are not asserted column stochastic.

Noise-sign projection diagnostic: J swaps two states, P_even=(I+J)/2=T_0, v_empty=u, v_1=(1/2,-1/2). P_even preserves vacuum but kills v_1; ell(v_1)=1 whereas ell(P_even v_1)=0. The target probe and source density are both odd, so their pairing has even combined parity. Vacuum-safe projection does not preserve this marked pairing. This finite projection is NOT identified with an author's BPHZ symmetry lemma or an actual gauge transformation; if the probe is multiplied into the original marked density before mass-preserving reduction, its total integral is retained instead. Classification METHOD_SPECIFIC_OBSTRUCTION only.

Source audit049 places the first actual obligation at R-I(1.76), retained disjoint integration, coordinate pullback/tree-gauge insertion and compensating residual/fluctuation transformations. Use the criterion only after identifying the true operator and target; no rank, kernel, probability reference or norm of that actual operation is established. Actual terminal-adjoint stability or complete forward marked transport and uniform bounds remain OPEN. No scientific edge closes.


## CDC-050: non-linear source resolvent vs. nilpotent trace linearization

Own conditional operator-theoretic analysis. For a general non-linear gauge observable O[U], coupling with real source J modifies the quadratic fluctuation operator to Q_J = Delta_YM[V] - J * D^2 O[V].

1. **Domain and gauge projection:** Let H = L^2(Lambda_a, su(N) tensor R^4) be the lattice vector field space. The gauge group action generates zero modes ker(Delta_YM) = Im(D_V), where D_V is the covariant exterior derivative. In background Feynman/axial gauge, Delta_YM[V] is strictly positive on H_perp = (Im D_V)^perp.
2. **Gradient flow smoothing:** At fixed physical flow time t_phys > 0, the Yang–Mills gradient flow semigroup e^(t Delta) provides Gaussian smoothing on physical scale sqrt(t_phys). Consequently, for a smooth test function f in H^3, the observable Hessian B = D^2 O_(a,t)(f)[V] is a bounded operator on H_perp on each finite lattice.
3. **Resolvent status:** The operator norm ||(I - J Delta_YM^(-1/2) B Delta_YM^(-1/2))^(-1)||_Op is finite for sufficiently small |J| < r(a, t). Dimensional counting ([D^2 O] = 4) shows that the unflowed limit t -> 0 is critically marginal in 4D, but at fixed t > 0 the flow cutoff prevents fixed-lattice operator norm divergence.
4. **Nilpotent reduction:** In the nilpotent algebra eta^2 = 0, the non-linear resolvent inversion is replaced identically by the linear operator trace (1/2) eta Tr(Delta_YM^(-1) B). This eliminates the infinite-series resolvent inversion obstacle, but leaves open the cutoff-uniform bound on the trace and the interaction-vertex contractions of linear fluctuation terms DX[V] . A.


## CDC-050R: correction of Faddeev–Popov orbit conflation, endpoint gauge action, and Family 215 scoped audit

1. **Faddeev–Popov orbit vs. configuration slice repair:** The previous statement equating the single-orbit tree-gauge average to O[V exp(g A)] prod_b delta(A(b)) conflated the single-orbit resolution of unity (which integrates to the scalar 1 / Delta_FP(V, A)) with a slice distribution. Setting O = 1 revealed the contradiction: 1 / Delta_FP != prod_b delta(A(b)). The gauge-slice delta distribution prod_(b in T) delta(A(b)) arises strictly under the full configuration-space functional integral int dmu(A), after inserting the resolution of unity and changing integration variables A -> A^(h^-1) using gauge invariance of the measure, determinant, and observable.
2. **Endpoint gauge transformations vs. Bałaban coordinates:** Link variables U_xy = V_xy exp(g A_xy) transform under site gauge transformations via separate endpoint factors: U_xy^h = h_x U_xy h_y^-1. Holding background V_xy fixed while transforming A_xy by h_y A_xy h_y^-1 does NOT produce U_xy^h unless h_x = V_xy h_y V_xy^-1. Bałaban's compensating transformations (R-I (1.85)–(1.88)) require joint transformation of both background V -> V^h and fluctuation A -> h^-1 A h. Asserting an uncoupled tree-gauge identity on fluctuation A with fixed background V is mathematically defective. The actual-model Bałaban coordinate pullback and tree-gauge orbit identity across all external bonds B0, charts, and cutoffs are classified as **CONDITIONAL_AND_OPEN** (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_ORBIT_IDENTITY_OPEN`).
3. **Explicit non-factorization quantifiers:** Parabolic diffusion demonstrates generic failure of spatial factorization across disjoint vacuum integration domains Zh, establishing that factorization cannot be universally assumed from vacuum domain disjointness, rather than an impossible universal non-factorization for all degenerate/trivial test functions.
4. **OpenAI Family 215 scoped audit:** Audited upstream openai/math Problem 215 (Oct 6, 2026 public release, math/lean/docs/215.md, formalization.yaml). Lean 4 declaration head `lattice_spin_decay_2d` formalizes classical lattice spin decay for O(n) (n >= 3) on 2D periodic lattices. Exhaustive search across declaration heads reveals zero Lean declarations for continuum QFT construction, OS axioms, non-Gaussianity, or mass gap pole. Classified as UNVERIFIED_CANDIDATE_PREPRINT / METHOD_SPECIFIC_OBSTRUCTION.

## CDC-050R2: repair of Family 215 source provenance, locators, boundary conditions, and proof status

1. **Path and prefix repair:** The accessible upstream path in repository `https://github.com/openai/math.git` (commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`) is `lean/docs/215.md` (LEN 1,031 bytes, SHA-256 `41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30`), NOT `math/lean/docs/215.md` (which returned HTTP 404). The repository name was mistakenly prefixed to the internal path.
2. **Boundary condition repair:** The mathematical model in `lean/docs/215.md` and comparator `lean/ComparatorChallenges/ClassicalON.lean` specifies finite square-lattice subgraphs with **FREE boundary conditions** (`structure LatticeGraph`), NOT periodic boundary conditions.
3. **Declaration name and module structure repair:** The phantom declaration head `lattice_spin_decay_2d` does not exist in the upstream repository. The exact comparator challenge specification in `lean/ComparatorChallenges/ClassicalON.lean` (LEN 1,961 bytes, SHA-256 `c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696`) defines `def ExponentialDecay : Prop` and `theorem main : ExponentialDecay := by sorry`. The comparator manifest `lean/ComparatorChallenges/ClassicalON.json` (LEN 308 bytes, SHA-256 `47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252`) links this challenge to candidate solution module `OAI.Probability.ClassicalON.Main`.
4. **Proof status repair (UNVERIFIED_UPSTREAM_PROOF_CODE):** In `lean/OAI/Probability/ClassicalON/Main.lean` (LEN 2,050 bytes, SHA-256 `0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a`), `theorem main : ExponentialDecay := by ...` contains proof text. However, because governance prohibits executing untrusted downloaded code, and no reproducible kernel-checked build receipt exists at commit `fd4aeeb2...`, its status is labeled `UNVERIFIED_UPSTREAM_PROOF_CODE`. Presence of `sorry` in the comparator challenge does not establish absence of a proof module, nor does unverified proof text establish kernel validity.
5. **Inspected search scope vs. nonexistence theorem:** Inspection of the scope document, comparator challenge, manifest, and solution main module establishes a search-negative finding: zero declarations for continuum QFT construction, Osterwalder–Schrader axioms, non-Gaussianity, or 4D Yang–Mills theory exist in these files. This search-negative finding is distinguished from an unproved universal assertion of nonexistence across the entire upstream repository.

