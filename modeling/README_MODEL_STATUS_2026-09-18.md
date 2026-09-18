# HEO Modeling Status

**Date:** 2026-09-18

## Current authoritative implementation

Python spatial phase-field gate v2 is the current mechanistic-development reference.

Model level:
- spherical conserved Li field c(r,t);
- non-conserved structural order parameter phi(r,t);
- galvanostatic 600 s pulse;
- 3600 s zero-flux rest;
- Mg stabilization through c_tr shift plus lower M_phi;
- ball-milling heterogeneity through a distribution of local transition thresholds.

## File hierarchy

1. `heo_minimal_mechanistic_model_v3.py`
   - earlier 0D/ensemble hypothesis-discrimination model;
   - useful negative-control and logic model.

2. `heo_spatial_phase_field_gate_v2.py`
   - current spatial Python reference;
   - supersedes the minimal model for the next physics-development stage.

3. `HEO_PhaseTransition_Model_Final.m`
   - legacy/provisional MATLAB port of an earlier phenomenological model;
   - **not** the final MATLAB implementation;
   - do not extend until the Python spatial model is frozen.

## Current gate status

Passed:
- D-only directional contradiction for Mg;
- Mg stabilization + slow structural mobility sufficiency;
- BM peak-down / width-up from transition-condition heterogeneity;
- radial mesh/interface-width convergence for HEO and Mg;
- BM-Mg partial recovery without restoration of pristine HEO transformation.

Still required before MATLAB:
- elastic/coherency-energy test;
- surface-energy/wetting test;
- spatial parameter sensitivity;
- voltage-observable sensitivity;
- final decision on main text vs SI.
