# HEO Figure Architecture and Captions v1

**Date:** 2026-09-18  
**Status:** Main-text figure architecture for manuscript v1  
**Design principle:** each Figure answers one scientific question. Characterization is grouped by its role in the argument rather than by instrument.

---

# Overall figure sequence

## Figure 1 — What structural/material perturbations are introduced by Mg and ball milling?

**Question answered:** What is changed before electrochemical cycling?

### Panel architecture

**a. Synthesis and 2 × 2 sample matrix**  
Compact schematic showing the common spinel HEO synthesis and the two controlled perturbations:

- HEO
- BM-HEO
- Mg-HEO
- BM-Mg-HEO

The schematic should emphasize that Mg is the composition variable and ball milling is the processing variable. Keep synthesis details minimal; full recipe belongs in Methods.

**b. XRD patterns of the four samples**  
Full spinel-pattern comparison with one enlarged inset around the principal reflection near 35.7°. The inset should show the small Mg-associated low-angle shift and the milling-induced peak broadening. Do not annotate a unique Mg site. Use final collaborator indexing only.

**c. SEM morphology comparison**  
Matched-magnification images for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. The role of this panel is to visualize the processing-induced morphology change, not to infer a quantitative diffusion length.

**d. TEM/HRTEM + SAED/EDS evidence**  
Use the collaborator-finalized structural assignment. Preferred composition is one compact representative HRTEM/SAED comparison plus EDS maps demonstrating multication homogeneity and Mg detection in Mg-containing samples. Do not use the preliminary CoGa2O4 labels.

### Main message

Mg modifies the parent spinel lattice only modestly, whereas ball milling produces the larger microstructural perturbation/disorder. These are two physically different starting states for the electrochemical comparison.

### Draft caption

**Figure 1. Structural and microstructural perturbations introduced by Mg incorporation and ball milling.** (a) Schematic of the four-sample comparison separating composition (Mg-free versus Mg-containing) from mechanical processing (pristine versus ball-milled). (b) X-ray diffraction patterns of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, with an enlarged view of the principal spinel reflection near 35.7° highlighting the small Mg-associated peak shift and milling-induced broadening. (c) Representative SEM images acquired at matched magnification. (d) Representative TEM/HRTEM, SAED, and elemental-mapping results after final crystallographic re-indexing. The structural data establish a modest Mg-associated lattice perturbation and a stronger milling-induced microstructural modification while preserving the dominant spinel-derived phase.

**Finalization requirement:** collaborator must supply final Mg composition/ICP, TEM/SAED indexing, and final XPS decision before this Figure is frozen.

---

# Figure 2 — How do those perturbations change electrochemical accessibility and utilization?

**Question answered:** Which synthesis variable controls how much of the electrode can participate electrochemically?

### Panel architecture

**a. BET surface area + relative interfacial-accessibility summary**  
Left: BET surface area for the four powders.  
Right: Cdl or capacitance-derived relative accessible-interface metric from the 3.0–3.3 V scan-rate series. Avoid presenting the Cs = 40 μF cm−2 conversion as absolute ECSA in the main Figure.

Key BET values:

- HEO: 3.94 m² g−1
- BM-HEO: 18.159 m² g−1
- Mg-HEO: 6.49 m² g−1
- BM-Mg-HEO: 16.64 m² g−1

**b. First-cycle voltage profiles**  
All four samples under the standardized 10 wt% FEC electrolyte condition. Use the latest 2026-09-17 dataset. Final labels should be lithiation/delithiation rather than charge/discharge once WonATech sign convention is verified.

Latest working first-cycle values:

- HEO: 901.25 / 609.12 mAh g−1; ICE 67.59%
- BM-HEO: 1056.10 / 782.08 mAh g−1; ICE 74.05%
- Mg-HEO: 731.15 / 458.91 mAh g−1; ICE 62.77%
- BM-Mg-HEO: 944.07 / 580.83 mAh g−1; ICE 61.52%

