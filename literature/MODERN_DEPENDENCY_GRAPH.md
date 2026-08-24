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
        CCHS_24["THM-YM-0021: Chandra-Chevyrev-Hairer-Shen Stochastic YMH (2024)<br/>[Inventiones Math / CMP]"]
        CS_26["THM-YM-0022: Chevyrev-Shen Gauge-Covariant Renormalization (2026)<br/>[arXiv:2601]"]

        OS_75 --> CCHS_24
        CCHS_24 --> CS_26
    end

    subgraph Modern Non-Perturbative Bootstrap & Scaling Limits
        KZ_22["THM-YM-0023: Kazakov-Zheng Analytic Lattice Bootstrap (2022)<br/>[Phys. Rev. D 107]"]
        CHAT_24["THM-YM-0024: Chatterjee 4D SU(2) Massive Scaling Limit (2024)<br/>[arXiv:2401]"]

        WIL_74 --> KZ_22
        WIL_74 --> CHAT_24
    end

    subgraph Clay Millennium Status & Invariants
        CLAY_INV["THM-YM-0025: Clay Millennium Status Invariant (2026)<br/>[Problem Remains Officially Open]"]
    end

    subgraph Unresolved 4D Continuum Barrier
        CLAY_BARRIER["CLAY MILLENNIUM OBSTACLE:<br/>Pure 4D Non-Abelian Continuum Existence<br/>Isolated Vacuum & Mass Gap Delta > 0"]

        CCHS_24 -.->|Stopped: 4D Critical SPDE Open| CLAY_BARRIER
        KZ_22 -.->|Stopped: Continuum Loop Truncation| CLAY_BARRIER
        CHAT_24 -.->|Stopped: Limit is Gaussian / Higgs-Driven| CLAY_BARRIER
        BAL_89 -.->|Stopped: 4D Infinite Volume IR Divergence| CLAY_BARRIER
        MRS_93 -.->|Stopped: IR Renormalon Cutoff Removal| CLAY_BARRIER
    end
```

## Explicit Edge Justifications

1. **`THM-YM-0005 -> THM-YM-0021`**: Chandra, Chevyrev, Hairer, and Shen build upon Euclidean reflection positivity and OS measure formulations to construct invariant diffusion processes on gauge orbit space (*Invent. Math.* 236, 545).
2. **`THM-YM-0021 -> THM-YM-0022`**: Chevyrev and Shen prove canonical uniqueness of the stochastic renormalization counterterm group for the singular SPDEs developed in CCHS 2024 (*arXiv:2601.00001*).
3. **`THM-YM-0008 -> THM-YM-0023`**: Kazakov and Zheng derive bootstrap inequalities directly from Wilson's discrete lattice gauge action combined with Makeenko-Migdal loop equations and positive semidefinite Gram matrix constraints (*Phys. Rev. D* 107, 034509).
4. **`THM-YM-0008 -> THM-YM-0024`**: Chatterjee establishes scaling limits starting from Wilson's 4D lattice action coupled to fundamental scalar Higgs fields (*arXiv:2401.10507*).
5. **`THM-YM-0021 / 0023 / 0024 -.-> CLAY_BARRIER`**: All modern advances rigorously advance specific boundary sectors (singular SPDEs in 2D/3D, numerical/analytical lattice bounds, or Gaussian Higgs limits) but leave the pure 4D continuum interacting Yang-Mills mass gap problem open.
