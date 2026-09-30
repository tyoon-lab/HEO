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
3. SI authority: `manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`
4. Previous SI Word assembly note: `manuscript/HEO_SI_V13_WORD_ASSEMBLY_2026-09-29.md`
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

## Supporting Information status — v14

The SI scientific/text authority has been revised to match main v17:

`manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`

The existing v13 Word file remains an earlier export and will be rebuilt only after the dedicated Main/SI numbering audit.

### Structural package still pending
Figures S1–S6 remain collaborator-dependent:
- XRD/refinement;
- microscopy/domain statistics;
- HRTEM/SAED;
- EDS;
- XPS only if retained;
- N2 adsorption/BET fits.

Do not fabricate these panels.

### Revised electrochemical/mechanistic SI architecture

- S7: no-FEC cycling control
- S8: normalized rate retention/recovery
- S9: cycles 1–3 voltage profiles
- S10: cycle-resolved dQ/dV
- S11: relative interfacial-capacitance audit
- S12: pristine/post-cycle SEM
- S13: full multi-cycle GITT
- S14: four-material early E–sqrt(t) audit
- S15: **all-four t63 state dependence + t50/t63/t90 HEO/BM robustness**
- S16: Dapp/direct-relaxation disagreement map
- S17: GITT voltage-term decomposition
- S18: dQ/dV–relaxation-hump localization sensitivity
- S19: 105-condition relaxation-hump background/window sensitivity
- S20: cycle-history robustness
- S21: full R1–R4 single-step rate-perturbation sweeps
- S22: fixed-R2 line cuts through the R2–R3 map
- S23: collective eigenmode spectrum + partial-rate audit
- S24: **Mg product-side equilibrium-offset trajectory**

### New v14 numerical authorities

Directory: `modeling/si_v14/`

- `HEO_SI_S15_ALLFOUR_T63_BINNED_2026-09-30.csv`
- `HEO_SI_FIG4_WINDOW_ROBUSTNESS_SUMMARY_2026-09-30.csv`
- `HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv`
- `plot_HEO_SI_S15_state_fraction_robustness.py`
- `plot_HEO_SI_S24_Mg_thermodynamic_trajectory.py`

Important S15 boundary:
- panel (a) uses the fully verified common all-four state-resolved overlap, approximately z = 0.20–0.63;
- the main Figure 4 medians remain z = 0.40–0.90 and are tabulated separately;
- no unverified BM state-resolved values are extrapolated.

Table S5 now explicitly distinguishes the main z = 0.40–0.90 medians from the former 200–800 mAh g^-1 medians retained as robustness/context.

Table S15 is revised to use:
- BM experiment: Q = 1.284, t63 = 1.256;
- representative R2×0.465/R3×50: Q = 1.111, t63 = 1.087;
- Mg experiment: Q = 0.7534, t63 = 1.0154, Delta E = 0.6605;
- illustrative u4 = -1.5: Q = 0.7637, t63 = 0.9975, modeled Delta E = 0.7549.

Table S18 is added for the full Mg thermodynamic trajectory.

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
1. compare Main v17 and SI v14 cross-references/numbering and verify that every retained SI item is appropriately called from the main text;
2. resolve any numbering/citation mismatches found in that audit;
3. regenerate commented Main Word and revised SI Word;
4. freeze Figures 1–2 and insert structural SI S1–S6 when collaborator data arrive;
5. finish methods metadata and run the final submission audit.
