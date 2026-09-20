# HEO — START HERE / Current Project State

**Last consolidated:** 2026-09-20
**Purpose:** This is the single entry point for continuing the HEO manuscript/project in a new chat without a separate handoff message.
**Rule:** Read this file first. Then open the linked authoritative files only as needed.

---

# 1. Current manuscript identity

## Working title
**Mg Incorporation and Ball Milling Independently Regulate Electrochemical Accessibility and Conversion in Spinel High-Entropy Oxide Anodes**

AFM target selected for the current drafting cycle. Keep the pitch materials-centered: two common HEO modifications alter lithium storage through different physical routes.

## Target journal

**Advanced Functional Materials (AFM)** is the current first target. Position the paper as a functional-materials/mechanism study: composition/process → accessibility and conversion → electrochemical function. Do not pitch a new GITT analysis method.

## Manuscript type
Synthesis/material-centered paper with electrochemical diagnostics used to resolve the distinct roles of Mg incorporation and ball milling.

## Manuscript identity boundary

**This is an HEO materials/mechanism paper, not a GITT-method paper.**

The GITT/current-off/relaxation literature is cited only to establish that:
- transient components and relaxation times can legitimately be analyzed separately;
- phase-transforming GITT can contain interface/structural kinetic information;
- phase-field descriptions are established tools for phase-evolving electrochemical systems.

Do not make method novelty the central contribution. Do not organize the Introduction around GITT history. The manuscript contribution is the **contrasting effect of ball milling and Mg incorporation on accessibility, conversion extent/distribution, and relaxation in the same HEO system**.

## Central mechanistic message

The 2 × 2 matrix is HEO / BM-HEO / Mg-HEO / BM-Mg-HEO.

### Ball milling
Ball milling primarily changes electrochemical accessibility and the distribution of the conversion-associated reaction.

Working interpretation:
BM -> larger accessible interface / shorter effective domain or transport length -> more heterogeneous local conversion conditions and structural mobilities -> conversion-associated peak decreases and broadens -> accessible capacity increases -> long-rest ensemble relaxation can become slower.

Do not reduce the BM story to faster diffusion.

### Mg incorporation
Mg primarily changes conversion extent / structural stability.

Working interpretation:
Mg -> stabilization of the oxide-derived parent/intermediate state + lower mobility of the residual structural rearrangement -> conversion shifts to lower potential + accessible conversion fraction decreases -> conversion-associated excess polarization strongly decreases -> relaxation does not become faster and can become slower.

Concise contrast:
- BM: accessibility/distribution increases; conversion broadens; utilization increases.
- Mg: conversion shifts to lower potential and its extent decreases; stabilization increases; excess polarization decreases without faster relaxation.

The three experimentally distinct coordinates are accessibility, conversion extent/distribution, and relaxation time.

---

# 2. Current authoritative manuscript and reference files

Main manuscript (current authoritative draft): manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md

Supporting Information (current authoritative draft): manuscript/HEO_SUPPORTING_INFORMATION_V2_CONVERSION_ALIGNED_2026-09-20.md

Manuscript architecture/literature positioning note: manuscript/HEO_MANUSCRIPT_ARCHITECTURE_AND_LITERATURE_POSITIONING_V2_2026-09-20.md

Current consolidation/scientific audit: manuscript/HEO_CONSOLIDATION_AUDIT_2026-09-20.md

Previous drafts retained for history:
- manuscript/HEO_MANUSCRIPT_V2_FIGURE_ALIGNED_2026-09-19.md
- manuscript/HEO_MANUSCRIPT_V1_INTEGRATED_2026-09-18.md

The earlier excess-area unit mistake has already been corrected in this integrated file. The capacity-weighted excess-polarization quantity is reported as mV·mAh g−1, not mWh g−1. It is explicitly treated as a comparative metric, not an energy quantity.

Mechanistic logic note: manuscript/HEO_DIFFUSION_VS_PHASE_TRANSITION_LOGIC_AND_SIMULATION_2026-09-18.md

Verified reference master: manuscript/HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md

Figure architecture: manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md

The visual-simulation direction described later in this START HERE file is newer than the original four-figure architecture and should be treated as a current extension/override.

Raw-derived electrochemical reanalysis:
- manuscript/FIGURE3_RAW_REANALYSIS_NOTE_2026-09-18.md
- manuscript/FIGURE4_RAW_REANALYSIS_NOTE_2026-09-18.md

