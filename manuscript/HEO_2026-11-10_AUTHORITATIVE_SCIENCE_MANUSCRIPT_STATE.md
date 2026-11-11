# HEO: authoritative current research and manuscript state — 2026-11-10

> **2026-11-11 TEXT STATUS UPDATE:** The PI approved the full Abstract and four Introduction paragraphs, recorded verbatim in [this new text-lock record](HEO_2026-11-11_PI_LOCKED_ABSTRACT_INTRODUCTION_AND_DECISION_LOG.md). This file remains authoritative for scientific numbers, evidence strength and pending source audits. Its older statements that Abstract/Intro wording was unapproved are dated snapshots. The GitHub documentation update does not change DOCX binaries, native comments, figure assets, SI or raw data.


## Purpose and authority

This file is the stable *research/science authority* for the next session. Begin at [START_HERE_CURRENT_STATE_2026-10-12.md](../START_HERE_CURRENT_STATE_2026-10-12.md), which links the live state, a full decision trajectory, the Abstract/Introduction deliberation, and the Word-review comment/action ledger. This file **does not claim that unpublished proposed text has been approved or applied to the Word**.

**Evidence priority:** (1) most recent explicit PI decision; (2) the actual uploaded author-edited Word for author wording; (3) numerical GITT evidence from all four original raw workbooks and adopted operational boundaries; (4) accepted actual figures/SI; (5) related verified literature with composition limitations; (6) prior assistant proposals. Older “locked” files remain historically meaningful but can be superseded by more recent PI direction. Keep science status separate from editor suggestions, missing metadata, and portal submission.

**Current activity:** post-November-7 full manuscript review. **No target journal selected.** Generic single-column paper. **Not submitted.** The present request is GitHub documentation, not Word editing.

## Verified exact Word identities

| File | Authority | SHA-256 | Local status |
|---|---|---|---|
| HEO_Manuscript_Revised_For_Collaborator (1).docx | Latest author-uploaded source on Nov 7, 2026 | f9eb838fc8e4bc792e1feb25ea8be7b756d69c98157133f8bdc3b1cc9080ccf1 | 6 figures; 11 highlighted paragraphs including 2 author placeholders; 0 native Word comments |
| HEO_Manuscript_Reviewed_With_Word_Comments_2026-11-07.docx | Latest assistant scientific-review copy, **45 actual Word comments** | 021faf908cb2d4e274c0ae9fc805381456c1af204ad8a964a7ae364590a13b41 | 14 rendered pages; 6 figures; 9 unresolved highlighted paragraphs; 45 comments |
| HEO_Manuscript_Collaborator_Review_JournalNeutral_2026-11-07.docx | Earlier assistant *clean collaborator draft*, not the authority for latest scientific comments | acaab10dc45993ba7b8f959d8195e8627a4b4b89a7c6aee2f7745c8d0896eb4a | 11 pages; 6 figures; 24 references; no Word comments |
| HEO_SI_v22_KineticBoundaryTextClean_2026-11-06.docx | Latest known SI text, not independently re-synchronized with newest Nov 7 main | ad843d6a77db860e977790d5ddca387454d23a96cce3ee78b33b95cccdcf3920 | 10-page prior render; S1–S7, six supporting figures, multiple tables; last MS↔SI cross-check pending |

The two November-7 Word full-text snapshots are **actually committed** to GitHub (see links below) to allow content-based future review without depending solely on binary availability:
- [Author-uploaded Word full-text snapshot](HEO_2026-11-07_AUTHOR_UPLOADED_MS_FULL_TEXT_SNAPSHOT.md)
- [45-comment reviewed Word full-text snapshot](HEO_2026-11-07_45_COMMENT_REVIEW_MS_FULL_TEXT_SNAPSHOT.md)

These are lossy page-text extracts, **not binary Word**, and omit native comments and image data. GitHub Markdown audit files are not themselves proof that the latest DOCX or SI binaries were uploaded. **Use the separate audit ledger for all 45 Word comment contents/anchors.**

## Authorship and packaging

The PI explicitly set order **Seonghyeon Park, Yoonju Kang, Taekyung Yu*, Taeho Yoon***; Yu and Yoon **joint corresponding authors**. Current English affiliations list Department of Chemical Engineering, Kyung Hee University, Yongin, Republic of Korea, with co-correspondence tkyu@khu.ac.kr and tyoon@khu.ac.kr. Student English romanizations and contributions await author confirmation. No specific journal; no AFM formatting, AFM target presumption, publisher boilerplate, or fabricated ethics/data/AI declarations.

