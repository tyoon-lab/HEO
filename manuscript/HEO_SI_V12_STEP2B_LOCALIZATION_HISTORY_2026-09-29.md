# HEO SI v12 Step 2B — Conversion Localization / History Robustness

**Date:** 2026-09-29  
**Status:** Figures S18–S19 complete and frozen; S20 pending.

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


## Figure S19 — 105-condition background/window sensitivity

Purpose: show whether the first-cycle conversion-associated excess amplitude and width depend strongly on the specific background/window choice.

Nominal values and tested ranges:

| Sample | peak nominal (mV) | peak range (mV) | width nominal (mAh g^-1) | width range (mAh g^-1) |
|---|---:|---:|---:|---:|
| HEO | 70.77 | 60.7–74.7 | 354.13 | 306–379 |
| BM-HEO | 44.07 | 36.7–51.0 | 430.17 | 379–497 |
| Mg-HEO | 15.91 | 13.0–18.6 | 250.29 | 192–351 |
| BM-Mg-HEO | 21.10 | 12.6–27.6 | 391.78 | 233–872 |

Directional robustness across all 105 tested definitions:
- BM-HEO peak < HEO peak: 105/105;
- BM-HEO width > HEO width: 105/105;
- Mg-HEO peak < HEO peak: 105/105;
- BM-Mg-HEO peak < HEO peak: 105/105;
- BM-Mg-HEO peak > Mg-HEO peak: 80/105.

Interpretation:
- the BM-HEO peak-down / width-up relation is robust;
- Mg-associated suppression of the excess amplitude is robust;
- the BM-Mg-HEO peak amplitude remains lower than HEO in every tested condition;
- the BM-Mg-HEO width is poorly constrained because the feature is shallow and broad, so its exact width should not be overinterpreted.

Current final artwork:
- `Figure_S19_background_window_sensitivity_final.png`

Current numerical summaries:
- `Figure_S19_105condition_sensitivity_summary.csv`
- `Figure_S19_105condition_directional_counts.csv`

## Next

- Figure S20: cycle-history robustness.
