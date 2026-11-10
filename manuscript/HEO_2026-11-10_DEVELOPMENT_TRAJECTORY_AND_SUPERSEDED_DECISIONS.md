# HEO manuscript research trajectory and decision history — reconstructed 2026-11-10

**Status:** This is a chronological record of *how and why the scientific narrative and artifacts changed*. Historical choices are not simultaneous current instructions. For the active scientific numbers, files and still-pending decisions, read [Nov-10 authoritative state](HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md). A series of older “LOCK” files is historical: a later explicit PI decision supersedes only the relevant scope, rather than silently rewriting the past.

## A. Original motivation and rejected/evolved framing

### September 18–28: conversion kinetics, apparent D, phase-field/microkinetic exploration
The HEO project initially explored GITT relaxation, diffusion-coefficient assumptions, conversion microkinetics, spatial phase-front modeling, and material-specific voltage/capacity differences. The 2026-09-18 source base included GITT, 4-sample materials characterization, and several scripts/models. Physical simulations served as candidate explanations and consistency tests, not experimental proof of a four-step unique chemical pathway.

**Exploratory paper identities** included:
- capacity-versus-kinetics mismatch;
- apparent GITT diffusion coefficient or Warburg-type limitations as the novelty;
- polarization/t63 endpoints;
- a four-step kinetic reaction/phase-field Main model;
- broad “kinetic fingerprints” without explicit allocation of capacity.

These remain useful for future EKF/GITT or methods projects but are **not the current paper identity**. Sources: [model development audit](../modeling/HEO_MODELING_DEVELOPMENT_LOG_2026-09-18.md), [four-step modeling caveats](../modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md), [main architecture toolkit](HEO_MANUSCRIPT_ARCHITECTURE_TOOLKIT_LOCK_2026-09-28.md). In the paper, do not narrate rejected modeling hypotheses just to defend current charge segmentation.

### September 26–October 8: t63 and reaction-fingerprint pivot
The PI sought a physical question that GITT could answer without pretending to resolve intrinsic D or unique reaction-rate constants. Current-off rest voltage magnitude and t63 were adopted as **operational** observables: t63 is the first 63.2% crossing over 3s-to-rest end, ΔErest is the recovered-voltage amplitude, and QOCV is the 60-min rest-end coordinate. These observables are coupled but *not equivalent*: large accessible charge and long time to equilibrate can coexist, and the same t63 does not imply the same chemical state.

October 3 polarization/t63 work found that a simple kinetics-versus-capacity contradiction was not robust enough to dominate the paper. The October 8 [reaction-fingerprint story lock](HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md) replaced capacity–kinetics mismatch with a **material intervention → pulse-resolved relaxation fingerprints → distinct electrochemical regions → material-specific effects** story. At this stage a 2×2 materials comparison was central, and a schematic conceptual figure was considered. “AFM” was a working target then; this is no longer a current journal choice.

### October 11–15: PI moves to **origin of charge change among reaction-associated regions**
The PI preferred a clearer materials-research question: the net capacity response to milling and Mg is already observed; **where does the gained/lost charge occur during overlapping conversion lithiation?** [October 12 stage-origin lock](HEO_STAGE_ORIGIN_STORY_LOCK_2026-10-12.md) explicitly superseded the fingerprint-only headline. **Main hierarchy:** region-resolved charge accounts quantitatively for capacity contributions, kinetic trajectories and model physics support/interpret it.

BM and Mg were chosen as *contrasting types of intervention* (particle morphology/process vs cation composition), **not** because opposite total-capacity signs were known before the experiments. Matched four-material comparisons supply the answer. Literature-guided R2 oxide destabilization/early conversion and R3 later conversion were retained as physically useful labels, but without claiming chemically isolated stages.

The Oct15 [dominant reaction mechanism audit](HEO_V25_DOMINANT_REACTION_STAGE_MECHANISM_REVIEW_2026-10-15.md) developed specific *testable* hypotheses: milling might improve access to early oxide-reorganization reactions; Mg might influence redox-active cation inventory or stability of partially converted environments. Those were explicitly **candidate mechanisms**, requiring actual Mg content, XAS/XRD and electrochemical matched-state tests. The paper must not automatically describe BM as faster intrinsic diffusion or Mg as slower intrinsic reaction rate.

