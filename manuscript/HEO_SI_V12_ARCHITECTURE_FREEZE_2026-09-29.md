# HEO SI v12 — Final Figure/Table Architecture Freeze

**Date:** 2026-09-29  
**Status:** architecture frozen before figure rebuilding and final Word assembly.  
**Main-text authority:** `manuscript/HEO_MANUSCRIPT_V16_AFM_CAPACITY_KINETICS_2026-09-28.md`

## Design rule

The Supporting Information must add controls, robustness, numerical audit, or mechanistic detail that is not already visible in the main figures. Main-text panels are not to be copied into the SI as standalone supplementary figures.

Main-text roles:
- Figure 3: accessible capacity and performance comparison.
- Figure 4: central capacity–relaxation mismatch and Dapp/direct-relaxation conflict.
- Figure 5: conversion localization of the excess current-off response.
- Figure 6: compact homogeneous four-step microkinetic result.

The SI therefore provides the underlying controls and audits rather than reproducing these panels.

# Frozen SI figure architecture

## Structural/compositional package — collaborator dependent

### Figure S1 — full XRD / refinement
Full XRD patterns, Rietveld/refinement comparison, phase fractions, refined lattice parameters, and residuals.  
**Not a repeat of main Figure 1:** main text should show only the compact structural comparison; S1 contains full patterns/refinement detail.

### Figure S2 — additional microscopy and particle/domain statistics
Additional SEM/TEM images and quantitative particle/domain-size distributions.  
**Not a repeat of main Figure 2:** main text retains representative morphology; S2 contains expanded fields/statistics.

### Figure S3 — HRTEM / SAED indexing audit
Final HRTEM lattice fringes, SAED, indexing, and spacing assignment.

### Figure S4 — EDS elemental maps
Full elemental maps for the four compositions.

### Figure S5 — XPS, only if retained
Survey/high-resolution spectra and fitting residuals. Remove the entire S5 panel if XPS is excluded from the final manuscript package.

### Figure S6 — N2 adsorption/desorption and BET fitting
Full isotherms, BET fitting intervals, and fitting quality.

## Electrochemical controls and additional performance

### Figure S7 — FEC control
Cycling with and without 10 wt% FEC.  
Purpose: electrolyte/interphase control only.

### Figure S8 — normalized rate retention and recovery
Use normalized rate retention/recovery and any additional rate-cycle detail that is not shown in main Figure 3d.  
**Do not simply repeat the main absolute rate-capability panel.**

### Figure S9 — multi-cycle voltage-profile evolution
Cycles 1–3 for all four materials, with the later-cycle information emphasized.  
Main Figure 3a remains the compact first-cycle comparison.

### Figure S10 — cycle-resolved dQ/dV
Selected/full dQ/dV evolution for all four materials beyond the compact first-cycle localization used in the main text.

### Figure S11 — relative interfacial-capacitance audit
Non-faradaic-window CVs and scan-rate regressions.  
Interpret only as a relative interfacial-accessibility metric.

### Figure S12 — post-cycle morphology
Pristine versus post-cycle SEM comparison.

### Figure S13 — full multi-cycle GITT traces
Full GITT histories for Mg-free and Mg-containing pairs.  
Main Figure 4a remains only the representative pulse/rest definition.

## GITT/current-off robustness and conventional-D audit

### Figure S14 — representative early current-off E–sqrt(t) fits
Representative short-time fits, ideally one selected state for each material or a compact four-material comparison.

### Figure S15 — t50 / t63 / t90 robustness
State-resolved t50, t63, and t90 or an equivalent normalized comparison demonstrating that the BM/HEO fast–slow ordering is not an artifact of choosing 63.2%.

### Figure S16 — descriptor-disagreement map
Dapp,BM/Dapp,HEO versus t63,HEO/t63,BM in ratio–ratio space, colored by matched capacity.  
**This replaces the old SI line plot that duplicated main Figure 4b.**

### Figure S17 — conventional-GITT voltage-term decomposition
State-matched ΔEs and ΔEτ ratios and their connection to the Dapp ratio.  
This is a mechanistic audit not shown in the main text.

## Conversion localization and history robustness

### Figure S18 — peak-localization sensitivity
dQ/dV peak voltage versus GITT excess-peak rest-end voltage with smoothing/background/window sensitivity ranges.  
Main Figure 5c shows the nominal comparison; S18 adds uncertainty/sensitivity.

### Figure S19 — background/window sensitivity
105-condition peak-amplitude and FWHM-like-width sensitivity audit.

### Figure S20 — cycle-history robustness
Cycle 1–3 evolution of excess-peak state, amplitude, t63, and the compact history-change map.  
This is the former main-text history analysis and remains SI-only.

