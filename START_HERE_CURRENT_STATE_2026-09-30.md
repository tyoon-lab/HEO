# HEO — Current State, 2026-09-30

## Read this first

This is the authoritative restart point for the HEO manuscript. A new session should be able to resume from the repository without a separate handoff.

## Paper identity

Working title:

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Working target: **Advanced Functional Materials (AFM)**.

The paper is a materials/conversion-mechanism paper using GITT relaxation as the diagnostic. It is not framed as a general GITT-method paper.

## Current authority order

1. Main manuscript: `manuscript/HEO_MANUSCRIPT_V16_AFM_CAPACITY_KINETICS_2026-09-28.md`
2. Main reference audit: `manuscript/HEO_REFERENCE_AUDIT_MAIN_V16_2026-09-28.md`
3. SI architecture freeze: `manuscript/HEO_SI_V12_ARCHITECTURE_FREEZE_2026-09-29.md`
4. SI final assembly note: `manuscript/HEO_SI_V13_WORD_ASSEMBLY_2026-09-29.md`
5. SI electrochemical redundancy audit: `manuscript/HEO_SI_V12_S7_S14_REDUNDANCY_AUDIT_2026-09-29.md`
6. SI Step 2A GITT robustness: `manuscript/HEO_SI_V12_STEP2A_GITT_ROBUSTNESS_2026-09-29.md`
7. SI Step 2B localization/history: `manuscript/HEO_SI_V12_STEP2B_LOCALIZATION_HISTORY_2026-09-29.md`
8. SI Step 2C microkinetic audit: `manuscript/HEO_SI_V12_STEP2C_MICROKINETIC_AUDIT_2026-09-29.md`
9. Four-step model authority: `modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`
10. Conventional-GITT audit: `modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`

Word files are exports and do not override the Markdown/data authority.

## Current scientific backbone

### Figure 3 — accessible capacity only

- first-cycle voltage profiles;
- lithiation/delithiation capacity + ICE;
- 0.1 C cycling;
- absolute rate capability and 0.1 C recovery.

Core first-cycle capacities:
- HEO: 901.25 / 609.12 mAh g^-1
- BM-HEO: 1056.10 / 782.08
- Mg-HEO: 731.15 / 458.91
- BM-Mg-HEO: 944.07 / 580.83

Interpretation:
- BM increases accessible capacity.
- Mg decreases accessible capacity.
- Figure 3 does not assign intrinsic conversion speed.

### Figure 4 — decisive capacity–relaxation mismatch

Median 200–800 mAh g^-1 values:

| Sample | Delta E_relax (mV) | t63 (min) | first-cycle delithiation capacity (mAh g^-1) |
|---|---:|---:|---:|
| HEO | 160.9 | 8.68 | 609.12 |
| BM-HEO | 176.3 | 11.57 | 782.08 |
| Mg-HEO | 109.5 | 11.01 | 458.91 |
| BM-Mg-HEO | 144.3 | 12.99 | 580.83 |

Primary contradiction:
**HEO -> BM-HEO gives capacity up while t63 also increases, i.e. higher accessible conversion with slower relaxation.**

Mg is complementary, not the same contradiction:
- capacity decreases;
- t63 increases;
- Delta E_relax decreases.

State-matched HEO/BM conventional-GITT audit:
- median Dapp,BM/Dapp,HEO = 1.7817;
- ratio > 1 at 37/37 states;
- median t63,HEO/t63,BM = 0.7622;
- direct rate ratio < 1 at 35/37 states.

### Figure 5 — conversion localization

The first-cycle GITT excess-relaxation peak is localized to the same voltage region as the independently reconstructed cathodic dQ/dV peak.

Nominal dQ/dV / GITT rest-end peak pairs:
- HEO: 0.5446 / 0.5275 V
- BM-HEO: 0.5891 / 0.6175 V
- Mg-HEO: 0.4188 / 0.3870 V
- BM-Mg-HEO: 0.4848 / 0.5029 V

All nominal offsets are within about 32 mV.

Important boundary:
- HEO, BM-HEO, and Mg-HEO peak localization is comparatively stable.
- the shallow BM-Mg-HEO GITT peak location is background/window sensitive (0.453–0.618 V).
- use **conversion-associated relaxation**, not a unique microscopic step assignment.

### Figure 6 — homogeneous four-step microkinetic feasibility

Current effective sequence:

[
O \rightleftharpoons I \rightleftharpoons J \rightleftharpoons K \rightleftharpoons C
]

Interpretation:
- R1: initial electrochemical lithiation/electron transfer
- R2: effective M–O dissociation/local reconstruction
- R3: effective Li2O-forming/product-side reconstruction
- R4: subsequent electron transfer/metal reduction

This is a literature-grounded four-effective-step sequence, not a claim that HEO elementary intermediates were identified.

Single-step audit:
- slowing R2 or R3 alone gives the conventional response: capacity down, t63 up;
- R1 and R4 are much weaker under the representative parameter set.

Two-dimensional R2–R3 audit:
- 28/396 sampled points satisfy Q/Q0 > 1 and t63/t0 > 1;
- therefore higher cutoff capacity and slower relaxation are physically accessible within a homogeneous multistep network.

Representative main-Figure-6d case:
- R2 x 0.465, R3 x 50
- Q ratio about 1.111
- t63 ratio about 1.087
- slowest finite eigenmode 15.35 -> 17.68 min

The minimal fixed-thermodynamics R2/R3 model is an existence proof, not a quantitative BM fit.

## Supporting Information status — v13

The electrochemical/mechanistic SI has been rebuilt and de-duplicated against the main text.

