# HEO four-step operating-polarization audit — 2026-10-01

## Question

For the representative BM-like four-step perturbation (R2 x 0.465, R3 x 50), does the higher cutoff-accessible capacity arise mainly from a smaller instantaneous current polarization, and can this coexist with slower post-interruption relaxation?

## Reconstruction/validation

The original production script used for the frozen SI-v13 four-step CSV files was not committed. The model equations were reconstructed from the frozen SI definitions and parameters:

- O <-> I <-> J <-> K <-> C
- R1 and R4 reversible electrochemical steps
- R2 and R3 reversible first-order internal steps
- k1 = 0.020
- k2f/k2r = 0.00200/0.00141421356
- k3f/k3r = 0.00100/0.00070710678
- k4 = 0.010
- u4 = -3
- japp = 2e-4
- Ecut = 0.020
- matched-state relaxation at DeltaQ = 0.30

The reconstruction reproduces the frozen representative response closely:
- frozen Q ratio: 1.11067; reconstructed: 1.11588
- frozen t63 ratio: 1.0867; reconstructed: 1.08682
- frozen reference slow eigenmode: 15.35 min; reconstructed: 15.36 min
- frozen BM-like slow eigenmode: 17.68 min; reconstructed: 17.83 min
- frozen and reconstructed 3 s partial rates agree within a few percent.

Therefore the following operating-polarization decomposition is suitable as a mechanistic audit, but the original production script should be recovered before treating the absolute numerical values as final submission authority.

## Definition

At each current-on state x(Q):

E_on(Q) = E[x(Q), japp]

E_0(Q) = E[x(Q), j=0]

eta_op(Q) = E_on(Q) - E_0(Q)

This compares the current-on potential with the instantaneous zero-current potential at the SAME internal state, so it separates the current-induced voltage displacement from changes in the internal-state trajectory.

## Result

Reference cutoff charge:
Qcut,ref = 0.99920

BM-like cutoff charge:
Qcut,BMlike = 1.11499

Thus:
Qcut,BMlike/Qcut,ref = 1.11588

Matched-state post-interruption relaxation:
t63,BMlike/t63,ref = 1.08682

Across the common charge interval, the magnitude of eta_op is only modestly lower in the BM-like case (approximately 6% lower in the sampled common range).

At the reference cutoff charge Q = 0.99920:
- reference E_on = 20.000 mV
- reference E_0 = 20.933 mV
- reference eta_op = -0.933 mV
- BM-like E_on = 23.962 mV
- BM-like E_0 = 24.826 mV
- BM-like eta_op = -0.864 mV

Therefore the BM-like case has 3.962 mV of voltage headroom relative to the reference at the charge where the reference reaches cutoff.

Decomposition of that headroom:
- difference in instantaneous zero-current state voltage: +3.893 mV (~98.3%)
- difference in current-induced polarization: +0.069 mV (~1.7%)

## Interpretation

For this representative four-step model, the higher cutoff-accessible capacity is NOT produced mainly by a large reduction in the instantaneous current polarization. It arises predominantly because the step-selective kinetics drive a different internal-state trajectory, which keeps the zero-current state voltage farther from the cutoff at the same passed charge.

This supports the following qualitative picture:

1. In a single-state reaction with the same thermodynamic trajectory, larger polarization causes earlier cutoff and lower accessible capacity.
2. In a multistep conversion network, the kinetics also determine how the passed charge is distributed among internal intermediate/product states.
3. Therefore two systems at the same total passed charge can have different zero-current state voltages even if their instantaneous current polarizations are similar.
4. The system with the more favorable internal-state trajectory can reach a larger total converted charge before cutoff.
5. After current interruption, that same state distribution can still contain a slower collective redistribution mode, giving a longer t63.

Thus the physically important distinction is not “large polarization can give larger capacity.” It cannot, all else being equal. The distinction is that in a multistep conversion reaction, kinetics can change BOTH the operating polarization and the state trajectory; cutoff capacity depends on the full loaded voltage trajectory, while t63 probes post-interruption equilibration.

## Consequence for Figure 6

A stronger Figure 6 should explicitly show:
- reference and BM-like E_on(Q);
- instantaneous E_0(Q) at the same internal states;
- eta_op(Q) = E_on - E_0;
- the longer current-off relaxation/eigenmode.

The central message becomes:

**Step-selective kinetics can change the internal conversion-state trajectory enough to increase cutoff-accessible reaction extent while simultaneously lengthening a post-interruption collective relaxation mode.**

This is more precise than saying simply that a reaction can be “easier to drive but slower to equilibrate.”
