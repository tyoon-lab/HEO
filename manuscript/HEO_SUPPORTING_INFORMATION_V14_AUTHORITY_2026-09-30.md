# HEO Supporting Information v14 — Revised Main-v17 Authority, 2026-09-30

## Status

This file is the scientific and numbering authority for the Supporting Information after the Main v17 revision.

Main manuscript authority:
- `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`

Previous SI Word export:
- `HEO_SI_V13_FinalElectrochem_2026-09-29.docx`

The v13 Word file remains the binary layout source for later Word assembly, but its scientific text is superseded by this v14 authority wherever the two differ.

## Design principle

The SI adds controls, robustness tests, numerical audit, or mechanistic detail that are not already visible in the main figures. Main panels are not duplicated as standalone supplementary figures.

The revised Main v17 requires four SI changes:

1. the four-material Figure 4 summary now uses the normalized first-lithiation window z = 0.40–0.90 rather than the former broad 200–800 mAh g^-1 summary;
2. Figure 5 terminology changes from “excess” to “relaxation hump” / “background-subtracted relaxation hump”;
3. the four-step calculation is described as a single-population coarse-grained model with explicit calculation flow and collective relaxation modes;
4. Mg-HEO is no longer treated as a lower-capacity/slower-relaxation case. A separate product-side equilibrium-offset trajectory is added as Figure S24.

---

# S1. Structural and compositional characterization — pending collaborator freeze

Figures S1–S6 remain placeholders until verified data arrive.

- Figure S1. Full XRD patterns and final refinement.
- Figure S2. Additional microscopy and particle/domain statistics.
- Figure S3. HRTEM/SAED indexing audit.
- Figure S4. EDS elemental maps.
- Figure S5. XPS spectra and fitting, only if retained.
- Figure S6. N2 adsorption/desorption and BET fitting.

Tables S1–S3 remain reserved for composition/refinement, XPS if retained, and BET/particle metrics.

Do not infer missing values or crystallographic assignments.

---

# S2. Electrochemical controls and additional performance data

The existing electrochemical-control architecture is retained.

- Figure S7. No-FEC cycling control.
- Figure S8. Normalized rate retention and recovery.
- Figure S9. Cycles 1–3 voltage profiles.
- Figure S10. Cycle-resolved dQ/dV.
- Figure S11. Relative interfacial-capacitance audit.
- Figure S12. Representative pristine/post-cycle SEM.
- Figure S13. Full multi-cycle GITT responses.
- Table S4. Nominal relative interfacial-accessibility metric derived from the non-faradaic-window capacitance regression; retained only as a relative comparison, not an absolute electrochemically active area.

Main/SI boundaries:
- absolute FEC cycling remains in main Figure 3c;
- absolute rate capability remains in main Figure 3d;
- Figure S13 is cited from Section 2.3 as the complete GITT-profile context.

---

# S3. GITT relaxation and conventional apparent-diffusivity robustness

## S3.1. Operational relaxation descriptors

The finite-window relaxation magnitude is

Delta E_relax = E_60 min - E_3 s.

t50, t63, and t90 are the first times required to complete 50%, 63.2%, and 90% of the observed 3 s-to-rest-end voltage recovery. The descriptors are obtained directly from the measured voltage trajectory and do not require a single-exponential fit.

The early relaxation is additionally represented empirically as E(t) = a + b sqrt(t) over 3–30 s. This short-time representation is retained only as an operational fit-quality audit and is not assigned uniquely to ohmic resistance, charge-transfer resistance, or intrinsic solid-state diffusion.

### Figure S14
Four-material representative early E versus sqrt(t) audit at approximately 500 mAh g^-1.

Frozen R2 values:
- HEO: 0.99931
- BM-HEO: 0.99877
- Mg-HEO: 0.99922
- BM-Mg-HEO: 0.99852

Do not compare the raw current-derived Roff values across Mg-free and Mg-containing source workbooks because the source current columns use different units.

## S3.2. Four-material analysis-window robustness

Main Figure 4(c,d) now uses the common normalized first-lithiation window z = 0.40–0.90.

The former 200–800 mAh g^-1 summary is retained only as an alternative-window robustness comparison.

### Table S5. Four-material relaxation summary under the main normalized window and the former absolute-capacity window

