# HEO SI v12 Step 2A — GITT Robustness Figures S15–S17

**Date:** 2026-09-29  
**Status:** Step 2A complete; figures generated and scientifically checked against main Figure 4.


## Raw HEO revalidation — exact sample-index convention

The HEO raw workbook was re-opened directly and the first-lithiation GITT block was segmented from the recorded current transitions.

Recovered timing:
- initial GITT pulse starts at test time 21601 s;
- each pulse contains 600 recorded current-on samples;
- each rest contains 3600 recorded zero-current samples;
- pulse (n) starts at (21601+(n-1)	imes4200) s;
- pulses 12–48 correspond to approximately 200–800 mAh g⁻¹.

For the historical direct-relaxation descriptor, the reference voltage is taken at the **third recorded zero-current sample after the switch**, and the characteristic time is the **first raw sample** reaching the requested fraction of the observed reference-to-rest-end recovery. No interpolation is required for the frozen value.

Using the raw HEO workbook over pulses 12–48 gives:
- median (t_{50}=4.3167) min;
- median (t_{63}=8.6833) min;
- median (t_{90}=34.8333) min.

The recalculated median (t_{63}=8.6833) min reproduces the frozen manuscript value of 8.68 min to rounding. This raw revalidation fixes the sample-index convention to be used for the BM-HEO robustness calculation.

Note: this sub-audit concerns the fractional relaxation times. The separately frozen (Delta E_{\mathrm{relax}}) median uses its established endpoint-processing convention and is not redefined here.


## Raw BM-HEO revalidation using the same sample-index convention

The same raw-sample procedure was applied to the BM-HEO workbook over the identical pulses 12–48.

Median fractional-relaxation times measured from the common third zero-current sample are:

| Sample | t50 (min) | t63 (min) | t90 (min) |
|---|---:|---:|---:|
| HEO | 4.3167 | 8.6833 | 34.8333 |
| BM-HEO | 6.0167 | 11.5500 | 38.9000 |

The raw-sample BM median t63 of 11.55 min differs by only 0.02 min from the frozen manuscript value of 11.57 min. The small difference is consistent with raw-sample threshold crossing versus the interpolated descriptor used in the frozen audit and does not affect the ordering.

Using the exact raw-sample crossings, the state-matched HEO/BM direct-rate ratios and directional counts are:

| Descriptor | median HEO/BM ratio | BM slower states |
|---|---:|---:|
| t50 | 0.7235 | 34/37 |
| t63 | 0.7599 | 35/37 |
| t90 | 0.8961 | 33/37 |

These counts are identical to the previously generated interpolated robustness audit (34/37, 35/37, and 33/37, respectively). Therefore the central conclusion is insensitive both to the chosen relaxation fraction and to the small choice between raw-sample threshold crossing and interpolation.

Exact raw-sample table generated in the active analysis session:
`HEO_BM_t50_t63_t90_raw_exact_2026-09-29.csv`.

## Figure S15 — relaxation-fraction robustness

Purpose: test whether the HEO/BM kinetic ordering depends on choosing the 63.2% relaxation time.

Definitions use the same current-off window as the main analysis:
- common reference: 3 s after current interruption;
- rest endpoint: end of the nominal 60 min rest;
- t50 and t90: first time to complete 50% and 90% of the observed 3 s-to-rest-end recovery;
- t63: frozen authoritative main-text ratio from the committed HEO/BM audit.

State-matched interval: 37 points, approximately 200–800 mAh g^-1.

Direct relaxation-rate ratio is oriented as HEO/BM so that values below unity mean BM-HEO relaxes more slowly.

| Descriptor | Median HEO/BM direct-rate ratio | BM slower states |
|---|---:|---:|
| t50 | 0.7297 | 34/37 |
| t63 | 0.7622 | 35/37 |
| t90 | 0.9007 | 33/37 |

Conclusion: the slower BM current-off response is not an artifact of choosing t63. The contrast weakens at the late 90% recovery criterion, but the ordering remains BM slower over most of the common interval.

Current local artwork:
- `heo_si_step2A/Figure_S15_t50_t63_t90_robustness.png`

## Figure S16 — descriptor-disagreement map

Plot:
- x = Dapp,BM / Dapp,HEO
- y = t63,HEO / t63,BM
- marker color = matched capacity

All 37 states lie at x > 1.
35/37 lie at y < 1.

Thus almost the entire dataset occupies the disagreement quadrant in which conventional Dapp ranks BM-HEO faster while direct relaxation ranks it slower.

This is intentionally different from main Figure 4b, which shows the two ratios as functions of capacity.

Current local artwork:
- `heo_si_step2A/Figure_S16_descriptor_disagreement_map.png`

## Figure S17 — voltage-term decomposition

Plot versus matched capacity:
- Delta Es,BM / Delta Es,HEO
- Delta Etau,BM / Delta Etau,HEO
- Dapp,BM / Dapp,HEO

Frozen median ratios from the conventional-GITT audit:
- median Delta Es ratio = 1.8095
- median Delta Etau ratio = 1.1758
- median Dapp ratio = 1.7817

The stronger increase in the relaxed voltage increment than in the finite-pulse voltage excursion raises the conventional Dapp ratio even though direct current-off relaxation is slower.

This decomposition is not shown in the main text and therefore adds SI-specific mechanistic audit value.

Current local artwork:
- `heo_si_step2A/Figure_S17_voltage_term_decomposition.png`

## Main–SI non-redundancy check

- S15: new robustness test, not present in main.
- S16: same underlying 37 states as main Figure 4b but a different ratio–ratio representation that directly visualizes the disagreement quadrant.
- S17: underlying voltage-term decomposition not shown in main.

Step 2A is therefore approved for the non-redundant SI architecture.

## Next step

Step 2B:
- Figure S18: dQ/dV–GITT peak localization with sensitivity ranges;
- Figure S19: 105-condition background/window sensitivity;
- Figure S20: cycle-history robustness.
