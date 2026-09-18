# HEO Modeling Development Log

**Date:** 2026-09-18
**Status:** Python minimal model v3 passes directional/robustness gate; MATLAB translation deferred until Python science is frozen.

## Scientific question

Can the observed combination of GITT features be explained by a single Li-diffusion parameter, or does it require an independently controlled phase-transition contribution?

Observed constraints:

- Mg: relaxation/polarization amplitude decreases, late-stage excess hump strongly decreases, accessible conversion capacity decreases, but t63 becomes longer rather than shorter.
- BM: accessible capacity increases, late-stage peak decreases and broadens, and long-rest t63 becomes longer.
- BM-Mg: milling increases utilization but does not restore the strong pristine-HEO transition hump.

## Model philosophy

This model is a **hypothesis-discrimination model**, not a unique parameter fit.

The goal is not to claim that fitted parameters are physical material constants. The goal is to ask which minimum set of independent physical coordinates is required to reproduce the directions of the observables.

The model separates:

1. diffusion-like relaxation;
2. broad background relaxation not uniquely assigned to the transition;
3. a state-localized phase-transition excess contribution.

The total current-off relaxation is represented phenomenologically as:

eta(t,z) = eta_D(t) + eta_BG(t) + eta_PT(t,z)

where z is normalized first-lithiation capacity.

## Physical logic tested

### D-only hypothesis

Under otherwise comparable pulse conditions,

- diffusion polarization amplitude decreases as D increases;
- diffusion relaxation time also decreases as D increases;
- tau_D scales approximately as L^2/D.

Therefore one D cannot naturally produce **smaller polarization together with slower relaxation**.

This is used as a direction test, not as a claim that the real electrode is governed by an exact single power law.

### Mg: stabilization-only hypothesis

Lower the amplitude/fraction of the phase-transition contribution while retaining the HEO structural mobility.

Result:
- hump decreases;
- capacity proxy decreases;
- total relaxation does not become sufficiently slower.

Conclusion: stabilization is necessary for hump/capacity suppression but does not by itself reproduce the observed t63 trend.

### Mg: mobility-only hypothesis

Slow the broad structural/phase relaxation while retaining the original transition extent.

Result:
- t63 increases;
- transition hump remains large.

Conclusion: slower mobility alone cannot explain the smaller Mg hump. If the same transformation were forced to proceed at the same current, slower mobility would tend to require greater, not smaller, transformation driving overpotential.

### Mg: stabilization + slower residual structural mobility

Decrease transition extent/amplitude and increase the characteristic time of the remaining structural relaxation.

Result:
- hump decreases;
- accessible conversion capacity proxy decreases;
- total relaxation becomes slower.

This is the minimum tested combination that reproduces all three Mg directions simultaneously.

### Ball milling

Represent BM by:

- larger accessible-capacity factor;
- broader distribution of local transition conditions (larger sigma);
- smaller concentrated transition peak;
- slower/broader structural background relaxation;
- slightly reduced effective diffusion time scale.

Result:
- peak decreases;
- width increases;
- accessible capacity increases;
- ensemble t63 can increase.

This demonstrates that lower local transition polarization and slower ensemble relaxation are not contradictory when local transition conditions and relaxation times are distributed.

## Development history

### v0 — conceptual equations

Started with diffusion + phase-transition contributions and the expectation that D-only would couple amplitude and time.

### v1 — pulse-driven transition ensemble

Implemented distributed local transition centers and structural relaxation times. The first scale choice produced phase-transition amplitudes orders of magnitude too large.

Decision:
- retain model structure;
- reject the original forcing scale.

### v2 — rescaled distributed model

Rescaled forcing to obtain tens-of-mV phase-transition amplitudes.

Finding:
- transition peak trends were reproduced;
- however, after strong Mg suppression of the transition hump, total t63 became dominated by the faster background/diffusion contribution and became too short.

Interpretation:
- the experimental 60-min relaxation contains a substantial background response in addition to the late-stage excess hump;
- a model containing only diffusion + localized transition excess is insufficient to represent the measured t63.

