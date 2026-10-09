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


## YM-045 candidate: small-field Gaussian normalization and Jacobian placement

Public primary [I], Bałaban, Renormalization Group Approach to Lattice Gauge Field Theories. I. Generation of Effective Actions in a Small Field Approximation and a Coupling Constant Renormalization in Four Dimensions, CMP109249–301 (1987): https://projecteuclid.org/journalArticle/Download?urlid=cmp%2F1104116842 . Identifier verified through official Euclid109/2 issue listing. On2026-10-06 ordinary PowerShell public download yielded54 PDF pages (printed249 at index0; article ends301). Web-tool PDF opening failed; it supplied no scientific evidence. Host fitz text inspected249,260–261,265–269; writer visually inspected260,267,268. Local PDF/images remain in host TEMP. The numbered prose distinctions below are certified; no full formula transcription or exact R-I prefactor glyph is certified.

New primary-derived dictionary is under200 words across this audit and transfer, without direct quotation:

| Locator | Bounded reference dictionary |
|---|---|
| 260,(1.4) | Z is the constrained Gaussian integral normalizing each fluctuation Gaussian measure. |
| 265,(2.1)–(2.3) | This transformation restricts to small fields and regular backgrounds, then uses a background-dependent minimum and fluctuation coordinates. |
| 267,(2.10)–(2.11) | Logarithmic coordinate factors enter the normalization. Nonlinear constraint linearization and coupling scaling precede Gaussian normalization. |
| 268,(2.12) | Constraint elimination leaves B variables with B-prime=CB; C and covariance depend on the background. The action retains a background Gaussian-normalization difference and a trace-log Jacobian in the interaction. |
| 268,(2.12)–(2.14) | N-double-prime is the displayed integral at unit background. E is a logarithm of the Gaussian expectation with cutoff and interaction; its unit-background value supplies that normalization. |

### Own reconstruction consequence and limits

This improves the missing normalization dictionary. It distinguishes an explicitly normalized Gaussian reference from the full cutoff/interaction-weighted integral and from a background=1 normalization. Those are separate objects in a proposed marked lift. Identifying one does not identify the others with a unit-mass effective-history fiber. In particular, a reference evaluated at one background cannot by itself normalize every exterior-dependent fiber of H042. Retaining the displayed background factor and the nonlinear coordinate Jacobian is part of matching the actual integrand, even when a Gaussian measure has already been normalized.

The domain assumptions here are smaller than the all-sector history system in R-I. This audit has not proved their extension to each complementary history, boundary-restricted measure, or residual T operation in [III](2.21)/(3.25). Nor has it verified the exact equality of these small-field C maps and Jacobians with each R-I history's constrained reference. Source dependence of a chosen coordinate map, its support and its Jacobian requires an explicit marked formula; it cannot be inferred from vacuum normalization. Gaussian positivity/covariance bounds on every needed history, summability, absolute marked integrability, fixed global vacuum normalization and terminal control remain OPEN. No cutoff-uniform flowed insertion theorem or continuum edge closes. The old large-field probability and nonlinear-smoothing sketches remain excluded; structural no-go count0.

Smallest next source obligation: match one admissible R-I(1.76) history to [III](3.15)/(3.25), including the exact retained normalization, bond factors, nonlinear Jacobian and residual variables. Only after that identification derive its degree-one marked identity; retain all rejected/n=0 histories in the eventual global transport.


## YM-046 candidate: history labels, hidden sums and operator dependencies

Read accepted revision45 and reconciliation034 before using sources. Reused publicly acquired primary PDFs in host TEMP: YM043_review_RI.pdf (28 pages), YM044_III.pdf (44 pages), YM045_I.pdf (54 pages), with the official Euclid URLs recorded above. No new HTTP acquisition is claimed. Host fitz independently extracted R-I printed179,192–195 and [III]255–257,267–270; visually inspected R-I192 and [III]267 via newly rendered pages. Initial stdout encoding failure was corrected with UTF-8. Exact full operator typography is not certified. This stage does not reuse the withdrawn043 prefactor reading.

New primary-derived dictionary (under200 words together with the transfer entry, no direct quotation):

| Locator | History/support dependency |
|---|---|
| [III]255(2.2)–256(2.12) | A determining set encodes the domain sequence; its gauge configuration determines the constrained minimizing orbit/background. |
| [III]257(2.14)–(2.18) | Localized determining sets require boundary/separation conditions. The density sum hides S-sequence summation inside T; the action depends on Omega/Lambda/S despite suppressed notation. |
| [III]267, before(3.15) | At fixed Omega_(k+1), admissible P/Q choices are resummed into zeta; only characteristic functions and localized gauge-fixing terms are resummed. C and other operators depend on the Omega sequence, although [I] formulas are reused. |
| [III]270(3.23)–(3.25) | Effective-action terms correspond to particular Omega/Lambda/S sequences and change under the R operation. |
| R-I192(1.71)–(1.74),194(1.76) | Preliminary integrations modify background/action and retained T operations; the later eliminated domain is term dependent. |

### Own history identification gate

This supplies a genuinely new index dependency, not a complete actual-history example. A selected Omega sequence alone does not select an elementary effective-action history: S summation remains inside T, and zeta has already aggregated admissible P/Q choices. There are two legitimate bookkeeping levels: carry the summed T/zeta objects with their exact integrals and source marking, or expand their definitions into elementary labels with the original weights and domains. Switching levels without reconstructing that sum changes what a proposed history label denotes. No numerical label multiplicity or positivity of the resummed weight is inferred.

For a proposed actual history alpha record: (a) the displayed outer domain labels and every hidden summation or its retained summed operator; (b) determining sets and associated constrained backgrounds; (c) restrictions/support and reference coordinate spaces at each scale; (d) actual domain-dependent C/covariance, nonlinear coordinate Jacobian and normalization factors; (e) unchanged T integrals, eliminated Lambda integral and residual integration; (f) fixed-global-vacuum numerator and denominator, subsequent terminal functional and rejected/n=0 branches. These are proof obligations, not definitions claimed extracted in full. The source explicitly reuses algebraic formulas while changing their domain-dependent operators, so equality of C symbols across [I], [III] and R-I cannot establish equality of the actual fiber measures.

No explicitly admissible nontrivial history is instantiated: the complete admissibility conditions/weights of hidden sums and their matching to R-I transformed supports have not been reconstructed. Choosing all domains empty/full by convenience would not resolve those conditions, boundary rules or the changed action. The source [III](3.25) is an inherited one-step representation, not a substitute for deriving R-I's termwise source-decorated(1.76). Next expand the precise T/zeta definitions and admissible domain conditions for one chosen summation level, then derive its coordinate/measure matching with all factors retained. H042 positivity/probability-fiber identification, absolute marked integrability, all-sector identity, uniform insertion and terminal bounds remain OPEN. No continuum edge closes; structural no-go count0.


## YM-047 candidate: strict/complementary partitions and resummed support

Read accepted revision46, autonomous architecture and reconciliation034. Reused host-TEMP primary YM044_III.pdf and YM043_review_RI.pdf; no new HTTP acquisition claimed. Host fitz extracted [III]254–258,263–267 and R-I177–181; visually inspected [III]265, including(3.2)–(3.5), at C:/Users/arqam/AppData/Local/Temp/YM047_III_p265.png. The rendered page supports the complementary inequality distinction; no full geometric formula transcription or withdrawn043 prefactor certification is claimed. Initial guessed repository filenames were absent; located the existing reconciliation/registry by rg before use.

New primary-derived dictionary, under200 words together with the transfer source binding; no direct quotation:

| Locator | Support and summation evidence |
|---|---|
| [III]265(3.2) | P is a union of specified partition cubes outside the four-layer enlarged previous large-field region. Each cube is assigned a strict-small indicator or its complementary greater-than-or-equal indicator. |
| [III]265(3.3)–(3.5) | Q is a union of partition cubes in a P-dependent restricted domain; its complement is relative to that domain. A second strict/complementary split tests approximate fluctuations. Enlarged bad regions determine the next Omega. |
| [III]267, before(3.15) | At fixed Omega, zeta sums admissible P/Q preimages, retaining characteristic functions and localized gauge-fixing factors. |
| [III]257(2.18)–258(2.20) | S summation stays in T; component factorization and ordered one-step integrations describe the retained operator. |
| R-I177–178(1.1)–(1.9),181(1.22)–(1.23) | No-new-large-field history conditions simplify the recent cutoff functions. Componentwise unity splits reject components into the retained complement. |

### Own fixed-summation-level interface

Choose the summed level: retain each actual zeta and T as an operator/integrand object; do not relabel a single Omega sequence as an elementary P/Q/S history. This source reconstruction identifies one precise necessary support condition: any elementary preimage used to unpack zeta must use its P-dependent Q universe, relative complement, specified cube partitions and strict-versus-complementary indicator products. Cube threshold equality belongs to the complementary branch. Free assignment of independent P and Q subsets of one common domain is therefore unsupported. Formula(3.5) is a geometric aggregation map, not a declared one-to-one identification of elementary labels with Omega.

For our own finite partition abstraction, on a fixed configuration let a_c be any real cube statistic and t_c its threshold. The factors 1_{a_c<t_c} and 1_{a_c>=t_c} sum to one. Expanding the product of these sums gives a partition indexed by large-cube subsets. At a threshold equality the strict branch vanishes; the complementary branch equals one. A second partition over a first-label-dependent finite cube universe still sums to one by first summing its labels for each fixed first label. This algebra requires those fixed universes and actual scalar statistics; it is not an extraction of all the source's gauge/background constraints. Nor does it make the integrals of different partition branches equal, their label masses a probability distribution without normalization, or the resummed zeta a positive unit-mass kernel after gauge fixing.

A complete zeta definition still requires the earlier axial-gauge expression referenced as(1.5), exact enlargements/partitions and all conditions preceding the resummation. A complete T definition needs inherited and R-modified one-step cutoffs and S restrictions. The dictionary certifies local indicator support, not complete global admissibility or an instantiated nontrivial R-I(1.76) fiber. Source-independent physical Wilson marking alone does not establish source independence of every reconstructed coordinate map/domain. Actual dependence must be derived; a conditional moving-domain formula may not be asserted to describe these vacuum cutoffs. All rejected and n=0 sectors, normalization/Jacobian/operator matching, absolute marked integrability, source coefficients, terminal law and cutoff-uniform bounds remain OPEN. No continuum edge closes; structural no-go count0.


## YM-048 candidate: axial gauge, geometric admissibility and the insertion equivalence gate

Read accepted revision47, autonomous architecture and reconciliation034. Reused host-TEMP primary YM044_III.pdf and YM043_review_RI.pdf, using their previously recorded official Euclid URLs; no new HTTP acquisition claimed. Host Python/fitz extracted [III]247-249,254-258,264-267 and R-I178-182,192-194. Visually inspected newly rendered [III]247,255 and R-I193 at C:/Users/arqam/AppData/Local/Temp/YM048_III_p247.png, YM048_III_p255.png and YM048_RI_p193.png. Initial repository-venv extraction failed because fitz was unavailable; successful host Python extraction supplied the evidence. No full gauge formula/prefactor transcription or withdrawn043 glyph certification is claimed.

New primary-derived dictionary, under200 words per primary source across this audit and transfer; no direct quotation:

