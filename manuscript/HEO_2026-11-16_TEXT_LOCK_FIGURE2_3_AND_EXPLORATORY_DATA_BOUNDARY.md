# HEO manuscript — current editorial decisions and strict boundary to exploratory 3-cycle work (2026-11-16)

**Purpose:** record manuscript-level decisions made in this conversation and prevent exploratory cycle analysis being silently written into the paper. Read the original source audits for exact evidence and PI-approved wording. This is NOT a new version of the manuscript.

## Current manuscript text authorities
1. `HEO_2026-11-11_PI_LOCKED_ABSTRACT_INTRODUCTION_AND_DECISION_LOG.md`: the **exact PI-approved Abstract and Introduction (four paragraphs)**. Keep them verbatim unless explicitly reopened by the PI; the final P4 states: “The dominant reaction process in each region was then inferred from previous mechanistic studies of spinel conversion oxides.” This is an **inference per electrochemical region**, not a claim “each region was assigned as a dominant reaction process.” The abstract and introduction are not to be edited by analogy with later-cycle exploration.
2. `HEO_2026-11-11_FIGURE3_SOURCE_CHECK_AND_STUDENT_DATA_REQUESTS.md`: reviewed §2.1 BET/XPS wording, Fig3 caption and **two** §2.2 paragraphs, plus explicit raw source-data requests. The PI prefers the original **two body paragraphs** rather than inserting an unnecessary third.
3. `HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md`: raw original first-lithiation t63 R1–R4 regions, signed regional charges, figure logic, Word provenance, SI open questions. The first-cycle GITT region boundaries remain fixed.
4. `modeling/HEO_2026-11-16_CYCLE1_3_R1R4_HUMP_DELITHIATION_FULL_CONTINUITY.md`: **exploratory** multi-cycle research only. Its hypothesis refinements are *not* approved revisions of the Abstract or published mechanism text.

## Specific author text decisions already taken, not fresh tasks

**BET, §2.1:** use *“4.6-fold ... Mg-free”* (3.94→18.16 m²/g) and *“2.6-fold ... Mg-containing”* (6.49→16.64 m²/g); say SEM coarse agglomerate breakup is **consistent with** greater gas-accessible BET area, not that BET directly establishes electrochemical reactive area. **Delete early capacity comparison** from this structural paragraph.

**XPS, §2.1:** retain restrained wording: multiple transition-metal photoelectron signals, *potentially* different valences; Mg 1s near 1303 eV establishes **Mg within XPS sampling depth**, not Mg lattice-site substitution; O1s main 529.8eV consistent with M–O, higher-binding component may reflect surface hydroxyl/oxygen species. Keep highlighted note requesting **oxidation-state assignment references, fits, BE calibration**, source batch-matched XPS and additional composition proof. No unverified oxygen vacancy concentration or unique mixed-valence fitting claims.

**Figure 3:** Figure 3 a–d first three cycle 0.1C voltage profiles; e cycling 100 cycles at 0.1C; f rate 0.1,0.3,0.5,1,3,5→0.1C; **FEC-containing electrolyte** (exact fraction unresolved). 100cycle approximate curve-read capacity HEO ~415, BM ~583, Mg ~431, BM-Mg ~492 mAh/g; original tester raw files remain missing. Do not say **all recover baseline**; return to 0.1C gives **substantial yet incomplete** recovery, to be quantified with original files. Avoid **featureless** for low voltage GCD; “broad, overlapping voltage features” more accurate. Original graph first-charge/lithiation numbers HEO 901.25/609.12; BM 1056.10/782.08; Mg 731.15/458.91; BM-Mg 944.07/580.83 mAh/g; sign/first 'Charging' label pending original tester-protocol confirmation. Never substitute 600s GITT pulse sums for these independent 0.1C GCD numbers.
- Author explicitly asked to answer paragraph/caption comments in chat for copy/paste; **DO NOT generate new Word without a direct request**. Latest Word versions/number of comments as recorded in November 11 §2.1/2.2 source audit (33 retained in local Nov 11 draft, vs 45 in older Nov 7 review). Markdown commits do not preserve actual native Word comments.

## Strong scientific results vs experimental inference

**Reliable operational main result:** among four paired HEO electrodes, ball milling raises net first lithiation capacity mostly in t63-defined R2 while Mg incorporation lowers it mostly in R3. These are **kinetically defined charge regions**, with literature-inferred important pathways; no unique chemical identification.

**Exploratory multi-cycle observation:** C1 starts with a large extra charge and complex t63; C1 delithiation is already quite similar to C2/C3 delithiation; C2/C3 lithiation has highly reproducible QOCV, |ΔErest| hump, ~0.90 V dQ/dV local peak and normalized voltage-rest profiles. Mg shows residual local amplitude deficit ~0.9–1.0V, but the later-cycle region-to-C1-R3 causal mapping is unproven. R1–R4 can remain an empirical first-cycle segmentation; hump may serve as a cross-cycle observational anchor rather than a replacement boundary.

**Interpretive caution introduced by new work:** a t63 region boundary is often a **smooth slope reversal**, not a discontinuous unique reaction. First-cycle region charge perturbations may partly reflect moving operational region limits, so “R2 contains greatest signed charge gain” is defensible, while “this unique chemical process gained exactly that much capacity” is not. Regularized spectra quantify voltage-rest response weights, not identifiable chemical phase charges.

## Unresolved evidence requests
Refer to the authoritative Nov 11 Fig3 source checklist for exact raw GCD, 100cycle, rate test and FEC/formation/C-rate details; XPS BE references, sample/batch fits; Mg stoichiometry/source, XRD/HRTEM indexing, wrong CoGa2O4 identification; source editable figure data; SI/manuscript synchronization. If students send new data, reconcile before claiming Figure 3 exact 100-cycle/recovery values or over-assigning XPS chemistry.

## Outstanding PI decision: modeling / FEM
The user floated adding FEM simulation **after** the later-cycle GITT study, but no model selection, simulation execution or manuscript inclusion decision was completed. See `modeling/HEO_2026-11-16_FEM_SIMULATION_OPTION_AND_DISCRIMINATION_GATE.md`.

## Working rules
- Update GitHub **only on explicit user request**, not automatically.
- Word/DOCX only on explicit user request, preserve native comments and yellow highlighted source holds.
- Text/figure editing is not implicit permission to change the locked Abstract, Introduction or R1–R4.
- Avoid unsupported phase assignments and unnecessary defensive or abstract prose; represent observations first, then physical hypotheses with evidence strength.
- Next chat does not require a separate handoff: begin at new `START_HERE_CURRENT_STATE_2026-11-16.md`.