**c. First-cycle capacity/ICE summary**  
Compact bar or point summary. This panel should make the 2 × 2 effects immediately visible: BM increases accessible capacity in both compositions; Mg lowers capacity despite not lowering BET area.

**d. Cycling performance with 10 wt% FEC**  
Show the common electrolyte condition used for the principal comparison. The main purpose is absolute capacity evolution and sustained sample ordering, not a detailed FEC mechanism.

**e. Rate capability**  
Use the latest 2026-09-17 rate dataset. BM-HEO remains above HEO across the tested rate sequence and recovers on return to 0.1 C. Do not repeat the older internal statement that ball milling necessarily worsens rate capability.

### Main message

Ball milling strongly increases surface/interfacial accessibility and accessible capacity. Mg lowers capacity even though Mg-HEO has a larger BET area than HEO. Capacity therefore cannot be explained by geometric area or one simple transport parameter alone.

### Draft caption

**Figure 2. Surface accessibility and electrochemical utilization of the four spinel HEO electrodes.** (a) BET specific surface area and relative electrochemically accessible interface obtained from the scan-rate dependence of the non-faradaic current. The capacitance-derived quantity is used only for relative comparison because the specific interfacial capacitance of the porous composite electrode is not independently known. (b) First-cycle voltage profiles and (c) corresponding first-cycle capacity and initial Coulombic efficiency under the common electrolyte condition of 1.0 M LiPF6 in EC/DEC (1:1) with 10 wt% FEC. (d) Cycling performance and (e) rate capability of HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO. Ball milling strongly increases interfacial accessibility and accessible capacity in both compositions, whereas Mg incorporation decreases capacity despite the larger BET area of Mg-HEO relative to HEO.

### SI associated with Figure 2

- full scan-rate CV series and Cdl fits;
- calculation using Cs = 40 μF cm−2, labeled as nominal/apparent ECSA only;
- no-FEC cycling controls showing stronger interphase penalty for BM-HEO;
- selected dQ/dV curves;
- post-cycle SEM images;
- cycling EIS series as qualitative/supporting data unless reproducible parameters are established.

---

# Figure 3 — Does lower polarization mean faster kinetics?

**Question answered:** Can capacity and polarization differences be explained by a simple monotonic change in Li transport?

### Panel architecture

**a. Representative GITT pulse/rest and analysis definitions**  
Show one 10 min pulse followed by 60 min rest. Mark:

- pulse end;
- early current-off fitting interval (3–30 s);
- extrapolated t → 0 current-off intercept;
- Eoff,3s;
- E60min;
- ΔErelax;
- t63.

A small inset of E versus √t with the linear 3–30 s fit is preferred.

**b. Apparent instantaneous current-off resistance vs cumulative first-lithiation capacity**  
All four samples. Include the large early BM-HEO response below 200 mAh g−1 but avoid allowing it to compress the 200–800 mAh g−1 region visually; a broken axis or small early-region inset may be useful.

Median 200–800 mAh g−1 values:

- HEO: 104.0 Ω
- BM-HEO: 102.9 Ω
- Mg-HEO: 40.2 Ω
- BM-Mg-HEO: 33.0 Ω

Initial 0–200 mAh g−1 values:

- HEO: 296 Ω
- BM-HEO: 575 Ω
- Mg-HEO: 43 Ω
- BM-Mg-HEO: 76 Ω

**c. 3 s-to-60 min relaxation amplitude vs capacity**  
All four samples. This panel should show the pronounced late-stage HEO hump and the smaller Mg response before Figure 4 isolates it quantitatively.

Median 200–800 mAh g−1 values:

- HEO: 160.9 mV
- BM-HEO: 174.1 mV
- Mg-HEO: 109.3 mV
- BM-Mg-HEO: 142.3 mV

