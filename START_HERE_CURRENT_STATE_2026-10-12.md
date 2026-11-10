# HEO — START HERE: current authoritative state (reconciled 2026-11-10)

**This is the SINGLE ENTRY POINT for starting a new HEO chat WITHOUT a separate handoff.**

**Status date: 2026-11-10** for GitHub records; the **latest scientific Word review was produced 2026-11-07**. The Nov-10 operation updated **GitHub text records only**. It did **not** modify a Word manuscript, SI, figures, new experimental data or an approved Abstract; **no journal is selected, no submission**.

## 1. Read these files IN ORDER

1. **[Authoritative science, current exact Word identities, numbers, figures and remaining gates](manuscript/HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md).** This takes priority for current physics/numeric boundaries.
2. **[All Abstract/Introduction deliberation, PI text and pending wording choices](manuscript/HEO_2026-11-10_ABSTRACT_INTRO_AND_CLAIM_DECISION_HISTORY.md).** This takes priority for *what the PI wants to say* and what is STILL PROPOSED.
3. **[All 45 native Word comments (IDs 0–44), nine unresolved yellow note locations, change actions](manuscript/HEO_2026-11-10_WORD_45_COMMENT_AND_YELLOW_HIGHLIGHT_AUDIT.md).** These are *suggestions*, not applied body changes.
4. **[Full scientific and editorial process, pivots and discarded alternatives Sep→Nov](manuscript/HEO_2026-11-10_DEVELOPMENT_TRAJECTORY_AND_SUPERSEDED_DECISIONS.md).** This explains why the science/storyline differs from older locked files.
5. **[Actual author-uploaded Nov7 Word full text](manuscript/HEO_2026-11-07_AUTHOR_UPLOADED_MS_FULL_TEXT_SNAPSHOT.md)** and **[Nov7 45-comment review Word full text](manuscript/HEO_2026-11-07_45_COMMENT_REVIEW_MS_FULL_TEXT_SNAPSHOT.md)**. These are GitHub full-text captures, with line-wrap artifacts, no binary images or native Word comment bodies. Use them to inspect actual wording when the DOCX bytes are not available in the new chat.

For original source figures, experiment details, manuscript provenance:
- [PI-accepted t63-only region cuts, accepted November 6](manuscript/HEO_V35_T63_ONLY_L4_SHOULDER_REASSIGNMENT_2026-11-06.md)
- [Original raw 4-workbook GITT check](modeling/HEO_FOUR_SAMPLE_RAW_GITT_KINETIC_BOUNDARY_CHECK_2026-11-05.md)
- [HEO terminology/physically grounded regional assignment](manuscript/HEO_TERMINOLOGY_AND_WRITING_GUIDE_2026-11-03.md)
- [Main/SI v40 R3 hump raw/literature analysis](manuscript/HEO_V40_R3_HUMP_CROSS_MATERIAL_LITERATURE_INTEGRATION_2026-11-06.md)
- [Figure 6 v43 conceptual QOCV decision](manuscript/HEO_V43_FIGURE6_QUALITATIVE_QOCV_REDESIGN_2026-11-06.md)

## 2. Which Word file currently has authority?

- **Author's latest uploaded source:** HEO_Manuscript_Revised_For_Collaborator (1).docx, SHA256 f9eb838fc8e4bc792e1feb25ea8be7b756d69c98157133f8bdc3b1cc9080ccf1, six figures. This source was edited by the PI; newer than earlier assistant v43.
- **Latest scientific REVIEW derivative:** HEO_Manuscript_Reviewed_With_Word_Comments_2026-11-07.docx, SHA256 021faf908cb2d4e274c0ae9fc805381456c1af204ad8a964a7ae364590a13b41; **14 pages, 6 figures, 45 native Word comments and nine paragraphs with yellow data requests**. **Those corrections are NOT all applied**; comment review and author acceptance still needed.
- **Earlier assistant clean journal-neutral collaborator draft:** HEO_Manuscript_Collaborator_Review_JournalNeutral_2026-11-07.docx, SHA256 acaab10dc45993ba7b8f959d8195e8627a4b4b89a7c6aee2f7745c8d0896eb4a; 11 pages; do NOT use its assistant-overhauled Abstract/Intro as PI authority. It contains no Word comments.
- **Latest known SI:** HEO_SI_v22_KineticBoundaryTextClean_2026-11-06.docx, SHA256 ad843d6a77db860e977790d5ddca387454d23a96cce3ee78b33b95cccdcf3920. Not resynchronized against the latest Nov7 author Word.