| Sample | Delta E_relax, z=0.40–0.90 (mV) | t63, z=0.40–0.90 (min) | Delta E_relax, 200–800 (mV) | t63, 200–800 (min) |
|---|---:|---:|---:|---:|
| HEO | 168.5 | 10.37 | 160.9 | 8.68 |
| BM-HEO | 160.5 | 13.02 | 176.3 | 11.57 |
| Mg-HEO | 111.3 | 10.53 | 109.5 | 11.01 |
| BM-Mg-HEO | 135.2 | 12.70 | 144.3 | 12.99 |

Interpretation:
- the BM-HEO/HEO higher-capacity/slower-relaxation direction is preserved under both window definitions;
- the Mg-HEO/HEO t63 difference is not robust enough to support a central “Mg slows relaxation” claim;
- the revised main interpretation therefore emphasizes the strong Mg-induced decrease in accessible capacity and relaxation magnitude while t63 remains nearly unchanged in the normalized conversion-focused window.

Numerical authority:
`modeling/si_v14/HEO_SI_FIG4_WINDOW_ROBUSTNESS_SUMMARY_2026-09-30.csv`

A new unverified all-four state-resolved t63 curve is **not** introduced. The available verified evidence consists of the main-window medians, the HEO/BM state-matched audit, and the cycle-resolved four-material medians in Figure S20. The state dependence of Delta E_relax is already displayed in main Figure 5.

## S3.3. Relaxation-fraction robustness for pristine HEO/BM-HEO

### Figure S15
HEO/BM-HEO t50/t63/t90 robustness over 37 state-matched points between approximately 200 and 800 mAh g^-1.

Direct relaxation-rate ratios are oriented HEO/BM so that values below unity indicate slower BM-HEO relaxation.

| Descriptor | Median HEO/BM ratio | BM slower states |
|---|---:|---:|
| t50 | 0.7235 | 34/37 |
| t63 | 0.7599 | 35/37 |
| t90 | 0.8961 | 33/37 |

The HEO/BM ordering therefore does not depend on selecting the 63.2% criterion.

## S3.4. Descriptor-disagreement map

### Figure S16
State-matched map:
- x = Dapp,BM / Dapp,HEO
- y = t63,HEO / t63,BM

All 37 states satisfy Dapp,BM/Dapp,HEO > 1 and 35/37 states lie below unity in the direct relaxation-rate ratio.

This is the disagreement quadrant in which conventional Dapp ranks BM-HEO faster while direct relaxation ranks it slower.

## S3.5. Voltage-term decomposition

### Figure S17
State dependence of:
- Delta Es,BM / Delta Es,HEO
- Delta Etau,BM / Delta Etau,HEO
- Dapp,BM / Dapp,HEO

Frozen medians:
- Delta Es ratio = 1.8095
- Delta Etau ratio = 1.1758
- Dapp ratio = 1.7817

The relaxed voltage increment changes more strongly after milling than the finite-pulse voltage excursion. This unequal change raises the conventional Dapp ratio even though the direct relaxation is slower.

Tables S6 and S7 retain the full 37-state audit and compact statistics.

---

# S4. Conversion-region localization, sensitivity, and cycle-history robustness

The terminology in this section is revised throughout:
- use **relaxation hump** for the raw late-stage feature above background;
- use **background-subtracted relaxation hump** after background subtraction;
- do not use “GITT excess” as the primary term.

## S4.1. Peak localization and sensitivity

### Figure S18
Cathodic dQ/dV peak voltage versus background-subtracted relaxation-hump peak at the 60 min rest-end voltage, including sensitivity ranges.

Nominal dQ/dV / relaxation-hump peak pairs:
- HEO: 0.5446 / 0.5275 V
- BM-HEO: 0.5891 / 0.6175 V
- Mg-HEO: 0.4188 / 0.3870 V
- BM-Mg-HEO: 0.4848 / 0.5029 V

All nominal offsets are within approximately 32 mV.

Interpretation:
- the HEO, BM-HEO, and Mg-HEO localization is comparatively tight;
- the shallow BM-Mg-HEO hump has a broad background/window-dependent peak range and is not assigned a uniquely determined conversion peak voltage;
- the main claim rests on the cross-material correspondence with the conversion region rather than on one exact BM-Mg-HEO voltage.

