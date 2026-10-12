# HEO Figure 1–6 REAL ASSET reuse audit — 2026-10-12

## Basis and correction

This audit inspected the **actual embedded raster figure images and captions** in the latest *stage-origin aligned* existing Word manuscript, rather than only reading historical September artwork notes.

**Actual inspected file:** `HEO_MANUSCRIPT_V21_STAGE_ORIGIN_ALIGNED_2026-10-11.docx` (Google Drive file `1gwWYW4UbCLWPxrXcsVnlOO8ndwsAml66`, 4,384,125 bytes; https://docs.google.com/document/d/1gwWYW4UbCLWPxrXcsVnlOO8ndwsAml66/edit).

Its DOCX package contains **six embedded PNG figures**, all visually inspected in the order Figure 1–6. This materially corrects the earlier `HEO_V22_FIGURE3_6_EVIDENCE_AUDIT_2026-10-12.md` judgment based solely on the **old September figure descriptions**. Figures 4–6 **already have October stage-origin-specific versions embedded in v21 Word**. Do not replace them automatically with newly plotted alternatives. The existing images have not been declared production-final; this is a reuse audit.

**Current body-text authority:** `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md` (October PI-reviewed prose). The v21 Word is the closest existing **Figure 1–6 visual basis**. Distinguish prose authority from visual authority.

## Actual Figure-by-Figure inventory

| Figure | What was directly seen in v21 Word (six embedded PNGs) | Compatibility with current v22 | Minimum next action |
|---|---|---|---|
| **1 — TEM/HRTEM/SAED/EDS** | Four-material microscopy/electron diffraction/elemental mapping panel; HEO, BM-HEO, Mg-HEO, BM-Mg-HEO | Supports sample characterization in Section 2.1, but **collaborator structural/composition finalization remains open** | Confirm final microscopy indexing, composition/EDS, quantitative XRD elsewhere, attribution. Reuse image if validated. |
| **2 — BET/SEM** | Four-material surface-area comparison plus four SEM representative fields | Directly useful for Section 2.1; figure already exists | Recheck area numbers and sample mapping and final caption; not a request to redo structural measurements. |
| **3 — first-cycle profiles/capacity bars** | Four first-cycle voltage profiles and initial lithiation/delithiation bar chart | **Direct fit** for v22 Section 2.2 | Keep. Check image legibility, axis sizes, original voltage-profile provenance, and half-cycle orientation. The latest *Word* figure does **not** show the older Sep design's extra cycling/rate panels; do not insist on adding them merely because the Sep artwork note mentioned them. |
| **4 — pristine HEO R1–R4** | Stacked `t63(z)`, `ΔErest(z)`, `Erest,60min(z)` with three dashed landmark lines and bottom R1/R2/R3/R4 conceptual bands | **Direct fit** for v22 Section 2.3; exactly the requested region-resolution concept is already plotted | Retain existing plot/data. Check dashed L1/L3/L4 correspondence and make boundary labels/endpoint convention legible; check stability and manuscript definitions. **No alternate L4 fitting.** |
| **5 — BM versus HEO** | Three first-lithiation state-dependent HEO/BM relaxation-voltage profiles; horizontal stacked 4-region fractions (R2 29→38%; R3 48→29%); per-region median t63 | **Direct fit** for v22 Section 2.4; central numerical evidence is already in the image | Retain. Connect **original signed regional GITT capacity changes** (BM R2 +166.7 mAh g⁻¹, R3 −150) in SI table or small inset if needed; check labels/legend/readability. Do not recompute region segmentation. |
| **6 — horizontal R1→R4 BM/Mg summary** | One horizontal four-stage reaction coordinate, BM arrow at R2 with 29→38% change, Mg arrow at R3 with 48→31% change, qualitative physical assignments and t63 remark | **Narrative fit** for v22 Sections 2.5–2.6, but currently a *schematic*, not independent four-sample 2×2 quantitative proof | Retain underlying concept. Improve overcrowded/overlapping small labels, remove oversized redundant heading, tie explicit **both Mg contrasts** and **BM in both compositions** to a compact evidence table/SI. Do not invent mechanistic phase proof. |

## Latest reuse decision

**Figure 3–5: preserve and lightly revise. Figure 6: preserve the reaction-sequence schematic and improve clarity and explicit numerical support. Figures 1–2: preserve working art pending collaborator verification.**

This is much smaller than the earlier blanket recommendation to redraw all Figures 4–6. Recreating Figure 4/5 without first checking the embedded Word images was unnecessary, and the recently generated draft plots should be treated as numerical QA illustrations, not replacement final figures.

## What can remain unchanged

- The agreed L1/L3/L4 stage boundaries, R1–R4 definition, previously audited ±1-step robustness, and old four-material region-partition percentages.
- PI-preferred Abstract and integrated v22 Main prose unless a real mismatch emerges.
- Previously generated state-resolved Figure 4 and Figure 5 embedded in v21 Word, their source data trends and sample color-order (pending cosmetic/citation verification).
- Old September apparent-D mismatch, excess/dQdV localization, cycling-history, microkinetic code and figures can remain archived as historical support; **do not automatically insert them all into SI**. Select only those that directly support the v22 narrative without introducing excess material or conflicting historical model R1–R4 labels.

## Actual open gates (without new numerical analysis)

1. Verify the Figure 4 dashed physical boundaries against the **accepted existing** cumulative-pulse allocations (HEO inferred 6/25/56); do not derive new boundaries.
2. Figure 5 already plots fractions and t63. Provide a single companion signed GITT region-delta table/plot from `modeling/HEO_ORIGINAL_REGION_CONTRASTS_2026-10-12.csv`, mainly to support the phrases “largest positive R2 change” and “largest negative R3 change.”
3. Figure 6 **has no direct four-material data panel** in the embedded image: add an economical SI or main table documenting both BM and Mg contrasts, or include small quantitative subpanel only if needed. Its schematic alone cannot verify cross-composition robustness.
4. Check readability, typography, non-bold panel labels, left/bottom ticks and legends in the existing six PNG images. Fig 6 has visibly dense and partially overlapping text.
5. Confirm Figure 1–2 collaborator XRD/refinement, Mg composition/processing, mapping, BET, and materials claims before finalization.
6. Use the existing Word captions as the **figure-caption starting point**, but align final captions with the v22 text. Do not cite old September figure numbers without confirming the October Word.
7. Continue full Experimental/metadata and SI reindex *after* minimal figure alignment rather than starting a new analysis project.

## Repository source/asset status

- GitHub contains numerous `.md`, `.csv`, and `.py` analysis/figure source records and September historical designs, but **no embedded 2026-10 Word PNG set in the tracked GitHub tree** as of this audit.
- Existing v21 Word file on Drive is a concrete six-image visual source and can be reused. This audit did **not** create new production art or edit the Word file.
- Figure 3 final standalone PNG/PDF and vector-derived CSV were separately confirmed in the user's Library, under `HEO_Figure3_final_2026-09-28.*`. The v21 Word's embedded Figure 3 (four profiles plus bars) should take precedence for **current panel allocation** over older September four-panel descriptions.
- Existing September plotting scripts in GitHub, including `modeling/heo_figure4_capacity_kinetics_mismatch.py`, `modeling/heo_figure6_history_dependence.py`, and `modeling/heo_figure7_microkinetic_existence_proof.py`, belong to earlier story variants. **Do not assume these scripts regenerate current v21 October Figure 4–6 images.** Regeneration-code/provenance for the current stage-origin-aligned embedded images remains to be identified (only if art editing necessitates it).

## Takeaway

**The scientific story and the aligned main figure suite already coexist in the existing Oct 11 Word draft.** Finish by reusing, polishing, and supporting these graphics, not by recomputing previously agreed region segmentation or rebuilding the entire Figure 4–6 suite.
