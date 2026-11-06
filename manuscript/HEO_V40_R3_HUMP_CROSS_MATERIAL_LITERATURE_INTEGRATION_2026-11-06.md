# HEO v40 — R3 hump cross-material literature integrated into main manuscript and SI (2026-11-06)

**PI decision:** Apply the 2026-11-06 literature survey of GITT recovery amplitude / relaxation in conversion and phase-changing electrodes to current HEO manuscript. Preserve the scientific hierarchy: **region-resolved nominal GITT charge is the primary explanation of capacity changes; R3 hump is a secondary relaxation descriptor**.

## Deliverables (conversation artifact files, not committed binaries)

- `HEO_Manuscript_v40_R3_Hump_Literature_2026-11-06.docx` — 14 pages, renders cleanly, all Word comments absent.
- `HEO_SI_v21_R3_CrossMaterial_Literature_2026-11-06.docx` — 10 pages, section S7 and new **Table S6**, renders cleanly, no comments.

## Main manuscript change

Only the §2.5 paragraph beginning “The R3 recovery-amplitude hump ...” was rewritten; existing Figure 4/5, absolute/signed regional charge comparisons, Figure 3 axes, Methods, 60-min GITT protocol and **Abstract** are unchanged.

The revised 180-word paragraph:

> The R3 recovery-amplitude hump in pristine HEO is dominated by increased recovery between 10 and 60 min (Figure S4), suggesting that delayed re-equilibration becomes more prominent during continued conversion. The distribution of nonequilibrium reaction states offers one physical explanation. In FeF₃, GITT voltage recovery varies with the spatial distribution of intermediate phases [28], and comparison of alternative phase-transition pathways separates rest-recoverable voltage changes from persistent hysteresis [30]. Phase coexistence and slow structural transformation in Fe₃O₄ provide related conversion-oxide precedents [22,29]. Diffraction measurements during rest further show Li redistribution in SiO–graphite composites and structural rearrangement in graphite and LiFePO₄ [31,32]. These observations support a possible contribution from heterogeneous reduction and structural reorganization in HEO R3; milling and Mg incorporation may change the population of states that contribute to delayed recovery. Variations in the QOCV–charge slope and internal Li redistribution can also influence the measured amplitude; the common-QOCV comparison (Table S5) indicates that slope variation alone provides an incomplete explanation of the pristine-versus-milled contrast. The hump therefore supplies a secondary relaxation signature alongside region-resolved charge, the primary quantitative descriptor of capacity changes.

## New full references
30. Jo, H.; Gong, M.; Kim, S. Y.; Seo, D.-H.; Jung, S.-K. Guided phase transition for mitigating voltage hysteresis of iron fluoride positive electrodes in lithium-ion batteries. Nat. Commun. 2025, 16, 8596. https://doi.org/10.1038/s41467-025-63676-9
31. Fu, J.; Takai, S.; Yabutsuka, T.; Yao, T. Relaxation Analysis of Silicon Monoxide-Graphite Composite Anode. JES 2024, 171, 020557. https://doi.org/10.1149/1945-7111/ad2956
32. Skurtveit, A.; North, E. T.; Park, H.; Chernyshov, D.; Wragg, D. S.; Koposov, A. Y. Stepwise Structural Relaxation in Battery Active Materials. ACS Mater. Lett. 2025, 7, 343–349. https://doi.org/10.1021/acsmaterialslett.4c02058

Literature facts checked against publisher abstracts/full-text where available.

## SI v21 change
- Added **S7, “Cross-material evidence for delayed voltage recovery during conversion and phase transformation”**.
- **Table S6** compares FeF₃ (Li 2016 and Jo 2025), SiO–graphite (Fu 2024), graphite/LiFePO₄ (Skurtveit 2025), and Si chemo-mechanical relaxation (Köbbing et al., ACS AMI 2024, https://doi.org/10.1021/acsami.4c12976).
- Explicitly separates **a statewise peak in finite-window ΔErest(Q)** from a hump within one rest, a bump on renewed cycling, or persistent charge–discharge hysteresis.
- Includes source DOIs and interpretive limits. All original S1–S6, Tables S1–S5 and Figures S1–S6 retained unchanged.
- Section S7 starts on a new page for readability; page 10 contains the entire comparison and conclusion.

## Non-changing raw GITT facts (still the accepted basis)
- Pristine HEO R3 pulse 26→50 ΔErest 145.1→189.3 mV (+44.2 mV). Increments: 3–60 s −9.8 mV; 1–10 min +16.5 mV; 10–60 min +37.5 mV.
- Mg-HEO weak interior hump, milled samples no pronounced interior R3 hump.
- L1/L3/L4 after-pulse `6/25/55`, `9/38/60`, `7/24/42`, `9/35/46`.
- GITT region charges and abstract values not amended; no phase identity assigned from voltage alone.

## Remaining scientific qualifications
FeF₃ provides the most direct across-state voltage-recovery precedent, while SiO/graphite and graphite/LFP directly show structural reorganization after interrupting current. Si mechanical relaxation and QOCV-slope differences remain competing influences, not unique HEO phase assignments. Main-text kinetics remain secondary to capacity allocation.

## QA
- Main 14 pages; SI 10 pages from canonical DOCX renderer.
- Abstract and all non-target main paragraphs explicitly compared byte-wise to previous v39, unchanged; only §2.5 paragraph and 3 new refs.
- DOCX ZIP integrity tested; comments.xml absent in both.