Table S8 retains the nominal peak positions and tested ranges.

## S4.2. Background/window sensitivity

### Figure S19
Sensitivity of the first-cycle **background-subtracted relaxation hump** to 105 tested background/window definitions.

Use:
- hump amplitude, not “excess amplitude”;
- FWHM-like width only as a response descriptor, not an intrinsic kinetic rate.

Frozen directional robustness:
- BM-HEO hump amplitude < HEO: 105/105
- BM-HEO width > HEO: 105/105
- Mg-HEO hump amplitude < HEO: 105/105
- BM-Mg-HEO hump amplitude < HEO: 105/105
- BM-Mg-HEO hump amplitude > Mg-HEO: 80/105

The BM-Mg-HEO width remains highly background sensitive and should not be overinterpreted.

Table S9 retains the amplitude/width ranges.

## S4.3. Cycle-history robustness

### Figure S20
Cycle-history evolution of the conversion-region relaxation:
(a) normalized hump-peak state;
(b) hump amplitude;
(c) median t63 over z = 0.40–0.90;
(d) cycle-3/cycle-1 amplitude ratio versus t63 ratio.

Frozen medians over z = 0.40–0.90:

| Sample | C1 t63 (min) | C2 t63 (min) | C3 t63 (min) |
|---|---:|---:|---:|
| HEO | 10.37 | 9.43 | 9.57 |
| BM-HEO | 13.02 | 11.18 | 11.33 |
| Mg-HEO | 10.53 | 9.83 | 9.53 |
| BM-Mg-HEO | 12.70 | 10.90 | 10.73 |

The hump amplitude changes substantially more than the characteristic timescale. BM-HEO retains longer t63 than HEO beyond the first cycle while also retaining higher approximate reversible capacity, showing that the BM capacity-relaxation ordering is not confined to first-cycle irreversibility.

Tables S10 and S11 retain cycle-history descriptors and later-cycle background-form sensitivity.

---

# S5. Four-step conversion microkinetic audit

## S5.1. Effective sequence and model boundary

The model represents the reacting electrode as **one kinetic population with one set of rate parameters**. Particle-to-particle and domain-to-domain kinetic distributions are not included.

The physical sequence is represented as:
1. R1: initial electrochemical lithiation/electron transfer;
2. R2: effective M–O dissociation/local reconstruction;
3. R3: effective Li2O-forming/product-side reconstruction;
4. R4: subsequent electron transfer/metal reduction.

For computation, the corresponding effective states are denoted:

O <-> I <-> J <-> K <-> C.

The symbols are computational states rather than uniquely identified HEO phases.

R1 and R4 are reversible electrochemical steps. R2 and R3 are reversible first-order internal steps.

For the internal steps:

r2 = k2,f aI - k2,r aJ

r3 = k3,f aJ - k3,r aK

with state balances:

dxI/dt = r1 - r2

dxJ/dt = r2 - r3

dxK/dt = r3 - r4

dxC/dt = r4

and xO = 1 - xI - xJ - xK - xC.

The external Faradaic current is:

jext = F(nu1 r1 + nu4 r4).

### Calculation flow

During galvanostatic operation:
1. the current state populations define the partial rates;
2. the electrode potential is solved from the imposed-current balance;
3. the state balances are integrated forward in time;
4. integration continues until the fixed model voltage cutoff is reached;
5. the modeled accessible capacity is the passed charge before cutoff.

During open-circuit relaxation:
1. jext is set to zero;
2. zero external current constrains the sum of the Faradaic partial currents but does not require r1 = r2 = r3 = r4 = 0;
3. the same state equations continue to evolve while internal populations redistribute;
4. the open-circuit potential is solved from the zero-current balance;
5. t63 is extracted using the same 3 s reference convention as the experiment.

For the matched-state model comparison, relaxation is initiated at Delta Q = 0.30 and followed for 3600 s.

Table S12 retains the representative parameter set:
- k1 = 0.02000
- k2,f = 0.00200
- k2,r = 0.001414...
- k3,f = 0.00100
- k3,r = 0.0007071...
- k4 = 0.01000
- product-side electrochemical equilibrium offset u4 = -3
- Japp = 2e-4
- Ecut = 0.020
- Delta Q = 0.30
- rest = 3600 s

