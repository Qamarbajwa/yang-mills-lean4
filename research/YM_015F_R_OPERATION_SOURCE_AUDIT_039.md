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

Here C_empty=1, so the first term vanishes. Covariance uses bilinear multiplication, without conjugation. For every indicated B, assume C_B, T_(S\B), and their product are individually absolutely integrable under nu; this makes both separate means and the product mean finite. Product integrability alone is insufficient: on y in (0,1) with uniform nu, C_1(y)=1/y and T_empty(y)=0 have integrable product but an undefined separate mean nu(C_1). The initial candidate wording was challenged before acceptance and is superseded by this explicit hypothesis. At any degree S the defect is sum_(B subset S) Cov_nu(C_B,T_(S\B)). This identifies the error from replacing a background-dependent jet by its exterior mean even when the mean is accurately computed.

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

## YM-041 candidate: predecessor-chain and retained-branch dictionary

Ordinary PowerShell public HTTP access succeeded again on 2026-10-05. Host Python fitz extracted printed177,190–202 in memory; printed201 was independently visually inspected at C:/Users/arqam/AppData/Local/Temp/YM041_RI_p201.png. No PDF denial page, subscription preview or OCR-only reading was substituted for that visual check. Same R-I public source and DOI as039. This adds numbered predecessors, not a full transcription of (1.100).

New primary-derived paraphrase/table below is under200 words; no additional direct quotation:

| Locator | Bounded dictionary |
|---|---|
| 177,(1.1) | Selected components factorize; the complementary operation is retained, usually omitted from intermediate displays. |
| 192,(1.71)–(1.73) | After N preliminary integrations, Lambda is a one-layer enlargement of the new region; its variables are integrated out. |
| 193,(1.75) | A unity split imposes exterior-extension regularity; failing components leave the selected class. Transformations so far preserve the density. |
| 194,(1.76) | Subsequent Lambda integration replaces density equality by equal-integral equivalence. The two integration regions are disjoint; the first is left unchanged. |
| 195,(1.81)–196,(1.82) | Fluctuation coordinates use the background; tree gauge and another unity split restrict surviving components. |
| 197,(1.88)–198,(1.89) | Additional large-field branches further shrink the selected union; cutoff removal uses the resulting restrictions. |
| 200–201,(1.99) | Complementary operations include all intermediate branch forms. Component integrations factorize; histories are localized to each component. |
| 201,(1.100) | Outer sum retains complementary regions/operations; selected-component sum includes n=0. Each product factor retains graph averaging, local quotient, remaining integrations and cutoffs. |

### Own marked-transport consequence

The selected union is not a permanent label attached only to the initial geometric conditions. A reconstruction must track its successive changes and carry each rejected branch into the complementary operations. Reading the displayed selected formula while forgetting the author's convention of omitting the complementary operation loses sectors. These are bookkeeping obligations; no quantitative suppression of those branches is inferred here.

The source's distinction between representation equality before the later integration and equal-integral equivalence after it identifies a separate marked gate even before adding local denominator jets. Suppose an integration replaces a density by a function independent of integrated variables. Vacuum equality alone cannot justify retaining the original observable unchanged. Our finite diagnostic: on x=0,1 with reference probabilities1/2, take density rho(0)=0,rho(1)=2. Integrating its only variable gives constant density1. Both vacuum integrals equal1, but the original test F(x)=x has marked integral1 under rho and1/2 under the replacement. This falsifies an unchanged-observable shortcut, not the source operation. Correct conditional transport of F gives constant1 in this example and restores the marked integral. An actual gauge source lift must derive that transport jointly with every changed operation, source-dependent map, gauge restriction, cutoff and compensated denominator, rather than infer it from (1.102).

