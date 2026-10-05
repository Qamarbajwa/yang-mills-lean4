# YM-015F-JET-002A — exact normalized source transport

Candidate for YM-035. Evidence: PROVED_WITHIN_STATED_HYPOTHESES, pending independent review. Finite-cutoff identities only; the nonperturbative uniform insertion estimate remains OPEN.

## Objects and disintegration premise

For a fixed finite lattice, Omega=SU(N)^E is compact metrizable. Let H be normalized product Haar measure, S the actual finite continuous Wilson action, Z=integral exp(-S)dH, and mu=exp(-S)H/Z. Then 0<Z<infinity. For t>0 the selected Wilson-flow clover observable is a bounded Borel function at this fixed cutoff; its bound need not be uniform in a. Let X=O_(a,t)(f)/||f||_(H^3) for f nonzero; zero tests give zero insertion.

Let Q:Omega->Y be Borel with Y standard Borel. The disintegration theorem gives m=Q_#H and probability kernels H_y supported on Q^{-1}(y) for m-almost every y. Verified source statement: Gagne–Panangaden, *A Categorical Characterization of Relative Entropy on Standard Borel Spaces*, Theorem 2.3, printed pages137–138, supplies this probability disintegration for standard Borel spaces, with almost-everywhere fiber support, measurability and the integral identity. [Author-hosted primary text](https://www.cs.mcgill.ca/~prakash/Pubs/ccre.pdf), PDF pages3–4. Access: theorem statement directly inspected; no formal machine proof invoked.

## T1: vacuum and degree-one transport

Define, m-almost everywhere,

    w(y)=integral exp(-S)dH_y,
    v(y)=integral exp(-S)X dH_y,
    K_y=exp(-S)H_y/w(y),
    nu=w m/Z,    X_eff=v/w.

Since exp(-S) is strictly positive and bounded above and below at fixed lattice parameters, w>0. K_y is a probability kernel, nu=Q_#mu, and X_eff=integral X dK_y. S_eff=-log w is an action relative to reference m; no locality or Bałaban norm assertion follows.

For eta^2=0 the identity

    integral exp(-S)(1+eta X)dH_y = w(1+eta X_eff)

holds coefficientwise. Integrate against m and divide by the vacuum Z to obtain

    Z^{-1} integral w(1+eta X_eff)dm = 1+eta integral X_eff dnu
                                             = 1+eta integral X dmu.

Proof: definitions and disintegration, applied to real/imaginary parts as needed. No source-dependent denominator was silently substituted. Normalizing by the full source partition instead would make the source expectation identically one and erase the desired derivative.

## T2: norm transport and its limitation

For 1<=p<infinity, conditional Jensen and disintegration give

    integral |X_eff|^p dnu <= integral |X|^p dmu.

The constant is one. With finite jets P(U)=sum_S z_S P_S(U) and weights r_i>0, coefficientwise conditional integration yields

    ||integral P dK_y||_r <= integral ||P||_r dK_y,
    integral ||integral P dK_y||_r dnu <= integral ||P||_r dmu.

The coefficient norm is defined in YM_015F_SOURCE_JET_REDUCTION.md. These inequalities transport existing integrability, rather than create cutoff-uniform input norms, flow locality, strict contraction, or small source-polymer activities. At general p the right side may diverge with cutoff; at fixed cutoff it is finite.

FALSIFY signed-piece shortcut: (2 delta_u-delta_v) has total mass one but sends X(u)=1,X(v)=-1 to3, despite ||X||_infinity=1. Its total variation is3, not1. Jensen cannot be applied to individual signed polymer pieces. A reconstructed positive Wilson measure does not make each effective activity positive.

## T3: second source defect and exact correction

For two distinct commuting labels z_1^2=z_2^2=0, direct transport gives

    E_K[(1+z_1 X_1)(1+z_2 X_2)]
      =1+z_1 m_1+z_2 m_2+z_1 z_2 m_12,

where m_i=E_K X_i and m_12=E_K(X_1 X_2). The approximation retaining only effective single insertions is (1+z_1 m_1)(1+z_2 m_2). Its exact defect is

    D=z_1 z_2 c_12,    c_12=m_12-m_1 m_2.

Adding this coefficient corrects the jet exactly at degree two. This finite algebra identity does not prove a small or summable correction norm. For complex observables c_12 is the bilinear connected coefficient without conjugation; Cauchy–Schwarz bounds it by the product of conditional centered L2 norms. At higher degree the full transported jet contains all conditional joint coefficients, not merely products of means.

FALSIFY source-factorization shortcut: let Q be constant and X_1=X_2 take values +1,-1 with equal probabilities. Then m_1=m_2=0 but m_12=1. The single-insertion product loses the entire mixed coefficient. Constant-one positive integration alone therefore cannot justify a marked RG closure that drops connected sources.

Exact finite certificates in tests/test_source_jet_finite_certificates.py check normalization, signed-kernel failure and this second-order defect using rational arithmetic. These certify the displayed finite examples only. The general identities above depend on the stated measure hypotheses and their analytical derivations, not on tests.

## Load-bearing residual and next task

No equality between this abstract disintegration and a published source-decorated Bałaban representation is established. The remaining task is to express the exact physically normalized flowed insertion and its conditional connected coefficients in the actual RG coordinates, with cutoff-uniform activity norms, gauge constraints, bad-field sectors, flow tails, vacuum normalization and terminal integration.

Next automatic bounded task YM-015F-JET-002B: derive the exact marked coefficient recurrence for a specified Bałaban integration map, including the connected source defect. If the primary source map cannot be extracted, retain that precise source-extraction gap and progress the numbered 3D proof audit independently. Neither T1 nor T2 supplies the missing uniform physical estimate by renaming it as a coarse expectation.

DAG update: T1/T2/T3 are finite interface obligations below OPEN JET-002; JET-002 still feeds conditional L1. E-UV-FLOWED PARTIAL_PROGRESS; local OS/free continuum OPEN_AND_UNSOLVED; crossover/P3 OPEN; YM-016 BLOCKED; structural no-go count0; Clay OPEN_AND_UNSOLVED.
