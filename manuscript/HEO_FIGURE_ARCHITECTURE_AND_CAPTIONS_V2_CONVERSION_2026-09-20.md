# HEO Figure Architecture and Captions v2 — AFM / conversion-centered

**Date:** 2026-09-20  
**Target:** Advanced Functional Materials  
**Main-paper identity:** HEO materials/mechanism paper; electrochemical diagnostics support the materials story.

## Figure sequence

### Figure 1 — Crystal structure, composition, and nanoscale microstructure
Characterization only.

- final refined XRD / lattice parameters / phase assignment;
- ICP-OES / nominal composition;
- HRTEM / SAED / EDS mapping;
- establish the parent spinel-type material and the structural/compositional perturbation introduced by Mg and milling;
- do not overassign Mg site before final refinement;
- remove the chemically impossible preliminary CoGa2O4 indexing.

### Figure 2 — Morphology and physical surface characteristics
Characterization only.

- SEM morphology;
- particle/domain-size statistics where defensible;
- BET surface area;
- optional XPS only if the final dataset is reproducible and mechanistically defensible;
- keep electrochemically derived interface metrics out of the characterization figures.

Narrative role:
Figures 1–2 establish what the synthesis changed in the material before any electrochemical interpretation is introduced.

### Figure 3 — Conventional electrochemistry and evolving conversion behavior
Electrochemistry begins here.

- first-cycle voltage profiles + capacity / initial-efficiency summary;
- cycling performance with common FEC condition;
- no-FEC comparison as interphase-control evidence where useful;
- rate capability from 0.1 C to 5 C + recovery;
- cycle-resolved dQ/dV showing the strong first-cycle cathodic feature and its evolution in later cycles;
- relative interfacial-capacitance metric, if retained in main text, explicitly as an electrochemical accessibility descriptor rather than absolute ECSA.

Literature alignment:
- milling/fragmentation increasing accessible conversion and interfacial storage is consistent with prior (FeCoNiCrMn)3O4 work;
- Mg-related capacity suppression is directionally consistent with stabilization reported in related Mg-containing HEO systems;
- strong first-cycle-to-later-cycle dQ/dV evolution is consistent with reconstructive conversion and persistent reconstructed states.

Narrative role:
establish the conventional electrochemical trends first, then state what these data cannot determine: whether the differences arise from Li transport, conversion onset/extent/distribution, or post-conversion relaxation.

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
