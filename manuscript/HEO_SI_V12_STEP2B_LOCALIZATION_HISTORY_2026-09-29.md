# HEO SI v12 Step 2B — Conversion Localization / History Robustness

**Date:** 2026-09-29  
**Status:** Figure S18 complete and frozen; S19–S20 pending.

## Figure S18 — peak localization with sensitivity ranges

Purpose: extend the nominal main-text Figure 5c peak-position comparison with the actual dQ/dV smoothing and GITT background/window sensitivity ranges.

Nominal peak positions:

| Sample | dQ/dV peak (V) | GITT excess peak (V) | nominal difference (mV) |
|---|---:|---:|---:|
| HEO | 0.544575 | 0.527481 | -17.1 |
| BM-HEO | 0.589146 | 0.617535 | +28.4 |
| Mg-HEO | 0.418819 | 0.386972 | -31.8 |
| BM-Mg-HEO | 0.484822 | 0.502865 | +18.0 |

Thus all four nominal peak offsets are within approximately 32 mV.

Sensitivity ranges:

| Sample | dQ/dV tested range (V) | GITT tested range (V) |
|---|---:|---:|
| HEO | 0.544–0.547 | 0.527481 |
| BM-HEO | approximately 0.589 | 0.592919–0.628391 |
| Mg-HEO | 0.408–0.419 | 0.386972 |
| BM-Mg-HEO | 0.485–0.486 | 0.453175–0.618300 |

Interpretation boundary:
- the nominal conversion-region correspondence is robust and tight for HEO, BM-HEO, and Mg-HEO;
- the shallow BM-Mg-HEO excess feature has a broad GITT peak-location range under the background/window audit and should therefore not be described as having a tightly determined unique conversion peak voltage;
- the main-text localization claim should rest primarily on the cross-sample conversion-region correspondence rather than on a precise BM-Mg-HEO peak position.

Current final artwork:
- `Figure_S18_peak_localization_with_sensitivity_final.png`

Current numerical summary:
- `Figure_S18_peak_localization_sensitivity_summary.csv`

## Non-redundancy versus main Figure 5c

Main Figure 5c shows nominal peak positions only.
Figure S18 adds:
- dQ/dV smoothing sensitivity;
- GITT background/window sensitivity;
- the visibly broad uncertainty of the shallow BM-Mg-HEO feature.

Therefore Figure S18 is retained as an SI robustness figure rather than a duplicate.

## Next

- Figure S19: 105-condition background/window sensitivity of excess-peak amplitude and width.
- Figure S20: cycle-history robustness.