### November 3: deliberate terminology and complete Introduction
The PI reviewed the Intro **line by line**, fixed four paragraphs, and made the operational region/physical process distinction explicit:
- “Overlapping reaction processes” for chemistry and reconstruction;
- “electrochemical regions” for intervals defined by measured GITT features;
- “dominant reaction processes” for interpretation associated with intervals using published structure/redox pathways.
The predecessor [consolidated Introduction](HEO_INTRO_CONSOLIDATED_REACTION_PROCESSES_ELECTROCHEMICAL_REGIONS_2026-11-03.md) is historical PI-approved wording at that point.

Key fine decisions: lower-rate GCD voltage shows quasi-thermodynamic broad profiles with plateau overlap; GITT is valuable for kinetic contrast; ΔErest is voltage *amplitude*, t63 a *time*, QOCV finite-rest *quasi* equilibrium; GITT alone is not a unique D. A NiO GITT electrochemical-region prior art exists; remove over-specific NiO review from focus Intro but do not claim method absolutely unprecedented. A statement of conflicting net BM/Mg outcomes belongs in Results, not the original motivation to choose those interventions.

### November 4: v30/v31 review and v12 Abstract restoration
The PI had locked a stronger direct Abstract, v12. An assistant accidentally replaced an author-approved Abstract with a newer unapproved draft; the author-approved wording was restored and explicitly archived. **Lesson:** source/author-approved Word and explicit PI edits supersede model-created working drafts; frozen text should not be overwritten by generic polishing.

v31 assembled and reviewed six figures, addressed BET/SEM, Figure3 cycling placeholder, early XPS evidence, and retained 15 actual Word comments. The notorious **CoGa2O4** HRTEM phase label was already recognized as inconsistent with Ga-free recipe. Preliminary Cr 2p near 579 eV assignment was flagged as batch-dependent and unvalidated; do not claim Cr(VI) or specific oxidation-state proof from that evidence. Figure3 100-cycle and rate plots were extracted from presentation/vector sources, **not raw cell-tester exports**.

### November 5: original four-workbook GITT and numerical reassignment
Earlier illustrative plot drawings were replaced by **original four raw GITT Excel workbooks** (HEO, BM, Mg, BM-Mg), 65/76/48/56 complete pulses. Uniform 100mA/g×600s+3600s protocol, E3s reference and signed t63 first crossing used. Revised boundaries selected from measured descriptor trajectories. This revealed that t63 initial shapes change with milling and that Mg modifies late t63; initial equal-pulse comparisons have different QOCV, so intrinsic fast insertion cannot be inferred.

The PI approved **region-charge as the dominant Results conclusion**. New Figure4 contains all 4 samples with t63/ΔErest/QOCV; Figure5 reports absolute and signed nominal regional charge. The first post-raw partition for late Mg used QOCV knees (Mg L4 39; BM-Mg L4 40); it was **later explicitly superseded**. The 729 ±1 pulse sensitivity framework was introduced. See [raw source audit](../modeling/HEO_FOUR_SAMPLE_RAW_GITT_KINETIC_BOUNDARY_CHECK_2026-11-05.md), [Nov5 v33 region-charge integration](HEO_V33_KINETIC_REGION_CHARGE_PRIORITY_INTEGRATION_2026-11-05.md).

Figure2 vector XPS and Figure3 GCD/rate data were improved from genuine archived PowerPoints (v34); no fabricated instrument raw counts. Restriction: don't claim figure-exported vector traces are raw potentiostat data, don't claim XPS calibration verified.

### November 6: PI t63-only L4 decision **supersedes Mg QOCV knees**
The PI annotated a late change in Mg-containing t63 curves and explicitly required that **all three boundaries are selected from t63 alone**. Adopted after-pulse L1/L3/L4:
- HEO 6/25/55;
- BM-HEO 9/38/60;
- Mg-HEO 7/24/42;
- BM-Mg 9/35/46.
ΔErest and QOCV stay as supporting observations; a change in another observable does not define the numerical cut.

Exact Mg slope feature amplitude only −1.26s / −1.76s between adjacent pulses, comparable to/below 3s acquisition. It is an **operational selection, not an independently validated sharp phase boundary**. The PI later asked the figure to **remove the visible “late t63 shoulder” annotation and the corresponding prose label**, not to discard the actual accepted boundaries or reproducibility definition. Results/SI should say “late change in t63 slope” as needed. [v35 decision and recalculated charge table](HEO_V35_T63_ONLY_L4_SHOULDER_REASSIGNMENT_2026-11-06.md), latest SI v22.

