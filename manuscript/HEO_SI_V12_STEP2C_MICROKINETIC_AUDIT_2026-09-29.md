# HEO SI v12 Step 2C — Four-Step Microkinetic Audit

**Date:** 2026-09-29  
**Status:** Figures S21–S23 complete and frozen.

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


## Figure S22 — fixed-R2 line cuts through the R2–R3 map

Purpose: unpack the two-dimensional regime map in main Figure 6b without reproducing that map.

Figure S22 panels:
- (a) normalized cutoff capacity, Qcutoff/Q0, versus R3 rate scale at four fixed R2 scales;
- (b) normalized relaxation timescale, t63/t63,0, versus the same R3 sweep.

Exact fixed R2 scales:
- 0.406063
- 0.464961
- 0.532402
- 0.698051

Finite Q↑/t63↑ intervals along these line cuts:

| R2 scale | R3 interval with Q/Q0 > 1 and t63/t0 > 1 | Q/Q0 range | t63/t0 range |
|---:|---:|---:|---:|
| 0.406063 | 8.498–50 | 1.005–1.042 | 1.200–1.211 |
| 0.464961 | 3.175–50 | 1.000–1.111 | 1.076–1.097 |
| 0.532402 | 2.141–2.607 | 1.003–1.034 | 1.009–1.041 |
| 0.698051 | none | — | — |

Interpretation:
- When R2 is slowed strongly enough, increasing R3 first recovers and then raises cutoff capacity while the slow current-off mode can remain longer than the reference.
- The Q↑/t63↑ regime is finite rather than generic.
- At R2≈0.532 the overlap is narrow; at R2≈0.698 the relaxation becomes faster before the capacity increase can coexist with a longer t63.
- The anomaly therefore requires coordinated step-selective changes rather than uniform acceleration or simple slowing of one step.
- The line cuts are a sensitivity/existence audit, not a material-specific assignment of R2 and R3 to ball milling.

## Non-redundancy versus main Figure 6b

Main Figure 6b shows the full 2D R2–R3 regime map and the boundaries Q/Q0=1 and t63/t0=1.
Figure S22 instead shows one-dimensional cuts through that map, making the origin and finite width of the higher-capacity/slower-relaxation region explicit.

Current final artwork:
- `Figure_S22_R2_fixed_linecuts_final.png`

Current numerical summary:
- `Figure_S22_R2_fixed_linecuts_summary.csv`


## Figure S23 — eigenmode spectrum and partial-rate audit

Purpose: provide the internal kinetic diagnostics behind main Figure 6d without repeating the main voltage-relaxation curves.

Representative cases:
- reference model;
- step-selective case (R_2\times0.465, R_3\times50), which lies in the higher-capacity/slower-relaxation regime.

### Panel (a): finite current-off eigen-timescales

Reference finite modes:
- slowest: 15.35 min;
- intermediate: 5.96 min;
- fast: 0.482 min.

(R_2\times0.465, R_3\times50):
- slowest: 17.68 min;
- intermediate: 0.584 min;
- fast: 0.183 min.

Thus the slowest internal mode becomes longer even while the faster internal modes accelerate strongly. The model therefore does not possess one common kinetic acceleration factor governing the full current-off response.

### Panel (b): partial rates at pulse end and 3 s after current interruption

At the 3 s open-circuit state:

Reference:
- (r_1=-5.0\times10^{-5});
- (r_2=1.13\times10^{-4});
- (r_3=7.4\times10^{-5});
- (r_4=+5.0\times10^{-5}).

Representative step-selective case:
- (r_1=-6.2\times10^{-5});
- (r_2=1.03\times10^{-4});
- (r_3=9.1\times10^{-5});
- (r_4=+6.2\times10^{-5}).

For both cases, (r_1+r_4\approx0) at open circuit while (r_2) and (r_3) remain finite. Zero external Faradaic current therefore does not require all internal conversion-network rates to vanish.

Interpretation:
- the representative (Q\uparrow/t_{63}\uparrow) case lengthens the slowest internal relaxation mode;
- at the same time, the network retains substantial internal redistribution after current interruption;
- faster and slower internal modes shift in opposite directions;
- this provides the mechanistic audit for the main-text statement that greater downstream reaction throughput can coexist with a slower dominant current-off mode.

The partial rates and eigenmodes are model diagnostics, not experimentally extracted microscopic rates or uniquely assigned HEO elementary steps.

## Non-redundancy versus main Figure 6d

Main Figure 6d shows only the observable current-off voltage relaxation for the reference and representative step-selective case.
Figure S23 instead exposes:
- the finite eigenmode spectrum;
- the sign and magnitude of the four partial rates at pulse end and immediately after current interruption.

Current final artwork:
- `Figure_S23_eigenmode_partial_rate_audit_final.png`

Current numerical summaries:
- `Figure_S23_eigenmode_summary.csv`
- `Figure_S23_rest3_partial_rate_summary.csv`

## Step 2C completion

Figures S21–S23 now provide SI-only mechanistic audits and do not reproduce main Figure 6 panels directly.
