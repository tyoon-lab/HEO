# HEO Mg-like Microkinetic Directional Test

**Date:** 2026-09-26  
**Role:** secondary mechanistic-consistency test for the Mg experimental combination; not a fit and not a microscopic assignment to Mg.

## 1. Experimental combination being tested

Relative to HEO, Mg-HEO shows the directional combination

- lower accessible capacity;
- lower first-cycle conversion-associated relaxation amplitude;
- longer effective relaxation time, \(t_{63}\).

The purpose of this calculation is only to test whether

\[
Q_{\rm cutoff}\downarrow,\qquad
\Delta E_{\rm relax}\downarrow,\qquad
t_{63}\uparrow
\]

can coexist within the same coarse-grained multistep conversion network.

## 2. Model and protocol

The current literature-informed network is retained:

\[
O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C.
\]

R1 and R3 are reversible Faradaic steps and R2 is the coarse-grained structural/reconstruction coordinate.

The reference parameter set is the same as in
`modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_INFORMED_2026-09-25.md`.

For this secondary directional test:

- reference accessible-population weight: 0.65;
- total normalized applied current: \(2\times10^{-4}\);
- voltage cutoff is fixed at the value that gives reference \(Q_{\rm cutoff}=0.55845\);
- current-off relaxation is evaluated at the same matched normalized passed charge, \(\Delta Q=0.30\);
- the 3 s-to-3600 s definition of \(\Delta E_{\rm relax}\) and \(t_{63}\) is retained.

The illustrative Mg-like perturbation uses two deliberately simple changes:

1. the deeper-conversion thermodynamic offset is shifted from \(u_3=-3\) to \(u_3=-2\), reducing cutoff-limited conversion;
2. both forward and reverse R2 coefficients are multiplied by 0.8, lengthening the internal reconstruction/redistribution timescale without changing its equilibrium constant.

These values are not fitted to Mg-HEO.

## 3. Numerical result

| Case | \(u_3\) | R2 rate scale | Normalized \(Q_{\rm cutoff}\) | Matched-state \(\Delta E_{\rm relax}\) (mV) | Matched-state \(t_{63}\) (min) |
|---|---:|---:|---:|---:|---:|
| Reference | -3.0 | 1.0 | 0.55845 | 30.82 | 13.45 |
| Illustrative Mg-like | -2.0 | 0.8 | 0.39688 | 26.37 | 16.45 |

Relative changes:

- \(Q_{\rm cutoff}\): **−28.9%**;
- \(\Delta E_{\rm relax}\): **−14.5%**;
- \(t_{63}\): **+22.3%**.

Thus the experimentally relevant direction

\[
Q\downarrow,\qquad
\Delta E_{\rm relax}\downarrow,\qquad
t_{63}\uparrow
\]

is physically admissible within the same multistep conversion model.

## 4. Interpretation boundary

This is a directional existence proof only.

Supported:

- a lower relaxation amplitude does not require a shorter relaxation timescale;
- suppressed conversion extent can coexist with a smaller relaxation amplitude and a longer effective relaxation time in a multistep network;
- the Mg experimental combination is therefore not internally contradictory.

Not supported:

- Mg experimentally changes \(u_3\) by the chosen amount;
- Mg specifically slows R2 by 20%;
- R2 is one uniquely identified structural process;
- the numerical parameter changes are a fit to Mg-HEO.

## 5. Manuscript role

Keep the main Figure 7 focused on the primary BM contradiction and the homogeneous-control / heterogeneous-accessibility existence proof.

Use the present Mg-like directional test in the Supporting Information or internal model audit to support the narrower statement that the Mg combination of lower capacity, lower relaxation amplitude, and longer relaxation is physically possible without requiring amplitude and timescale to share one scalar kinetic coordinate.
