# HEO L3/L4 raw-data re-audit — 3 of 4 samples (2026-10-12)

## Status

**PRELIMINARY / NOT FOR FINAL PUBLICATION NUMBERS.** This audit reprocessed three first-lithiation datasets from original Excel workbooks. BM-HEO raw data have **not** been recovered, so the four-sample L4 boundary rule, the BM-dominant R2 absolute capacity gain, and the crossed 2×2 capacity partition are **not closed**. Do not silently overwrite `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md` or historical 29/38/48/31% figures with the candidate values below.

## Source provenance

- **HEO:** `[GITT try 2_031].xlsx`, Google Drive file ID `1Lbh5tWYQBmx1O3EdrDZhcfBX8ZH2EPCG`. Embedded original path: `HEO GITT TRY 4_cyc/20221215/GITT try 2_031.wrd`. 1,264,853 total rows (two data worksheets).
- **Mg-HEO:** `HEO 3 Mg 로우 데이터.xlsx`, Sept. 17, 2026 email `HEO 데이터입니다.`, original `HEO Mg GITT.cyc`.
- **BM-Mg-HEO:** `BM HEO 3 Mg 로우 데이터.xlsx`, same email, original `BM HEO 3 Mg GITT.cyc`.
- **Missing:** standalone BM-HEO first-lithiation raw Excel workbook, needed for four-sample gate. Historical name: `BM HEO 3 GITT 로우 데이터.xlsx`.
- Excel importer failed on 1.26-million-row HEO workbook, so immutable XLSX archive sheets were extracted via streaming XML. No original file was modified. Current work session generated pulse-level numerical CSVs and diagnostic plots.
- The HEO data-source identity is corroborated by the previously published-working nominal conversion-associated excess peak: HEO pulse 50, Erest 0.527481 V. Mg-HEO pulse 38, 0.386972 V; BM-Mg-HEO pulse 37, 0.502865 V also exactly reproduce archived voltage-coordinate audit (`HEO_FIGURE5_VOLTAGE_COORDINATE_AUDIT_2026-09-27.md`).

## Common extraction and data basis

- Select **first lithiation** from first negative-current pulse until onset of positive-current delithiation, excluding cutoff-truncated final pulse.
- HEO: 65 full pulses; Mg-HEO: 48; BM-Mg-HEO: 56.
- 600 s nominal current pulse, followed by 3600 s rest. 3 s post-current reference for `ΔErest = |E60min − E3s|`; `t63` from first crossing of 63.2% of signed 3s–60min relaxation.
- State `z` is normalized within each *GITT first-lithiation* sequence, not across independent GCD capacities. Protocol-derived full-pulse totals, computed from logged current/time and nominal 100 mA g⁻¹ mass inference: HEO ~1081.5, Mg-HEO ~796.0, BM-Mg-HEO ~928.7 mAh g⁻¹. **These are not independent GCD totals**, and the cutoff-truncated pulse is omitted.
- L3 operational candidate: `t63` minimum in central `0.15 < z < 0.70`. This is not microscopic completion of one reaction.
- L4 operational candidate: fit the 60 min rest-end voltage `E(z)` with a *continuous broken-stick* function
  `E(z)=a+b z+c max(0,z−z_L4)`, scanning candidate discrete pulse positions from five states after L3 until there remain five or more points after the break. Minimize unweighted voltage residual sum of squares, fitted over states beginning at L3 and excluding the final two full pulses. These objective fit settings must be frozen and justified across all four samples before using L4 for main text.
- Sensitivity: repeat fit with start at L3−2, L3, L3+2 and with 2, 3, 5, 7 terminal full pulses excluded (12 combinations per sample).

## Numerical results (new reanalysis, not current v22 authority)

| Sample | Full pulses | L3 (pulse; z) | L4 nominal (pulse; z; V) | L4 sensitivity pulse range | Provisional R3 share |
|---|---:|---|---|---|---:|
| HEO | 65 | 25; 0.385 | 53; 0.815; ~0.49 | 50–53 | 43.08% |
| Mg-HEO | 48 | 24; 0.500 | 37; 0.771; ~0.403 | 34–37 | 27.08% |
| BM-Mg-HEO | 56 | 34; 0.607 | 39; 0.696; ~0.47 | 38–40 | 8.93% |