## Scientific question and evidence hierarchy

The study asks **where along conversion lithiation a morphology-changing intervention (ball milling) or a cation-chemistry intervention (Mg incorporation) increases or decreases accessed charge** and what plausible physical processes are prominent in those parts. Conventional full-profile capacity mixes overlapping reductions, oxide structural transformations, metal/Li2O nanocomposite development, and possible interface charge. State-resolved spectroscopy provides valuable (sometimes quantitative) chemical information but does not itself resolve the change in pulse-integrated GITT charge assigned to each kinetically selected interval.

**Primary direct finding:** t63-defined **electrochemical-region-resolved nominal GITT charge** separates signed material-modification effects otherwise hidden in total capacity. **Supporting kinetic observation:** initial R1 t63 trajectory and late R3 relaxation magnitude/shape vary across processing/composition. **Physical association:** early Li uptake, oxide destabilization/early conversion, further intermediate oxide reduction/metal-Li2O development, and late lithiation/interface participation are *literature-grounded candidates*, not experimentally measured unique dominant pathways in each of the four present powders.

Crucial terminology (see [Nov 3 terminology guide](HEO_TERMINOLOGY_AND_WRITING_GUIDE_2026-11-03.md)):
- **Overlapping reaction processes:** chemically distinct but concurrently contributing insertion/reduction/reconstruction/product-development processes.
- **Electrochemical regions R1–R4:** **measured coordinate intervals** defined by operational changes in t63 during GITT. Do not call them four separately validated reaction stages/chemical phases.
- **Dominant reaction processes:** literature-supported *relative prominence hypotheses* within a region. They may overlap across boundaries. Prefer “associated with”.
- **GITT regional charge:** nominal I × pulse-duration × number of complete pulses. It is neither a phase-specific Faradaic inventory nor identical to continuous 0.1C GCD capacity.
- **t63:** 63.212% first crossing of the *signed* E(3s)-to-rest-end voltage recovery; operational effective time of a multicomponent response, not intrinsic D, Rct, or elementary rate constant.
- **ΔErest:** absolute 3s-to-rest-end voltage recovery, not directly reaction charge or simply kinetic overpotential.
- **QOCV:** 60-min rest-end voltage under finite time, not certified equilibrium OCV.
- The final **region boundaries use t63 only**. Earlier GITT-QOCV joint segmentation is superseded. ΔErest and QOCV remain physically informative supporting plotted quantities.

## Source data and exact adopted boundaries

Four original complete first-lithiation workbooks:
1. HEO GITT 로우 데이터.xlsx — 65 complete negative-current pulses.
2. BM HEO 3 GITT 로우 데이터.xlsx — 76 pulses.
3. HEO 3 Mg 로우 데이터.xlsx — 48 pulses.
4. BM HEO 3 Mg 로우 데이터.xlsx — 56 pulses.

Nominal protocol **100 mA g−1**, **600 s pulse**, **3600 s rest**, giving **16.6667 mAh g−1 per complete pulse**. Common E(3 s) after interruption, signed recovery and t63 first crossing. Source provenance [four-workbook audit](../modeling/HEO_FOUR_SAMPLE_RAW_GITT_KINETIC_BOUNDARY_CHECK_2026-11-05.md), [adopted t63 boundaries/robustness](HEO_V35_T63_ONLY_L4_SHOULDER_REASSIGNMENT_2026-11-06.md). Partial terminal pulse excluded.

**Adopted, PI-approved boundary index after each pulse**, NOT universal phase boundaries:

| Material | L1 / L3 / L4 | R1 | R2 | R3 | R4 | Total nominal GITT |
|---|---|---:|---:|---:|---:|---:|
| HEO | **6 / 25 / 55** | 100.0 | 316.7 | 500.0 | 166.7 | 1083.3 |
| BM-HEO | **9 / 38 / 60** | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 |
| Mg-HEO | **7 / 24 / 42** | 116.7 | 283.3 | 300.0 | 100.0 | 800.0 |
| BM-Mg-HEO | **9 / 35 / 46** | 150.0 | 433.3 | 183.3 | 166.7 | 933.3 |