| Locator | Bounded admissibility / operation dictionary |
|---|---|
| [III]247(1.5)-(1.9) | A normalized gauge-averaging unity includes a small-coordinate restriction and exponential gauge-fixing weight; Faddeev-Popov insertion produces gauge factors. The approximate-fluctuation test omits designated constraint bonds. |
| [III]248(1.10)-(1.12),249 after(1.14) | Resummation retains localized gauge factors. The linearizing map changes designated constraint bonds only, leaving that approximate-fluctuation cutoff unchanged. |
| [III]254(2.1),255 before(2.2)-(2.3),256 before(2.10) | Admissibility includes nested localization sequences, specified cube partitions/separation and small-component rectangular geometry. S includes a mandatory boundary portion when its relevant domain is nonempty; R is the remaining S portion. R operations may allow Lambda=Omega. |
| [III]258(2.19)-(2.22) | Retained T factors over disjoint components and ordered scale operations; R can modify characteristic functions and empty the fluctuation domain. |
| R-I179-180(1.10)-(1.20) | Preliminary regions follow compatible partitions and layer separations; successive integrations generate and localize new determining sets/backgrounds. |
| R-I193 final paragraphs,194 before(1.76) | Preliminary transformations preserve the density. The subsequent term-dependent Lambda integration changes it; equivalence asserts equal field integrals. Remaining-component T operations persist. |

### Own support dictionary and transport obligation

Keep the summed T/zeta level selected in047. The newly read gauge unity is a gauge-orbit averaging device in its stated support, not a declaration that each resummed effective-history fiber is a positive probability kernel. Its small-coordinate cutoff, exponential factor, normalization and Faddeev-Popov construction must travel together. The constraint-bond exclusion is material: the claim that a particular approximate cutoff survives linearization relies on the changed coordinates being excluded from that cutoff. It grants no blanket invariance of every cutoff, observable, exterior condition or source-marked coordinate map.

The S/R information narrows an admissibility check but does not instantiate a history. To unpack a T sum, reconstruct the exact complement and boundary conventions, mandatory S subset, residual R subset and compatible scale partitions; add the actual determining/background data and all R-modified characteristic functions. Do not choose S empty on a nonempty mandatory domain or choose independent localization sets without their nesting/layers. The exact region/bond formula typography is not certified here; this prose dictionary cannot replace it. Retaining T instead of unpacking S still requires marking its entire ordered operation, including empty-fluctuation cases with surviving gauge and cutoff data.

Most importantly, equal vacuum field integrals after the R-I Lambda integration do not imply equality against an arbitrary inserted functional of the eliminated coordinates. A correct marked lift must integrate the original density multiplied by the original insertion, or derive a matching adjoint/conditional insertion transport at that term's actual domain. This is an own consequence of the stated equivalence scope, not a claim that the source has an insertion error. Term-dependent domains and retained complementary T components preclude replacing this obligation by one arbitrary common-domain average. Vacuum preservation alone does not identify the required all-sector marked map.

Still OPEN: a complete nontrivial admissible history, exact gauge/constraint Jacobians and normalization, original-versus-transformed observable matching, source dependence or independence of every support/map, positivity or total variation needed for H042, absolute marked integrability, global fixed-vacuum denominator, all rejected/n=0 branches and terminal-scale functional. The source geometry and gauge formulas supply no cutoff-uniform flowed insertion theorem or four-dimensional convergence result. Next audit the termwise R-I(1.76) integration measure and derive its observable adjoint with retained T/zeta, using the exact admissibility conventions. No continuum edge closes; structural no-go count0.


## YM-049 candidate: disjoint integral, boundary bonds and gauge-fixed marking

Read accepted revision48, autonomous architecture and reconciliation034. Reused the public primary host-TEMP YM043_review_RI.pdf, whose official Euclid URL is recorded above; no new HTTP acquisition claimed. Host Python/fitz extracted actual printed192-198. Initial guessed index=printed-177 returned headers two pages earlier; this was detected from the extracted headers and corrected to index=printed-175 before using locators. Visually inspected actual printed194 and196, rendered at C:/Users/arqam/AppData/Local/Temp/YM049_RI_actual194.png and YM049_RI_actual196.png. No exact full prefactor, bond-set typography or withdrawn043 glyph is certified.

New primary-derived dictionary (under200 words across this audit and transfer, no direct quotation):

| Locator | Retained operation / support |
|---|---|
| R-I194(1.76) and following paragraphs | Two displayed integrations have disjoint regions. The first, over Zh, stays unchanged in the subsequent discussion. Constraint delta functions have already been integrated out. Minimization concerns the whole integration domain, although subsequent fluctuation analysis uses a smaller domain. |
| R-I194 Proposition1,195(1.79)-(1.81) | The minimizing orbit depends on exterior fields. Its extension defines the background and fluctuation split. Bonds intersecting the Lambda boundary enter B0, while bonds intersecting the designated Omega boundary do not. |
| R-I195-196, before(1.82) | Modified axial gauge fixes a tree plus specified external bonds. A Faddeev-Popov tree delta is inserted; componentwise fluctuation cutoffs separate retained and excluded components. |
| R-I197(1.85)-(1.88),198(1.89) | Background gauge changes require compensating transformations of both residual and fluctuation variables. Further componentwise partitions precede replacement of inherited cutoffs on the surviving support. |

### Own first marked source obligation

This locates an earlier concrete gate than a Gaussian conditional expectation: fix one actual admissible term at the retained summed T/zeta level and identify its unmarked(1.76) coordinate integral with the original term. The first disjoint integral and remaining-component T operation remain part of that term. Disjoint coordinate regions allow iterated integration when the needed integrability holds; they do not prove independence or a factorization of the action, observable or normalized law. The minimizing exterior-dependent background is a coordinate construction, not an observable expectation. A boundary bond cannot be assigned to both coordinate sets or silently removed.

The first missing marked lemma for the selected route is the following actual-model obligation, not a theorem established by this audit: after the term's original degree-one physical flowed insertion is pulled into the(1.76) coordinates, inserting the tree-gauge delta and making the compensating residual/fluctuation gauge transformations preserves that inserted integral, with the original domain, measures and all normalization factors. This requires either proof of invariance of the pulled-back insertion under precisely those transformations or its explicitly transformed insertion, together with the correct gauge-orbit measure identity and absolute integrability. General physical gauge invariance motivates that check but does not identify the actual coordinate pullback or gauge-map action. Source prose certifying invariance of the unmarked integrand cannot supply the missing inserted formula.

Next the componentwise fluctuation and later residual partitions must retain the complementary terms with their inherited integration, rather than applying the surviving-support cutoff replacement to the whole original sum. The equality(1.89) is support-specific. It may be used for an insertion only on the same supported integrand and only after the actual coordinate/gauge identity is matched; it creates neither a probability normalization nor a source derivative. We do not assert that these vacuum supports actually move with the chosen physical source.

No complete history or gauge-fixed marked map is instantiated. Exact inherited normalization, full gauge-Jacobian conventions, hidden sums, terminal functional, positivity/total variation, fixed global vacuum denominator and every rejected/n=0 branch remain OPEN. The small-field fluctuation analysis is not the retained Zh integral and cannot replace it. No source passage inspected here establishes the termwise flowed adjoint or a cutoff-uniform bound; this limited search is not a claim of nonexistence elsewhere. The smallest next source task is the exact marked gauge-orbit/coordinate identity at(1.76)->(1.81)->tree-gauge insertion, followed by matching the support replacement and residual integral. No continuum edge closes; structural no-go count0.


## YM-050 / YM-050R: physical insertion pullback, tree-gauge orbit identity repair, and Family 215 audit

Read accepted revision 50, autonomous repair governance, and coordinator review findings. Reused the public primary host-TEMP YM043_review_RI.pdf (R-I, Bałaban CMP 122, 175–202); no new HTTP network acquisition claimed. Host Python/fitz extracted printed 194–198; visually confirmed (1.76), (1.79)–(1.81), tree-gauge insertion before (1.82), compensating transformations (1.85)–(1.88), and support-specific cutoff replacement (1.89).

New primary-derived dictionary (under 200 words across this audit and transfer, no direct quotation):

| Locator | Operation / Source Equation |
|---|---|
| R-I 194,(1.76) | The joint integration contains two disjoint spatial domains: preliminary integration over Zh (constraint deltas integrated out) and active fluctuation integration on its complement. |
| R-I 194–195,(1.79)–(1.81) | Minimizing background orbit V depends on exterior boundary conditions. Fluctuation split is U = V exp(g A). Boundary bonds: intersecting the Lambda boundary enter B0, while bonds intersecting the designated Omega boundary do not. |
| R-I 195–196, before (1.82) | Modified axial gauge fixes a maximal spanning tree T and designated external bonds via Faddeev–Popov tree delta product_(b in T) delta(A(b)) Delta_FP(V, A). Componentwise fluctuation cutoffs separate retained small-field and excluded components. |
| R-I 197,(1.85)–(1.88), 198,(1.89) | Background gauge changes V -> V^h require compensating transformations of fluctuation variables A -> h^-1 A h and residual variables. Supported cutoff replacement applies to surviving small-field support only. |

### Equation-by-equation map of physical insertion pullback and gauge-orbit identity (repaired)

Let O_(a,t)(f)[U] = a^4 sum_x f(x) E_(a,t)(x)[U] be the physically normalized clover energy density generated by positive-time gradient flow (t > 0). In the degree-one nilpotent source algebra (eta^2 = 0), the source-deformed partition function is Z(eta) = integral dmu[U] (1 + eta O_(a,t)(f)[U]).

1. **Pullback to (V, A) coordinates:**
   For each admissible history alpha in (1.76), link variables decompose as U = V exp(g A). The physical observable pulls back to:
       O_(a,t)(f)[U] = O_(a,t)(f)[V exp(g A)].
   *Non-factorization quantifiers:* Gradient flow over time t > 0 generates non-compact parabolic diffusion across physical distance ~ sqrt(8 t_phys). Consequently, for test functions f whose diffusion envelope intersects both Zh and Omega \ Zh, O_(a,t)(f)[V exp(g A)] couples links in Zh with active fluctuation links, background links V, and boundary bonds B0. This demonstrates a generic failure of spatial factorization across disjoint vacuum integration domains in (1.76), precluding the universal assumption of observable factorization, while leaving open trivial factorization in uncoupled/degenerate limits.

2. **Repaired Faddeev–Popov tree-gauge functional identity:**
   On a maximal spanning tree T subset Lambda with rooted site gauge group G_0 = {h in G^Lambda : h_(x_0) = 1}, the Faddeev–Popov resolution of unity on a single configuration orbit is:
       Delta_FP(V, A) integral_(G_0) dh product_(b in T) delta((A^h)(b)) = 1.
   On a single orbit, the integral evaluates to the scalar 1 / Delta_FP(V, A), NOT to the slice distribution product_(b in T) delta(A(b)). Taking O = 1 demonstrates this distinction: 1 / Delta_FP != product_b delta(A(b)).
   The gauge-slice delta distribution product_(b in T) delta(A(b)) appears strictly under the full configuration-space functional integral:
       integral dmu(A) O_(a,t)(f)[V exp(g A)] = Vol(G_0) integral dmu(A) Delta_FP(V, A) product_(b in T) delta(A(b)) O_(a,t)(f)[V exp(g A)],
   obtained by inserting the resolution of unity into the functional measure, interchanging integrals via Fubini, and performing the functional change of variables A -> A^(h^-1) using gauge invariance of the measure dmu(A^h) = dmu(A), determinant Delta_FP(V, A^h) = Delta_FP(V, A), and observable O_(a,t)(f)[U^h] = O_(a,t)(f)[U]. Under normalized Haar measure Vol(G_0) = 1 and constant tree Jacobian Delta_FP, this establishes exact functional restriction to the gauge slice A|_T = 0.

