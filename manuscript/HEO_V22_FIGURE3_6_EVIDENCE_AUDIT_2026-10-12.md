# HEO v22 — Figure 3–6 evidence-to-claim audit (2026-10-12)

**Scope:** Check new manuscript claims against the existing GitHub-recorded experimental analyses and against the **actual prior figure designs**. This is a documentary audit, NOT a new raw-data analysis, final graphical rendering, or verification of as-yet-unmade v22 artwork.

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

> **VISUAL AUDIT CORRECTION (2026-10-12):** This earlier claim audit compared v22 text mainly with the September 2026 Figure 4–6 *historical layouts*. Subsequently the actual **October 11 v21 stage-origin-aligned Word document** was retrieved and all six embedded PNGs were visually inspected. That Word already has **Figure 4 = t63/ΔErest/rest-end-voltage L1/L3/L4 R1–R4 plot, Figure 5 = HEO/BM stage fractions and median t63, Figure 6 = horizontal BM-R2/Mg-R3 stage synthesis**. Thus the blanket assessment “Figures 4–6 need to be redrawn” is **superseded** for current artwork. Keep/revise Fig 4–5 minimally; retain Fig 6 concept with readability polish and explicit four-sample evidence table. Full evidence and visual descriptions: `manuscript/HEO_EXISTING_FIGURE1_6_ASSET_REUSE_AUDIT_2026-10-12.md`. The older September figures remain prior art/provenance, not the images present in the latest Word. No additional region-finding calculations are authorized by this correction.

## Decision

1. **Figure 3 — Mostly narrative-compatible:** establishes the first-cycle macroscopic capacity contrast. Publication-grade numerical data provenance remains incomplete.
2. **Figure 4 — Redraw required:** the older Figure 4 addresses apparent diffusivity, t63 and capacity mismatch; it does not plot the three GITT observables with L1, L3, L4 and R1–R4 as the v22 text requires.
3. **Figure 5 — Redraw required:** the older Figure 5 localizes a conversion-associated excess relaxation peak against dQ/dV; it does not show the BM-induced dominant R2 increase demanded by Results 2.4.
4. **Figure 6 — Redraw required:** the older Figure 6 shows C1–C3 relaxation history. It does not show Mg R3 suppression or the full 2×2 stage comparison demanded by Results 2.5–2.6.

**Therefore, Figures 4–6 cannot be called already aligned or already proving the new v22 Abstract.** Data-backed claims exist in prior analytical records, but the new main panels, captions and cross-references remain a material submission gate.

## Claim-by-claim audit

| Manuscript claim | Existing evidence record | Verdict / task |
|---|---|---|
| 2.2: BM raises lithiation capacity, Mg lowers it | Figure 3 capacities: HEO 901.25, BM 1056.10, Mg 731.15, BM-Mg 944.07 mAh g⁻¹ (first lithiation) | **Supported by recorded numeric summary.** Source artwork based on September Origin vector exports; original source numerical profiles/cycling/rate still desired. |
| 2.2: capacity differences span substantial portions of lithiation | September 2026 vector first-cycle voltage profiles (Figure 3a) | **Qualitatively supported by working art**; exact original continuous data not yet recovered. |
| 2.3: GITT 100 mA g⁻¹; 600 s pulse; 3600 s rest; common 3 s reference; t63 and ΔErest | HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md | **Supported operational definitions.** ΔErest = absolute E60min−E3s; t63 = first time reaching 63.2% of this finite-window relaxation. |
| 2.3: L1/L3/L4 divide R1–R4 | HEO_STAGE_ORIGIN_STORY_LOCK_2026-10-12.md; HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md | **Archived analysis, absent from old main art.** Figure 4 needs 3 observable profiles, shared capacity-state coordinates and annotated boundaries; common L4 rule still must be finalized. |
| 2.3: t63 and ΔErest minima near L3; nearby dQ/dErest peak; broad plateau through R3 | v21 observed-landmark description, current analysis lock | **Archived descriptor observation needing plotted evidence and QA.** Differential capacity maximum and the plateau originate from the same 60-min voltage curve; do not count them as independent measurements. Near very small relaxation amplitude, t63 can be unstable. |
| 2.3: R2 = oxide destabilization/reconstruction; R3 = later conversion toward metal/Li₂O | Operando/ex situ spinel HEO conversion literature + previous conversion-localization result | **Broad literature-supported interpretation, not direct identification**. Microscopic processes overlap; no unique cation, phase or bond step identified by GITT. |
| 2.4: HEO/BM R2 share ~29%→~38%, HEO/BM R3 share ~48%→~29% | HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md; HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md | **Recorded stage-partition result; Figure 5 plot missing**. Fractions are GITT-protocol fractions, not fractions of GCD total capacity. R2 as largest *absolute positive region change* is recorded but must be plotted/re-integrated from the numerical partition before publication. |
| 2.4: BM t63 decreases R1, increases R2–R4 | HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md, boundary sensitivity | **Recorded direction; Figure 5 plot missing**. t63 is current-off recovery time, not a microscopic forward conversion rate. |
| 2.4: particle refinement/disorder/interfacial accessibility causes R2 gain | Working materials hypothesis; final collaborator Figures 1–2 still provisional | **Conditional, not proved.** Keep modal verbs; verify structural characterization before claiming causation. |
| 2.5: HEO→Mg R3 share ~48%→~31% and largest Mg-related regional loss | HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md; prior ±1-step sensitivity | **Recorded, new Figure 6 required.** Confirm regional absolute delta from GITT-normalized data; do not calculate it by multiplying GCD capacity by GITT fraction. |
| 2.5: Mg shifts relaxed voltage, reduces ΔErest, modestly alters remaining R3 t63 | GITT audits and HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md | **Recorded directions; Figure 6 plot missing**. A smaller voltage relaxation magnitude is not direct evidence for faster rate or less metal/Li₂O product. |
| 2.5: reduced active-redox inventory vs Mg-specific suppression | Historical ICP table in modeling/HEO_MG_CROSS_COMPOSITION_GITT_CHECK_2026-09-27.md shows near-equimolar Mg with principal cations | **Mechanistic ambiguity remains**. Uniform inert dilution alone leaves normalized regional fractions unchanged, but composition-specific redox inventories could affect some regions disproportionately; verify nominal/ICP and theoretical redox capacities before excluding alternatives. |
| 2.6: R2 dominant milling effect survives Mg; R3 dominant Mg effect survives milling | Four-composition region audit and ±1 pulse boundary sensitivity recorded in Oct story lock (729 boundary combinations per pair) | **Recorded robustness; four-way comparative Figure 6 required**. Does not establish BM/Mg perfect independence or unique physicochemical step. |
| Conclusion: macroscopic capacity changes have stage-localized origins | 2.2–2.6 combined | **Scientifically plausible and recorded; publication proof depends on completing new figure suite, boundary and raw integration verification.** |