All charge values mAh g−1. Boundary after-pulse convention: R1 contains pulses 1..L1, R2 L1+1..L3, R3 L3+1..L4, R4 L4+1..end.

**Signed matched comparisons**, mAh g−1:

| Intervention | ΔR1 | ΔR2 | ΔR3 | ΔR4 | ΔTotal |
|---|---:|---:|---:|---:|---:|
| BM-HEO − HEO | +50.0 | **+166.7** | −133.3 | **+100.0** | +183.3 |
| BM-Mg-HEO − Mg-HEO | +33.3 | **+150.0** | −116.7 | **+66.7** | +133.3 |
| Mg-HEO − HEO | +16.7 | −33.3 | **−200.0** | −66.7 | −283.3 |
| BM-Mg-HEO − BM-HEO | 0.0 | −50.0 | **−183.3** | −100.0 | −333.3 |

**Strongest contrast:** milling largest positive R2, also positive R4 but negative R3; Mg largest negative R3, with R2/R4 also affected. **Do not claim** milling transfers a chemically identified R3 reaction into R2 or R4. In fact milling Δ(R3+R4)=−33.3 (no Mg) and −50.0 (Mg present); this directly contradicts a simple R3→R4 charge-transfer narrative.

The ±1-pulse independent boundary perturbation exercise enumerates **729 combinations per matched pair**, a deterministic geometry/sensitivity check, not physical replicates or statistical confidence: milling R2 positive and R3 negative in 729/729; Mg R3 negative in 729/729. Mg R3 is strictly largest negative term unmilled 729/729 and milled 702/729, with 18 ties in the latter. Do not imply a fully unique inflection-detection algorithm or replicate reproducibility, particularly for late Mg slope changes (1.26 and 1.76 seconds compared with nominal 3-second logging).

**Separate continuous GCD 0.1C first lithiation values**, from Fig3/reporting: HEO 901.25, BM-HEO 1056.10, Mg-HEO 731.15, BM-Mg-HEO 944.07 mAh g−1. These values and total GITT pulse charges are different measurement/protocol bases; do not force them equal or substitute them when reporting signed regional GITT ΔQ.

## R1–R4 physical interpretation, by evidence level

| Region | Measured definition | Literature-supported physical candidates | Claims requiring new direct validation |
|---|---|---|---|
| R1 | early post-transient t63 trajectory to L1 | initial Li uptake, cation rearrangement, spinel-to-rocksalt-like changes before extensive conversion | exact site/metal valence changes, insertion barrier or intrinsic faster surface reaction |
| R2 | L1→L3, central t63 trend | parent oxide destabilization/reconstruction; early transition-metal reduction; overlapping initial metal/Li2O product emergence | proven surface-only or faster-than-R3 conversion |
| R3 | L3→L4 | further reduction of partially reconstructed intermediate oxides; development of metal/Li2O products; heterogeneous reaction states with delayed re-equilibration | proven diffusion-limited unconverted **particle core**, exact Fe/Mn/Cr order, shell thickness or metal/Li2O yield |
| R4 | L4 to final pulse | later residual oxide reduction plus potential interfacial Li storage and parasitic contributions at deep lithiation | R4 uniquely/dominantly interfacial, or a distinct isolated redox reaction |

“Deep lithiation” is a position in the voltage/charge trajectory, not a mechanistic definition. Distinguishing further residual reduction from interfacial storage requires state-specific additional data. Related studies (HEO operando XAS, spinel/rocksalt XRD/XAS, NiO GITT region precedent) establish plausible process classes, not this sample's unique assignments. In particular Luo 2022 studies Co-free CrMnFeNiCu rather than present FeCoCrNiMn, and Triolo studies a Zn-containing spinel.

## R3 ΔErest hump and kinetic support

