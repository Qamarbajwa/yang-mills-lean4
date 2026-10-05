# YM-015F — terminal and sector normalization, stage 037

Candidate, pending independent review. These are finite identities and conditional estimates, not a cutoff-uniform flowed insertion theorem. Read together with the accepted 034 reconciliation and 035/036 source transport. No assertion below reconstructs the unverified all-sector Bałaban operator.

## Terminal functional and extracted source factors

Use the finite commutative algebra z_i^2=0 with coefficients indexed by subsets. For fixed cutoff let W_0(z) be an unnormalized integrable jet. Assume source-independent linear integration maps L_0,...,L_(R-1) are defined coefficientwise, and a source-independent terminal functional lambda_R is defined on the final coefficients. Write W_R=L_(R-1)...L_0 W_0. Assume the actual initial terminal functional satisfies the exact identity lambda_0=lambda_R L_(R-1)...L_0 on every selected coefficient, not only on the vacuum. Then, with Z=lambda_R W_(R,empty)>0,

    G(z)=lambda_0 W_0(z)/Z=lambda_R W_R(z)/Z.

Proof: the assumed functional identities and finite coefficientwise linearity. They are obligations to verify for an actual map. Vacuum equality alone does not imply marked equality. No number of formal integration steps proves the premise.

If the exact final density has the form W_R(z)=C(z) V_R(z), where C is a scalar jet independent of terminal variables and C_empty is nonzero, then

    G(z)=[C(z)/C_empty] [lambda_R V_R(z)/lambda_R V_(R,empty)].

Every mixed coefficient is the disjoint-subset convolution of these two normalized jets. If several scalar factors were extracted, C is their product, including any inverse source-normalization jets that the exact representation requires. A factor depending on terminal variables must instead remain inside lambda_R; it cannot be pulled outside by this argument. Dropping C changes marked observables even when C_empty=1. This identity does not specify which source factors arise in the actual gauge RG.

## Positive all-sector mixture, not positive polymer activities

At a fixed cutoff suppose the actual positive unnormalized measure has an exact finite or countable decomposition rho=sum_alpha rho_alpha into positive finite measures. For countably many sectors assume absolute summability of every selected marked integral. Let Z_alpha=rho_alpha(1), Z=sum_alpha Z_alpha>0, and discard zero-mass sectors (their positive measures are zero). Let P(z)=product_i(1+z_i X_i). Define sector jets J_alpha=rho_alpha(P)/Z_alpha and p_alpha=Z_alpha/Z. Then

    rho(P)/Z=sum_alpha p_alpha J_alpha,
    |[z_S]rho(P)/Z| <= sum_alpha rho_alpha(|product_(i in S) X_i|)/Z.

Proof: countable integral additivity under the stated absolute-integrability hypothesis; p_alpha>=0 and sum p_alpha=1. A measurable partition of a finite Wilson configuration space gives such a decomposition, but no claimed RG large-field partition is identified here. Taking logarithms after summation generates inter-sector connected terms; averaging sector logarithms does not reconstruct the global logarithm.

For signed or complex activities the probability-mixture interpretation is invalid. If their selected integrals are absolutely summable and the reconstructed vacuum Z is positive, the triangle bound instead uses total variation |rho_alpha| in each numerator divided by the actual reconstructed Z. Neither summable vacuum values nor positivity of their final sum controls those numerators or the denominator. The signed counterexample of 035 remains binding.

## Terminal reweighting cost

Let nu be a probability, h>=0 measurable with 0<nu(h)<infinity, and nu_h=h nu/nu(h). For a scalar marked coefficient M, or a finite jet M with coefficient norm ||M||_r=sum_S r_S |M_S|, positivity and Holder give

    |nu_h(M_S)| <= nu(h |M_S|)/nu(h),
    ||nu_h(M)||_r <= [||h||_(L^q(nu))/nu(h)] || ||M||_r ||_(L^p(nu)),
    1<=p,q<=infinity, 1/p+1/q=1,

whenever the displayed norms are finite. Proof: triangle inequality coefficientwise, finite summation, and Holder applied to h and ||M||_r. The conventions include p=infinity,q=1, for which the weight factor equals1; p=1,q=infinity needs an L-infinity bound on h. The coarse terminal law is nu_h, not nu. A constant-one conditional bound in L^p(nu) does not alone bound terminal expectations under a changing nu_h. Uniform control requires both the coefficient norms and the terminal density ratio. A deterministic scale count or vacuum-at-identity normalization cannot substitute for this ratio.

Conditional composition: if an exact positive coarse map has M=E[X|Q] and h is measurable in Q, then nu_h(M)=E_mu[h(Q)X]/E_mu[h(Q)]. This is a reweighted fine expectation; it equals E_mu X only with a separately verified representation that compensates the terminal weight, or in a special case such as h constant. This follows directly from conditional integration and makes the changed measure explicit.

## Rare-sector defect and corrected sufficient estimate

Let epsilon in (0,1), mu(B)=epsilon^2, and X=epsilon^(-3) 1_B. The rare-sector probability tends to zero, but E_mu X=epsilon^(-1) diverges. This finite positive countermodel does not concern a physical Wilson measure and is not a structural no-go. It rules out deriving marked control solely from vanishing bad-sector probability.

For an actual measurable bad event B, a scalar mixed insertion F=product_(i in S) X_i, and 1<p<=infinity, Holder gives

    E_mu[1_B |F|] <= mu(B)^(1-1/p) ||F||_(L^p(mu)).

For finite p, a proved mu(B)<=b_a and ||F||_p<=A_a therefore gives the sufficient marked remainder bound b_a^(1-1/p) A_a. It vanishes if that product tends to zero. Under a terminal reweighting the corresponding bound is

    E_(mu_h)[1_B |F|] <= ||1_B h||_q ||F||_p / E_mu h,

where mu_h=h mu/E_mu h and the norms use mu. This is the relevant denominator-sensitive estimate; no uniform b_a,A_a,h estimate for the actual flowed observable is supplied. Mixed products require the appropriate moments, not just a bound for a single unmarked insertion. Terminal weighting and signed sector decomposition require their own hypotheses.

## Representation transfer and exact residual

XFER-YM-TERMINAL-037: conditional change-of-measure/Holder transfer from full positive coarse laws to terminal marked observables. Verified mapping is the finite probability identity above. Missing hypotheses: the exact all-sector source-decorated RG representation, actual terminal reference law/density, uniform normalized density-ratio bounds, physically normalized flowed coefficient bounds, source-factor restoration and summable marked large-field estimates. Allowed conclusion is the displayed estimate only after those hypotheses are discharged. This is our elementary derivation, not a cited theorem imported from an uninspected source.

DAG: the finite terminal functional and mixture identities are interface obligations below OPEN JET-002 and L1. The smallest analytic estimate exposed is a joint marked/terminal ratio bound for the actual representation; a vacuum stability statement or vanishing bad-event probability does not discharge it. E-UV-FLOWED stays PARTIAL_PROGRESS; all continuum/OS/crossover edges remain open, YM-016 BLOCKED, structural no-go count0, goal_complete=false and Clay OPEN_AND_UNSOLVED.
