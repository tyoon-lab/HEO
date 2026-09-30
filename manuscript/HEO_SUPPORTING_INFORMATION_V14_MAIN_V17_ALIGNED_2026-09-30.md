# HEO Supporting Information v14 — Main-v17 Aligned Authority, 2026-09-30

## Status

This file is the current Supporting Information scientific/text authority after the PI-comment review, the Figure 4 conversion-window revision, and the revised Mg four-step model audit.

Main-text authority:
`manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`

Previous SI authority:
`manuscript/HEO_SUPPORTING_INFORMATION_V13_AUTHORITY_2026-09-30.md`

The existing v13 Word file remains an earlier export only. A revised Word file will be assembled after the Main–SI cross-reference audit.

## SI design principle

The SI adds controls, state dependence, robustness, numerical audit, and model detail that are not already visible in the main figures. Main panels are not duplicated as standalone SI figures.

The revised terminology follows main v17:
- use **GITT relaxation**, **voltage relaxation**, or **relaxation after current interruption**;
- use **late-stage relaxation hump** / **background-subtracted relaxation hump** for the Figure 5 feature;
- do not use “GITT excess” as the preferred main/SI term;
- use **single-step rate perturbation**, not “single-step limiting” when describing the model calculation;
- describe model eigenmodes as **collective relaxation modes**, not elementary-reaction time constants.

---

# S1. Structural/compositional characterization — collaborator dependent

Figures S1–S6 remain placeholders until collaborator-verified data are frozen.

### Figure S1 — full XRD/refinement
Full XRD patterns, refinement, phase fractions, lattice parameters, and residuals.

### Figure S2 — additional microscopy and particle/domain statistics
Additional SEM/TEM fields and quantitative particle/domain-size distributions.

### Figure S3 — HRTEM/SAED indexing audit
Final HRTEM lattice fringes, SAED, indexing, and spacing assignments.

### Figure S4 — EDS elemental maps
Full elemental maps for the four materials.

### Figure S5 — XPS, only if retained
Survey/high-resolution spectra and final fitting residuals. Remove and renumber once, globally, if XPS is excluded.

### Figure S6 — N2 adsorption/desorption and BET fitting
Full isotherms and fitting intervals.

Do not infer missing structural quantities or Mg-site assignments.

---

# S2. Electrochemical controls and additional performance

### Figure S7 — FEC control
Cycling with and without the common 10 wt% FEC condition. This is an electrolyte/interphase control only.

### Figure S8 — normalized rate retention and recovery
Normalized rate retention/recovery and additional rate-cycle detail not duplicated from main Figure 3d.

### Figure S9 — cycles 1–3 voltage-profile evolution
Multi-cycle voltage profiles for all four materials.

### Figure S10 — cycle-resolved differential capacity
Cycle-resolved cathodic/anodic dQ/dV evolution beyond the compact first-cycle localization used in main Figure 5.

### Figure S11 — relative interfacial-capacitance audit
Non-faradaic-window CV and scan-rate regression. Interpret only as a relative interfacial-accessibility metric.

### Figure S12 — pristine/post-cycle SEM
Morphological comparison before and after cycling. Recheck exact pristine-image duplication after main Figure 2 is frozen.

### Figure S13 — full multi-cycle GITT
Full GITT histories for all four materials. Main Figure 4a remains only the representative pulse/rest definition.

---

# S3. GITT relaxation and conventional-apparent-diffusivity robustness

## S3.1. Early post-interruption fit audit

### Figure S14 — four-material early E–sqrt(t) audit
Representative 3–30 s E versus sqrt(t) fits at approximately 500 mAh g^-1.

Interpretation boundary:
- this is an operational early-time fit-quality audit;
- it is not evidence that the entire pulse/rest response obeys a single diffusion model;
- do not assign the fitted slope uniquely to ohmic resistance, charge transfer, or intrinsic solid diffusion.

