# HEO SI v11 Build Plan — 2026-09-29

## Goal

Rebuild the Supporting Information so that all currently available electrochemical figures/tables are populated rather than left as empty placeholders, while keeping collaborator-dependent structural characterization placeholders explicit.

Final deliverable: a fully assembled Word SI after all batches are complete.

## Build sequence

### Batch 1 — electrochemical performance/control figures
Populate and caption the currently available electrochemical material:
- Figure S7: cycling comparison with and without 10 wt% FEC.
- Figure S8: rate capability and normalized retention/recovery.
- Figure S9: first-three-cycle voltage profiles for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO.
- Figure S10: cycle-resolved dQ/dV evolution for all four materials.
- Figure S11: non-faradaic-window CV / interfacial-capacitance comparison.
- Figure S12: pristine versus 100-cycle SEM comparison for HEO and BM-HEO.
- Figure S13: full multi-cycle GITT traces for Mg-free and Mg-containing pairs.

Primary source for S7–S13: `HEO 진행상황 (20260917).pptx`.
The GITT condition is confirmed as 10 min current pulse + 60 min open-circuit rest.

Current electrochemical raw files recovered:
- `HEO GITT 로우 데이터.xlsx`
- `BM HEO 3 GITT 로우 데이터.xlsx`
- `HEO 3 Mg 로우 데이터.xlsx`
- `BM HEO 3 Mg 로우 데이터.xlsx`

### Batch 2 — GITT/current-off and conventional-D audit
Populate:
- representative early current-off E–sqrt(t) fits;
- full first-lithiation GITT traces;
- t50/t63/t90 versus state;
- state-matched HEO/BM Dapp-ratio audit;
- voltage-term decomposition/sensitivity tables;
- current-off descriptor tables.

Use the verified project CSVs and raw GITT files rather than empty placeholders.

### Batch 3 — conversion-associated excess and cycle-history robustness
Populate:
- first-cycle background/excess fits;
- 105-condition background/window sensitivity;
- dQ/dV–GITT voltage-localization comparison;
- cycle-resolved relaxation/history analysis moved from the former main Section 2.5;
- corresponding descriptor tables.

### Batch 4 — four-step homogeneous microkinetic SI
Replace the obsolete three-step / heterogeneous-accessibility model in SI v10 with the current homogeneous four-step sequence:
- R1 initial lithiation/electron transfer;
- R2 effective M–O dissociation/local reconstruction;
- R3 effective Li2O-forming/product-side reconstruction;
- R4 subsequent electron transfer/metal reduction.

Include:
- equations and representative parameters;
- R1–R4 single-step limiting audit;
- R2–R3 two-dimensional regime map;
- current-off eigenmode analysis;
- interpretation boundaries;
- Mg as a qualitative complementary experimental constraint, not a parameter fit.

Do not include the former heterogeneous-population existence proof as current manuscript evidence.

### Batch 5 — assemble and QA final SI Word
- Integrate all figures and tables.
- Keep collaborator-dependent structural items S1–S5 explicit if still unavailable.
- Harmonize captions and cross-references with main v16.
- Render every page and visually inspect before delivery.

## Current boundaries

- Do not infer missing Yoo-group XRD refinement, HRTEM/SAED indexing, final XPS fitting, or final Mg synthesis/composition metadata.
- Electrochemical figures may be populated from the latest project/progress material and verified derived analyses.
- The full experimental relaxation magnitude is not a quantitative target of the conversion microkinetic model.
- Heterogeneous-population fitting is excluded from the current main/SI interpretation.