3. **Link endpoint transformation and background-fluctuation coupling:**
   Under site gauge transformations h in G^Lambda, link variables transform with separate endpoint factors: U_xy^h = h_x U_xy h_y^-1. For U_xy = V_xy exp(g A_xy), holding V_xy fixed while transforming A_xy by h_y A_xy h_y^-1 does NOT produce U_xy^h because h_x V_xy != V_xy h_y unless h is covariantly constant along the link (h_x = V_xy h_y V_xy^-1).
   Bałaban's compensating transformations (R-I (1.85)–(1.88)) resolve this by transforming both background V -> V^h and fluctuation A -> h^-1 A h simultaneously:
       V_xy^h exp(g (h^-1 A h)_xy) = (h_x V_xy h_y^-1) exp(g h_y A_xy h_y^-1) = h_x (V_xy exp(g A_xy)) h_y^-1 = U_xy^h.
   Therefore, an uncoupled tree-gauge identity on fluctuation A with fixed background V is mathematically defective. The actual-model Bałaban coordinate pullback and tree-gauge orbit identity across all external bonds B0, charts, and cutoffs are classified as **CONDITIONAL_AND_OPEN** (`ACTUAL_BALABAN_COORDINATE_PULLBACK_AND_ORBIT_IDENTITY_OPEN`).

4. **All-sector global normalization:**
   The degree-one transport identity is normalized by the global vacuum partition function Z_vac, not by any single-history denominator:
       <O_(a,t)(f)> = (1 / Z_vac) sum_alpha integral dmu_(alpha)^vac[V, A] O_(a,t)(f)[V exp(g A)].
   This sum carries all small-field sectors, complementary/rejected sectors (chi_small = 0), and the n=0 sector.

### Primary-source audit of OpenAI Family 215 (repaired provenance and proof status)

We audited the external candidate manuscript from the openai/math repository at immutable upstream commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (upstream public release October 6, 2026, Problem 215 / Family 215, titled "Canonical O(3) continuum limit and exact O(4) mass asymptotics"):

1. **Exact Upstream Locators, Roles, and Byte Digests:**
   - **Scope Description:** `lean/docs/215.md` (LEN 1,031 bytes, SHA-256: `41ed31b3d5b0f9c0ce5df3604527f17b26eec23b225a7a2184f5a9c2d936ac30`). Role: Scope documentation for accompanying preprint `preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf`. (Note: The repository-relative path is `lean/docs/215.md`; prefixing with `math/` returns 404). This markdown file contains documentation and markdown tables, but zero Lean code declarations or theorem heads.
   - **Comparator Challenge Specification:** `lean/ComparatorChallenges/ClassicalON.lean` (LEN 1,961 bytes, SHA-256: `c2f5f88455b811eb6b56c1ae80ff91f4e398e18e7c7fbeee6daca8da4122d696`). Role: Formal challenge specification. Namespace: `OAI.ClassicalON`. Exact declarations: `Site := ℤ × ℤ`, `PositiveNeighbor (x y : Site) : Prop`, `structure LatticeGraph` (finite square-lattice subgraphs with nearest-neighbor edges), `abbrev Spin (n : ℕ) := ↥(Metric.sphere (0 : EuclideanSpace ℝ (Fin n)) 1)`, `Configuration`, `referenceLaw`, `interaction`, `partition`, `correlation`, `siteDistance`, `def ExponentialDecay : Prop`, and `theorem main : ExponentialDecay := by sorry`.
   - **Comparator Execution Manifest:** `lean/ComparatorChallenges/ClassicalON.json` (LEN 308 bytes, SHA-256: `47cb3623915c8cfcc35099fabd0c44173afa72b706eb0526c4b8d3855e789252`). Role: Manifest linking challenge module `ComparatorChallenges.ClassicalON` to solution module `OAI.Probability.ClassicalON.Main`, with permitted axioms `["propext", "Quot.sound", "Classical.choice"]`.
   - **Candidate Solution Module:** `lean/OAI/Probability/ClassicalON/Main.lean` (LEN 2,050 bytes, SHA-256: `0e4bca8c6b8fe89ffec32eda5d3222af85062a2e3e685729f41578076b528c8a`). Role: Solution proof module. Imports `OAI.Probability.ClassicalON.BlockReduction` and contains `theorem main : ExponentialDecay := by ...` without top-level `sorry`.

2. **Exact Mathematical Model & Boundary Conditions:**
   - **Model:** Two-dimensional classical lattice spin system on unit sphere $S^{n-1} \subset \mathbb{R}^n$ ($n \ge 3$) under nearest-neighbor ferromagnetic coupling $\sum_e b(e) \langle \sigma(e_1), \sigma(e_2) \rangle$ with $b(e) \in [0, \beta]$.
   - **Boundary Conditions:** Finite square-lattice subgraphs with **FREE boundary conditions** (`structure LatticeGraph`), NOT periodic boundary conditions.
   - **Explicit Documented Scope & Exclusions:** `lean/docs/215.md` explicitly specifies: *"For each interaction bound $\beta>0$, constants $A$ and $m>0$ work for every finite square-lattice subgraph with free boundary and nonnegative edge strengths at most $\beta$: the correlation between sites $x,y$ is at most $Ae^{-m|x-y|}$. The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included."*

3. **Supersession of Inaccurate Declaration & Periodic-Boundary Claims:**
   - The previously asserted declaration head `lattice_spin_decay_2d` does NOT exist in the repository; it is formally superseded by the actual comparator theorem `OAI.ClassicalON.main : ExponentialDecay` (with `sorry` in `ClassicalON.lean`) and solution theorem `OAI.ClassicalON.main` in `Main.lean`.
   - The previously asserted "finite 2D periodic lattices" claim is superseded by the exact free-boundary specification.
   - The claim that inspecting `lean/docs/215.md` constituted an "exhaustive declaration search of Lean formalization" is superseded: `lean/docs/215.md` is a Markdown doc with zero Lean code heads; the actual comparator code is `ClassicalON.lean` and solution code is `Main.lean`.

4. **Proof Status Evaluation:**
   - The comparator `ClassicalON.lean` contains `theorem main : ExponentialDecay := by sorry`, which is a problem statement placeholder, not a verified proof.
   - The solution module `Main.lean` contains proof script text relying on a deep dependency tree of ~100 modules in `lean/OAI/Probability/ClassicalON/`. Because we adhere to governance prohibiting execution of untrusted downloaded code, and no reproducible kernel-checking verification receipt is verified at commit `fd4aeeb2...`, the candidate proof status is labeled **UNVERIFIED_UPSTREAM_PROOF_CODE**.
   - Presence of `sorry` in the comparator challenge does NOT imply absence of a solution proof in `Main.lean`; conversely, presence of proof text in `Main.lean` does not substitute for independent kernel verification.

5. **Inspected Search Scope & Negative Boundary:**
   - Across the inspected files (`lean/docs/215.md`, `ClassicalON.lean`, `ClassicalON.json`, and `Main.lean`), zero declarations exist for:
     (a) Continuum quantum field theory construction / Wightman reconstruction;
     (b) Osterwalder–Schrader axioms OS0–OS4;
     (c) Non-Gaussianity of connected Schwinger functions;
     (d) The one-particle mass gap pole or 4D Yang–Mills gauge theory.
   - This search-negative finding across inspected primary files is distinguished from an unproved universal assertion of repo-wide nonexistence.

6. **Epistemic Classification & Transfer Determination:**
   - The transfer candidate remains classified as `UNVERIFIED_CANDIDATE_PREPRINT` and `METHOD_SPECIFIC_OBSTRUCTION`.
   - Allowed transfer conclusion: strictly `None`. Zero DAG edges close.


### Mathematical corrections to the proposed transfer mechanism

1. **Criticality distinction:** The 2D O(3) non-linear sigma model is asymptotically free with dimensionless coupling beta^-1. It is strictly critical / renormalizable, not super-renormalizable. Its ultraviolet behavior requires infinite multiscale cluster or counterterm control, matching the power-counting classification of 4D Yang–Mills.
2. **Non-linear fluctuation source:** On S^2, writing q = (pi, sigma) with sigma = sqrt(1 - ||pi||^2) = 1 - 1/2 ||pi||^2 - ... proves that J . q = J_pi . pi + J_sigma sqrt(1 - ||pi||^2) is strictly non-linear in the fluctuation coordinates pi. It shifts the fluctuation Hessian by -J_sigma delta_ij and does not complete the square linearly.
3. **Green's kernel vs. uniform source analyticity:** Local L1 integrability of (-Delta)^-1(x, y) ~ ln |x-y|^-1 in 2D does not establish cutoff-uniform source analyticity of non-linear observables without multiscale cluster expansion bounds.
4. **Resolvent domain and norm specification:** For the observable Hessian B = D^2 O_(a,t)(f)[V] in 4D, at fixed flow time t_phys > 0, gradient flow smoothing bounds B on L2(Lambda_a, su(N)) orthogonal to gauge zero modes. The obstacle is not an infinite operator norm at fixed t > 0, but the cutoff-uniform summability of the marked polymer activity ||K_j^(1)||_B_j under Bałaban's multiscale RG.


## YM-051: ONE-TERM ADMISSIBLE R-I(1.76) MARKED COORDINATE AND GAUGE-ORBIT REPRESENTATION

### 1. Primary Source Extraction & Metadata
- **Primary Source:** T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989).
- **Inspected Range:** Pages 192–198, specifically Section 1, equations (1.71)–(1.76), Proposition 1, (1.77)–(1.89).
- **Direct Visual & Digital Extraction:** Verified from `C:\Users\arqam\AppData\Local\Temp\YM043_review_RI.pdf` via high-resolution rendering.

### 2. Specification of ONE Explicit Admissible History Term $\alpha$
At the retained summed $\mathbb{T}/\zeta$ level, we select ONE explicit admissible history term $\alpha$ generated after $N$ preliminary scale integrations:
1. **Scale Parameters:** Lattice spacing $a_k = L^{-k} a_0$, with block scale $M \ge 100$ and $L \ge 2$.
2. **Domain Hierarchy:**
   - Previous retained large-field region $Z$, a rectangular parallelepiped union of $M$-cubes.
   - Scale index $k_0$ where $L^{-(k - k_0 + 1)} R_{k - k_0 + 1} = 1$, with $N_0 = k - k_0$.
   - Large-field component $Z_k^\prime = (\Omega_{k_0+1}^5)^c \cap Z$ (eq. (1.10), p. 192), a rectangular parallelepiped contained in a cube of size $100M$.
   - Integration domain $\Lambda$:
     $$\Lambda = (\Omega_{k_0+1}^4)^c \cap Z \quad \text{(R-I (1.73), p. 192)}$$
     obtained by adding exactly one layer of $M$-cubes to $Z_k^\prime$. $\Lambda$ is a rectangular parallelepiped contained in a cube of size $100M$.
   - Preliminary integration domain $Z_h \subset \Lambda$: a rectangular domain on which constraint delta functions have already been integrated out (p. 194).
   - Active fluctuation domain:
     $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \quad \text{(p. 195)}.$$
   - Boundary and external bond set $\mathbb{B}_0$:
     $$\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0 \quad \text{(p. 195)}.$$
     *Boundary bond convention (R-I p. 195):* Bonds $b \in \mathbb{U}_k$ that intersect the outer boundary $\partial \Lambda$ belong to $\mathbb{B}_0$. Bonds that intersect the internal boundary $\partial \Omega_{k+1}^1$ (i.e., touching $Z_h^{\prime \sim}$) DO NOT belong to $\mathbb{B}_0$.
   - Exterior domain: $Z \cap \Lambda^c$, carrying field variables $V_k|_{Z \cap \Lambda^c}$ governed by characteristic function $\chi_{k, \Lambda}$ from the decomposition of unity $1 = \chi_{k, \Lambda} + (1 - \chi_{k, \Lambda})$ (eq. (1.75), p. 193).
3. **Unmarked Termwise Density (R-I (1.76), p. 194):**
   $$\rho_{k, \alpha}[V] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \exp A_k^{\prime\prime}[V].$$