Frozen representative R2 values:
- HEO 0.99931
- BM-HEO 0.99877
- Mg-HEO 0.99922
- BM-Mg-HEO 0.99852

## S3.2. State dependence and relaxation-fraction robustness

### Figure S15 — state-resolved t63 and t50/t63/t90 robustness

**Panel (a): all-four state dependence.**
Plot binned first-lithiation t63 against normalized lithiation capacity z over the fully verified common raw-data overlap, approximately z = 0.20–0.63.

Purpose:
- show directly that the four-sample median values used in main Figure 4 do not hide the state dependence of the relaxation timescale;
- provide the missing all-four t63-versus-state view requested during PI review.

Data authority:
`modeling/si_v14/HEO_SI_S15_ALLFOUR_T63_BINNED_2026-09-30.csv`

Important boundary:
- panel (a) uses only the common state interval for which state-resolved values are independently verified for all four materials;
- it is not used to redefine the main Figure 4 z = 0.40–0.90 medians.

**Panel (b): HEO/BM relaxation-fraction robustness.**
Retain the state-matched HEO/BM direct relaxation-rate ratios for t50, t63, and t90 over approximately 200–800 mAh g^-1.

Frozen exact raw-crossing summary:

| Descriptor | Median HEO/BM direct-rate ratio | BM slower states |
|---|---:|---:|
| t50 | 0.7235 | 34/37 |
| t63 | 0.7599 | 35/37 |
| t90 | 0.8961 | 33/37 |

Data authority:
`modeling/si_v13/HEO_SI_S15_T50_T63_T90_RAW_EXACT_2026-09-29.csv`

Plotting authority:
`modeling/si_v14/plot_HEO_SI_S15_state_fraction_robustness.py`

## S3.3. Descriptor disagreement

### Figure S16 — Dapp/direct-relaxation disagreement map
Plot:
- x = Dapp,BM / Dapp,HEO
- y = t63,HEO / t63,BM
- point color/ordering = matched capacity.

All 37 states have x > 1 and 35/37 have y < 1. This visualizes the disagreement quadrant without duplicating main Figure 4b.

## S3.4. Conventional-GITT voltage-term decomposition

### Figure S17 — state dependence of Delta Es and Delta Etau
Plot the state-matched ratios:
- Delta Es,BM / Delta Es,HEO
- Delta Etau,BM / Delta Etau,HEO
- Dapp,BM / Dapp,HEO.

Frozen medians:
- Delta Es ratio = 1.8095
- Delta Etau ratio = 1.1758
- Dapp ratio = 1.7817.

Interpretation:
the relaxed voltage increment increases more strongly after milling than the finite-pulse voltage excursion, which drives the conventional Dapp ratio upward even though the direct relaxation is slower.

## S3.5. State-window robustness of the four-material summary

The main Figure 4(c,d) authority is the normalized first-lithiation window z = 0.40–0.90:

| Sample | Delta E_relax (mV) | t63 (min) |
|---|---:|---:|
| HEO | 168.5 | 10.37 |
| BM-HEO | 160.5 | 13.02 |
| Mg-HEO | 111.3 | 10.53 |
| BM-Mg-HEO | 135.2 | 12.70 |

The former absolute-capacity 200–800 mAh g^-1 summary is retained only as a robustness/context comparison:

| Sample | Delta E_relax (mV) | t63 (min) |
|---|---:|---:|
| HEO | 160.9 | 8.68 |
| BM-HEO | 176.3 | 11.57 |
| Mg-HEO | 109.5 | 11.01 |
| BM-Mg-HEO | 144.3 | 12.99 |

Data authority:
`modeling/si_v14/HEO_SI_FIG4_WINDOW_ROBUSTNESS_SUMMARY_2026-09-30.csv`

Interpretation:
- the primary BM result, higher accessible capacity with longer relaxation, is robust to state-window choice;
- the Mg t63 ordering is state-window dependent and should therefore not be used as a central fast/slow claim;
- the robust Mg result in the main normalized window is lower capacity and markedly lower relaxation magnitude with nearly unchanged t63.

