# HEO manuscript logic audit: R1 milling fingerprint and Mg-associated late kinetic contrast (2026-11-05)

**Status:** Analytical review and **proposed** manuscript edits, not a PI-approved wording rewrite or boundary update. Do NOT modify locked Abstract v12 or data figures until explicit PI approval.

## Data provenance
Original four first-lithiation XLSX files obtained via collaborator's Sept 17 Gmail/linked Google Drive. Raw pulse descriptors and verified Figure 4 are documented at `modeling/HEO_FOUR_SAMPLE_RAW_GITT_KINETIC_BOUNDARY_CHECK_2026-11-05.md`. Proposed (L1/L3/L4) after-pulse indices: HEO 6/25/55, BM-HEO 9/38/60, Mg-HEO 7/24/39, BM-Mg-HEO 9/35/40. Only the four full pulse counts 65/76/48/56 are confirmed as source facts; landmark positions remain operational selections.

## New two-by-two observations

### Early R1: milling strongly alters entire first-lithiation t63 trajectory
- HEO first GITT pulse t63=16.90 min, dropping to 9.98 min at pulse 6.
- BM-HEO starts 4.94 min, rises to 10.05 min at pulse 7 and exhibits modest early local min ~9.77 min at pulse 9.
- Mg-HEO starts 18.51 min, falls to 12.29 min at pulse 7.
- BM-Mg-HEO starts 4.46 min, rises to 14.16 min at pulse 5 then falls to ~12.95 at pulse 9 before rising again.
- Hence the **beginning of the R1 trajectory** differs strongly between milled/unmilled independent of Mg status. This is an observation of operational normalized voltage recovery t63, not direct proof of faster/slower intrinsic solid diffusion or a specific microscopic reaction step.
- **IMPORTANT cross-state caveat:** after *first* pulse QOCV is ~1.505 V (HEO), 2.488 V (BM), 1.602 V (Mg), 2.408 V (BM-Mg). Therefore equal pulse indices do NOT sample matched potential/reaction state in R1. Even when interpolating t63 at the same QOCV (e.g. ~1.45 V and ~0.90 V), the trajectories are not identical: HEO ~16.18→10.44 min; BM ~9.85→11.47; Mg ~17.46→12.32; BM-Mg ~13.52→13.20. Last BM-Mg pair illustrates that full-R1 “sign reversal” is strongest at the initially high voltages, so the manuscript must not claim universal BM-induced acceleration over a matched-potential R1 interval.
- Better inference: milling changes initial voltage-recovery trajectory/participation of accessible surface and conversion-onset environments; structural origin is a plausible hypothesis given BET increase, not directly proven. Avoid language of rate acceleration.

### Later R3/R4: Mg attenuates late t63 maximum and downturn
- HEO reaches t63 ~14.734 min at pulse 55, decreases to ~13.70 at pulse 60 before rising again at terminal pulses.
- BM-HEO reaches t63 ~16.127 at pulse 59, decreases to ~14.286 at pulse 67 then rises again.
- Mg-HEO continues rising ~11.98 at pulse 39 to ~14.06 at pulse 48.
- BM-Mg-HEO continues rising ~12.44 at pulse 40 to ~15.90 at pulse 56.
- Same late-direction contrast remains at **similar QOCV**: between 0.45 and 0.30 V, HEO t63 ~14.73→13.69; BM ~15.77→14.29; Mg ~10.76→12.62; BM-Mg ~12.46→13.46.
- Source-backed conclusion: a resolved late t63 turning point accompanies the Mg-free pair; the Mg-containing pair exhibits a gradual/continuously increasing terminal t63. Only Mg-containing L4 uses a quasi-open-circuit-voltage slope-break rather than a definite late t63 maximum.
- Candidate physical hypotheses: fewer reducible TM centers, stabilization/persistence of Mg-containing oxide environments, redistribution/overlap of later reduction processes, or a different voltage–composition response. The data do **not** identify an Mg-rich residual oxide phase or prove that a chemically distinct R4 disappears.

## Capacity consequence under proposed kinetic landmarks (NOT yet incorporated)
- Nominal regional charges (R1/R2/R3/R4, mAh/g):
  - HEO 100/316.7/500/166.7
  - BM 150/483.3/366.7/266.7
  - Mg 116.7/283.3/250/150
  - BM-Mg 150/433.3/83.3/266.7
- R3 widths decrease under Mg: HEO 30→Mg 15 pulses, BM 22→BM-Mg 5 pulses. R4 *absolute* charge does **not** compensate (HEO 166.7 vs Mg 150; BM 266.7 vs BM-Mg 266.7).
- BM positive R2: +166.7/+150; BM negative R3: −133.3/−166.7; Mg negative R3: −250/−283.3. Directional signs survive independent ±1-pulse shifts of respective segment borders, but R3 BM-Mg length (5 pulses) is relatively sensitive to precise L3/L4.
- v12 locked abstract's original numerical ranges for BM-associated R3 loss and Mg-associated R3 loss **would no longer match** the proposed assignments. Hold abstract and Figure 5 until PI approves a coherent update across main/SI, then update all simultaneously.

## Manuscript-specific revision map

- Introduction P3/P4 (PI-approved): core kinetic-first motivation **holds**. Leave unchanged. Do not claim 4 isolated kinetic phases.
- §2.3: current text describes pristine only and sends other 3 to SI; now four-sample Figure 4 should be considered. Explicitly state L1/L3 selected from early and middle t63 local minima **after recognizing initial transient**, while L4 uses late t63 decline or QOCV knee when late t63 downturn is not resolved; ΔErest retained as auxiliary signal, not mandatory segmentation channel. Avoid “the same extrema coincide across all 4”.
- Figure 4 caption: describe four materials and indicate distinct L4 provenance; show color/line style for L4 from QOCV vs t63. Make potential-width mismatch visible; axes normalized by each sample's total GITT first-lithiation charge.
- §2.4: if region cuts approved, correct every number. Current §2.4 claims “R1 and R4 remain unchanged under Mg,” which is **false** under candidates: Mg–HEO vs HEO: R1 +16.7 and R4 −16.7; BM vs BM-Mg R1/R4 unchanged.
- §2.5: replace “milling shortens t63 during early R1” with actual **shape change**; distinguish early full trajectory from matched potential windows. New observation of absent late Mg t63 downturn strengthens composition-sensitive electrochemical-response claim without assigning atomistic reaction.
- §2.6 and Conclusions: add one cohesive sentence that magnitude of region charge and kinetic fingerprint each encode different response dimensions. Capacity redistribution and attenuation of late t63 turning occur together under Mg but remain distinct observables.
- Figure 5 and Tables S1–S3; Figure 6: numerical/diagrammatic boundary remapping required only after approval.
- Abstract v12 remains PI locked until explicit revision instruction; if new boundary set is approved, changes are necessary to ensure self-consistent reported numeric ranges.

## Recommended revised scientific spine
Material change (morphology/cation chemistry) → electrochemical performance → all-four GITT state-dependent relaxation fingerprints → operational region partition with two physically meaningful contrasts (R1 milling vs late Mg) → signed regional-charge accounting → literature-grounded hypotheses and actionable materials-design insights.

**Important epistemic limit:** A finite-window t63 reflects the composite relaxation response and can change with potential/state, reaction pathways, and transport; it is not direct evidence of individual elementary rate constants. QOCV is a 60 min rest-end voltage, not proof of thermodynamic OCV. Kinetic-region assignments are observational and nonunique when late t63 has no downturn.
