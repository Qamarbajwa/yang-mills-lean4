#!/usr/bin/env python3
"""
update_ym_t05_t06.py

Updates YM_T05 and YM_T06:
1. Universal Author: Qamar Munawer, Brandenburg University of Technology Cottbus-Senftenberg.
2. Zero 'Arqam' or '(BTU)'.
3. 'ai is being used as a tool' in acknowledgments & .zenodo.json.
4. Includes 'How Energy, Quantum Matter, Pfaffian Squares, and Real-Life Fields Connect'.
5. Compiles PDFs via pdflatex (2 passes, 0 errors).
6. Rebuilds Zenodo ZIP bundles.
"""

import json
import os
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

ym_root = Path(r"d:\Comfy UI\yang mills and the mass gap")
papers_dir = ym_root / "zenodo_theorem_papers"

CONNECT_SECTION_YM = r"""
\section{How Energy, Quantum Matter, Pfaffian Squares, and Real-Life Fields Connect}

The mathematical identities certified in \texttt{YangMillsSymanzikQuaternionAndYJunctionCert.lean} connect directly to observable physical reality across quantum chromodynamics and topological materials:

\begin{enumerate}
  \item \textbf{Symanzik Improvement and Relativistic Spacetime Symmetry:}
  In quantum field theory, discrete lattice discretizations break continuous Lorentz/Euclidean rotational invariance $SO(4)$. The exact L\"uscher--Weisz rational weight cancellation $c_0 + 8c_1 = 1$ and $(1/12)c_0 + (20/12)c_1 = 0$ eliminates $O(a^2)$ lattice discretization errors, restoring isotropic relativistic invariance in quantum computer simulations of the vacuum.
  
  \item \textbf{Non-Abelian Twist and Center Vortex Energy Defects:}
  Unlike Abelian electrodynamics where commuting $U(1)$ phases yield vanishing topological energy $E(2) = 0$, non-Abelian $SU(2)$ quaternionic twists produce an exact topological energy defect $E(-2) = 2$. This topological defect eliminates toron zero-mode infrared divergence, anchoring a strictly positive energy floor in non-abelian gauge vacua.
  
  \item \textbf{Baryonic Three-Slit Y-Junction and Quark Confinement:}
  In baryons containing three quarks ($qqq$), color flux tubes meet at a $120^\circ$ Steiner Fermat--Torricelli junction. The constructive geometric inequality $L_Y^2 > (a+b+c)^2 / 3 > 0$ proves that the three-body potential cannot collapse, establishing an indestructible geometric string tension floor that confines three quarks into protons and neutrons.
  
  \item \textbf{Pfaffian Parity and Quantum Matter Superconductors:}
  Quaternionic and Clifford matrix structures govern topological superconductivity and Majorana edge modes. The non-vanishing Pfaffian invariant ensures topological stability of the gap against boundary perturbations.
\end{enumerate}
"""

def main():
    targets = [
        papers_dir / "YM_T05_Finite_To_Continuum_OS_And_Symanzik",
        papers_dir / "YM_T06_Balaban_Multiscale_Mass_Floor_And_Area_Law"
    ]
    for pdir in targets:
        tex_path = list(pdir.glob("*.tex"))[0]
        txt = tex_path.read_text(encoding="utf-8")

        # 1. Author and BTU sanitize
        txt = txt.replace("BTU Cottbus-Senftenberg", "Brandenburg University of Technology Cottbus-Senftenberg")
        txt = txt.replace("(BTU) ", "").replace("(BTU)", "")
        txt = re.sub(r"\bArqam\b", "Qamar Munawer", txt)

        # 2. Add Connect Section if missing
        if "How Energy, Quantum Matter" not in txt:
            if r"\section{Conclusion}" in txt:
                txt = txt.replace(r"\section{Conclusion}", CONNECT_SECTION_YM + "\n" + r"\section{Conclusion}", 1)
            elif r"\begin{thebibliography}" in txt:
                txt = txt.replace(r"\begin{thebibliography}", CONNECT_SECTION_YM + "\n" + r"\begin{thebibliography}", 1)
            else:
                txt = txt.replace(r"\end{document}", CONNECT_SECTION_YM + "\n" + r"\end{document}", 1)

        # 3. ai is being used as a tool
        if "ai is being used as a tool" not in txt.lower():
            note = r"""
\section*{Methodology Note}
Throughout this research, ai is being used as a tool to assist with formal verification in Lean 4, numerical simulation, and manuscript preparation.
"""
            txt = txt.replace(r"\begin{thebibliography}", note + "\n" + r"\begin{thebibliography}", 1)

        tex_path.write_text(txt, encoding="utf-8")
        print(f"[OK] Updated {tex_path.name}")

        # 4. Update .zenodo.json
        zpath = pdir / ".zenodo.json"
        if zpath.exists():
            zdata = json.loads(zpath.read_text(encoding="utf-8"))
            zdata["creators"] = [{"name": "Qamar Munawer", "affiliation": "Brandenburg University of Technology Cottbus-Senftenberg"}]
            desc = zdata.get("description", "")
            desc = desc.replace("BTU Cottbus-Senftenberg", "Brandenburg University of Technology Cottbus-Senftenberg").replace("(BTU)", "")
            if "ai is being used as a tool" not in desc.lower():
                desc += " In this work, ai is being used as a tool to assist in formal verification and manuscript preparation."
            zdata["description"] = desc
            zpath.write_text(json.dumps(zdata, indent=2), encoding="utf-8")
            print(f"[OK] Updated .zenodo.json in {pdir.name}")

        # 5. Compile PDF
        for step in range(2):
            res = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_path.name], cwd=pdir, capture_output=True, text=True)
            if res.returncode != 0:
                print(f"[ERROR] pdflatex failed on {tex_path.name} pass {step+1}:")
                print(res.stdout[-1000:])
                raise RuntimeError("pdflatex compilation error")
        pdf_path = pdir / (tex_path.stem + ".pdf")
        print(f"[OK] Compiled {pdf_path.name} ({pdf_path.stat().st_size:,} bytes)")

        # 6. Clean aux
        for ext in [".aux", ".log", ".out", ".toc"]:
            aux = pdir / (tex_path.stem + ext)
            if aux.exists():
                try: aux.unlink()
                except Exception: pass

        # 7. Rebuild zip
        zips = list(pdir.glob("*.zip"))
        zip_name = zips[0].name if zips else f"{pdir.name}_ZENODO.zip"
        zip_path = pdir / zip_name
        all_files = [f for f in pdir.iterdir() if f.is_file() and f.suffix not in [".zip", ".aux", ".log", ".out", ".toc"]]
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in all_files:
                zf.write(f, arcname=f.name)
        print(f"[OK] Rebuilt {zip_path.name} ({zip_path.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