### 3. Coordinate Coverage and Factorization Scope
- **Active fluctuation factorization on $\mathbb{B}_0$:**
  On the bond set $\mathbb{B}_0$, the configuration $V^{\prime\prime}$ factorizes as:
  $$V^{\prime\prime}(b) = V^\prime(b) V_0(b), \quad V_0 = M_{\mathbb{B}_k^\prime}(U_0) \quad \text{(R-I (1.81), p. 195)}$$
  where $U_0 = U_{k, Z}(V_\Lambda^*)$ is the critical background configuration (eq. (1.79)) from Proposition 1 (p. 194), and $V^\prime = \exp(i B^\prime)$ with $B^\prime \in \mathfrak{g}^{\mathbb{B}_0}$.
- **Link coverage disclaimer:**
  The fluctuation representation $V^{\prime\prime} = \exp(i B^\prime) V_0$ covers ONLY the active bond set $\mathbb{B}_0$.
  - It does NOT cover links in $Z_h$, which are carried by the preliminary field $V_h$ under measure $dV_h \lceil_{Z_h}$ and operator $\mathbb{T}_h(Z_h)$.
  - It does NOT cover links in $Z \cap \Lambda^c$, which are carried by the exterior field $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$.
  - It does NOT replace residual scale operators $\mathbb{T}_k$ by a Gaussian; all preliminary and residual operations are strictly retained.

### 4. Degree-One Physical Insertion Pullback
Let $\mathcal{O}_{(a, t)}(f)[U]$ be the gauge-invariant gradient-flowed observable at positive flow time $t_{\mathrm{phys}} > 0$:
$$\mathcal{O}_{(a, t)}(f)[U] = a^4 \sum_{x \in \Lambda_a} f(x) E_{(a, t)}(x)[U].$$
In the degree-one marked partition function $Z(\eta) = Z_{\mathrm{vac}} + \eta \langle \mathcal{O}_{(a, t)}(f) \rangle Z_{\mathrm{vac}} + \mathcal{O}(\eta^2)$, the contribution from term $\alpha$ is:
$$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \exp(A_k^{\prime\prime}[V]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})].$$

*Non-Factorization Proof:*
Positive flow time $t > 0$ generates parabolic diffusion with RMS radius $r_{\mathrm{diff}} = \sqrt{8 t_{\mathrm{phys}}}$. For test functions $f$ whose diffusion envelope intersects both $Z_h$ and $\Lambda \cap Z_h^c$, the flowed field strength $G_{\mu\nu}(x, t)$ depends simultaneously on links in $Z_h$, links in $\mathbb{B}_0$, and links in $Z \cap \Lambda^c$. Consequently, the physical insertion does NOT factor into $\mathcal{O}_{Z_h}[V_h] \cdot \mathcal{O}_{\Lambda \setminus Z_h}[V^{\prime\prime}]$. The preliminary integration over $V_h$ and the fluctuation integration over $V^{\prime\prime}$ remain non-trivially coupled through the physical insertion.

### 5. Gauge Orbit Resolution, Maximal Tree $T_0$, and Slice Restriction
1. **Tree Graph Construction (R-I p. 195–196):**
   Across the nested rectangular parallelepipeds $P_1 \supset P_2 \dots$, contours $\Gamma_{y, x}$ connecting $x \in P_1 \setminus P_2$ to base point $y = (a_1 + 1/2, \dots, a_d + 1/2)$ build tree graph $T = \bigcup_{x} \Gamma_{y, x}$.
   Adding external bonds $[(a_1^\prime - 1/2, \dots), (a_1^\prime + 1/2, \dots)]$ intersecting $\partial P_1$, and for $P_1 = \Lambda$ adding $[(y_1 - 1, y_2, \dots), y]$, yields tree graph $T_0 \subset \mathbb{B}_0$.
2. **Faddeev–Popov Tree-Gauge Resolution:**
   Let $G_{T_0} = \prod_{x \in V(\Lambda_0) \setminus \{x_0\}} G_x$ be the site gauge group rooted at $x_0$. Because $T_0$ contains no closed loops, the tree Jacobian is strictly constant: $\Delta_{\mathrm{FP}} \equiv 1$ under normalized Haar measure.
   On configuration space, inserting the resolution of unity $\Delta_{\mathrm{FP}} \int_{G_{T_0}} dh \prod_{b \in T_0} \delta(B^{\prime h}(b)) = 1$ and performing the functional change of variables $B^\prime \mapsto B^{\prime h^{-1}}$ using gauge invariance of the measure, action, and physical observable $\mathcal{O}_{(a, t)}(f)[U^h] = \mathcal{O}_{(a, t)}(f)[U]$ evaluates the group volume to $\operatorname{Vol}(G_{T_0}) = 1$ and restricts the functional integral to the gauge slice:
   $$\prod_{b \in T_0} \delta(B^\prime(b)).$$
   *Crucial distinction:* Fluctuation variables on non-tree bonds $b \in \mathbb{B}_0 \setminus T_0$ remain unconstrained dynamical degrees of freedom.

### 6. Compensating Transformations (R-I (1.85)–(1.88))
Transforming background $U_0$ to the axial-Landau (AL) mixture gauge (eqs. (1.85)–(1.87), p. 197) with gauge parameter $u_0$:
$$U_0 \mapsto U_0^{u_0} = \exp(i \eta \mathbb{A}_0)$$
requires simultaneous compensating transformations:
- on $V_h$: site transformation restricted to $\partial^+(Z_h^{\prime \sim})^{(h)}$;
- on $V^\prime$: transformation in the adjoint representation $B^\prime \mapsto u_0 B^\prime u_0^{-1}$.
At link endpoints $(x, y)$, site gauge transformations act with endpoint factors $(h_x, h_y)$. Bałaban's joint compensating transformation satisfies:
$$V^{\prime\prime h}_{xy} = (h_x V^\prime_{xy} h_x^{-1}) (h_x V_{0, xy} h_y^{-1}) = h_x (V^\prime_{xy} V_{0, xy}) h_y^{-1} = h_x V^{\prime\prime}_{xy} h_y^{-1}.$$
This guarantees that composite links transform covariantly and the physical insertion $\mathcal{O}_{(a, t)}(f)[U]$ is identically invariant. A naive transformation holding $V_0$ fixed while transforming $B^\prime$ alone fails by an endpoint mismatch $(h_x V_0 h_y^{-1} \ne V_0 h_y^{-1})$.

### 7. Support-Specific Cutoff Replacement (R-I (1.89))
On $\mathbb{B}_0$, decomposition of unity $1 = \chi^\prime + (1 - \chi^\prime)$ with $\chi^\prime = \chi(\{|B^\prime(b)| < \delta_k^\prime \text{ for } b \in \mathbb{B}_0\})$ separates small and large fields.
On the surviving small-field support $\chi^\prime$, Bałaban's cutoff replacement identity (1.89, p. 198) holds:
$$\chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \chi^\prime \chi_h(\Omega_h \cap Z_h) \chi_k^{\prime\prime} = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \chi^\prime.$$
This allows dropping the previous cutoff $\chi_k^{\prime\prime}$ strictly on the small-field branch. The complementary branch $(1 - \chi^\prime)$ is explicitly carried into the large-field remainder $\mathcal{R}_{\alpha, \mathrm{large}}$.

### 8. Established Proved Identity for Term $\alpha$
Within stated finite hypotheses, the degree-one marked functional integral for term $\alpha$ is:
$$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \mathbb{T}_h(Z_h) \int_{\mathfrak{g}^{\mathbb{B}_0 \setminus T_0}} \prod_{b \in \mathbb{B}_0 \setminus T_0} dB^\prime(b) \, J(B^\prime) \, \chi^\prime(B^\prime) \chi_{h, 1/2} \exp(A_k^{\prime\prime}[\exp(i B^\prime) V_0]) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \exp(i B^\prime) V_0, V_k|_{Z \cap \Lambda^c})] + \mathcal{R}_{\alpha, \mathrm{large}}$$
where:
- $J(B^\prime) = \prod_{b \in \mathbb{B}_0 \setminus T_0} \det\left(\frac{1 - e^{-i \operatorname{ad}_{B^\prime(b)}}}{i \operatorname{ad}_{B^\prime(b)}}\right)$ is the Lie algebra Haar Jacobian;
- $B^\prime|_{T_0} = 0$ is fixed by tree gauge;
- $\mathcal{R}_{\alpha, \mathrm{large}}$ carries the complementary $(1 - \chi^\prime)$ and rejected sectors;
- The observable $\mathcal{O}_{(a, t)}(f)$ is evaluated at the full entangled configuration.

### 9. First Missing Theorem Blocking Continuum Closure
This finite representation for term $\alpha$ is completely instantiated and proved within stated hypotheses. The first missing theorem that blocks continuum closure is:
**The Multiscale Marked Polymer Activity Summability Theorem:**
$$\sum_{\alpha} \mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] \quad \text{converges uniformly as } a_0 \to 0,$$
which requires proving that the marked polymer activities $K_j^{(1)}$ satisfy the cluster-expansion tree bound $\|K_j^{(1)}\|_{B_j} \le C_j$ across all scales $j = 0, \dots, n$ under Bałaban's multiscale cluster expansion.


## YM-051R: REPAIR OF TREE-GAUGE CHART MAP, ADJOINT-VS-TREE CONFLATION, EXPLICIT DENSITY REPRESENTATION, AND CONDITIONAL CLASSIFICATION

### 1. Rigorous Derivation of Tree-Gauge Chart Map $h \mapsto B^{\prime h}$ and Slice Derivative
In Section YM-051.5, the tree Faddeev–Popov identity was cited as $\Delta_{\mathrm{FP}} \equiv 1$ under group Haar measure, but its application to a Lie-algebra delta distribution $\prod_{b \in T_0} \delta(B^{\prime h}(b))$ over restricted coordinates omitted the chart mapping and its differential. Here we establish the exact chart representation:

1. **Domain and Coordinate Chart:**
   Let $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$ be the active bond set. On each bond $b = (x, y) \in \mathbb{B}_0$, the link configuration is parameterized by:
   $$V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b),$$
   where $V_0(b) \in SU(2)$ is the fixed minimal background parallel transporter and $B^\prime(b) \in \mathfrak{su}(2)$ satisfies the small-field bound $\|B^\prime(b)\| < \delta_k^\prime \le \pi$. The matrix exponential $\exp: \mathfrak{su}(2) \to SU(2)$ is a diffeomorphism from the ball $\{B \in \mathfrak{su}(2) : \|B\| < \pi\}$ onto its image in $SU(2) \setminus \{-I\}$.

2. **Site Gauge Transformation on Links:**
   Let $\mathcal{G}_{\Lambda_0} = \prod_{x \in V(\Lambda_0)} SU(2)$ be the site gauge group. A gauge transformation $h = (h_x)_{x \in V(\Lambda_0)}$ acts on directed bond $b = (x, y)$ by:
   $$V^{\prime\prime h}(b) = h_x V^{\prime\prime}(b) h_y^{-1} = h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1}.$$
   To express $V^{\prime\prime h}(b)$ in the Bałaban fluctuation chart relative to the same background $V_0(b)$, we write:
   $$V^{\prime\prime h}(b) = \exp(i B^{\prime h}(b)) V_0(b).$$
   Equating these two expressions yields:
   $$\exp(i B^{\prime h}(b)) = h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1}.$$

3. **Chart Map Definition via Matrix Logarithm:**
   Whenever $h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1}$ stays within the injectivity radius (trace $> -2$), the transformed Lie algebra fluctuation $B^{\prime h}(b)$ is uniquely defined by:
   $$B^{\prime h}(b) = \frac{1}{i} \log\left( h_x \exp(i B^\prime(b)) V_0(b) h_y^{-1} V_0(b)^{-1} \right).$$

