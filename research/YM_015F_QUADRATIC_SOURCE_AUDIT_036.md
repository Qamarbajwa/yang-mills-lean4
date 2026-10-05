# YM-015F quadratic-source audit 036

Date: 2026-10-05. RAW research proposal, no accepted-state promotion. Inputs: accepted plaquette compatibility 035 and raw JET-002B reconnaissance. No DAG edge, global closure, continuum construction, or mass-gap claim is made.

## Primary-source receipt (under 200 words total)

[Author PDF v2](https://arxiv.org/pdf/2205.07376v2), visually inspected from locally rendered pages and checked against extracted text: printed p.30 (PDF index29), Remark16, prints H=A_p/(a^4 g), S=a^d H. Printed p.31 (index30), Theorem4 eq83 has numerator exponent 2^d Lambda_r/(r Lambda_s), denominator exponent 2^d(Lambda_r+Lambda_e)/(r Lambda_s). Eq84 gives gamma^(-N^2/2) times K exp(pi^2 N |J|^2/8), K=pi^(N^2+N/4) sqrt(N_S)/N_C. The next definition of c'_u visibly prints an additive expression rather than log K. Theorem4 item3 prints constant coefficient 2^d(d-1)/r and source coefficient pi^2 Nr/8. SectionVI.5 starts printed p.34 (index33), and continues p.35 (index34): Holder, multireflection, deletion of actions, factorization, then Weyl/Gaussian domination for a linear source. It contains no explicit quadratic-source integral estimate or determinant-one version. Eq84 also prints equality between the absolute imaginary-trace integral and the sum-of-absolute-sines integral; these generally differ. Remark16's carryover assertion therefore requires a separate derivation and does not specify its uniform source radius.

## Literal discrepancies, independently diagnosed

These are checks on the printed formulas, not a silently repaired author theorem.

1. With U_p=exp(i g a^2 F+...), A_p=||U_p-I||_HS^2=g^2 a^4 Tr(F^2)+higher terms. Printed H has leading g Tr(F^2). Dividing by g^2 instead would change the observable. Keep the printed S=g gamma A_p, gamma=a^(d-4)/g^2.
2. Define c=log K independently. The explicit multiplicative bound in eq84 can be used with c; the printed additive definition of c'_u does not give that identity.
3. Since |sum sin(lambda_j)|<=sum |sin(lambda_j)|, eq84's second integral is an upper majorant, generally not an equality. The proof first uses sqrt(N)||U-I||_HS; this is another majorant. Neither should be identified with the original trace observable by equality.
4. Literal substitution of eq84's multiplicative estimate and z_l>=gamma^(-q) exp(c_l), q=N^2/2, in item2 gives

   exp{2^d(d-1)(c-c_l) + [pi^2 N/8] 2^d(d-1) r sum_j |J_j|^2}.

   This differs from item3 in both coefficients. SectionVI.5 supplies the item2 exponent and no intervening improvement explaining their removal. No corrected theorem is imported. At finite volume the literal product additionally has gamma^[2^(d-1)N^2 Lambda_e/Lambda_s], with constant exponent 2^d[Lambda_r(c-c_l)-Lambda_e c_l]/Lambda_s, as already calculated in035. Its diagonal compatibility does not eliminate the other discrepancies.

## Independent quadratic-source lemma: exact measure and radius

Let G=U(N) or SU(N), normalized Haar sigma_G, A(U)=||U-I||_HS^2=2 sum_j(1-cos lambda_j), 0<=A<=4N. Define

    z_G(t)=int_G exp(-t A(U)) d sigma_G(U),
    d mu_G,gamma(U)=z_G(gamma)^(-1) exp(-gamma A(U)) d sigma_G(U).

This is a single group-matrix Wilson probability measure. It is not the marginal of an arbitrary plaquette in an interacting lattice. All normalizations below are explicit. For c_g>0 set Q=c_g gamma A. The printed Remark16 field has c_g=g; a separately defined conventional action-scaled field has c_g=1. For complex J, positivity gives

    |E_mu exp(J Q)| <= z_G(gamma[1-c_g Re J])/z_G(gamma).

Equality holds for real J. For unnormalized integral the same right side has no denominator. Negative effective t causes no finite-cutoff divergence: compactness gives entire analyticity, and

    |E_mu exp(JQ)| <= exp(4N c_g gamma |J|)

for every J. This all-source bound is generally not cutoff-uniform.

For a uniform disk choose 0<delta<1 and c_g |J|<=1-delta. The effective coupling is at least delta gamma. If k=dim G and gamma>=gamma_min>0, there are constants b_G,B_G>0 such that

    b_G gamma^(-k/2)<=z_G(gamma),
    z_G(delta gamma)<=B_G(delta gamma)^(-k/2).

Thus |E_mu exp(JQ)|<= (B_G/b_G) delta^(-k/2), uniformly in gamma. Constants may depend on G,gamma_min, but not cutoff, J in this disk, or gamma. A direct proof uses exponential coordinates near the identity, A comparable to squared Lie-algebra norm and smooth positive Haar Jacobian; outside that neighborhood A has a strictly positive minimum. For bounded positive t the constants extend by continuity. This proves the group-integral estimate for SU(N) with k=N^2-1, without replacing U(N) eigenvalue formulas by fiat. Under a in(0,1], d<=4, g<=g0, gamma>=g0^(-2).

For printed S, each g has radius (1-delta)/g; for every fixed delta in (0,1), the disk |J|<=(1-delta)/g0 is uniformly bounded over the whole allowed coupling range. The open disk |J|<1/g0 is their union; uniformity is local on compact subdisks, not a bound on its full supremum. For r Holder-amplified sources the sufficient condition is r g0 max|J_j|<=1-delta. For c_g=1 the corresponding radius is 1-delta, or (1-delta)/r after amplification. The distinction changes both normalization and source radius.

The finite-radius result cannot be called an all-source uniform estimate. For fixed c_g=1 and real J=1, E exp(JQ)=1/z_G(gamma) grows like gamma^(k/2); for J>1 it grows exponentially. For the printed S in d=4, gamma=1/g^2 and fixed J are eventually inside the admissible disk as g->0. Nevertheless, for a fixed g with Jg>1 in d=3, gamma->infinity as a->0, and the estimate grows exponentially. Uniformity over the full parameter domain therefore needs the stated disk. This observation does not disprove a distinct d=4-only improvement.

## What a lattice transfer still requires

The single-plaquette lemma is exact for mu_G,gamma only. For a lattice normalized measure dnu=Z^(-1) exp(-gamma sum_p A_p) product_b d sigma_G, one cannot substitute its plaquette marginal by mu_G,gamma. A proposed reflection/deletion derivation for positive quadratic sources must retain a nonnegative coefficient gamma(1-rg|J|) on every sourced retained plaquette, prove the reflected insertion inequality for this observable, and prove the resulting source-decorated factorization against a valid lattice denominator. For SU(N), the local lemma above is proved independently, but an SU(N) lattice reflection/factorization theorem with constants and boundary count is not extracted here. The author PDF's U(N) Weyl calculation is not that theorem.

No flowed uniform clover bound follows. Flow changes links nonlocally over a growing lattice neighborhood at fixed physical time; clover curvature averages several transported plaquettes and its squared trace has a different normalization. An unflowed one-matrix estimate supplies neither a domination of that insertion nor physical-time bounds uniform in cutoff. Source support and Holder amplification can grow with a^(-4), shrinking a naive admissible radius; constants for fixed r do not solve this. Positive full-measure estimates do not automatically apply to signed RG activities.

## XFER-YM-QUADRATIC-036 (conditional proposal)

Source: compact Wilson action integral and independently proved finite-radius shifted-coupling lemma. Target: SU(N), fixed physical four-torus AF diagonal, actual positive-physical-time clover energy tested in H^3.

Required hypotheses: exact target/source normalization including g; proved SU(N) lattice reflected quadratic-source factorization and denominator bound; a flow/clover source domination valid on a cutoff-uniform disk; control of source support growth and all required moments; and normalized marked RG transport if the conclusion is to concern individual activities. Under those hypotheses, bounded holomorphic source functions on that disk give moments by Cauchy estimates, then the independently specified topology/limit arguments may be attempted.

Current admissible conclusion: local compact-group quadratic-source domination and a precise missing lattice/flow lemma. The source formula discrepancies remain explicitly flagged. No global edge closes. Failure classification: METHOD_SPECIFIC_OBSTRUCTION / missing hypotheses, not a structural no-go.