---

# 3. Key experimental / raw-derived numbers

## GITT protocol
- current: 100 mA g−1
- voltage window: 0.005–2.5 V
- pulse: 10 min = 600 s
- rest: 60 min = 3600 s
- common current-off reference: 3 s
- early current-off fit: 3–30 s, E = a + b sqrt(t)
- t50/t63/t90 are finite-window model-free descriptors.

## Current-off summary, approximately 200–800 mAh g−1

| Sample | apparent current-off R (Ω) | ΔErelax (mV) | t63 (min) |
|---|---:|---:|---:|
| HEO | ~106 | 160.9 | 8.68 |
| BM-HEO | ~106 | 176.3 | 11.57 |
| Mg-HEO | 40.2 | 109.5 | 11.01 |
| BM-Mg-HEO | 33.0 | 144.3 | 12.99 |

Interpretation:
- Mg strongly decreases polarization amplitude but does not shorten relaxation.
- BM has almost unchanged intermediate-capacity fast current-off resistance relative to HEO but a longer long-rest relaxation.

## Late-stage excess transition feature

| Sample | peak excess polarization | FWHM-like width | normalized excess area |
|---|---:|---:|---:|
| HEO | 70.8 mV | 354 mAh g−1 | 22.1 mV |
| BM-HEO | 44.1 mV | 430 mAh g−1 | 14.1 mV |
| Mg-HEO | 15.9 mV | 250 mAh g−1 | 4.94 mV |
| BM-Mg-HEO | 21.1 mV | 392 mAh g−1 | 7.58 mV |

Absolute capacity-weighted excess metric:
- HEO ~2.39 × 10^4 mV·mAh g−1
- BM-HEO ~1.79 × 10^4
- Mg-HEO ~3.96 × 10^3
- BM-Mg-HEO ~7.08 × 10^3

This is not dissipated energy.

---

# 4. Key diagnostic logic: why the late-stage feature is not explained by one D

If a single diffusion coefficient were the dominant changing variable under otherwise comparable pulse conditions, a lower D would be expected to produce larger diffusion-associated concentration polarization and slower relaxation, with tau_D scaling approximately as L^2/D.

Experimentally, Mg does the opposite: polarization amplitude strongly decreases, the late-stage excess peak strongly decreases, and t63/t90 do not decrease.

Therefore do not claim diffusion is absent. Claim instead that a simple single-diffusivity explanation cannot account for the synthesis dependence of the late-stage response.

The stronger current assignment is a conversion/transformation-associated contribution because the GITT excess peak coincides with the first-cycle cathodic dQ/dV feature within 32 mV across all four samples. Related five-cation spinel HEO literature also reports reconstructive low-voltage conversion chemistry and spinel -> mixed spinel/rock-salt -> rock-salt evolution. This supports conversion-associated interpretation without assigning the signal to one unique microscopic conversion step.

---

# 5. Current Mg mechanism

A pure Mg-slows-phase-boundary-mobility explanation is insufficient.

Current minimum interpretation uses two coordinates:
1. thermodynamic / structural stabilization of the oxide-derived parent/intermediate state: accessible conversion fraction decreases, conversion capacity decreases, and the conversion-associated excess peak decreases/shifts to lower potential;
2. slower residual structural mobility: remaining conversion-associated structural rearrangement relaxes more slowly, so t63 does not shorten.

Thus: Mg -> stabilization increases + residual structural mobility decreases -> conversion extent decreases + conversion feature shifts lower in potential + excess peak decreases + capacity decreases + relaxation remains slow.

---

# 6. Current BM mechanism

The initial intuition that nanosizing must increase phase-transition overpotential was rejected as a general rule.

Current evidence in the present sample is BET increase, XRD broadening, similar BSE aggregate scale, and increased capacity/accessibility. Do not claim 15 nm nanoparticles.

Simulation development showed:
- shorter effective scale / easier local transformation alone can lower the peak;
- experimental-like peak decrease + broadening requires heterogeneous local transition conditions;
- robust peak decrease + width increase + slower ensemble t63 requires heterogeneity in both transition conditions and structural mobility.

Current qualitative BM model:
BM -> shorter effective scale / more interface + heterogeneous local surface/defect/strain conditions + heterogeneous structural mobilities -> lower concentrated peak + broader state interval + higher accessible transformation fraction/capacity + slower ensemble long-rest relaxation.

---

# 7. Modeling status and authority order

