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


### Figure 4 — GITT separates relaxation magnitude from relaxation time
Keep the main figure focused on the materials response rather than the short-time fitting procedure.

**Main panels**
- (a) representative 600 s pulse + 3600 s rest, defining $\Delta E_{\mathrm{relax}}$ (3 s → 60 min) and $t_{63}$;
- (b) state-resolved $\Delta E_{\mathrm{relax}}$ for all four materials;
- (c) state-resolved $t_{63}$ for all four materials;
- (d) median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ over 200–800 mAh g⁻¹ as a compact four-material summary.

**Supporting Information**
- 3–30 s $E$ versus $\sqrt{t}$ fits and fit-quality statistics;
- apparent fast current-off resistance versus reaction state;
- sensitivity to the 3 s reference choice if needed;
- full raw representative pulse/rest traces.

**Core materials message**
- ball milling increases accessible capacity but does not accelerate the post-pulse relaxation;
- Mg incorporation strongly lowers the relaxation magnitude but also does not shorten the relaxation time;
- relaxation magnitude and timescale are therefore distinct responses to the materials modifications;
- do not claim diffusion is absent; state only that one changing diffusivity is insufficient to explain all observed trends.

**Transition to Figure 5**
Figure 4 establishes the magnitude–timescale decoupling. Figure 5 then localizes the additional state-dependent relaxation to the conversion region and compares it directly with the first-cycle dQ/dV response.


### Figure 5 — Ball milling redistributes conversion whereas Mg incorporation suppresses it
This is the main mechanistic experimental figure. The dQ/dV–GITT correspondence is used to establish assignment; the materials conclusion is the contrasting BM and Mg response.

**Main panels**
- (a) state-resolved 3 s-to-60 min relaxation response showing the late-stage excess feature;
- (b) background-subtracted GITT excess relaxation on a voltage axis together with first-cycle cathodic dQ/dV for all four materials;
- (c) dQ/dV peak voltage versus GITT excess-peak voltage, used only to validate localization to the conversion window;
- (d) peak-amplitude versus FWHM-like width map, with marker area proportional to normalized excess area.

**Core materials message**
- HEO: relatively concentrated conversion-associated response;
- BM-HEO: higher accessible capacity but lower/broader excess response → conversion redistributed over a broader range of local reaction states;
- Mg-HEO: lower capacity, strongly suppressed excess, and lower-potential conversion response → accessible conversion is reduced/delayed, consistent with stabilization of oxide-derived parent/intermediate states;
- BM-Mg-HEO: milling partially restores capacity and shifts/broadens the Mg-containing response but does not recover the concentrated Mg-free response;
- do not use the small BM-Mg > Mg nominal amplitude difference as a required trend because it is baseline-sensitive.

**Interpretation boundaries**
- use “conversion-associated” or “conversion/transformation-associated” response;
- do not assign the feature to one unique microscopic event;
- lower conversion potential indicates a larger electrochemical driving-force requirement, not a direct equilibrium thermodynamic measurement;
- amplitude is a relaxation-response magnitude, not conversion fraction;
- width is the breadth over reaction state, not a direct phase-distribution measurement;
- normalized excess area is comparative and not dissipated energy.

**Supporting Information**
- raw background fits and subtraction;
- all 105 baseline/window sensitivity combinations;
- smoothing sensitivity for dQ/dV;
- individual material overlays if needed;
- final numerical dQ/dV regeneration once the original first-cycle source is recovered.

**Transition to Figure 6**
Figure 5 establishes experimentally that milling and Mg alter conversion in different ways. Figure 6 tests whether those roles can reproduce the directional state-evolution trends in a reduced spatial model.


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