R2 positive milling range +150–167, R3 negative milling −117–133, R4 positive milling +67–100; Mg strongest R3 negative −183–200. The “R3 charge physically migrates to R4” narrative was rejected: BM Δ(R3+R4) decreases in both pairs. **R1 changes** are real but secondary, state-mismatch-sensitive.

### November 6: R3 relaxation-amplitude hump as a secondary discovery
The PI noticed pristine R3 ΔErest amplitude **hump**, despite t63 growth in all four. Raw time-window decomposition:
- pristine onset pulse26→peak50 = +44.2mV;
- early (3–60s) −9.8mV;
- middle (1–10min) +16.5mV;
- late (10–60min) +37.5mV (dominant positive contribution);
- Mg weak +8.6mV; BM pair do not show an interior R3 amplitude hump.

A matched-QOCV 0.50V comparison ruled out the **simplest voltage-slope-only explanation** for HEO vs BM but does not uniquely determine internal Li redistribution, phase fractions or nucleation. The literature survey distinguished *a hump in ΔErest across sequential pulse positions* from nonmonotonic transients within one rest curve, cycle-to-cycle capacity bumps and irreversible hysteresis. FeF3, Fe3O4, SiO-graphite, graphite and LFP suggest slow phase/Li-redistribution precedents. The PI accepted incorporating this survey in main §2.5 and SI S7/Table S6 **while keeping charge allocation the main story**; no proof of HEO-specific core-shell mechanism. [v39 raw window](HEO_V39_R3_HUMP_RAW_TIME_WINDOW_ANALYSIS_2026-11-06.md), [v40 literature integration](HEO_V40_R3_HUMP_CROSS_MATERIAL_LITERATURE_INTEGRATION_2026-11-06.md).

### November 6: visual publication-quality decisions v38→v43
User requests and corrections were cumulative:
1. **Figure3(a–d):** common capacity −35..1100mAh/g, voltage −0.1..2.8V. Some source >2.8V initial points intentionally clipped; avoid claims to show all. a–d include sample names *inside panels*; e no title; f must have full legend.
2. **All figures:** panel letters outside the axes, weight normal, avoid extraneous titles; underlying microscope/XPS source labels may require editable originals to change old bold text safely.
3. **Figure4:** four materials/2×2 grid of t63, ΔErest, QOCV; remove overall “Region boundaries follow...” title, dashed-line explanation beneath plot, pulse-count parentheticals and literal “late t63 shoulder” annotations; keep L1/L3/L4 and stable sample identification.
4. **Figure5:** omit global title, panel a only letter, b/c titles inside plot; keep measured positive/negative changes and separate from physical schematic.
5. **Word layout:** put Figs1+2 immediately after §2.1 heading, Fig3 §2.2, Fig4 §2.3, Fig5 §2.4, Fig6 §2.6; captions follow figures.
6. **Figure6:** earlier **rectangular process boxes** disliked and rejected. Next revision used actual HEO QOCV plus many signed regional numbers; PI called it too similar to Figure5. Finally **qualitative leader arrows** on actual pristine QOCV preferred: BM R2 gain (largest), BM/Mg R3 losses, BM R4 gain; region-specific candidate physical processes. Figure6 is interpretive, not a second Figure5. No R3→R4 charge transfer arrow, no isolated chemical proof. The user said they would inspect v43, so stylistic acceptance is **not final submission signoff**.

[Fig3/2 v38](HEO_V38_MULTIELEMENT_XPS_HUMP_FIG3_COMMON_VOLTAGE_2026-11-06.md), [v41 caption/reference audit](HEO_V41_ARTWORK_CAPTION_REFERENCE_AUDIT_2026-11-06.md), [v42 section placement/typography](HEO_V42_FIGURE_PLACEMENT_REGULAR_TYPOGRAPHY_2026-11-06.md), [v43 qualitative Figure6 design](HEO_V43_FIGURE6_QUALITATIVE_QOCV_REDESIGN_2026-11-06.md).

### November 7: author collaborator Word vs assistant clean rewrite
PI supplied two actual Word artifacts: earlier commented v43 and newer **author-revised collaborator manuscript**, then requested generic journal format, authors Park/Kang/Yu/Yoon with Yu/Yoon joint correspondence, source-verified yellow notes, Publication Toolkit latest rules and final collaborator Word.

