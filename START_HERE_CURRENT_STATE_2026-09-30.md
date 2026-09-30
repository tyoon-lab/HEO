# HEO — Current State, 2026-09-30

## Read this first

This is the authoritative restart point for the HEO manuscript. A new session should be able to resume from the repository without a separate handoff.

## Paper identity

Working title:

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Working target: **Advanced Functional Materials (AFM)**.

The paper is a materials/conversion-mechanism paper using GITT relaxation as the diagnostic. It is not framed as a general GITT-method paper.

## Current authority order

1. Main manuscript: `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`
2. Main reference audit: `manuscript/HEO_REFERENCE_AUDIT_MAIN_V16_2026-09-28.md`
3. SI architecture freeze: `manuscript/HEO_SI_V12_ARCHITECTURE_FREEZE_2026-09-29.md`
4. SI final assembly note: `manuscript/HEO_SI_V13_WORD_ASSEMBLY_2026-09-29.md`
5. SI electrochemical redundancy audit: `manuscript/HEO_SI_V12_S7_S14_REDUNDANCY_AUDIT_2026-09-29.md`
6. SI Step 2A GITT robustness: `manuscript/HEO_SI_V12_STEP2A_GITT_ROBUSTNESS_2026-09-29.md`
7. SI Step 2B localization/history: `manuscript/HEO_SI_V12_STEP2B_LOCALIZATION_HISTORY_2026-09-29.md`
8. SI Step 2C microkinetic audit: `manuscript/HEO_SI_V12_STEP2C_MICROKINETIC_AUDIT_2026-09-29.md`
9. Four-step model authority: `modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`
10. Revised Mg four-step audit: `modeling/HEO_MG_REVISED_WINDOW_FOUR_STEP_TEST_2026-09-30.md`
11. Revised Mg thermodynamic trajectory: `modeling/HEO_MG_REVISED_WINDOW_U4_TRAJECTORY_2026-09-30.csv`
12. Conventional-GITT audit: `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`

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

Main four-material medians now use the common normalized first-lithiation window z = 0.40–0.90:

| Sample | Delta E_relax (mV) | t63 (min) | first-cycle delithiation capacity (mAh g^-1) |
|---|---:|---:|---:|
| HEO | 168.5 | 10.37 | 609.12 |
| BM-HEO | 160.5 | 13.02 | 782.08 |
| Mg-HEO | 111.3 | 10.53 | 458.91 |
| BM-Mg-HEO | 135.2 | 12.70 | 580.83 |

Primary contradiction:
**HEO -> BM-HEO gives capacity up while t63 also increases, i.e. higher accessible conversion with slower relaxation.**

The same milling direction is also present in the Mg-containing pair:
- Mg-HEO -> BM-Mg-HEO: capacity increases;
- t63 also increases.

Mg incorporation is a different comparison:
- capacity decreases;
- Delta E_relax decreases strongly;
- t63 changes very little.

Therefore Mg should not be described as a lower-capacity/slower-relaxation case in the main text.

Panel (b) remains the state-matched pristine-HEO/BM-HEO conventional-GITT audit over 200–800 mAh g^-1:
- median Dapp,BM/Dapp,HEO = 1.7817;
- median t63,HEO/t63,BM = 0.7622;
- detailed 37-state directional counts remain in the SI rather than the main prose.

The former four-material 200–800 mAh g^-1 medians are retained only as SI robustness/context, not as the main Figure 4(c,d) authority.

### Figure 5 — conversion localization

Use **relaxation hump** / **background-subtracted relaxation hump**, not “GITT excess” as the main terminology.

Figure 5a should show:
- full first-lithiation Delta E_relax versus normalized lithiation capacity;
- an enlarged late-stage view of the hump;
- sample-specific background used to isolate the hump over z = 0.40–0.90.

For voltage localization, each GITT step is placed at the 60 min rest-end voltage of that step.

Nominal dQ/dV / relaxation-hump rest-end peak pairs:
- HEO: 0.5446 / 0.5275 V
- BM-HEO: 0.5891 / 0.6175 V
- Mg-HEO: 0.4188 / 0.3870 V
- BM-Mg-HEO: 0.4848 / 0.5029 V

All nominal offsets are within about 32 mV.

