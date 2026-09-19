# HEO Main–SI Scientific Consistency Audit

**Date:** 2026-09-19  
**Mode:** YL AUDIT  
**Audited files:**  
- `manuscript/HEO_MANUSCRIPT_V3_POLISHED_2026-09-19.md`  
- `manuscript/HEO_SUPPORTING_INFORMATION_V1_2026-09-19.md`  
- `manuscript/FIGURE3_RAW_REANALYSIS_NOTE_2026-09-18.md`  
- `manuscript/FIGURE4_RAW_REANALYSIS_NOTE_2026-09-18.md`  
- `modeling/HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md`  
- `START_HERE_CURRENT_STATE_2026-09-18.md`

## Audit Summary

- **MUST FIX before submission: 4**
- **WORTH FIXING before final freeze: 3**
- **OPTIONAL PRECISION / POLISH: 2**
- **Scientific storyline contradiction between current Main and SI: none identified after corrections below.**

---

# A. Issues resolved during this audit

## A1. Prior-art boundary for phase-transformation GITT — RESOLVED

A direct precedent exists for extracting phase-transformation kinetics from intermittent titration. Zhu and Wang (2010) formulated phase-transformation GITT/PITT and extracted both Li diffusivity and phase-interface mobility in the two-phase region of LiFePO4. Additional precedents exist for GITT-based phase-transformation kinetics, full pulse/rest model fitting, multi-timescale voltage relaxation, structural relaxation after current interruption, and phase-field analysis of GITT/PITT.

**Action completed:** references [21]–[29] were added to the reference master, Main, and SI. The novelty boundary was revised so the HEO manuscript does not claim the first phase-transformation GITT parameterization or first interface-mobility extraction.

**Current bounded distinction:** the present paper combines independent current-off observables, a state-localized transition-associated excess response, a 2 × 2 synthesis-variable comparison, and a non-unique spatial internal-state model. This is narrower and more defensible than a priority claim.

## A2. Model parameter-identification wording — RESOLVED

The frozen spatial model was developed through constrained directional mechanism tests, not a formal inverse fit that uniquely extracts material constants.

**Action completed:** Main Methods and SI now state explicitly that:
- no formal inverse parameter identification is claimed;
- model coordinates are effective and non-unique;
- the model is a mechanism-sufficiency/rationalization tool rather than independent validation.

This distinction is especially important because Zhu and Wang [21] provide a true phase-transformation parameter-extraction precedent.

## A3. Experimental width vs model width — RESOLVED

Experimental Figure 4 uses an **FWHM-like capacity width**. Model convergence uses a **polarization-weighted second-moment width in model state**.

**Action completed:** SI now explicitly states that the two widths are not numerically equivalent and only the directional broadening/narrowing is compared.

## A4. Experimental t63 vs model t63 — RESOLVED

Experimental median t63 values are 8.68, 11.57, 11.01, and 12.99 min, whereas the frozen directional model produces different absolute characteristic times.

**Action completed:** SI now explicitly states that model t63 values were not fit to experimental t63 values; only directional ordering is used.

## A5. Background wording — RESOLVED

Main previously used wording that could be read as one common fitted background curve. SI defines separate background fits for each sample using the same functional form and state windows.

**Action completed:** Main now states that the **same background-fitting procedure is applied independently to each sample**.

## A6. Mathematical source corruption — RESOLVED

Several LaTeX backslashes had been converted into control characters during programmatic Markdown generation.

**Action completed:** Main and SI equations were repaired and rechecked. No residual non-newline control characters remain in the current authoritative Markdown files.

---

# 1. MUST FIX

## 1.1. Freeze the final GITT analysis provenance

**Location:** Figure 3 / Main 3.3 / SI S3 / `FIGURE3_RAW_REANALYSIS_NOTE_2026-09-18.md`

**Problem:** The raw-reanalysis note explicitly states that exact manuscript values should be frozen only after the final analysis script is archived and checked against the plotted source CSVs. The Main and SI already report exact values.

