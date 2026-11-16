# HEO — FEM/spatial simulation: open decision and proposed discriminator (2026-11-16)

**Not performed / no PI decision yet.** Last scientific question before the current GitHub archiving request was “시뮬레이션을 추가하는건 어떤가 fem이나” (“What about adding a simulation, e.g. FEM?”). It was **not answered with a completed design or execution** before the handoff request. This file preserves it as the next discussion topic, NOT a simulation result, PI-approved figure, or manuscript revision.

## Purpose of any simulation
The goal is to address a **specific ambiguity uncovered by cycle-resolved GITT analysis**, not to decorate the paper:
- The initial pristine-spinel C1 lithiation has extra throughput and complex nonmonotonic t63; C1 delithiation already resembles later delithiation more than C1 lithiation; C2/C3 lithiation repeats more closely.
- A voltage-rest-amplitude hump persists in C2/C3 even where t63 becomes monotone. The hump is an empirical landmark, not a charge maximum or unique reaction identity.
- The first C1 t63 R1–R4 segmentation is operationally useful, but local minima/slope reversals do not prove sharp individual reaction boundaries. Modified materials have moving operational boundaries.
- Does **initial-state memory / spinel-to-reconstructed-oxide evolution** suffice to produce these observations with the same baseline reaction/transport model? Or is a new reaction channel, active-material area/particle-size distribution, SEI, extra interfacial kinetics or potential-dependent thermodynamics required?

## Existing material in repository to inspect BEFORE writing code
- `modeling/HEO_SPATIAL_PHYSICS_GATE_V3_2026-09-18.md`, `modeling/HEO_Spatial_PhaseField_Model_Final.m`, `modeling/HEO_spatial_phase_field_frozen_v4.py`, `modeling/HEO_SPATIAL_PHASE_FIELD_GATE_V2_SUMMARY.csv` and `manuscript/HEO_DIFFUSION_VS_PHASE_TRANSITION_LOGIC_AND_SIMULATION_2026-09-18.md` (legacy spatial/phase-field attempts; audit their validation and failures).
- `modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_INFORMED_2026-09-25.md`, `modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`, `modeling/HEO_GITT_CONSTRAINED_CONVERSION_DYNAMICS_2026-09-22.md` (competing lumped mechanism families).
- Latest manuscript science authority / C1 pulse boundary record and **2026-11-16 cycle1–3 full continuity**. Do not resurrect an older simulation solely because it generates a visually plausible relaxation hump; previous studies may have concluded mechanistic non-uniqueness.

## Recommended scientific sequence for NEXT chat, pending PI discussion

**A. Test minimal null models FIRST.** A 0D/lumped kinetic model including coupled states `x_spinel`, `x_reconstructed_oxide`, `x_metal_Li2O` (and optional separately bounded SEI irreversible loss), total charge balance, potential-dependent response, and a finite rest-voltage kernel. Calibrate basic dynamics on C2/C3 **without using the held-out C1**; then vary C1 initial state. Competing nulls: (i) only a bulk capacity multiplier, (ii) only a voltage/QOCV shift, (iii) coupled modes with varying weights, (iv) state/history-dependent conversion. Require reproduction of the **direction and morphology of t63, |ΔErest| hump, QOCV, dQ/dV**, as well as C1/C2/C3 charge balance.

**B. Add spatial physics only if it changes discrimination or prediction.** A 1D radial reaction–diffusion/phase-front model (implemented by finite volume/finite elements, potentially using Python FEniCSx or MATLAB PDE Toolbox) can test effects of particle size, diffusion length, interfacial kinetics and spatially distributed reconstructed phases. For morphology/ball milling, compare *measured particle/aggregate distributions* if available rather than merely assuming BET converts one-to-one to electrolyte-active surface. For Mg, vary plausible reaction free energy/barrier/inactive fraction rather than asserting a proven Mg lattice site occupancy. A 2D/3D FEM model is optional and would require real morphology/geometry and validation sufficient to avoid parameter overfitting.

**C. Explicit discriminatory predictions.**
1. Does spatial/state-history modeling explain *first-only* nonmonotonic t63 and surviving later |ΔErest| hump **without** inventing discontinuous boundaries at all R1–R4?
2. Does it reproduce C1 initial extra 340–425 mAh/g and C1 delithiation capacity already close to C2/C3, while preserving accurate absolute QOCV and amplitude?
3. Does one morphology intervention account for BM's C1 R2 gain and later total charge advantage, and one chemistry intervention account for Mg's C1 R3 decrease and later ~0.90V local normalized charge/amplitude deficits, **without fitting those outcomes separately by hand**?
4. Compare held-out C1/C2/C3 pulse-rest waveforms, **not just derived summary t63**; examine identifiable parameter ranges and model selection/predictive cross-validation. A perfect fit produced by many free parameters is insufficient.
5. Can full model predict a different pulse duration/rest length or partial state protocol? If no independent validation, qualify as an existence proof rather than causal explanation.

**D. Numerical and evidence limitations to register.**
- A 3–3600 s voltage relaxation is not one diffusion coefficient: multi-exponential inverse modes are ill-conditioned and overflexible; no unique assignment of mode to metal oxide species or reaction step.
- Distinguish full-rest GITT vs terminal cutoff partial pulses, and GITT vs independent GCD curves. Same-cell C2/C3 are not independent replicates.
- First lithiation starts in pristine spinel; post-cycle delithiation/re-lithiation may start in a different structure. Literature supports that possibility, but direct proof for these four powders is absent.
- Need verified electrode loading and area, particle size distribution, crystallographic/porosity inputs, raw per-cycle current/voltage protocols, and ideally state-of-charge-resolved XRD/XAS/TEM if promoting mechanistic phase narrative.
- Domain choice: begin in Python/MATLAB with controlled equations and mesh-convergence tests. Use FEM only for **a spatially resolved physical question**, not because it is perceived as inherently more accurate.

## Manuscript gate
Do **not** add an FEM section, a new Figure, simulation-derived R1–R4 mechanism labels, or claims of validated Mg incorporation mechanisms without PI review of a concrete, held-out, falsifiable improvement relative to simpler models. Preserving a concise paper with region-based GITT modification contrasts is the default.

**Workflow:** update GitHub only when the PI explicitly requests. This note is created solely under the 2026-11-16 archiving request. Word and SI unchanged.