**d. Model-free t63 vs capacity**  
All four samples, preferably on the same cumulative-capacity coordinate as panels b and c. A compact inset may summarize medians over 200–800 mAh g−1:

- HEO: 8.68 min
- BM-HEO: 11.61 min
- Mg-HEO: 11.01 min
- BM-Mg-HEO: 13.00 min

### Main message

Polarization magnitude and relaxation time are independent observables. Mg greatly lowers polarization without producing faster relaxation, while BM increases utilization despite unchanged intermediate-capacity fast resistance and a longer t63. Therefore reduced polarization cannot automatically be equated with faster Li diffusion.

### Draft caption

**Figure 3. Current interruption separates polarization magnitude from relaxation time.** (a) Representative GITT pulse and 60 min current-off response showing the operational definitions used in the analysis. The early 3–30 s rest region was represented as E = a + b√t and extrapolated to t → 0 to obtain an apparent instantaneous current-off jump; ΔErelax denotes the voltage change from 3 s to 60 min, and t63 is the model-free time required to reach 63.2% of that finite-window relaxation. (b) Apparent instantaneous current-off resistance, (c) 3 s-to-60 min relaxation amplitude, and (d) t63 as functions of cumulative first-lithiation capacity. Over 200–800 mAh g−1, HEO and BM-HEO have nearly identical apparent fast current-off resistance but BM-HEO relaxes more slowly. Mg incorporation substantially lowers the polarization amplitude while t63 remains comparable to or longer than that of HEO. Polarization magnitude and relaxation time therefore do not vary as a single kinetic quantity.

### SI associated with Figure 3

- E versus √t representative fits and R² distribution;
- t50 and t90 versus capacity;
- early √t slope;
- terminal relaxation slope;
- current-on/pulse descriptors;
- conventional apparent DGITT as a comparator, not the causal descriptor.

---

# Figure 4 — What does the experiment establish about the late-stage transition-associated response?

**Question answered:** What experimentally observed features distinguish redistribution of the transition-associated response from suppression of its extent?

### Panel architecture

**a. State-resolved late-stage relaxation**  
Plot Delta E_relax versus normalized capacity z = Q/Qmax for all four samples, focused on the late-stage region. The relaxed GITT voltage may be included only as a light secondary reference if it remains readable.

**b. Background-subtracted transition-associated excess relaxation**  
Plot eta_excess(z) for all four samples using the common declared background procedure. This panel should make the concentrated HEO peak, BM broadening/lowering, Mg suppression, and partial BM-Mg recovery visually obvious.

**c. Peak amplitude versus width map**  
Plot FWHM-like capacity width on the x-axis and excess peak amplitude on the y-axis. Marker area may encode normalized excess area. This is the compact experimental summary panel.

Do not include a mechanistic cartoon in Figure 4. The model/interpretation begins explicitly in Figure 5a.

### Working values

| Sample | Excess peak | FWHM-like width | normalized excess area |
|---|---:|---:|---:|
| HEO | 70.8 mV | 354 mAh g−1 | 22.1 mV |
| BM-HEO | 44.1 mV | 430 mAh g−1 | 14.1 mV |
| Mg-HEO | 15.9 mV | 250 mAh g−1 | 4.94 mV |
| BM-Mg-HEO | 21.1 mV | 392 mAh g−1 | 7.58 mV |

### Draft caption

**Figure 4. State-resolved current-off relaxation isolates a synthesis-dependent late-stage transition-associated polarization.** (a) Late-stage relaxation amplitude plotted against normalized first-lithiation capacity. Pristine HEO develops a concentrated high-state response in the voltage/state region associated in related spinel HEO literature with spinel-to-rock-salt/conversion evolution, whereas the feature is broadened after ball milling and strongly suppressed after Mg incorporation. (b) Background-subtracted excess polarization obtained using the same fitting windows and functional form for all four samples. Ball milling lowers the local maximum while distributing the excess response over a wider capacity interval; Mg incorporation strongly suppresses the excess response. (c) Peak-amplitude versus FWHM-like-width map, with marker area representing normalized excess area. The excess area is a comparative polarization descriptor derived from discrete GITT states and is not interpreted as dissipated energy.

