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


---

## Spatial phase-field gate — 1D spherical c(r,t) + phi(r,t)

### Why this gate was added

The minimal v3 model established directional sufficiency but used prescribed relaxation branches. The next gate asks whether the same mechanistic directions emerge from spatially resolved conserved Li transport coupled to a non-conserved structural phase variable, without prescribing a state-localized hump by hand.

### Governing model

A dimensionless spherical free-energy density was defined as

f = c ln c + (1-c) ln(1-c)
    + W phi^2(1-phi)^2
    + K(c_tr-c) phi
    + (kappa/2)|grad phi|^2.

The Li chemical potential is

mu = ln[c/(1-c)] - K phi.

Li is conserved:

dc/dt = -div(J),
J = -D_eff grad(mu).

The structural order parameter is non-conserved:

dphi/dt = -M_phi [
    2W phi(1-phi)(1-2phi)
    + K(c_tr-c)
    - kappa laplacian(phi)
].

Boundary conditions reproduce the GITT protocol:
- spherical symmetry at r = 0;
- prescribed inward Li flux for 600 s;
- zero Li flux for 3600 s rest;
- zero-gradient structural boundary condition.

The voltage-like response is the volume-averaged Li chemical-potential proxy. Absolute voltage is not interpreted; only state dependence and directional changes are used.

### Numerical development failure: under-resolved diffuse interface

The first spatial prototype used kappa = 5e-4. At N = 18 radial finite-volume cells, the HEO transition peak moved to a different state and changed strongly relative to N = 30.

Interpretation:
the diffuse-interface scale sqrt(kappa/W) was not sufficiently resolved by the coarse mesh.

This result was treated as a failed numerical gate, not ignored.

### Mesh/interface-width correction

kappa was increased to 0.002 so that the diffuse interface is numerically resolved by the intended mesh.

HEO mesh check:

| N | peak proxy | c at peak | t63 at peak (min) | final phi |
|---:|---:|---:|---:|---:|
| 18 | 0.9815 | 0.676 | 8.857 | 1.0001 |
| 24 | 0.9650 | 0.676 | 7.961 | 1.0001 |
| 30 | 0.9877 | 0.676 | 7.961 | 1.0001 |
| 40 | 0.9993 | 0.676 | 7.961 | 1.0001 |

Mg mesh check:

| N | peak proxy | c at peak | t63 at peak (min) | final phi |
|---:|---:|---:|---:|---:|
| 18 | 0.2250 | 0.892 | 35.271 | 0.2451 |
| 24 | 0.2250 | 0.892 | 35.271 | 0.2451 |
| 30 | 0.2250 | 0.892 | 35.271 | 0.2451 |
| 40 | 0.2250 | 0.892 | 35.271 | 0.2451 |

Decision:
use N = 30 and kappa = 0.002 for the spatial-mechanism gate.

### Frozen hypothesis-level spatial cases

#### HEO
- D_eff/R^2 = 0.0015
- M_phi = 0.015
- c_tr = 0.60
- W = 0.60
- K = 1.80

This gives a relatively sharp transformation localized near c_bar ~ 0.676.

#### Mg-HEO
- c_tr increased to 0.79;
- M_phi reduced to 0.001;
- W increased modestly to 0.80;
- transport scale otherwise kept HEO-like.

Physical meaning:
Mg stabilizes the parent/intermediate structure and lowers structural mobility.

Result:
- transformed fraction after the simulated lithiation window drops from ~1.00 to ~0.245;
- peak relaxation proxy drops strongly;
- the remaining transition occurs later;
- transition-local t63 becomes substantially longer.

This spatial model therefore reproduces the qualitative combination:
smaller transformation extent + smaller transition-associated response + slower residual structural response.

#### BM-HEO
BM is represented as an ensemble rather than one smaller homogeneous particle.

Common BM changes:
- D_eff/R^2 increased to 0.0030;
- W reduced to 0.50;
- K = 1.60.

Local transition thresholds are distributed:
c_tr = [0.48, 0.54, 0.60, 0.66, 0.72]
with weights [0.1, 0.2, 0.4, 0.2, 0.1].

Reason:
a smaller effective transport/domain scale alone makes the transition easier but does not naturally generate the experimentally observed broad state interval. Broadening requires heterogeneous local transition conditions, consistent with ball-milling-induced distributions of strain, defects, coherent-domain size, and local nucleation environments.

Result:
- concentrated peak decreases strongly relative to HEO;
- the feature spans multiple state increments;
- the final transformed fraction remains ~1;
- the ensemble transition is broader and slower than the sharp HEO event.

#### BM-Mg-HEO
Mg stabilization is retained, but the transition threshold is broadened by milling:

c_tr = [0.64, 0.71, 0.78, 0.85, 0.92].

Result:
- final transformed fraction rises from ~0.245 for Mg-HEO to ~0.446;
- the transition response partially re-emerges and broadens;
- it remains far below the complete HEO transformation.

This reproduces the experimental internal-control logic:
ball milling can reopen/access more of the Mg-containing conversion pathway without eliminating the compositional stabilization imposed by Mg.

### Spatial gate v2 summary

| Sample | peak proxy | c at peak | FWHM in c | t63 at peak (min) | final transformed fraction |
|---|---:|---:|---:|---:|---:|
| HEO | 0.9877 | 0.676 | < one GITT state step | 7.96 | 1.000 |
| BM-HEO | 0.4162 | 0.676 | 0.108 | 10.96 | 1.000 |
| Mg-HEO | 0.2250 | 0.892 | < one GITT state step | 35.27 | 0.245 |
| BM-Mg-HEO | 0.2612 | 0.856 | 0.108 | 31.72 | 0.446 |

Important:
the HEO and Mg FWHM values are reported as narrower than the discrete simulated GITT state increment, not as physically zero-width transitions.

### What this spatial gate supports

1. A sharp phase-transition-associated relaxation feature can emerge from coupled conserved Li transport and non-conserved structural dynamics without inserting a Gaussian hump directly into the voltage response.
2. Mg-like stabilization plus reduced structural mobility can simultaneously reduce transformation extent and delay/slow the residual transition.
3. Ball-milling-like broadening requires heterogeneity in local transition conditions in addition to a shorter effective transport/domain scale.
4. BM-Mg can partially recover transformed fraction without restoring the pristine HEO transition.
5. The original qualitative mechanism survives a spatial model after mesh convergence is enforced.

### What it does not yet establish

- unique free-energy coefficients;
- an absolute phase fraction for the real HEO;
- an absolute interfacial energy;
- actual particle radius after milling;
- unique Mg-induced change in M_phi;
- quantitative voltage fitting;
- unique elastic-strain contribution.

The current parameters remain hypothesis-level coordinates.

### Next physics gate before MATLAB

Before a new MATLAB implementation is written, Python should test whether the directional conclusions survive:
- explicit elastic/coherency energy;
- surface-wetting or surface-energy terms;
- moderate changes in c_tr distribution shape;
- alternative voltage observables (surface vs volume-averaged chemical potential);
- parameter perturbations around the converged spatial solution.

Only after those checks should the spatial equations be frozen for MATLAB translation.

### MATLAB status correction

The existing file modeling/HEO_PhaseTransition_Model_Final.m is an earlier translation of the phenomenological/minimal model. It predates the spatial c(r,t)+phi(r,t) gate.

It is therefore **legacy/provisional**, not the final spatial MATLAB model.

Do not extend or use it as the final mechanistic implementation until the Python spatial model is frozen.