Original four workbooks give pristine HEO pulse 26→50 **145.1→189.3 mV**, +44.2 mV. Decomposing change by voltage-recovery window: **3–60s −9.8 mV; 1–10min +16.5mV; 10–60min +37.5mV**. The late window dominates the positive hump increment. Mg-HEO has only ~+8.6mV weak interior maximum; BM-HEO and BM-Mg-HEO amplitudes decline over R3 despite all four increasing t63 there. Common-QOCV 0.50 V recovered amplitude HEO 185.5mV, BM 142.6mV while |dQOCV/dQ| HEO 0.83 < BM 1.14 mV/(mAh g−1); a **slope-only amplification** does not suffice for this comparison. It does **not prove** absolute suppressed slow modes, kinetic homogenization, or a unique intermediate oxide phase. Literature analogies: FeF3 GITT phase heterogeneity, Fe3O4 transformation, Li redistribution during SiO-graphite and graphite/LFP rest. See [time-resolved raw analysis](HEO_V39_R3_HUMP_RAW_TIME_WINDOW_ANALYSIS_2026-11-06.md) and [literature-integrated main/SI v40](HEO_V40_R3_HUMP_CROSS_MATERIAL_LITERATURE_INTEGRATION_2026-11-06.md).

Interpretation of R1 BM response also needs common-state caution: the initial unmilled/milled pulses differ drastically in rest-end QOCV. Different first-pulse t63 values establish altered *trajectory*, not a unique faster intrinsic Li insertion.

## Figure map and actual status

| Figure | Scientific role | Accepted/latest visual history and open gates |
|---|---|---|
| Fig1 | four-material TEM/HRTEM/SAED/EDS | original micrograph montage retained. Existing **CoGa2O4** HRTEM indexing contradicts nominal Ga-free chemistry; DO NOT silently replace with Spinel 311 without checking raw d-spacing/FFT/card. XRD/ICP pending |
| Fig2 | N2 BET, SEM, Ni/Co/Fe/Mn/Cr/O/Mg XPS | BM surface areas: Mg-free **3.94→18.16 = 4.61×**, Mg-containing **6.49→16.64 = 2.56×**. Source vector XPS and fit curves from poster/PPT; Cr~579eV identity/calibration unresolved; Mg 1s detects surface Mg, not necessarily substitution site. Some source-image label clipping |
| Fig3 | 4 sample first-three-cycle GCD a–d, 100-cycle e, rate f | common x limits −35..1100 and voltage −0.1..2.8 V in historical v41; a–d names inside, f legend; source from poster vector plots. Check source GCD numbers, 100cycle/rate actual tester settings and recovery claims |
| Fig4 | ALL FOUR original pulsewise t63/ΔErest/QOCV | pulse counts hidden from panel labels; remove unneeded “late t63 shoulder” literal, bottom explanatory labels and redundant headings; keep accepted t63-only dashed boundaries and material panel identifiers |
| Fig5 | nominal GITT charge distribution and matched ΔQ | absolute four-region bins and signed milling/Mg differences above; no extra overall figure title; b/c panel titles inside, normal-weight text |
| Fig6 | **qualitative physical interpretation** on real pristine-HEO QOCV curve | Former boxes and v42 Figure5-duplicating bar/numeric list rejected; v43 qualitative arrows R2 BM gain, R3 BM/Mg loss, R4 BM gain plus representative candidates preferred; absolutely no R3→R4 reaction-transfer arrow. Last Nov7 author-edited caption contains mechanistic overclaims flagged in Word comment, so **not finally approved** |

Figures 1+2 after §2.1, Fig3 §2.2, Fig4 §2.3, Fig5 §2.4, Fig6 §2.6 (all immediately after headings as PI requested). Panel letter outside plot and text normal/nonbold across newly redrawn graphics; original embedded XPS/SEM lettering may still have pre-existing bold and requires editable source to fully correct. See [Figure v41 audit](HEO_V41_ARTWORK_CAPTION_REFERENCE_AUDIT_2026-11-06.md), [Figure v42 layout](HEO_V42_FIGURE_PLACEMENT_REGULAR_TYPOGRAPHY_2026-11-06.md), [Fig6 v43 conceptual design](HEO_V43_FIGURE6_QUALITATIVE_QOCV_REDESIGN_2026-11-06.md).

**Reference status:** main v41 onward contains **24 numbered citations** after removing uncited references; their bracket number mapping was checked against main text, but *not all bibliographic author/volume/page metadata or every claim-to-source relation independently checked*. SI may have different, older numbering; reconcile independently. Section S7 literature comparisons remain candidate context, not validation of an HEO-specific phase mechanism.

## Current textual editorial state: do not silently overwrite

User's Nov7 **author-supplied** manuscript contains a stronger Abstract/Intro with phrases “quantifying the charge associated with each process”, spectroscopy “qualitative and localized”, “regions governed by dominant reactions”, R2 rapid near-surface redox, R3 diffusion-limited core conversion, R4 interfacial dominance, and selective Mg suppression. These are all specifically **flagged as proposed revisions** in the latest **45-comment Word**; scientific text was largely **not edited**, because PI asked for suggestions as comments.