Interpretation:
- the late-stage relaxation hump is dominated by processes occurring in the conversion region;
- relevant coupled processes can include nucleation/phase growth, phase-boundary motion, M–O rearrangement, cation/oxygen redistribution, and metal/Li2O formation;
- the hump does not identify one unique microscopic step.

The shallow BM-Mg-HEO peak remains background/window sensitive in the SI.

### Figure 6 — distinct kinetic and thermodynamic perturbations in the four-step model

Current effective sequence:
oxide-derived state -> lithiated/reduced oxide -> M–O-reconstructed state -> product-side reconstructed state -> metal/Li2O-containing converted state.

Computational state symbols remain O <-> I <-> J <-> K <-> C.

Model meaning:
- one kinetic population with one set of rate parameters;
- particle/domain kinetic distributions are not included;
- R1: initial electrochemical lithiation/electron transfer;
- R2: effective M–O dissociation/local reconstruction;
- R3: effective Li2O-forming/product-side reconstruction;
- R4: subsequent electron transfer/metal reduction.

Single-step rate-perturbation audit:
- slowing R2 or R3 alone gives the conventional response: capacity down, t63 up;
- do not call this an a priori RDS assignment.

BM-oriented R2–R3 audit:
- a finite region gives Q/Q0 > 1 and t63/t0 > 1;
- representative R2 x 0.465, R3 x 50 gives Q ratio about 1.111, t63 ratio about 1.087, slowest finite collective mode 15.35 -> 17.68 min;
- experimental BM/HEO is Q = 1.284 and t63 = 1.256 with the revised z = 0.40–0.90 t63 authority;
- the minimal model reproduces the direction but not the full experimental magnitude.

Revised Mg authority:
- experimental Mg/HEO Q ratio = 0.7534;
- t63 ratio = 1.0154;
- Delta E_relax ratio = 0.6605.

The fixed-thermodynamics R2–R3 map does not reproduce this Mg direction well. In the same four-step network, keeping all kinetic rates fixed and shifting only the product-side electrochemical equilibrium offset gives a Mg-like trajectory. Illustrative u4 = -3 -> -1.5:
- Q/Q0 = 0.7637;
- t63/t0 = 0.9975;
- modeled Delta E ratio = 0.755.

Thus Figure 6c should retain BOTH experimental markers but distinguish two model trajectories:
- BM marker with the step-selective R2–R3 kinetic response;
- Mg marker with a separate product-side thermodynamic-shift trajectory.

Do not assign BM uniquely to R2/R3 or Mg uniquely to u4. The calculations are mechanistic-consistency tests.

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

Main v17 retains the audited 24-reference list in first-citation order.

Important corrected DOI/title pairings retained in v17:
- Ng et al., DOI 10.1039/D0TA09683K: NiO conversion-anode/SEI paper
- Li et al., DOI 10.1021/jacs.6b00061: metal-fluoride conversion-electrode voltage-hysteresis paper
- Parsons, DOI 10.1351/pac197437040499: Electrochemical nomenclature

Retain these corrected metadata.

## Claim boundaries

Preferred:
- accessible conversion capacity
- relaxation voltage change / relaxation magnitude
- t63 as a directly measured characteristic relaxation timescale
- late-stage relaxation hump dominated by the conversion region after Figure 5 localization
- conflicting apparent-diffusivity indication

Avoid:
- calling Delta E_relax itself a kinetic rate
- treating Mg as a lower-capacity/slower-relaxation case after the revised z = 0.40–0.90 analysis
- saying apparent D proves faster kinetics
- saying GITT is invalid
- saying diffusion is absent
- assigning one unique rate-determining step
- equating t63 with a microscopic forward rate constant
- assigning experimental Delta E_relax quantitatively to the four-step model
- reviving the discarded heterogeneous-population model as current evidence
- forcing Mg onto the BM-oriented fixed-thermodynamics R2–R3 kinetic map

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

Current main-text authority is v17. The Figure 4–6 logic is now revised after PI comment review and the Mg re-analysis.

Next:
1. revise the Supporting Information to match the new main-text terminology, Figure S15 state-resolved t63 addition, detailed model derivation, and Mg thermodynamic trajectory;
2. compare Main and SI cross-references/numbering after the SI revision;
3. regenerate commented Main Word and revised SI Word;
4. freeze Figures 1–2 and insert structural SI S1–S6 when collaborator data arrive;
5. finish methods metadata and run the final submission audit.
