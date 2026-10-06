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