This stage locates a finite part of the actual dictionary. It does not reconstruct all admissible histories, domain intersections, boundary bond conventions, reference measures, backgrounds or source-decorated operations in (1.100). The n=0 convention ensures no selected component is required; it does not prove positivity or summability of complementary terms. R-II localization, all-sector marked equality, terminal law and cutoff-uniform analytic estimates remain OPEN. Atlas regrading/all-subtree hypotheses and the earliest numbered4Dfailure are unchanged. No scientific edge closes and structural no-go count remains zero.


## YM-042 candidate: first density-changing integration and its degree-one gate

Ordinary public PowerShell HTTP again acquired the same 28-page R-I PDF on 2026-10-05; host Python fitz read printed193–196 in memory and rendered printed193/194. Writer visually inspected printed194, including (1.76). Printed193 is text-inspected only. No primary PDF is stored in the scientific tree. New source-derived dictionary below is under200 words, without direct quotation; exact boundary/intersection typography outside these bounded descriptions is not certified.

| Locator | Newly bounded operation dictionary |
|---|---|
| 193,(1.75) | Exterior configuration on Z intersect Lambda-complement is tested for a regular extension; rejected components join the retained complement. |
| 194,(1.76) | For each summand Lambda variables are integrated. The resulting function is independent of them; integration regions can differ between summands. |
| 194,(1.76) | First integral uses V_h on Z_h and retains its cutoff and T_h operation. Second integral uses V-double-prime on its specified B-double-prime_k subset intersecting Lambda and Z_h-complement; it retains chi-prime_k and exp(A-prime_k). The integrals have disjoint regions; the first remains unchanged. |
| 194,(1.76)–(1.78) | Delta constraints have already been integrated out here. The variational problem uses regularity restrictions; the minimizing orbit depends on exterior fields. |
| 195,(1.79)–(1.81) | U_0 is built from that exterior-dependent minimum; fluctuations use V-double-prime=V-prime V_0 on B_0. |
| 195–196,(1.81)–(1.82) | Tree gauge is imposed later on B_0, then a fluctuation unity split rejects additional components. |

### Own finite premise, tied to (1.76) rather than inferred from it

The newly distinguished integration is before the later tree gauge delta; treating that later delta as already part of the (1.76) measure would misorder the source lift. The first, unchanged integral and omitted complementary T_k operations remain in the outer bookkeeping. Neither reading supplies positivity of every term or reconstruction of its effective action.

For one fixed admissible history alpha, let x denote precisely its Lambda variables eliminated by this density replacement; let y retain the exterior variables, V_h variables of the unchanged first integral, and all unintegrated variables. This is a proposed finite dictionary, not a completed bond-by-bond transcription of (1.76). Hypothesis H042 requires a source-independent measurable assignment of these coordinates and product positive probability reference m_alpha(dy) h_(alpha,y)(dx), with the actual support indicators placed in the integrand. If a constrained reference replaces product Haar, its measure interpretation and total mass must first be proved. Domain variations with alpha are retained; no single common domain is assumed. Fixed physical Wilson-flow marking changes the density on a fixed finite lattice, but its representation through these histories/coordinates has not been verified.

Assume rho_(alpha,0)(x,y)>=0 is measurable and integrable, X_alpha is a finite complex-valued measurable function, and rho_(alpha,1)=rho_(alpha,0) X_alpha is absolutely integrable jointly. Define

    R_(alpha,0)(y)=integral rho_(alpha,0)(x,y) h_(alpha,y)(dx),
    R_(alpha,1)(y)=integral rho_(alpha,1)(x,y) h_(alpha,y)(dx).

On fibers with 0<R_(alpha,0)<infinity set X_eff=R_(alpha,1)/R_(alpha,0); set it zero on zero fibers. Fubini gives R_(alpha,1)=0 almost everywhere on zero fibers, since rho_(alpha,0)>=0 and rho_(alpha,1)=rho_(alpha,0)X_alpha. Exceptional infinite fibers have m_alpha-measure zero by joint vacuum integrability. The displayed identities hold almost everywhere; exceptional fibers may be modified to zero without changing either integral. Thus

    R_(alpha,0)(1+z X_eff)=R_(alpha,0)+z R_(alpha,1), z^2=0,
    integral R_(alpha,1) dm_alpha=integral rho_(alpha,1) dm_alpha dh_alpha,
    integral |R_(alpha,1)| dm_alpha<=integral |rho_(alpha,1)| dm_alpha dh_alpha.

