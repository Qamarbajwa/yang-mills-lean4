# YM-015F-JET-002A research-writer receipt

Date: 2026-10-04. RAW UNREVIEWED. This receipt is not an accepted mathematical artifact or theorem premise. Pending inclusion in a scientific candidate and fresh review. Baseline inspected: HEAD `4e268bd0e12c8b1b4eaa3774368cd1ea19dd03bb` and `research/YM_015F_SOURCE_JET_REDUCTION.md`. No governance status or scientific acceptance is changed by this receipt.

## Exact degree-one transport derivation

On each fixed finite lattice let Omega=SU(N)^E, H be normalized product Haar measure, and mu(dU)=Z^(-1)exp(-S(U))H(dU), with the actual continuous finite Wilson action. Compactness implies 0<Z<infinity. Let Q:Omega->Y be a Borel blocking map with Y standard Borel. The target-space qualification is necessary for regular conditional probability existence; an arbitrary measurable codomain is not sufficient.

Set m=Q_#H. Disintegrate H(dU)=integral H_y(dU)m(dy), where for m-almost every y the probability H_y is supported on Q^(-1)(y). For the actual normalized flowed insertion X=O_(a,t)(f)/||f||_(H^3), with nonzero denominator, define

    w(y) = integral exp(-S(U)) H_y(dU),
    v(y) = integral exp(-S(U)) X(U) H_y(dU).

The finite-lattice flowed observable is bounded, though its bound may diverge as a decreases. Consequently all these integrals exist. The positive Wilson density implies w>0 almost everywhere. Define

    S_eff(y) = -log w(y),
    nu(dy) = w(y)m(dy)/Z,
    K_y(dU) = exp(-S(U))H_y(dU)/w(y),
    X_eff(y) = v(y)/w(y) = integral X(U)K_y(dU).

Here nu=Q_#mu and K_y is a probability kernel. S_eff is an action relative to the pushed-forward Haar reference m; it is not asserted to be local or to coincide with a published Bałaban density.

For a commuting source eta with eta^2=0,

    integral exp(-S(U))(1+eta X(U))H_y(dU)
        = w(y)(1+eta X_eff(y)).

Therefore, with the vacuum normalization explicitly retained,

    Z^(-1) integral w(y)(1+eta X_eff(y))m(dy)
        = 1+eta integral X_eff(y)nu(dy)
        = 1+eta integral X(U)mu(dU).

This proves exact degree-one transport at finite cutoff under the stated standard-Borel hypothesis. It does not prove a multiscale estimate or a source-polymer interface.

For 1<=p<infinity, positivity and Jensen give

    integral |X_eff|^p dnu <= integral |X|^p dmu.

For ||c+eta x||_r=|c|+r|x|, coefficientwise triangle inequality likewise gives the conditional jet-norm inequality. These have constant one, not a strict contraction factor. A sufficient missing physical estimate is

    sup_(a,t>=t_min,||f||_(H^3)=1) integral |X_eff(y)|nu_a(dy) < infinity.

Bounding this by E_mu_a|X| simply transfers the still-unproved uniform insertion norm. Existing deterministic compactness ceilings diverge with a. The vacuum identity, positivity, and finite-lattice integrability supply none of the necessary cutoff-uniform integrability, flow locality, terminal-scale bounds, or source-decorated activity norms.

## Signed pieces: independent countermodel

A signed mass-one kernel 2 delta_u - delta_v sends the bounded function X(u)=1, X(v)=-1 to 3, although ||X||_infinity=1. Jensen and probability-kernel contraction therefore cannot be applied to individual signed polymer pieces. Their bounds involve total variation and control of normalization denominators. Such pieces may reconstruct a positive Wilson measure when summed, but positivity of the reconstructed measure does not make each piece positive.

## Primary-source summary (under 200 words)

The accessible 2024 author version associated with the 2025 paper defines P^s=a^(d/2)P^u=a^((d-4)/2) ImTr(U_p-1)/g in equations (32)/(82). Section V, Theorem 4, equation (83), gives a periodic finite-volume generating-function bound; equation (84) estimates its one-plaquette source factor. Its denominator exponent includes boundary count Lambda_e. The thermodynamic bound removes that boundary ratio. Remark 16 discusses an action-density variant scaled by a^d. The displayed eigenvalue formulas use U(N); the precise SU(N) extension requires further extraction. These are unflowed scaled plaquette observables. The paper does not supply the target fixed-positive-flow clover energy insertion estimate. The author introduction explicitly distinguishes its finiteness results from direct construction of the ultraviolet limit.

Sources: [author full text, Section V, Theorem 4 and Remark 16](https://arxiv.org/html/2205.07376v2#S5); [2025 publisher record](https://www.sciencedirect.com/science/article/pii/S0034487725000357). Exact introductory locator: Section I, paragraph beginning “Of course, this finiteness properties”. Exact field locator: equations (32) and (82).

## Independent algebraic analysis of the source bound and corrected target diagonal

Write gamma=a^(d-4)/g^2. Substituting the upper and lower one-plaquette factors gamma^(-N^2/2) into equation (83) leaves, per source factor, the boundary factor

    gamma^[2^(d-1) N^2 Lambda_e/(r Lambda_s)].

For a fixed finite lattice with nonzero Lambda_e, this displayed upper estimate can grow as g->0. This observation does not disprove uniformity of the actual generating function. More importantly, it is NOT an obstruction on the YM-015F physical-volume diagonal.

Indeed, if L_sites=L_phys/a and Lambda_e/Lambda_s=O(1/L_sites)=O(a), then in d=4 on the asymptotically-free trajectory gamma=1/g_0^2=O(log(1/a)). The logarithm of the combined boundary factor is O(a log gamma)=O(a log log(1/a)), which tends to zero. Thus that boundary factor tends to one on the target diagonal. This corrects any inference from the fixed-site g->0 observation to a target-diagonal failure. The count ratio must be verified under the paper's exact geometry when this analysis is formally imported.

The observable mismatch remains independent of the boundary correction. Restoring a physical unscaled field introduces inverse powers of a, and no bound for its fixed-flow image follows from the rescaled unflowed bound alone. Further, for the fundamental SU(2) representation every group element has real trace, so ImTr(U_p-1)=0 identically. Its trace-field generating function is then trivial although quadratic clover energy need not vanish. This is an elementary algebraic diagnostic of the mismatch, not a criticism of the source theorem for its stated observable. Remark 16's action-density variant still requires exact coupling normalization and flow transport before application to YM-015F.

## Remaining primary extraction and epistemic boundary

The bounded search did not retrieve verified accessible full-text CMP 122 Theorem 1. Publisher abstracts verify the historical 4D vacuum-stability scope, but no exact source norm or insertion premise is imported from an abstract. This receipt establishes finite-cutoff conditional identities and records a candidate primary-source route; it does not establish YM-015F-L1, a nonperturbative cutoff-uniform moment theorem, reflection positivity for flowed fields, nontriviality, or a mass gap.
