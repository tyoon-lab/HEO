# HEO Figure Architecture and Captions v2 — AFM / conversion-centered

**Date:** 2026-09-20  
**Target:** Advanced Functional Materials  
**Main-paper identity:** HEO materials/mechanism paper; electrochemical diagnostics support the materials story.

## Figure sequence

### Figure 1 — Crystal structure, composition, and nanoscale microstructure
**Provisional collaborator figure.** Final panel composition and interpretation will be supplied/frozen with the Yoo-group characterization package.

- final refined XRD / lattice parameters / phase assignment;
- ICP-OES / nominal composition;
- HRTEM / SAED / EDS mapping;
- establish the parent spinel-type material and the structural/compositional perturbation introduced by Mg and milling;
- do not overassign Mg site before final refinement;
- remove the chemically impossible preliminary CoGa2O4 indexing.

### Figure 2 — Morphology and physical surface characteristics
**Provisional collaborator figure.** Final panel composition and interpretation will be supplied/frozen with the Yoo-group characterization package.

- SEM morphology;
- particle/domain-size statistics where defensible;
- BET surface area;
- XPS is provisionally kept in the Supporting Information or held pending final collaborator review; only promote it to a separate main characterization figure if the final dataset is unusually strong and materially changes the materials argument;
- keep electrochemically derived interface metrics out of the characterization figures.

Narrative role:
Figures 1–2 establish what the synthesis changed in the material before any electrochemical interpretation is introduced.

### Figure 3 — Conventional electrochemistry: utilization, retention, and conversion evolution
Electrochemistry begins here. Keep the main figure compact and materials-centered.

**Main panels**
- (a) first-cycle voltage profiles: overlay the four materials on a common axis; include first-cycle lithiation/delithiation capacity and ICE as a compact inset/table;
- (b) 0.1 C cycling with the common 10 wt% FEC electrolyte: plot absolute specific capacity only in the main panel;
- (c) absolute rate capability over 0.1–5 C and recovery at 0.1 C;
- (d) cycle-resolved dQ/dV: emphasize selected cycles (preferred: 1, 2, 10, 100) for each material so the first-cycle conversion feature and subsequent reconstruction remain readable.

**Supporting Information**
- no-FEC cycling comparison;
- Coulombic-efficiency evolution;
- normalized rate-capacity retention;
- first three voltage profiles for each material;
- full multi-cycle dQ/dV set if the selected-cycle main panel is used;
- CV-derived relative interfacial-capacitance/ECSA-style comparison.

**Core materials message**
- milling increases accessible capacity/utilization in both Mg-free and Mg-containing compositions;
- BM-HEO has the highest absolute capacity but lower fractional cycling retention;
- Mg lowers low-rate accessible capacity but shows comparatively stronger normalized high-rate retention;
- the large first-cycle dQ/dV feature evolves into a broader/weaker response, consistent with a reconstructed post-first-cycle state;
- do not quantify/assign the exact conversion-peak displacement here; reserve that analysis for Figure 5.


### Figure 4 — Polarization magnitude and relaxation time are independent
GITT current-off analysis.

- representative 600 s pulse + 3600 s rest;
- apparent fast current-off response;
- Delta E_relax;
- model-free t63;
- key contradiction: Mg lowers polarization but does not shorten relaxation; BM increases capacity but lengthens relaxation.

### Figure 5 — Conversion assignment and experimental conversion phenotype
Experimental figure.

- (a) state-resolved 3 s-to-60 min relaxation response showing the late-stage excess feature;
- (b) background-subtracted GITT excess relaxation on a voltage axis together with independently derived first-cycle cathodic dQ/dV;
- (c) one-to-one comparison of dQ/dV peak voltage versus GITT excess peak voltage;
- (d) peak-amplitude versus FWHM-like width map, marker area proportional to normalized excess.

Current peak-voltage comparison:

| Sample | dQ/dV peak (V) | GITT excess peak (V) |
|---|---:|---:|
| HEO | 0.545 | 0.527 |
| BM-HEO | 0.589 | 0.618 |
| Mg-HEO | 0.419 | 0.387 |
| BM-Mg-HEO | 0.485 | 0.503 |

All pairs agree within 32 mV.

Interpretation:
- use “conversion/transformation-associated excess relaxation”;
- do not claim a unique microscopic conversion step;
- BM: lower + broader response = redistributed accessible conversion;
- Mg: much smaller response + lower-potential shift = suppressed/delayed deeper conversion;
- BM-Mg: partial reopening;
- raw background fits and sensitivity remain in SI.

Data-source boundary:
current dQ/dV peaks were reconstructed from vector first-cycle voltage profiles in the 2026-09-17 progress presentation. Replace with original numerical profiles if recovered.

### Figure 6 — Reduced spatial model of conversion-associated state evolution
Model begins only after the experimental assignment has been established in Figure 5.

- mechanism-sufficiency logic;
- 4 × 7 circular pulse-end radial phi maps;
- pulse-end mean phibar versus model cbar;
- phi is an effective conversion-associated internal-state coordinate, not a measured phase fraction;
- cbar is not calibrated to experimental Q/Qmax;
- frozen model cross-check without refitting:
  BM cbar_peak 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100;
- model is directional and non-unique.

## Main-text narrative

Figure 1: crystal/composition/nanoscale structure  
→ Figure 2: morphology/physical surface characterization  
→ Figure 3: conventional electrochemistry and cycle evolution  
→ Figure 4: polarization–relaxation decoupling  
→ Figure 5: excess relaxation localized to conversion electrochemistry  
→ Figure 6: reduced model rationalization.
