# HEO v35: four-sample t63-only region boundaries, red-marked late shoulders (2026-11-06)

## PI decision and provenance
The PI supplied an annotated four-sample Figure 4 screenshot marking a shallow shoulder in each Mg-containing t63 trace. They instructed use of **t63 only** for all R1–R4 boundaries, retaining finite-window voltage-recovery amplitude (ΔErest) and 60-min QOCV as **supporting plotted observables**. The prior late-Mg QOCV-knee criterion is superseded.

The red-marked features align with **Mg-HEO pulse 42** and **BM-Mg-HEO pulse 46** in the 2026-09-17 original GITT raw-workbook descriptors. Specifically:
- Mg-HEO: t63 pulse42=12.66120 min, pulse43=12.64028 min, change −0.02092 min (−1.26 s).
- BM-Mg-HEO: pulse46=13.48898 min, pulse47=13.45971 min, change −0.02927 min (−1.76 s).

Both changes are smaller than the nominal 3-s sample spacing; they are interpreted as **operational shoulders** rather than robust sharp kinetic maxima or unique chemical phase boundaries. The kinetic-only rule is therefore a visual t63 turning/shoulder criterion rather than a uniquely recovered global change-point algorithm. A sensitivity check with independent ±1-pulse perturbations is essential.

## Reconciled working region boundaries (after pulse)
| Sample | Full pulses | L1/L3/L4 | R1/R2/R3/R4 charge, mAh g^-1 |
|---|---:|---|---|
| HEO | 65 | 6/25/55 | 100.0 / 316.7 / 500.0 / 166.7 |
| BM-HEO | 76 | 9/38/60 | 150.0 / 483.3 / 366.7 / 266.7 |
| Mg-HEO | 48 | **7/24/42** | 116.7 / 283.3 / 300.0 / 100.0 |
| BM-Mg-HEO | 56 | **9/35/46** | 150.0 / 433.3 / 183.3 / 166.7 |

The sum of complete nominal 10-min/100-mA-g^-1 pulses is unchanged across a given sample: 1083.3/1266.7/800.0/933.3 mAh g^-1 for HEO/BM/Mg/BM-Mg. These GITT pulse allocations are distinct from conventional continuous-current discharge capacity.

## Updated signed contrasts (R1/R2/R3/R4, mAh g^-1)
- BM-HEO − HEO: +50.0 / +166.7 / −133.3 / +100.0 (total +183.3).
- BM-Mg-HEO − Mg-HEO: +33.3 / +150.0 / −116.7 / +66.7 (total +133.3).
- Mg-HEO − HEO: +16.7 / −33.3 / −200.0 / −66.7 (total −283.3).
- BM-Mg-HEO − BM-HEO: 0.0 / −50.0 / −183.3 / −100.0 (total −333.3).

Milling R2 increment remains the main positive contribution. R3 milling losses are −117 to −133 mAh g^-1, offset partly by R4 gains. Combined R3+R4 milling charge *decreases* by 33.3 or 50.0 mAh g^-1; a literal transfer of the same chemical process from R3 to R4 has not been independently demonstrated.

Mg incorporation causes its largest single negative regional charge in R3 (−183 to −200 mAh g^-1), with additional R4 losses. This is a charge accounting result: molecular/phase mechanism remains literature-informed hypothesis.

## 3^6 boundary sensitivity across matched pairs (729 independent ±1-pulse combos each)
- Milling R2 increases in **729/729** scenarios for both composition pairs.
- Milling R3 decreases in **729/729** scenarios for both composition pairs.
- Mg R3 decreases in **729/729** for both processing pairs.
- Mg R3 is **strictly** the largest negative regional contribution in unmilled **729/729** and milled **702/729 (96.3%)** scenarios.
- Milling R1+/R2+/R3−/R4+ full sign motif in Mg-free **729/729** and Mg-containing **648/729 (88.9%)** scenarios (Mg-containing R1 can be zero).

This is deterministic boundary robustness, **not repeat-sample statistical uncertainty**.

## Generated local artifacts (conversation attachments, no binaries committed to GitHub)
- `HEO_Manuscript_v35_t63Only_RegionReassigned_2026-11-06.docx` — 14 rendered pages, Figures 1–6, **all 15 prior Word comments preserved** byte-for-byte.
- `HEO_SI_v19_t63Only_ShoulderBoundaries_2026-11-06.docx` — 4 rendered pages with updated SI Tables S1–S3 and t63-only Methods.
- `Figure4_All4_t63Only_v35.png/.pdf` and `Figure5_NewBoundaryCharge_v35.png/.pdf` — figure derivatives from original pulse-level CSV, not traced/designed mock measurements.
- Reproducibility script `build_v35.py` and `boundary_results.json` in conversation working output `/mnt/data/heo_v35_work/`.

## Main manuscript edits
- Abstract: kinetic-only t63 region wording; BM R2 +150–167, BM R3 −117 to −133 and Mg R3 −183 to −200; source Introduction P3 last sentence minimally reconciled to t63-only assignment.
- §2.3 and Figure 4/caption: R1/R2/R3 derived from t63 minima and L4 from peak (Mg-free) or shoulder (Mg-containing). QOCV and ΔErest remain plotted but are supporting observables.
- §2.4, Figure 5, SI Tables S1–S3: all absolute and signed quantities reallocated and independently ±1-pulse audited.
- §2.5–2.6, Conclusion, Figure 6 caption: regional charge primary, early milling and late Mg t63 changes secondary; R4 gain discussed as charge redistribution/continued charge access, not uniquely identified reaction migration or chemically proven conversion.
- Existing v34 XPS/Figure 3 vector-replotted images and other figures unchanged; XPS Cr2p assignment, figure1 CoGa2O4 index and missing Mg synthesis/electrode provenance remain pre-submission verification items.

**Status:** updated v35 manuscript + v19 SI ready for PI review. The late t63 shoulders are small and their exact location is operational. No arbitrary chemical phase assignment made.