Decision:
- add a broad background relaxation coordinate rather than artificially forcing the small transition hump to control the entire 60-min response.

### v3 — diffusion + broad background + phase-transition excess

Components:
- eta_D: diffusion-like branch;
- eta_BG: broad relaxation background;
- eta_PT: state-localized transition excess.

Working parameter values were chosen to reproduce the **observed direction and approximate scale**, not by nonlinear fitting.

Observed versus v3 model, transition window:

| Sample | Observed DeltaErelax (mV) | Model (mV) | Observed t63 (min) | Model (min) | Observed PT peak (mV) | Model (mV) |
|---|---:|---:|---:|---:|---:|---:|
| HEO | 160.9 | 158.6 | 8.68 | 8.58 | 70.8 | 69.7 |
| BM-HEO | 176.3 | 176.5 | 11.57 | 11.56 | 44.1 | 41.8 |
| Mg-HEO | 109.5 | 108.6 | 11.01 | 11.16 | 15.9 | 14.4 |
| BM-Mg-HEO | 144.3 | 143.0 | 12.99 | 12.90 | 21.1 | 18.8 |

These agreements are **construction/closure**, not independent validation.

## Robustness test

1000 Monte-Carlo trials with all positive v3 parameters independently perturbed by ±15%.

Directional criteria preserved in 100% of trials:

- Mg DeltaErelax lower than HEO;
- Mg t63 longer than HEO;
- Mg PT peak lower than HEO;
- BM PT peak lower than HEO;
- BM transition width broader than HEO;
- BM t63 longer than HEO;
- BM-Mg PT peak remains below HEO;
- BM-Mg t63 remains longer than HEO.

Interpretation:
the qualitative conclusions do not depend on fine tuning around the current working parameter set.

This still does **not** establish unique parameters or prove the microscopic mechanism.

## Literature basis added to the model logic

- Cogswell & Bazant, ACS Nano 2012, DOI 10.1021/nn204177u: coherency strain changes nanoscale phase-separation thermodynamics and kinetics.
- Cogswell & Bazant, Nano Letters 2013, DOI 10.1021/nl400497t: coherent nucleation barrier decreases with increasing area/volume and can vanish below a critical size.
- Li et al., Angew. Chem. Int. Ed. 2025, DOI 10.1002/anie.202518569: ~15 nm spinel-type HEO shows reduced kinetic limitation and more complete phase transformation compared with ~150 nm HEO.
- Komayko et al., J. Power Sources 2024, DOI 10.1016/j.jpowsour.2024.235589: nucleation can make a major material-level contribution to phase-transition overpotential.
- Jin et al., Materials Today Chemistry 2025, DOI 10.1016/j.mtchem.2025.102949: direct spinel -> mixed spinel/rock-salt -> rock-salt pathway in the five-cation spinel family.

## Python-to-MATLAB gate

Do not translate to MATLAB yet unless all of the following are satisfied:

- D-only directional contradiction is retained under reasonable scaling assumptions.
- Mg stabilization-only and mobility-only remain individually insufficient.
- combined Mg stabilization + slower structural mobility remains sufficient over sensitivity ranges.
- BM peak-down / width-up result remains robust to transition-distribution assumptions.
- model parameters are explicitly labeled phenomenological unless independently identified.
- decision is made whether the model belongs in main text, SI, or only mechanistic development notes.

After this gate, reproduce the frozen Python equations in MATLAB using the same test cases and unit tests before developing the more physical radial phase-field model.

## Next model level

Only after the minimal model is frozen:

- conserved Li concentration c(r,t);
- nonconserved structural order parameter phi(r,t);
- free-energy term for phase stability;
- gradient/interfacial energy;
- optional elastic energy;
- Mg stabilization term;
- structural mobility M_phi;
- galvanostatic 600 s pulse and 3600 s zero-flux rest.

Preferred implementation path:
radial finite difference + method of lines + stiff solver.

Python first; MATLAB only after the Python equations and parameter roles are frozen.