Proof: integrate both coefficients and use triangle inequality. Reference probability mass is essential when the integrated result is lifted back to a function of x; a nonunit fiber mass produces an extra factor. A merely signed vacuum summand has no positive conditional-kernel interpretation and may have zero R_0 but nonzero R_1. Direct coefficient integration still makes sense under absolute integrability; division or Jensen then needs separate justification. This is a conditional first-degree lift of the specified elimination, not the actual source-decorated R-prime operation.

For finitely/countably many actual histories require sum_alpha integral (rho_(alpha,0)+|rho_(alpha,1)|) dm_alpha dh_alpha<infinity in the positive formulation, or absolute values of both coefficients for signed representations. All rejected and n=0 histories are included. Divide the summed marked coefficient by the actual global vacuum denominator, not a history denominator or source-dependent partition. Remaining T operations, the later background/fluctuation coordinate change, gauges/cutoffs and terminal law must transport this jet in turn; source derivatives of changed maps or domains cannot be discarded. The displayed L1 estimate carries existing integrability and gives no cutoff-uniform flowed input bound or terminal change-of-measure control.

### Failure record and next load-bearing obligation

Positive finite disintegration from stage035 applies to the physical Wilson law with a specified Borel coarse map. It does not establish H042 for each effective-action history in (1.76). This audit has not verified the exact reference domains, all effective-action terms, positivity or finite masses needed for that identification. The marked lift is therefore conditional. Next reconstruct those actual reference variables and complementary operations, prove their source-decorated equal-integral identity, and retain all terminal/sector coefficients before seeking uniform estimates. Vacuum equivalence alone does not discharge that gate. No source operation, continuum edge or earliest numbered4Dfailure is closed; structural no-go count remains zero.


## YM-043 candidate: inherited reference and normalization obligations

Ordinary public PowerShell access obtained the same R-I PDF on 2026-10-05. Host fitz extracted printed177–195/202; writer visually inspected printed188, including the first portion of (1.60). Initial extraction failed only from stdout encoding, then succeeded with UTF-8. No source PDF was stored. Exact normalization-symbol typography and full inherited definitions are unaudited; the preliminary notification's tentative prefactor symbol is not certified.

New primary-derived dictionary (under200 words total with the transfer entry; no direct quotation):

| Locator | Bounded reference/factor evidence |
|---|---|
| 182,(1.25) | Preliminary integration retains fluctuation A variables, a Gaussian quadratic form, constrained V variables and gauge-fixing factors. |
| 187,(1.53)–188,(1.60) | V fluctuations are logarithmic; delta constraints are linearized, removed using C, then variables are coupling-rescaled. An additional A integration remains. The displayed transformed integral retains a normalization prefactor, two Gaussian integrations, interaction terms and background action. |
| 189,(1.60)–(1.62) | Constant E refers to [III](3.15); new boundary terms collect successive integration contributions and Wilson-action renormalization. |
| 195,(1.81) | Boundary-intersecting bonds belong to B_0 at the Lambda boundary, but not at the other stated boundary. Measure and integrand are gauge invariant before the later tree gauge. |
| 202,References | [III] is CMP119243–285; [I] is CMP109249–301. |

### Own disposition of H042

This advances the predecessor dictionary: the already-eliminated constraints in (1.76) are connected to an explicit earlier linearization/C-elimination/coupling-scaling chain, with surviving A integration and normalization/background factors. It does not make those fluctuation references probability measures. A Gaussian quadratic factor alone supplies neither its normalization nor the total mass after cutoffs and interactions; those factors cannot be erased merely because the final density is considered independent of eliminated variables.