The parameter values define a representative coarse-grained network. They are not fitted microscopic rate constants for the HEO materials.

## S5.2. Single-step rate perturbation

Rename the former “single-step limiting audit” throughout as **single-step rate perturbation**.

### Figure S21
Detailed R1–R4 rate-scale sweeps:
(a) Q/Q0 versus rate scale;
(b) t63/t63,0 versus rate scale.

For reversible R2 and R3 perturbations, forward and reverse rate constants are scaled together so the equilibrium constants remain unchanged.

Representative 0.1x results:
- R1: Q/Q0 = 0.893, t63/t0 = 0.959
- R2: 0.351, 2.437
- R3: 0.495, 1.573
- R4: 0.907, 1.058

Representative 10x results:
- R1: 1.010, 0.997
- R2: 1.183, 0.952
- R3: 1.325, 0.530
- R4: 1.009, 1.003

The perturbation identifies sensitivity of the observable response and does not designate an a priori rate-determining step.

Table S13 retains the compact 0.1x/1x/10x numerical audit.

## S5.3. Step-selective R2–R3 kinetic regime — BM-oriented test

### Figure S22
Fixed-R2 line cuts through the R2–R3 kinetic map at fixed thermodynamics.

The full map contains a finite region satisfying both:
- Q/Q0 > 1
- t63/t63,0 > 1.

Across the 18 x 22 grid, 28/396 points lie in this higher-capacity/slower-relaxation regime.

The representative case R2 x 0.465, R3 x 50 gives:
- Q/Q0 = 1.111
- t63/t0 = 1.087.

Experimental BM-HEO/pristine-HEO under the revised main-window authority:
- capacity ratio = 782.08 / 609.12 = 1.284
- t63 ratio = 13.02 / 10.37 = 1.256.

The model reproduces the **direction** but not the full experimental magnitude. It is therefore a mechanistic-consistency test rather than a quantitative BM fit.

Table S14 retains the selected fixed-R2 intervals and full-grid statistics.

## S5.4. Collective relaxation modes and partial-rate audit

After current interruption, the coupled intermediate populations continue to redistribute. Near the relaxed state,

d(delta x)/dt = J delta x

and

delta E(t) = sum_i Bi exp(-t/tau_i).

Each tau_i is a **collective relaxation mode of the coupled reaction network**, not the time constant of a single elementary reaction.

### Figure S23
Internal diagnostics for the reference case and R2 x 0.465, R3 x 50:
(a) finite collective relaxation timescales;
(b) partial rates at pulse end and 3 s after interruption.

Frozen eigen-times:
Reference:
- 15.35 min
- 5.96 min
- 0.482 min

R2 x 0.465, R3 x 50:
- 17.68 min
- 0.584 min
- 0.183 min

Thus the slowest collective mode lengthens while faster modes accelerate.

At 3 s open circuit, r1 + r4 is approximately zero while r2 and r3 remain finite. Zero external Faradaic current therefore does not imply that all internal conversion-network rates vanish.

Tables S16 and S17 retain eigenmode and partial-rate values.

## S5.5. Mg directional test through a product-side equilibrium shift

The revised experimental Mg-HEO/pristine-HEO ratios are:

- capacity ratio = 458.91 / 609.12 = 0.7534
- t63 ratio = 10.53 / 10.37 = 1.0154
- Delta E_relax ratio = 111.3 / 168.5 = 0.6605

This point is **not** represented well by the fixed-thermodynamics R2–R3 kinetic map. Reducing capacity through slower R2/R3 kinetics lengthens t63 much more than observed experimentally.

A separate directional test therefore keeps the kinetic rates fixed and varies only the product-side electrochemical equilibrium offset u4.

### Figure S24. Mg-like thermodynamic-shift trajectory within the same four-step network

Panels:
(a) Q/Q0 versus u4;
(b) t63/t63,0 versus u4;
(c) modeled relaxation-magnitude ratio versus u4.

Reference:
u4 = -3
- Q/Q0 = 1
- t63/t0 = 1
- Delta E_model/Delta E0 = 1