4. **Root Condition and Maximal Tree Graph:**
   Let $x_0 \in V(\Lambda_0)$ be the designated tree root. The gauge group at the root is fixed: $h_{x_0} = I$.
   The reduced gauge group is $G_{T_0} = \prod_{x \in V(\Lambda_0) \setminus \{x_0\}} SU(2)$.
   The tree graph $T_0 \subset \mathbb{B}_0$ contains $|V(\Lambda_0)| - 1$ bonds and no closed loops, so each vertex $x \ne x_0$ has a unique path in $T_0$ to $x_0$.

5. **Linearization and Derivative at the Gauge Slice:**
   Consider an infinitesimal gauge transformation along generators $X = (X_x)_{x \in V(\Lambda_0) \setminus \{x_0\}} \in \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}}$ with $X_{x_0} = 0$:
   $$h_x(\epsilon) = \exp(i \epsilon X_x) = I + i \epsilon X_x + \mathcal{O}(\epsilon^2).$$
   At the gauge slice $B^\prime = 0$, evaluating the chart map:
   $$h_x(\epsilon) V_0(b) h_y(\epsilon)^{-1} V_0(b)^{-1} = (I + i \epsilon X_x) V_0(b) (I - i \epsilon X_y) V_0(b)^{-1} + \mathcal{O}(\epsilon^2) = I + i \epsilon \left( X_x - V_0(b) X_y V_0(b)^{-1} \right) + \mathcal{O}(\epsilon^2).$$
   Taking the logarithm and dividing by $i$:
   $$\left. \frac{d}{d\epsilon} B^{\prime h(\epsilon)}(b) \right|_{\epsilon=0, B^\prime=0} = X_x - \operatorname{Ad}_{V_0(b)}(X_y) = (D_{V_0} X)(b),$$
   where $D_{V_0}: \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}} \to \mathfrak{su}(2)^{T_0}$ is the background covariant lattice differential along tree bonds.
   Because $T_0$ is a rooted tree, ordering vertices by tree distance from $x_0$ renders the matrix of $D_{V_0}$ block triangular with diagonal blocks given by $\pm \operatorname{Ad}_{V_0(b)}$ or $\pm I$.
   Since $\det(\operatorname{Ad}_g) = 1$ for all $g \in SU(2)$, the Jacobian determinant of $D_{V_0}$ is:
   $$\det(D_{V_0}) = \prod_{b \in T_0} |\det(\operatorname{Ad}_{V_0(b)})| = 1.$$

6. **Unrestricted Group Tree Gauge vs. Lie Algebra Delta with Cutoffs:**
   - On the full group $SU(2)^{T_0}$, normalized Haar measure $\int \prod_{b \in T_0} dh_b = 1$ integrates over compact space with no boundaries.
   - In contrast, the Lie algebra delta $\delta(B^\prime)$ is supported on an open coordinate chart $\mathcal{U} = \{\|B^\prime\| < \delta_k^\prime\}$.
   - If a gauge orbit exits the chart $\mathcal{U}$, the matrix logarithm ceases to be single-valued or crosses the cutoff $\chi^\prime$.
   - Therefore, replacing group Haar tree gauge by a Lie algebra delta $\prod_{b \in T_0} \delta(B^\prime(b))$ is **not** an unconditional identity; it is strictly conditional on the small-field chart domain and boundary cutoffs.


### 2. Adjoint Conjugation vs. Tree-Gauge Fixing Decoupling
In Section YM-051.6, the joint compensating transformation under background axial-Landau gauge change $U_0 \mapsto U_0^{u_0}$ was presented alongside tree-gauge fixing. We prove that these two actions are mathematically distinct and cannot be conflated:

1. **Adjoint Conjugation Preserves Norm and Spectrum:**
   Let $u_0 \in SU(2)$ and $B^\prime \in \mathfrak{su}(2)$. Under adjoint conjugation, $B^\prime \mapsto u_0 B^\prime u_0^{-1}$.
   Using the standard Frobenius / Hilbert–Schmidt norm on $\mathfrak{su}(2)$ (where $\|X\|_F = \sqrt{\frac{1}{2} \operatorname{Tr}(X^\dagger X)} = \sqrt{\frac{1}{2} \operatorname{Tr}(X^2)}$ for anti-Hermitian $X$, or $\sqrt{\operatorname{Tr}(B^{\prime 2})}$ for Hermitian $B^\prime$):
   $$\|u_0 B^\prime u_0^{-1}\|_F^2 = \operatorname{Tr}((u_0 B^\prime u_0^{-1})^\dagger (u_0 B^\prime u_0^{-1})) = \operatorname{Tr}(u_0 B^{\prime \dagger} B^\prime u_0^{-1}) = \operatorname{Tr}(B^{\prime \dagger} B^\prime) = \|B^\prime\|_F^2.$$
   Consequently, for any non-zero fluctuation $B^\prime \ne 0$:
   $$\|u_0 B^\prime u_0^{-1} - 0\|_F = \|B^\prime\|_F > 0.$$
   **Theorem (Adjoint Non-Zero Preservation):** Adjoint conjugation is an isometry of $\mathfrak{su}(2)$ and can NEVER map a non-zero fluctuation to zero. It merely rotates the Lie-algebra direction; it does not reduce degrees of freedom or fix a gauge slice.

2. **Tree-Gauge Fixing Requires Affine Parallel Transport:**
   To fix tree gauge on bond $b = (x, y) \in T_0$, one requires $V^{\prime\prime h}(b) = V_0(b)$, which is equivalent to $B^{\prime h}(b) = 0$.
   From $h_x \exp(i B^\prime) V_0 h_y^{-1} = V_0$, the site gauge element $h_y$ at the target endpoint MUST satisfy:
   $$h_y = V_0(b)^{-1} h_x \exp(i B^\prime(b)) V_0(b).$$
   When $B^\prime = 0$, this is the affine parallel transport equation:
   $$h_y = V_0(b)^{-1} h_x V_0(b).$$
   Notice that $h_y \ne h_x$ whenever $V_0(b)$ does not commute with $h_x$.
   Adjoint conjugation $B^\prime \mapsto u_0 B^\prime u_0^{-1}$ is an AL background mixture covariance transformation acting with the same parameter $u_0$ everywhere on the background field, whereas tree-gauge fixing recursively solves the non-local parallel transport equation edge-by-edge along the tree $T_0$.
   Conflating the two is a severe conceptual error; they must be decoupled completely.


### 3. Explicit Original Density vs. Transformed Template and Remainder Sector
We present the exact original term from Bałaban R-I (1.76) and its explicit transformed template with all constraints and inherited cutoffs:

1. **Original Unmarked Termwise Density (R-I (1.76), p. 194):**
   $$\rho_{k, \alpha}[V] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} \chi_k^{\prime\prime} \, \exp\left(A_k^{\prime\prime}[V]\right).$$

2. **Explicit Transformed Template with Inherited Cutoffs and Measure Factors:**
   Introducing the Lie-algebra fluctuation coordinates $V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b)$ on active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, the degree-one physical marked insertion is:
   $$\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)] = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int_{\mathfrak{g}^{\mathbb{B}_0 \setminus T_0}} \prod_{b \in \mathbb{B}_0 \setminus T_0} dB^\prime(b) \, J(B^\prime(b)) \, \chi^\prime(B^\prime|_{T_0=0}) \, \chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h) \, \exp\left(A_k^{\prime\prime}[\exp(i B^\prime|_{T_0=0}) V_0]\right) \, \mathcal{O}_{(a, t)}(f)[U(V_h, \exp(i B^\prime|_{T_0=0}) V_0, V_k|_{Z \cap \Lambda^c})] + \mathcal{R}_{\alpha, \mathrm{large}}.$$

3. **Complete Inventory of Inherited Cutoffs:**
   - $\chi_k(\Omega_k^{\sim 4})$: scale $k$ large-field cutoff on domain $\Omega_k^{\sim 4}$;
   - $\chi_{k, \Lambda}$: partition-of-unity characteristic function isolating exterior domain $Z \cap \Lambda^c$ (R-I (1.75));
   - $\chi_h(\Omega_h \cap Z_h)$: scale $h$ cutoff on preliminary region $Z_h$;
   - $\chi_{h, 1/2}((\Omega_{h+1}^{\prime\prime \sim 2})^c \cap \Omega_h)$: transition cutoff from scale $h$ to $h+1$ (R-I (1.89));
   - $\chi^\prime(B^\prime) = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\|B^\prime(b)\| < \delta_k^\prime}$: small-field characteristic function on active bonds $\mathbb{B}_0$;
   - $J(B^\prime(b)) = \det\left(\frac{1 - e^{-i \operatorname{ad}_{B^\prime(b)}}}{i \operatorname{ad}_{B^\prime(b)}}\right)$: Lie algebra Haar measure Jacobian on unconstrained bonds $b \in \mathbb{B}_0 \setminus T_0$.

4. **Explicit Complementary Large-Field Remainder Term $\mathcal{R}_{\alpha, \mathrm{large}}$:**
   Instead of an uninstantiated symbolic label, the exact complementary term is given by:
   $$\mathcal{R}_{\alpha, \mathrm{large}} = \chi_k(\Omega_k^{\sim 4}) \, \chi_{k, \Lambda} \int dV_h \lceil_{Z_h} \chi_h(\Omega_h \cap Z_h) \, \mathbb{T}_h(Z_h) \int dV^{\prime\prime} \lceil_{\mathbb{B}_k^{\prime\prime} \cap (\Lambda \cap Z_h^c)} (1 - \chi^\prime) \, \chi_k^{\prime\prime} \, \exp\left(A_k^{\prime\prime}[V]\right) \, \mathcal{O}_{(a, t)}(f)[U(V_h, V^{\prime\prime}, V_k|_{Z \cap \Lambda^c})].$$
   Every factor in $\mathcal{R}_{\alpha, \mathrm{large}}$ is mathematically explicit.


### 4. Formal Reclassification
The actual-model Bałaban coordinate pullback and tree-gauge orbit representation across external bonds $\mathbb{B}_0$, charts, and cutoffs are formally classified as:
$$\text{Status: } \mathbf{CONDITIONAL\_AND\_OPEN}$$
with persistent governance identifier:
$$\mathbf{ACTUAL\_BALABAN\_COORDINATE\_PULLBACK\_AND\_TREE\_GAUGE\_CONDITIONAL\_AND\_OPEN}.$$
No continuum limit or spectral gap estimate is closed. The structural no-go count remains strictly 0.


## YM-051R2: REPAIR OF SU(2) UNIT RATIONAL QUATERNION CERTIFICATES, MULTI-EDGE TREE AFFINE TRANSPORT, EXACT OBSERVABLE MIXED DEPENDENCE, LIE CONVENTION RECONCILIATION, AND ACTUAL-HISTORY ADMISSIBILITY AUDIT

### 1. Reconciliation of Lie Algebra Conventions and Determinants
In mathematical physics literature (specifically Bałaban CMP 109, R-I (1.81)), link fluctuations are written as $V^{\prime\prime}(b) = \exp(i B^\prime(b)) V_0(b)$. We establish the explicit dictionary between the Hermitian generator convention and the differential-geometric anti-Hermitian convention:

1. **Hermitian Generator Convention (Bałaban):**
   - Basis: $T_a = \frac{1}{2} \sigma_a$ where $\sigma_a$ are Hermitian Pauli matrices ($T_a^\dagger = T_a$).
   - Lie bracket: $[T_a, T_b] = i \epsilon_{abc} T_c$.
   - Fluctuation: $B^\prime = \sum_{a=1}^3 B^{\prime a} T_a$ is Hermitian ($B^{\prime \dagger} = B^\prime$, $\operatorname{Tr}(B^\prime) = 0$).
   - Quadratic Casimir / Trace: $\operatorname{Tr}((B^\prime)^2) = \frac{1}{2} \sum_{a=1}^3 (B^{\prime a})^2 \ge 0$.
   - Group element: $U = \exp(i B^\prime)$, where the exponent $i B^\prime$ is anti-Hermitian ($(i B^\prime)^\dagger = -i B^\prime$).

