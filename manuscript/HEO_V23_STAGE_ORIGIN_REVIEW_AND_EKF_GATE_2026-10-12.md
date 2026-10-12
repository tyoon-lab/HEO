# HEO v23 scientific-review release and EKF gate — 2026-10-12

## Authority and output
- Working target: Advanced Functional Materials.
- Abstract authority **unchanged**: `manuscript/HEO_ABSTRACT_PI_PREFERRED_2026-10-12.md`. Its three paragraphs were verified byte-for-byte unchanged between the 12-page v22 and new v23 Word.
- GitHub text snapshot v22 remains the baseline; new Word review draft `HEO_Manuscript_V23_StageOrigin_Reviewed_2026-10-12.docx` (conversation artifact, not committed as binary) contains the next editorial corrections. This document records them so nothing silently supersedes the approved abstract.
- Focused new SI: `HEO_SI_V15_StageOrigin_Focused_Review_2026-10-12.docx` (conversation artifact, not in GitHub).
- New Figure 6: `HEO_Figure6_v23_stage_origin.png` and source SVG/plot code (conversation artifacts). The original October stage-origin Figures 1–5 were retained; six embedded figures remain in v23.
- The main Word rendering was visually inspected at 12 pages; the focused SI was inspected at 4 pages. Word QA: main 6 images/0 tables, SI 3 reused supplemental images/3 tables; legacy four-material table moved from Main to SI, original v14 SI left unmodified as archive.
- Disclaimer: These are scientifically reviewed PI proofs, **NOT submission-ready files**.

## Revision decisions
1. Intro retains materials/conversion identity and original approved Abstract, but more carefully distinguishes literature-established multistep chemistry from this study's new electrochemical stage attribution. A 60-minute rest-end voltage is a standardized state coordinate, not proved equilibrium.
2. Section 2.1 stops asserting unverified structural metrics. It describes existing TEM/EDS, SEM and BET art and explicitly waits for quantitative collaborator XRD/refinement, composition, Mg recipe, surface area and specimen identity.
3. Section 2.3 now explains why a shallow rest-end plateau and the nonunique voltage-relaxation response are consistent with overlapping conversion/reconstruction while not independently proving oxide bond breaking or any unique elementary product. L3 minima in t63 / ΔErest mark changes in the measured response; do **not** establish phase completion or faster microscopic Li diffusion. R2 oxide destabilization/reconstruction, R3 continuing evolution toward reduced metal/Li2O-derived states: **broad literature-guided associations only**.
4. Section 2.4 strengthens numerical BM evidence: pristine HEO→BM-HEO R2 29.2→38.2% of nominal GITT total, signed nominal ΔR2 +166.7 mAh/g. R2 is the **largest positive regional** increment, not necessarily the largest absolute increment across every comparison.
5. Section 2.5 Mg result: pristine HEO→Mg-HEO R3 47.7→31.2%, signed nominal ΔR3 −266.7 mAh/g, largest negative regional change; no unique Mg-site or local bond-energy inference.
6. Section 2.6 contains four-material replication: BM Mg-free +166.7, BM Mg-containing +133.3 in R2; Mg without milling −266.7, Mg with milling −283.3 in R3 (nominal protocol GITT mAh/g). Positive/negative components may cancel. **Do not** multiply GITT regional shares by separately measured GCD capacities.
7. Figure 6 is an uncluttered *single horizontal* R1→R2→R3→R4 scheme. BM connects to R2, Mg to R3; numerical examples are nominal protocol-derived. The footer correctly labels v23.
8. SI v15 is reduced to: S1 characterization placeholders; S2 GITT definitions/provenance; S3 three tables: original accepted region charges and percentages, all four signed contrasts, the archived ±1-pulse landmark sensitivity; S4 three reused original cycle/GITT/percentile-control images; S5 limitations and remaining input. Superseded Dapp/microkinetic modeling remains archived in old SI v14, not a necessary part of current submission companion.
9. Original 2026-10-07 four-material R1–R4 partition remains the authoritative working partition. Inferred pulse-index endpoints for HEO/BM/Mg/BM-Mg: (6,25,56), (9,38,60), (6,24,39), (9,35,40); these are arithmetic reconstructions from rounded old tables, **not** newly recovered raw boundary measurements. No experimental broken-stick L4 redefinition.

## EKF experiment and gate
An independent, first-lithiation pristine-HEO time-domain exploration analyzed 65 full-pulse current-off traces from `[GITT try 2_031].xlsx`, nominal 100 mA/g, 600 s pulse, 3600 s rest. Nonnegative finite-window distributed exponential fit was applied to normalized voltage relaxation, not to modal charge. A spectrum-only four-region algorithm suggested cuts near pulse 21/39/56 rather than established 6/25/56. Among 27 fit/window variations, the final cut generally falls near 54–57, but early boundaries lack stable agreement with L1/L3. Changes in regularizer/bin/window also change detailed component weights. Thus the pilot does **not** improve four-stage assignment or identify individual chemical phases. **Decision: omit EKF maps from HEO AFM Main and SI**, retain classical GITT descriptors and literature-constrained assignments, reserve pristine HEO for cross-chemistry GITT time-domain paper. Full pilot: EKF repository `03_LFP/HEO_PRISTINE_GITT_TIME_DOMAIN_PILOT_2026-10-12.md`.

## Pending external verification before submission
- Final collaborator quantitative XRD/refinement, ICP/EDS verification, Mg synthesis recipe and material mapping. Do not fabricate site, composition or degree of amorphization.
- Experiment: cell format, voltage reference/cutoffs, electrolyte, current collector, coating formulation, active loading, thickness, separator, electrolyte volume, temperature/formation, replicate counts and actual source record.
- Retrieve `BM HEO 3 GITT 로우 데이터.xlsx` or original signed primary pulse-boundary record to independently confirm the old BM segmentation; consistently document the L4 plateau-end criterion across four materials. Working regional capacity estimates remain preliminary/nominal without that check.
- Final publisher-by-publisher verification of all 20 citation entries and the link between each mechanistic/material-specific claim and its reference. Partial checks: DOI 10.1002/advs.202201219 (Luo 2022 operando XAS), 10.1039/D0RA00255K (Chen et al. 2020 Mg-containing ball-milled spinel), and 10.1016/j.jpowsour.2026.240338 (Jorkesh et al. 2026) confirmed; **full reference audit incomplete**.
- Figure1–2 final captions and collaborator acceptance; Figure3 electrochemical source mapping; Figure4–5 original endpoint annotations; finalized main/SI cross-reference count and SI archive/provenance; final AFM template, title and proof.

## Stage-origin guardrails
- This is a **materials** paper (BM mainly R2, Mg mainly R3), not an independent GITT inversion novelty.
- Voltage recovery t63 describes the time needed to reach 63.2% of the measured 3s-to-60min relaxation; ΔErest its magnitude; 60-min voltage a rest-end coordinate.
- Four electrochemical regions do not imply four independently observed microscopic products.
- Keep modifications (BM/Mg, R2/R3 numerical comparisons) here. EKF-GITT uses pristine HEO only for reconstructive-conversion generality.

## Next restart
Continue from this note plus `START_HERE_CURRENT_STATE_2026-10-12.md`. Do not restart data partitioning or redraw Figs 1–5. v23 Word is the most recent review artifact, v22 GitHub markdown is the preceding baseline and fixed Abstract is separate. Resolve the genuine external input blockers and then complete references/SI final verification and production export.