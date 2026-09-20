# HEO Figure Architecture and Captions v2 — AFM / conversion-centered

**Date:** 2026-09-20  
**Target:** Advanced Functional Materials  
**Main-paper identity:** HEO materials/mechanism paper; electrochemical diagnostics support the materials story.

## Figure sequence

### Figure 1 — What synthesis changed
Structural/compositional/interfacial perturbations across HEO / BM-HEO / Mg-HEO / BM-Mg-HEO.

- final refined XRD / composition / microscopy;
- BET/interface comparison;
- do not overassign Mg site before final ICP/refinement;
- remove chemically impossible preliminary CoGa2O4 indexing.

### Figure 2 — How much reaction became accessible
Electrochemical accessibility and utilization.

- BET / relative interface;
- first-cycle profiles and capacities;
- cycling and rate capability;
- central contrast: BM increases accessible conversion; Mg lowers accessible conversion despite comparable or higher external area.

### Figure 3 — Polarization magnitude and relaxation time are independent
Current-off analysis.

- representative 600 s pulse + 3600 s rest;
- apparent fast current-off response;
- Delta E_relax;
- model-free t63;
- key contradiction: Mg lowers polarization but does not shorten relaxation; BM increases capacity but lengthens relaxation.

### Figure 4 — Conversion assignment and experimental conversion phenotype
This figure is experimental only.

**Preferred current layout**
- (a-d) each sample: normalized first-cycle cathodic dQ/dV response versus voltage with the corresponding GITT excess-relaxation peak voltage;
- (e) one-to-one comparison of dQ/dV peak voltage versus GITT excess peak voltage;
- (f) peak-amplitude versus FWHM-like width map, marker area proportional to normalized excess.

Current peak-voltage comparison:

| Sample | dQ/dV peak (V) | GITT excess peak (V) |
|---|---:|---:|
| HEO | 0.545 | 0.527 |
| BM-HEO | 0.589 | 0.618 |
| Mg-HEO | 0.419 | 0.387 |
| BM-Mg-HEO | 0.485 | 0.503 |

All pairs agree within 32 mV.

**Interpretation**
- use “conversion/transformation-associated excess relaxation”;
- do not claim the signal uniquely measures metal/Li2O nucleation or one crystallographic transition;
- BM: lower + broader response = redistributed accessible conversion;
- Mg: much smaller response + lower-potential shift = suppressed/delayed deeper conversion;
- BM-Mg: partial reopening.

Raw state-resolved curves, background fits, and baseline/window sensitivity can move to SI.

**Data-source boundary**
The current dQ/dV peaks were reconstructed from vector first-cycle voltage profiles in the 2026-09-17 progress presentation. Replace with original numerical continuous-GCD profiles if recovered before submission.

### Figure 5 — Reduced spatial model of conversion-associated state evolution
Model begins only after the experimental conversion assignment has been established in Figure 4.

- (a) mechanism-sufficiency logic;
- (b) 4 × 7 circular pulse-end radial phi maps;
- (c) pulse-end mean phibar versus model cbar.

Updated meaning:
- phi ~ 0: oxide-derived parent/intermediate state;
- larger phi: progression toward a more deeply converted state;
- phi is not a measured rock-salt, metal, or Li2O fraction;
- cbar is not calibrated to experimental Q/Qmax.

Frozen model cross-check without refitting:
BM cbar_peak 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100.
This earlier-to-later model ordering matches the experimental higher-to-lower conversion-peak voltage ordering.

The model is directional and non-unique. It does not explicitly resolve stoichiometric Li2O formation, metallic nanoparticle nucleation, sequential transition-metal reduction, or oxygen redistribution.

## Main-text narrative

Figure 1: synthesis perturbation  
→ Figure 2: utilization/accessibility  
→ Figure 3: polarization–relaxation decoupling  
→ Figure 4: excess relaxation is localized to conversion electrochemistry; BM redistributes while Mg suppresses/delays  
→ Figure 5: reduced model shows those directions can coexist with independent stabilization and heterogeneity coordinates.