Subsequent discussion developed better Abstract logic: first two author-preferred opening sentences; explain *why* underlying mechanism is difficult to identify due to overlapping processes; acknowledge real quantitative chemical spectroscopy without equating that to regional charge; introduce GITT *as a solution to that information gap*, with t63-defined regions and 2×2 material comparison; only strongest **qualitative** regional gains/losses in Abstract (user asked **omit numerical charge ranges**); infer R2 oxide reconstruction/early metal reduction and R3 further intermediate oxide reduction/metal-Li2O evolution from literature. The PI explicitly dislikes “Yet” except where causally justified; “However” appears in their later draft and is not universally banned. A and B outside-critic drafts were discussed; B's flow preferred but “impossible”, exclusive chemistry, spectroscopy-only-qualitative, and “selectively suppresses” require correction.

**There is no newly PI-approved final Abstract/Introduction after the Word comment review.** Most recent assistant minimal-edit Abstract is a proposal, still absent from Word. Do not treat it as accepted or automatically insert it. See [full Abstract/Intro decision history](HEO_2026-11-10_ABSTRACT_INTRO_AND_CLAIM_DECISION_HISTORY.md) and [45-comment review action ledger](HEO_2026-11-10_WORD_45_COMMENT_AND_YELLOW_HIGHLIGHT_AUDIT.md).

Writing rules from Toolkit v0.22: evidence first, then P/plain observations, S/strong supported central results, C/calibrated for interpretation-critical uncertainties. Avoid blanket defensive academic prose and hollow nominalization, routine “not” construction, boilerplate “Together” or “Yet” in author's context, repeated caveats, and internal development rationale in submission text. Mechanistic testable hypotheses are permitted if literature grounded and distinctly labeled. **Do not rephrase author-accepted strong text without a scientific or readability reason.**

## Unresolved experimental and manuscript gates

Priority 0 (submission blocking):
1. Complete exact **Mg precursor/nominal stoichiometry/substituted element** versus 5→6-cation mixture; verify full synthesis conditions and actual batch.
2. **Electrode/cell**: active/carbon/binder types and ratios, coating/solvent/drying, loading, Li counter, separator, electrolyte + FEC, size, voltage limits, 1C rated-current definition, actual cycle/rate test schedule.
3. **CoGa2O4 indexing contradiction** with Ga-free powders; raw HRTEM d-spacing/FFT, SAED, diffraction reference.
4. **XPS original/fit source** and calibration, especially Cr 2p near 579 eV, O1s, Mg1s; avoid assigning Cr(VI) or oxygen defects without support.
5. **XRD/ICP-OES** raw traces, actual measured composition, crystallographic phase/magnesium site evidence; do not assert unmeasured single-phase bulk/microchemistry.
6. **BET conditions** degassing and exact figure values (4.6× vs 2.6×).
7. Review/comment decisions for strong speculative R1–R4 mechanism wording, Abstract and Intro; approve one text version before applying.
8. Reconcile **main vs SI v22** numeric/definition/caption/figure/citation references after current author Word edits.

Priority 1 (scientific/visual):
- Verify Fig3 continuous galvanostatic tester exports vs PPT-vector values; 100-cycle endpoint, rate-recovery claim and 0.1 C versus 5C protocols.
- Preserve region raw pulse indices and 729 sensitivity; compare late Mg 1–2 s feature against 3-s sample resolution and explicitly qualify operational boundary.
- Refine Figure6 so it explains candidate physical processes without restating Figure5 bars.
- Finalize 24-ref author/volume DOI mapping and each central paper's actual applicability.
- Check all panel letters normal type and outside axes; source XPS/SEM may require editable native graphic.
- Only after PI accepts edits: implement Word text/caption modifications, keep and resolve comments, clean collaborator yellow requests with real facts, rerender every page, verify Figure/SI/abstract cross-consistency.
- Choose journal later, then apply target-specific compliance and disclosure without altering the scientific story.

**Next-chat instruction:** do not request a new handoff. Begin by reading this file, the Abstract/Intro decision history, and the Word comment audit, then ask only for decisions on open substantive edits if needed. The proposed manuscript is **not** yet a submission-clean file.