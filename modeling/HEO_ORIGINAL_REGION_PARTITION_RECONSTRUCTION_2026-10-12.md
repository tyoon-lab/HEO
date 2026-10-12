# Recovery of original HEO L1/L3/L4 region partition and Figure 4–6 data — 2026-10-12

## Why this file exists

The 2026-10-07 agreed region-capacity table has been recovered from previous manuscript-analysis discussion. This is the **original accepted L1–L3–rest-end-voltage-L4 partition**, not the alternative broken-stick fitting explored later on 2026-10-12. No new segmentation rule is introduced here.

**Evidence hierarchy:** (1) original accepted *rounded region capacities and percentages* are recovered historical results; (2) region pulse counts and cumulative pulse boundary IDs are **arithmetically inferred** from those values and nominal 100 mA g⁻¹ × 600 s = 16.6667 mAh g⁻¹ per pulse; (3) numerical directional differences below are arithmetic differences of this old table; (4) direct original boundary-index table, BM-HEO raw GITT file, and final source-code provenance have not yet been recovered independently. Do not label the inferred IDs as newly re-measured extrema.

## Original accepted table (October 7)

| Sample | R1, mAh g⁻¹ (%) | R2, mAh g⁻¹ (%) | R3, mAh g⁻¹ (%) | R4, mAh g⁻¹ (%) |
|---|---:|---:|---:|---:|
| HEO | 100 (9.2) | 317 (29.2) | 517 (47.7) | 150 (13.8) |
| BM-HEO | 150 (11.8) | 483 (38.2) | 367 (28.9) | 267 (21.1) |
| Mg-HEO | 100 (12.5) | 300 (37.5) | 250 (31.2) | 150 (18.8) |
| BM-Mg-HEO | 150 (16.1) | 433 (46.4) | 83 (8.9) | 267 (28.6) |

These are **protocol-derived GITT** regional capacities. They are not obtained by multiplying regional fractions by separate first-cycle GCD capacities. Rounded original entries may differ by ±1 mAh g⁻¹ from exact 16.6667-per-pulse arithmetic.

## Reconstructed original pulse counts and boundary endpoints

| Sample | R1 pulses | R2 pulses | R3 pulses | R4 pulses | Full-pulse total | inferred L1 end | inferred L3 end | inferred L4 end |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HEO | 6 | 19 | 31 | 9 | 65 | **6** | **25** | **56** |
| BM-HEO | 9 | 29 | 22 | 16 | 76 | **9** | **38** | **60** |
| Mg-HEO | 6 | 18 | 15 | 9 | 48 | **6** | **24** | **39** |
| BM-Mg-HEO | 9 | 26 | 5 | 16 | 56 | **9** | **35** | **40** |

**Index convention for this reconstruction:** R1 includes pulses 1…L1; R2 L1+1…L3; R3 L3+1…L4; R4 L4+1…end. The numerical IDs are inferred endpoints, not directly sourced original pulse-index annotations. Raw full-pulse sequence lengths **65, 48, 56** independently agree for the three available original workbooks (HEO, Mg-HEO, BM-Mg-HEO). BM-HEO still needs its own raw workbook if exact statewise t63 is to be reproduced.

## What the original table PROVES numerically

Using **exact nominal-pulse** charge, not the rounded region entries:

| Contrast | ΔR1 | ΔR2 | ΔR3 | ΔR4 | ΔTotal |
|---|---:|---:|---:|---:|---:|
| BM-HEO − HEO | +50.0 | **+166.7** | −150.0 | +116.7 | +183.3 |
| BM-Mg-HEO − Mg-HEO | +50.0 | **+133.3** | −166.7 | +116.7 | +133.3 |
| Mg-HEO − HEO | 0.0 | −16.7 | **−266.7** | 0.0 | −283.3 |
| BM-Mg-HEO − BM-HEO | 0.0 | −50.0 | **−283.3** | 0.0 | −333.3 |

Unit for all cells: nominal-protocol GITT **mAh g⁻¹**. R2 is the **largest positive regional BM contribution** in both Mg conditions; it is **not** the largest absolute-magnitude BM-related change in the Mg-containing comparison because R3 is −166.7 there, larger in absolute value than the positive R2 +133.3. R3 is the largest negative Mg-associated contribution in both milling conditions. The net capacity gain/loss is the *signed sum* across regions, so individual regional contributions may be greater in magnitude than the net response.

Special proportions (arithmetically derived, not statistically inferred):
- HEO→BM: R2 positive increment +166.7 is ~90.9% of net +183.3; R1+R4 positive contributions partly compensate R3 negative −150.
- HEO→Mg: R3 −266.7 is ~94.1% of net loss −283.3.
- BM-HEO→BM-Mg: R3 −283.3 is 85.0% of net loss −333.3.

**Manuscript wording:** “BM produces its **largest positive regional capacity increment** in R2” and “Mg produces its **largest negative regional capacity change** in R3.” These are supported by the original table; avoid stating every BM-induced regional absolute change is smaller than R2 in magnitude.

## Figure 4–6 evidence restoration (draft stage)

- **Fig 4 data-only reference draft:** HEO actual 65-pulse rest-end voltage, absolute 3s–60min relaxation amplitude and t63, annotated using original-inferred L1/L3/L4 = 6/25/56. The graph is **not a new boundary fit**. It does not contain BM-HEO or an experimentally identified unique phase.
- **Fig 5 data-only draft:** HEO versus BM-HEO four-region percent contribution and the four signed *protocol-derived GITT* regional differences. R2 +166.7, R3 −150, Δtotal +183.3. BM raw-time-resolved t63 remains missing, so a complete main Figure 5 is not yet done.
- **Fig 6 data-only draft:** Four-material region percentages and both Mg contrasts' signed regional changes, showing R3 suppression at both milling levels. Physical schematic and full relaxation plots remain to be composed.
- Artifacts built locally, not yet uploaded as figure binaries to GitHub: `HEO_v22_Figure4_REFERENCE_FIXED_REGIONS_DRAFT.png`, `HEO_v22_Figure5_BM_R2_PARTITION_DRAFT.png`, `HEO_v22_Figure6_Mg_R3_2x2_PARTITION_DRAFT.png`; three numerical CSV files also generated.

## Interaction with the later alternative knee exploration

`modeling/HEO_L4_THREE_SAMPLE_RAW_REAUDIT_2026-10-12.md` contains an **alternative experimental estimation** using a broken-stick voltage knee. Its candidate L4 positions must **not** supersede the originally agreed L4 segmentation. The objective that remained open in `HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md` was consistent application/documentation of the original plateau-end criterion across all four materials, not replacing it with a new algorithm.

## Next concrete gate

- Recover the original **BM-HEO GITT workbook** and exact prior numeric plotting source to close statewise time/amplitude plot, and verify index convention directly (currently only inferred).
- Check the original L4 positions against all four rest-end voltage traces and the prior Q–OCV criteria, keeping original region allocation as working authority.
- Extend v22 Figure 4–6 with complete relaxation data and final captions; move superseded apparent-D mismatch, excess-localization and cycling-history visualizations to SI only where appropriate.
- Preserve the PI-preferred Abstract and integrated v22 Main text; this file is a **numeric evidence restoration**, not an authorized story change.