Provisional R3 shares were calculated from the pulse fractions between L3 and L4, excluding the L3 boundary pulse, including the L4 boundary pulse. Range under sensitivity for fixed L3:
- HEO ~38.5–43.1%
- Mg-HEO ~20.8–27.1%
- BM-Mg-HEO ~7.1–10.7%

**Important discrepancy with prior figures:** Current working v22 numbers `HEO R3 ≈48%` and `Mg-HEO R3 ≈31%` arise from prior boundary choices, not these new candidate knee fits. The sign of the HEO→Mg R3 fractional contrast remains negative across the tested L4 fit variations, **but** the absolute shares and exact quantitative partition are still boundary-dependent. The nominal BM-R2 29→38% result cannot be independently revalidated because the BM-HEO raw workbook is missing.

## L3 cross-descriptor offset — additional audit

The central extrema do not co-locate exactly across modifications. Within `0.15 < z < 0.70`:

| Sample | t63-min pulse | ΔErest-min pulse | Minimum absolute rest-voltage slope, Savitzky–Golay windows 5–11 |
|---|---:|---:|---|
| HEO | 25 | 25 | 29–30 |
| Mg-HEO | 24 | 18 | 20–21 |
| BM-Mg-HEO | 34 | 39 | 29 |

The slope minimum and the maximum of `dQ/dErest` are derived from the same 60 min voltage trace. These pulse offsets mean that **coincident minima should not be claimed for all samples**. In the v22 Section 2.3, phrase the L3 illustration explicitly as the **pristine HEO reference** and inspect the other materials' landmarks separately. Do not infer that an internal elemental conversion stage shifts by the pulse difference alone. A single frozen operational rule is necessary for comparative capacity partitioning.

## Reasoning and limitations

1. Continuous two-slope regression supplies an **explicit reproducible candidate** for L4 where the post-plateau voltage decline steepens; it is not uniquely mandated by electrochemical thermodynamics. Broader/shorter windows change the knee index.
2. The BM-Mg-HEO knee appears only five full pulses after its t63 minimum, giving an unusually short candidate R3 interval. This is a genuine **definition-sensitivity / assignment gate**, not evidence for disappearance of all microscopic late conversion.
3. Near-flat E(z) and a peak in dQ/dE(z) are two descriptions of the **same voltage curve**, not independent confirmations.
4. Late-stage t63 can be unreliable when the total post-current voltage signal approaches noise; no automatic microscopic rate assignment is made.
5. The recorded conversion-associated excess-relaxation peak at pulse 50/38/37 is distinct from L3 at pulse 25/24/34.
6. No new structural identification of oxide reconstruction, metallic nucleation, Li₂O fraction, Mg coordination or interfacial reaction rates follows from this fit.
7. Large-file ingestion and extraction were done without modifying source Excel files; a final reproducible sample identification and mass normalization audit are still needed.

## Diagnostic artifacts produced in the working session

- `HEO_Fig4_three_signal_PRELIMINARY.png/.pdf`: HEO `Erest,60min`, `ΔErest`, `t63` stacked on common first-lithiation coordinate with L3 and proposed L4; **not a final Figure 4 because L1 and all-sample comparison are missing**.
- `HEO_GITT_L4_three_sample_knee_diagnostic.png/.pdf`: three-sample voltage-knee fit.
- `HEO_R3_sensitivity_three_sample_PRELIMINARY.png/.pdf`: candidate R3 fractions, explicitly preliminary.
- `HEO_GITT_L4_three_sample_candidate_summary.csv` and `HEO_GITT_L4_three_sample_sensitivity.csv`: numerical summaries.
- Three individual first-lithiation pulse CSV files `HEO_from_Drive_try2_first_lithiation_pulses.csv`, `Mg_HEO_first_lithiation_pulses.csv`, and `BM_Mg_HEO_first_lithiation_pulses.csv`.

These artifacts are local conversation outputs, **not assumed to be on GitHub**, and binary images have not been committed through the UTF-8 contents API.

## Immediate next step

Recover `BM HEO 3 GITT 로우 데이터.xlsx`. Then rerun the exact same segmentation and candidate L4 procedure across all four, freeze objective L1/L3/L4 rules, compute four-by-four GITT regionwise fractions/absolute deltas and boundary sensitivity, and redraw final Figure 4–6 with synchronized captions. Do not change the PI-approved Abstract prematurely.
