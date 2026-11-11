# HEO — same-cell GITT cycles 1–3: preliminary source-data audit (2026-11-11)

## Status and scientific purpose

**INTERNAL RESEARCH NOTE; not an approved manuscript revision.** The PI clarified that **the same four cells have GITT over three full lithiation/delithiation cycles**. This permits a stronger question than the earlier first-lithiation-only R1–R4 analysis: do the initial region-specific modification effects persist in later reversible lithiation and delithiation, and how does the relaxation response evolve between cycles? **Keep technical complexity here; only promote a compact, well-supported scientific result to main text or SI after PI review.** Do not construct a new Word file without explicit request.

**Verified:** Each source has three complete current-direction pairs (−, +) followed by a *partial fourth lithiation* (−). The previous locked R1–R4 regional GITT charges are for complete pulses in **first lithiation only**. DO NOT project those same pulse indices onto later cycles or state that an R2 charge packet can be uniquely followed into subsequent delithiation. After initial conversion, oxidation/reduction mechanisms and voltage coordinates may differ.

## Source files and provenance

Existing HEO primary GITT raw spreadsheets used previously for t63 segmentation, newly re-read as full time/current streams:

| Material | Exact source file | SHA256 | Recorded source |
|---|---|---|---|
| HEO | `HEO GITT 로우 데이터.xlsx` | `4f3fcfc643adb5814902c5c503a73642635c34ed0ec2f5d362cd393f107c4cb2` | [Park Sep17 Gmail-shared Drive file](https://drive.google.com/file/d/1mYRsquXEmMg1beCvtOqrWXEoOdaU1YgR/view) |
| BM-HEO | `BM HEO 3 GITT 로우 데이터.xlsx` | `b5e27b1c31c581cec65954506f1c0cb2246a39682f53ea93c894349829176f54` | [Park Sep17 Gmail-shared Drive file](https://drive.google.com/file/d/1VpWKWk85ubxYFVEzY_8UNkCZL0LszGQN/view) |
| Mg-HEO | `HEO 3 Mg 로우 데이터.xlsx` | `1a3bbafa84a5583acb3d60dac073de2bbc717a538d2dd9814b0aadd7338411a5` | Park Sep17, 2026 Gmail attachment `HEO 데이터입니다.` |
| BM-Mg-HEO | `BM HEO 3 Mg 로우 데이터.xlsx` | `7a5650d2054b022940569e0ac56d95c0cd8c5fe8deaa9d40412ec9861f465661` | Same Gmail message |

HEO and BM-HEO split records across Excel `데이터_1_1` (1 million rows) and `데이터_1_2`; the stream was concatenated by row order. Mg sheets have one data tab, sampled predominantly at ~3s; Mg-free sheets ~1s. The first data-row header in the large Mg-free sheets is a *four-field header encoded as shared-string IDs*, not a current sample; exclude it. Current sign and within-file continuity must be tested before identifying cycles.

**Instrument evidence:** ~600-second constant-current pulse, ~3600-second rest; source e-mail explicitly corrected presentation-slide's stale `60초` rest to 60 minutes. Current negative lowers voltage (lithiation), positive raises voltage (delithiation). Approximate common voltage cutoffs 0.005V and 2.50V. No inference of electrochemical phase identity from current sign alone.

## Segmentation results — confirmed current-direction blocks

| Material | Cycle 1 lith/delith nonzero segments | Cycle 2 lith/delith | Cycle 3 lith/delith | Fourth lithiation |
|---|---|---|---|---|
| HEO | 66 / 46 | 43 / 45 | 43 / 45 | partial 14 |
| BM-HEO | 77 / 52 | 52 / 51 | 51 / 50 | partial 10 |
| Mg-HEO | 49 / 31 | 29 / 30 | 28 / 29 | partial 26 |
| BM-Mg-HEO | 57 / 35 | 35 / 34 | 33 / 33 | partial 19 |

Each **full first lithiation** contains 65/76/48/56 **complete 600s pulses** (HEO/BM/Mg/BM-Mg), plus a terminal **partial pulse** reaching the cutoff. This exactly explains why the complete-pulse regional-charge totals in the locked article (1083.3/1266.7/800.0/933.3 mAh/g) are smaller than half-cycle totals below. Each of cycles 1–3 reaches the cutoff; partial fourth-cycle data are excluded from comparisons.

## Half-cycle integrated nominal charge — exploratory, mAh g−1

These values integrate the **entire nonzero-current windows including partial cutoff pulses**, assuming the nominal **100 mA g−1** level, with interval length inferred from row count and sample spacing (1s Mg-free / 3s Mg-containing). They are preliminary and **not** replacement values for original complete-pulse R1–R4 charge; next final QA should check exact current-weighted time integration and sample active masses from tester logs.

| Material | Li 1 | delith 1 | Li 2 | delith 2 | Li 3 | delith 3 |
|---|---:|---:|---:|---:|---:|---:|
| HEO | 1094.2 | 762.3 | 715.0 | 746.3 | 710.5 | 742.9 |
| BM-HEO | 1278.5 | 858.5 | 860.9 | 840.8 | 844.4 | 827.6 |
| Mg-HEO | 814.3 | 515.7 | 476.1 | 495.2 | 462.8 | 478.5 |
| BM-Mg-HEO | 948.2 | 583.2 | 577.6 | 563.4 | 549.6 | 543.5 |

Paired differences (nominal mAh g−1, each cell's first three GITT cycles):

| Matched comparison | Li 1 | delith 1 | Li 2 | delith 2 | Li 3 | delith 3 |
|---|---:|---:|---:|---:|---:|---:|
| BM − HEO | +184.3 | +96.2 | +145.9 | +94.5 | +133.9 | +84.7 |
| BM-Mg − Mg | +133.9 | +67.5 | +101.5 | +68.3 | +86.8 | +65.0 |
| Mg − HEO | −280.0 | −246.6 | −238.9 | −251.1 | −247.7 | −264.4 |
| BM-Mg − BM | −330.3 | −275.4 | −283.3 | −277.4 | −294.8 | −284.1 |

**Direct finding:** milling's positive and Mg's negative net-capacity comparisons persist in both later lithiation and delithiation within these SAME GITT cells. The first-lithiation difference is larger than subsequent delithiation differences, confirming that some initial net gain/loss is associated with first-cycle-only or irreversible processes, but the regional source of that difference is not uniquely identifiable from totals. Later comparisons do not unambiguously trace first-cycle R2 Li into a specific delithiation interval.

**Internal warning:** A few nominal second/third half-cycle delith/lith ratios exceed 100% (HEO and Mg-HEO). Do not report such ratios as validated Coulombic efficiencies without confirming exact currents, mass, timing and tester normalization. The initial method uses a common nominal current, not actual current-weighted integration; per-stage ratio may be affected by partial cutoff pulses, side reactions and instrument conventions. The correct *direction* of paired sample comparisons is robust to small rounding.

## Pulsewise kinetic reconstruction

For every completed nonzero pulse followed by rest, compute:
- `E_3s` (3 seconds after current interruption) and final rest voltage `QOCV` (end of ~3600s rest);
- `ΔErest = abs(QOCV − E_3s)`, in mV;
- `t63` = first crossing of `E_3s + (1-e^-1) × (QOCV − E_3s)`; linear interpolation between sampled rest points, subtracting the 3s origin;
- retain all first/second/third lithiation and delithiation profiles separately. Exclude final cutoff pulses with no full rest from t63 curves.

**Cross-check:** first lithiation pristine-HEO pulse 26 `ΔErest=145.10mV`, pulse 50 `189.28mV`; agrees with existing November 6 R3-hump audit, validating extraction/3s convention.

To avoid comparing different states at the same pulse index, interpolate t63 and ΔErest as functions of **QOCV** over the same shared 0.20–1.40V range, in 0.05V steps. The following are mean absolute differences of interpolated two-curve values (MAE), **deterministic profile differences, not replicate uncertainties**.

### Successive lithiation: t63 and ΔErest (common QOCV interval)

| Material | t63 Li1→Li2 (s) | t63 Li2→Li3 (s) | ΔE Li1→Li2 (mV) | ΔE Li2→Li3 (mV) |
|---|---:|---:|---:|---:|
| HEO | 220 | **17** | 177 | **7.8** |
| BM-HEO | 105 | **12** | 142 | **4.0** |
| Mg-HEO | 272 | **14** | 117 | **5.7** |
| BM-Mg-HEO | 217 | **12** | 112 | **5.3** |

The **first→second shift is far larger than the second→third shift for all four materials**. After first lithiation/delithiation the later lithiation relaxation profiles largely overlap at matched measured QOCV, consistent with a large first-cycle evolution and a more reproducible later cycling state. This does **not** establish that R1 alone drives the evolution, or that four first-lithiation-defined reaction bins recur with identical chemistry/potential in later cycles.

### Successive delithiation: kinetic continuity

| Material | t63 delith1→2 (s) | t63 delith2→3 (s) | ΔE delith1→2 (mV) | ΔE delith2→3 (mV) |
|---|---:|---:|---:|---:|
| HEO | 37.9 | 9.5 | 6.3 | 1.9 |
| BM-HEO | 15.7 | 5.2 | 3.5 | 0.7 |
| Mg-HEO | 39.0 | 21.4 | 3.2 | 2.9 |
| BM-Mg-HEO | 22.5 | 24.1 | 2.8 | 2.1 |

The delithiation ΔErest profiles are much more stable already between cycles 1 and 2 than the first-lithiation profiles. t63 has modest changes, with BM-Mg showing a comparable cycle1→2 and cycle2→3 difference. Avoid overgeneralizing complete convergence for all delithiation metrics.

## Mechanistic interpretation, and limits

**Supportable interpretation:** The first lithiation gives a larger modification-dependent total charge and relaxation trajectory and appears to change the later electrochemical response. Despite losing some first-cycle-only charge, BM and Mg intervention effects continue in subsequent reversible cycling. First lithiation t63-landmark R1–R4 partition gives **where initial gains and losses occur**; repeat-cycle GITT demonstrates **whether the net effects are persistent**. Later kinetics in same cells become fairly stable by the second lithiation, across each material's different chemistry.

**Not yet proven:** A Li charge initially in R2 can be identified as the same charge removed on delithiation; R1 irreversible insertion is uniquely responsible for every lost charge; R3 Mg effect is only reversible conversion or only degraded material; later-cycle chemical species and structures are experimentally isolated; GITT stability proves 100-cycle stability. The first-cycle conversion may irreversibly reconstruct the spinel; redox pathways on delithiation may differ.

For any potential-resolved correspondence, use identical **QOCV windows** and explicit first-vs-later charge distributions; do not simply keep first-lithiation pulse-count boundaries fixed. A useful follow-up is to inspect whether the first-lithiation R2/R3 contributions have distinct **delithiation potential windows**, but unique process tracing will require physical support beyond total charge.

## Presentation recommendation — minimal manuscript changes

**Hold approved Abstract and Introduction, Figure1–6 structure, R1–R4 numerical boundaries and original Figure3 text unchanged for now.** First produce an INTERNAL compact same-cell cycle summary and one SI candidate: pulsewise lithiation `t63 vs QOCV` overlay (1st/2nd/3rd) for four materials plus a table of Li/delith total capacities over three cycles. Possible main-text inference should be **one concise paragraph** if the key effect is judged material. Do not add new central figures or extend manuscript scope by default.

Main paper story remains *modification-induced capacity gain/loss localized to initial electrochemical regions*; this 3-cycle result strengthens it by showing later electrochemical relevance and first-cycle kinetic restructuring. Keep detailed per-pulse and interpolation choices in internal notes or SI.

## Reproducibility and open verification

- Raw Excel files are not committed as binary datasets to GitHub; identify them by file names, source links and SHA256 above.
- Current-duration capacities from nominal current × sample count; rerun mass/calibration-aware time-weighted integration using actual timestamps and active masses before freezing exact values.
- t63/ΔE first crossing reconstructed from full rest arrays, not from a fitted distribution; validate a few second/third-cycle traces and any incomplete terminal rest.
- Comparison of curves at equal QOCV is an electrochemical coordinate comparison, not necessarily an equal SOC or identical phase.
- Other GCD 0.1C/100-cycle data are separate tests and must not be combined quantitatively into the same-cell GITT balance.
- No text has been inserted into the scientific Word by this analysis.

**Next decision after PI review:** if the first↔second relaxation shift and second↔third persistence are compelling enough, add one small SI display and one short Results sentence; otherwise keep as an internal robustness finding.