Current Word export generated in the latest session:
`HEO_SI_V13_FinalElectrochem_2026-09-29.docx`

It contains 20 rendered/QA-checked pages.

### Structural package still pending
Figures S1–S6 remain collaborator-dependent:
- XRD/refinement;
- microscopy/domain statistics;
- HRTEM/SAED;
- EDS;
- XPS only if retained;
- N2 adsorption/BET fits.

Do not fabricate these panels.

### Frozen electrochemical/mechanistic SI figures

- S7: no-FEC cycling control only
- S8: normalized rate retention/recovery only
- S9: cycles 1–3 voltage profiles
- S10: cycle-resolved dQ/dV
- S11: relative interfacial-capacitance audit
- S12: pristine/post-cycle SEM; recheck exact pristine-image duplication after main Figure 2 is frozen
- S13: full multi-cycle GITT
- S14: four-material 3–30 s E–sqrt(t) fits at about 500 mAh g^-1
- S15: t50/t63/t90 robustness
- S16: Dapp/direct-relaxation disagreement map
- S17: GITT voltage-term decomposition
- S18: dQ/dV–GITT peak localization with sensitivity
- S19: 105-condition background/window sensitivity
- S20: cycle-history robustness
- S21: full R1–R4 single-step sweeps
- S22: fixed-R2 line cuts through the R2–R3 map
- S23: eigenmode spectrum + partial-rate audit

### Newly committed SI numerical authorities

Directory: `modeling/si_v13/`

- `HEO_SI_S14_ESQRT_FIT_SUMMARY_2026-09-29.csv`
- `HEO_SI_S15_T50_T63_T90_RAW_EXACT_2026-09-29.csv`
- `HEO_SI_S16_DISAGREEMENT_SUMMARY_2026-09-29.csv`
- `HEO_SI_S17_VOLTAGE_TERM_DECOMPOSITION_SUMMARY_2026-09-29.csv`
- `HEO_SI_S18_PEAK_LOCALIZATION_SENSITIVITY_2026-09-29.csv`
- `HEO_SI_S19_BACKGROUND_WINDOW_SENSITIVITY_2026-09-29.csv`
- `HEO_SI_S19_DIRECTIONAL_COUNTS_2026-09-29.csv`
- `HEO_SI_S20_CYCLE_HISTORY_SUMMARY_2026-09-29.csv`
- `HEO_SI_S21_SINGLE_STEP_SWEEP_SUMMARY_2026-09-29.csv`
- `HEO_SI_S22_R2_FIXED_LINECUTS_SUMMARY_2026-09-29.csv`
- `HEO_SI_S23_EIGENMODE_SUMMARY_2026-09-29.csv`
- `HEO_SI_S23_REST3_PARTIAL_RATE_SUMMARY_2026-09-29.csv`

Key SI robustness results:
- t50: median HEO/BM direct-rate ratio 0.7235; BM slower 34/37 states
- t63: 0.7599 by exact raw crossing; BM slower 35/37
- t90: 0.8961; BM slower 33/37
- conventional-GITT conflict quadrant: 35/37 states
- median Delta Es ratio BM/HEO = 1.8095
- median Delta Etau ratio BM/HEO = 1.1758
- 105-condition BM peak < HEO: 105/105
- 105-condition BM width > HEO: 105/105
- BM-Mg width is highly background-sensitive and should not be overinterpreted.

## Reference state

Main v16 currently contains 24 references in first-citation order.

Important corrected DOI/title pairings now present in v16:
- Ng et al., DOI 10.1039/D0TA09683K: NiO conversion-anode/SEI paper
- Li et al., DOI 10.1021/jacs.6b00061: metal-fluoride conversion-electrode voltage-hysteresis paper
- Parsons, DOI 10.1351/pac197437040499: Electrochemical nomenclature

Retain these corrected metadata.

## Claim boundaries

Preferred:
- accessible conversion capacity
- relaxation voltage change / relaxation magnitude
- t63 as a directly measured, model-free effective relaxation timescale
- conversion-associated relaxation after Figure 5 localization
- conflicting apparent-diffusivity indication

Avoid:
- calling Delta E_relax itself a kinetic rate
- treating Mg as a second BM-like capacity–kinetics contradiction
- saying apparent D proves faster kinetics
- saying GITT is invalid
- saying diffusion is absent
- assigning one unique rate-determining step
- equating t63 with a microscopic forward rate constant
- assigning experimental Delta E_relax quantitatively to the four-step model
- reviving the discarded heterogeneous-population model as current evidence

## Remaining submission blockers

1. Final Figures 1–2 collaborator structural/compositional package.
2. Final Mg synthesis recipe and collaborator-verified nominal/ICP composition.
3. Cell/electrode metadata:
   - current collector
   - drying temperature/time
   - active loading
   - electrode thickness
   - separator
   - electrolyte volume
   - glovebox H2O/O2
   - exact 1 C basis and rate sequence
4. Original numerical first-cycle voltage profiles if recoverable; otherwise retain documented vector-reconstruction provenance for dQ/dV.
5. Final XPS inclusion/exclusion decision.
6. Recheck S12 pristine SEM against final main Figure 2.
7. Final main/SI cross-reference, figure/table numbering, and reference-numbering audit after S1–S6 insertion.

## Next recommended work

Do not reopen the central BM/Mg story or Figure 3–6 logic unless new data require it.

Next:
1. freeze Figures 1–2 with Yoo-group input;
2. insert structural SI S1–S6;
3. finish methods metadata;
4. run one final main/SI reference and numbering audit;
5. regenerate final tracked Main Word and final submission SI Word.
