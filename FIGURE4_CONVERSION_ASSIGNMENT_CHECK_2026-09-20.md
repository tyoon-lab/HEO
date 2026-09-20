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