**Why it matters:** The numerical values are central evidence for the amplitude–time decoupling. Submission requires a traceable chain from raw GITT data → analysis code → plotted data → manuscript numbers.

**Required action:** archive the final Figure 3 analysis script and exact plotted source tables/CSVs, rerun once, and freeze the reported medians and state windows. If the final rerun changes only rounding, update Main/SI/Figures together.

---

## 1.2. Freeze the Figure 4 background/window sensitivity audit

**Location:** Main 3.4 / SI S4 / Figure S18 / Table S5

**Problem:** Peak/width/area values currently use a defined exponential background fitted over z = 0.20–0.40 and 0.90–1.00, but the final robustness range for reasonable background/window alternatives has not yet been frozen.

**Why it matters:** “BM lower + broader” and “Mg strongly suppressed” are central mechanistic observations. They should not depend critically on one reasonable background choice.

**Required action:** complete the planned background/window sensitivity test and report the range in Figure S18/Table S5. The central trend should remain stable. If the trend is not robust, the Main claim must be narrowed.

---

## 1.3. Resolve collaborator and experimental metadata placeholders

**Location:** Main Methods 2.1–2.3; Main 3.1; Figure 1/2 captions; SI S1/S2

**Problem:** Exact Mg synthesis/composition, ICP, refined XRD, final HRTEM/SAED, XPS decision, and several electrochemical assembly/acquisition metadata remain unresolved.

**Why it matters:** These are required for reproducibility and, for Mg composition/structure, for the material identity underlying the central 2 × 2 comparison.

**Required action:** obtain and freeze:
- Mg precursor, nominal composition, substitution/addition basis, ICP composition;
- refined XRD/lattice/phase result;
- final HRTEM/SAED indexing;
- XPS only if reproducible and retained;
- current collector, drying, loading/thickness, separator, electrolyte amount, glovebox specifications;
- 1 C definition/rate sequence, potentiostat details;
- WonATech half-cycle convention.

Do not infer missing values from related papers.

---

## 1.4. Decide the status of the unverified MATLAB spatial port

**Location:** SI S7.4 / internal modeling files

**Problem:** The Python directional model is the current physics authority. The MATLAB spatial translation has not been runtime-verified in MATLAB/Octave.

**Why it matters:** An unexecuted port should not appear in a submission SI as though it independently supports the results.

**Required action:** before submission, either:
1. run the MATLAB file locally and confirm the directional unit tests; or
2. remove the MATLAB-port status statement from submission SI and keep the unverified translation as an internal development file.

The Python model itself remains usable for the manuscript because the Main/SI claims are based on the frozen Python directional result.

---

# 2. WORTH FIXING

## 2.1. Finalize citation numbering after the target journal is chosen

**Location:** Main References [1]–[29]

**Issue:** The newly added references [21]–[29] are appended by development history rather than renumbered strictly by first appearance.

**Recommended action:** let the final reference manager/journal style renumber citations automatically during submission-format preparation. Do not manually renumber repeatedly during active drafting.

---

## 2.2. Replace SI checklist placeholders with actual cross-references after Figures S1–S20 are assembled

**Location:** SI S9

**Issue:** The SI currently functions correctly as an architecture/checklist, but many Supporting Figures/Tables do not yet exist as final compiled objects.

**Recommended action:** after the data figures are assembled, convert S9 from a planning checklist into real in-text cross-references and remove any unused planned item.

---

## 2.3. Freeze the exact Figure 5 plotting source alongside the model specification

**Location:** Main Figure 5 / SI S6–S7

**Issue:** The frozen model equations/parameters are archived, but the publication Figure 5 rendering was generated during the manuscript-development session and should have an explicit reproducible plotting source/data snapshot.

**Recommended action:** archive the final plotting script and the pulse-end radial profiles/selected-state table used for Figure 5. This is not required to change the scientific interpretation, but it completes the Figure provenance chain.