---

# S4. Conversion-region localization and cycle-history robustness

## S4.1. Peak-localization sensitivity

### Figure S18 — dQ/dV versus relaxation-hump peak localization with sensitivity
Use the revised terminology **background-subtracted relaxation hump**.

Nominal first-cycle peak positions:

| Sample | dQ/dV peak (V) | Relaxation-hump peak, 60 min rest-end V (V) | Difference (mV) |
|---|---:|---:|---:|
| HEO | 0.544575 | 0.527481 | -17.1 |
| BM-HEO | 0.589146 | 0.617535 | +28.4 |
| Mg-HEO | 0.418819 | 0.386972 | -31.8 |
| BM-Mg-HEO | 0.484822 | 0.502865 | +18.0 |

Sensitivity ranges:
- HEO relaxation-hump peak: 0.527481 V
- BM-HEO: 0.592919–0.628391 V
- Mg-HEO: 0.386972 V
- BM-Mg-HEO: 0.453175–0.618300 V.

The broad BM-Mg range reflects its shallow hump and is uncertainty, not a distinct mechanistic signal.

## S4.2. Background/window sensitivity

### Figure S19 — 105-condition relaxation-hump sensitivity
Report peak-amplitude and FWHM-like-width sensitivity across the tested background/window definitions.

Frozen ranges:

| Sample | Peak range (mV) | Width range (mAh g^-1) |
|---|---:|---:|
| HEO | 60.7–74.7 | 306–379 |
| BM-HEO | 36.7–51.0 | 379–497 |
| Mg-HEO | 13.0–18.6 | 192–351 |
| BM-Mg-HEO | 12.6–27.6 | 233–872 |

Directional robustness:
- BM-HEO hump amplitude < HEO: 105/105
- BM-HEO width > HEO: 105/105
- Mg-HEO hump amplitude < HEO: 105/105
- BM-Mg-HEO hump amplitude < HEO: 105/105
- BM-Mg-HEO > Mg-HEO amplitude only 80/105; do not require this trend.

Amplitude and width are response descriptors, not intrinsic rates.

## S4.3. Cycle-history robustness

### Figure S20 — cycle history of the conversion-region relaxation hump
Retain the cycle-1–3 history analysis in the SI.

Panels:
- (a) normalized state z_peak of the background-subtracted relaxation hump;
- (b) hump amplitude;
- (c) median t63 over z = 0.40–0.90;
- (d) cycle-3/cycle-1 amplitude ratio versus t63 ratio.

Cycle-1 to cycle-3 amplitude ratios span 0.435–1.698, whereas t63 ratios remain within 0.845–0.923.

BM-HEO retains higher approximate reversible reaction extent with longer t63 after the first cycle. Thus the BM capacity–relaxation ordering is not attributable only to first-cycle irreversibility.

Terminology rule:
use “conversion-region relaxation hump” or “relaxation hump localized to the conversion region”; avoid treating hump amplitude as a stationary phase fraction.

---

# S5. Four-step conversion microkinetic audit

## S5.1. Model definition and numerical procedure

The model represents the reacting electrode as one kinetic population with one set of rate parameters. It does not contain a distribution of particle-specific or domain-specific rate constants.

Physical effective sequence:
1. R1 — initial electrochemical lithiation/electron transfer;
2. R2 — effective M–O dissociation/local structural reconstruction;
3. R3 — effective Li2O-forming/product-side reconstruction;
4. R4 — subsequent electrochemical electron transfer/metal reduction.

Computational state labels:

O <-> I <-> J <-> K <-> C

where O is oxide-derived and C is the metal/Li2O-containing converted state. I, J, and K are coarse-grained intermediate states and are not assigned to uniquely identified phases in the experimental HEO.

R1 and R4 are represented by reversible Butler–Volmer-type rate functions. R2 and R3 are reversible first-order internal rates:

