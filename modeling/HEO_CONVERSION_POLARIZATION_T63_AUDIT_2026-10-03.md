# HEO conversion-polarization–t63 audit — 2026-10-03

## Purpose

Reframe the kinetic analysis after abandoning the assumption that the sample-to-sample capacity difference can be interpreted directly as a conversion-rate difference or as a consequence of terminal polarization.

The new question is:

> Does the polarization developed in the conversion region track the timescale of the post-interruption relaxation?

The answer from the raw first-lithiation GITT data is no: polarization magnitude and t63 do not move along one universal fast–slow coordinate.

---

## Raw sources

Recovered original GITT workbooks:

- HEO: `HEO GITT 로우 데이터.xlsx`
- BM-HEO: `BM HEO 3 GITT 로우 데이터.xlsx`
- Mg-HEO: `HEO 3 Mg 로우 데이터.xlsx`
- BM-Mg-HEO: `BM HEO 3 Mg 로우 데이터.xlsx`

Protocol:
- 600 s current pulse
- 3600 s open-circuit rest
- 0.005–2.5 V
- first lithiation analyzed here

The re-parsed z = 0.40–0.90 medians reproduce the existing manuscript-authority values for Delta E_relax and t63, validating the step segmentation.

---

## Operational polarization definition

To avoid comparing voltages at different lithiation states, define the recoverable end-of-pulse polarization relative to the subsequent rest endpoint:

[
Delta E_{mathrm{pol,60}}
=
left|E_{mathrm{rest,60,min}}-E_{mathrm{pulse,end}}ight|.
]

This is an **operational 60-min recoverable polarization**, not an exact thermodynamic overpotential, because the 60 min rest endpoint is not proven to be the true equilibrium potential.

It can be separated operationally into:

[
Delta E_{mathrm{fast}}
=
left|E_{mathrm{rest,3,s}}-E_{mathrm{pulse,end}}ight|
]

and

[
Delta E_{mathrm{relax}}
=
left|E_{mathrm{rest,60,min}}-E_{mathrm{rest,3,s}}ight|.
]

The characteristic t63 remains defined from the 3 s-to-60 min relaxation and therefore measures the timescale of the slower post-interruption voltage recovery.

---

## Main first-cycle conversion-window result

Common normalized first-lithiation window: z = 0.40–0.90.

| Sample | Delta E_pol,60 (mV) | fast 0–3 s recovery (mV) | Delta E_relax, 3 s–60 min (mV) | t63 (min) |
|---|---:|---:|---:|---:|
| HEO | 195.9 | 26.3 | 168.5 | 10.37 |
| BM-HEO | 182.6 | 22.2 | 160.5 | 13.02 |
| Mg-HEO | 126.4 | 15.3 | 111.3 | 10.53 |
| BM-Mg-HEO | 148.2 | 12.8 | 135.2 | 12.70 |

### Material-modification directions

HEO -> BM-HEO:
- Delta E_pol,60 ratio = 0.932
- t63 ratio = 1.256

Thus milling slightly **decreases** recoverable polarization while clearly **lengthening** relaxation.

HEO -> Mg-HEO:
- Delta E_pol,60 ratio = 0.645
- t63 ratio = 1.015

Thus Mg incorporation strongly decreases polarization magnitude while leaving the characteristic timescale almost unchanged.

Mg-HEO -> BM-Mg-HEO:
- Delta E_pol,60 ratio = 1.172
- t63 ratio = 1.207

Here both descriptors increase.

Therefore there is no material-independent monotonic mapping between conversion-region polarization magnitude and post-interruption relaxation timescale.

Do not use a four-point Pearson/Spearman coefficient as the central evidence; n = 4 is too small and the four samples represent different material perturbations. The directional contrasts themselves are the main experimental result.

---

## Conversion-associated polarization excess

The same first-cycle background protocol already used for the relaxation hump was applied to Delta E_pol,60:

- fit background over z = 0.20–0.40 and 0.90–1.00;
- exponential background of the same form used in the existing Figure 5 analysis;
- evaluate the background-subtracted excess over z = 0.40–0.90.

Nominal excess-polarization peaks:

| Sample | excess peak (mV) | z_peak | rest-end V at peak (V) | dQ/dV peak (V) | offset (mV) |
|---|---:|---:|---:|---:|---:|
| HEO | 72.5 | 0.754 | 0.537 | 0.545 | -7.5 |
| BM-HEO | 49.3 | 0.671 | 0.618 | 0.589 | +28.4 |
| Mg-HEO | 16.9 | 0.792 | 0.387 | 0.419 | -31.8 |
| BM-Mg-HEO | 22.0 | 0.661 | 0.503 | 0.485 | +18.0 |

All four nominal offsets remain within approximately 32 mV.

This is essentially the same localization result as the previous 3 s-to-60 min relaxation-hump analysis, showing that the conversion-associated component survives when the fast current-off recovery is included.

Safe interpretation:

**The additional recoverable polarization that appears late in first lithiation is localized to the conversion region, but its magnitude does not uniquely determine the post-interruption relaxation timescale.**

---

## Definition robustness

The same material-level qualitative conclusion is obtained with:

- total recoverable polarization Delta E_pol,60;
- the slower 3 s-to-60 min relaxation magnitude Delta E_relax;
- the finite-pulse excursion Delta E_tau.

For HEO -> BM:
- all polarization/amplitude descriptors are unchanged or smaller;
- t63 becomes longer.

For HEO -> Mg:
- polarization/amplitude descriptors become substantially smaller;
- t63 remains nearly unchanged.

Therefore the polarization–timescale decoupling is not created by one particular operational voltage-difference definition.

---

## State-resolved relationship

Within z = 0.40–0.90, the sign of the state-trajectory association between polarization magnitude and t63 is not universal.

For Delta E_pol,60 versus t63, the state-resolved Spearman direction is:
- HEO: positive;
- BM-HEO: strongly negative;
- Mg-HEO: positive;
- BM-Mg-HEO: weakly negative.

These state-wise correlations are strongly influenced by the common state coordinate z and should not be interpreted as causal rate laws. Their value is only to show that even the trajectory shape is sample dependent.

Preferred presentation:
- plot the state-resolved polarization–t63 trajectories with z encoded along the trajectory;
- emphasize different trajectory directions rather than one pooled regression line.

---

## Capacity claim boundary after this audit

Capacity remains an important electrochemical outcome, but it is no longer used as a direct kinetic coordinate.

Safe:
- milling increases accessible capacity;
- Mg incorporation decreases accessible capacity;
- these capacity changes coexist with distinct polarization and relaxation responses.

Not safe:
- larger capacity proves faster conversion kinetics;
- smaller capacity proves slower conversion kinetics;
- terminal polarization determines the sample-to-sample capacity;
- the four-step Q-based model identifies the origin of the experimental capacity difference.

---

## Consequence for conventional GITT Dapp

The existing Dapp/direct-relaxation disagreement remains numerically valid, but it is no longer required to carry the main paper logic.

Preferred role:
- secondary diagnostic or SI robustness result;
- useful for showing that conventional apparent diffusivity need not rank the same response as directly measured current-off relaxation.

Do not let the paper become a general GITT-method manuscript.

---

## Consequence for the former Figure 6 microkinetic model

The former capacity-based R2/R3 existence test is no longer needed as the main explanatory endpoint.

Current status:
- preserve the numerical work as a historical/optional SI audit;
- do not use Q-up/t63-up as the central model claim;
- do not map ball milling onto R2/R3;
- do not use voltage cutoff or polarization to explain experimental capacity.

If modeling is retained later, it should address the narrower question:

> How can polarization amplitude and current-off relaxation timescale vary independently in a multistep conversion network?

A purely experimental Figure 6 based on cycle-history robustness may ultimately be preferable.

---

## Immediate manuscript consequence

The revised scientific spine should be:

Figures 1–2: material modification
-> Figure 3: electrochemical capacity/performance as outcomes, without kinetic inference
-> Figure 4: direct GITT polarization magnitude and t63 comparison
-> Figure 5: localization of the polarization/relaxation feature to the conversion region
-> Figure 6: robustness / history dependence / optional minimal consistency model focused on polarization–timescale decoupling

Main v17 and SI v14 are not yet rewritten. This audit supersedes the former capacity-driven interpretation for the next revision.