---

# 3. OPTIONAL PRECISION / POLISH

## 3.1. Keep the recent relaxation literature compact in the Main

The new references [21]–[29] are scientifically useful, but the Introduction should not become a review of GITT methodology. The current Main treatment is acceptable; the detailed comparison belongs in SI S8.

## 3.2. Journal-dependent terminology normalization

After target-journal selection, standardize whether the manuscript uses:
- “phase transformation” vs “phase-transition” in compound modifiers;
- “current-off” vs “current-interruption” for specific descriptors;
- (t_{63}) typography and subscript formatting.

These are presentation issues, not current scientific inconsistencies.

---

# 4. Main–SI consistency checks passed

## Experimental protocol

Main and SI agree on:
- GITT current = 100 mA g−1;
- voltage range = 0.005–2.5 V;
- pulse = 600 s;
- rest = 3600 s;
- common current-off reference = 3 s;
- early fit window = 3–30 s.

## Current-off numerical summary

Main and SI agree, within intended rounding, on:
- HEO: Roff 106.4 Ω; ΔErelax 160.9 mV; t63 8.68 min;
- BM-HEO: 106.5 Ω; 176.3 mV; 11.57 min;
- Mg-HEO: 40.2 Ω; 109.5 mV; 11.01 min;
- BM-Mg-HEO: 33.0 Ω; 144.3 mV; 12.99 min.

## Transition-excess metrics

Main rounded values and SI full-precision values are consistent:
- HEO: 70.77 mV, 354.13 mAh g−1;
- BM-HEO: 44.07 mV, 430.17 mAh g−1;
- Mg-HEO: 15.91 mV, 250.29 mAh g−1;
- BM-Mg-HEO: 21.10 mV, 391.78 mAh g−1.

The normalized excess areas and capacity-weighted metrics are consistent with the project reanalysis note. Both Main and SI correctly state that the capacity-weighted quantity is **not dissipated energy**.

## Accessibility metrics

Main and SI agree on:
- BET = 3.94 / 18.159 / 6.49 / 16.64 m2 g−1;
- nominal relative interface metric = 4.18 / 30.17 / 6.56 / 39.68 cm2.

Both documents correctly avoid calling the latter an absolute ECSA.

## Model role

Main and SI now consistently state:
- φ is a modeled internal-state coordinate, not a measured phase fraction;
- model c-bar is not directly calibrated to experimental normalized capacity;
- BM maps are ensemble-averaged radial states, not simulated random 2D heterogeneity;
- parameters are effective/non-unique;
- the model provides mechanistic sufficiency/rationalization, not independent validation;
- model width and t63 are compared directionally, not as quantitative fits to the experimental metrics.

## Mechanistic interpretation

Main and SI consistently support:
- BM: accessibility increases; transition-associated response broadens and becomes less concentrated; long-rest ensemble relaxation may become slower.
- Mg: conversion/transformation extent is suppressed through structural stabilization; residual structural relaxation remains slow.
- A single changing diffusivity is insufficient to explain the observed amplitude–time directions.
- Diffusion is not claimed to be absent.

---

# 5. Audit limitations

The following could not be independently checked from the current repository state:

- final plotted Main Figures 1–4 against the manuscript captions;
- final collaborator-provided composition/refinement files;
- raw instrument files and final analysis script execution in the present runtime;
- final Figure 4 background-sensitivity output;
- local MATLAB execution of the spatial port;
- journal-specific reference formatting.

These limitations should be cleared during the next project freeze rather than filled by inference.

---

# Audit conclusion

After the corrections made during this audit, no unresolved **Main–SI scientific contradiction** was identified in the current storyline, definitions, numerical summaries, or model claim boundaries.

The remaining MUST-FIX items are provenance/reproducibility and missing-source-data issues rather than a need to redesign the central mechanism. The current mechanistic storyline can remain frozen unless the final Figure 4 robustness test or collaborator structural data contradict it.
