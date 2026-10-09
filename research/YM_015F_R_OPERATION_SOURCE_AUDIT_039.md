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
