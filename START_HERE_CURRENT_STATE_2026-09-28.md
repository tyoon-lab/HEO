# HEO — Current State, 2026-09-28

## Read this first

This file is the authoritative restart point for the HEO manuscript. A new chat/session should be able to resume from the repository without a separate handoff message.

## Current paper identity

Working title:

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Current target: **Advanced Functional Materials (AFM)** as the working target while the manuscript is developed to the strongest defensible form.

The paper is an HEO conversion-mechanism/materials paper using GITT relaxation as the diagnostic. It is **not** framed as a general GITT-method paper.

## Current authoritative files

- Main manuscript: `manuscript/HEO_MANUSCRIPT_V15_AFM_CAPACITY_KINETICS_2026-09-28.md`
- Supporting Information: `manuscript/HEO_SUPPORTING_INFORMATION_V10_CAPACITY_KINETICS_2026-09-27.md`
- Story lock: `manuscript/HEO_MANUSCRIPT_ARCHITECTURE_TOOLKIT_LOCK_2026-09-28.md`
- Abstract lock: `manuscript/HEO_ABSTRACT_LOCK_2026-09-28.md`
- Introduction lock: `manuscript/HEO_INTRODUCTION_LOCK_2026-09-28.md`
- Figure logic: `manuscript/HEO_FIGURES_3_7_CURRENT_LOGIC_V6_2026-09-27.md`
- Figure 3 logic/caption/source note: `manuscript/HEO_FIGURE3_ARTWORK_FINAL_NOTE_2026-09-27.md`
- Figure 3 source-provenance audit: `manuscript/HEO_FIGURE3_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`
- Figure 4 logic/caption/source note: `manuscript/HEO_FIGURE4_ARTWORK_FINAL_NOTE_2026-09-27.md`
- Figure 5 logic/caption/source note: `manuscript/HEO_FIGURE5_ARTWORK_FINAL_NOTE_2026-09-27.md`
- Figure 5 source-provenance audit: `manuscript/HEO_FIGURE5_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`
- Figure 5 nominal peak-localization authority: `manuscript/HEO_FIGURE5_DQDV_GITT_PEAK_CHECK_2026-09-27.csv`
- Figure 5 voltage-coordinate audit: `manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_AUDIT_2026-09-27.md`
- Figure 5 voltage-coordinate sensitivity: `manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_SENSITIVITY_2026-09-27.csv`
- Figure 6 microkinetic authority note: `manuscript/HEO_FIGURE6_FOUR_STEP_MICROKINETIC_NOTE_2026-09-28.md`
- Former cycle-history Figure 6 materials are retained as Supporting Information robustness assets: `manuscript/HEO_FIGURE6_ARTWORK_FINAL_NOTE_2026-09-27.md`, `modeling/HEO_FIGURE6_PANEL_DATA_2026-09-27.csv`, `modeling/heo_figure6_history_dependence.py`
- Figure 4 plotting code: `modeling/heo_figure4_capacity_kinetics_mismatch.py`
- HEO/BM conventional-GITT audit: `modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`
- HEO/BM state-matched ratios: `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`
- HEO/Mg exploratory cross-composition check: `modeling/HEO_MG_CROSS_COMPOSITION_GITT_CHECK_2026-09-27.md`
- Microkinetic authority: `modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`
- Microkinetic reference candidates: `manuscript/HEO_REFERENCE_CANDIDATES_MICROKINETICS_2026-09-28.md`
- Literature audit: `references/HEO_CONVERSION_GITT_LITERATURE_AUDIT_2026-09-26.md`
- Main-reference audit: `manuscript/HEO_REFERENCE_AUDIT_MAIN_V16_2026-09-28.md`
- Microkinetic reference candidates: `manuscript/HEO_REFERENCE_CANDIDATES_MICROKINETICS_2026-09-28.md`
- Kinetic interpretation lock: `manuscript/HEO_KINETIC_INTERPRETATION_DECISION_LOCK_2026-09-26.md`
- Main scientific audit: `manuscript/HEO_MAIN_SCIENTIFIC_AUDIT_2026-09-27.md`