The physical compact-group Wilson probability reference established in035 is still a different identification from H042 for effective-action histories. We searched the entire extracted R-I text for Haar/measure/normalization terminology; that search did not locate an explicit unit-total-mass Haar convention for the reference of (1.76). This is a bounded search limitation, not proof the convention is absent in the source series. Gauge invariance on195 is affirmative evidence for the stated symmetry, not positivity, unit mass or source-independent disintegration. Exact prefactor/Jacobian reconstruction and inherited [III] integration conventions remain OPEN, as do each history's support, nonnegative effective density, summability and all complementary operations. The noted boundary convention prevents identifying the integrated coordinate set solely by interior sites.

Next load-bearing source task: reconstruct [III](2.21),(3.15),(3.25) and [I] Sect2 measures, constants and C-elimination maps, then match them history-by-history to (1.72)/(1.76). Preserve all prefactors in the global fixed-vacuum marked identity. No actual source-decorated R operation, cutoff-uniform insertion estimate, terminal bound or continuum edge is proved; structural no-go count0.


## YM-044 candidate: inherited integration split and retained constants

Public primary [III], Bałaban, Convergent Renormalization Expansions for Lattice Gauge Theories, CMP119243–285, DOI10.1007/BF01217741: https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104162401 . Euclid issue119/2 provided this identifier. Ordinary PowerShell downloaded on2026-10-06; host fitz opened44 PDF pages (printed243 at index0); article ends285. Text inspected243,257,258,267,268,269,270; visually inspected258,267,268,270. Local PDF/images remain in host TEMP outside the scientific tree. Initial publisher content/pdf response was3038 bytes HTML, not a usable PDF; an initially guessed Euclid identifier was inaccessible and supplied no evidence. Exact full operator typography is not transcribed or certified.

New primary-derived paraphrase, under200 words across this audit and transfer:

| Locator | Bounded inherited dictionary |
|---|---|
| 258,(2.20)–(2.21) | Ordered one-step operations integrate gauge variables on Omega_(j+1) intersect X, and fluctuation variables on Z_(j+1) intersect Omega_(j+1) intersect X. Quadratic couplings across components enter boundary terms. R changes characteristic functions; fluctuation domains may become empty. |
| 267–268,(3.15) | Constraint linearization, C-elimination and coupling scaling precede an integral retaining normalization constants, a bond-factor product, cutoff and fluctuation/background interactions. |
| 270,(3.23)–(3.25) | The Lambda_(k+1) fluctuation integral is conditional; remaining fluctuation integration on Omega_(k+1) intersect Lambda_(k+1)-complement enters the new T operation. Constants from the first exponential of (3.15) become E_0^(k); the bond-factor product persists in the last integral. |

### Own marked-interface consequence and falsification boundary

This is a concrete placement dictionary for inherited factors, not a normalized effective-history reference. Any proposed reconstruction of H042 must keep the conditional inner integration and residual T integration distinct. Their support restrictions and retained constants cannot be merged into a unit-mass kernel by notation. A conditional integral here is an integral with other variables retained; the word alone does not establish a probability conditional expectation. Neither its constrained gauge measure nor its fluctuation measure has been identified with the positive probability reference needed by H042. Exact measure conventions, all Jacobians, full bond factors, effective-action positivity and global source/vacuum normalization remain OPEN.

The ordinary source text confirms where constants are retained. Their values, complete defining formulas from [I] Sect2, and a history-by-history match to R-I(1.60)/(1.76) remain unaudited; no exact prefactor symbol from043 is rehabilitated. Empty fluctuation domains need their actual integration convention and retained gauge/cutoff factors, rather than automatic deletion of the history. Boundary action terms require the same source marking as retained interior terms. Next reconstruct [I] Sect2 measure/Jacobian/C conventions and instantiate one actual history's full fixed-vacuum marked identity, including residual operations and terminal law. The source's convergence scope remains superrenormalizable; this dictionary grants no four-dimensional convergence, cutoff-uniform insertion estimate or continuum edge closure. Structural no-go count0.
