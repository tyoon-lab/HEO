# LATEST HANDOFF — HEO v23 / EKF pilot, 2026-10-12

**Read first:** `manuscript/HEO_V23_STAGE_ORIGIN_REVIEW_AND_EKF_GATE_2026-10-12.md`. This adds a 12-page v23 PI scientific-review Word proof (Abstract unchanged, Figures 1–5 reused, Figure 6 layout cleaned) and 4-page focused SI v15 (main Table 1 moved to SI; three region-capacity/contrast/robustness tables). Word/SI binaries are in the conversation artifacts, not tracked in GitHub. v23 is not submission-ready: collaborator Section 2.1, synthesis/electrode metadata, raw BM boundary provenance and full references remain open. The v22 GitHub manuscript remains the preceding textual baseline; follow the new v23 review note for its changes.

**EKF decision:** a pristine HEO raw-GITT 65-pulse time-domain pilot, tested with 27 sensitivity settings, did not robustly improve the accepted four-region boundaries (original 6/25/56 versus spectrum-only ~21/39/56), nor directly identify specific conversion products. Exclude the new EKF analysis from HEO AFM Main/SI. Retain it for the separate LFP–Li2MnO3–pristine HEO GITT manuscript; all BM/Mg contrasts stay in HEO materials paper. Detailed pilot in EKF repo: `03_LFP/HEO_PRISTINE_GITT_TIME_DOMAIN_PILOT_2026-10-12.md`. No new physical-stage claims are authorized by the pilot.

---

# CROSS-PAPER BOUNDARY UPDATE — 2026-10-12

A separate GITT relaxation manuscript may use **pristine HEO only** as a reconstructive-conversion generalization case.

- Keep BM/Mg modification comparisons and the BM-R2 / Mg-R3 stage-origin story owned by this HEO materials manuscript.
- Do not migrate the HEO paper's central modification figures/results into the GITT manuscript.
- Existing HEO/BM apparent-D method-dependence audits remain background/reviewer-defense material.
- Cross-paper boundary authority: `GITT_CROSS_PAPER_DATA_USE_BOUNDARY_2026-10-12.md`.

# HEO — Current State, 2026-10-12

## Read this first

This is the single authoritative restart point for the HEO manuscript.

A new chat/session should be able to resume from this file without a separate handoff message.

The 2026-10-08 reaction-fingerprint state remains useful history, but the paper identity has sharpened further during PI Abstract review.

## Recovered original 2026-10-07 region partition — AUTHORITATIVE WORKING EVIDENCE

The exact **rounded original accepted four-sample GITT region-capacity table** was recovered from previous analysis discussion and archived in:
- `modeling/HEO_ORIGINAL_REGION_PARTITION_RECONSTRUCTION_2026-10-12.md`
- `modeling/HEO_ORIGINAL_REGION_PARTITION_RECONSTRUCTION_2026-10-12.csv`
- `modeling/HEO_ORIGINAL_REGION_CONTRASTS_2026-10-12.csv`

Original fractional shares **R1/R2/R3/R4**: HEO **9.2/29.2/47.7/13.8%**, BM-HEO **11.8/38.2/28.9/21.1%**, Mg-HEO **12.5/37.5/31.2/18.8%**, BM-Mg-HEO **16.1/46.4/8.9/28.6%**.

Using **16.6667 mAh g⁻¹ per 600s / 100 mA g⁻¹ GITT pulse**, original region counts reconstruct as HEO **6/19/31/9**, BM-HEO **9/29/22/16**, Mg-HEO **6/18/15/9**, BM-Mg-HEO **9/26/5/16**. Therefore **inferred** L1/L3/L4 *cumulative region-end pulses* are **HEO 6/25/56; BM-HEO 9/38/60; Mg-HEO 6/24/39; BM-Mg-HEO 9/35/40**. These IDs are *inferred from rounded accepted region charges*, not directly recovered boundary annotations; do not portray them as new extremum measurements.

Main stage-origin numbers based on the old GITT protocol table:
- HEO→BM-HEO: **R2 +166.7**, R3 −150, net +183.3 mAh g⁻¹.
- Mg-HEO→BM-Mg-HEO: **R2 +133.3** (largest POSITIVE region change), R3 −166.7, net +133.3.
- HEO→Mg-HEO: **R3 −266.7**, net −283.3.
- BM-HEO→BM-Mg-HEO: **R3 −283.3**, net −333.3.
- These signed regional differences are derived from the original GITT pulse partition; not from independently measured GCD totals.

