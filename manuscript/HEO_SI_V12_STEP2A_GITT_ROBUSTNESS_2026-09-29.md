# HEO SI v12 Step 2A — GITT Robustness Figures S15–S17

**Date:** 2026-09-29  
**Status:** Step 2A complete; figures generated and scientifically checked against main Figure 4.

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
