# HEO Modeling Development Log — Diffusion vs Phase-Transition Polarization

**Date:** 2026-09-18  
**Status:** Python v2 completed; MATLAB port deferred until Python logic is frozen.

## 0. Modeling question

The experimental observation to explain is not simply a change in apparent diffusivity.

Over 200–800 mAh g−1:

| Sample | DeltaE_relax (mV) | t63 (min) | excess phase-transition peak (mV) |
|---|---:|---:|---:|
| HEO | 160.9 | 8.68 | 70.8 |
| BM-HEO | 176.3 | 11.57 | 44.1 |
| Mg-HEO | 109.5 | 11.01 | 15.9 |
| BM-Mg-HEO | 144.3 | 12.99 | 21.1 |

The central anomaly is Mg-HEO: polarization decreases strongly while relaxation becomes slower.

## 1. Hypotheses defined before coding

### H0 — single-D diffusion model

Under otherwise comparable pulse conditions:
- diffusion polarization decreases monotonically as D increases;
- diffusion relaxation time decreases monotonically as D increases.

Illustrative scaling:
- eta_diff ~ D^(-1/2)
- tau_diff ~ L^2/D

The exact exponent is not critical for the sign test.

### H1 — Mg stabilization only

Mg reduces the fraction of material entering late-stage conversion:
- smaller transition hump;
- lower conversion capacity;
- relaxation time remains approximately HEO-like.

### H2 — Mg mobility reduction only

Mg slows phase-boundary / structural rearrangement:
- t63 increases;
- if the same transformation extent must proceed, smaller polarization is not naturally expected.

### H3 — Mg stabilization + lower residual structural mobility

Two independent physical coordinates:
- transformation extent / transition-polarization strength decreases;
- structural relaxation time increases.

Expected:
- hump down;
- capacity down;
- t63 up.

### H4 — ball milling changes accessibility + distribution

Ball milling is represented by:
- increased accessible fraction/interface;
- reduced effective domain/transport length;
- broader distribution of local transition conditions;
- broader distribution of structural relaxation times.

Expected:
- accessible capacity up;
- transition peak down;
- transition width up;
- t63 can increase.

## 2. Stage 1 — D-only negative control

The HEO reference values were used to define the single-D locus:

eta(D) = eta_HEO / sqrt(D/D_HEO)

t63(D) = t63_HEO / (D/D_HEO)

### Result

Best joint fits:

| Sample | best D/D_HEO | observed eta (mV) | D-only eta (mV) | observed t63 (min) | D-only t63 (min) | normalized residual |
|---|---:|---:|---:|---:|---:|---:|
| HEO | 1.000 | 160.9 | 160.9 | 8.68 | 8.68 | 0.000 |
| BM-HEO | 0.763 | 176.3 | 184.3 | 11.57 | 11.38 | 0.054 |
| Mg-HEO | 0.915 | 109.5 | 168.3 | 11.01 | 9.49 | 0.405 |
| BM-Mg-HEO | 0.725 | 144.3 | 188.9 | 12.99 | 11.97 | 0.302 |

### Important interpretation

D-only is **not strongly rejected by the BM median pair alone**. BM can lie relatively close to the D-only amplitude-time locus.

The strongest falsification is Mg:

- matching Mg amplitude requires D/D_HEO = 2.161;
- this predicts t63 = 4.02 min;
- observed t63 = 11.01 min.

Conversely:

- matching Mg t63 requires D/D_HEO = 0.789;
- this predicts relaxation amplitude = 181.2 mV;
- observed amplitude = 109.5 mV.

This directional contradiction is robust to the precise diffusion exponent as long as increasing D decreases both diffusion polarization and diffusion-relaxation time.

**Decision:** retain D-only as a negative-control model, not as the preferred physical description.

## 3. Stage 2 — state-distributed phase-transition polarization

The background-subtracted late-stage excess polarization was represented with an asymmetric Gaussian in normalized capacity z = Q/Qmax:

eta_PT(z) = A exp[-(z-mu)^2 / (2 sigma_side^2)]

This is a phenomenological representation of a distribution of local transition conditions, not a microscopic free-energy fit.

Fitted results:

| Sample | A_PT (mV) | center z | sigma_left | sigma_right | profile RMSE (mV) |
|---|---:|---:|---:|---:|---:|
| HEO | 71.46 | 0.780 | 0.186 | 0.087 | 1.14 |
| BM-HEO | 44.23 | 0.682 | 0.162 | 0.116 | 0.96 |
| Mg-HEO | 14.73 | 0.829 | 0.251 | 0.052 | 0.82 |
| BM-Mg-HEO | 20.62 | 0.672 | 0.254 | 0.127 | 0.51 |

**Result:** a distributed transition profile reproduces the empirical excess curves to approximately 0.5–1.1 mV RMSE.

**Boundary:** these profile parameters are descriptive; they are not uniquely identified nucleation energies or phase fractions.

## 4. Stage 3 — distributed structural relaxation

Structural relaxation was represented as a lognormal ensemble of exponential modes.

For each mode tau_i:

R_i(t) = exp(-t/tau_i)