[
r_2=k_{2,f}a_I-k_{2,r}a_J,
qquad
r_3=k_{3,f}a_J-k_{3,r}a_K.
]

The state balances are

[
rac{dx_I}{dt}=r_1-r_2,
qquad
rac{dx_J}{dt}=r_2-r_3,
qquad
rac{dx_K}{dt}=r_3-r_4,
qquad
rac{dx_C}{dt}=r_4,
]

with

[
x_O=1-x_I-x_J-x_K-x_C.
]

The external Faradaic current is constrained by

[
j_{mathrm{ext}}=F(
u_1r_1+
u_4r_4).
]

In the normalized calculation, (
u_1=
u_4=1).

### Galvanostatic calculation

At every integration step during the current pulse:
1. the current state populations are used to evaluate the rate functions;
2. the electrode potential is determined by solving the Faradaic current-balance equation for the imposed normalized current;
3. the state balances are integrated forward;
4. integration stops when the fixed model voltage cutoff is reached;
5. modeled accessible capacity is proportional to the total charge passed before the cutoff.

The model therefore calculates capacity and relaxation from the same coupled reaction network.

### Current interruption and relaxation

At open circuit,

[
j_{mathrm{ext}}=0
]

constrains the sum of the Faradaic partial currents but does not require every internal rate to be zero. R2 and R3 can remain finite while R1 and R4 carry opposing partial currents. The state balances are integrated for 3600 s during the rest.

Relaxation comparisons are made at a common normalized passed charge, (Delta Q=0.30), using the same 3 s reference convention as the experiment.

### Collective relaxation modes

Near the relaxed state, small deviations obey

[
rac{d,deltamathbf{x}}{dt}=mathbf{J}deltamathbf{x},
]

where (mathbf{J}) is the Jacobian of the coupled state equations. The voltage response can then be written locally as

[
E(t)-E_{mathrm{eq}}=sum_i B_iexp(-t/	au_i).
]

Each finite (	au_i) is a collective mode of the coupled intermediate redistribution. It is not identified with the time constant of one elementary step.

### Reference parameters

| Parameter | Reference value | Role |
|---|---:|---|
| k1 | 0.02000 | R1 electrochemical lithiation/electron transfer |
| k2,f | 0.00200 | R2 forward reconstruction |
| k2,r | 0.001414 | R2 reverse reconstruction |
| k3,f | 0.00100 | R3 forward product-side reconstruction |
| k3,r | 0.0007071 | R3 reverse product-side reconstruction |
| k4 | 0.01000 | R4 electrochemical electron transfer/metal reduction |
| u4 | -3.000 | dimensionless product-side electrochemical equilibrium offset |
| Japp | 2.000e-4 | normalized galvanostatic current |
| Ecut | 0.02000 | normalized model cutoff voltage |
| Delta Q | 0.30000 | common normalized passed charge for relaxation comparison |
| rest time | 3600 s | modeled open-circuit period |

The model is a mechanistic-consistency calculation. No parameter is fitted uniquely to BM-HEO or Mg-HEO.

## S5.2. Single-step rate perturbation

### Figure S21 — full R1–R4 rate sweeps
Each effective step is varied independently from 0.1× to 10× while the remaining kinetic parameters and relevant equilibrium parameters are held fixed.

For R2 and R3, forward and reverse constants are scaled together so their equilibrium constants remain unchanged.

Panels:
- (a) Q/Q0 versus individual rate scale;
- (b) t63/t63,0 versus individual rate scale.

Representative values:

| Step | scale | Q/Q0 | t63/t63,0 |
|---|---:|---:|---:|
| R1 | 0.1 | 0.893 | 0.959 |
| R2 | 0.1 | 0.351 | 2.437 |
| R3 | 0.1 | 0.495 | 1.573 |
| R4 | 0.1 | 0.907 | 1.058 |
| R2 | 10 | 1.183 | 0.952 |
| R3 | 10 | 1.325 | 0.530 |