**Interpretation:** This restores the original already-agreed BM→R2 and Mg→R3 quantitative evidence. The subsequent 3-sample *broken-stick* L4 calculation remains exploratory and NOT a replacement for accepted region boundaries. Three original raw first-lithiation pulse counts (HEO 65, Mg 48, BM-Mg 56) match reconstructed table totals. BM raw, exact raw-original boundary markers, and per-region t63 for all four remain pending.

**New local-only figure drafts:** `HEO_v22_Figure4_REFERENCE_FIXED_REGIONS_DRAFT.png` (HEO raw + old reconstructed boundaries), `HEO_v22_Figure5_BM_R2_PARTITION_DRAFT.png` and `HEO_v22_Figure6_Mg_R3_2x2_PARTITION_DRAFT.png`. These are numerical audit plots, NOT final publication artwork or GitHub-committed binary files.

## Latest raw-GITT boundary audit — 2026-10-12 (PRELIMINARY)

> **IMPORTANT CORRECTION:** Region criteria L1/L3/L4 and a ±1-step sensitivity check were agreed and audited in the 2026-10-08 fingerprint and 2026-10-12 Methods locks. The three-sample broken-stick L4 and minimum-t63 boundary proposals below are **separate exploratory candidate estimators**, NOT approved replacements of the established region partition or the historical R2/R3 fractions. Existing four-sample stage story remains the baseline; only a consistent final application/documentation of the already-agreed L4 plateau-end criterion was pending.



- Detailed provenance, extraction method, and result: `modeling/HEO_L4_THREE_SAMPLE_RAW_REAUDIT_2026-10-12.md`.
- Available original GITT files recovered: HEO ([GITT try 2_031].xlsx from Drive), Mg-HEO and BM-Mg-HEO (Sept. 17 Gmail). **BM-HEO raw remains missing**, so all four-sample regional partitions are not finalized.
- First-lithiation whole pulses extracted: HEO 65, Mg-HEO 48, BM-Mg-HEO 56. Three prior conversion-associated excess peak voltages reproduce the archived audit exactly (HEO pulse 50 at 0.527481 V; Mg pulse 38 at 0.386972 V; BM-Mg pulse 37 at 0.502865 V).
- Candidate L3 from central `t63` minima: HEO pulse 25; Mg pulse 24; BM-Mg pulse 34. Candidate common broken-stick voltage L4: pulses **53, 37, 39**, sensitivity ranges **50–53, 34–37, 38–40**, respectively.
- Under **this unfinalized new L4 definition**, corresponding R3 shares are **43.08%, 27.08%, 8.93%**. These do **not** match historical manuscript HEO/Mg R3 shares ~48%/~31%; **do not silently replace frozen Abstract/Results numbers**. Direction of HEO→Mg R3 decrease survives tested L4 variations.
- Figure 4 preliminary HEO three-trace diagnostic and three-sample L4 knee diagnostics were generated locally (not final figure artwork, not binary-committed to GitHub).
- Next: obtain **BM HEO 3 GITT 로우 데이터.xlsx**; apply common L1/L3/L4 rules across **four** datasets, check exact region-wise absolute/fractional GITT charge and sensitivity, redraw Figures 4–6. Preserve the v22 prose and PI-preferred Abstract pending completed audit.

## Latest PI-integrated manuscript and figure audit — 2026-10-12

**Current reviewed prose authority (v22):**

- `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md`
- Companion claim-to-evidence audit: `manuscript/HEO_V22_FIGURE3_6_EVIDENCE_AUDIT_2026-10-12.md`
- The independently maintained PI-preferred Abstract remains `manuscript/HEO_ABSTRACT_PI_PREFERRED_2026-10-12.md`; the v22 Abstract is a verbatim copy.
- Prior v21 and legacy Figure 3–6 notes are **historical**, not the current body prose/figure assignments. Section 2.1 and the experimental section are not complete.

**Critical submission status:** Figure 3 largely supports the material-capacity contrast (with raw source-provenance limitations). The *existing old* Figures 4, 5 and 6 **do not match the new Main story** and must be redrawn: new Fig 4 = L1/L3/L4 and R1–R4 electrochemical segmentation; new Fig 5 = BM R2 capacity gain with regional t63; new Fig 6 = Mg R3 capacity loss, cross-composition 2×2 comparison and horizontal reaction-sequence synthesis. Do not claim Figure 4–6 publication artwork is final.