The distribution width sigma_ln(tau) was treated as a hypothesis-level heterogeneity parameter and was not fitted as a unique microscopic observable.

Chosen widths for the first test:
- HEO: 0.25
- BM-HEO: 0.65
- Mg-HEO: 0.40
- BM-Mg-HEO: 0.75

For each assumed width, the median tau was solved to reproduce the measured finite-window t63.

**Important identifiability note:** many pairs of median tau and distribution width can reproduce the same t63. The model is therefore used for mechanistic sufficiency, not unique parameter extraction.

## 5. Stage 4 — real 600 s pulse + 3600 s rest model (Python v2)

Each structural mode is built during the actual 600 s GITT pulse:

build_i = 1 - exp(-600/tau_i)

and relaxes after current interruption:

R_i(t) = build_i exp(-t/tau_i)

The same experimental 3 s-to-3600 s t63 definition is then applied.

Python v2 parameters:

| Sample | median tau (s) | sigma_ln(tau) | transition-polarization scale (mV) | observed excess peak (mV) |
|---|---:|---:|---:|---:|
| HEO | 537 | 0.25 | 106.3 | 70.8 |
| BM-HEO | 950 | 0.65 | 94.3 | 44.1 |
| Mg-HEO | 741 | 0.40 | 29.0 | 15.9 |
| BM-Mg-HEO | 1247 | 0.75 | 54.4 | 21.1 |

### Interpretation of v2

Mg requires two independent changes:
1. much smaller transition-polarization scale;
2. slower structural relaxation.

This is exactly the behavior expected for:
- structural/thermodynamic stabilization that suppresses conversion extent;
- lower mobility of the residual structural rearrangement.

BM requires:
- lower concentrated transition scale;
- broader state distribution;
- broader/slower structural relaxation distribution.

This is consistent with:
- larger interface/accessibility;
- reduced effective domain/transport length;
- heterogeneous local strain/defects/nucleation conditions.

## 6. Literature constraint added during development

### Nanosizing does not necessarily increase phase-transition overpotential

Cogswell & Bazant phase-field theory shows that coherent nucleation barriers can decrease with area-to-volume ratio because surfaces permit wetting and elastic relaxation, and the barrier may vanish below a critical size.

- Cogswell & Bazant, ACS Nano 2012, DOI 10.1021/nn204177u.
- Cogswell & Bazant, Nano Letters 2013, DOI 10.1021/nl400497t.

### Direct spinel-HEO precedent

Li et al. compared ~150 nm and ~15 nm spinel-type HEOs and found that the nanosized material:
- shortened effective diffusion length;
- reduced GITT polarization;
- showed less pronounced plateaus;
- enabled more complete/reversible conversion.

Li et al., Angew. Chem. Int. Ed. 2025, 64, e202518569. DOI 10.1002/anie.202518569.

**Boundary for the present project:** the present BSE aggregate sizes are ~2 micrometers and do not prove 15 nm primary particles after ball milling. The literature is used only to support the general physical possibility that refinement can lower, rather than raise, transition polarization.

## 7. Model decision after Python v2

### What the model successfully establishes

- A single-D explanation fails for Mg.
- Mg stabilization-only is insufficient because it does not explain slower relaxation.
- Mg mobility-only is insufficient because it does not explain the smaller hump/polarization.
- Stabilization + lower residual structural mobility is sufficient to reproduce the observed direction of all key Mg observables.
- A distributed transition-state representation reproduces the measured late-stage excess profiles accurately.
- BM peak-down / width-up / t63-up is internally compatible with a broader distribution of transition conditions and structural relaxation times.

### What the model does NOT establish

- unique microscopic Mg site;
- unique phase-boundary mobility;
- unique nucleation energy;
- unique relaxation-time distribution;
- true nanoscale particle radius after ball milling;
- absolute phase fraction from the excess-polarization area.

## 8. Gate before MATLAB port

Python v2 passes the intended mechanistic-discrimination test.

The MATLAB port should therefore preserve:
1. the D-only negative control;
2. independent transition-strength and structural-mobility coordinates;
3. state-distributed transition conditions;
4. distributed relaxation times;
5. the real 600 s pulse + 3600 s rest protocol;
6. explicit non-identifiability warnings.

A higher-dimensional phase-field PDE should be added only if it produces a new discriminating prediction that can be checked against experiment. Do not add PDE complexity merely to make the model look more microscopic.

## 9. Files

Python/model artifacts generated in the working environment:
- heo_phase_transition_model_v1.py
- heo_phase_transition_model_v2.py
- HEO_model_donly_fit.csv
- HEO_model_donly_discriminator.png
- HEO_model_profile_fit.csv
- HEO_model_observed_excess.png
- HEO_model_modeled_excess.png
- HEO_model_relaxation_parameters.csv
- HEO_model_relaxation_kernels.png
- HEO_model_Mg_hypothesis_test.csv
- HEO_model_validation_summary.csv
- HEO_model_v2_pulse_rest_parameters.csv
- HEO_model_v2_mechanistic_parameters.csv
- HEO_model_v2_pulse_rest_relaxation.png
