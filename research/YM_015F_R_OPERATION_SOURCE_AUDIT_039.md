# YM-015F — R-operation source audit 039

Candidate for independent review. Read constrained-coordinates038 and terminal037. This is bounded primary-source progress, not an all-sector source-flow construction.

## Access and bounded extraction

On 2026-10-05, ordinary PowerShell HTTP access to the [Euclid issue page](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-122/issue-2) identified R-I as `cmp/1104178393`. Its [public download](https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104178393) returned HTTP200, application/pdf, 2,826,369 bytes, 28 pages. Extracted in memory; rendered printed176/PDF2 and printed201/PDF27 in memory and visually checked. Read printed175–180 and198–202, not the whole paper. Python urllib separately returned a one-page Incapsula denial; that response was not treated as the article. No access bypass or paid access was used. The [publisher record](https://link.springer.com/article/10.1007/BF01257412) remains a subscription preview. R-I DOI is BF01257412; BF01238433 in038 identifies R-II.

Primary-derived extraction below is under200 words in total:

Printed176,(0.3):

    (R rho)(V) = sum_Z rho(Z'',V)
       [integral dV|_(Z') rho(Z,V)] /
       [integral dV|_(Z') rho(Z'',V)].

This introductory representation splits Z into components Z' requiring renormalization and Z'' retaining sufficient small factors. Printed177 explicitly cautions that the actual denominators integrate localized parts, not whole densities. Printed201,(1.100), defines R', only a basic part of R; its component quotient is

    delta_(G_i)(V') chi(Lambda_i)
    exp[-g_k^(-2) A(zeta_i,U_(k,X_i)(V'_k V_(Lambda_i)))]
    / integral dV'|_(Lambda_i) delta_(G_i)(V') chi(Lambda_i)
      exp[-g_k^(-2) A(zeta_i,U_(k,X_i)(V' V_(Lambda_i)))].

This is one factor of (1.100), not its complete expression. G_i fixes axial gauge; graph averaging restores Euclidean invariance with N_i=1/(2^d d!). Printed201,(1.102), states

    integral dV_k (R' rho_k)(V_k) = integral dV_k rho_k(V_k).

Printed177 conditions(i),(ii) select components fitting100MR_k cubes with no new large-field regions in preceding N steps. Printed200 retains other components and varying integral operations. Printed202 postpones localization, polymer expansion and exponentiation to R-II.

## Own interpretation and obligations

The exact numbered introductory representation (0.3) now has direct visual evidence. It must not be promoted into the actual full operator: the author's printed177 qualification prevents that. The visually checked quotient from(1.100) improves the dictionary for the actual basic operation, but this audit deliberately does not transcribe or reconstruct the remaining nested summations, characteristic functions, background maps and integrations of that equation.

The normalized local quotient integrates to one in its specified local variables when its denominator is finite and positive. That observation identifies a conditional normalization interface; it does not establish a single positive conditional measure representing every sector of the physical Wilson law. The remaining integrations and sector sums of(1.100) must still be retained, including the components outside conditions(i),(ii). Their precise admissibility, support, positivity, integrability and reconstruction require inspection of the complete source chain.

Equation(1.102) is a vacuum integral identity for the author's transformed density. For selected marked/source coefficients, terminal037 still requires equality of the corresponding integrals, not merely vacuum equality. Source dependence in local denominators would generate inverse scalar jets or variable-dependent factors; those must be derived from a verified source-decorated representation and restored before global normalization. Graph averaging, gauge fixing, constrained coordinates from038, cutoff support, Jacobians and local background dependence must accompany each transported insertion.

The final coarse law, its terminal functional and reference density must be identified from the actual full representation. No uniform marked numerator estimate, terminal density-ratio bound, source-counterterm estimate or marked large-field summability follows from(1.102). Excluding the unselected components would lose the global observable. No all-sector uniform flowed estimate, continuum/OS construction, mass gap or closure is claimed; the analytic obligations exposed in037 remain open.

## YM-040 candidate: exact localized quotient jets and their normalization defect

This section is our conditional finite-algebra derivation, not a further extraction of (1.100). The complete basic R-prime dictionary and R-II localization remain OPEN. The source locators above retain precisely their stage039 scope; this stage imports no new primary-source claim.

Fix k distinct nilpotent source labels, z_i^2=0, and a parameter y representing all exterior/background variables, graph choice, sector choice and retained constraints. Let m_y(dx) be a source-independent positive local measure. Gauge deltas may enter this hypothesis only after their meaning as a positive measure has been established; a formal distribution is insufficient. Suppose

    L(z,x;y)=sum_S L_S(x;y) z_S,
    D_S(y)=integral L_S(x;y) m_y(dx),
    0<D_empty(y)<infinity,

with every L_S absolutely integrable, and L_empty>=0. These are assumptions, not verified properties of every factor in the gauge RG. Define Q=L/D in the finite source algebra. Division exists because D_empty is nonzero. If Q_S denotes its coefficient, exact disjoint-subset multiplication gives

    Q_empty=L_empty/D_empty,
    Q_S=L_S/D_empty
        -sum_(nonempty B subset S) [D_B/D_empty] Q_(S\B).
    integral Q_empty dm_y=1; integral Q_S dm_y=0 for nonempty S.

Proof: D Q=L, solve each coefficient by increasing |S|; integrate and use the same recursion inductively. At degree one Q_i=L_i/D_empty-(D_i/D_empty)Q_empty. At degree two

    Q_ij=L_ij/D_empty
       -(D_i L_j+D_j L_i+D_ij L_empty)/D_empty^2
       +2 D_i D_j L_empty/D_empty^3.

The coefficient 2 comes from the two ordered disjoint singleton products. This quotient is a normalized source-dependent kernel jet, not the raw marked conditional expectation. In the special exponential-marking case L_S=L_empty product_(i in S) X_i, its first derivative is Q_empty times X_i-E_(Q_empty)X_i. Thus integrating Q_i alone gives zero, whereas the conditional insertion is D_i/D_empty. This normalization subtraction is unavoidable. Source-dependent local measures, domains, cutoffs, gauges or coordinate maps must first be incorporated into L (or differentiated with their own justified rules); the displayed formula does not discard their derivatives.

### Exact restoration and exterior-variable dependence

As jets, L/D_empty=(D/D_empty)Q. Both sides must remain inside exterior integration when D depends on y. In particular, for a source-independent local test F with integrable selected products,

    integral F L_S dm_y / D_empty
      =sum_(B subset S) [D_B/D_empty] integral F Q_(S\B) dm_y.

This is the exact local compensation identity. It is not an assertion that inserting a physical source into the author's vacuum quotient produces the source-decorated R-prime operation. That operation must still be defined and matched to the Wilson source jet. If a proposed transformed density has an identified outer jet H(z,y), sector sum and terminal functional, every H coefficient and every D/D_empty factor used in restoring the fine density requires the same disjoint-subset convolution before the actual global vacuum normalization. An exterior-dependent D cannot be extracted as a global scalar; a nonconstant terminal weight incurs the stage037 change-of-measure cost. Vacuum equality (1.102) supplies none of these marked identities.

The exterior dependence creates an exact covariance defect already at two labels. For a fixed positive exterior probability nu and jets C=D/D_empty, T=integral F Q dm_y, the difference between nu(CT) and nu(C)nu(T) in degree {1,2} is

    Cov_nu(C_empty,T_12)+Cov_nu(C_1,T_2)
      +Cov_nu(C_2,T_1)+Cov_nu(C_12,T_empty).

Here C_empty=1, so the first term vanishes. Covariance uses bilinear multiplication, without conjugation. It is valid when all indicated products are integrable. At any degree S the defect is sum_(B subset S) Cov_nu(C_B,T_(S\B)). This identifies the error from replacing a background-dependent jet by its exterior mean even when the mean is accurately computed.

Own finite diagnostic: exterior y=0,1 equiprobable; local x=0,1 equiprobable under m_y; let h(0)=0,h(1)=2 and m(0)=0,m(1)=1. Set

    D=1+z_1 h(y), Q=1+z_2 m(y)(2x-1), L=D Q, F=2x.

Then integral Q dm_y=1, integral L dm_y=D, L_empty=1 and D_empty=1. Thus this is a valid instance of the local pair assumptions, with finite integrable coefficients. The terminal test gives T=integral F Q dm_y=1+z_2 m(y). The degree12 coefficient of nu(D T) is nu(h m)=1; replacing D by nu(D) gives nu(h)nu(m)=1/2. The defect is1/2. Formal inverse jets are valid; if positive real source interpretation is desired, taking |z_1|<1/2 and |z_2|<1 keeps the corresponding ordinary affine factors strictly positive before nilpotent truncation. This example is unrelated to an actual gauge RG law.

For sectors, distinguish the target fixed-vacuum normalization rho(P(z))/rho(1) from the different source-normalized expectation rho(FP(z))/rho(P(z)). Suppose actual positive vacuum sector measures rho_alpha give source partition jets Z_alpha(z), normalized sector jets J_alpha=Z_alpha(z)/Z_alpha(0), and vacuum weights p_alpha=Z_alpha(0)/sum_beta Z_beta(0). Then the fixed-vacuum source jet is sum_alpha p_alpha J_alpha. If a source-dependent conditional sector law divides by Z_alpha(z), restoring the marked numerator requires J_alpha as well as p_alpha. The alternative source-normalized law has formal weights Z_alpha(z)/sum_beta Z_beta(z) and is a different target; it cannot silently replace the chosen Gibbs generating jet. For countably many sectors require summability of integrals of absolute values of every selected marked coefficient and every selected compensation product under the actual exterior/terminal law. Summability of vacuum weights alone is insufficient. Signed activity representations require total variation and the actual reconstructed vacuum denominator as in037.

### Conditional finite norm cost

With the existing weighted coefficient norm, write U=D/D_empty-1 and u=||U||_r. The ideal of positive-degree elements has (k+1)st power zero. Therefore

    (1+U)^(-1)=sum_(j=0)^k (-U)^j,
    ||Q||_r <= [||L||_r/D_empty] sum_(j=0)^k u^j,
    integral ||Q||_r dm_y
       <= [integral ||L||_r dm_y/D_empty] sum_(j=0)^k u^j.

Proof: finite geometric identity and submultiplicativity; coefficientwise integrability permits the last finite sum. No condition u<1 is needed for finite k. Nevertheless u, normalized marked input norms, their products across scales and exterior/terminal integration may depend on the cutoff. This is a conditional interface bound, not strict RG contraction, an analytic source disk, or a uniform flowed-observable bound. Positivity is assumed only for Q_empty; nonempty coefficients are generally signed even when the vacuum kernel is positive.

### Falsification experiment: omitted denominator derivative

Use the probability measure on x in {0,1} with both weights 1/2, one source z^2=0, and L=1+zx. Then D=1+z/2 and Q=1+z(x-1/2). Taking F=x gives

    integral F L_1 dm=1/2,
    integral F Q_1 dm=1/4,
    integral F Q_1 dm+(D_1/D_empty) integral F Q_empty dm=1/2.

Hence replacing the source-decorated local density by its normalized quotient and dropping its denominator jet changes a marked coefficient, despite identical vacuum integrals. This finite countermodel falsifies that shortcut only. It is not a counterexample to Bałaban's construction or to any continuum theorem. Writer executed Python Fraction checks of this example and the exterior covariance example: results (1/2,1/4,1/2) and (1,1/2,1/2), all assertions passed. Root E3 must independently verify the frozen candidate; this writer check is not independent acceptance.

### Remaining operator dictionary / smallest next obligation

For every quotient actually occurring in the complete (1.100), determine its integration variables and reference measure; graph weights; axial constraint and gauge transformation; cutoffs and localized action; background dependence; source numerator; source denominator; source dependence of coordinate maps; sector selection and retained unselected components; outer factors and terminal functional. Prove the resulting all-sector marked integral identity against the original normalized Wilson jet. The formulas above specify the coefficient obligations for a verified local pair (L,D), not that entire dictionary. R-II localization and any uniform marked/terminal estimates remain OPEN. No numbered 4D Failure Atlas edge advances in this section; its source-tree/regrading and all-subtree hypothesis obligations remain independent. Structural no-go count stays zero and no continuum edge closes.