**Immediate next work:** standardize L4 across four samples; freeze exact region-wise GITT numerical partition/absolute deltas and t63; regenerate main Figure 4–6 and captions; verify old excess-localization and cycling-history panels' SI relocation; integrate final collaborator Figures 1–2 and Methods; then revise SI/references and audit Abstract against final results.

## v22 integrated Word export — 2026-10-12 (LATEST)

A **12-page** Word review document was produced and successfully rendered with **all 6 original October stage-origin-aligned figures** preserved:
- `HEO_Manuscript_V22_PI_Integrated_Figures1-6_2026-10-12.docx` (downloadable conversation artifact, **not** a GitHub-tracked binary).
- GitHub release/QA note: `manuscript/HEO_V22_WORD_EXPORT_RELEASE_NOTE_2026-10-12.md`.
- Text authority: `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md` (Abstract, Introduction, Results 2.2–2.6, Conclusion PI-reviewed).
- Word source for existing figures + provisional Section 2.1/Experimental/20 reference entries: `HEO_MANUSCRIPT_V21_STAGE_ORIGIN_ALIGNED_2026-10-11.docx` from Google Drive.
- Original Oct Word Figure 4 and Figure 5 **already** match the current stage-origin narrative; no full redraw and no new boundary calculation. Figure 6 original schematic is retained but small labels overlap; fix *artwork only* if needed.
- **Working Table 1** with four-material original GITT R1–R4 fractions is embedded in the Word; still decide whether to keep in Main or place in SI. It is not a new calculation.
- Proof rendered and all **12 pages reviewed**; image captions stay with pictures and Conclusion is not split over pages.
- Work remains: Section 2.1 collaborator validation, missing Experimental details, Figure 6 label cleanup, final reference/citation check, SI sync. The Word is a PI-review draft, **not a submission-ready final**.

## October 11 embedded main-figure visual audit — 2026-10-12 (CURRENT)

**Current real Figure 1–6 visual basis is in `HEO_MANUSCRIPT_V21_STAGE_ORIGIN_ALIGNED_2026-10-11.docx` in the HEO preparation Google Drive folder.** All six embedded PNGs and captions have been directly inspected. Figure 4 already plots three GITT descriptors with L1/L3/L4 and R1–R4; Figure 5 already plots BM/HEO relaxation, R2/R3 region fractions and median t63; Figure 6 already shows the BM-R2/Mg-R3 horizontal reaction-sequence synthesis. The old September “redraw Figure 4–6” assumption is **obsolete** for current artwork.

Reuse existing Figure 4 and 5 with minor labeling/caption/QC changes; keep Figure 6 schematic and improve small overlapping text plus supply the two-Mg-contrast/four-sample signed GITT comparison. Figure 3 already exists with first-cycle profiles and bars; Figures 1–2 existing working microscopy/BET art pending collaborator verification. **Do not restart segmentation, numerical analysis, or redraw all figures.** Full audit: `manuscript/HEO_EXISTING_FIGURE1_6_ASSET_REUSE_AUDIT_2026-10-12.md`.

Body prose authority remains `manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md`; figure-art basis remains the stage-origin v21 Word. Only the minimal figure-to-text reconciliation, collaborator characterization completion, and Methods/SI/caption sync are open.

## Current paper identity

Working target: **Advanced Functional Materials (AFM)**.

Working title remains provisional:

**GITT Relaxation Fingerprints Resolve Material-Specific Perturbations of Conversion Lithiation in Spinel High-Entropy Oxide Anodes**

Current manuscript-facing identity:

> **Use GITT relaxation to resolve the multistep HEO conversion reaction electrochemically, then identify which reaction stage is primarily responsible for the familiar macroscopic capacity change produced by ball milling or Mg incorporation.**

The paper is a **materials/conversion paper**, not a generic GITT-method paper.

## Current central result

The materials-level starting observation is simple:

- ball milling increases first-lithiation capacity;
- Mg incorporation decreases first-lithiation capacity.

The stage-resolved GITT result explains where those opposite capacity changes arise:

> **Ball-milling capacity gain originates predominantly from expansion of the conversion-onset/progression regime associated with oxide destabilization and structural reconstruction, whereas Mg-induced capacity loss is concentrated in the subsequent late-conversion regime associated with evolution toward reduced metal/Li2O-derived states.**

Headline mapping:

- **BM -> R2 dominant expansion -> capacity gain**
- **Mg -> R3 dominant suppression -> capacity loss**

Secondary observations remain scientifically useful but are not the Abstract headline:

- BM also changes R1/R4 and reduces the relative R3 contribution;
- BM makes post-onset relaxation more persistent;
- Mg changes the remaining R3 relaxation timescale only weakly;
- accessibility and relaxation persistence are not the same quantity.

## Abstract status — PI-preferred working baseline, 2026-10-12

**Current abstract for all Introduction and body review**:

`manuscript/HEO_ABSTRACT_PI_PREFERRED_2026-10-12.md`

This is the PI-preferred, improved-flow version agreed in conversation after the earlier provisional lock. Preserve the approved text during line-by-line body review; refine only when evidence, logic, or a final PI decision warrants it. **It supersedes the older abstract text in the v21 snapshot for current narrative alignment**, but does not erase the historical version.

The new abstract begins with multistep conversion, poses the question of which reaction regions control macroscopic capacity changes, states the four GITT electrochemical regimes, contrasts the BM-R2 and Mg-R3 stage origins, and ends with the materials-facing significance of stage specificity.

**Do not infer unique microscopic phases at R1-R4 boundaries or claim demonstrated cycling-stability optimization.** Physical assignments are broad associations supported by literature plus state-resolved electrochemistry.

## Why the Abstract changed the paper

During line-by-line PI review, several earlier phrasings were rejected because they made the work sound method-driven or abstract:

- `GITT is used to resolve ... rather than only to extract Dapp` was rejected as an artificial method announcement.
- `state-dependent reaction fingerprint` was too compressed to be immediately interpretable.
- exhaustive BM statements (`R1/R2/R4 up, R3 down`) diluted the headline.
- the relaxation-persistence result, although valid, distracted from the stronger materials message in the Abstract.
- later sentences initially switched from concrete conversion chemistry to abstract regime names, breaking the reader's physical mental picture.

The adopted Abstract therefore anchors on a familiar macroscopic materials effect and uses GITT to reveal its **reaction-stage origin**.

## Reaction sequence and region map

The four electrochemically defined regimes remain:

- **R1:** early lithiation
- **R2:** conversion onset and progression; broadly associated with oxide destabilization and structural reconstruction
- **R3:** late conversion; broadly associated with continued evolution toward reduced metal/Li2O-derived states
- **R4:** post-plateau deep lithiation

Important evidence rule:

> Regions are defined electrochemically first from GITT relaxation / relaxed-voltage landmarks. Their physical labels are broad literature-supported assignments, not direct spectroscopic identification by GITT and not four discrete elementary microscopic steps.

Current landmarks:

- L1: early transition
- L3: central conversion-associated landmark
- L4: end of broad relaxed-voltage plateau / transition to steeper post-plateau branch

L2/L5 remain internal features, not boundaries.

## Quantitative headline

First-cycle lithiation/delithiation capacities:

- HEO: 901.25 / 609.12 mAh g-1
- BM-HEO: 1056.10 / 782.08 mAh g-1
- Mg-HEO: 731.15 / 458.91 mAh g-1
- BM-Mg-HEO: 944.07 / 580.83 mAh g-1

Regional fraction headline:

- HEO R2 ~29% -> BM-HEO R2 ~38%: **largest BM-driven expansion**
- HEO R3 ~48% -> BM-HEO R3 ~29%: reduced relative late-conversion contribution
- HEO R3 ~48% -> Mg-HEO R3 ~31%: **dominant Mg-driven suppression**

Use regional percentages as the preferred Main-text partition metric.

## Current section architecture

### 1. Introduction

Literature-established multistep HEO conversion
-> materials-development question: capacity changes are known, but which reaction stage causes them?
-> GITT relaxation provides state-resolved electrochemical information
-> BM and Mg provide opposite macroscopic perturbations
-> present study localizes the stage origin of the capacity gain/loss.

### 2. Results and Discussion

**2.1. Structural and morphological perturbations introduced by ball milling and Mg incorporation**

**2.2. Opposite capacity changes motivate a stage-resolved analysis of conversion**

**2.3. GITT relaxation fingerprints resolve four lithiation regimes**

**2.4. Ball milling capacity gain originates predominantly from conversion onset and reconstruction**

**2.5. Mg-induced capacity loss originates predominantly from late conversion**

**2.6. Stage-resolved GITT links macroscopic capacity changes to their reaction origin**

### 3. Conclusion

Restate the four broad regimes, then the BM-R2 and Mg-R3 origins, then the materials-level implication.

## Current Figure logic

