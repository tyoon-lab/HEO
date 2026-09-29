# HEO SI v12 Step 2C — Four-Step Microkinetic Audit

**Date:** 2026-09-29  
**Status:** Figure S21 complete and frozen; Figures S22–S23 pending.

## Figure S21 — full single-step rate sweeps

Purpose: provide the detailed rate-scale dependence underlying main Figure 6a without duplicating the main Q–t63 observable-space summary.

Each effective step R1–R4 is varied independently over the same 0.1×–10× range used in the current four-step model while all other kinetic and equilibrium parameters are held fixed.

Figure S21 panels:
- (a) normalized cutoff capacity, Qcutoff/Q0, versus individual rate scale;
- (b) normalized relaxation timescale, t63/t63,0, versus the same rate scale.

Representative 0.1× results:
- R1: Q/Q0 ≈ 0.893, t63/t0 ≈ 0.959;
- R2: Q/Q0 ≈ 0.351, t63/t0 ≈ 2.437;
- R3: Q/Q0 ≈ 0.495, t63/t0 ≈ 1.573;
- R4: Q/Q0 ≈ 0.907, t63/t0 ≈ 1.058.

Representative 10× results:
- R1: Q/Q0 ≈ 1.010, t63/t0 ≈ 0.997;
- R2: Q/Q0 ≈ 1.183, t63/t0 ≈ 0.952;
- R3: Q/Q0 ≈ 1.325, t63/t0 ≈ 0.530;
- R4: Q/Q0 ≈ 1.009, t63/t0 ≈ 1.003.

Interpretation:
- R2 and R3 dominate the capacity/timescale response under the representative parameter set.
- Slowing R2 or R3 individually gives the conventional combination Q↓ and t63↑.
- R1 and R4 perturb the observables much less.
- Therefore the experimental BM-HEO Q↑/t63↑ ordering cannot be reproduced by simply slowing one isolated step in this representative homogeneous sequence.
- This is a sensitivity result for the representative model, not identification of a unique rate-determining step in the HEO electrode.

## Non-redundancy versus main Figure 6a

Main Figure 6a collapses each one-dimensional rate sweep into normalized Qcutoff–t63 observable space.
Figure S21 instead exposes the underlying independent-variable dependence, showing which step perturbations control capacity and which control current-off timescale.

Current final artwork:
- `Figure_S21_full_single_step_sweeps_final.png`

Current numerical summary:
- `Figure_S21_single_step_sweep_summary.csv`

## Next

Figure S22 — fixed-R2 line cuts through the R2–R3 map, showing explicitly how R3 acceleration crosses the capacity boundary while the t63 response depends on the selected R2 scale.

Figure S23 — eigenmode spectrum and partial-rate audit for the reference and representative R2×0.465/R3×50 case.