Authoritative current model: Python spatial phase-field physics frozen for directional mechanism testing, not parameter identification.

Read:
- modeling/HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md
- modeling/HEO_MODELING_DEVELOPMENT_LOG_2026-09-18.md
- modeling/heo_spatial_phase_field_frozen_v4.py

MATLAB spatial translation: modeling/HEO_Spatial_PhaseField_Model_Final.m

Current environment did not runtime-verify MATLAB/Octave. First local MATLAB run must pass directional unit tests.

Legacy/provisional phenomenological model: modeling/HEO_PhaseTransition_Model_Final.m

All present parameters are effective, non-unique, hypothesis-level descriptors. Excellent fit does not imply unique physics.

---

# 8. Parameter table placement decision

Parameter tables are not the main originality.

Reason: observe GITT shape -> hypothesize mechanism -> choose model -> fit/extract values can become circular if the extracted values are presented as the main evidence.

Decision:
- detailed parameter table -> Supporting Information
- compact effective-parameter summary -> optional, likely SI
- visual simulation -> main-text candidate

Current effective descriptors: D_eff/R^2, M_phi, stabilization energy G_Mg/DeltaG_stab, heterogeneity width.

---

# 9. Visual simulation — current main-text direction

This is the newest manuscript-development direction and should be prioritized.

## Meaning of phi
phi is the effective conversion-associated structural-state coordinate.
- phi ~ 0: oxide-derived parent/intermediate-like state
- larger phi: progression toward a more deeply converted-like state
- intermediate phi: local/coarse-grained partial conversion-associated structural evolution

Crucial boundary: phi is a modeled internal-state variable, not a directly measured rock-salt, metallic-product, or Li2O phase fraction.

The current phi represents only the late-stage conversion-associated structural evolution. It is not a stoichiometrically complete model of the full conversion reaction or of every earlier structural change during lithiation.

## Preferred visualization format
Current preferred main-text visualization: circular particle snapshots.

Rows:
1. HEO
2. BM-HEO
3. Mg-HEO
4. BM-Mg-HEO

Recommended displayed frozen-v4 model states:
- 0.55
- 0.62
- 0.68
- 0.75
- 0.80
- 0.86
- 0.91

The 0.55 column is retained so all four materials begin from a comparable low-transformation state. The final displayed states are aligned to the frozen-v4 GITT state grid rather than the earlier prototype table.

This should be presented explicitly as a late-stage transition window, not as full 0→1 lithiation history.

## Current matched-state behavior from the visual prototype

Final Figure-5 construction now uses pulse-end radial phi(r), sampled at the end of each 600 s pulse immediately before current interruption. Approximate pulse-end phi-bar values over the displayed states are:
- HEO: 0.00, 0.04, 0.63, 0.79, 0.94, ~1, ~1;
- BM-HEO: 0.04, 0.48, 0.64, 0.80, 0.94, ~1, ~1;
- Mg-HEO: 0, 0, 0, 0, ~0, 0.05, 0.15;
- BM-Mg-HEO: 0, 0, 0.002, 0.03, 0.21, 0.63, 0.78.

Main Figure 5c should show pulse-end mean structural state phi-bar versus model mean lithiation state c-bar. The additional Delta phi-bar_rest during the subsequent 60 min rest is retained in SI as a model-side dynamics check, not as a numerical substitute for Delta E_relax.

Safe wording:
The circular snapshots visualize the modeled late-stage transition-associated state variable phi within a spherical particle across a common reaction-progress window. The visualization is intended as a mechanistic representation of the GITT-derived interpretation and should not be interpreted as a directly measured phase fraction or as a complete reconstruction of all structural transitions throughout lithiation.

Dedicated note: manuscript/HEO_VISUAL_SIMULATION_MAIN_FIGURE_DIRECTION_2026-09-18.md

---

# 10. Current figure strategy

Original structure:
- Figure 1: structural/microstructural perturbations
- Figure 2: accessibility/utilization
- Figure 3: current-off polarization vs relaxation
- Figure 4: experimental late-stage transition polarization / peak-width-area map

New development: visual simulation should be in the main text.

Current preferred numbering is to retain Figure 4 as the experimental transition-polarization figure and add Figure 5 as an independent model-visualization figure. Figure 4 is intentionally experimental-only (raw late-stage relaxation -> background-subtracted excess -> peak/width/area summary map); the mechanistic/model schematic begins in Figure 5a. This keeps model interpretation visually separate from the experimental evidence.

