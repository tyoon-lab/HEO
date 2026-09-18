# Final MATLAB Spatial Port

**Date:** 2026-09-18

## Status

The frozen Python spatial physics model has been translated to:

\`modeling/HEO_Spatial_PhaseField_Model_Final.m\`

The older \`HEO_PhaseTransition_Model_Final.m\` remains legacy/provisional and represents the earlier phenomenological model.

## MATLAB implementation

The final MATLAB port preserves:

- spherical finite-volume geometry;
- conserved Li chemical-potential transport;
- nonconserved Allen-Cahn structural order parameter;
- explicit Mg stabilization energy;
- reduced coherency and surface-wetting terms;
- 600 s pulse + 3600 s rest;
- refined state increment using \(j=9\times10^{-6}\) and 50 states;
- volume-averaged and surface chemical-potential voltage proxies;
- 11-quantile Gaussian joint distributions for BM and BM-Mg;
- polarization-weighted moment width;
- directional unit tests for the four-sample mechanism.

## Frozen Python target

Volume-\(\mu\) target used for comparison:

| Sample | peak / HEO | moment width | t63 at peak | final phi |
|---|---:|---:|---:|---:|
| HEO | 1.000 | 0.06825 | 22.03 min | 1.00015 |
| BM-HEO | 0.23658 | 0.08468 | 26.91 min | 1.00015 |
| Mg-HEO | 0.13590 | 0.03081 | 40.17 min | 0.21436 |
| BM-Mg-HEO | 0.18829 | 0.04977 | 40.17 min | 0.82411 |

The MATLAB file prints this reference table and asserts the directional relations rather than hard-coding an exact numerical-fit requirement.

## Runtime verification status

The current execution environment contains neither MATLAB nor Octave. Therefore:

- the MATLAB source has been translated structurally from the frozen Python equations;
- it has not been executed in this environment;
- the first local MATLAB run must confirm the directional unit tests and compare the printed summary against the frozen Python snapshot.

If small absolute numerical differences arise from \`ode15s\` solver behavior, the directional tests are the primary gate. Large changes in ordering should be treated as a translation/numerical bug, not refitted away.
