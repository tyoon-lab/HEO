# HEO v26 — Main/SI evidence-aligned PI review and remaining gates (2026-10-15)

## Read-first manuscript authority
- **Full Main text:** [HEO_MANUSCRIPT_V26_EVIDENCE_ALIGNED_2026-10-15.md](HEO_MANUSCRIPT_V26_EVIDENCE_ALIGNED_2026-10-15.md). Text faithfully mirrored from rendered v26 Word; the six embedded figures remain in Word/older Drive sources, not in GitHub Markdown.
- **Main Word reviewer artifact:** `HEO_Manuscript_V26_EvidenceAligned_PIReview_2026-10-15.docx` (generated conversation artifact, NOT a GitHub binary). Source `HEO_Manuscript_V25_DominantStageMechanism_2026-10-15.docx`.
- **Supporting Information reviewer artifact:** `HEO_SI_V17_SourceEvidenceReview_2026-10-15.docx` (generated conversation artifact, NOT a GitHub binary); source `HEO_SI_V16_RawVerified_Focused_Review_2026-10-12.docx`.
- **Source Figure 1–2 audit:** [HEO_V26_FIGURE1_2_STRUCTURE_EVIDENCE_GATE_2026-10-15.md](HEO_V26_FIGURE1_2_STRUCTURE_EVIDENCE_GATE_2026-10-15.md).
- Previous [v25 Main](HEO_MANUSCRIPT_V25_STAGE_MECHANISM_INTEGRATED_2026-10-15.md), v24 Word, and earlier findings preserved. **Do not assume a main 2026-10-15 Word published on Drive is v26 just because the name is similar; use the exact v26 filename.**

## Verified changes introduced in v26
1. **§2.1 source-grounded characterization** from collaborator's Figure 2 printed BET values (m² g−1): HEO **3.94**, BM-HEO **18.159**, Mg-HEO **6.49**, BM-Mg-HEO **16.64**. BM increases BET in both matched materials. The Mg-free vs Mg comparison has **larger** BET but **less** R3 charge after Mg: surface-area shortage alone fails as a complete explanation. Figure 2 is an adsorption-uptake curve with annotated BET values, **not** a displayed BET linear-regression fit; raw BET analyses unverified.
2. **§2.1 + Figure 1 caption** explicitly flag the unresolved source **CoGa₂O₄ reflection indexing**. No Ga precursor in collaborator Ni/Fe/Co/Mn/Cr Mg-free recipe; these labels already appear in 2026-09-17 collaborator presentation. No speculative replacement phase index or Mg lattice occupancy.
3. **§2.4 BM physical discussion** now cites quantitative matched-pair BET area and proposes greater oxide-domain participation/interfacial access in R2, without claiming independently proven primary particle size refinement, new defects or specific reconstruction product. Electrode BSE aggregation sizes from 2026-09 source deck are ~1.95 μm HEO, ~2.12 μm BM-HEO, ~1.93 μm Mg-HEO, ~1.99 μm BM-Mg-HEO; they **do not** show smaller electrode aggregates after milling.
4. **§2.5 Mg physical discussion** explicitly uses Mg 6.49 vs 3.94 m²/g contradiction to a simple BET-area reduction explanation; proposes redox-active inventory / later conversion accessibility / local energetics as **alternative testable hypotheses**. Mg composition, substitution site, M–O bond stabilization, Li₂O yield unverified.
5. **§2.6 and Conclusion** reconcile structural and electrical evidence while preserving the first-lithiation nominal GITT regional contrasts and non-equivalence of t63 and charge:
   - BM−HEO ΔR2 +166.7 mAh g−1 (largest positive signed),
   - BM-Mg−Mg ΔR2 +133.3,
   - Mg−HEO ΔR3 −266.7 (largest negative signed),
   - BM-Mg−BM ΔR3 −283.3.
   Counts 65/76/48/56 for complete first-lithiation 600s GITT pulses. These are **nominal GITT protocol** contrasts, not GCD.
6. **Experimental Section** now documents that BET values come from a displayed collaborator figure, not an independently rerun fitting/regression. Neither ΔE_rest nor t63 is asserted to identify a unique chemical species.
7. **SI v17** expands S1 with Figure2-source numeric evidence, Figure1 indexing warning and updated requested records, while retaining 3 numeric GITT tables, 3 electrochemical SI figures and the historical boundary sensitivity caveat.

## Reproduction / rendering QA
- Rendered Main v26 via DOCX skill: **13 pages**, 6 embedded Main figures, no document tables, 20 existing numbered reference entries. Pages visually contact-sheet reviewed for text flow, captions, symbol rendering; no new overlapping figures observed. Figure1 *source artwork's old HRTEM labels remain unresolved* as a scientific QA issue, not a layout defect.
- Rendered SI v17: **4 pages**, 3 tables, 3 images; captions remain near their associated images.
- The Main PDF/render directory and SI PDF/render directory are session QA artifacts only, not publication outputs.
- **Abstract:** v26 Word still contains the historical v24 Abstract as a *clearly labeled PI-review placeholder*, unchanged, with superseded “Yet” etc. The latest PI line-by-line edits and new conversion–reconversion opening are not yet publication-locked; do not call the historical abstract final or silently promote an assistant-generated new draft.

