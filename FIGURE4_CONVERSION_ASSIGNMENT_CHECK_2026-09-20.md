# Figure 4 conversion-assignment check — 2026-09-20

## Purpose

Test whether the late-stage Figure 4 GITT excess-relaxation hump is located in the same voltage region as the first-cycle cathodic differential-capacity feature. This is intended to distinguish a generic "phase-transition-associated" interpretation from the more specific hypothesis that the excess response is linked to the low-voltage conversion reaction.

## Data used

GITT raw files recovered from the 2026-09-17 data package:
- HEO GITT raw data
- BM-HEO GITT raw data
- Mg-HEO GITT raw data
- BM-Mg-HEO GITT raw data

First-cycle differential-capacity traces:
- Cycle-1 dQ/dV curves already plotted in the 2026-09-17 HEO progress deck.
- For this preliminary check, the lightest Cycle-1 curve was digitized directly from the embedded vector plot. The raw first-cycle galvanostatic source file was not reprocessed here, so the dQ/dV peak voltages should be treated as plot-resolution estimates (approximately ±0.01 V).

## GITT reconstruction

For the first lithiation GITT sequence:
- current pulse = 600 s
- rest = 3600 s
- common current-off reference = 3 s
- relaxation amplitude = E(rest end) - E(3 s)
- the same independent background form currently used for Figure 4 was fitted to each sample:
  eta_bg(z) = c + a exp(-z/tau)
- fit windows: z = 0.20–0.40 and 0.90–1.00
- excess evaluated over z = 0.40–0.90.

The reconstructed peak amplitudes reproduced the frozen Figure 4 values essentially exactly for Mg-HEO and BM-Mg-HEO and within ~1 mV for HEO/BM-HEO, confirming that the same feature was recovered. The small HEO/BM differences arise from the preliminary capacity normalization used in this reconstruction and do not change the peak pulse/state.

## Peak-voltage comparison

| Sample | Cycle-1 cathodic dQ/dV peak (V) | GITT excess peak, 60-min relaxed voltage (V) | Difference (V) |
|---|---:|---:|---:|
| HEO | ~0.531 | 0.527 | -0.003 |
| BM-HEO | ~0.539 | 0.618 | +0.078 |
| Mg-HEO | ~0.365 | 0.387 | +0.022 |
| BM-Mg-HEO | ~0.425 | 0.503 | +0.078 |

All four GITT-excess maxima lie within ~0.08 V of the first-cycle reduction feature.

The composition-induced shift is especially notable:
- HEO -> Mg-HEO: dQ/dV peak shifts by about -0.166 V; GITT excess peak shifts by about -0.141 V.
- BM-HEO -> BM-Mg-HEO: dQ/dV peak shifts by about -0.114 V; GITT excess peak shifts by about -0.115 V.

Thus the Mg-induced displacement of the GITT excess closely tracks the independently observed displacement of the first-cycle reduction feature.

## Interpretation

This comparison materially strengthens the assignment of the Figure 4 excess response to the **low-voltage conversion/transformation reaction** rather than to an unspecified phase transition.

The safest current wording is:
- **conversion/transformation-associated excess relaxation** for the quantitative descriptor;
- discussion can state that its voltage localization and sample-dependent shift coincide with the first-cycle cathodic conversion feature.

The data do not by themselves prove a unique microscopic step. The excess can still contain contributions from rock-salt-like intermediate evolution, cation/oxygen rearrangement, metal/Li2O nucleation, phase-boundary motion, and heterogeneous structural relaxation. Therefore avoid assigning the hump solely to one elementary process.

## Implication for the four-sample mechanism

- HEO: concentrated conversion-associated response near ~0.53 V.
- BM-HEO: lower and broader excess, consistent with redistribution of conversion over a wider state interval; the relaxed-voltage maximum moves to ~0.62 V.
- Mg-HEO: strongly suppressed excess and a lower-voltage maximum near ~0.39 V, matching the lower-voltage shift of the cathodic dQ/dV feature.
- BM-Mg-HEO: partial reopening/broadening of the response, with peak near ~0.50 V.

This supports the materials-centered interpretation that ball milling redistributes electrochemically accessible conversion whereas Mg imposes a compositional/structural constraint on conversion extent.

## Before manuscript wording is frozen

1. Recompute the first-cycle dQ/dV directly from the raw GCD source data rather than relying on plot digitization.
2. Freeze the exact peak positions with the same smoothing/differentiation procedure for all four samples.
3. Run the planned Figure 4 background/window sensitivity audit.
4. If both checks remain robust, revise Main 3.4 from generic "late-stage transformation" toward "late-stage conversion/transformation" and consider adding a compact dQ/dV overlay or vertical conversion-band annotation to Figure 4/SI.


## Figure 5 frozen-v4 cross-check against the conversion assignment

The frozen spatial model was recalculated without refitting any parameter. For this cross-check, the model variable (phi) is interpreted conservatively as an **effective conversion-associated structural-state coordinate**, not as a measured rock-salt or metallic-phase fraction.

### Frozen-v4 relaxation-peak state

Using both the volume-averaged and surface chemical-potential readouts, the state of maximum 3 s-to-60 min relaxation is identical:

| Sample | Model (ar c) at relaxation peak |
|---|---:|
| BM-HEO | 0.5860 |
| HEO | 0.6184 |
| BM-Mg-HEO | 0.7966 |
| Mg-HEO | 0.9100 |

Thus the model ordering from earlier to later conversion-associated response is:

**BM-HEO → HEO → BM-Mg-HEO → Mg-HEO.**

The experimental peak-voltage ordering is the same when higher cathodic voltage is interpreted as an earlier/easier conversion event:

- GITT excess peak: **BM-HEO (0.618 V) > HEO (0.527 V) > BM-Mg-HEO (0.503 V) > Mg-HEO (0.387 V)**.
- Digitized first-cycle dQ/dV peak: **BM-HEO (~0.539 V) ≈ HEO (~0.531 V) > BM-Mg-HEO (~0.425 V) > Mg-HEO (~0.365 V)**.

The BM-HEO versus HEO dQ/dV difference is only ~8 mV and is within the approximate plot-digitization uncertainty, so those two should be treated as effectively similar until raw GCD data are reprocessed. The much larger Mg-related displacement is robust at the present level.

### Conversion-onset robustness in the model

A second check used the pulse-end ensemble-averaged (arphi) rather than the relaxation peak. Linear interpolation gives:

| Pulse-end converted-state threshold | BM-HEO | HEO | BM-Mg-HEO | Mg-HEO |
|---|---:|---:|---:|---:|
| (arphi=0.02) | 0.545 | 0.606 | 0.735 | 0.834 |
| (arphi=0.05) | 0.557 | 0.619 | 0.763 | 0.859 |
| (arphi=0.10) | 0.570 | 0.620 | 0.779 | 0.889 |

The same ordering is preserved over all three onset definitions:

**BM-HEO → HEO → BM-Mg-HEO → Mg-HEO.**

Therefore the agreement is not an artifact of selecting the single model relaxation maximum.

### Interpretation

This cross-check supports the revised model interpretation:

- (phi) should be described as an **effective conversion-associated internal-state variable**.
- (G_{m Mg}>0) represents stabilization of the unconverted oxide-derived parent/intermediate state, delaying conversion to higher lithiation state / lower experimental potential.
- BM broadens and advances the distribution of local conversion conditions rather than simply accelerating one diffusion coefficient.
- BM-Mg partially reopens the Mg-suppressed conversion pathway but does not restore the HEO/BM conversion behavior.

### Important boundary: do not map model (ar c) directly onto experimental normalized capacity

The model (ar c) is not calibrated to (Q/Q_{max}), and the four samples have substantially different accessible capacities. Therefore agreement is assessed by **direction/order and qualitative onset displacement**, not by equating a numerical model (ar c) with an experimental normalized-capacity value.

This is especially important because cross-sample (Q/Q_{max}) peak positions do not provide the same ordering as the peak voltages. Peak voltage is the more appropriate current experimental comparator for the conversion-onset question.

### Current conclusion

Without any refitting after the conversion reassignment, the frozen spatial model remains internally consistent with the new experimental interpretation. It should be renamed/reworded as a **reduced spatial model of conversion-associated state evolution**, not as a literal complete conversion-reaction model.

The remaining manuscript gate is the raw-GCD recalculation of first-cycle dQ/dV. If that confirms the current peak positions, Main Figure 4/5 wording can be revised together.


## Updated first-cycle validation from the latest 2026-09-17 voltage-profile slide

The preliminary direct digitization of the plotted dQ/dV traces was replaced by a stronger check using the **latest first-cycle voltage profiles** in Park Seonghyeon's HEO 진행상황 (20260917).pptx, slide 10.

The Origin vector previews embedded in the PowerPoint were extracted and the Cycle-1 lithiation branches were reconstructed directly from the voltage-versus-specific-capacity curves. The reconstructed terminal first-cycle capacities were:

- HEO: 901.14 mAh g^-1
- BM-HEO: 1055.84 mAh g^-1
- Mg-HEO: 731.05 mAh g^-1
- BM-Mg-HEO: 943.87 mAh g^-1

These reproduce the values printed in the same slide (901.25, 1056.10, 731.15, and 944.07 mAh g^-1, respectively) to within ~0.03%, confirming that the vector-curve extraction is faithful.

A common Savitzky-Golay treatment was then applied to the reconstructed first-cycle voltage profiles and cathodic dQ/dV was recalculated. Using a 40 mAh g^-1 smoothing window, the low-voltage first-cycle reduction maxima are:

| Sample | Profile-derived dQ/dV peak (V) | GITT excess peak (V) | GITT - dQ/dV (V) |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | -0.018 |
| BM-HEO | 0.589 | 0.618 | +0.029 |
| Mg-HEO | 0.419 | 0.387 | -0.032 |
| BM-Mg-HEO | 0.485 | 0.503 | +0.018 |

Smoothing-window sensitivity (20-60 mAh g^-1) gives:
- HEO: 0.544-0.547 V
- BM-HEO: 0.589 V
- Mg-HEO: 0.408-0.419 V
- BM-Mg-HEO: 0.485-0.486 V

Thus all four conversion-associated GITT excess maxima fall within ~32 mV of the independently reconstructed first-cycle cathodic dQ/dV maximum. This is substantially tighter than the earlier direct digitization of the noisy plotted dQ/dV traces and should be treated as the preferred current validation.

### Current implication

The voltage localization now strongly supports describing the Figure 4 feature as **conversion/transformation-associated excess relaxation**. The evidence is still phenomenological rather than a direct structural identification of one elementary conversion step, so the manuscript should not assign the peak uniquely to metal/Li2O nucleation or any single microscopic event.

This latest-PPT validation supersedes the earlier plot-resolution dQ/dV peak estimates for manuscript positioning. The remaining required gate is the Figure 4 background/window sensitivity audit.
