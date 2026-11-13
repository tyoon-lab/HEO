# HEO — Matched-QOCV raw GITT relaxation test, C1 vs C2/C3 (2026-11-13)

**INTERNAL WORKING ANALYSIS, NOT A MANUSCRIPT EDIT.** PI directed continued testing of hump-centered recurrence hypothesis and requested raw voltage-rest relaxation comparison at a shared quasi-open-circuit voltage, ~0.90 V. Existing first-lithiation t63-based R1–R4 segmentation, Abstract, Introduction, Word MS and figure numbering remain unchanged.

## Purpose and precise scope

At an **identical measured rest-end QOCV** (0.85, 0.90, 0.95 V), compare full 3–3500 s current-interruption voltage recovery curves from C1, C2 and C3 lithiation within the **same original electrode/cell** for HEO/BM-HEO/Mg-HEO/BM-Mg-HEO. A fixed voltage removes one trivial source of variation in earlier hump comparisons, but **does not establish equal lithium content, phase identity, rate-limiting step or identical electrochemical reaction**. In this dataset GITT halfcycles and cutoffs differ significantly in Q(V).

## Input and provenance
- Reopened all four original GITT XLSX source reports in the conversation's working container: `HEO GITT 로우 데이터.xlsx` (HEO), `BM HEO 3 GITT 로우 데이터.xlsx`, `HEO 3 Mg 로우 데이터.xlsx`, `BM HEO 3 Mg 로우 데이터.xlsx`. Same source files used in earlier three-cycle raw GITT audits, with full 600-s nominal current pulses followed by ~3600-s rests. This analysis reads raw time/voltage/current records, not merely previously calculated t63.
- Streaming XLSX XML parsing with duplicate sheet-boundary treatment, separating lithiation/delithiation by actual current sign across direct sign reversals, selecting only fully rested negative-current lithiation pulses. Voltage traces were drawn from **two pulses bracketing each target QOCV**, linearly interpolated pointwise to 0.85, 0.90 or 0.95 V **on a common 3–3500 s time grid**. All reported measurements at exactly 0.90 V are interpolated, not independently measured at that exact rest voltage.
- Define `A=E(3500s)-E(3s)`, `F(t)=(E(t)-E(3s))/A`, and `t63=first crossing of 1-exp(-1) ≈0.6321`. This consistent 3500s endpoint differs slightly from the original author's near-3600s derived values. More dense and low-noise raw records allow linear time interpolation. If comparing numerically with earlier paper, recompute with a common endpoint.
- Code in local conversation workspace: `HEO_QOCV_matched_raw_relaxation.py` and `HEO_C1_QOCV_matched_extract.py` (per-sample source extraction), `HEO_QOCV_matched_plot_and_validation.py`, `HEO_C1C3_QOCV_plot.py`. Data CSVs include `HEO_C1C3_QOCV_matched_relaxation_metrics.csv`, `HEO_C1C3_QOCV_matched_relaxation_grids.csv`, `HEO_C1C3_QOCV0p90_capacity_positions.csv`, `HEO_C1C3_QOCV0p90_shape_RMSE.csv`, plus source pulse QA. PNG/SVG visualization `HEO_C1C3_QOCV0p90_normalized_2x2`, `HEO_C1C3_QOCV0p90_absolute_2x2`, `HEO_C2C3_QOCV0p90_cross_material_shapes`, and `HEO_C2C3_QOCV_matched_voltage_sensitivity`. Files are local conversation artifacts, not GitHub binary commits.

## Main 0.90 V results

| sample | C1 t63 (s) | C2 t63 | C3 t63 | C1 |ΔErest| (mV) | C2 |ΔErest| | C3 |ΔErest| | C1 recovery fraction by 300s | C2 | C3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| HEO | 629.5 | 548.4 | 565.1 | 325.4 | 135.2 | 147.3 | 0.494 | 0.512 | 0.504 |
| BM-HEO | 687.1 | 570.3 | 585.8 | 276.6 | 142.7 | 150.2 | 0.475 | 0.497 | 0.491 |
| Mg-HEO | 746.2 | 545.8 | 541.6 | 249.1 | 127.7 | 136.8 | 0.438 | 0.509 | 0.512 |
| BM-Mg-HEO | 796.5 | 542.1 | 549.0 | 269.0 | 141.9 | 150.3 | 0.420 | 0.508 | 0.505 |

