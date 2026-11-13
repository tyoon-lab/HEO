# HEO — First-lithiation horizontal-shift test against second/third lithiation (2026-11-13)

**Status: Exploratory internal test; NOT a manuscript-approved mechanism assignment.** The PI hypothesizes that approximately 200–400 mAh/g of initial pristine-spinel-specific charge during C1 might precede a partially recurring conversion response. To test whether the visible later |ΔErest| hump reflects a repeatable later process, apply **one common horizontal charge shift** to C1 lithiation, comparing simultaneously its t63, absolute voltage-recovery amplitude |ΔErest|, and rest-end quasi-open-circuit voltage QOCV with the near-coincident C2/C3 lithiation trajectories.

## Data provenance and equation
- Source in current conversation runtime: previously extracted/audited four-material, three-cycle GITT full-rest pulse dataset `HEO_GITT_C1_C3_joined_lith_delith_throughput.csv`. This dataset contains pulse-wise `sample`, `halfcycle`, `capacity_mAh_g`, `t63_s`, `deltaErest_abs_mV`, and `QOCV_V`. Four materials: HEO, BM-HEO, Mg-HEO, BM-Mg-HEO.
- Full 600s pulses only, nominal 16.67 mAh/g each; **the pulse partial at cutoff is NOT included**. Thus full-pulse C1/C2 total charge differences may differ slightly from earlier total-charge/partial-pulse analyses.
- Set `Qaligned,C1 = Q1 - ΔQ`; C2/C3 remain at original within-lithiation cumulative charge. Look for **a single ΔQ that reduces error in all three observables**.
- Scan ΔQ=200–450 mAh/g in 5 mAh/g increments; additionally scan 0–500 as a sensitivity check.
- To eliminate the artificial preference for larger shifts by shortening the overlap, all 200–450 candidates per sample use the **same fixed capacity comparison window** `x = linspace(max(35, 0.1*Qmax), Qmax, 150)`, where `Qmax = min(QC2,end,QC3,end,QC1,end-450)-25`. The plotted curves show the whole available range; quantitative score is on this fixed window.
- For each property compute `RMSE` between `C1(Q+ΔQ)` and `[C2(Q)+C3(Q)]/2`. Normalize each property's RMSE by its C2/C3 mean trajectory 5–95 percentile range, with lower-floor scales 80 s, 40 mV, 0.2 V, respectively. Joint score = root mean square of the three squared normalized RMSE values. **Equal relative score weighting is an operational choice and does not uniquely identify ΔQ.**
- Secondary test: shape-only matching removes a separate constant vertical offset *per property* before scoring. This is a sensitivity check only; the raw, actual voltages and characteristic times are NOT matched by that model.
- Script in conversation runtime: `/mnt/data/HEO_first_lithiation_horizontal_shift_test.py`; summary: `/mnt/data/HEO_C1_shift_alignment_summary.csv`; scan: `/mnt/data/HEO_C1_shift_alignment_scan_scores.csv`. These artifacts/PNGs **are not currently added as binaries to this GitHub repository**.

## Absolute-value matching — best common ΔQ 200–450

| Sample | Combined optimum ΔQ (mAh/g) | RMSE t63 (s) | RMSE |ΔErest| (mV) | RMSE QOCV (V) | C2 vs C3 trajectory RMSE t63 / |ΔErest| / QOCV |
| --- | ---: | ---: | ---: | ---: | --- |
| HEO | **200** (search lower bound; global 0–500 best 185) | 98.7 | 35.2 | 0.349 | 19.2 s / 9.9 mV / 0.0078 V |
| BM-HEO | **325** | 155.9 | 21.8 | 0.267 | 14.9 s / 5.4 mV / 0.0146 V |
| Mg-HEO | **285** | 123.2 | 32.1 | 0.460 | 8.9 s / 8.7 mV / 0.0161 V |
| BM-Mg-HEO | **325** | 202.7 | 15.5 | 0.365 | 10.1 s / 7.6 mV / 0.0075 V |