## External references: independently checked source/claim roles (partial bibliographic audit)
- [4] Zhai et al., 2024, *J. Power Sources* 603, 234418, DOI 10.1016/j.jpowsour.2024.234418: closely related (FeCoNiCrMn)₃O₄, particle fragmentation/reversibility/interfacial capacity. **Not** direct proof that this exact BM specimen has smaller primary grains.
- [7] Luo et al., 2022, *Adv. Sci.* 9, 2201219, DOI 10.1002/advs.202201219: operando XAS of a **Co-free** spinel HEO; shows element-dependent two-step reduction/reoxidation; do not transpose the exact Co-free transition-metal sequence to the present Co-containing material.
- [8] Jin et al., 2025, *Mater. Today Chem.* 48, 102949, DOI 10.1016/j.mtchem.2025.102949: closely related five-cation spinel `(FeCoCrNiMn)₃O₄`, reported spinel → mixed spinel/rock-salt → rock-salt transformation. This corroborates stage-based reconstruction *as literature*, not direct identification of the present R2/R3 endpoints.
- [9] Li et al., 2025, *Angew. Chem. Int. Ed.* 64, e202518569, DOI 10.1002/anie.202518569: intermediate-phase evolution, size-dependent diffusion-path effects; not a measured phase map of the present samples.
- [14] Horner et al., 2021, *ACS Appl. Energy Mater.* 4, 11460–11469, DOI 10.1021/acsaem.1c02218: GITT assumptions and model dependence, especially transport and active surface. Intercalation-focused; do not treat as direct proof of microscopic HEO conversion assignments.
- [16] Jorkesh et al., 2026, *J. Power Sources* 682, 240338, DOI 10.1016/j.jpowsour.2026.240338: SOC-dependent voltage relaxation in NMC811 cells; general finite-rest caveat, **not HEO-specific stage evidence**.
- [17] Chen et al., 2020, *RSC Adv.* 10, 9736–9744, DOI 10.1039/D0RA00255K: Mg/Ti/Zn/Cu/Fe spinel HEO, **not** the current Mg-substituted Ni/Fe/Co/Mn/Cr family; cite only as composition comparator.
- [2] Wang et al., 2020, *J. Alloys Compd.* 844, 156158, DOI 10.1016/j.jallcom.2020.156158: baseline closely related five-transition-metal spinel composition.
- Other reference entries **still need full publisher metadata and claim-to-citation checks**; this list is not a blanket all-20 verification.

## Main scientific open issues (cannot honestly close with present sources)
1. **Immediate:** resolve Figure1 `CoGa₂O₄` source indexing (reference vs wrong assignment), actual phase identity using matching parent/Mg sample XRD/SAED/HRTEM and correct label, provide original crystallographic standard/index card. Do not claim CoGa₂O₄ exists without actual Ga analysis.
2. Final independent N₂ adsorption/BET fits and sample IDs (including number of measurement replicates/uncertainty), BET temperatures/degas/preparation if required by journal.
3. Exact Mg-HEO/BM-Mg synthesis, measured actual Mg fraction/ICP/EDS, possible lattice incorporation, phase content, anomalous ~579 eV Cr6+ XPS in recent batch: use valid final fit before XPS claims.
4. Full electrode active/binder/additive ratios, loading, electrode dimensions/current collector, cell/separator/electrolyte, C-rate basis, GITT full cycle sequence and replicates.
5. Historic original L1/L3/L4 landmark choices still reconstructed from rounded pulse tables; confirm source markers and robustness; do not invent phase boundaries. The 3-cycle GITT source contains later cycles but only first-lithiation region partitions are established.
6. Freeze PI-approved abstract; finish all-20 bibliographic check; cross-verify manuscript Figure1–6 specimen labels, captions and SI and final AFM submission style. Avoid using preliminary ECSA (4.18/30.17/6.56/39.68 cm²) from September deck without original nonfaradaic slope and specific capacitance-unit calibration.

## Specific concise collaborator requests
- Confirm CoGa₂O₄ HRTEM indexing/phase-standard reference, provide original annotated d-spacing/FFT/SAED/XRD files, specify phase identification for **all four** samples.
- Supply raw N₂ adsorption/desorption + selected BET linear fitting ranges for all four and actual sample mass, degassing, uncertainties.
- Supply Mg salt identity and stoichiometry, measured ICP ratios and matching XRD/EDS maps and final Cr XPS spectra with batch labels.
- Supply full electrochemical cell recipe and cell replicates and exported GITT original L1/L3/L4 event annotation.
- If original response of 2nd/3rd cycles is to enter Main, specify the actual cycle-indexed data and a consistent comparison basis; otherwise keep multicycle GITT as SI context.

## Handoff
Use v26 Main full-text and this QA note as active **BODY review**; preserve prior original accepted regional charge partition and avoid EKF spectral plots from the separate GITT manuscript. Final artifact is a **PI-review proof, not AFM submission-ready**. The user's PI-edited Abstract remains the next unresolved editorial decision, with the requested removal of rhetorical “Yet”, avoidable “not”, and “Together” already recorded.
