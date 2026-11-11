# HEO — 2026-11-11 Figure 3 original-source audit, PI text changes and student requests

## Status
**Partial evidence-based revision; raw source-data gate remains.** The user moved scientific editing from a stray investment project conversation back to HEO and explicitly asked to check emails/data and revise the Figure 3 discussion. Current local reviewed Word after this audit:
`HEO_Manuscript_Fig3_SourceChecked_PI_Intro_2026-11-11.docx` (created in conversation environment; not committed as a GitHub binary). It integrates the PI-locked 2026-11-11 Abstract/Introduction and the present Section 2.1–2.2 wording. All six embedded figures and remaining nine highlighted requests retained. Starting Word was `HEO_Manuscript_Abstract_Integrated_v3_2026-11-11.docx`; original 35 native review comments, 2 addressed comments removed (BET id 15; return-to-baseline/featureless id 19), **33 retained**, with Figure 3 comment id 17 re-scoped to raw source needs. The render produced 13 pages and was inspected. Do not confuse this with the pre-Nov 11 native 45-comment source.

## Sources actually checked (not inferred from manuscript)
1. Park Seonghyeon's September 17, 2026 Gmail conversation `HEO 데이터입니다.` and follow-up `Re: HEO 데이터입니다.`. A correction explicitly confirms GITT is **600 s pulse + 3600 s rest**, although a slide in the September presentation still says 60 s (outdated slide label). This GITT correction does **not** determine the separate GCD protocol.
2. Drive PowerPoint `HEO 진행상황 (20260917).pptx` at [Google Drive](https://drive.google.com/file/d/1Sbodv7h-YegT4OeZgd12e3maNJzpTjh5/view). **Slide 9** contains FEC four-sample 100-cycle `0.1 C` plot, unnormalized capacity rate plot and normalized capacity-ratio rate plot. **Slide 10** contains four first-three-cycle voltage plots, including curves/legend, plus the original 1st Charging / 1st Discharging / ICE numerical table. These slides were rendered and directly checked, beyond mere filename inspection.
3. `Figure 구성 전 데이터.pptx` (July 30/Sep 17 email attachment) has structural/XPS but **does not** contain Figure 3 GCD cycle/rate primary numeric tables.
4. `Method and characterization_HEO (1).docx`, sent Sep 17, documents synthesis/physical characterization only; it does **not** establish FEC percentage, 1C current definition, cycling/rate raw tables or coin-cell electrochemical conditions.
5. Existing GitHub provenance records: `HEO_FIGURE3_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`, `HEO_V34_XPS_FIGURE3_VECTOR_REPLOT_WRITING_AUDIT_2026-11-05.md`, `HEO_V37_FIG3_COMMON_AXES_R3_RELAXATION_HUMP_AUDIT_2026-11-06.md`. Plots originate in embedded Origin OLE objects / PPT vector paths; these are more traceable than approximate screenshot redraws but are **not** original tester CSV/XLS exports.

## Results supported by source slides
- Slide 10 four first cycle table (first `Charging` / second `Discharging` labels in source; the physical interpretation `initial lithiation/delithiation` is retained **provisionally** until instrument convention is confirmed):
  - HEO: **901.25 / 609.12** mAh/g; ICE 67.59%.
  - BM-HEO: **1056.10 / 782.08**; ICE 74.05%.
  - Mg-HEO: **731.15 / 458.91**; ICE 62.766%.
  - BM-Mg-HEO: **944.07 / 580.83**; ICE 61.524%.
- Figure 3 matched first-lithiation **continuous GCD** changes remain: BM +154.85 no Mg, BM +212.92 with Mg; Mg −170.10 unmilled, −112.03 milled mAh/g. Separate GITT nominal-charge magnitudes differ; do not equate experiments. PI prefers no repetitive GITT/GCD disclaimers in regular prose, but Figure axes and exact methodological provenance must remain distinguishable; no false equality implied.
- Slide 9 clearly marks **0.1 C with FEC-containing electrolyte** on the 100-cycle curves (all four sample names) and shows rate-step sequence **0.1 → 0.3 → 0.5 → 1 → 3 → 5 → 0.1 C**, roughly five cycles per step. Exact FEC concentration and number of cycles per segment still require raw protocol export or experiment log.
- Original PowerPoint ratio/absolute-rate plots demonstrate marked capacity drop at higher C-rates and **substantial, incomplete recovery** on return to 0.1 C. The 0.1 C return curves stay below the initial 0.1 C values. Therefore the older exact claim `all four electrodes recover their baseline capacity` is unsupported and was replaced.
- Earlier v34 source-vector reconstructed 100-cycle approximate capacities are HEO **~415**, BM-HEO **~583**, Mg-HEO **~431**, BM-Mg **~492** mAh/g; valid **approximate graph-derived values**, not authoritative tester exports. Slide 9 plot visually supports the sample ranking and approximate values, not exact digits.
- Slide 10 explicitly labels curves `1 Cycle`, `2 Cycle`, `3 Cycle` for all four materials. Current Figure3 captions align. Original slide 10 calls the initial large-capacity half-cycle `Charging` and the reverse `Discharging` — request confirmation of true lithiation sign from test program before any irreversible nomenclature change.
- The existing Figure3 panels (e)/(f) are from FEC-labeled curves. Original chart legends/normalized curve order were previously rechecked in v34 (source color order HEO blue, BM red, Mg green, BM-Mg yellow); the manuscript repainted chart is NOT an instrument-export replacement.

## PI-approved Section 2.1 revised passages in current Word

### BET paragraph
> Ball milling substantially refines the particle and aggregate morphology, increasing the BET specific surface area by 4.6-fold from 3.94 to 18.16 m² g⁻¹ for the Mg-free pair and by 2.6-fold from 6.49 to 16.64 m² g⁻¹ for the Mg-containing pair (Figure 2a,b). This increase in gas-accessible surface area is consistent with the breakup of coarse secondary agglomerates into finer nanoscale particulates observed by SEM.

Removed prematurely introduced Mg sample total-capacity/BET comparison and capacity-causation claims. Changed `directly reflects` to `is consistent with` to distinguish N₂ gas-accessible surface from electrode electrolyte-accessible activity.

### XPS paragraph
> High-resolution XPS spectra provide information on the near-surface chemical states of the as-prepared powders (Figure 2c–i). The Ni 2p, Co 2p, Fe 2p, Mn 2p, and Cr 2p spectra exhibit characteristic signals of the constituent transition metals, with features potentially associated with different oxidation states. The Mg 1s signal near 1303 eV is observed in Mg-HEO and BM-Mg-HEO, confirming the presence of Mg within the XPS sampling depth. In the O 1s region (Figure 2h), all samples exhibit a dominant component near 529.8 eV, consistent with metal–oxygen bonding, and a higher-binding-energy contribution that may arise from surface hydroxyl groups and other oxygen-containing species.

**No** independent identification of Mg lattice site, mixed valence amounts, Cr(VI), O vacancies or binding-energy fits. Kept the yellow XPS calibrations/fit note and added a request for the spectral assignment **literature references**.

## Revised Figure3 caption (current Word)
> Figure 3. Galvanostatic electrochemical performance of the four HEO electrodes with an FEC-containing electrolyte: (a–d) first-three-cycle voltage profiles at 0.1 C for (a) HEO, (b) BM-HEO, (c) Mg-HEO, and (d) BM-Mg-HEO; (e) discharge capacity over 100 cycles at 0.1 C; and (f) rate capability at 0.1, 0.3, 0.5, 1, 3, and 5 C, followed by a return to 0.1 C.

## Revised 2.2 first paragraph (current Word)
> Galvanostatic measurements at 0.1 C show the net effects of ball milling and Mg incorporation on lithium storage (Figure 3a–d). The initial lithiation/delithiation capacities are 901.25/609.12 mAh g⁻¹ for HEO, 1056.10/782.08 mAh g⁻¹ for BM-HEO, 731.15/458.91 mAh g⁻¹ for Mg-HEO, and 944.07/580.83 mAh g⁻¹ for BM-Mg-HEO. Ball milling increases the first-lithiation capacity by 154.85 mAh g⁻¹ without Mg and by 212.92 mAh g⁻¹ with Mg. Conversely, Mg incorporation decreases the first-lithiation capacity by 170.10 mAh g⁻¹ in the unmilled state and by 112.03 mAh g⁻¹ after milling.

## Revised 2.2 second paragraph (current Word)
> This contrast is also evident in the cycling and rate-capability measurements (Figure 3e,f). After 100 cycles at 0.1 C, the discharge capacities are approximately 415, 583, 431, and 492 mAh g⁻¹ for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. The rate-capability curves show decreasing capacity with increasing C-rate and substantial, although incomplete, capacity recovery upon returning from 5 to 0.1 C. The broad, overlapping voltage features below 0.8 V in the first-lithiation profiles (Figure 3a–d) provide limited resolution of the individual processes responsible for the observed capacity differences. Pulse-resolved GITT measurements are therefore used to examine the lithiation response in distinct electrochemical regions.

## What the students need to supply — target only unresolved original evidence
**Priority P0 (Figure3 numeric reproducibility):**
1. Four original **cycler-exported** first-three-cycle V–capacity numeric source files (or actual Origin .opju/.opj project with workbook numerical tables), with material/cell IDs and protocol/cycle sign definition. Confirm 901.25 etc belong to the plotted same four cells, and clarify source `1st Charging / Discharging` vs manuscript's `lithiation / delithiation`. Confirm old May 8 shutdown/restart artifact is absent from the latest selected four traces.
2. Four original FEC **100-cycle capacity vs cycle** numeric outputs; identify exactly what `discharge capacity` means in the tester (lithiation vs delithiation); confirm 100th-cycle values and same/replicate cell correspondence.
3. Four original FEC **rate-capability** cycle-by-cycle tables and cycler program/step file; verify 0.1/0.3/0.5/1/3/5/0.1 C, approximately 5 cycles each, initial/final 0.1 C comparison and recovery ratios.

**Priority P1 (comparability & methods):**
4. Common electrolyte composition, **FEC additive percentage by mass or volume**, lithium salt/solvent and formation history for Fig3 a–f; confirm all four samples tested at matched conditions and whether any plotted panel mixes no-FEC with FEC.
5. **C-rate reference** (e.g., nominal specific capacity defining 1 C and resulting mA/g), cutoff 0.005–2.5 V, temperature, electrode loading, active fraction, each cell ID, and any capacity normalization or per-pulse correction.
6. Source files for Figure3's editable Origin plot **if raw tester CSV unavailable**. The currently accessible PPT embeds Origin OLE plots, but source/reproducible values remain unavailable.

**Separate ongoing P1 (Section2.1, from earlier comments):**
7. Original calibrated batch-matched Ni/Co/Fe/Mn/Cr/O/Mg XPS spectra and peak fits; charge reference, per-peak assignments and specific citations, confirmation of any repeat after July 30 unusual Cr~579 eV batch.
8. Actual Mg precursor/composition, XRD/ICP, HRTEM d-spacing and wrong `CoGa₂O₄` indexing; original native source plots for BET/SEM if available. These remain under previous yellow data holds.

**Source caveats:** Earlier 2026-09-17 HEO PPT itself has a stale `60s rest` annotation; the student explicitly corrected this by email to 60min for GITT. Do not use the stale slide label. All comments and paper-level mechanisms beyond 2.1/2.2 remain under review.

## Next use
1. Use the PI-lock [2026-11-11 Abstract and Intro](HEO_2026-11-11_PI_LOCKED_ABSTRACT_INTRODUCTION_AND_DECISION_LOG.md).
2. Use this source-checked §2.1/2.2 text as the current **reviewed** version.
3. Upon receipt of student test exports, calculate exact paired GCD and cycle/rate recovery (each sample), replace approximations if warranted, and redraw/QA Figure3(e)/(f) from source.
4. Keep SI, figure captions and raw chemistry claims aligned; do not silently replace the accepted t₆₃-only 6/25/55;9/38/60;7/24/42;9/35/46 boundaries.
