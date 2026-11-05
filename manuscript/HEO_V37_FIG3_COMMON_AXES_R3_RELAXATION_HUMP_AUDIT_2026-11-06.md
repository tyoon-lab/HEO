# HEO v37 — common-axis Figure 3 and independent raw-GITT R3 ΔErest hump audit (2026-11-06)

**Status:** Figure 3 layout modification is applied in conversation Word v37. Hump/physical interpretation is analytic work **for PI review**; no new mechanism or abstract changes silently adopted.

## Figure 3
- Four 0.1C voltage subpanels (a–d) use one common scale: specific capacity −35 to 1100 mAh/g and voltage −0.08 to 3.35 V vs Li, giving margins without clipping.
- Limits set by highest-capacity BM-HEO 1st-lithiation vector trace: max approx 1017 mAh/g, voltage max approximately 3.2 V; other three panels share both limits.
- Original vector-reconstructed sample traces, colors, cycle order from v34/v36 retained; only common axis margins and Figure 3 caption updated.
- Delivered Word: `HEO_Manuscript_v37_Figure3_CommonAxes_2026-11-06.docx` (14 pages, no Word comments). Standalone PNG/PDF `HEO_Figure3_CommonAxes_v37` and supplementary **diagnostic** PNG/PDF `HEO_R3_DeltaE_hump_diagnostics`. Physical Figure 6 remains prior working figure pending PI discussion.
- Note: vector graph reconstruction is not raw cycling instrument export.

## Analysis source: all four actual original GITT Excel files; 600 s galvanostatic pulses, ~60 min rest, E(3 s) reference. Preserve t63-only locked boundaries
| Sample | L1/L3/L4 | R3 first ΔErest mV | R3 peak mV (pulse) | R3 end mV | R3 peak rise vs R3 start mV | R3 t63 first→last min |
| HEO | 6/25/55 | 145.10 | 189.28 (50) | 172.46 | +44.19 | 7.07→14.73 |
| BM-HEO | 9/38/60 | 163.60 | 163.60 (39, **R3 onset**) | 136.53 | 0 | 11.37→15.89 |
| Mg-HEO | 7/24/42 | 109.17 | 117.73 (38) | 111.61 | +8.56 | 10.18→12.66 |
| BM-Mg-HEO | 9/35/46 | 135.77 | 135.77 (36, **R3 onset**) | 116.05 | 0 | 11.96→13.49 |

Interpretation: pronounced within-R3 finite-window rest-voltage amplitude hump only for pristine, small in Mg-HEO, absent as interior maximum in two milled specimens. **All four t63 values increase during R3**, so the amplitude hump and characteristic relaxation time carry different information. ΔErest is composite recovery from rest start 3s to end ~3600s: amplitude can change due to changes in transient polarization, distribution of reduction/phase conversion, OCV-vs-charge slope, and interfacial response. It is not a unique kinetic rate/transport coefficient or a uniquely identified phase. Literature support for multi-step species-specific metal reduction: Luo et al., Advanced Science 2022, DOI:10.1002/advs.202201219 (different spinel composition); Kang & Chueh JES 2021, DOI:10.1149/1945-7111/ac3940 (GITT limitations). Do not label hump as proof of one specific metal redox without operando data.

## Nominal kinetic-region charge changes:
- Milling Mg-free: R1+50.0 R2+166.7 R3−133.3 R4+100.0 mAh/g.
- Milling Mg-containing: R1+33.3 R2+150.0 R3−116.7 R4+66.7.
- Mg added unmilled: R1+16.7 R2−33.3 R3−200.0 R4−66.7.
- Mg added milled: R1~0 R2−50 R3−183.3 R4−100.
- **R3 is the largest negative regional charge change in all four comparisons**, but this alone does NOT prove R3 hosts an inherently easiest-to-modify elementary reaction, because t63 region borders correspond to different QOCV values and nominal pulse allocation counts.
- Independent check of QOCV-fixed 0.60→0.40 V charge: HEO 314.6; BM-HEO 178.1; Mg-HEO 418.6; BM-Mg-HEO 243.9 mAh/g. Mg actually increases charge in this common voltage window vs corresponding Mg-free sample; avoid claiming fixed-potential suppression simply from R3 assignment.
- Candidate future analysis with existing data: compare amplitude vs common QOCV and local QOCV slope; compare normalized individual rest traces at R3 start/peak/end; consider potential-slope correction before attributing hump to reaction resistance. The R3 charge result remains higher-ranking than the subtle relaxation-shape result.

**Status change scope:** Figure 3 shared axes and caption only. Hump interpretation is not inserted into main manuscript until PI decides and thermodynamic/kinetic decomposition is checked.