## Scientific event that creates the paper

**Ball milling increases accessible conversion capacity while the GITT relaxation becomes slower.**

This is the primary contradiction.

Mg is complementary but scientifically different:

- HEO → Mg-HEO: accessible conversion capacity decreases.
- $t_{63}$ increases, so capacity ↓ and slower relaxation are directionally consistent.
- however, the relaxation voltage-change magnitude also decreases.
- therefore Mg constrains **relaxation magnitude versus relaxation timescale/rate**, not a second capacity–rate contradiction.

Do not flatten BM and Mg into the same kind of mismatch.

## Frozen abstract

The PI-reviewed AFM-length abstract is provisionally locked for the current line-by-line review round:

> Faster conversion kinetics are generally expected to raise accessible capacity in conversion-type anodes. However, conversion couples electron transfer, structural reconstruction, nucleation/phase growth, and cation/oxygen redistribution, complicating the link between capacity and overall kinetics. This relationship is examined in spinel high-entropy oxide (HEO) anodes modified by ball milling or Mg incorporation. Galvanostatic intermittent titration (GITT) is used to characterize current-off relaxation in terms of the voltage relaxation magnitude and a characteristic relaxation time, $t_{63}$. Ball-milled HEO (BM-HEO) exhibits higher accessible conversion capacity but slower relaxation, contrary to the conventional expectation. Mg-containing HEO (Mg-HEO) shows lower accessible capacity and slower relaxation, as expected, while its voltage relaxation magnitude also decreases. Conventional GITT-derived apparent diffusivity, widely used to compare Li-ion transport kinetics, fails to preserve the observed kinetic ordering: $D_{\mathrm{app}}$ ranks BM-HEO faster even though its relaxation is slower. Microkinetic analysis recovers the conventional capacity–rate coupling under uniform kinetic acceleration but shows that a heterogeneous multistep conversion network can produce higher accessible capacity with slower relaxation. These results distinguish reaction accessibility from kinetic speed and show that neither capacity gains nor apparent diffusivity alone establishes improved overall conversion kinetics, providing a basis for evaluating materials modifications in multistep conversion systems.

The 2026-09-28 review deliberately:
- keeps the unexpected BM result out of the background premise;
- distinguishes BM's capacity–relaxation contradiction from Mg's complementary magnitude–timescale constraint;
- contextualizes conventional GITT-derived apparent diffusivity as a widely used kinetic comparator before showing its failure to preserve the observed ordering;
- uses a literature-grounded homogeneous four-step microkinetic model to recover the conventional single-step limit first and then establish a finite step-selective regime with higher cutoff capacity and slower relaxation;
- ends with materials-evaluation significance rather than a GITT warning alone.

Do not rewrite the abstract casually. Reopen only if body review or new analysis changes a scientific claim.


## 2026-09-28 PI line-by-line writing update

The Abstract and Introduction have now been reviewed as one synchronized argument.

Frozen/current writing decisions:
- Abstract remains the compressed control surface; scientific edits must propagate to the body, but wording is not copied mechanically.
- Introduction now follows: physical conversion problem → conventional GITT apparent-diffusivity interpretation → direct relaxation descriptors + capacity comparison → HEO/BM/Mg experimental leverage → present-study question and minimal analysis map.
- Use $D_{\mathrm{app}}$ consistently after definition.
- Use `pristine HEO` for the unmodified reference on first definition.
- Avoid repeated lists of conversion processes, repeated contrast markers, and abstract wording such as `manifestation` or unexplained `kinetic ordering`.
- Section 2.2 title is now **Ball milling increases accessible capacity whereas Mg incorporation decreases it**.
- Figure 3(b) uses **lithiation / delithiation**, not lithiation/delithiation.
- Figure 3 main role remains accessible reaction extent only; kinetic interpretation begins in Figure 4.
- Current Figure 3 artwork was regenerated from embedded Origin vector previews; panel (c) CE traces were removed.
- Figure 5 and Figure 6 captions have been synchronized to their current final panel architectures.

