# HEO Spatial Physics Gate v3

**Date:** 2026-09-18  
**Status:** Python physics gate passed qualitatively; MATLAB spatial port still deferred.

## Purpose

Test whether the previously proposed HEO/BM/Mg mechanism survives after adding explicit reduced coherency energy, surface wetting, and an Mg stabilization free-energy term to the 1D spherical c(r,t)+phi(r,t) model.

## Free energy

The spatial model now uses

```
f = c ln c + (1-c) ln(1-c)
  + W phi^2(1-phi)^2
  + K(cstar-c)phi
  + G_Mg phi
  + 0.5 B_el q_el(r) phi^2
  - S_surf w_surf(r) phi
  + 0.5 kappa |grad phi|^2
```

with

```
q_el(r) = 1 - exp[-(1-r)/ell_relief]
w_surf(r) = exp[-(1-r)/ell_wet]
```

The reduced elastic term penalizes transformation in the coherent interior while allowing partial relief near the particle surface. The wetting term lowers the transformed-phase free energy near the surface.

**Boundary:** this is still a reduced isotropic coherency-energy representation, not a full solution of mechanical equilibrium.

The Mg effect is now explicit through `G_Mg > 0`; `cstar` is held fixed between HEO and Mg. Therefore Mg stabilization is no longer represented by an ad hoc shift of the transition composition.

## Main result

Final hypothesis-level cases:

| Sample | peak proxy | c at peak | FWHM in c | t63 at peak (min) | final transformed fraction |
|---|---:|---:|---:|---:|---:|
| HEO | 0.7456 | 0.640 | < one state step | 7.09 | 1.000 |
| BM-HEO | 0.2970 | 0.604 | 0.180 | 17.73 | 1.000 |
| Mg-HEO | 0.1844 | 0.892 | < one state step | 37.97 | 0.226 |
| BM-Mg-HEO | 0.1973 | 0.892 | 0.072 | 37.97 | 0.490 |

Absolute amplitudes and times are not fitted to experiment. Only directional behavior is interpreted.

## New conclusion 1 — BM broadening requires heterogeneity

A single BM-like particle with:
- larger D_eff/R^2,
- larger surface-relief zone,
- explicit surface wetting,
- lower local barrier,

shows a somewhat smaller peak but still a narrow transition.

A BM ensemble with a distribution of local surface/defect wetting strengths gives:
- much lower ensemble peak;
- broad FWHM in state;
- complete overall conversion.

Ablation:

| Case | peak proxy | FWHM in c |
|---|---:|---:|
| HEO | 0.7456 | < state step |
| BM single local condition | 0.6693 | < state step |
| BM heterogeneous surface conditions | 0.2970 | 0.180 |

Therefore **nanosizing/surface relief alone is insufficient to explain the experimental peak-down + width-up result**. Milling-induced heterogeneity in local surface/defect/strain conditions is required in the present model.

This sharpens the BM interpretation:

```
BM
-> shorter effective transport/domain scale
 + easier surface-assisted transformation
 + heterogeneous local transition environments
-> higher utilization + lower concentrated peak + broader transition interval
```

## New conclusion 2 — Mg stabilization and mobility are independent controls

The explicit Mg free-energy penalty and structural mobility were ablated separately.

- **stabilization only:** strongly suppresses transformation extent, but the remaining relaxation is fast;
- **mobility only:** makes relaxation very slow, but most of the material still transforms and the transition response remains appreciable;
- **stabilization + lower mobility:** suppresses transformed fraction and peak while also slowing the residual transition.

Thus the previous two-coordinate Mg interpretation survives the spatial physics gate without shifting cstar:

```
Mg
-> positive stabilization free energy G_Mg
 + lower structural mobility M_phi
-> smaller transformed fraction / conversion capacity
 + smaller transition-associated polarization
 + slower residual structural relaxation
```

## Numerical check

N = 18, 24, and 30 give stable transition locations and closely similar peak/final-fraction results for both HEO and Mg after the diffuse-interface correction introduced in spatial gate v2.

## Literature connection

Cogswell and Bazant show that coherency strain can suppress phase separation, elastic relaxation occurs near particle surfaces, and surface wetting can reduce nucleation overpotential in nanoparticle phase transformations. The present reduced terms are qualitative representations of those physical effects, not a parameterization of LiFePO4 physics for HEO.

- Cogswell & Bazant, ACS Nano 2012, DOI 10.1021/nn204177u.
- Cogswell & Bazant, Nano Letters 2013, DOI 10.1021/nl400497t.

## Decision after gate v3

The core mechanism survives, but the BM statement should now be more specific:

**Do not say only that smaller particles reduce the phase-transition barrier.**
Instead state that milling can facilitate local transformation through surface/strain relaxation while simultaneously generating a distribution of local transition conditions; the latter is required to explain the broad low-amplitude ensemble response.

For Mg, retain the two-coordinate interpretation:
- thermodynamic/structural stabilization controls transformation extent;
- structural mobility controls the relaxation time of the remaining transformation.

## Next gate

Before MATLAB translation:
1. test surface versus volume-averaged chemical-potential voltage observables;
2. perturb the new physics parameters around the v3 solution;
3. test alternative heterogeneity distributions (Gaussian/lognormal rather than five discrete surface-energy states);
4. decide whether the spatial model adds enough manuscript value for main text or should remain SI/mechanistic support.

Only then freeze the Python equations for MATLAB.
