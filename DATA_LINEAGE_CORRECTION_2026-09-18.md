# HEO Electrochemical Data Lineage Correction

**Date:** 2026-09-18

## Why this note exists

During manuscript integration, the May 2026 internal presentation and the 2026-09-17 progress deck were found to contain different first-cycle capacity values and different qualitative notes about the effect of ball milling on rate capability. The manuscript should not mix these versions.

## Source priority

Current priority for electrochemical manuscript drafting:

1. Raw instrument data, when directly reconstructed and audited.
2. Latest 2026-09-17 progress dataset/plots.
3. Earlier May 2026 presentation values only as historical context.

## First-cycle values currently used

From the 2026-09-17 progress deck under the WonATech charge/discharge convention:

| Sample | 1st Charging (mAh g-1) | 1st Discharging (mAh g-1) | ICE (%) |
|---|---:|---:|---:|
| HEO FEC | 901.25 | 609.12 | 67.59 |
| BM HEO FEC | 1056.10 | 782.08 | 74.05 |
| HEO Mg FEC | 731.15 | 458.91 | 62.766 |
| BM HEO Mg FEC | 944.07 | 580.83 | 61.524 |

Earlier May 2026 values are not used in the current draft when they conflict with these values.

## Rate-capability correction

The earlier internal interpretation `ball milling -> poorer rate capability` is not supported by the latest plotted rate dataset. In the 2026-09-17 plot, BM-HEO maintains a higher absolute capacity than HEO across the tested 0.1 C -> 5 C sequence and after return to 0.1 C.

Therefore manuscript wording should not claim that the longer GITT relaxation time of BM-HEO causes poorer rate capability.

Preferred interpretation:

- BM increases accessible interface and galvanostatic utilization.
- BM also lengthens the 60-min current-off relaxation.
- Practical rate utilization and long-rest relaxation time are distinct observables and can move in opposite directions.

This is scientifically more informative than the previous rate-penalty interpretation.

## Cycling / FEC correction

Under 10 wt% FEC, BM-HEO maintains higher absolute capacity than HEO over the 100-cycle plot. The no-FEC control shows stronger capacity decay for BM-HEO, consistent with a larger surface/interphase burden after milling.

Thus FEC should be described as a standardized interphase-control condition that mitigates the surface penalty of the enlarged BM interface. The HEO manuscript should not make FEC a third central mechanistic variable.

## GITT source status

The current-off GITT descriptors were recalculated from the raw Excel files and therefore have higher source priority than internal slide summaries:

- 3-30 s E vs sqrt(t) extrapolated current-off jump/apparent resistance;
- Delta E_relax;
- t50/t63/t90 using a common 3 s reference;
- transition-hump peak/width/area, pending final baseline-sensitivity freeze.

## Manuscript files corrected

- `manuscript/HEO_MANUSCRIPT_V0_1_PART2_2026-09-18.md`
- `manuscript/HEO_MANUSCRIPT_V0_1_PART3_2026-09-18.md`
- `manuscript/HEO_MANUSCRIPT_V0_1_PART4_2026-09-18.md`

## Remaining verification

Before final manuscript freeze:

- verify WonATech charge/discharge naming vs lithiation/delithiation;
- if available, reconstruct cycling/rate values directly from raw source files rather than plot-only values;
- finalize transition-hump baseline sensitivity;
- audit cycling EIS before any fitted resistance is used mechanistically.