Illustrative shifted point:
u4 = -1.5
- Q/Q0 = 0.7637
- t63/t0 = 0.9975
- Delta E_model/Delta E0 = 0.7550

Experimental Mg-HEO/pristine-HEO:
- Q ratio = 0.7534
- t63 ratio = 1.0154
- Delta E_relax ratio = 0.6605

The same four-step network can therefore produce the Mg-like **direction** of lower accessible capacity, smaller relaxation magnitude, and nearly unchanged characteristic timescale through a thermodynamic perturbation rather than a global kinetic slowdown.

This result does **not** establish that Mg incorporation uniquely changes u4 or that u4 = -1.5 is a fitted Mg parameter.

Numerical authority:
- `modeling/HEO_MG_REVISED_WINDOW_FOUR_STEP_TEST_2026-09-30.md`
- `modeling/HEO_MG_REVISED_WINDOW_U4_TRAJECTORY_2026-09-30.csv`
- `modeling/si_v14/HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv`

## S5.6. Experimental/model comparison boundary

Revise Table S15 to distinguish the two perturbation classes.

### Table S15. Experimental trend directions and representative four-step model responses

| Comparison | Type | Q ratio | t63 ratio | relaxation-magnitude ratio |
|---|---|---:|---:|---:|
| BM-HEO / HEO | experiment | 1.284 | 1.256 | 160.5/168.5 = 0.953 |
| R2 x 0.465, R3 x 50 / reference | step-selective kinetics | 1.111 | 1.087 | 1.014 |
| Mg-HEO / HEO | experiment | 0.753 | 1.015 | 0.661 |
| u4 = -1.5 / reference | product-side equilibrium shift | 0.764 | 0.998 | 0.755 |

The modeled relaxation magnitude is used only directionally. The experimental voltage relaxation can include transport, interfacial polarization, and state-dependent thermodynamic contributions beyond the four-step conversion sequence.

## S5.7. Interpretation boundaries

Supported:
- one multistep conversion network can show higher accessible capacity together with slower relaxation under step-selective kinetic changes;
- the revised Mg trend can arise in the same network through a thermodynamic perturbation without a large change in t63;
- relaxation magnitude and characteristic timescale are distinct observables.

Not supported:
- a unique assignment of ball milling to R2/R3;
- a unique assignment of Mg incorporation to u4;
- quantitative fitting of experimental Delta E_relax by the four-step model;
- one unique microscopic rate-determining step;
- the claim that GITT-derived Dapp is invalid or that Li transport is absent;
- the discarded heterogeneous-population model.

---

# S6. References cited in Supporting Information

Retain SI references [S1]–[S8] from v13 without renumbering at this stage.

---

# S7. Items pending before submission

- replace Figures S1–S6 and Table S1 with the collaborator-verified structural/compositional package;
- decide whether XPS is retained;
- recheck Figure S12 pristine SEM against the final main microscopy figure;
- insert final experimental methods metadata;
- use original numerical first-cycle voltage profiles if recovered, replacing the present vector-reconstructed dQ/dV source while retaining the smoothing-sensitivity audit;
- run the main/SI cross-reference and numbering audit after this v14 revision;
- generate the revised SI Word file only after that audit.

## Numerical authority

Existing:
- `modeling/si_v13/` for S14–S23 frozen summaries.

New v14 additions:
- `modeling/si_v14/HEO_SI_FIG4_WINDOW_ROBUSTNESS_SUMMARY_2026-09-30.csv`
- `modeling/si_v14/HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv`
- `modeling/si_v14/plot_HEO_SI_S24_Mg_thermodynamic_trajectory.py`

## Current figure authority

S1–S6 pending structural package.
S7–S13 unchanged electrochemical controls.
S14 early E–sqrt(t) audit.
S15 t50/t63/t90 robustness.
S16 Dapp/direct-relaxation disagreement map.
S17 voltage-term decomposition.
S18 dQ/dV–relaxation-hump localization sensitivity.
S19 105-condition relaxation-hump background/window sensitivity.
S20 cycle-history robustness.
S21 full R1–R4 single-step rate-perturbation sweeps.
S22 fixed-R2 line cuts / R2–R3 kinetic-regime audit.
S23 collective eigenmode + partial-rate audit.
S24 Mg product-side equilibrium-shift trajectory.