These **original DOCX binaries and figure images have NOT been committed** to GitHub. They were generated/uploaded as ChatGPT conversation artifacts; plaintext GitHub snapshots are not editable substitutes. If new chat can access attached bytes, verify exact SHA. If a future task requires editing Word/figures and bytes are unavailable, request the exact file; for *discussion* use GitHub full-text first.

**Authorship decided:** Seonghyeon Park, Yoonju Kang, Taekyung Yu*, Taeho Yoon*; Yu and Yoon are **joint corresponding**; English names of students and actual contributions to verify. Generic one-column Word while journal TBD (historical “AFM working target” is **superseded**).

## 3. Scientific conclusion (quantitative authority)

The paper is a **conversion-type spinel HEO materials study**, not a generic GITT method paper. Ask: *which portion of lithiation accounts for milling/Mg-induced capacity gain/loss, and which literature-supported chemical processes are likely to be relatively influential there?*

**Main result = signed nominal GITT pulse charge assigned to t63-defined electrochemical regions.** Kinetic trajectories and the R3 voltage-recovery hump support physical interpretation; they do not trump the charge result. The four regions are **not** four uniquely proven pure reactions.

**Four raw GITT sources:** 65/76/48/56 complete pulses, each 100mA g−1 ×600s →16.6667mAh g−1; 3600s rests, signed E3s-to-rest-end t63. After-pulse L1/L3/L4 (PI final):
- HEO **6 / 25 / 55** → R1/R2/R3/R4 **100.0 / 316.7 / 500.0 / 166.7**
- BM-HEO **9 / 38 / 60** → **150.0 / 483.3 / 366.7 / 266.7**
- Mg-HEO **7 / 24 / 42** → **116.7 / 283.3 / 300.0 / 100.0**
- BM-Mg-HEO **9 / 35 / 46** → **150.0 / 433.3 / 183.3 / 166.7**
Values mAh g−1. **Do not use the earlier superseded Mg L4=39/40.**

**Signed matched changes (R1/R2/R3/R4):**
- BM−HEO: **+50 / +166.7 / −133.3 / +100** (total +183.3).
- BM-Mg−Mg: **+33.3 / +150 / −116.7 / +66.7** (total +133.3).
- Mg−HEO: **+16.7 / −33.3 / −200 / −66.7** (total −283.3).
- BM-Mg−BM: **0 / −50 / −183.3 / −100** (total −333.3).

BM **largest gain R2**, **additional R4 gain and R3 loss**; Mg **largest loss R3** (also affects other regions). BM R3+R4 combined change is **negative**, so **DO NOT draw a transfer arrow R3→R4**. No claim that (t_{63}) proves surface/core specific pathways or intrinsic diffusion alone. Each physical interpretation must be constrained by published studies and actual data.

GCD first-lithiation 0.1 C capacities **901.25/1056.10/731.15/944.07 mAh/g** are from separate continuous-cycling measurements, **not equal to** protocol GITT totals 1083.3/1266.7/800/933.3. 729 ±1 pulse combinations are **deterministic boundary sensitivity, not replicates**; strict Mg-R3 dominance in milled pair **702/729**.

**R3 hump:** pristine ΔErest R3 start→peak +44.2mV, with **+37.5mV from 10–60min** dominating; weak +8.6mV Mg; both milled R3 amplitudes decline. Hypothesis heterogeneous delayed re-equilibration; no confirmed core-shell structural gradient/homogenization. See source notes.

## 4. Fig1–6 design and evidence status

- **Fig1** TEM/SAED/EDS of 4 materials; Ga-free powder contradicts HRTEM **CoGa2O4** indexing; raw diffraction required.
- **Fig2** BET (Mg-free **4.61×**, Mg pair **2.56×** from milling), SEM, Ni/Co/Fe/Mn/Cr/O/Mg XPS; Cr2p ~579eV uncertain, no validated oxidative-state interpretation.
- **Fig3** a–d four-source first-three-cycle profiles common voltage −0.1 to 2.8V and charge axes, sample names inside; e 100 cycles, f rate full legend. Tester data provenance still needs check.
- **Fig4** all four raw GITT pulsewise t63, ΔErest, QOCV with t63-only dashed boundaries; no extra headline/footnote/pulse-count parentheses/“late t63 shoulder” label.
- **Fig5** four regional-charge bars and signed intervention comparisons; title removed, panel b/c names within axes, panel letters outside, all normal-weight text where retypeset.
- **Fig6** actual pristine-HEO QOCV curve plus a few **qualitative** effect arrows: BM R2+/R4+, BM/Mg R3− and literature-guided physical candidates. **Avoid boxes and duplicate Figure5 numbers.** User previously said v42 was too similar to Figure5; v43 is a *candidate* pending final PI figure approval.

