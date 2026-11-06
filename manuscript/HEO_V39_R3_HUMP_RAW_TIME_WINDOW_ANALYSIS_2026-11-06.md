# HEO v39: R3 recovery-hump raw-data validation and manuscript integration (2026-11-06)

**Status:** Analysis executed on four ORIGINAL GITT XLSX time-voltage-current workbooks (no graph digitization), and resulting physically calibrated discussion integrated into manuscript v39 and SI v20. Author-approved `t63` segmentation, Abstract quantitative claims, Introduction and regional charge results unchanged.

**Generated conversation files (not binary-committed here)**
- `HEO_Manuscript_v39_R3_Hump_TimeResolved_2026-11-06.docx` (14 rendered pages; no comments)
- `HEO_SI_v20_R3_RelaxationWindow_2026-11-06.docx` (9 rendered pages, Tables S4/S5 and Figures S4/S5/S6)
- `HEO_R3_Hump_RawGITT_TimeWindow_Analysis_2026-11-06.zip` (all pulse-window CSVs, selected raw rest curves, plotting/extraction Python code and PNG/PDF figures)

## Exact method
Four source GITT workbooks `HEO GITT 로우 데이터.xlsx`, `BM HEO 3 GITT 로우 데이터.xlsx`, `HEO 3 Mg 로우 데이터.xlsx`, `BM HEO 3 Mg 로우 데이터.xlsx` were streamed from worksheet XML (245 complete negative-current 600-s pulses total). Rest voltage at 3, 60, 600 s after last current-on sample and final ~3600 s rest was linearly interpolated. Parts: (E60-E3), (E600-E60), (Eend-E600), sum=Eend-E3. Cross-checked total amplitude and QOCV against the accepted original pulse descriptors for every pulse (max amp error ~2e-13 mV, QOCV ~5e-8 V).

Selected locked kinetic (L1/L3/L4) after-pulse boundaries: HEO 6/25/55; BM-HEO 9/38/60; Mg-HEO 7/24/42; BM-Mg-HEO 9/35/46.

## Hump result
In pristine HEO, from R3 start pulse 26 to peak pulse 50, total ΔErest rises 145.0955→189.2816 mV (+44.1861 mV):
- first minute (3–60 s) 40.8224→31.0373 mV (**−9.7851**)
- 1–10 min 59.6283→76.1407 (**+16.5124**)
- 10–60 min 44.6448→82.1036 (**+37.4588**)
- late fraction increases **30.77%→43.38%**; reaches 45.92% at R3 endpoint pulse55. The largest positive hump contribution comes from delayed recovery, NOT a proportional increase across all time intervals.
- Mg-HEO mild R3 interior hump start 109.1657→peak 117.7277 mV (pulse38; +8.562 mV); Mg-HEO early −1.99, mid +3.67, late +6.88 mV.
- BM-HEO total R3 declines 163.5956→136.5335 (pulses39→60); BM-Mg-HEO 135.7690→116.0458 (36→46). Late fractions still rise 39.72→47.37% and 40.77→43.61%, respectively.
- Thus late-time **relative** fraction increases in all four, whereas the distinctive large **absolute** amplitude hump is seen in pristine only. A new individual exponential/phase cannot be inferred.

## Independent local QOCV-slope check
Interpolated at common QOCV=0.50 V (inside all four R3 ranges):
- HEO ΔE 185.47 mV / |dQOCV/dQ| 0.829 mV/(mAh/g)
- BM-HEO 142.63 / 1.142
- Mg-HEO 109.47 / 0.339
- BM-Mg-HEO 134.47 / 0.880
Thus HEO > BM in amplitude despite HEO < BM in local equilibrium-like voltage slope. A fixed internal Li redistribution with purely slope-amplified voltage cannot by itself account for this paired contrast. The redistribution itself is unmeasured and may differ; matched QOCV is not matched chemical state.

## Physical interpretation and external references
- **Primary compatible hypothesis:** spatially heterogeneous successive reduction or restructuring leaves a delayed relaxation contribution near pristine-HEO R3. Analogous GITT and spatially heterogeneous FeF3 conversion: Li et al., JACS 2016, 138, 2838–2848 DOI:10.1021/jacs.6b00061 (**new ref [28]**). Spinel Fe3O4 phase coexistence during lithiation: He et al., Nat Commun 2016, 7, 11441 (existing [22]). Fe3O4 phase-transformation-mediated slow relaxation model: Knehr et al., Electrochimica Acta 2017, 238, 384–396 DOI:10.1016/j.electacta.2017.04.041 (**new ref [29]**).
- **Secondary alternative:** locally varying QOCV–charge slope and redistribution magnitude. Different voltage recovery cannot uniquely identify new reaction modes without inversion, spatially resolved phase probes, or constraints.
- Keeps priority hierarchy: signed region charge (Figure 5) is primary explanation of overall capacity changes; R3 hump is a secondary kinetic/voltage-recovery fingerprint.

## Manuscript and SI
- Main §2.3 extended with explicit time-window and rise/fall numbers; §2.5 reworked into physically anchored FeF3/Fe3O4 hypothesis + constrained voltage-slope alternative; bibliography appended [28] and [29]. Abstract and confirmed t63-only boundaries unchanged.
- SI v20 §S6 documents time window method; Table S4 includes four samples' start/peak/end amplitudes; Table S5 shows 0.48 and 0.50 V matched-QOCV amplitudes; Figures S4–S6 show window-separated R3 amplitudes, absolute rest traces, normalized rest traces.
- Word files rendered and page layout checked. No comments.

**Next optional scientific question:** finite-window multiexponential spectral fits could test whether a distinct late mode emerges, but an unconstrained fit might be non-identifiable; current demonstration does not claim a unique new time constant.