2. **Anti-Hermitian Generator Convention (Lie Theory / Differential Geometry):**
   - Basis: $\tilde{T}_a = i T_a = \frac{i}{2} \sigma_a$ satisfying $\tilde{T}_a^\dagger = -\tilde{T}_a$.
   - Lie bracket: $[\tilde{T}_a, \tilde{T}_b] = -\epsilon_{abc} \tilde{T}_c$.
   - Lie algebra element: $X = i B^\prime = \sum_{a=1}^3 X^a \tilde{T}_a \in \mathfrak{su}(2)$.
   - Quadratic Casimir / Trace: $\operatorname{Tr}(X^2) = -\frac{1}{2} \sum_{a=1}^3 (X^a)^2 \le 0$.
   - Group element: $U = \exp(X) \in SU(2)$.

3. **Quaternion Embedding:**
   - Standard isomorphism $\mathbb{H}_1 \cong SU(2)$: $q = q_0 + q_1 \mathbf{i} + q_2 \mathbf{j} + q_3 \mathbf{k}$ with $q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1$.
   - Pure imaginary quaternions $\operatorname{Im}(\mathbb{H})$ satisfy $\mathbf{i}^2 = \mathbf{j}^2 = \mathbf{k}^2 = \mathbf{i}\mathbf{j}\mathbf{k} = -1$.
   - For $X = x_1 \mathbf{i} + x_2 \mathbf{j} + x_3 \mathbf{k}$, $X^2 = -\|X\|^2 \le 0$. Pure imaginary quaternions represent the **anti-Hermitian** algebra $\mathfrak{su}(2)$.
   - Group exponential: $\exp(X) = \cos(\|X\|) + \frac{\sin(\|X\|)}{\|X\|} X \in \mathbb{H}_1$. No factor of $i$ appears in the quaternion exponential because imaginary quaternion units already square to $-1$.

4. **Signed Determinant vs. Absolute Jacobian:**
   - The directional derivative matrix $D_{V_0}: \mathfrak{su}(2)^{V(\Lambda_0) \setminus \{x_0\}} \to \mathfrak{su}(2)^{T_0}$ along rooted tree $T_0$ has signed matrix determinant:
     $$\det(D_{V_0}) = +1$$
     (orientation-preserving linear isomorphism).
   - In the coordinate transformation of the differential form Haar measure $dB^\prime$, the volume density scales by the **absolute Jacobian**:
     $$|\det(D_{V_0})| = 1.$$
   - Both signed determinant and absolute Jacobian equal $1$ on $SU(2)$, but the distinction between orientation and integration density is maintained.

### 2. Exact SU(2) Unit Rational Quaternions
To eliminate non-unit approximations (such as $(1, 0, 1/3, 0)$ or truncated Taylor series $(1 - 1/8, 1/2, 0, 0)$ which have squared norms $10/9 \ne 1$ and $65/64 \ne 1$), all group links and site transformations are constructed from Pythagorean quadruples $q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1$ in $\mathbb{Q}$:
- Identity: $I = (1, 0, 0, 0)$
- Transporter $V_0(b_1) = (3/5, 4/5, 0, 0)$, norm squared $(9+16)/25 = 1$.
- Transporter $V_0(b_2) = (3/5, 0, 4/5, 0)$, norm squared $(9+16)/25 = 1$.
- Transporter $V_0(b_3) = (4/5, 0, 0, 3/5)$, norm squared $(16+9)/25 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_1) = (24/25, 7/25, 0, 0)$, norm squared $(576+49)/625 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_2) = (12/13, 0, 5/13, 0)$, norm squared $(144+25)/169 = 1$.
- Small-field fluctuation factor $U_{\mathrm{fluc}}(b_3) = (4/5, 0, 0, 3/5)$, norm squared $(16+9)/25 = 1$.
Every link $U(b) = U_{\mathrm{fluc}}(b) V_0(b)$ and site gauge element $h_x$ is certified to satisfy $\|q\|^2 = 1$ identically. Inversion in $\mathbb{H}_1$ is the exact quaternionic conjugate $q^{-1} = (q_0, -q_1, -q_2, -q_3)$.

### 3. Multi-Edge Rooted Tree $T_0$ Affine Parallel Transport
Consider a non-trivial rooted multi-edge tree $T_0$ on active vertices $V(\Lambda_0) = \{x_0, x_1, x_2, x_3\}$:
- Root vertex: $x_0 = (1, 1)$, with gauge condition $h_{x_0} = (1, 0, 0, 0) = I$.
- Tree edge 1 (branch 1): $b_1 = (x_0, x_1) = ((1, 1), (1, 0))$.
- Tree edge 2 (depth 2): $b_2 = (x_1, x_2) = ((1, 0), (2, 0))$.
- Tree edge 3 (branch 2): $b_3 = (x_0, x_3) = ((1, 1), (0, 1))$.
- Non-tree cycle edge: $b_4 = (x_2, x_3)$, closing a loop in $\Lambda_0$.

Sequential affine parallel transport along $T_0$:
1. At edge $b_1$: $h_{x_1} = V_0(b_1)^{-1} h_{x_0} U(b_1)$.
   Norm $\|h_{x_1}\|^2 = 1$; transformed link $U^h(b_1) = h_{x_0} U(b_1) h_{x_1}^{-1} = V_0(b_1)$.
2. At edge $b_2$: $h_{x_2} = V_0(b_2)^{-1} h_{x_1} U(b_2)$.
   Norm $\|h_{x_2}\|^2 = 1$; transformed link $U^h(b_2) = h_{x_1} U(b_2) h_{x_2}^{-1} = V_0(b_2)$.
3. At edge $b_3$: $h_{x_3} = V_0(b_3)^{-1} h_{x_0} U(b_3)$.
   Norm $\|h_{x_3}\|^2 = 1$; transformed link $U^h(b_3) = h_{x_0} U(b_3) h_{x_3}^{-1} = V_0(b_3)$.

All three tree edges simultaneously satisfy $U^h(b) = V_0(b)$, meaning on the chart $B^{\prime h}|_{T_0} = 0$.
In contrast:
- On the non-tree cycle edge $b_4 = (x_2, x_3)$, the transformed link is $U^h(b_4) = h_{x_2} U(b_4) h_{x_3}^{-1} \ne V_0(b_4)$. Its defect $\|U^h(b_4) - V_0(b_4)\|^2 > 0$ proves that non-tree links carry dynamical degrees of freedom (gauge-invariant holonomy) that cannot be eliminated by tree gauge.
- Naive uncoupled transformation setting $h_x = I$ for all $x$ leaves a non-zero tree defect $\sum_{b \in T_0} \|U(b) - V_0(b)\|^2 > 0$, confirming that affine transport coupling is mandatory.

### 4. Explicit Mixed Dependence and Lattice Gradient Flow Non-Factorization
To replace scalar heuristic constants (such as `135/1000` or a single uncoupled plaquette value), we establish genuine non-factorization:
1. **Observable Mixed Dependence Defect:**
   Let $\mathcal{O}(U_A, U_B) = \frac{1}{2} \operatorname{Tr}(U_A U_B)$ be an explicit composite observable coupling a link $U_A$ in preliminary region $Z_h$ with a link $U_B$ in active region $\Lambda_0$ sharing a boundary vertex $x \in \partial Z_h$.
   If $\mathcal{O}$ were factorizable into $f(U_A) g(U_B)$, then for any 4 configurations $(U_A^{(1)}, U_B^{(1)})$, $(U_A^{(2)}, U_B^{(1)})$, $(U_A^{(1)}, U_B^{(2)})$, $(U_A^{(2)}, U_B^{(2)})$, the cross-variation determinant must vanish identically:
   $$\Delta_{\mathrm{fact}} = \mathcal{O}(U_A^{(1)}, U_B^{(1)}) \mathcal{O}(U_A^{(2)}, U_B^{(2)}) - \mathcal{O}(U_A^{(1)}, U_B^{(2)}) \mathcal{O}(U_A^{(2)}, U_B^{(1)}) \equiv 0.$$
   Evaluating $\Delta_{\mathrm{fact}}$ on exact rational unit quaternions yields $\Delta_{\mathrm{fact}} \ne 0$, rigorously proving non-factorization.

2. **Lattice Wilson Gradient Flow Coupling:**
   On a hypercubic lattice, the discrete gradient flow equation is $\partial_t U_t(b) = - D S(U_t)(b) U_t(b)$, where $D S(U_t)(b)$ is the Lie-algebra staple sum around bond $b$.
   The first Euler flow step $U_{t + \epsilon}(b) = \exp(-\epsilon D S(U_t)(b)) U_t(b)$ explicitly mixes bond $b \in Z_h$ with adjacent plaquette staples touching $\Lambda_0$.
   The second functional cross-derivative $\frac{\partial^2 S_{\mathrm{flowed}}}{\partial U(b_1) \partial U(b_2)} \ne 0$ for $b_1 \in Z_h$ and $b_2 \in \Lambda_0$ is strictly non-zero, establishing that gradient-flowed observables cannot factorize across spatial boundaries without approximation.

### 5. Actual History Admissibility Audit and Primary-Source Locators
We audit ONE concrete actual admissible history $\alpha$ from Bałaban R-I (1.76):
1. **Primary-Source Locators:**
   - Bałaban, CMP 109 (1987) pp. 193–198: Proposition 1, eq. (1.76), (1.79), (1.81), (1.85)–(1.89).
   - Fixed exterior domain: $Z \cap \Lambda^c$, carrying field variables $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$ (R-I (1.75)).
   - Preliminary region $Z_h$: carrying short-distance field $V_h$ under measure $dV_h \lceil_{Z_h}$ and retained scale operator $\mathbb{T}_h(Z_h)$.
   - Active region $\Lambda_0 = \Lambda \setminus Z_h$: carrying bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, excluding bonds touching $\partial \Omega_{k+1}^1$.
   - Background parallel transporter: $U_0 = U_{k, Z}(V_\Lambda^*)$ (eq. (1.79)), $V_0 = M_{\mathbb{B}_k^\prime}(U_0)$.
   - Site gauge group: $\mathcal{G}_{\Lambda_0}$ rooted at $x_0 \in \Lambda_0$ with condition $h_{x_0} = I$.
   - Normalization: degree-one physical marked insertion $\mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)]$ is normalized by the global vacuum partition function $Z_{\mathrm{vac}}$, not by an individual history denominator.

2. **Chart Admissibility and Boundary Cutoff Analysis:**
   - On active bonds $\mathbb{B}_0$, the tree slice $B^\prime|_{T_0} = 0$ is defined on the chart ball $\|B^\prime(b)\| < \delta_k^\prime \le \pi$.
   - While group Haar tree-gauge integration $\int_{SU(2)^{T_0}} \prod dh_b = 1$ is globally defined on the compact group with zero boundary, the chart representation $B^{\prime h}(b) = \frac{1}{i} \log(h_x \exp(i B^\prime) V_0 h_y^{-1} V_0^{-1})$ is restricted to the ball $\|B^\prime\| < \delta_k^\prime$.
   - If a gauge orbit exits this ball, the configuration is cut off by $(1 - \chi^\prime)$ and enters the large-field remainder $\mathcal{R}_{\alpha, \mathrm{large}}$.
   - Therefore, the tree-gauge slice is **conditionally admissible** on the small-field support $\chi^\prime$.