Toolkit **v0.22** (2026-11-07) prohibits *uniform defensive AI-academic prose*. Each sentence should be evidence-calibrated P/plain, S/strong supported, C/calibrated when interpretation really changes; no stock “Together” and unnecessary abstraction/negation/development-history debris. Assistant created a **clean collaborator draft** 11p/6 figures/24 references and inserted 11 yellow source-verification notes. However it **rewrote** author Abstract/Introduction too much: replacing detailed physical question with generic overall-capacity phrasing, restoring unrequested BET/Mg mechanism in Abstract and diluting PI style. The author requested an explicit old/new comparison and rejected those unnecessary changes. This case is an author-authority lesson, not evidence of a change in experimental data.

### November 7: new PI Abstract logic and several editorial rounds
The PI clarified that previous Abstract lacked explanatory cause; desired structure:
**modification of morphology/cation chemistry → unknown effect on lithium storage mechanism → because overlapping conversion processes prevent clean attribution of signed regional charge → total capacity and spectroscopy provide different incomplete views → GITT t63 electrochemical-region decomposition → crossed BM/Mg region charge → literature-supported physical assignment → design.**

Specific directives:
- Keep first two English background/intervention sentences as authored.
- Avoid “Yet” as automatic connector; if using “because”, make causal link **explicit**.
- Don't jump directly to “Here GITT compares BM/Mg”; explain GITT *method* as response to the analytical gap and only then name applied modifications.
- Don't claim structural/XAS spectroscopy is exclusively qualitative. Don't claim no older electrochemical stage division exists.
- **No charge values in the proposed final Abstract**, only which region shows largest gain/loss (R2 BM+, R3 Mg−) and perhaps secondary BM R4+/R3− in context.
- R2 and R3 should be physically interpretable. “Deep lithiation” and “continued conversion” alone are descriptive/ambiguous. Candidates R2 oxide reconstruction plus early reduction; R3 reduction of reconstructed intermediates plus metal/Li2O products; R4 remaining reduction and possible interface storage. These are hypotheses, not direct chemical state measurement.
- Avoid “selectively suppresses continued conversion” when Mg also affects R2/R4 and no phase-resolved probe proves mechanism.

Outside reviewer A/B Abstracts were evaluated; B's *cause→solution→qualitative result* structure better, but language “impossible”, “regions governed by dominant reactions” and overconfident reaction effects not accepted literally. The most recent assistant produced a minimal-edit *candidate*, **not yet user-approved**. Its full text and user-authored predecessor are archived in [Abstract/Intro decision history](HEO_2026-11-10_ABSTRACT_INTRO_AND_CLAIM_DECISION_HISTORY.md).

### November 7: newest actual author Word + native 45-comment scientific audit
PI uploaded **HEO_Manuscript_Revised_For_Collaborator (1).docx** and requested review of Abstract, Intro and full text, **suggested revisions in Word comments**, yellow requests filled only when supported, toolkit latest. The author text includes **strong mechanistic claims** (R2 rapid near-surface, R3 diffusion-limited unreacted core, R4 interfacial dominance, Mg selective suppression and BM reaction transfer) that are plausible **hypotheses**, but currently **unproven as material-specific outcomes**.

Assistant generated a **14-page six-figure Word containing 45 actual Word comments**, kept 9 yellow collaborator data requests, filled known author and co-correspondence. Current reviewed Word scientific body was **intentionally not rewritten**; comments require PI approval before changes are applied. Title/method/captions and 24 bibliographic entries audited. See [all 45 comment inventory + 9 data holds](HEO_2026-11-10_WORD_45_COMMENT_AND_YELLOW_HIGHLIGHT_AUDIT.md), plus [full two text snapshots](HEO_2026-11-07_45_COMMENT_REVIEW_MS_FULL_TEXT_SNAPSHOT.md).

### November 10: GitHub-only source-of-truth consolidation
In response to PI request to resume in new chat without a separate handoff, archived:
- full text of **author source Word** and **review Word** into searchable GitHub Markdown;
- current authoritative scientific/quantitative/figure state and exact DOCX hashes;
- exact Abstract/Intro candidate/vs-approved decision chain;
- comment IDs 0–44 and 9 highlighted unknown-data locations;
- this historical narrative.
The active START_HERE and README have to point to this new authority and remove **superseded 2026-10-12 “AFM, v21, Introduction next”** instructions. This operation **does not edit source Word/SI**, create new raw measurements, prove unresolved mechanisms or imply a submission.

