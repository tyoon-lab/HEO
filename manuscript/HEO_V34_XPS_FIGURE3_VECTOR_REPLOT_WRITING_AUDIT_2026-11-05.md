# HEO manuscript v34: source-replotted XPS, electrochemical Figure 3 and language audit (2026-11-05)

**Status:** New PI-review Word manuscript `HEO_Manuscript_v34_XPS_CyclingReplotted_Polished_2026-11-05.docx`, 14 rendered pages; all 15 prior Microsoft Word comments retained verbatim (comments.xml identical to v33, 15 anchors/references). Word is a conversation artifact, not a file committed in this repository. Companion source-plot extraction ZIP: `HEO_v34_Figure2_3_SourceVectorData_and_Code.zip` (conversation artifact).

## Sources and figure provenance

- `Figure 구성 전 데이터.pptx`, slide 8: the **current four labeled samples** (HEO, BM-HEO, Mg-HEO, BM-Mg-HEO) each have a Cr 2p measured curve and reported total fit stored as editable PDF vector paths after slide export. These path vertices have been extracted and the four spectra directly replotted, normalized within spectrum and vertically offset; both pairings appear in Figure 2(c,d). Graph coordinates are **not the original XPS instrument count files**.
- Slide 8 also has spectra from earlier students and other HEO compositions. They were EXCLUDED as unmatched controls. In particular, the slide itself warns that the Cr 2p feature near ~579 eV, historically attributed to Cr(VI), appears exceptionally in a recent batch. Do not present such a chemical-state assignment as fact. Current Figure 2 presents measured envelopes and provisional archived total fits, not confirmed Cr(III)/Cr(VI) quantitative deconvolutions.
- Figure 2(a,b) reproduces the original BET plot and matched four micrographs as high-resolution exports from source slides 2 and 7; no fabricated points.
- `HEO 진행상황 (20260917).pptx` slides 9–10: all four sample 0.1 C charge/discharge voltage traces for cycles 1–3, 100-cycle FEC discharge capacity and FEC rate curves were extracted from **PPT vector plot paths** and redrawn into Figure 3(a–f), 2×3 arrangement. Exported graph curves are not equivalent to original cell instrument data.
- IMPORTANT corrected attribution: cycle plot vector-path order is HEO (blue), Mg-HEO (green), BM-HEO (red), BM-Mg-HEO (yellow), **not** the label order. Figure 3(e) was repaired accordingly. Approximate cycle-100 FEC capacity (graph-digitized) HEO ~415, BM ~583, Mg ~431, BM-Mg ~492 mAh g−1.
- Previous Figure 3 caption erroneously specified Coulombic efficiency in panel (e). **Current Figure 3(e) plots discharge capacity only**; caption and §2.2 corrected. Non-FEC cycle traces were extracted to sidecar CSV/PNG for possible SI use without enlarging the main six-panel figure.
- The Figure 2 BET upper panel comes from graph export not independent raw numeric replot, and Figure 3 current exports must be validated against instrument numeric originals before journal submission.

## Manuscript changes

- Figure 2 and Figure 3 graphics replaced with high-resolution source-derived replots and matching captions.
- §2.1 revised to quantify BET changes and present the supported Cr 2p spectral comparison with calibrational restraint; no inferred unique elemental oxidation state, no inference of lithiation products from as-prepared XPS.
- §2.2 gives numeric 100-cycle FEC capacities directly as approximate graph-reconstructed values and describes rate return.
- §2.3 and §2.4 original kinetic boundary/region-charge definitions and values preserved.
- §2.5, §2.6 and Conclusion revised to follow toolkit preferences: direct measured observation → quantitative region charge → literature-supported physical interpretation; remove repetitive negative/defensive/dev-history sentences. Regional charge remains primary capacity finding and relaxation-trajectory differences the subordinate kinetic evidence.
- PI-approved Introduction maintained; Abstract v13 boundary-consistent text maintained. Source document v33 remains untouched.
- Toolkit sources applied: `profiles/PI_WRITING_PROFILE.md`, `workflow/MANUSCRIPT_LANGUAGE_AND_CLAIM_CALIBRATION.md`, `prompts/MASTER_PROMPT.md`, and `figure_tools/STYLE_SPEC.md`.

## Remaining items for final submission

1. Obtain original **XPS instrument count data** and energy referencing; confirm recent batch repeatability, Cr 2p multiplet fit assignments and optional 579 eV component. A recurring 579 eV signal is visible in current spectra, but its oxidation-state identity requires independent check.
2. Obtain original cycling/rate numeric exports, rather than depending on faithful vector reconstruction of archived plots.
3. Resolve TEM `CoGa2O4` attribution despite Ga absent from precursor list; verify relevant d-spacing/indexing.
4. Confirm Mg-containing synthesis/electrode/cell metadata and electrolyte FEC fraction from independent experimental record.
5. Release a submission-clean copy with resolved existing 15 comments only after source confirmation and PI approval.

This document records verified replot provenance and editorial decisions. Its scientific conclusions do not overwrite the accepted kinetic-region boundary audit in the v33 integration record.
