# HEO — START HERE / Current Project State

**Last consolidated:** 2026-09-18
**Purpose:** This is the single entry point for continuing the HEO manuscript/project in a new chat without a separate handoff message.
**Rule:** Read this file first. Then open the linked authoritative files only as needed.

---

# 1. Current manuscript identity

## Working title
**Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Phase Evolution, Polarization, and Electrochemical Utilization**

Alternative:
**Mg Incorporation and Ball Milling Regulate Phase-Transformation Polarization in Spinel High-Entropy Oxide Anodes**

## Manuscript type
Synthesis/material-centered paper with electrochemical diagnostics used to resolve the distinct roles of Mg incorporation and ball milling.

## Central mechanistic message

The 2 × 2 matrix is HEO / BM-HEO / Mg-HEO / BM-Mg-HEO.

### Ball milling
Ball milling primarily changes electrochemical accessibility and the distribution of the phase-transforming reaction.

Working interpretation:
BM -> larger accessible interface / shorter effective domain or transport length -> more heterogeneous local transition conditions and structural mobilities -> transition peak decreases and broadens -> accessible capacity increases -> long-rest ensemble relaxation can become slower.

Do not reduce the BM story to faster diffusion.

### Mg incorporation
Mg primarily changes transformation extent / structural stability.

Working interpretation:
Mg -> thermodynamic/structural stabilization of the parent/intermediate oxide-derived state + lower mobility of the residual structural transformation -> smaller conversion/transformation fraction -> lower conversion-associated capacity -> much smaller late-stage transition polarization -> relaxation does not become faster and can become slower.

Concise contrast:
- BM: accessibility/distribution increases; transformation broadens; utilization increases.
- Mg: transformation extent decreases; stabilization increases; transition polarization decreases without faster relaxation.

The three experimentally distinct coordinates are accessibility, transformation extent, and relaxation time.

---

# 2. Current authoritative manuscript and reference files

Main manuscript: manuscript/HEO_MANUSCRIPT_V1_INTEGRATED_2026-09-18.md

The earlier excess-area unit mistake has already been corrected in this integrated file. The capacity-weighted excess-polarization quantity is reported as mV·mAh g−1, not mWh g−1. It is explicitly treated as a comparative metric, not an energy quantity.

Mechanistic logic note: manuscript/HEO_DIFFUSION_VS_PHASE_TRANSITION_LOGIC_AND_SIMULATION_2026-09-18.md

Verified reference master: manuscript/HEO_REFERENCE_MASTER_VERIFIED_2026-09-18.md

Figure architecture: manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V1_2026-09-18.md

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

The more likely origin is a phase-transition/conversion-associated contribution because the feature is localized in the relevant low-voltage range, related five-cation spinel HEO literature directly reports spinel -> mixed spinel/rock-salt -> rock-salt evolution, and phase-transforming electrodes can exhibit nucleation and phase-boundary overpotential.

---

# 5. Current Mg mechanism

A pure Mg-slows-phase-boundary-mobility explanation is insufficient.

Current minimum interpretation uses two coordinates:
1. thermodynamic / structural stabilization: transformed fraction decreases, conversion capacity decreases, transition excess peak decreases;
2. slower residual structural mobility: remaining structural/phase rearrangement relaxes more slowly, so t63 does not shorten.

Thus: Mg -> stabilization increases + residual structural mobility decreases -> transformed fraction decreases + transition peak decreases + capacity decreases + relaxation slower.

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
phi is the spatial structural order parameter.
- phi ~ 0: parent-like / pre-transition state
- phi ~ 1: transformed-like state
- intermediate phi: local/coarse-grained partial transformation state

Crucial boundary: phi is a modeled internal-state variable, not a directly measured phase fraction.

The current phi represents the late-stage transition-associated transformation only. It is not a complete model of every structural transformation over the full lithiation range.

## Preferred visualization format
Current preferred main-text visualization: circular particle snapshots.

Rows:
1. HEO
2. BM-HEO
3. Mg-HEO
4. BM-Mg-HEO

Common target model states:
- 0.55
- 0.62
- 0.68
- 0.74
- 0.80
- 0.86
- 0.92

The 0.55 column was deliberately added so all four materials appear to begin from a comparable low-transformation state.

This should be presented explicitly as a late-stage transition window, not as full 0→1 lithiation history.

## Current matched-state behavior from the visual prototype

HEO: ~0.53 phi_bar 0; ~0.60 0.02; ~0.68 0.64; ~0.75 0.84; ~0.78 0.95; >=0.86 ~1.

BM-HEO: already partially transformed around ~0.57; transition develops more broadly; reaches near-complete transformation by high state.

Mg-HEO: essentially no late-stage transformation until high state; ~0.86 phi_bar ~0.06; ~0.89 ~0.13 in current visual model.

BM-Mg-HEO: transformation begins earlier than Mg-HEO, remains strongly below HEO/BM over much of the state range, and partially recovers transformation at high state.

Safe wording:
The circular snapshots visualize the modeled late-stage transition-associated state variable phi within a spherical particle across a common reaction-progress window. The visualization is intended as a mechanistic representation of the GITT-derived interpretation and should not be interpreted as a directly measured phase fraction or as a complete reconstruction of all structural transitions throughout lithiation.

Dedicated note: manuscript/HEO_VISUAL_SIMULATION_MAIN_FIGURE_DIRECTION_2026-09-18.md

---

# 10. Current figure strategy

Original structure:
- Figure 1: structural/microstructural perturbations
- Figure 2: accessibility/utilization
- Figure 3: current-off polarization vs relaxation
- Figure 4: late-stage transition polarization / peak-width mechanism

New development: visual simulation should be in the main text.

Exact numbering is not frozen. Preferred options are either a new final main figure dedicated to GITT -> modeled internal-state visualization, or selected simulation panels integrated into the final mechanistic figure if readable.

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

- Cogswell & Bazant, ACS Nano 2012, DOI 10.1021/nn204177u
- Cogswell & Bazant, Nano Letters 2013, DOI 10.1021/nl400497t
- Li et al., Angew. Chem. Int. Ed. 2025, DOI 10.1002/anie.202518569
- Komayko et al., J. Power Sources 2024, DOI 10.1016/j.jpowsour.2024.235589
- Jin et al., Materials Today Chemistry 2025, DOI 10.1016/j.mtchem.2025.102949

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

---

# 15. Immediate next actions in a new chat

Start here without asking for another handoff.

Recommended order:
1. Refine the 4 × 7 circular-particle visual simulation figure into publication style.
2. Decide whether state labels remain model mean lithiation state or are carefully mapped to normalized/experimental capacity.
3. Add the visual-simulation section and claim boundary to the integrated manuscript.
4. Update main figure architecture/numbering to include visual simulation.
5. Keep compact/detailed model parameter tables in SI.
6. If stronger model validation is desired, fit/compare representative experimental GITT voltage transients; do not automatically fit all phase-field parameters because identifiability remains a concern.
7. Later run the spatial MATLAB port locally and check directional unit tests.
8. Continue collaborator-dependent structural/method cleanup.

If raw GITT files are needed for new numerical reanalysis and are not available in the active chat/runtime, request re-upload. Current GitHub notes preserve the key raw-derived numerical outputs and logic.

---

# 16. Future research extension: sulfide systems

A future collaborative extension is planned from high-entropy oxide / oxide conversion systems to sulfide-based materials.

See: FUTURE_DIRECTION_SULFIDE_EXTENSION_2026-09-18.md

This should remain a future/collaboration direction and should not be mixed into the present oxide manuscript unless new sulfide data are generated.