## B. Scientific and editorial no-regression checks

**Locked data (unless PI reopens):**
- Four original complete GITT series, 65/76/48/56 pulses, I=100 mA/g, 600s/3600s, t63 E3 to end.
- L1/L3/L4 HEO 6/25/55, BM 9/38/60, Mg 7/24/42, BM-Mg 9/35/46.
- Region charge matrix and signed changes as Nov-10 authority.
- BM R2 dominant gain, R4 additional gain, R3 reduction; Mg R3 largest loss; no simple R3→R4 transfer.
- ΔErest R3 time-window decomposition and composition-specific hump, interpretation secondary.
- Prior source data uncertainties and pending lab metadata.

**Physical claims to avoid as established without new evidence:**
- t63 directly reports single diffusivity/rate constant;
- four unique element-specific reaction stages “proven” from GITT;
- R2 exclusively rapid surface reduction, R3 specifically core diffusion-limited, R4 exclusively interfacial;
- ball milling transfers reduced material physically from R3 into R2/R4 or guarantees accelerated elementary reaction;
- Mg is universally inactive or stabilizes a measured (Mg,M)O phase in these powders;
- an XPS ~579eV peak proves Cr(VI) or oxygen defects absent calibration;
- Ga-containing spinel indexing in nominal Ga-free powder is accurate;
- “all four 0.1C rates recover baseline” without actual source;
- 729 simulated boundary perturbations count as electrochemical replicates.

**Current task status:**
- Complete source Word reviewed; comments **45 proposed**; no PI approval of replacements yet.
- Yellow metadata unknown until collaborator sends actual source. Do not invent.
- Manuscript target journal undecided; neutral formatting desired.
- Main–SI newest consistency still pending.
- Resolve actual author feedback in next chat; no extra user “handoff text” needed.

## C. Prior primary evidence files worth retaining

| Topic | Historical authority / evidence |
|---|---|
| Original raw GITT provenance | [Raw-workbook audit](../modeling/HEO_FOUR_SAMPLE_RAW_WORKBOOK_AUDIT_2026-10-12.md), [Nov5 four-sample check](../modeling/HEO_FOUR_SAMPLE_RAW_GITT_KINETIC_BOUNDARY_CHECK_2026-11-05.md) |
| t63-only final regions | [Nov6 explicit PI decision v35](HEO_V35_T63_ONLY_L4_SHOULDER_REASSIGNMENT_2026-11-06.md) |
| Manuscript stage-origin pivot | [Oct12 story lock](HEO_STAGE_ORIGIN_STORY_LOCK_2026-10-12.md) |
| Exact HEO region terminology | [Nov3 terminology](HEO_TERMINOLOGY_AND_WRITING_GUIDE_2026-11-03.md) |
| Physically informed source comparison | [Nov3 HEO prior art](HEO_SPINEL_HEO_LITHIATION_VOLTAGE_REGION_MECHANISM_PRIOR_ART_2026-11-03.md) |
| R3 hump original decomposition | [Nov6 time-window raw](HEO_V39_R3_HUMP_RAW_TIME_WINDOW_ANALYSIS_2026-11-06.md) |
| R3 literature integration | [Nov6 main/SI v40](HEO_V40_R3_HUMP_CROSS_MATERIAL_LITERATURE_INTEGRATION_2026-11-06.md) |
| Figures 1–6 restyling | [v41](HEO_V41_ARTWORK_CAPTION_REFERENCE_AUDIT_2026-11-06.md), [v42](HEO_V42_FIGURE_PLACEMENT_REGULAR_TYPOGRAPHY_2026-11-06.md), [v43](HEO_V43_FIGURE6_QUALITATIVE_QOCV_REDESIGN_2026-11-06.md) |
| Current PI-assisted language control | [Nov10 Abstract/Intro review history](HEO_2026-11-10_ABSTRACT_INTRO_AND_CLAIM_DECISION_HISTORY.md), [Toolkit v0.22](https://github.com/tyoon-lab/Yoon-Lab-Publication-Toolkit/blob/main/MANUSCRIPT_VOICE_CONSTITUTION.md) |

**Never erase this record merely because a later manuscript chooses a simpler rhetorical framing. The *paper* should be clean of development debris; the GitHub research history should preserve discarded alternatives and reasons.**