Do not bury the visual simulation entirely in SI if it becomes the primary methodological originality. Parameter tables and most sensitivity details should remain SI.

---

# 11. Current experimental-performance numbers

BET:
- HEO 3.94 m² g−1
- BM-HEO 18.159
- Mg-HEO 6.49
- BM-Mg-HEO 16.64

Nominal Cdl/Cs=40 µF cm−2 apparent interface metric:
- HEO 4.18 cm²
- BM-HEO 30.17
- Mg-HEO 6.56
- BM-Mg-HEO 39.68

Do not treat this as absolute ECSA in the main text.

Latest first-cycle values:
- HEO: 901.25 / 609.12 mAh g−1; ICE 67.59%
- BM-HEO: 1056.10 / 782.08; ICE 74.05%
- Mg-HEO: 731.15 / 458.91; ICE 62.77%
- BM-Mg-HEO: 944.07 / 580.83; ICE 61.52%

WonATech charge/discharge labels must still be verified before assigning lithiation/delithiation wording.

Cycling/rate message:
- with 10 wt% FEC, BM-HEO maintains higher absolute capacity than HEO;
- BM-HEO also has higher rate capacity despite longer t63;
- therefore practical rate utilization and long-rest relaxation are distinct observables;
- no-FEC BM shows stronger degradation, consistent with increased interphase burden from larger accessible interface.

---

# 12. Structural / methods items still unresolved

Collaborator-dependent:
- exact Mg synthesis recipe
- final nominal and ICP composition
- final XRD refinement / lattice parameters
- HRTEM/SAED re-indexing
- final XPS decision, especially anomalous Cr6+ feature

Important: preliminary CoGa2O4 HRTEM label is chemically impossible for the Ga-free synthesis and must not appear.

Electrochemistry metadata still to confirm:
- current collector
- vacuum drying conditions
- active loading
- final electrode thickness
- separator model
- electrolyte volume
- glovebox specifications
- exact 1C definition and rate sequence
- potentiostat/model details
- WonATech half-cycle label convention

---

# 13. Literature anchors added for the current mechanism

Material/phase-transition anchors:
- Cogswell & Bazant, ACS Nano 2012, DOI 10.1021/nn204177u
- Cogswell & Bazant, Nano Letters 2013, DOI 10.1021/nl400497t
- Li et al., Angew. Chem. Int. Ed. 2025, DOI 10.1002/anie.202518569
- Komayko et al., J. Power Sources 2024, DOI 10.1016/j.jpowsour.2024.235589
- Jin et al., Materials Today Chemistry 2025, DOI 10.1016/j.mtchem.2025.102949

GITT/relaxation/phase-field precedents added 2026-09-19:
- Zhu & Wang, J. Phys. Chem. C 2010, DOI 10.1021/jp9113333 — phase-transformation GITT; diffusivity + interface mobility.
- Chen et al., Electrochim. Acta 2017, DOI 10.1016/j.electacta.2017.04.137 — GITT phase-transformation kinetics.
- Heubner et al., J. Electroanal. Chem. 2016, DOI 10.1016/j.jelechem.2016.02.013 — StairCase-GITT kinetic separation.
- Horner et al., ACS Appl. Energy Mater. 2021, DOI 10.1021/acsaem.1c02218 — full pulse/rest direct model fitting.
- Fath et al., J. Power Sources 2024, DOI 10.1016/j.jpowsour.2024.234100 — particle-distribution effects on rest-phase relaxation.
- Skurtveit et al., ACS Mater. Lett. 2025, DOI 10.1021/acsmaterialslett.4c02058 — direct structural relaxation after interruption.
- Han et al., Electrochim. Acta 2004, DOI 10.1016/j.electacta.2004.05.024 — phase-field impact on GITT/PITT interpretation.
- Singh et al., Electrochim. Acta 2008, DOI 10.1016/j.electacta.2008.03.083 — phase-transformation dynamics.
- Jorkesh et al., J. Power Sources 2026, DOI 10.1016/j.jpowsour.2026.240338 — fast/slow time-domain voltage relaxation.

Methodological boundary: do not claim first phase-transition parameter extraction from GITT. References on GITT decomposition, phase-transition kinetics, and phase-field modeling are supporting precedents only. The manuscript must remain centered on the HEO 2 × 2 synthesis comparison and its mechanistic interpretation.

Use the reference master for exact claim boundaries.

