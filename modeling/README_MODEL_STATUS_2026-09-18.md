# HEO Modeling Status

**Updated:** 2026-09-23

## Current modeling hierarchy

### 1. Current Figure 7 candidate — authoritative mechanistic interpretation

`HEO_CONVERSION_MICROKINETICS_2026-09-23.md`  
`heo_conversion_microkinetics_electrochemical_growth.py`

Purpose:
- explain amplitude–timescale decoupling and cycle-history dependence using a minimal multi-step conversion network;
- test mechanistic consistency;
- **not** assign a unique microscopic RDS.

Effective network:
- electrochemical activation A <-> B
- effective nucleation/activity evolution B -> N
- electrochemical phase growth B <-> P

At current off:
- j_ext = r1 + r3 = 0
- internal r1 = -r3 != 0 is permitted

Core conclusion:
a simple single-step RC picture is insufficient, while internal-state nucleation/growth-type dynamics are physically compatible with the data.

### 2. Current Figure 6 — experimental, not primarily a model

`HEO_CYCLE_RESOLVED_GITT_AND_BACKGROUND_AUDIT_2026-09-23.md`

Figure 6 now uses cycle-resolved GITT to show that conversion-associated relaxation is history-dependent. The strongest cycle effect is in response amplitude/population rather than a comparable change in t63.

### 3. 2026-09-22 distributed-threshold model — historical/exploratory

`HEO_GITT_CONSTRAINED_CONVERSION_DYNAMICS_2026-09-22.md`  
`heo_gitt_constrained_conversion_dynamics.py`

Useful insight:
reaction-state distribution and relaxation speed can play different roles.

Current status:
- not the preferred main Figure 6;
- X is not capacity or phase fraction;
- Q×X is not a valid capacity prediction;
- high-rate rate-capability behavior was not reproduced satisfactorily;
- cycle-resolved experiments provide a stronger Figure 6.

### 4. Older spatial phase-field models — historical only

Files include:
- `HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md`
- `heo_spatial_phase_field_frozen_v4.py`
- earlier MATLAB/spatial variants

These are not in the current revised Main/SI.

Do not reinsert them by default.

## Modeling constraints

- do not turn the paper into a GITT-method paper;
- do not call t63 a local microscopic time constant;
- do not infer unique conversion fraction from hump amplitude;
- do not assign a unique nucleation/growth RDS;
- do not say charge transfer is absent;
- safe negative-control statement: **a simple single-step RC description is insufficient**;
- safe model-purpose statement: **the model tests mechanistic consistency rather than assigning a unique elementary rate-limiting step**.