## Four-step homogeneous microkinetic audit

### Figure S21 — full R1–R4 single-step sweeps
Two-panel detailed sweep:
(a) Qcutoff/Q0 versus individual rate scale;
(b) t63/t63,0 versus individual rate scale.
**Main Figure 6a remains the compact Q–t63 summary; S21 shows the underlying sweeps.**

### Figure S22 — fixed-R2 line cuts through the R2–R3 map
Two-panel line cuts:
(a) Qcutoff/Q0 versus R3 scale at several fixed R2 scales;
(b) t63/t63,0 versus R3 scale at the same fixed R2 values.
**Main Figure 6b remains the 2D map; S22 shows how the finite Q-up/t63-up region is generated.**

### Figure S23 — eigenmode spectrum and partial-rate diagnostics
(a) finite current-off eigen-timescales for the reference and representative step-selective case;
(b) r1–r4 at pulse end and early current-off state.
**Main Figure 6d remains the compact voltage-relaxation comparison; S23 contains the internal diagnostic quantities.**

## Deliberately omitted as figures

- No SI copy of main Figure 6c observable-space map.
- No bar-chart restatement of the BM/Mg experimental ratios. The experimental-versus-closest-model magnitude comparison belongs in a table.
- No SI copy of main Figure 4b line plot.
- No duplicate nominal Figure 5c peak-position scatter without uncertainty.
- No heterogeneous-population model figure.

# Frozen SI table architecture

### Table S1 — final composition and structural refinement
Nominal composition, final ICP-OES composition, refined lattice parameters, phase assignment/fractions, and refinement statistics.

### Table S2 — XPS fit parameters, only if XPS is retained
Binding energies, assignments, fit constraints, and relative areas. Remove if XPS is excluded.

### Table S3 — BET / particle-size metrics
BET surface area, pore/particle/domain metrics used in the structural interpretation.

### Table S4 — relative interfacial-capacitance regression
Fitted slopes, R2 values, and the nominal area-conversion sensitivity.

### Table S5 — current-off descriptor summary
Roff,app and ΔErelax together with t50/t63/t90 summaries over the common state interval.

### Table S6 — full 37-state HEO/BM GITT audit
Matched capacity, Dapp ratio, direct relaxation-rate ratio, ΔEs ratio, and ΔEτ ratio.

### Table S7 — compact conventional-GITT audit statistics
Medians, directional counts, and key voltage-term statistics.

### Table S8 — peak-voltage localization and sensitivity
Nominal dQ/dV/GITT peak voltages and tested ranges.

### Table S9 — 105-condition background/window sensitivity
Amplitude/width ranges, directional pass counts, and peak-location range.

### Table S10 — cycle-history descriptors
Cycle-resolved amplitude, t63, peak state, and capacity descriptors.

### Table S11 — later-cycle background-form sensitivity
Exponential versus linear background comparison for cycles 2–3.

### Table S12 — four-step model parameters
Reference kinetic/equilibrium parameters and simulation protocol.

### Table S13 — single-step limiting audit
Selected numerical values from the R1–R4 rate sweeps.

### Table S14 — R2–R3 regime / line-cut audit
Selected line-cut points, finite Q-up/t63-up window, and grid statistics.

### Table S15 — experimental magnitude boundary
Experimental BM-HEO/HEO and Mg-HEO/HEO Q and t63 ratios versus closest sampled model points.  
Use only to define the model boundary; do not assign microscopic R2/R3 values to BM or Mg.

### Table S16 — current-off eigenmodes
Finite eigenvalues/eigen-timescales for the reference and representative step-selective case.

### Table S17 — partial rates
r1–r4 at pulse end and selected early current-off times for the same two cases.

# Numbering / assembly rule

1. Figure numbers S1–S23 and Table numbers S1–S17 above are frozen for the next build.
2. If XPS is excluded, retain the numbering gap as “Figure S5 not used” only during internal drafting; before submission renumber once, globally.
3. Do not build the final Word until Figures S15, S16, S21, S22, and S23 have been visually compared against main Figures 4–6 for non-redundancy.
4. Structural Figures S1–S6 may remain placeholders during the electrochemical/mechanistic build, but the final submitted SI cannot contain empty placeholders.
5. The former v11 SI Word is a working archive only and is not the current layout authority.

# Next build steps

- Step 2A: generate/verify Figures S15–S17 (GITT robustness) using raw/verified derived data.
- Step 2B: generate/verify Figures S18–S20 (localization/history robustness).
- Step 2C: generate/verify Figures S21–S23 (microkinetic detailed audit).
- Step 3: assemble v12 Word only after the above figures and captions are approved.