---

# 14. Revision history / decisions that must not be reversed accidentally

1. Correct GITT rest is 60 min, not 60 s.
2. Old interpretation 'slower relaxation means worse rate' was rejected; BM has better rate utilization despite longer t63.
3. Apparent current-off resistance is a descriptor, not uniquely ohmic resistance.
4. Do not center the paper on a conventional apparent GITT diffusivity.
5. Do not treat phi as direct measured phase fraction.
6. Do not interpret excess-polarization area as energy.
7. Do not claim Mg is simply a diffusion accelerator.
8. Do not claim BM simply makes transport faster.
9. Mg stabilization-only and mobility-only are each incomplete; current minimum mechanism uses both.
10. BM transition-condition heterogeneity alone was insufficient to robustly reproduce slower t63; structural-mobility heterogeneity was also required.
11. Spatial model is a mechanism-sufficiency model; parameters are non-unique.
12. Main-text value of modeling is GITT -> visual internal-state simulation; parameter details belong mainly in SI.
13. Current visual-simulation window begins around model state 0.55 to avoid implying that the single-phi model captures all earlier structural transitions.
14. Preferred visual layout is 4 sample rows × 7 common-state circular-particle snapshots.
15. Main Figure 5c uses pulse-end mean structural state phi-bar versus c-bar; the 60 min Delta phi-bar_rest curve is supporting information rather than the primary main-text model panel.

---

# 15. Immediate next actions in a new chat

Start here without asking for another handoff.

Recommended order:
1. Read the current authoritative main manuscript, aligned SI draft, and consolidation audit:
   - manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md
   - manuscript/HEO_SUPPORTING_INFORMATION_V2_CONVERSION_ALIGNED_2026-09-20.md
   - manuscript/HEO_CONSOLIDATION_AUDIT_2026-09-20.md
   Results follow Figures 1–5 directly: structure → accessibility/utilization → current-off decoupling → experimental conversion-associated response → modeled conversion-associated internal-state evolution.
2. Use the current Figure 5 architecture: compact mechanism-sufficiency schematic + 4 × 7 pulse-end circular state array + pulse-end phi-bar versus model mean lithiation state. Keep Delta phi-bar_rest in SI.
3. Retain the column coordinate as model mean lithiation state c-bar; do not relabel it directly as experimental normalized capacity without a validated mapping.
4. For BM-containing samples, depict ensemble-averaged radial phi states or representative quantiles; do not imply a directly simulated heterogeneous 2D single particle.
5. Complete missing collaborator/student methods and structural metadata in V2; do not reopen the Figure 1–5 story unless new data require it.
6. Keep compact/detailed model parameter tables in SI.
7. If stronger model validation is desired, fit/compare representative experimental GITT voltage transients; do not automatically fit all phase-field parameters because identifiability remains a concern.
8. Later run the spatial MATLAB port locally and check directional unit tests.
9. Continue collaborator-dependent structural/method cleanup.

If raw GITT files are needed for new numerical reanalysis and are not available in the active chat/runtime, request re-upload. Current GitHub notes preserve the key raw-derived numerical outputs and logic.

---

# 16. Future research extension: sulfide systems

A future collaborative extension is planned from high-entropy oxide / oxide conversion systems to sulfide-based materials.

See: FUTURE_DIRECTION_SULFIDE_EXTENSION_2026-09-18.md

This should remain a future/collaboration direction and should not be mixed into the present oxide manuscript unless new sulfide data are generated.

## 2026-09-20 conversion assignment / Figure 4–5 cross-check

The earlier direct digitization of already-plotted dQ/dV curves was superseded by reconstruction of the latest vector first-cycle voltage profiles from the 2026-09-17 progress presentation.

Current authoritative peak values are given in the next subsection and in `FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md`.

Frozen-v4 model was rerun without refitting:
- model relaxation peak cbar: BM 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100;
- pulse-end phibar onset gives the same ordering over thresholds 0.02–0.10.

Current interpretation:
- Figure 4 feature is **conversion/transformation-associated**;
- Figure 5 is a **reduced spatial model of conversion-associated state evolution**;
- phi is an effective conversion-associated internal-state coordinate, not a measured phase fraction;
- do not map model cbar directly to experimental Q/Qmax or voltage.


# 2026-09-20 Figure 4 conversion assignment — latest profile reconstruction

