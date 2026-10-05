# YM-015F-JET-002B — marked coefficient recurrence

Candidate YM-036; pending independent review. This is a conditional algebraic interface, not the required uniform flowed insertion theorem. The accompanying Bałaban extraction identifies which actual source map, if any, has been verified.

## Exact linear-step obligation

Fix the commuting finite algebra z_i^2=0, i=1,...,q. Write an unnormalized source density as W_k(z)=sum_S z_S W_(k,S), with vacuum coefficient W_(k,empty). If an actual RG integration operator T_k is linear, independent of these sources, and defined on every coefficient, then

    W_(k+1,S) = T_k W_(k,S).

Proof: finite coefficientwise integration. This asserts no source-dependent gauge fixing or source-dependent integration boundary; if either is used it must enter the operator's source jet and the coefficients mix instead.

Where W_(k+1,empty)(y) is nonzero, the normalized coefficient is

    M_(k+1,S)(y) = T_k[W_(k,empty) M_(k,S)](y)
                    / T_k[W_(k,empty)](y).

The identity requires W_(k,S)=W_(k,empty)M_(k,S) on the integration domain. If that representation fails, use the unnormalized recurrence and do not divide. A source-dependent rescaling or extracted vacuum/source factor is itself a jet: products obey (AB)_S=sum_(I disjoint J, I union J=S) A_I B_J. Therefore source-dependent counterterms and deterministic factors cannot be omitted from transported marked coefficients.

Neither an abstract disintegration nor a notation T_k proves equality with Bałaban's actual operator. An all-sector map must include its constraints, gauge fixing, field domains, rescaling and terminal integrations. Extracting one small-field formula does not establish that entire map or its norms.

## Connected recurrence for a positive normalized step

For the positive conditional kernel K_y and coarse law nu of the accepted YM-035 transport, define R_y(z)=E_K product_i(1+z_i X_i). Its constant coefficient is1. Let c_B(y) be the z_B coefficient of log R_y; finite logarithms are well defined since the augmentation ideal is nilpotent. All functions are bounded at each fixed cutoff.

The full source jet is R(z)=E_nu R_y(z). Its connected coefficient satisfies the finite law of total cumulance

    [z_S] log R = sum_(partitions pi of S) cumulant_nu(c_B : B in pi).

Here the one-variable coarse cumulant is the ordinary mean. All cumulants are multilinear without complex conjugation. Proof: use an auxiliary source u_B for each nonempty subset B and expand log E_nu exp(sum_B u_B c_B) coefficientwise. Substitute u_B=z_B. A product of such monomials survives only for disjoint blocks; the ordered block permutations cancel the factorial and leave each set partition once. All expansions are finite after substitution; no exponential integrability at a uniform cutoff radius is assumed.

For three distinct labels the identity is

    c_123 = E_nu c_123(y)
          + Cov_nu(c_1,c_23) + Cov_nu(c_2,c_13) + Cov_nu(c_3,c_12)
          + cumulant_nu(c_1,c_2,c_3).

This is the precise connected defect that a recurrence retaining only effective single insertions misses. It is exact within the positive-kernel hypotheses, but none of its terms has been proved small in a Bałaban norm. Signed polymer pieces require separate absolute and denominator estimates; the conditional-kernel interpretation does not apply to them individually.

## Finite certificate and scope

Let the coarse label Y take values 0 and 1 with probabilities 1/4 and 3/4; let xi independently be +/-1 with equal probabilities. Set X_1=2Y and X_2=X_3=(1+Y)xi. Every conditional c_123(y) and every coarse cumulant of the single conditional means is zero. But Cov_nu(2Y,(1+Y)^2)=9/8, which equals the full connected coefficient. Dropping the conditional covariance sector therefore loses the entire answer. Exact rational verification is in tests/test_marked_recurrence_finite_certificate.py. This is a finite countermodel, not a physical Wilson-measure counterexample.

## Remaining load-bearing theorem

The recurrence identifies the coefficients to estimate. It supplies no lattice-spacing-uniform input bound or gain. The actual problem remains: prove physically normalized fixed-flow marked coefficient estimates through a verified all-sector source-decorated RG map, including flow tails, source counterterms, denominators, marginal terms and terminal integration. The smallest source-interface subtask is to match the explicit primary map to the displayed coefficient recurrence before proposing a polymer norm induction.

New negative evidence: retaining only conditional means or ignoring source-factor convolutions does not preserve higher connected observables. Classification METHOD_SPECIFIC_OBSTRUCTION. No structural no-go; no continuum edge closure; E-UV-FLOWED remains PARTIAL_PROGRESS and YM-016 remains BLOCKED.
