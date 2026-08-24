# CONSTRUCTIVE DEPENDENCY GRAPH (1980–2000)

## Logical and Technical Prerequisite Structure

```mermaid
flowchart TD
    subgraph Foundational Precursors
        OS_REC["THM-YM-0005: Osterwalder-Schrader Reconstruction (1973/75)"]
        AF["THM-YM-0006: Asymptotic Freedom (1973)"]
        WIL["THM-YM-0008: Wilson Lattice Gauge Theory (1974)"]
        OS_SEIL["THM-YM-0009: Osterwalder-Seiler Lattice RP (1978)"]
        POLY_3D["THM-YM-0011: Polyakov 2+1D Semiclassical Screening (1977)"]
    end

    subgraph Rigorous 3D Confinement & Screening
        GM_81["THM-YM-0013: Göpfert-Mack 3D U(1) Confinement Proof (1981)<br/>[CMP 82, 545]"]
        BFS_82["THM-YM-0014: Brydges-Fröhlich-Spencer Coulomb Screening (1982)<br/>[CMP 83, 123]"]
        SEIL_82["THM-YM-0015: Seiler Constructive Lattice Framework (1982)<br/>[LNP 159, 1]"]

        POLY_3D --> GM_81
        WIL --> GM_81
        POLY_3D --> BFS_82
        OS_SEIL --> SEIL_82
    end

    subgraph Bałaban Multi-Scale Renormalization Group Program
        BAL_PROP["THM-YM-0016: Bałaban RG Averaging & Propagator Bounds (1984-85)<br/>[CMP 95/96/98]"]
        BAL_SF["THM-YM-0017: Bałaban Small-Field Effective Actions (1987-88)<br/>[CMP 109/114/115]"]
        BAL_UV["THM-YM-0018: Bałaban 4D UV Stability & Polymer Expansions (1988-89)<br/>[CMP 116/119]"]

        AF --> BAL_PROP
        WIL --> BAL_PROP
        BAL_PROP --> BAL_SF
        BAL_SF --> BAL_UV
    end

    subgraph Cluster Expansions & IR-Regulated 4D Constructions
        FED_86["THM-YM-0019: Federbush Phase-Cell Cluster Expansions (1986-88)<br/>[CMP 107/114]"]
        MRS_93["THM-YM-0020: Magnen-Rivasseau-Sénéor YM4 with IR Cutoff (1993)<br/>[CMP 155, 325]"]

        BAL_PROP --> FED_86
        BAL_UV --> MRS_93
        AF --> MRS_93
    end

    subgraph The Unresolved 4D Infrared Barrier
        CLAY_BARRIER["CLAY MILLENNIUM OBSTACLE:<br/>Removing 4D IR Cutoff (V -> infty, Lambda_IR -> 0)<br/>Non-Perturbative Mass Gap Delta > 0 in Continuum"]
        
        BAL_UV -.->|Stopped by IR Boundary| CLAY_BARRIER
        MRS_93 -.->|Stopped by IR Renormalons| CLAY_BARRIER
        GM_81 -.->|Abelian / 3D Only| CLAY_BARRIER
    end
```

## Explicit Edge Justifications

1. **`THM-YM-0011 -> THM-YM-0013`**: Göpfert and Mack (1981) mathematically proved the Polyakov 1977 semiclassical monopole Debye screening mechanism for 3D $U(1)$ lattice gauge theory with Villain action (*Comm. Math. Phys.* 82, 545).
2. **`THM-YM-0011 -> THM-YM-0014`**: Brydges, Fröhlich, and Spencer (1982) provided rigorous mathematical bounds for 3D Coulomb / dipole gases underpinning Debye screening (*Comm. Math. Phys.* 83, 123).
3. **`THM-YM-0009 -> THM-YM-0015`**: Seiler (1982) systematically synthesized Osterwalder–Seiler reflection positivity, transfer matrix spectral theory, and cluster expansions for general lattice gauge models (*LNP* 159, 1).
4. **`THM-YM-0006 & THM-YM-0008 -> THM-YM-0016`**: Bałaban's RG averaging operations combine Wilson lattice link variables with asymptotic freedom running across scale steps (*Comm. Math. Phys.* 95, 419; 98, 17).
5. **`THM-YM-0016 -> THM-YM-0017`**: Bałaban's small-field effective action inductively applies the propagator bounds and gauge-fixing operations developed in 1984–1985 (*Comm. Math. Phys.* 109, 249; 114, 627).
6. **`THM-YM-0017 -> THM-YM-0018`**: Bałaban's full 4D UV stability theorem combines the small-field effective actions with convergent polymer expansions for large-field deviations (*Comm. Math. Phys.* 116, 1; 119, 243).
7. **`THM-YM-0016 -> THM-YM-0019`**: Federbush's phase-cell cluster expansion builds upon multi-scale lattice block gauge operations (*Comm. Math. Phys.* 107, 319; 114, 317).
8. **`THM-YM-0018 & THM-YM-0006 -> THM-YM-0020`**: Magnen, Rivasseau, and Sénéor rely on UV asymptotic stability techniques to construct 4D Yang–Mills Schwinger distributions in the presence of an infrared mass cutoff (*Comm. Math. Phys.* 155, 325).
9. **`THM-YM-0018 / THM-YM-0020 -.-> CLAY_BARRIER`**: Neither Bałaban nor Magnen–Rivasseau–Sénéor could take the infinite-volume / zero-IR-cutoff limit in 4D continuum due to the absence of non-perturbative control over infrared confinement and the mass gap.