Place Figures1+2 under §2.1 heading; Fig3 under §2.2; Fig4 under §2.3; Fig5 under §2.4; Fig6 under §2.6. Original microscope/XPS bitmap/vector internal text may need native source to normalize font.

24 main references renumbered; each claim's DOI/publisher relevance not yet exhaustively reverified. SI v22 includes S1–S7 and Table S6, not yet aligned with latest main.

## 5. Current Abstract/Introduction status — important

The PI now prefers a **causal mechanism-first abstract**:
morphological/cation modification → underlying lithium-storage mechanism remains hard to attribute **because overlapping chemical/structural and possible interfacial processes** → total capacity and spectroscopy give different partial views → GITT **t63-only electrochemical regions** and nominal regional charge comparison → matched BM/Mg largest regional gain/loss → plausible R2/R3 literature-based process interpretation → materials-design significance.

- **First two sentences** PI-preferred, keep.
- Avoid reflex **“Yet”** (explicit PI wording preference), empty abstractions and globally defensive tone. “However” is present in PI-authored later text; meaning governs.
- **No numerical regional charge ranges in the next proposed Abstract** (latest explicit PI request); keep full numerical evidence in Results.
- Do **not claim** spectroscopy exclusively qualitative, impossible precedent for electrochemical staging, each t63 region a proved isolated reaction, R2 a verified rapid surface reaction, R3 a proved diffusion-limited core, R4 solely interfacial, or Mg uniquely suppressing R3.
- The latest assistant minimal-edit draft is **NOT PI APPROVED and NOT inserted into Word**. Read the full [Abstract/Intro decision history](manuscript/HEO_2026-11-10_ABSTRACT_INTRO_AND_CLAIM_DECISION_HISTORY.md) before touching text.
- Nov7 Word was intentionally left mostly intact for **comment-only review**, despite mechanism language needing revision. Read **all 45 comment IDs** before changing.

## 6. Immediate next work (actual priority)

1. PI decides wording at Word comments **2, 4–7, 18–19, 23–29, 30–33**: Abstract/Intro, physical region assignment, BM/Mg mechanisms, R3 hump, Fig6, conclusion. Make *scoped* edits after approval, not blanket overhaul.
2. Collaborator supplies **nine yellow-note locations**: Mg precursor and stoichiometry, true coprecipitation and milling conditions, BET degassing, powder XRD+ICP, source HRTEM indexing, calibrated matched XPS, actual electrode/cell/electrolyte/FEC/loading/1C/rate metadata. No invented routine recipes.
3. Correct BET wording to **4.6× vs 2.6×** and “reproducible inflections” to operational landmarks. Main/SI GITT charge and GCD basis consistent.
4. Revise figures/captions only for justified corrections, ensure Fig6 makes **interpretive** rather than duplicate Fig5 quantitative contribution, source image text/labels verified.
5. After PI accepts text and collaborator measurements, synchronize main vs **SI v22** (S tables and figures), audit 24 citations and source applicability, render final Word, only then select/apply target journal requirements.

**Open manuscript state: scientific revision COMMENTED, not yet fully accepted or submission-clean.** The next chat should begin by reading these five files rather than asking for a separate handoff.

## 7. Historical record retention

This START_HERE **replaces the outdated 79-kB historical index** whose bottom still said “begin with v22 / AFM / Introduction line-by-line” and whose top had many mutually superseded updates. The old exact text is preserved in [history/START_HERE_CURRENT_STATE_PRE_2026-11-10_RECONCILIATION.md](history/START_HERE_CURRENT_STATE_PRE_2026-11-10_RECONCILIATION.md) and Git history. Old README likewise in [history/README_PRE_2026-11-10_RECONCILIATION.md](history/README_PRE_2026-11-10_RECONCILIATION.md). These are for audit, not ongoing workflow direction.

**Toolkit authority:** [Yoon Lab Publication Toolkit v0.22 manuscript voice constitution](https://github.com/tyoon-lab/Yoon-Lab-Publication-Toolkit/blob/main/MANUSCRIPT_VOICE_CONSTITUTION.md), v0.21 source/Word data gate. PI-approved physical wording outranks decorative style changes.