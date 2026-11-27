# HEO — current manuscript and SI integration state, 2026-11-27

**Current state:** Word manuscript and SI integrated for PI review; not submission-ready. This supersedes the Nov 23 proposed-prose and figure-planning state. The PI explicitly requested completion of the next stage and GitHub update. No new experiments or FEM.

## Read in this order

1. [Integrated Results/Discussion §§2.3–2.6, Conclusion, Figure 4–6 captions, synchronized GITT methods and refs 25–27](manuscript/HEO_2026-11-27_INTEGRATED_RESULTS_DISCUSSION_AND_CONCLUSION.md).
2. [Integrated SI text and tables S1–S11 with captions S1–S12](manuscript/HEO_2026-11-27_INTEGRATED_SI_TEXT_AND_TABLES.md).
3. [Nov 11 PI-locked Abstract/Introduction](manuscript/HEO_2026-11-11_PI_LOCKED_ABSTRACT_INTRODUCTION_AND_DECISION_LOG.md). The entire baseline through §2.2, including first three figures, was preserved exactly; edits require PI decision.
4. [Nov 23 evidence and source gates](manuscript/HEO_2026-11-23_REFERENCE_CLAIM_AND_SUBMISSION_GATE_AUDIT.md), [prior handoff (historical)](START_HERE_CURRENT_STATE_2026-11-23.md), [Nov 11 Fig3 source check](manuscript/HEO_2026-11-11_FIGURE3_SOURCE_CHECK_AND_STUDENT_DATA_REQUESTS.md).
5. [Reproducibility scripts and file instructions](modeling/2026-11-27/README.md). [Yoon Lab writing constitution](https://github.com/tyoon-lab/Yoon-Lab-Publication-Toolkit/blob/main/MANUSCRIPT_VOICE_CONSTITUTION.md) controls prose.

## Current Word deliverables (retrieve by exact filename from PI-accessible files)

- `HEO_Manuscript_Integrated_2026-11-27.docx`, based on the actual Nov 11 Word `HEO_Manuscript_Abstract_Introduction_Revised_2026-11-11.docx`. Review copy; original preserved. The actual baseline has 27 native comments (IDs 0–26), **not** the older Nov 7 45-comment audit count. All original comment XML parts and highlighted text preserved; anchors in replaced passages are mapped to relevant new prose. First 29 manuscript paragraphs verified XML-identical; figures 1–5 retained byte-identical. Figure 4/5 captions clarified, figures unchanged.
- `HEO_SI_Integrated_2026-11-27.docx`, based on `HEO_SI_v22_KineticBoundaryTextClean_2026-11-06.docx`. Preserves S1–S6 graphics and tables; S7 literature source numbering synchronized by DOI/author name; includes S8–S11, Figures S7–S12 and Tables S7–S11.
- `HEO_Figure6_SI_2026-11-27.zip` (figure assets, pulse-level derived data, source hashes and reproducibility scripts; raw XLSX not included). Word binaries, private comments, and raw XLSX/pulse tables are deliberately not uploaded to public GitHub.

## Scientific conclusions and conventions

- C1 four operational t63 regions, after-pulse boundaries: HEO 6/25/55; BM-HEO 9/38/60; Mg-HEO 7/24/42; BM-Mg-HEO 9/35/46. R2 gain for milling +166.7/+150.0 mAh g−1, R3 loss −133.3/−116.7; Mg R3 charge loss −200.0/−183.3. The boundaries differ from chemistry-specific assignments.
- Main Figure 6a,b: whole-half-cycle nominal GITT charge, includes terminal partial pulse. Fig 6c: cumulative complete-pulse charge divided by the total fully rested pulse charge. Fig 6d: measured C3 t63 vs rest-end QOCV. C1–C3 are sequential histories in one cell per material, not independent repeats.
- Figures S7/S8: lithiation/delithiation trajectories C1–C3; S9 C2 delithiation; S10 conditional C2→C3 cumulative distribution residuals; S11 conditional waveform shape; S12 literature-guided operational region context replacing the former causal conceptual main Fig6.
- C3 delithiation milling redistributes normalized charge contribution toward 1.05–1.40 V and away from 1.40–1.70 V in both Mg groups; direction is reproduced in C2. Whole-half-cycle denominator RMSE shift-only→shift+redistribution 0.01436→0.00867 and 0.00967→0.00420; rested-only sensitivity 0.01654→0.01142 and 0.00931→0.00303.
- Primary t63 is first crossing measured from the 3 s reference to 63.212% of the signed 3–3600 s recovery. Potential-matched C3 t63 increases +81.6/+52.1 s for milling (3–3500 s archival alternative +81.2/+50.3 s). Separate 10–3500 s normalized waveform analysis: ΔF300 −3.05/−2.03 percentage points; time stretch and nonlinear voltage-shape alternatives yield nearly equivalent conditional fits. This does not identify elementary reaction kinetics or improve absolute-voltage prediction.
- S7/S8 total counts: 1020 complete rested pulses (282,327,190,221), 24 half-cycle nominal totals. Figures 4/5 complete pulse boundaries; nominal 100 mA g−1, 16.6667 mAh g−1 per full pulse. Distinguish GITT charge from GCD capacities. Exact material mass/current normalization not resolved.

## Outstanding submission gates (existing-source review, not new experiments)

1. HRTEM CoGa2O4 label in Fig1 for nominal Ga-free composition: source FFT/d-spacing/indexing verification or removal before submission.
2. Mg stoichiometry/actual synthesis, XRD/ICP availability, XPS charge/energy calibration and assignment, BET degassing, electrode loading/current normalization, cell and electrolyte/FEC protocol, cutoff and test metadata. Preserve yellow holds; use actual source records only.
3. Figure3 original numerical data, cycle/rate sign and partial rate recovery; source figures remain locked.
4. All pre-existing refs 1–24 kept to avoid breaking locked prose; new refs 25–27 added. Current visible citations exclude 1–3, 13–14, 16–18; final PI/journal citation ordering and unused-entry cleanup after approval. DOI/author verification for new references completed; S7 literature references use author and DOI rather than stale numbers.
5. PI review of new §2.3–2.6, Conclusion, captions and SI; no journal selected. Only after source holds and PI review are closed prepare submission-specific reference and formatting pass.

Future repository updates only on explicit PI request.