**Measured temporal behavior:**
1. At fixed 0.90 V, later-cycle C2/C3 **t63 of all four materials clusters at ~542–586 s** and normalized full-rest shapes are surprisingly similar: C2 sample-vs-HEO normalized full-curve RMSE is 0.000 (HEO), 0.00983 (BM-HEO), 0.00141 (Mg-HEO), 0.00577 (BM-Mg-HEO). These RMSE values are on unit normalized F(t), not voltage units.
2. Within a sample, C2/C3 full shape RMSE is HEO 0.00550, BM-HEO 0.00382, Mg-HEO 0.00148, BM-Mg-HEO 0.00194. **C2/C3 are same-cell sequential cycles, not independent replicates.**
3. At same voltage, C1 **has both a larger 3–3500s voltage recovery magnitude** (~1.84–2.30× C2/C3 mean) and a **longer t63**. The *additional* C1 vs C2/C3 mean t63 is HEO ~73 s; BM-HEO ~109 s; Mg-HEO ~202 s; BM-Mg-HEO ~251 s. Thus first-to-later change is not merely a shift of the voltage coordinate. But reaction state differs at equal QOCV so this does not isolate chemical mechanisms.
4. All samples' C3 absolute recovery amplitude is ~5–9% higher than C2 at 0.90 V. Their t63 changes need not have the same sign.
5. The same directional trends broadly remain at 0.85 and 0.95 V. Later-cycle t63 there ranges ~536–606 s and C1 is generally slower, so result is not peculiar to picking exactly 0.90 V.

## Crucial state/composition caveat

At QOCV 0.90 V, nominal cumulative **first vs later lithiation** passed charge is very different (mAh/g, approximate linear pulse interpolation):
- HEO: C1 ~76.9, C2 ~324.7, C3 ~317.0.
- BM-HEO: C1 ~270.7, C2 ~373.6, C3 ~361.4.
- Mg-HEO: C1 ~113.5, C2 ~172.6, C3 ~176.6.
- BM-Mg-HEO: C1 ~189.6, C2 ~213.9, C3 ~216.2.

Notably C1 HEO at 0.90 V is within t63-defined R1, while C1 BM-HEO lies within R2; this is **not** a state-matched comparison of equivalent conversion reaction. These state differences may be the physical point of the first-cycle structural reconstruction hypothesis, but cannot be used to claim equal lithiation depth or a unique transfer of R2/R3 modifications to later cycle capacity.

## What it says about hump hypothesis and t63 region segmentation

- **Supports:** A reproducible after-formation response exists: all four C2/C3 raw relaxation curves show closely related *normalized time dependence* at 0.90 V despite substantial total capacity differences and distinct broad |ΔErest| hump voltages. First-cycle C1 at same voltage is a distinct dynamic response. This is compatible with an initial pristine-spinel-specific reaction history followed by a broadly shared later-cycle relaxation response.
- **Does not establish:** 0.90 V/|ΔErest| hump is a unique reaction identity; an invariant microscopic kinetic process; the C1 R1–R4 region meanings are incorrect; the specific initial R2 ball milling capacity gain or R3 Mg loss directly becomes later-cycle post-hump charge. The common shape may reflect the **same test's long 3500 s window, common generic relaxation kernel, finite-window normalization, transport coupling, or conversion-product response**; must challenge this against a null/sensitivity control.
- **Scientific distinction:** initial C1 t63 regional partition = empirical lithiation segmentation; later-cycle hump + ~0.90 V dQ/dV landmark = recurring *observational* feature. These serve different purposes; direct identity is a hypothesis.

## Recommended next internal discriminator

1. Compare C2/C3 **shape** at potential 0.85–0.95 V **against a broader voltage scan** (0.5–1.3 V) to test whether all normalized GITT rest curves are already almost identical independent of the 0.90 V landmark. If generic shape invariance holds broadly, then the 0.90 V feature's mechanism-specific diagnostic value is limited even if the dQ/dV peak is real.
2. Quantify **absolute amplitude and its voltage derivative** together with local differential capacity versus QOCV; these may retain modification-specific information lost by normalizing the kinetic kernel.
3. Directly compare the four samples' matched C2/C3 response to first-cycle R1/R2/R3 location with no forced equivalence of composition at equal potential; only consider manuscript addition after PI evaluation.

**No manuscript/Word edits.**
