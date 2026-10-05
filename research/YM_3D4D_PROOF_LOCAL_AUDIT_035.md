# YM 3D/4D proof-local audit 035

Status: CANDIDATE SOURCE AUDIT; no result promotion. Access: 2026-10-04.
Binding: FA-001 of `YM_3D4D_FAILURE_ATLAS.md`; architecture retains YM-015F and the measure/OS/lattice bridges. Only this research note is changed.

## Source-derived extraction (under 200 words)

Chandra–Chevyrev–Hairer–Shen, [publisher full text](https://link.springer.com/article/10.1007/s00222-024-01264-2), §5, immediately before Remark 5.2: κ∈(0,1/100], deg(z)=2−κ, deg(l̄)=−5/2−κ, reg(z)=−1/2−4κ, reg(l̄)=−5/2−2κ. Rule (5.6) is R̊(z)={l̄,z∂ⱼz,zzz}, 1≤j≤3. The paragraph immediately following (5.6) asserts subcriticality and a subcritical completion after normal extension, citing reference [10], §5. This is an exact numbered rule and subsequent proof-construction step, not a numbered failing lemma.

The introduction distinguishes stochastic C^(−1/2−κ) regularity from the YM scaling threshold −1. Section 5.2, (5.15), explicitly says the naive fixed point already fails in 3D because integration requires η∧α>−2. Lemma A.4 supplies extensions at t=0; (5.19)–(5.20) then separate initial data, stochastic convolution, and remainder. Therefore this naive failure cannot identify a 3D/4D separator.

The paper constructs a local stochastic dynamic allowing explosion, not a continuum invariant measure or mass gap. Its §5 notation α is not the diagnostic α below. The [arXiv HTML](https://arxiv.org/html/2201.03487) truncates after (1.1), so the publisher supplies the proof locators.

## Independent calculation, not a source theorem

For parabolic weights (2,1,…,1), physical heat integration gains 2; space-time white noise has regularity below −(d+2)/2. Write a=(2−d)/2−ε, ε>0, without identifying ε with the source's κ or its several slack conventions. The two nonlinear branches of (5.6), after integration, have formal homogeneities 2a+1 and 3a+2. Relative to a their gains are a+1 and 2a+2:

| Dimension | derivative branch gain | cubic branch gain |
|---|---:|---:|
| 3 | 1/2−ε | 1−2ε |
| 4 | −ε | −2ε |

This is renormalised-tree power counting; it does not claim ordinary products of distributions exist.

The source's deliberately reduced kernel degree requires different bookkeeping. For r=reg(z)=−1/2−4κ and b=deg(z)=2−κ, compare each branch's integrated assigned regularity with r:

- noise: b+reg(l̄)−r=κ;
- derivative: b+2r−1−r=1/2−5κ;
- cubic: b+3r−r=1−9κ.

All are positive for the stated κ range. These are independently computed margins using the extracted conventions, not printed numerical estimates attributed to the paper. A formal dimension-adjusted assignment r₄=−1−4κ, reg(l̄)₄=−3−2κ, b=2−κ keeps the noise margin κ but gives −5κ and −9κ for the nonlinear branches. At κ=0 these are zero. Thus the strict subcritical-rule assertion following (5.6) loses its margin under the direct 4D substitution before its subcritical completion can be reused.

The dimension-adjusted assignments are our diagnostic, not a source-prescribed 4D theorem. In physical homogeneity conventions a repair adding output gains δ₂,δ₃ needs δ₂>ε and δ₃>2ε; this differs from the bookkeeping thresholds 5κ,9κ above. Neither a finite positive endpoint gain nor a logarithmic replacement is supplied by the calculation.

## Exact conclusion and remaining extraction

The formerly pending rule-level locator is resolved: (5.6) and its immediately following subcritical completion assertion. The exact first failing numbered lemma is **not established**. Claiming Lemma A.4 fails first would be wrong: it addresses an obstruction already present in 3D. A complete lemma-level transfer audit still needs the cited [10], §5 definition/completion proof and the actual model-convergence and fixed-point estimates under a specified 4D replacement rule. Some publisher formulas are image-only, and no complete reconstruction of those estimates was performed.

Classification: method-specific obstruction to directly reusing this usual subcritical construction; no generic obstruction to critical SPDE methods, no structural no-go. STRUCTURAL_NO_GO_COUNT remains zero. Gauge-compatible endpoint estimates remain hypotheses; neither invariant-measure existence nor YM-015F is closed.
