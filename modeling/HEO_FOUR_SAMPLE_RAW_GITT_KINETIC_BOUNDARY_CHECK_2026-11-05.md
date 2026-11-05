# Four-sample original GITT raw extraction and kinetic-boundary check — 2026-11-05

**Status:** Candidate for PI examination; does NOT supersede accepted main text, v12 PI-locked abstract, SI, or v31/v32 region-charge table.

## Original raw sources recovered directly
- `HEO GITT 로우 데이터.xlsx`, Google Drive linked from Park Seonghyeon's 2026-09-17 email (65 complete pulses, original 2022-12-15 test).
- `BM HEO 3 GITT 로우 데이터.xlsx`, same email linked Drive file (76 complete pulses, 2022-12-15 test).
- `HEO 3 Mg 로우 데이터.xlsx`, same email actual xlsx attachment (48 complete pulses, 2023-01-11 test).
- `BM HEO 3 Mg 로우 데이터.xlsx`, same email actual xlsx attachment (56 complete pulses, 2023-01-11 test).
- These are the numerical raw workbooks themselves, beyond PDF/PPT curve digitization or earlier assistant hand-drawn traces. All four were streamed from XLSX worksheet XML for reproducible current-sign pulse detection. Partial cutoff pulse excluded.

## Uniform descriptor definition
- Nominal applied current `100 mA g^-1`; each complete negative-current pulse ~600 s; ~3600 s rest.
- Use 3 s after interruption as initial rest voltage, final rest sample just before next current pulse as QOCV.
- `DeltaE_rest = abs(E_end - E_3s)`.
- `t63` first time reaching 63.212% of the **signed** E3s-to-end recovery, measured relative to the 3 s reference.
- HEO raw pulse25 t63 6.9875 min vs archived exact 7.000 min; BM raw pulse25 t63 11.803 min vs archived exact 11.8167 min. Agreement supports extraction validity at ~1-2 s scale. Values derive from actual original workbooks; the earlier hand-approximated figures are retired as scientific evidence.

## Candidate updated kinetic boundaries after pulse indices

| Material | Full negative 600-s pulses | Previous cumulative (L1/L3/L4) | Raw-based new proposal | Basis |
|---|---:|---|---|---|
| HEO | 65 | 6/25/56 | **6/25/55** | early t63 minimum at6, central minimum25, late max55 then downturn |
| BM-HEO | 76 | 9/38/60 | **9/38/60** | small early local minimum9 after initial rise, broad central minimum38, late maximum60 |
| Mg-HEO | 48 | 6/24/39 | **7/24/39** | early minimum7, central minimum24; late t63 does NOT turn down so QOCV slope break near39 |
| BM-Mg-HEO | 56 | 9/35/40 | **9/35/40** | early minimum9 after large initial rise, central minimum35; late t63 continues rising so QOCV slope break near40 |

- Current figure: `HEO_Figure4_All4_OriginalRaw_KineticLandmarks_2026-11-05.png/.pdf` and four pulse-level CSVs delivered as conversation artifacts (not committed binaries).
- Figures retain `DeltaE_rest` as an **auxiliary descriptor**; the boundary choices come primarily from t63 and, for Mg samples R4, from QOCV.
- BM initial t63 rises from pulse1 to7 before a minor dip around9, therefore the R1→R2 statement needs an operational clause to exclude initial transients and identify a sustained renewed increase; it is NOT literally the first positive slope from the earliest pulse.
- QOCV late change is gradual; Mg L4=39 and BM-Mg L4=40 remain sensitivity-dependent candidates. A fixed change-point scoring and ±pulse sensitivity audit across four raw datasets should precede publication.
- Cumulative boundaries are placed **after** the stated pulse index, so R2 begins with next pulse, R3 with next, R4 with next.

## Quantitative consequences if PI approves revised boundaries
Each shifted boundary transfers one complete-pulse nominal charge (16.667 mAh g^-1) between adjacent regions.

| Sample | R1 | R2 | R3 | R4 | mAh/g nominal first-lithiation GITT |
|---|---:|---:|---:|---:|---|
| HEO | 100.0 | 316.7 | 500.0 | 166.7 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 |
| Mg-HEO | 116.7 | 283.3 | 250.0 | 150.0 |
| BM-Mg-HEO | 150.0 | 433.3 | 83.3 | 266.7 |

- Milling (no Mg): R2 +166.7, R3 −133.3; milling (Mg): R2 +150.0, R3 −166.7.
- Mg (unmilled): R3 −250.0; Mg (milled): R3 −283.3.
- v12 Abstract and Figure 5 currently contain **old partition numbers** (e.g. BM R2 +133–167, R3 −150 to−167, Mg R3 −267 to−283). If new landmark choices are approved, update **all** Abstract/Table S1–S3/Figure 5/etc **together after PI explicit approval**. No silent changes.

## Source and reproducibility notes
Four raw xlsx files were obtained via user-connected Gmail or Google Drive linked in the collaborator's 2026-09-17 original email. Local raw extraction script `heo_extract_raw.py` and plotting script `heo_final_figure4_actual.py` plus pulse descriptors were provided in a downloadable data-and-diagnostics ZIP. The scripts use streaming worksheet XML because Mg-free spreadsheets exceed one million rows in total and include split sheets.

**Action:** PI review new real-data figure and provisional L1/L3/L4 positions. Preserve old approved manuscript/figures pending this decision.
