# HEO v22 — Word export and actual figure reuse QA, 2026-10-12

## Output identity
- **Word deliverable:** `HEO_Manuscript_V22_PI_Integrated_Figures1-6_2026-10-12.docx` (conversation-download artifact; binary file is **not** stored in GitHub by this update).
- Assembled from **existing October 11 v21 stage-origin-aligned Word** `HEO_MANUSCRIPT_V21_STAGE_ORIGIN_ALIGNED_2026-10-11.docx`, retrieved from Google Drive's `[Preparation]Park_HEO` folder. All six original embedded main figure PNGs were retained; not replaced with alternative regenerated plots.
- **Current PI-approved text authority:** `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md`.
- The PI-preferred Abstract was preserved verbatim. Introduction (four paragraphs), Results 2.2–2.6 and Conclusion were exchanged for corresponding v22 reviewed wording. Existing Section 2.1, Figure 1–6 PNGs and corresponding collaborator-related cautions, Experimental Section 4.1–4.4, and 20 historical reference entries remain in place as **provisional, not final-audited, material**.

## Figure and quantitative evidence integration

| Component | Export disposition |
|---|---|
| Figure 1: TEM/HRTEM, SAED, EDS | Reused October v21 inline PNG and existing collaborator-caveated caption. Final structure validation remains open. |
| Figure 2: BET and SEM | Reused October v21 inline PNG and caption. Final interpretation/metadata remains open. |
| Figure 3: voltage profiles and first-lithiation/delithiation bars | Reused aligned v21 inline PNG. Revised caption to fit the v22 materials-first story. |
| Figure 4: measured HEO t63, ΔErest, 60-min rest-end voltage and R1–R4 | Reused existing **already stage-aligned v21** PNG with L1/L3/L4, caption clarified. No L4 redefinition or new fitting. |
| Figure 5: HEO–BM-HEO three descriptors, stage fractions and regional median t63 | Reused existing **already stage-aligned v21** PNG; caption refers to established R2 ~29→38%. |
| Figure 6: BM-R2 / Mg-R3 one-dimensional sequence schematic | Reused existing v21 PNG; caption warns schematic is not direct phase proof. **Internal image still has dense/partially overlapping labels**, to improve in a subsequent artwork-only pass. |
| **Working Table 1** | Added **review-only** four-material GITT regional fractions: HEO 9.2/29.2/47.7/13.8; BM 11.8/38.2/28.9/21.1; Mg 12.5/37.5/31.2/18.8; BM-Mg 16.1/46.4/8.9/28.6%. Caption explicitly says **SI placement remains undecided**. This table uses the October 7 accepted numerical partition, and is not a reanalysis. |

- Existing figure images have the same data and meaning as the October aligned Word. No newly derived boundaries, microkinetic fits, inferred oxidation-state fractions or new experiments were added.
- The Table 1 percentages are **GITT-protocol shares**, not independent GCD percentages. Cross-composition differences remain based on the original region charges.
- Old September figure numbering and panel architectures must not supersede this October 11 aligned Word.

## Word quality assurance

- `python-docx` used to preserve original embedded PNGs in place while inserting new reviewed body text.
- Rendered using `/home/oai/skills/docx/render_docx.py` and visually inspected all **12** pages.
- Fixed figure-caption page separation by keeping image paragraphs with following captions. Kept the Conclusion heading with its entire final paragraph; verified all 6 images and the reference section remain.
- Main figure 6's original internal text overlap is a **source-artwork limitation**, not a page-rendering or export fault.
- No supporting-data experimental recalculations performed.

## Working limitations still visible

1. **Section 2.1 and Figures 1–2:** pending collaborator-verified quantitative XRD, ICP/stoichiometry, microscopy and BET conclusions.
2. **Experimental Section 4.1:** synthesis/electrode details are incomplete and clearly marked `[INPUT REQUIRED BEFORE SUBMISSION]` in the Word file.
3. **References:** 20 older entries were retained to avoid losing the existing bibliography, but v22 inline citation numbering and close-prior-art attribution need a dedicated audit. **Not citation-verified or submission-ready**.
4. **Figure 6:** artwork lettering/layout needs readability polish, but its scientific logic was preserved.
5. **Working Table 1** requires a Main-vs-SI placement decision; it is currently review-only.
6. **Methods/SI cross-references:** existing older references are provisional and require a final current-v22 synchronization.

## Current handoff decision

**Do not redo the L1/L3/L4 region partition or all figures.** Review the actual delivered v22 Word first. Next provide collaborator-confirmed Section 2.1/experimental metadata, improve Figure 6 schematic lettering, decide whether the quantitative table belongs in SI, audit citation numbering and finalize a minimal revised SI. Re-render Word after these small edits.

## Traceability

- `manuscript/HEO_EXISTING_FIGURE1_6_ASSET_REUSE_AUDIT_2026-10-12.md`
- `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md`
- `modeling/HEO_ORIGINAL_REGION_PARTITION_RECONSTRUCTION_2026-10-12.md`
- `manuscript/HEO_ABSTRACT_PI_PREFERRED_2026-10-12.md`