- **Figures 1–2:** material structure/composition/morphology; final collaborator package still pending.
- **Figure 3:** opposite macroscopic capacity changes.
- **Figure 4:** four GITT-defined electrochemical regimes and broad physical assignment.
- **Figure 5:** BM capacity gain is dominated by R2 expansion; relaxation persistence is secondary mechanistic information.
- **Figure 6:** single horizontal R1 -> R2 -> R3 -> R4 reaction sequence showing BM acting mainly on R2 and Mg mainly on R3.

Important Figure decision:

> The final conceptual Figure 6 must be a **single horizontal reaction-sequence schematic**, not a 2 x 2 conceptual matrix. The experimental design may be 2 x 2, but the conceptual figure should visualize the reaction coordinate and the dominant action point of each modification.

## Main manuscript authority

Current rendered Word working manuscript:

**HEO_MANUSCRIPT_V21_STAGE_ORIGIN_ALIGNED_2026-10-11.docx**

GitHub text snapshot:

`manuscript/HEO_V21_STAGE_ORIGIN_TEXT_SNAPSHOT_2026-10-12.md`

Current story/decision authority:

`manuscript/HEO_STAGE_ORIGIN_STORY_LOCK_2026-10-12.md`

Abstract dependency map:

`manuscript/HEO_ABSTRACT_CONTROL_MAP_2026-10-12.md`

Analysis/method guardrails:

`manuscript/HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md`

The 2026-10-08 v18 files remain historical and are superseded for manuscript story and wording.

## Retired / demoted stories

Do not restart from these without an explicit audit reason:

- capacity–kinetics mismatch as the paper identity;
- capacity as a direct kinetic-speed coordinate;
- polarization–t63 non-equivalence as the endpoint;
- conventional GITT Dapp conflict as Main novelty;
- four-step microkinetic model as Main Figure 6;
- exact microscopic mapping of old model steps onto experimental R1–R4;
- 2 x 2 conceptual synthesis figure;
- BM as a simple kinetic acceleration;
- Mg as a simple kinetic slowing;
- `beta broadening` as the BM interpretation.

These may remain historical, SI, or reviewer-defense material where scientifically useful.

## Internal robustness

Boundary sensitivity (L1/L3/L4 independently shifted +/-1 GITT step) supports the qualitative conclusions:

- BM capacity pattern R1+, R2+, R3-, R4+: 100% in tested comparisons.
- BM t63 pattern R1-, R2+, R3+, R4+: 100%.
- Mg-induced R3 capacity loss: 100%.
- R3 is the most negative Mg capacity change: 100%.
- Mg-induced R3 t63 change remains small (|Delta t63| <= 1.5 min): 100%.

Keep this internal unless reviewer defense or SI robustness becomes necessary.

## Analysis guardrails

- t63 is an operational relaxation timescale, not a microscopic elementary rate constant.
- Delta Erest is a relaxation amplitude, not a pure kinetic overpotential.
- relaxed 60 min voltage is used as a state coordinate.
- physical reaction labels are assigned after electrochemical segmentation.
- exact element-specific reduction steps are not assigned to R1–R4 without direct evidence.
- protocol-derived regional capacity is not identical to the separate GCD absolute capacity scale.
- Main text should emphasize regional fractions; exact absolute regional mAh g-1 requires direct raw-current integration if later needed.

## Remaining blockers

1. Final collaborator Figures 1–2 package: quantitative XRD/refinement, composition, TEM/SEM/BET, XPS decision.
2. Final Mg synthesis recipe and collaborator-verified composition.
3. Missing cell/electrode metadata for submission-ready Experimental.
4. Exact reference verification for close prior art and any working citations not yet publisher-checked.
5. Standardized final L4 algorithm across all four samples before numerical freeze.
6. Main/SI synchronization after PI line-by-line body review.
7. Final title/TOC/keywords only after body review and reverse Abstract audit.

## Next task in a new chat

**Begin from v22 Word export, not an unassembled v21 manuscript.** The 12-page file `HEO_Manuscript_V22_PI_Integrated_Figures1-6_2026-10-12.docx` contains all existing main figures and the current PI-approved text, plus provisional v21 2.1/Experimental/20 refs and review-only four-material GITT table. Read `manuscript/HEO_V22_WORD_EXPORT_RELEASE_NOTE_2026-10-12.md` for current limitations. Resolve collaborator Section 2.1/Experimental metadata, Figure 6 small-label overlap, table Main-vs-SI placement, reference numbering, and SI alignment. **Do not** redo established L1/L3/L4 segmentation or Figures 4–5.