### SI associated with Figure 4

- exact background definition and fitting windows;
- background-fit sensitivity;
- capacity-axis and normalized-capacity versions;
- absolute capacity-weighted excess area;
- conventional apparent DGITT overlay in the same state region;
- literature comparison table for reported spinel/rock-salt phase-evolution voltage ranges.

---

# Figure 5 — What internal-state evolution is compatible with the GITT constraints?

**Question answered:** What modeled internal-state evolution can simultaneously accommodate the observed polarization amplitude, transition width, accessible transformed state, and relaxation-time directions?

### Panel architecture

**a. Mechanism-sufficiency logic schematic**  
Experimental constraints -> independent model coordinates -> modeled radial state. Keep this broad and non-mathematical in the main Figure.

**b. Pulse-end circular radial-state array**  
Rows: HEO / BM-HEO / Mg-HEO / BM-Mg-HEO.  
Columns: model mean lithiation state c-bar ≈ 0.55, 0.62, 0.68, 0.75, 0.80, 0.86, 0.91.  
Color: phi, with 0 = parent-like/pre-transition and 1 = transformed-like.  
For BM-containing samples, show the ensemble-averaged radial state over the frozen 11-quantile distribution; do not invent angular domains.

**c. Pulse-end phi-bar versus c-bar**  
Show the mean structural-state progression for all four samples. This should visually establish earlier/broader BM progression, strong Mg suppression, and partial reopening for BM-Mg.

### Draft caption

**Figure 5. Spatial mechanism-sufficiency model visualizes distinct late-stage internal-state evolution.** (a) Experimental GITT constraints are evaluated against independent model coordinates for transport scale, transformation stabilization/extent, local-transition heterogeneity, and structural-mobility heterogeneity. (b) Pulse-end radial maps of the late-stage structural order parameter phi at selected values of the model mean lithiation state c-bar. HEO and Mg-HEO use the single frozen radial parameter set, whereas BM-HEO and BM-Mg-HEO are shown as ensemble-averaged radial states over the frozen 11-quantile distributions. phi near 0 denotes a parent-like/pre-transition state and phi near 1 a transformed-like state. (c) Pulse-end mean structural state phi-bar versus c-bar. Ball milling advances and distributes the modeled transformation over a broader reaction-progress interval, Mg strongly suppresses the late-stage transformed state, and BM-Mg-HEO partially recovers transformation while retaining Mg-related suppression. The model is used as a mechanism-sufficiency visualization and does not represent a unique parameter identification, a directly measured phase fraction, or a complete reconstruction of all structural transitions during lithiation.

### SI associated with Figure 5

- full governing equations and effective-parameter table;
- 7-versus-11-quantile convergence;
- volume- versus surface-chemical-potential readout robustness;
- directional unit-test table and sensitivity/identifiability note;
- Delta phi-bar_rest during the 60 min rest as a model-side internal-state descriptor.

---

# Main-text figure call order

## Results 3.1

Call **Figure 1** after the first paragraph defining the 2 × 2 sample matrix. Continue the structural discussion using panels 1b–d.

## Results 3.2

Call **Figure 2a** immediately after introducing the BET/interface contrast, then **Figure 2b,c** for the first-cycle comparison and **Figure 2d,e** for cycling/rate behavior.

## Results 3.3

Call **Figure 3a** when introducing the current-off analysis. Use **Figure 3b–d** in the order fast polarization → relaxation amplitude → relaxation time. This order is important because the contradiction between amplitude and time is the mechanism discriminator.

## Results 3.4–3.5

