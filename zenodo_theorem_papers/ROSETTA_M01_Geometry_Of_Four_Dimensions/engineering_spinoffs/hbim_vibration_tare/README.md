# HBIM Schur Vibration Tare Toolkit

**Heritage Building Information Modeling (HBIM) Structural Health Monitoring**  
**Author:** Qamar Munawer  
**Affiliation:** Brandenburg University of Technology Cottbus-Senftenberg  
**Methodology Note:** ai is being used as a tool  
**Epistemic Status:** `status: verified-finite practical engineering toolkit`

---

## 1. Overview and Engineering Background

In structural health monitoring of historic masonry vaults, cathedrals, and timber trusses (Heritage BIM / HBIM), vibration sensors placed on critical keystones and piers capture vast amounts of low-frequency ambient environmental drift:
- Diurnal solar thermal expansion cycles ($0.00001$ to $0.05$ Hz).
- Heavy street traffic and railway ground rumble ($1.0$ to $3.0$ Hz).
- Foundation ground creep and wind sway.

Meanwhile, structural damage—such as mortar joint slipping, micro-fracturing of ashlar blocks, and crack propagation—presents as high-frequency modal shifts ($\omega_{\text{crack}} \ge 15$ Hz) with tiny vibration amplitudes ($<0.5 \text{ mm/s}^2$).

This toolkit implements the **Schur Complement Tare** (Guyan static condensation) coupled with a **Three-Tier Sub-Gap Spectral Filter** to eliminate bulk environmental noise without requiring expensive finite element supercomputing.

---

## 2. Mathematical Foundation

### Spatial Guyan / Schur Condensation
Partition the structural stiffness matrix into:
$$K = \begin{pmatrix} A & B \\ B^T & D \end{pmatrix}$$
where:
- $A$: Secondary infill masonry, bulk facade, and boundary noise nodes.
- $D$: Monitored primary structural joints (keystones, piers, abutments).
- $B$: Cross-coupling stiffness.

The condensed Schur complement stiffness matrix is:
$$S_D = D - B^T A^{-1} B$$

For monitored sensor displacements $x(t) = (x_A(t), x_D(t))^T$, the spatial Schur tare subtracts the bulk ambient contribution:
$$x_D^{\text{tared}}(t) = x_D(t) - B^T A^{-1} x_A(t)$$

### Spectral Sub-Gap Taring
The remaining signal is projected through the sub-gap filter:
$$x_{\text{clean}}(t) = (I - P_{\text{sub-gap}}) x_D^{\text{tared}}(t)$$
where modes below $\omega_{\text{cutoff}}$ (environmental drift) are projected to zero.

---

## 3. Benchmark Verification Results

Running `python hbim_schur_tare.py` evaluates an 8-node masonry facade coupled to a 2-node stone arch:
- **Noise Subtracted:** $99.67\%$ of total ambient bulk vibration energy.
- **SNR Improvement:** $+24.78 \text{ dB}$.
- **Target Crack Resonance:** $18.50 \text{ Hz}$ (detected at $18.50 \text{ Hz}$, $0.00 \text{ Hz}$ error).
- **Audit Receipt:** `hbim_schur_tare_receipt.json` (`status: PASS`).

---

## 4. Usage

Run the benchmark and produce the receipt:
```bash
python engineering_spinoffs/hbim_vibration_tare/hbim_schur_tare.py
```

Run automated unit tests:
```bash
python -m unittest engineering_spinoffs/hbim_vibration_tare/test_hbim_schur_tare.py
```