Interpretation:
slowing R2 or R3 alone produces the conventional lower-capacity/slower-relaxation response. This is a sensitivity result, not an assignment of an experimental rate-determining step.

## S5.3. Step-selective R2–R3 kinetic response

### Figure S22 — fixed-R2 line cuts through the R2–R3 map
Retain the fixed-R2 line cuts that unpack main Figure 6b.

Finite Q-up/t63-up intervals:

| R2 scale | R3 interval | Q/Q0 range | t63/t0 range |
|---:|---:|---:|---:|
| 0.406063 | 8.498–50 | 1.005–1.042 | 1.200–1.211 |
| 0.464961 | 3.175–50 | 1.000–1.111 | 1.076–1.097 |
| 0.532402 | 2.141–2.607 | 1.003–1.034 | 1.009–1.041 |
| 0.698051 | none | — | — |

The finite overlap demonstrates that the BM-like direction requires coordinated step-selective changes rather than uniform acceleration or simple slowing of one step.

## S5.4. Collective modes and partial rates

### Figure S23 — eigenmode spectrum and partial-rate diagnostics
Compare the reference model with the representative R2×0.465, R3×50 case.

Finite collective relaxation modes:

| Case | tau1 (min) | tau2 (min) | tau3 (min) |
|---|---:|---:|---:|
| Reference | 15.353 | 5.959 | 0.482 |
| R2×0.465, R3×50 | 17.680 | 0.584 | 0.183 |

At 3 s after current interruption:

Reference:
- r1 = -5.038e-5
- r2 = 1.127e-4
- r3 = 7.377e-5
- r4 = +5.038e-5
- r1+r4 approximately 0.

Representative step-selective case:
- r1 = -6.202e-5
- r2 = 1.031e-4
- r3 = 9.051e-5
- r4 = +6.202e-5
- r1+r4 approximately 0.

The slowest collective mode lengthens while faster modes accelerate and internal redistribution remains finite at zero external current.

## S5.5. Mg thermodynamic-shift audit

### Figure S24 — product-side equilibrium-offset trajectory
This new SI figure unpacks the Mg trajectory shown compactly in main Figure 6c without duplicating that panel.

Hold all kinetic rate constants fixed and vary only the dimensionless product-side electrochemical equilibrium offset u4.

Recommended panels:
- (a) Q/Q0 versus u4;
- (b) t63/t63,0 versus u4;
- (c) modeled relaxation-magnitude ratio versus u4.

Horizontal dashed references show the experimental Mg-HEO/pristine-HEO ratios.

Data authority:
`modeling/si_v14/HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv`

Plotting authority:
`modeling/si_v14/plot_HEO_SI_S24_Mg_thermodynamic_trajectory.py`

Representative comparison:

| Case | Q/Q0 | t63/t0 | Delta E ratio |
|---|---:|---:|---:|
| Experimental Mg-HEO / HEO | 0.7534 | 1.0154 | 0.6605 |
| Illustrative u4 = -1.5 | 0.7637 | 0.9975 | 0.7549 |

Interpretation:
- the fixed-thermodynamics R2–R3 kinetic map does not reproduce the revised Mg point well;
- a product-side thermodynamic shift within the same four-step network produces the experimental direction of lower accessible capacity, lower relaxation magnitude, and nearly unchanged t63;
- the numerical u4 change is illustrative and is not assigned uniquely to Mg incorporation;
- modeled Delta E is compared directionally only, not as a quantitative fit to the full measured voltage relaxation.

Detailed audit:
`modeling/HEO_MG_REVISED_WINDOW_FOUR_STEP_TEST_2026-09-30.md`

---

# Revised table architecture

The table architecture for the v14 build is:

### Table S1 — final composition and structural refinement
Nominal composition, final ICP-OES composition, refined lattice parameters, phase assignments/fractions, and refinement statistics.

### Table S2 — XPS fit parameters, only if retained
Remove if XPS is excluded.

### Table S3 — BET / particle-size metrics