Call **Figure 4a,b** when assigning the late-stage hump to the phase-transition region. Use **Figure 4c** to compare BM and Mg quantitatively. End Figure 4 with the experimental summary map; the synthesis–electrochemistry model interpretation begins with Figure 5a.

## Results 3.6

Call **Figure 5a–c** in the spatial-modeling section. Keep the logic order model constraints -> pulse-end internal-state maps -> mean structural-state progression.

## Results 3.7–3.8

Refer back to Figures 2, 4, and 5 when discussing cycling/rate consequences and the integrated mechanism. Do not add a sixth main Figure unless new independent experimental evidence requires it.

---

# Supporting Information architecture

Recommended order:

- **Figure S1:** additional XRD/Rietveld or full structural refinement.
- **Figure S2:** additional SEM/TEM/EDS and final plane-indexing support.
- **Figure S3:** XPS after collaborator dataset is finalized.
- **Figure S4:** full N2 adsorption/desorption and BET fits.
- **Figure S5:** scan-rate CV series and Cdl extraction.
- **Figure S6:** no-FEC cycling controls.
- **Figure S7:** selected dQ/dV evolution.
- **Figure S8:** post-cycle SEM.
- **Figure S9:** representative E–√t current-off fits + fit-quality statistics.
- **Figure S10:** t50 and t90 versus capacity.
- **Figure S11:** early √t slope and terminal relaxation slope.
- **Figure S12:** conventional apparent DGITT versus capacity.
- **Figure S13:** transition-hump background/sensitivity audit.
- **Figure S14:** alternative absolute-capacity and normalized-capacity hump representations.
- **Figure S15:** cycling EIS series, retained as supporting data unless a stable parameter extraction is established.

Tables:

- **Table S1:** synthesis/ICP composition and final sample nomenclature.
- **Table S2:** electrode/cell parameters and active loading.
- **Table S3:** first-cycle capacity and ICE values from the final raw-data source.
- **Table S4:** median current-off descriptors by selected capacity interval.
- **Table S5:** peak/width/area values and sensitivity ranges.
- **Table S6:** literature comparison of spinel HEO phase-evolution pathways/voltage regions.

---

# Figure-level claim boundaries

1. Figure 1 may show Mg-associated lattice expansion/incorporation only after final ICP/structural analysis; do not claim a unique crystallographic Mg site from the small XRD shift.
2. Figure 2 Cdl-derived interface is relative, not absolute physical ECSA.
3. Figure 3 current-off intercept is an apparent fast-response resistance, not a uniquely ohmic or charge-transfer resistance.
4. Figure 3 t63 is model-free; it equals a true exponential time constant only for an ideal single exponential.
5. Figure 4 assigns the late-stage hump primarily to the spinel-to-rock-salt/conversion transition based on voltage/state dependence plus literature, but does not claim direct operando phase-fraction measurement in the present experiment.
6. Peak/width/area numbers remain working values until the common-background sensitivity audit is frozen.
7. Rate capability and long-rest relaxation time are distinct observables; do not imply that the longer BM t63 necessarily means poorer galvanostatic rate performance.
8. Figure 5 is a mechanism-sufficiency visualization. phi is not a measured phase fraction, c-bar is not directly calibrated to experimental normalized capacity, and BM circular maps are ensemble-averaged radial states rather than simulated heterogeneous 2D particles.

---

# Final visual logic

The five main Figures should read as one causal sequence:

`Figure 1: what was changed`

→ `Figure 2: how much electrochemistry became accessible`

→ `Figure 3: how polarization and relaxation changed independently`

→ `Figure 4: which part of the phase-transforming reaction BM and Mg regulate experimentally`

→ `Figure 5: what internal-state evolution is physically compatible with those constraints`

This sequence keeps GITT as a mechanistic diagnostic and keeps the spatial model as a mechanism-sufficiency visualization rather than turning the manuscript into either a conventional diffusivity paper or a parameter-fitting paper.