The latest first-cycle voltage profiles in the 2026-09-17 progress presentation were reconstructed from vector graphics and differentiated with a common smoothing procedure.

| Sample | first-cycle cathodic dQ/dV peak | GITT excess peak |
|---|---:|---:|
| HEO | 0.545 V | 0.527 V |
| BM-HEO | 0.589 V | 0.618 V |
| Mg-HEO | 0.419 V | 0.387 V |
| BM-Mg-HEO | 0.485 V | 0.503 V |

All four peak pairs agree within 32 mV. This supersedes the earlier preliminary digitization of already-plotted dQ/dV curves.

Current interpretation:
- the Figure 4 excess response is **conversion/transformation-associated**;
- it should not be assigned solely to spinel→rock-salt;
- same-family literature shows low-voltage conversion chemistry, including Mn nanocrystal formation around 0.5 V and deeper metallic conversion;
- BM redistributes accessible conversion over a broader state interval;
- Mg suppresses and shifts deeper conversion to lower potential;
- BM-Mg partially reopens the Mg-suppressed pathway.

Data-source boundary:
the latest numerical continuous-GCD source files are not currently available. Present dQ/dV values are reconstructed from the user's own vector voltage-profile plots. Replace with original numerical profiles if recovered before submission.

Detailed note: FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md
Archived peak table: manuscript/HEO_FIGURE4_LATEST_PPT_DQDV_GITT_PEAK_CHECK_2026-09-20.csv

# 2026-09-20 Figure 5 interpretation update

The frozen v4 model remains compatible with the conversion assignment without refitting.

Model relaxation-peak state:
BM 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100.

Use:
- phi = effective conversion-associated structural-state coordinate;
- G_Mg = stabilization of the unconverted oxide-derived parent/intermediate state;
- M_phi = effective mobility of conversion-associated structural rearrangement;
- BM ensemble = distribution of local conversion conditions and structural mobilities.

Do not claim the reduced model explicitly resolves Li2O formation, metal-nanoparticle nucleation, sequential cation reduction, or oxygen migration.

## 2026-09-20 latest first-cycle conversion validation — authoritative

The latest continuous first-cycle Excel export is not available. The older first-cycle dataset is excluded because a power interruption produced an obvious profile artifact.

Current preferred source: Park Seong Hyeon's `HEO 진행상황 (20260917).pptx`, slide 10. The latest first-cycle voltage profiles were embedded as Origin vector artwork and reconstructed at high resolution.

Reconstructed terminal first-cycle capacities reproduce the printed values to within ~0.03%:
- HEO 901.14 mAh g-1;
- BM-HEO 1055.84;
- Mg-HEO 731.05;
- BM-Mg-HEO 943.87.

Common profile-derived cathodic dQ/dV peaks versus GITT excess peaks:

| Sample | dQ/dV peak (V) | GITT excess peak (V) | absolute mismatch |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | 18 mV |
| BM-HEO | 0.589 | 0.618 | 29 mV |
| Mg-HEO | 0.419 | 0.387 | 32 mV |
| BM-Mg-HEO | 0.485 | 0.503 | 18 mV |

Smoothing sensitivity over 20-60 mAh g-1 keeps the same peak locations within narrow ranges. This **supersedes the earlier direct digitization of plotted dQ/dV curves**.

Interpretation lock:
- call the Figure 4 feature **conversion-associated excess relaxation** or, when broader wording is useful, **conversion/transformation-associated excess relaxation**;
- the voltage correspondence localizes the response to the conversion-electrochemistry window but does not identify one unique microscopic conversion step;
- do not claim direct measurement of metal/Li2O phase fraction.

Figure 5 lock after the reassignment:
- no parameter refitting was required;
- model relaxation-peak c-bar ordering is BM 0.5860 < HEO 0.6184 < BM-Mg 0.7966 < Mg 0.9100;
- pulse-end mean-phi onset thresholds 0.02-0.10 give the same earlier-to-later ordering;
- describe phi as an **effective conversion-associated structural-state variable**;
- do not map model c-bar numerically to experimental Q/Qmax or voltage.

Preferred Figure 4 main-text layout now centers the dQ/dV-GITT voltage correspondence and peak-width-area map. Raw state-resolved/background-subtraction details move to SI.

Submission-source boundary: regenerate dQ/dV from the original Origin/source numerical profile if recovered before submission. The current vector reconstruction is the preferred manuscript-development source and the old power-interrupted profile must not be substituted.

Detailed note: `FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md`.