### Table S4 — relative interfacial-capacitance regression

### Table S5 — current-off descriptor/state-window summary
Include both:
- main-authority z = 0.40–0.90 medians;
- former 200–800 mAh g^-1 medians as robustness/context.
Do not use the latter to claim Mg is intrinsically slower.

### Table S6 — full 37-state HEO/BM conventional-GITT audit

### Table S7 — compact conventional-GITT audit statistics
Dapp ratio, direct relaxation-rate ratio, directional counts, Delta Es and Delta Etau summary.

### Table S8 — peak-voltage localization/sensitivity
Use relaxation-hump terminology.

### Table S9 — 105-condition background/window sensitivity
Use relaxation-hump terminology.

### Table S10 — cycle-history descriptors

### Table S11 — later-cycle background-form sensitivity

### Table S12 — four-step model parameters and protocol
Use the parameter definitions in S5.1.

### Table S13 — single-step rate-perturbation audit
Replace “single-step limiting” terminology.

### Table S14 — R2–R3 regime / line-cut audit

### Table S15 — experimental/model observable-space boundary
Revise the former experimental-magnitude table.

Use:
- BM experimental: Q ratio 1.284; t63 ratio 1.256.
- Representative BM-oriented R2×0.465, R3×50: Q 1.111; t63 1.087.
- Mg experimental: Q 0.7534; t63 1.0154; Delta E ratio 0.6605.
- Illustrative Mg-oriented u4 = -1.5: Q 0.7637; t63 0.9975; modeled Delta E ratio 0.7549.

The table compares observable directions/boundaries only. It does not assign microscopic model parameters to the materials.

### Table S16 — current-off collective eigenmodes

### Table S17 — representative partial rates

### Table S18 — Mg product-side thermodynamic trajectory
List u4 and the resulting Q, t63, and modeled-Delta-E ratios.

---

# Main/SI boundary after v14 revision

Main Figure 3:
accessible capacity and conventional electrochemical performance.

Main Figure 4:
- central capacity–relaxation mismatch;
- magnitude–timescale distinction;
- state-matched Dapp/direct-relaxation conflict.

SI adds:
- S15 all-four t63 state dependence and fractional-relaxation robustness;
- S16 disagreement map;
- S17 voltage-term decomposition;
- Table S5 state-window robustness.

Main Figure 5:
full/zoomed late-stage relaxation hump and nominal conversion localization.

SI adds:
- S18 localization sensitivity;
- S19 105-condition hump amplitude/width sensitivity;
- S20 cycle-history robustness.

Main Figure 6:
compact model summary including both the BM kinetic trajectory and Mg thermodynamic trajectory.

SI adds:
- S21 full one-dimensional single-step sweeps;
- S22 R2–R3 line cuts;
- S23 collective modes/partial rates;
- S24 detailed u4 trajectory.

---

# Numerical authority added in v14

Directory:
`modeling/si_v14/`

- `HEO_SI_S15_ALLFOUR_T63_BINNED_2026-09-30.csv`
- `HEO_SI_FIG4_WINDOW_ROBUSTNESS_SUMMARY_2026-09-30.csv`
- `HEO_SI_S24_MG_U4_TRAJECTORY_2026-09-30.csv`
- `plot_HEO_SI_S15_state_fraction_robustness.py`
- `plot_HEO_SI_S24_Mg_thermodynamic_trajectory.py`

Previously frozen v13 numerical files remain valid for S14, S15(b), S16–S23 unless explicitly superseded above.

---

# Remaining before Word assembly

1. Use this v14 authority to revise the SI Word body, captions, and tables.
2. Insert the revised S15 and new S24 artwork.
3. Run the dedicated Main-v17/SI-v14 cross-reference and numbering audit before final Word output.
4. Structural S1–S6 remain collaborator-dependent and cannot be fabricated.
5. Final submitted SI must replace the S1–S6 placeholders with verified data and apply one global renumbering if XPS is removed.