Current keywords:
`high-entropy oxide; conversion anode; GITT; apparent diffusion coefficient; voltage relaxation; ball milling; Mg incorporation; microkinetics`

## Figure 3 → Figure 7 logic

### Figure 3 — accessible capacity

Figure 3 panel logic is frozen for the current round:

- (a) first-cycle voltage profiles;
- (b) first-cycle lithiation/delithiation capacity + ICE summary;
- (c) absolute 0.1 C cycling;
- (d) absolute rate capability and 0.1 C recovery.

Core interpretation:
- BM increases accessible capacity.
- Mg decreases accessible capacity.
- capacity alone is not used to infer intrinsic conversion speed.

Cycle-resolved $dQ/dV$ is not a main Figure 3 panel. First-cycle cathodic $dQ/dV$ is reserved for Figure 5 conversion localization; cycle-resolved $dQ/dV$ belongs in the Supporting Information.

Source status: the latest Figure 3 working graphs are traceable to embedded Origin objects in `HEO 진행상황 (20260917).pptx`. The independent conventional cycling/rate raw files have not yet been recovered, so panel logic is frozen but final numerical-source reproducibility remains an artwork blocker.

### Figure 4 — decisive mismatch figure

Current final panel architecture:

- (a) representative **measured** GITT pulse/rest trace defining $\Delta E_{\mathrm{relax}}$ and $t_{63}$
- (b) HEO/BM state-matched conventional $D_{\mathrm{app}}$ ratio versus direct relaxation-rate ratio
- (c) median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ for all four materials
- (d) First-cycle delithiation capacity versus median $t_{63}$

Core median values over 200–800 mAh g⁻¹:

| Sample | $\Delta E_{\mathrm{relax}}$ (mV) | $t_{63}$ (min) | First-cycle delithiation capacity (mAh g⁻¹) |
|---|---:|---:|---:|
| HEO | 160.9 | 8.68 | 609.12 |
| BM-HEO | 176.3 | 11.57 | 782.08 |
| Mg-HEO | 109.5 | 11.01 | 458.91 |
| BM-Mg-HEO | 144.3 | 12.99 | 580.83 |

Panel interpretation:
- (d) shows the primary BM contradiction: capacity ↑ while $t_{63}$ ↑.
- (c) shows the Mg complementary constraint: $\Delta E_{\mathrm{relax}}$ ↓ while $t_{63}$ ↑.
- (b) shows that conventional $D_{\mathrm{app}}$ points in the conflicting direction for BM.

HEO/BM state-matched result:
- median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}=1.7817$
- $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}>1$ at 37/37 states
- median direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}=0.7622$
- direct rate ratio <1 at 35/37 states

The main Figure 4(b) must remain HEO/BM-HEO because this compositionally identical pair is the cleanest apparent-$D$ audit.

### Figure 5 — conversion localization

Figure 5 is now frozen as a three-panel localization test:

- (a) state-resolved first-cycle relaxation + background definition;
- (b) GITT excess / cathodic $dQ/dV$ comparison on a common voltage axis;
- (c) peak-voltage one-to-one comparison.

Each GITT excess peak is mapped using the **60 min rest-end voltage of the same GITT state**. Under the nominal background definition, the GITT-rest-end and first-cycle cathodic $dQ/dV$ peak pairs are within 32 mV for all four materials.

The 105-condition peak-location audit shows that HEO and Mg-HEO peak states are invariant and BM-HEO remains in a narrow 0.593–0.628 V band. The shallow BM-Mg-HEO feature has a broader 0.453–0.618 V peak-position range. Therefore the 32 mV statement is nominal, while the robust four-material result is that the directions of HEO → BM, HEO → Mg, and Mg → BM-Mg voltage shifts are preserved across all tested GITT definitions and match the $dQ/dV$ shifts.

This supports **conversion-associated** wording but does not identify a unique microscopic conversion step.

