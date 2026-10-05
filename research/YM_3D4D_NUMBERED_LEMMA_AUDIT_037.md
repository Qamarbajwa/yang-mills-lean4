# YM 3D/4D numbered model-lemma audit 037

Status: CANDIDATE SOURCE AUDIT; no result promotion. Access: 2026-10-05. Binding: Failure Atlas FA-001 and proof-local audit 035. The governance architecture and reconciliation 034 remain binding; YM-015F remains the primary dependency.

## Primary extraction (under 200 source-derived words)

Chandra–Chevyrev–Hairer–Shen, *Stochastic quantisation of Yang–Mills–Higgs in 3D*, [Edinburgh author manuscript](https://www.pure.ed.ac.uk/ws/portalfiles/portal/435998276/YangMills.pdf), dated 24 April 2024; repository cover identifies it as the peer-reviewed version of DOI 10.1007/s00222-024-01264-2. In §5.2.1, Lemma 5.17, manuscript pp. 69–70 (PDF pages 70–71, counting the cover), the BPHZ models converge in probability as the mollifier is removed. Its proof invokes [CH16, Theorem 2.15] and checks three criteria. The third uses

\[
\min\{\deg(\tau):\tau\in\mathcal T(R),\ |N(\tau)|>1\}=-2-2\kappa>-5/2=-|\mathfrak s|/2.
\]

The proof then uses noise degree −5/2−κ for its second criterion and records the worst first-criterion margin as 1−4κ>0. In §5.3, p. 73, model convergence from Lemma 5.17 enters short-time fixed-point stability together with Lemmas 5.18–5.19 and (A.1). These are actual numbered model-convergence and downstream proof locators, beyond rule (5.6).

## Independent dimension diagnostic

The displayed third-criterion inequality has 3D margin 1/2−2κ. In physical parabolic homogeneity conventions, a heat-convolved noise has degree a_d=(2−d)/2−κ. The unintegrated quadratic derivative branch Ψ∂Ψ has degree q_d=2a_d−1=1−d−2κ. Its margin above −(d+2)/2 is

\[
q_d+(d+2)/2=2-d/2-2\kappa.
\]

Thus it is 1/2−2κ in 3D, −2κ in 4D, and zero in 4D at κ=0. This independently calculated branch reproduces the displayed numerical 3D minimum, but matching numbers alone does not identify its printed tree drawing. It does not substitute physical heat-degree conventions for the source's reduced-degree bookkeeping in audit 035.

Under that explicit physical-convention transfer diagnostic, the quadratic derivative branch no longer clears the third criterion used in Lemma 5.17's proof. Adding a power gain δ to this branch would require δ>2κ for that particular sufficient criterion. This is a model-convergence criterion, distinct from the recursive subcriticality margin and its repair threshold in audit 035. No such gain is proved here.

## Exact disposition and gap

Resolved: a numbered model-convergence lemma, its explicit strict inequality, and its use in fixed-point stability are now directly inspected in a primary author manuscript. This is a concrete proof-local transfer obstruction candidate rather than another unlocated scaling statement.

Not resolved: the **first** failing numbered lemma of the complete proof. No earlier numbered statements were exhaustively audited. The full [CH16, Theorem 2.15] hypotheses, the source tree drawing attaining the minimum, and a specified dimension-adjusted rule/model construction remain to be reconciled before asserting an exact 4D criterion failure in the source's conventions. Failure of this sufficient criterion would not prove model convergence impossible, nor falsify any full 4D theorem.

Access record: publisher opening was available; targeted publisher opens timed out and find calls failed. The SISSA publisher-PDF mirror returned HTTP 403. The Edinburgh full PDF text was available and supplied the numbered statement and proof. No full dependency-chain reconstruction was performed.

Classification: METHOD_SPECIFIC_OBSTRUCTION candidate for direct reuse of this subcritical BPHZ proof. STRUCTURAL_NO_GO_COUNT remains zero. No invariant measure, lattice matching, positivity/local OS bridge, YM-015F closure, or physical mass gap follows.