Scores improve substantially vs **no shift** in all four samples, but matched C1 remains **farther from C2/C3 than C2 and C3 are from one another**. Thus this is a *partial* phenomenological alignment, not successful registration of identical first-/later-cycle responses.

Individual-optimum ΔQ, by property (same 200–450 search):
- HEO: t63 225, |ΔErest| 200, QOCV 200.
- BM-HEO: t63 200, |ΔErest| 450, QOCV 200.
- Mg-HEO: t63 265, |ΔErest| 395, QOCV 200.
- BM-Mg-HEO: t63 370, |ΔErest| 235, QOCV 200.

**These independent optimum shifts are inconsistent**, a direct test against strong `single extra C1 process, otherwise unchanged later response` model.

## Data-grounded physical capacity-difference check

From the *complete-pulse-only* total lithiation charge, `Q_C1 − (Q_C2+Q_C3)/2` gives:
- HEO **383.3** mAh/g
- BM-HEO **425.0** mAh/g
- Mg-HEO **341.7** mAh/g
- BM-Mg-HEO **383.3** mAh/g

When C1 is shifted by **these observed capacity differences**, which automatically aligns the *ends* of lithiation, a joint-score improvement relative to zero shift remains for all samples, but substantial mismatches persist:
- HEO: t63 RMSE 163.8 s; |ΔErest| RMSE 39.2 mV; QOCV RMSE 0.388 V
- BM-HEO: 184.8 s; 13.0 mV; 0.300 V
- Mg-HEO: 136.0 s; 30.5 mV; 0.482 V
- BM-Mg-HEO: 198.3 s; 21.1 mV; 0.405 V.

The PI's hypothesis of a large initial-only charge component remains **plausible**, but simple horizontal capacity subtraction **does not** bring full t63, |ΔErest| and QOCV responses into coincidence.

## Sensitivity checks
- Shape-only optimum (if a different constant vertical offset is permitted *for each observable*): HEO **450**, BM-HEO **300**, Mg-HEO **450**, BM-Mg-HEO **450** mAh/g (upper-bound solutions in 3/4). Hence an apparently successful registration can be manufactured by relaxing amplitude conditions; avoid calling this proof of recurring identical chemistry.
- Restricting the raw matching to the latter **50%** of a fixed comparison window gives joint best ΔQ HEO 200, BM-HEO 360, Mg-HEO 200, BM-Mg-HEO 260, again differing. Curve-shape/voltage choices affect the inferred shift.
- The C2/C3 curves are **sequential observations in the same cell**, not independent replicates. Their near-coincidence does show after-initial-cycle repeatability of this response.
- In particular, QOCV and t63 absolute values cannot be aligned well simultaneously; a matching local |ΔErest| hump on its own does not identify the same phase/reaction, or prove the first 300–400 mAh/g were a single irrecoverable chemical step.

## Scientific interpretation and next question
- **Supported:** There is a substantial first-cycle extra lithiation throughput; the subsequent C2/C3 curves are very similar; a substantial horizontal registration makes some response features more comparable.
- **Not supported as a unique result:** first C1 after ΔQ subtraction is identical to C2/C3, or one-to-one recurrence of a specific reaction located at an |ΔErest| hump.
- **More useful refined hypothesis:** initial pristine-spinel insertion/rearrangement/conversion creates extra charge and changes the subsequent energy landscape and relaxation weights; the reconstructed material thereafter cycles on a more stable, partially related but **nonidentical** path. The contribution may be distributed over first R1–R4; do not assign the entire total difference to R1/R2 without region-specific independent evidence.
- **Recommended next internal test:** examine first-cycle and later-cycle **rest-voltage-matched or end-of-lithiation-referenced** windows, and the 3s–3600s relaxation curve spectra in candidate hump regions. Quantify position, amplitudes and relative time components before proposing any new chemically labeled region, and check compatibility with the PI-locked first-cycle four-region analysis.

**Word/main manuscript, Abstract, Introduction and figure numbering were NOT modified by this analysis.**
