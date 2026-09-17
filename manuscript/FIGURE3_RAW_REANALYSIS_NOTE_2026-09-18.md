# Figure 3 Raw Reanalysis Note

**Date:** 2026-09-18

## Purpose

This note records the raw-data reconstruction used for the preliminary main-text Figure 3. The four first-discharge GITT datasets were re-read directly from the raw Excel files rather than from the older summary CSVs.

## Common definitions

- First discharge block only.
- Nominal pulse increment: 100 mA g−1 × 10 min = 16.667 mAh g−1 per pulse.
- Early current-off response: fit `E(t) = a + b sqrt(t)` over 3–30 s after current interruption.
- Apparent current-off resistance: `(a − E_pulse,end)/|I|`.
- Finite-window relaxation amplitude: `E_60min − E_3s`.
- Model-free `t63`: first time required to reach 63.2% of the observed 3 s-to-60 min recovery.
- The Mg-free datasets are sampled at ~1 s in the GITT region, whereas the Mg-containing datasets are sampled at ~3 s; the 3 s reference is therefore used for the common relaxation definition.

## Recalculated medians

| Sample | Roff, 0–200 mAh g−1 (Ω) | Roff, 200–800 mAh g−1 (Ω) | ΔErelax, 200–800 (mV) | t63, 200–800 (min) | Median R2 of 3–30 s sqrt(t) fit |
|---|---:|---:|---:|---:|---:|
| HEO | 308.1 | 106.4 | 160.9 | 8.68 | 0.9995 |
| BM-HEO | 592.7 | 106.5 | 176.3 | 11.57 | 0.9992 |
| Mg-HEO | 44.5 | 40.2 | 109.5 | 11.01 | 0.9994 |
| BM-Mg-HEO | 93.8 | 33.0 | 144.3 | 12.99 | 0.9985 |

These values are close to, but not numerically identical with, the earlier working summary because the present calculation reconstructs the current-off event directly from the raw Excel stream and applies one common 3–30 s regression definition.

## Figure-level interpretation

### Panel a — representative current interruption

A representative HEO pulse near 800 mAh g−1 gives an extrapolated current-off jump of ~15 mV from the 3–30 s sqrt(t) fit. The purpose of this panel is operational definition, not mechanism assignment.

### Panel b — fast current-off polarization

- BM-HEO has a much larger initial first-lithiation fast response than HEO.
- HEO and BM-HEO converge to nearly identical apparent current-off resistance over 200–800 mAh g−1.
- Mg substantially lowers the fast current-off polarization.

### Panel c — finite-window relaxation amplitude

- Pristine HEO shows a distinct late-stage rise/hump after its mid-capacity minimum.
- BM-HEO shows a broader, less localized response.
- Mg-HEO strongly suppresses the late-stage hump.
- BM-Mg-HEO remains broader than Mg-HEO but does not recover the concentrated HEO-like feature.

### Panel d — model-free t63

- Ball milling lengthens the characteristic post-pulse relaxation despite increasing accessible galvanostatic capacity.
- Mg lowers polarization amplitude without shortening the characteristic relaxation time.
- This decoupling is the key reason not to interpret smaller polarization as automatically faster Li transport.

## Publication note

The exact manuscript values should be frozen only after the final analysis script is archived and checked against the plotted source CSVs. The qualitative mechanistic conclusions are unchanged by the small numerical differences relative to the earlier working summary.
