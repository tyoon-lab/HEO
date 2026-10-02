# HEO Project

## Start here

This repository is maintained so a new chat/session can resume **without a separate handoff message**.

Read first:

`START_HERE_CURRENT_STATE_2026-10-03.md`

That file is the single authoritative current-state entry point.

## Current paper identity

Working title:

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Working target: **Advanced Functional Materials (AFM)**.

## Current scientific chain

Figure 1–2: materials structure/composition/morphology  
→ Figure 3: accessible conversion capacity  
→ Figure 4: BM capacity-up / slower-relaxation mismatch + conventional Dapp conflict + Mg magnitude/timescale constraint  
→ Figure 5: localization of the relaxation anomaly to the conversion region  
→ Figure 6: **multistep model under active reassessment; existence/consistency test only**

## Critical 2026-10-03 Figure 6 update

Before editing Figure 6 or Section 2.5, read:

`manuscript/HEO_FIGURE6_REASSESSMENT_LOCK_2026-10-03.md`

New checks show:

- raw first-lithiation GITT pulse excursions do **not** grow near the 0.005 V cutoff; they decrease in all four samples;
- therefore experimental capacity should not be explained by a progressively growing terminal polarization;
- near the reference model state, Q and t63 sensitivities are almost scalar-like (cosine similarity ~0.993), so do not claim that the observables locally probe different elementary steps;
- the Q-up / t63-up regime remains possible under **finite step-selective perturbations**;
- the qualitative Q-up result survives when the modeled conversion voltage is placed far above the experimental cutoff;
- in that realistic-headroom limit, the useful model interpretation is different progression through the multistep conversion sequence / accessible conversion extent, not a near-cutoff polarization artifact;
- there is no experimental basis to assign ball milling uniquely to R2 slowing and R3 acceleration.

## Current manuscript authorities

- `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`
- `manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`
- `manuscript/HEO_MAIN_SI_CROSSREF_AUDIT_2026-09-30.md`

Main v17 and SI v14 remain the text authorities. Do not rewrite them until the final Figure 6 interpretation is frozen.

## Key new audit files

- `manuscript/HEO_FIGURE6_REASSESSMENT_LOCK_2026-10-03.md`
- `modeling/HEO_TERMINAL_POLARIZATION_AUDIT_2026-10-03.md`
- `modeling/HEO_TERMINAL_POLARIZATION_SUMMARY_2026-10-03.csv`
- `modeling/HEO_FOUR_STEP_LOCAL_SENSITIVITY_2026-10-03.csv`
- `modeling/HEO_FOUR_STEP_OPERATING_POLARIZATION_AUDIT_2026-10-01.md`
- `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.md`
- `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.csv`

## Current locked experimental message

- BM-HEO has higher accessible capacity than pristine HEO.
- BM-HEO has a longer directly measured post-interruption relaxation time, t63.
- Conventional GITT-derived Dapp ranks BM-HEO in the opposite fast/slow direction.
- The anomalous relaxation is localized to the conversion region.
- Mg incorporation lowers accessible capacity and relaxation magnitude while leaving t63 nearly unchanged.

## Current model boundary

Safe:

**A minimal multistep conversion network can reproduce higher accessible charge together with slower post-interruption relaxation under finite step-selective changes, and this qualitative ordering survives a realistic voltage-headroom test.**

Not safe:

- ball milling specifically slows R2 and accelerates R3;
- the model quantitatively fits BM-HEO;
- terminal polarization growth explains the experimental capacity;
- different observables always probe different elementary rates;
- a unique HEO rate-determining step has been identified.

## Immediate next task

Start with Figure 6 physics, not prose:

1. choose whether the main modeled accessibility coordinate remains normalized passed charge Q or is augmented/replaced by final converted-state fraction C;
2. decide whether the voltage-headroom robustness belongs in Main Figure 6 or SI;
3. freeze the minimum model claim;
4. only then update Section 2.5, Figure 6 caption, Abstract, Conclusion, and corresponding SI text.

Do not restart from older manuscript/model states unless auditing history.