The previous amplitude–FWHM-like-width map is moved to the SI together with the 105-condition background/window sensitivity audit. These secondary descriptors are not kinetic rates. Figure 5(c) retains the one-to-one comparison but should display the GITT peak-location sensitivity ranges.

Current $dQ/dV$ values are reconstructed from the latest vector voltage-profile figures. The GITT side is raw-data based; recover the original numerical first-cycle voltage profiles if possible before submission, otherwise retain the documented vector-reconstruction provenance and smoothing-sensitivity checks.

### Figure 6 — history dependence

Final main-panel architecture:
- (a) $z_{\mathrm{peak}}$ versus cycle;
- (b) excess peak amplitude versus cycle;
- (c) median $t_{63}$ versus cycle;
- (d) $A_3/A_1$ versus $t_{63,3}/t_{63,1}$ change map.

Full cycle-resolved excess profiles remain in the SI to avoid repeating the curve-level presentation of Figure 5.

Cycle-resolved GITT shows:
- the late first-cycle peak shifts toward a common earlier normalized reaction-state region in cycles 2–3;
- conversion-associated response magnitude evolves strongly;
- $t_{63}$ changes more modestly;
- BM higher-accessibility/longer-$t_{63}$ relation persists beyond the first cycle.

Role: robustness/history constraint, not a separate headline.

### Figure 7 — microkinetic existence proof

Final main-panel architecture:
- (a) effective $O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C$ network;
- (b) schematic current-off balance showing that $j_{\rm ext}=0$ can coexist with finite opposing partial currents and finite R2;
- (c) homogeneous global-rate control on $Q_{\rm cutoff}$ versus matched-state $t_{63}$;
- (d) heterogeneous-accessibility existence proof on the **same axes**, with the homogeneous trajectory retained as a dashed reference.

R1/R3 are Faradaic; R2 is a coarse-grained structural/reconstruction coordinate.

Homogeneous global speed scaling recovers:
- faster → cutoff capacity ↑
- faster → $t_{63}$ ↓

Illustrative heterogeneous accessibility gives:
- cutoff capacity 0.55845 → 0.65714 (+17.67%)
- $t_{63}$ 13.45 → 15.28 min (+13.63%)

Main artwork deliberately avoids “BM-like,” population weights, and the illustrative R2 ratio so the calculation is not presented as a material-specific fit. Those parameters remain in the SI/model audit.

Separate Mg-like SI test gives:
- $Q_{\rm cutoff}$ 0.55845 → 0.39339
- relaxation amplitude 33.02 → 28.64 mV
- $t_{63}$ 13.78 → 16.78 min

All model calculations are existence proofs, not material-specific fits.

Important: a local Figure 7 draft was previously generated, but the Figure 7 plotting code was **not** committed at that time. Do not claim that it is already in the repo unless it is explicitly added later.

## Figure 4 Word integration

A tracked Word manuscript was generated in the 2026-09-27 chat with Figure 4 inserted after Section 2.3 and caption/text references updated.

Latest conversation artifact name:
`HEO_Fig4_Integrated_Tracked.docx`

The Word binary is not the repository authority. In a new session, use Main v13 + Figure-4 logic note to regenerate the Word file if the conversation artifact is unavailable.

## Mg composition recovered

Historical ICP data were recovered from:
`241010_HEO for battery_유태경 (2).pptx`

Ni-normalized HEO3-set ratios:

- HEO3: Ni 1, Co 1.02, Mn 1.03, Fe 1.00, Cr 1.27
- BM-HEO3: Ni 1, Co 1.01, Mn 1.07, Fe 1.00, Cr 1.02
- Mg-HEO3: Ni 1, Co 1.01, Mn 1.01, Fe 0.990, Cr 0.994, Mg 1.10
- BM-Mg-HEO3: Ni 1, Co 1.00, Mn 1.02, Fe 1.01, Cr 1.01, Mg 1.07

Thus Mg-HEO3 is not obviously a trace-doped material; Mg is approximately equimolar with the other principal cations in this historical ICP dataset.