## Proposed v22 panel alignment

### Figure 3 — materials performance contrast

Keep the Sept 2026 first-cycle voltage profiles, first lithiation/delithiation summary, 0.1 C cycling, absolute rate capability. Do not label more capacity as faster intrinsic conversion kinetics. Recheck original numerical acquisition/source (including known older power-interruption artifact).

### Figure 4 — derive electrochemical segmentation

Recommended:
- a: representative measured pulse and rest, clearly define 3 s/60 min ΔErest and t63;
- b: pristine-HEO t63 and ΔErest against a shared first-lithiation state coordinate, mark L1 and L3;
- c: 60-min rest-end voltage profile (plus dQ/dErest if useful), mark L3 and standardized L4 plateau ending;
- d: aligned R1–R4 overlay / four-region map with sensitivity check in SI.

Allow aligned axes instead of four redundant panels. Do not identify four individual metal-reduction reactions.

### Figure 5 — BM → R2 expansion

Recommended:
- a: HEO versus BM voltage/relaxation features on equivalent states;
- b: four-region GITT fractional-capacity comparison emphasizing 29→38% R2;
- c: region-wise protocol-derived capacity differences to establish R2 as the greatest positive contribution (pending numerical verification);
- d: regional median t63 with R1-versus-R2–R4 contrast and restrained physical annotation.

The old excess-relaxation/dQdV localization is relevant to broad conversion assignment but is **not** the R2-dominance proof; move selectively to SI.

### Figure 6 — Mg → R3 contraction and 2×2 confirmation

Recommended:
- a: HEO–Mg-HEO four-region fractions / R3 48→31%;
- b: BM-HEO–BM-Mg-HEO contrast for repeatability;
- c: distinguish R3 contribution from its small median t63 change and ΔErest/voltage shift;
- d: a **single horizontal R1 → R2 → R3 → R4** sequence: BM centered at R2, Mg centered at R3. No claim of exclusive or orthogonal action.

The old cycle-history Figure 6 should be moved to SI or retained as separate supporting analysis, not relabeled as this new figure.

## Remaining verification gates

1. Standardize an **L4 rule using the same relaxed-voltage criterion for all four samples**, report indices/state values and sensitivity.
2. Compile the exact numerical four-material, four-region table: pulse counts, normalized fractions, protocol-derived regional capacities, region-to-region deltas, and t63 summary. Validate the strongest-positive-BM-R2 and strongest-negative-Mg-R3 attribution, not only percentage-point changes.
3. Verify raw-current integration / active-mass basis if exact regional mAh g⁻¹ values are retained. The published independent GCD 901.25 etc must not be substituted for the total GITT capacity.
4. Check any low-amplitude L3 percentile-time ill-conditioning. Show t63 minima and ΔErest minima without implying unique elementary-rate changes.
5. Finalize collaborator Figures 1–2, Mg nominal and ICP stoichiometry, processing/morphology metrics, and electrode Methods.
6. Recover original numerical conventional-electrochemistry files when feasible; Figure 3 current curves are traceable to the collaborator Origin vector presentations, not yet independently archived source tables.
7. Only then redraw Figure 4–6, finalize captions, reassign older Figure 4–6 content to SI selectively, and synchronize references and SI.

## Sources (all existing repository records)

- manuscript/HEO_MANUSCRIPT_V22_PI_INTEGRATED_2026-10-12.md
- manuscript/HEO_V21_STAGE_ORIGIN_TEXT_SNAPSHOT_2026-10-12.md
- manuscript/HEO_ABSTRACT_PI_PREFERRED_2026-10-12.md
- manuscript/HEO_STAGE_ORIGIN_STORY_LOCK_2026-10-12.md
- manuscript/HEO_METHODS_ANALYSIS_LOCK_2026-10-12.md
- manuscript/HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md
- manuscript/HEO_FIGURE3_ARTWORK_FINAL_NOTE_2026-09-27.md
- manuscript/HEO_FIGURE4_ARTWORK_FINAL_NOTE_2026-09-27.md
- manuscript/HEO_FIGURE5_ARTWORK_FINAL_NOTE_2026-09-27.md
- manuscript/HEO_FIGURE6_ARTWORK_FINAL_NOTE_2026-09-27.md
- manuscript/HEO_FIGURE3_SOURCE_PROVENANCE_AUDIT_2026-09-27.md
- manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_AUDIT_2026-09-27.md
- modeling/HEO_MG_CROSS_COMPOSITION_GITT_CHECK_2026-09-27.md

**Audit boundary:** documentary check of pre-existing records and legacy artwork, not a claim of new numerical reanalysis or inspection of finalized v22 images.