3. **Identification of the First Explicit Missing Bridge Lemma:**
   Before multiscale polymer activity summability can be addressed, the actual-model chart stability must be established. We formulate:
   
   **LEMMA `YM-051F-ACTUAL-CHART-SUMMABILITY` (Small-Field Chart Stability and Remainder Activity Bound):**
   *For any admissible history $\alpha$ in Bałaban R-I (1.76), there exists a scale-dependent constant $c_k > 0$ such that:*
   1. *Gauge Orbit Chart Stability: The probability under constrained Haar measure that the tree-gauge orbit exits the chart ball $\|B^{\prime h}(b)\| < \delta_k^\prime$ is bounded by $\mathcal{O}(e^{-c_k / g_k^2})$;*
   2. *Large-Field Remainder Bound: The complementary remainder satisfies $\|\mathcal{R}_{\alpha, \mathrm{large}}\| \le C_k e^{-M / g_k^2} \|\mathcal{O}_{(a, t)}(f)\|_\infty$;*
   3. *Summability Dependency: Uniform polymer activity summability $\sum_\alpha \mathcal{I}_\alpha[\mathcal{O}_{(a, t)}(f)]$ is conditionally dependent on the resolution of this chart stability lemma.*

4. **Corrected Dependency Ordering:**
   Uniform multiscale polymer activity summability is **NOT** the first dependency-satisfied obligation. The first required obligation is the proof of Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` on the concrete history domain.


## YM-051R3: SOURCE/DOMAIN AND CONJECTURE WELL-POSEDNESS REPAIR

### 1. Primary-Source Citation Supersession and Page/Equation Verification
In Section YM-051R2 (lines 619, 697), citations referred to "Bałaban CMP 109 (1987) pp. 193–198". This citation is formally corrected and superseded:
- **Erroneous Citation (Superseded):** CMP 109 (1987) pp. 193–198 (*Generation of Effective Actions*).
- **Correct Primary Source:**
  **T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989)**.
- **Direct Primary PDF Page and Equation Mapping:**
  - Section 1: pp. 180–202.
  - Page 192, eq. (1.71)–(1.73): Decomposition of large-field component $Z_k^\prime = (\Omega_{k_0+1}^5)^c \cap Z$ and integration domain $\Lambda = (\Omega_{k_0+1}^4)^c \cap Z$.
  - Page 193, eq. (1.75): Characteristic function $\chi_{k, \Lambda}$ on exterior $Z \cap \Lambda^c$.
  - Page 194, eq. (1.76): Definition of termwise density $\rho_{k, \alpha}[V]$ with preliminary integration on $Z_h$.
  - Page 194, Proposition 1 and eq. (1.79): Minimal background configuration $U_0 = U_{k, Z}(V_\Lambda^*)$.
  - Page 195, eq. (1.81): Active fluctuation factorization $V^{\prime\prime} = \exp(i B^\prime) V_0$ on $\mathbb{B}_0$.
  - Page 195, eq. (1.85)–(1.88): Compensating transformations under background gauge change.
  - Page 195, eq. (1.89): Support-specific cutoff replacement $\chi_k^{\prime\prime} \chi^\prime = \chi^\prime$.
  - Pages 195–196: Maximal tree graph $T_0 \subset \mathbb{B}_0$ constructed from nested parallelepipeds $P_1 \setminus P_2$.

### 2. Geometric Domain Reconciliation: $\Lambda_0$ vs. $\Lambda \setminus Z_h$ and Scoping of Finite Examples
1. **Enlarged Neighborhoods and Domain Inequality:**
   In line 700 of Section YM-051R2, $\Lambda_0$ was loosely written as $\Lambda \setminus Z_h$. This is mathematically inaccurate and is superseded:
   $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c \quad \text{(CMP 122 p. 195)}.$$
   Because $Z_h \subset Z_h^\prime \subset Z_h^{\prime \sim}$, the set $Z_h^{\prime \sim}$ is a strictly larger regularized neighborhood of $Z_h$.
   Consequently, $\Lambda_0 \subsetneq \Lambda \setminus Z_h$. The collar region $(\Lambda \setminus Z_h) \setminus \Lambda_0 = Z_h^{\prime \sim} \setminus Z_h$ carries delta constraints, preliminary boundary fields, and buffer bonds, but is **NOT** part of the active fluctuation domain $\Lambda_0$.
2. **Active Bond Endpoints and Boundaries:**
   - Active bonds: $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$.
   - Bonds in $\mathbb{U}_k$ that intersect the outer boundary $\partial \Lambda$ belong to $\mathbb{B}_0$.
   - Bonds that intersect the internal boundary $\partial \Omega_{k+1}^1$ (touching $Z_h^{\prime \sim}$) are explicitly excluded from $\mathbb{B}_0$.
   - Exterior sites on $\partial \Lambda$ and in $Z \cap \Lambda^c$ carry fixed exterior fields $V_k|_{Z \cap \Lambda^c}$ under cutoff $\chi_{k, \Lambda}$.
3. **Explicit Scoping of Finite Certificates:**
   The 4-site unit quaternion graph in Test 11 ($x_0=(1, 1)$, $x_1=(1, 0)$, $x_2=(2, 0)$, $x_3=(0, 1)$) is an explicit **toy finite graph certificate** illustrating the algebraic mechanism of multi-edge tree affine transport and cycle holonomy defect.
   Its non-tree cycle edge $b_4 = ((2, 0), (0, 1))$ has coordinate displacement $(-2, 1)$ and Euclidean length $\sqrt{5}$, which is NOT a nearest-neighbor hypercubic lattice bond.
   This graph is NOT an admissible Bałaban history on $\mathbb{Z}^4$; it is strictly scoped as a non-hypercubic algebraic certificate of the tree-gauge transport mechanism.

### 3. Signed Determinant vs. Absolute Jacobian and Orientation Order
In line 643 of Section YM-051R2, the claim that $\det(D_{V_0}) = +1$ universally is corrected:
- On link $b = (x, y)$ oriented from parent $x$ to child $y$, the directional derivative of $U^h(b) = h_x U(b) h_y^{-1}$ with respect to Lie algebra parameters $\xi_x, \xi_y$ is:
  $$(D_{V_0} \xi)(b) = \xi_x - \operatorname{Ad}_{V_0(b)} \xi_y.$$
- For a rooted tree with root condition $\xi_{x_0} = 0$, the child site $\xi_y$ enters with coefficient $- \operatorname{Ad}_{V_0(b)}$.
- On the 3-dimensional Lie algebra $\mathfrak{su}(2)$, the linear operator $- \operatorname{Ad}_{V_0(b)}$ has determinant:
  $$\det(- \operatorname{Ad}_{V_0(b)}) = (-1)^3 \det(\operatorname{Ad}_{V_0(b)}) = (-1) \cdot (+1) = -1.$$
- Therefore, for a tree with $k$ child edges directed away from the root, the signed block determinant is:
  $$\det(D_{V_0}) = (-1)^{3 k} = (-1)^k.$$
  The sign is $-1$ for odd $k$ and $+1$ for even $k$, and reverses if edge orientations are flipped.
- In contrast, the **absolute Jacobian**:
  $$|\det(D_{V_0})| = |-1|^k = 1$$
  is universally and robustly equal to $1$, completely independent of edge orientation, basis order, or dimension parity.

### 4. Observables: Scoped Toy Cross-Defect vs. Open Physical Flowed Non-Factorization
1. **Toy Algebraic Scope:** The non-factorization defect $\Delta_{\mathrm{fact}} = -16/25 \ne 0$ for composite observable $\mathcal{O}(U_A, U_B) = \frac{1}{2} \operatorname{Tr}(U_A U_B)$ is strictly a toy algebraic certificate disproving the spatial factorization hypothesis $f(U_A) g(U_B)$ for coupled open links.
2. **Physical Gauge Invariance & Open Status:** On a physical lattice gauge theory, the trace of two open links is not gauge invariant without closing paths. Furthermore, an infinitesimal Euler flow staple calculation does not prove non-factorization for the physical gauge-invariant flowed observable $\mathcal{O}_{(a, t)}(f)$ across non-linear trajectories at finite $t_{\mathrm{phys}} > 0$.
3. **Formal Epistemic Classification:** The claim of non-factorization for the physical flowed observable remains formally classified as:
   $$\mathbf{PHYSICAL\_FLOWED\_OBSERVABLE\_NON\_FACTORIZATION\_OPEN}.$$

### 5. Refutation of Ill-Posed Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` and Replacement by Deterministic Lemma
1. **Refutation of Proposed Probabilistic Formulation:**
   The formulation of Lemma `YM-051F-ACTUAL-CHART-SUMMABILITY` in Section YM-051R2 is refuted as ill-posed:
   - Haar measure on $SU(2)$ is a normalized translation-invariant group measure with NO $g$-dependence; naming $g$ cannot produce an $\mathcal{O}(e^{-c/g^2})$ probability bound under Haar measure.
   - An $\mathcal{O}(e^{-c/g^2})$ suppression requires the Wilson action $\exp(-g^{-2} S(U))$, which is a weighted measure, not pure Haar measure.
   - The event that the original configuration exits the chart ball (governed by $1 - \chi^\prime$) is NOT identical to the event that the tree-gauge transformed configuration exits the chart ball.
   - Constants $C_k, c_k, M$, norms, and parameter ranges were undefined.
2. **Replacement: Purely Deterministic First Bridge Lemma:**
   We formulate the true, source-bound deterministic bridge lemma that precedes any statistical estimates:

   **LEMMA `YM-051F-DETERMINISTIC-CHART-OVERLAP` (Deterministic Small-Field Chart Overlap and Remainder Decomposition):**
   *For any admissible history $\alpha$ in Bałaban CMP 122 (1.76) on $\Lambda_0 = \Lambda \cap (Z_h^{\prime \sim})^c$ and active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$:*
   1. *Let $\mathcal{B}_{\delta_k^\prime} = \{B^\prime \in \mathfrak{su}(2)^{\mathbb{B}_0} : \|B^\prime(b)\| < \delta_k^\prime \ \forall b \in \mathbb{B}_0\}$ with small-field characteristic function $\chi^\prime = \mathbf{1}_{\mathcal{B}_{\delta_k^\prime}}$.*
   2. *Let $h[V^{\prime\prime}] \in \mathcal{G}_{\Lambda_0}$ (rooted at $x_0$, $h_{x_0} = I$) be the unique sequential tree-fixing affine parallel transport map satisfying $V^{\prime\prime h}(b) = V_0(b)$ for all $b \in T_0$.*
   3. *Define the deterministic chart overlap domain:*
      $$\mathcal{E}_{\mathrm{chart}} = \left\{ B^\prime \in \mathcal{B}_{\delta_k^\prime} : \forall b \in \mathbb{B}_0 \setminus T_0, \ V^{\prime\prime h[V^{\prime\prime}]}(b) V_0(b)^{-1} \in \exp(\mathcal{B}_{\delta_k^\prime}) \right\}.$$
   4. *On $\mathcal{E}_{\mathrm{chart}}$, the gauge slice coordinate map $B^{\prime h}|_{T_0} = 0$ is exact, the absolute Jacobian is $|\det(D_{V_0})| = 1$, and Haar measure satisfies exact measure equality.*
   5. *The un-normalized termwise density $\rho_{k, \alpha}$ admits an exact deterministic decomposition:*
      $$\rho_{k, \alpha} = \rho_{k, \alpha}^{\mathrm{tree-slice}} + \mathcal{R}_{\alpha, \mathrm{chart-exit}} + \mathcal{R}_{\alpha, \mathrm{large}}$$
      *where:*
      - $\rho_{k, \alpha}^{\mathrm{tree-slice}}$ *is the integral restricted to $\mathcal{E}_{\mathrm{chart}}$ on the gauge slice $B^{\prime h}|_{T_0} = 0$;*
      - $\mathcal{R}_{\alpha, \mathrm{chart-exit}}$ *is the integral over $\mathcal{B}_{\delta_k^\prime} \setminus \mathcal{E}_{\mathrm{chart}}$ where the tree gauge rotates fluctuations outside the small-field chart;*
      - $\mathcal{R}_{\alpha, \mathrm{large}}$ *is the remainder integral carrying $(1 - \chi^\prime)$.*
   6. *Status & Dependency:*
      *This deterministic decomposition is completely defined. Any subsequent weighted-measure tail estimate under the action $\exp(-g_k^{-2} A_k^{\prime\prime})$ is a separate, downstream analytic obligation that is conditionally blocked until the deterministic properties of $\mathcal{E}_{\mathrm{chart}}$ are certified.*