Still unresolved:
- Mg precursor identity
- exact nominal Mg ratio
- whether the synthesis is formally addition/substitution
- collaborator-verified final composition/formula

## HEO/Mg conventional apparent-D exploratory check

A preliminary cross-composition check was performed after recovering the Mg composition.

Development result:
- median $D_{\mathrm{app,Mg}}/D_{\mathrm{app,HEO}}\approx13.36$
- ratio >1 at 36/37 matched states
- median $t_{63,\mathrm{HEO}}/t_{63,\mathrm{Mg}}\approx0.772$
- direct rate ratio <1 at 36/37 states
- nominal-equimolar composition treatment gave a similar median apparent-$D$ ratio (~13.27)

Interpretation:
conventional apparent $D$ also points toward faster Mg-HEO while direct relaxation is slower.

Decision:
**do not add this to main Figure 4(b).** HEO/Mg is cross-composition and requires frozen composition/density/molar-volume/active-mass prefactors. Keep as SI robustness candidate only.

Audit:
`modeling/HEO_MG_CROSS_COMPOSITION_GITT_CHECK_2026-09-27.md`

## Terminology / claim boundaries

Preferred:
- accessible conversion capacity
- relaxation voltage change / relaxation magnitude
- $t_{63}$ = model-free effective relaxation timescale
- conversion-associated kinetics only after independent conversion localization
- conflicting apparent-diffusivity indication/trend

Avoid:
- calling relaxation magnitude itself a rate
- calling Mg a second capacity–kinetics contradiction
- “small Mg substitution” until synthesis/composition is frozen
- saying apparent $D$ “proves” faster kinetics
- saying GITT is invalid
- saying diffusion is absent
- identifying one unique rate-determining step
- equating $t_{63}$ with a microscopic forward rate constant

## EIS decision

Cycling EIS is excluded from the manuscript evidence chain because of state matching, outliers, and process overlap. Do not reinsert it unless new, cleaner evidence creates a specific need.

## Remaining MUST-FIX submission inputs

1. Figures 1–2 final collaborator structural/compositional package and text.
2. Mg synthesis details and final nominal/ICP composition.
3. Cell/electrode metadata:
   - current collector
   - drying temperature/time
   - active loading
   - final thickness
   - separator model
   - electrolyte volume
   - glovebox H2O/O2
   - 1 C capacity basis
   - exact rate sequence / cycles per rate
4. Original numerical first-cycle voltage profiles for final $dQ/dV$, if recoverable.
5. Exact active masses / molar-volume metadata only if absolute $D$ or HEO/Mg cross-composition $D$ is promoted. Absolute $D$ is not required for the current main claim.

## Immediate next work

The revised AFM-length abstract and Figures 3–7 scientific logic are sufficiently closed for the present round.

Next priority:
1. continue PI line-by-line review using Main v15; Sections 2.2–2.5 and the Conclusions now reflect the current four-step homogeneous microkinetic interpretation;
2. propagate only evidence-supported changes across Abstract/Introduction/Results/Conclusion rather than rewriting mechanically;
3. complete/freeze Figures 1–2 with Yoo-group input;
4. recover/freeze Figure 3 raw numerical sources and remaining methods metadata / original $dQ/dV$ numerical source;
5. regenerate the full tracked Word manuscript after line-by-line text review and collaborator inputs.

Do not reintroduce the discarded heterogeneous-population microkinetic model unless new evidence requires it. Do not reopen the central BM/Mg story or the Figure 4 architecture unless new data require it.


## 2026-09-28 late-session reference update

- Main manuscript authority advanced to v16.
- Main references were pruned to cited literature and renumbered in first-citation order.
- Main reference count is 24.
- General GITT-assumption/pitfall support was added using methodological literature already present in the verified project reference pool.
- Ng et al. is the direct four-step metal-oxide conversion mechanism precedent; Alsaç et al. is the broader conversion reaction-network precedent; Li et al. (JACS 2016) bounds interpretation of the full relaxation-voltage magnitude.
- Uncited literature was not deleted from the project and remains available in the reference master/audit files.
