# MODERN DEPENDENCY GRAPH (2000–2026)

## Logical and Technical Prerequisite Structure

```mermaid
flowchart TD
    subgraph Foundational & Constructive Precursors
        OS_75["THM-YM-0005: Osterwalder-Schrader (1975)"]
        WIL_74["THM-YM-0008: Wilson Lattice Gauge Theory (1974)"]
        BAL_89["THM-YM-0018: Bałaban 4D UV Stability (1988-89)"]
        MRS_93["THM-YM-0020: Magnen-Rivasseau-Sénéor YM4 with IR Cutoff (1993)"]
    end

    subgraph Singular SPDE / Stochastic Quantization
        CCHS_22["THM-YM-0021: Chandra-Chevyrev-Hairer-Shen 2D YM Langevin (2022)<br/>[Publ. Math. IHES 136]"]
        CCHS_24["THM-YM-0022: Chandra-Chevyrev-Hairer-Shen 3D YMH Flow (2024)<br/>[Inventiones Math 237]"]
        CS_26["THM-YM-0023: Chevyrev-Shen 3D YMH Counterterm Uniqueness (2026)<br/>[ARMA 250]"]

        OS_75 --> CCHS_22
        OS_75 --> CCHS_24
        CCHS_24 --> CS_26
    end

    subgraph Modern Non-Perturbative Lattice Bounds & Functional Inequalities
        KZ_23["THM-YM-0024: Kazakov-Zheng Large-N Lattice Bootstrap (2023)<br/>[Phys. Rev. D 107]"]
        KZ_24["THM-YM-0025: Kazakov-Zheng Finite-N Lattice Bootstrap (2024)<br/>[arXiv:2404]"]
        SZZ_22["THM-YM-0026: Shen-Zhu-Zhu Infinite-Volume Strong-Coupling Mass Gap (2022)<br/>[Ann. Probab. / arXiv:2204]"]
        CNS_25["THM-YM-0027: Cao-Nissim-Sheffield Area Law & Mass Gap Bounds (2025)<br/>[arXiv:2505]"]

        WIL_74 --> KZ_23
        KZ_23 --> KZ_24
        WIL_74 --> SZZ_22
        WIL_74 --> CNS_25
    end

    subgraph Nearby Gauge-Higgs Scaling Limits
        CHAT_24["THM-YM-0028: Chatterjee 4D SU(2) Massive Scaling Limit (2024)<br/>[arXiv:2401]"]
        WIL_74 --> CHAT_24
    end

    subgraph Official Governance Invariant
        CLAY_INV["CLAY_STATUS_INVARIANT_2026:<br/>4D Quantum Yang-Mills Problem Remains Officially Open"]
    end

    subgraph Unresolved 4D Continuum Barrier
        CLAY_BARRIER["CLAY MILLENNIUM OBSTACLE:<br/>Pure 4D Non-Abelian Continuum Existence<br/>Isolated Vacuum & Mass Gap Delta > 0"]

        CCHS_24 -.->|Stopped: 4D Critical SPDE Open / 3D Invariant Measure Open| CLAY_BARRIER
        KZ_24 -.->|Stopped: Continuum Loop Truncation L_max -> inf| CLAY_BARRIER
        SZZ_22 -.->|Missing Bridge: Strong Coupling beta < beta_0 -> Weak Coupling beta -> inf| CLAY_BARRIER
        CNS_25 -.->|Stopped: Discrete Lattice Area Law Bounds| CLAY_BARRIER
        CHAT_24 -.->|Stopped: Limit is Gaussian / Higgs-Driven| CLAY_BARRIER
        BAL_89 -.->|Stopped: 4D Infinite Volume IR Divergence| CLAY_BARRIER
        MRS_93 -.->|Stopped: IR Renormalon Cutoff Removal| CLAY_BARRIER
    end
```

## Explicit Edge Justifications

1. **`THM-YM-0005 -> THM-YM-0021`**: Chandra, Chevyrev, Hairer, and Shen build upon Euclidean reflection positivity and OS measure formulations to construct the 2D invariant Langevin dynamic (*Publ. Math. IHÉS* 136, 1).
2. **`THM-YM-0005 -> THM-YM-0022`**: CCHS use Euclidean regularity structures and gauge orbit geometry to construct the local 3D stochastic flow (*Invent. Math.* 237, 85).
3. **`THM-YM-0022 -> THM-YM-0023`**: Chevyrev and Shen prove canonical uniqueness of the stochastic renormalization counterterm group for the 3D singular SPDE developed in CCHS 2024 (*ARMA* 250, art. 11).
4. **`THM-YM-0008 -> THM-YM-0024`**: Kazakov and Zheng derive large-N bootstrap inequalities directly from Wilson's discrete lattice gauge action combined with planar loop equations (*Phys. Rev. D* 107, L051501).
5. **`THM-YM-0024 -> THM-YM-0025`**: Kazakov and Zheng extend the planar bootstrap to finite-N ($SU(2)$) gauge theories using trace relations and finite-N Gram matrices (*arXiv:2404.16925*).
6. **`THM-YM-0008 -> THM-YM-0026`**: Shen, Zhu, and Zhu construct the infinite-volume Gibbs measure and prove Poincaré/log-Sobolev inequalities starting from Wilson's lattice action at strong coupling (*Ann. Probab.* / *arXiv:2204.12737*).
7. **`THM-YM-0008 -> THM-YM-0027`**: Cao, Nissim, and Sheffield expand Wilson loop area-law bounds using dynamical lattice methods (*arXiv:2505.16585*).
8. **`THM-YM-0008 -> THM-YM-0028`**: Chatterjee establishes scaling limits starting from Wilson's 4D lattice action coupled to fundamental scalar Higgs fields (*arXiv:2401.10507*).
9. **`SZZ_22 -.-> CLAY_BARRIER`**: Shen–Zhu–Zhu rigorously proves an infinite-volume mass gap on the lattice at strong coupling ($eta < eta_0$). The decisive missing bridge is connecting this strong-coupling regime to the weak-coupling continuum trajectory ($eta 	o \infty, g 	o 0, a 	o 0$).