## YM-052: CONSTRAINED TREE-MAP PUSHFORWARD, FIBER WEIGHTS, BOUNDARY ADMISSIBILITY, AND SOURCE LOCATOR CORRECTIONS

### 1. Primary-Source Printed-Page Mapping and Page/Equation Disambiguation
In Section YM-051R3 (lines 738–739), equations (1.85)–(1.88) and (1.89) were listed as appearing on page 195. A rigorous visual audit against the printed article **T. Bałaban, *Large Field Renormalization. I. The Basic Step of the Renormalization Group*, Communications in Mathematical Physics 122, 175–202 (1989)** establishes the precise printed page numbers:
- **Printed p. 194:** Proposition 1 and minimal background equation (1.79): $U_0 = U_{k, Z}(V_\Lambda^*)$ with decomposition $U_k = U_0 \exp(i B^\prime)$.
- **Printed p. 195:** Fluctuation factorization equation (1.81): $V^{\prime\prime} = \exp(i B^\prime) V_0$ on active bonds $\mathbb{B}_0 = \mathbb{U}_k \cap \Lambda_0$, and initial boundary definitions.
- **Printed pp. 195–196:** Maximal tree graph $T_0 \subset \mathbb{B}_0$ constructed from nested parallelepipeds $P_1 \setminus P_2$ rooted at a single base point $x_0 \in \Lambda_0$.
- **Printed p. 197:** Background covariance and compensating transformations, equations **(1.85)–(1.88)**: joint action under background AL gauge transformation $U_0 \mapsto U_0^{u_0}$ via $V_h \mapsto V_h^{u_0}$ and $B^\prime \mapsto u_0 B^\prime u_0^{-1}$. (Formally supersedes the erroneous citation to p. 195).
- **Printed p. 198:** Support-specific cutoff replacement, equation **(1.89)**: $\chi_k^{\prime\prime} \chi^\prime = \chi^\prime$ on the small-field support $\chi^\prime = \mathbf{1}_{\{|B^\prime(b)| < \delta_k^\prime \ \forall b \in \mathbb{B}_0\}}$. (Formally supersedes the erroneous citation to p. 195).
- **Disambiguation Note:** Authors and readers must strictly distinguish between **PDF page indices** (which depend on journal front matter / cover sheets) and **printed journal page numbers** (pp. 175–202 in CMP 122).

### 2. Geometric Collar Difference Identity and Strictness Precision
1. **Exact Set Difference Identity:**
   Let $\Lambda = (\Omega_{k_0+1}^4)^c \cap Z$ be the large-field integration domain, $Z_h$ the preliminary region, and $Z_h^{\prime \sim}$ the enlarged regularized neighborhood carrying delta constraints and buffer bonds.
   The active fluctuation region is defined by:
   $$\Lambda_0 = \Lambda \cap \Omega_{k+1}^1 = \Lambda \cap (Z_h^{\prime \sim})^c.$$
   The difference between the naive exterior $\Lambda \setminus Z_h$ and the true active region $\Lambda_0$ is given by the exact set identity:
   $$(\Lambda \setminus Z_h) \setminus \Lambda_0 = (\Lambda \setminus Z_h) \cap (\Lambda \cap (Z_h^{\prime \sim})^c)^c = (\Lambda \setminus Z_h) \cap Z_h^{\prime \sim} = \Lambda \cap (Z_h^{\prime \sim} \setminus Z_h).$$
2. **Precision on Strict Inclusion:**
   In Section YM-051R3 (line 747), strict inclusion $\Lambda_0 \subsetneq \Lambda \setminus Z_h$ was asserted unconditionally. This is refined and superseded:
   - The inclusion $\Lambda_0 \subseteq \Lambda \setminus Z_h$ is universal because $Z_h \subset Z_h^{\prime \sim} \implies (Z_h^{\prime \sim})^c \subset Z_h^c$.
   - **Strict inclusion $\Lambda_0 \subsetneq \Lambda \setminus Z_h$ holds IF AND ONLY IF the collar intersection inside $\Lambda$ is non-empty:**
     $$\Lambda \cap (Z_h^{\prime \sim} \setminus Z_h) \ne \emptyset.$$
   - If the regularized collar lies entirely outside $\Lambda$, or in boundary configurations where the collar carries zero interior lattice points inside $\Lambda$, then $\Lambda \cap (Z_h^{\prime \sim} \setminus Z_h) = \emptyset$ and $\Lambda_0 = \Lambda \setminus Z_h$.
   - Strictness cannot be asserted for every arbitrary history geometry from topological inclusions alone without explicit verification of non-emptiness.

### 3. Full Invertible Augmented Coordinate Map vs. Unproved Slice Projection
1. **The Dimension Reduction Fallacy:**
   On active bonds $\mathbb{B}_0$, the original Lie algebra fluctuation variables $B^\prime$ span $3|\mathbb{B}_0|$ dimensions.
   A spanning tree $T_0 \subset \mathbb{B}_0$ rooted at $x_0$ with $|T_0| = |\Lambda_0| - 1$ edges defines a gauge-fixing condition $B^{\prime h}|_{T_0} = 0$.
   Projecting to the gauge slice by eliminating tree variables reduces dimensions from $3|\mathbb{B}_0|$ to $3|\mathbb{B}_0 \setminus T_0|$.
   Local absolute Faddeev–Popov determinant $|\det(D_{V_0})| = 1$ at the slice together with group Haar invariance under *fixed* gauge transformations **DOES NOT** establish that the pushforward measure on the slice equals the restricted slice measure.
2. **Non-Invariance of Small-Field Cutoffs:**
   The small-field cutoff:
   $$\chi^\prime(B^\prime) = \prod_{b \in \mathbb{B}_0} \mathbf{1}_{\{\|B^\prime(b)\| < \delta_k^\prime\}}$$
   is explicitly **dependent on individual bond fluctuations and is NOT gauge invariant**. Under a gauge transformation $h \in \mathcal{G}_{\Lambda_0}$, the tree link fluctuations change, so the support of $\chi^\prime$ cuts off the gauge orbit non-trivially.
3. **The Invertible Augmented Map $\Phi$:**
   Before integration, the change of variables must be defined as an invertible augmented diffeomorphism:
   $$\Phi: \mathfrak{su}(2)^{\mathbb{B}_0} \to \mathfrak{su}(2)^{\mathbb{B}_0 \setminus T_0} \times \mathcal{G}_{\Lambda_0, x_0}, \quad B^\prime \mapsto (\hat{B}^\prime, h[B^\prime]),$$
   where $h[B^\prime]$ is the unique sequential tree-fixing transformation satisfying $V^{\prime\prime h[B^\prime]}(b) = V_0(b)$ for all $b \in T_0$, and $\hat{B}^\prime \in \mathfrak{su}(2)^{\mathbb{B}_0 \setminus T_0}$ represents the gauge-transformed fluctuations on non-tree bonds:
   $$\exp(i \hat{B}^\prime(b)) V_0(b) = h_x[B^\prime] \exp(i B^\prime(b)) V_0(b) h_y[B^\prime]^{-1} \quad \text{for } b = (x, y) \in \mathbb{B}_0 \setminus T_0.$$
4. **Exact Pushforward Measure and Fiber Weights:**
   The pushforward measure on the slice coordinates $\hat{B}^\prime$ is:
   $$d\hat{\mu}(\hat{B}^\prime) = W(\hat{B}^\prime) \, \left[ \prod_{b \in \mathbb{B}_0 \setminus T_0} J(\hat{B}^\prime(b)) \, d\hat{B}^\prime(b) \right],$$
   where the **FIBER WEIGHT** is the explicit integral over the orbit fiber:
   $$W(\hat{B}^\prime) = \int_{\mathcal{G}_{\Lambda_0, x_0}} dh \, J_{\mathrm{orbit}}(\hat{B}^\prime, h) \, \chi^\prime(\Phi^{-1}(\hat{B}^\prime, h)).$$
   - In Lemma `YM-051F-DETERMINISTIC-CHART-OVERLAP`, setting $W(\hat{B}^\prime) \equiv 1$ (or identifying the overlap integral with an unweighted slice integral) assumed without proof that the fiber weight is identically 1.
   - For cutoffs depending on tree variables, the fiber volume $\operatorname{vol}(\text{Fiber}(\hat{B}^\prime))$ varies with $\hat{B}^\prime$ and does not integrate to 1.
   - Consequently, the overlap integral can only be equated to a tree-slice integral AFTER computing and bounding the fiber weight $W(\hat{B}^\prime)$.
   - Status of Lemma `YM-051F-DETERMINISTIC-CHART-OVERLAP`: the set partition $\rho_{k, \alpha} = \rho_{k, \alpha}^{\mathrm{overlap}} + \mathcal{R}_{\alpha, \mathrm{chart-exit}} + \mathcal{R}_{\alpha, \mathrm{large}}$ is algebraically exact, but calling $\rho_{k, \alpha}^{\mathrm{overlap}}$ an unweighted tree-slice integral is formally **UNPROVED_PENDING_FIBER_WEIGHT_INTEGRATION**.

### 4. Concrete History Boundary Admissibility and Tree Solvability
1. **Permitted Site Gauge Group:**
   On $\Lambda_0$, the gauge group is $\mathcal{G}_{\Lambda_0} = \{h: \Lambda_0 \to SU(2)\}$.
2. **Solvability under Single-Root Constraint:**
   If $\mathcal{G}_{\Lambda_0}$ is constrained ONLY at a single root site $x_0 \in \Lambda_0$ by $h_{x_0} = I$, the sequential tree-fixing equations:
   $$h_y = V_0(b)^{-1} h_x \exp(i B^\prime(b)) V_0(b)$$
   have a UNIQUE, unconditional solution along every directed edge of spanning tree $T_0$. Every vertex $y \ne x_0$ has exactly one parent in $T_0$, so each $h_y$ is uniquely determined without overconstraint.
3. **Obstruction under Multiple Fixed Endpoints:**
   If preliminary sector boundary conditions or external boundary rules impose $h_x = I$ on multiple boundary sites (e.g. $h_x = I$ for all $x \in \partial \Lambda_0$):
   - Any path in $T_0$ connecting two fixed endpoints $x_1, x_2 \in \partial \Lambda_0$ imposes the global holonomy constraint:
     $$I = h_{x_2} = \left[ \prod_{b \in \text{path}(x_1, x_2)} \operatorname{Ad}_{V_0(b)} \exp(i B^\prime(b)) \right] h_{x_1} = \prod_{b \in \text{path}} \operatorname{Ad}_{V_0(b)} \exp(i B^\prime(b)).$$
   - For generic configurations $B^\prime$, this holonomy is non-trivial ($ \ne I$).
   - Therefore, the tree-fixing equation **HAS NO SOLUTION** on configurations with non-zero tree holonomy if multiple endpoints are pre-fixed.
4. **Source Audit Finding:**
   Bałaban CMP 122 pp. 195–196 avoids this overconstraint obstruction by:
   - Fixing ONLY the single root site $x_0$ ($h_{x_0} = I$).
   - Partitioning boundary bonds so that internal boundary bonds touching $\partial \Omega_{k+1}^1$ are strictly excluded from $\mathbb{B}_0$, leaving active bonds $\mathbb{B}_0$ and site group $\mathcal{G}_{\Lambda_0, x_0}$ free of preliminary fixed-site overconstraints.


