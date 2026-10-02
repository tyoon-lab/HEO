# HEO — Current State, 2026-10-03

## Read this first

This is the authoritative restart point for the HEO manuscript.

A new chat/session should be able to resume from this file alone without a separate handoff.

The key update since 2026-09-30 is a **reassessment of Figure 6 and the physical meaning of the modeled capacity**. The experimental manuscript is not being rewritten yet. Main v17 and SI v14 remain the text authorities until Figure 6 is re-frozen.

---

## Paper identity

Working title:

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

Working target: **Advanced Functional Materials (AFM)**.

The paper is a materials/conversion paper using GITT relaxation as the kinetic diagnostic. It is not intended as a general GITT-method paper.

---

## Current authority order

### Manuscript / SI

1. Main manuscript:
   `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`
2. SI authority:
   `manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`
3. Main/SI cross-reference audit:
   `manuscript/HEO_MAIN_SI_CROSSREF_AUDIT_2026-09-30.md`
4. Main reference audit:
   `manuscript/HEO_REFERENCE_AUDIT_MAIN_V16_2026-09-28.md`

### Figure 6 / model reassessment

5. **Read next before touching Figure 6:**
   `manuscript/HEO_FIGURE6_REASSESSMENT_LOCK_2026-10-03.md`
6. Original four-step model authority:
   `modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`
7. Operating-polarization exploratory audit:
   `modeling/HEO_FOUR_STEP_OPERATING_POLARIZATION_AUDIT_2026-10-01.md`
8. Local kinetic sensitivity:
   `modeling/HEO_FOUR_STEP_LOCAL_SENSITIVITY_2026-10-03.csv`
9. Realistic voltage-headroom audit:
   `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.md`
   `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.csv`
10. Raw GITT terminal-polarization audit:
   `modeling/HEO_TERMINAL_POLARIZATION_AUDIT_2026-10-03.md`
   `modeling/HEO_TERMINAL_POLARIZATION_SUMMARY_2026-10-03.csv`

### Other current model/data authorities

11. Revised Mg four-step audit:
   `modeling/HEO_MG_REVISED_WINDOW_FOUR_STEP_TEST_2026-09-30.md`
12. Mg thermodynamic trajectory:
   `modeling/HEO_MG_REVISED_WINDOW_U4_TRAJECTORY_2026-09-30.csv`
13. Conventional GITT state-matched audit:
   `modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`
   `modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`

Word exports do not override these Markdown/data authorities.

---

# Current experimental backbone

## Figure 3 — accessible capacity

First-cycle lithiation/delithiation capacities:

- HEO: 901.25 / 609.12 mAh g^-1
- BM-HEO: 1056.10 / 782.08
- Mg-HEO: 731.15 / 458.91
- BM-Mg-HEO: 944.07 / 580.83

Safe interpretation:
- ball milling increases accessible capacity;
- Mg incorporation decreases accessible capacity;
- Figure 3 does not by itself establish a microscopic kinetic rate.

---

## Figure 4 — primary experimental contradiction

Current main four-material medians use the common normalized first-lithiation window z = 0.40–0.90:

| Sample | Delta E_relax (mV) | t63 (min) | first-cycle delithiation capacity (mAh g^-1) |
|---|---:|---:|---:|
| HEO | 168.5 | 10.37 | 609.12 |
| BM-HEO | 160.5 | 13.02 | 782.08 |
| Mg-HEO | 111.3 | 10.53 | 458.91 |
| BM-Mg-HEO | 135.2 | 12.70 | 580.83 |

Primary result:

**HEO -> BM-HEO gives higher accessible capacity while t63 becomes longer.**

The same milling direction is also present in the Mg-containing pair:
- Mg-HEO -> BM-Mg-HEO: capacity up;
- t63 up.

Mg incorporation is different:
- capacity down;
- Delta E_relax strongly down;
- t63 almost unchanged.

Do NOT describe Mg as simply lower-capacity/slower-relaxation.

### Conventional GITT conflict

HEO/BM state-matched range: approximately 200–800 mAh g^-1, 37 states.

- median Dapp,BM/Dapp,HEO = 1.7817
- median t63,HEO/t63,BM = 0.7622
- Dapp ratio > 1 at 37/37 states
- direct relaxation ranks BM slower at 35/37 states

Safe statement:

**Conventional GITT-derived apparent diffusivity does not preserve the observed HEO/BM current-off relaxation ordering.**

Do not say GITT is invalid or diffusion is absent.

---

## Figure 5 — conversion localization

Use:
- relaxation hump
- background-subtracted relaxation hump

not “GITT excess” as the main term.

Nominal dQ/dV / rest-end relaxation-hump peak pairs:

- HEO: 0.5446 / 0.5275 V
- BM-HEO: 0.5891 / 0.6175 V
- Mg-HEO: 0.4188 / 0.3870 V
- BM-Mg-HEO: 0.4848 / 0.5029 V

All nominal offsets are within ~32 mV.

Safe interpretation:
- the late-stage relaxation hump is dominated by processes in the conversion region;
- it does not identify one unique microscopic elementary step.

---

# Figure 6 — CURRENT STATUS AFTER 2026-10-03 REASSESSMENT

## Original role

The four-step model uses:

O <-> I <-> J <-> K <-> C

with:
- R1: initial electrochemical lithiation/electron transfer
- R2: effective M–O dissociation/local reconstruction
- R3: effective Li2O-forming/product-side reconstruction
- R4: subsequent electron transfer/metal reduction

The model was introduced as a minimal homogeneous multistep network to test whether higher accessible capacity and slower current-off relaxation can coexist.

### Frozen original representative result

R2 x 0.465, R3 x 50:

- Q/Q0 ≈ 1.111
- t63/t0 ≈ 1.087
- slowest finite mode ≈ 15.35 -> 17.68 min

This remains a valid **mathematical/kinetic existence test**.

---

## Critical new issue: experimental cutoff is not approached by growing pulse polarization

The real cell operates between 0.005 and 2.5 V. The conversion region is in the several-hundred-mV range.

Raw first-lithiation GITT traces for all four samples were re-parsed to test whether pulse polarization grows near the terminal cutoff.

Definitions:
- dE_inst = |E_3s - E_previous_rest_end|
- dE_tau = |E_pulse_end - E_3s|
- dE_total = |E_pulse_end - E_previous_rest_end|

Fixed 600 s pulses only; final partial pulse excluded from terminal-window comparison.

Median dE_tau:

| Sample | z=0.80–0.90 | z=0.90–0.98 |
|---|---:|---:|
| HEO | 185.6 mV | 147.8 mV |
| BM-HEO | 139.2 | 119.3 |
| Mg-HEO | 136.2 | 128.1 |
| BM-Mg-HEO | 132.1 | 119.9 |

The total pulse excursion also decreases in every sample.

Therefore:

**There is no evidence that first-lithiation cutoff is reached because pulse polarization progressively grows at the end of lithiation.**

The baseline/rest voltage itself moves downward toward cutoff.

Consequences:
- do not explain experimental capacity differences by a growing terminal overpotential;
- do not say “polarization drives cutoff” as the principal physical mechanism;
- pulse excursion is operational and is not a unique microscopic overpotential.

Authority:
`modeling/HEO_TERMINAL_POLARIZATION_AUDIT_2026-10-03.md`

---

## Local sensitivity result: the strong “different observables see different steps” claim is too strong

Reference-point +/-1% kinetic sensitivity:

| step | d ln Q/d ln k | d ln t63/d ln k |
|---|---:|---:|
| R1 | +0.0116 | -0.0025 |
| R2 | +0.2099 | -0.2768 |
| R3 | +0.3475 | -0.5976 |
| R4 | +0.0103 | +0.0079 |

Cosine similarity between S_Q and -S_t ≈ 0.993.

Therefore near the reference point:
- Q and t63 behave almost like a common scalar fast/slow coordinate;
- small perturbations preserve the conventional ordering;
- it is NOT supported to claim that Q and t63 locally probe strongly different rate directions.

This is important.

The anomalous Q-up / t63-up result appears only for **finite, step-selective perturbations**.

---

## Finite R2/R3 perturbation interpretation

Reconstructed-model comparison:

| perturbation | Q/Q0 | t63/t0 |
|---|---:|---:|
| R2 x 0.465 only | ~0.755 | ~1.373 |
| R3 x 50 only | ~1.355 | ~0.528 |
| both | ~1.111 | ~1.087 |

Thus:
- R2 slowing alone: conventional Q down / t63 up
- R3 acceleration alone: conventional Q up / t63 down
- both together: capacity gain remains positive while relaxation crosses back to slower-than-reference

This is a **finite nonlinear crossover**, not a generic feature of all multistep reactions.

Do NOT map this onto actual ball milling.

No experimental evidence currently shows that ball milling:
- slows R2;
- accelerates R3;
- changes those specific microscopic barriers in opposite directions.

---

## Operating-polarization exploratory audit

A reconstructed-model decomposition showed that the representative perturbation produced only a modest difference in instantaneous current polarization, whereas most of the voltage headroom at the original model cutoff came from a changed internal-state voltage trajectory.

This supports caution against a simple polarization explanation.

However:
- the original production script used for the frozen SI model results was not committed;
- this is an exploratory reconstructed-model audit;
- do not promote its exact percentages/numbers to the manuscript.

Authority:
`modeling/HEO_FOUR_STEP_OPERATING_POLARIZATION_AUDIT_2026-10-01.md`

---

## Realistic voltage-headroom test — key result

To test whether the original Q-up result was merely caused by a model cutoff placed too close to the operating voltage:

- keep all kinetics unchanged;
- add a constant voltage-reference offset;
- set the reference loaded voltage at DeltaQ=0.30 to a chosen conversion anchor;
- retain the experimental cutoff 0.005 V.

At a 0.50 V conversion anchor:

- Q_ref = 1.650904
- Q_pert = 1.775121
- Q_pert/Q_ref = 1.075242
- terminal C_ref = 0.780904
- terminal C_pert = 0.905121
- C_pert/C_ref = 1.159068

For conversion anchors >=0.2 V:
- Q ratio stabilizes at ~1.075;
- terminal converted-state ratio stabilizes at ~1.159.

Therefore:

**The higher-accessible-charge direction survives when conversion is placed far above the cutoff.**

So the anomaly is not solely a near-cutoff polarization artifact.

Under large voltage headroom, the physically useful model interpretation becomes:

**the perturbation changes how far the population progresses through the multistep conversion sequence before the accessible reaction extent is exhausted.**

This is closer to the experimental intuition that the important quantity may be **how much conversion can be accessed**, rather than a terminal polarization that grows until cutoff.

Authority:
`modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.md`

---

# Current Figure 6 claim boundary

## Safe

Experimental:
- BM gives higher accessible capacity and slower post-interruption relaxation.
- Conventional Dapp gives a conflicting HEO/BM ordering.
- the relaxation anomaly is localized to the conversion region.

Model:
- a minimal multistep network can produce the same qualitative Q-up / t63-up ordering under finite step-selective perturbations;
- this qualitative ordering survives a realistic separation between conversion voltage and the 0.005 V cutoff;
- therefore the ordering is kinetically possible without requiring the model to rely on a near-cutoff polarization artifact.

## Not safe

Do NOT claim:
- ball milling specifically slows R2 and accelerates R3;
- R2/R3 are experimentally identified elementary steps;
- higher BM capacity is caused by lower operating polarization;
- the capacity difference is caused by terminal polarization growth;
- “current-on is easier while current-off is slower” as an experimentally demonstrated mechanism;
- different observables always probe different steps;
- multistep kinetics automatically destroys fast/slow ordering;
- the model quantitatively fits BM;
- the exact reconstructed-model polarization decomposition is a submission-level result.

---

# Current preferred conceptual wording

Preferred experimental statement:

> **Higher accessible capacity can coexist with slower post-interruption relaxation in the ball-milled HEO.**

Preferred model statement:

> **A minimal multistep conversion network can reproduce this qualitative ordering under finite step-selective kinetic changes.**

If the voltage-headroom robustness is mentioned:

> **The qualitative ordering persists when the modeled conversion voltage is placed well above the experimental cutoff, indicating that the effect does not depend on a near-cutoff polarization artifact.**

Prefer “accessible conversion extent” or “progression through the multistep conversion sequence” over “polarization-limited cutoff capacity” in the physical interpretation.

---

# Manuscript status

## Do not rewrite the whole paper yet

Main v17 and SI v14 remain authoritative for text and numbering.

However, the following v17 Section 2.5 ideas are now under review and should NOT be treated as frozen:
- language that emphasizes “greater reaction throughput before voltage cutoff” as the physical explanation;
- any implication that BM maps microscopically to R2/R3;
- any broad statement that different observables necessarily correspond to different elementary steps.

The Abstract/Conclusion should not be revised until the final Figure 6 architecture is locked.

---

# Supporting Information status

Current SI authority:
`manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`

Existing electrochemical/mechanistic structure remains:
- S7 no-FEC
- S8 normalized rate retention/recovery
- S9 cycles 1–3 voltage profiles
- S10 cycle dQ/dV
- S11 relative interfacial-capacitance audit
- S12 pristine/post-cycle SEM
- S13 full multi-cycle GITT
- S14 early E–sqrt(t)
- S15 relaxation-fraction/state robustness
- S16 Dapp/direct-relaxation disagreement
- S17 GITT voltage-term decomposition
- S18 localization sensitivity
- S19 background/window sensitivity
- S20 cycle-history robustness
- S21 single-step kinetic sweeps
- S22 R2–R3 line cuts
- S23 eigenmode/partial-rate audit
- S24 Mg product-side equilibrium trajectory

New 2026-10-03 audits are not yet inserted into SI numbering.

---

# Remaining submission blockers

1. Final Figures 1–2 collaborator structural/compositional package.
2. Final Mg synthesis recipe and collaborator-verified nominal/ICP composition.
3. Missing cell/electrode metadata:
   - current collector
   - drying temperature/time
   - active loading
   - electrode thickness
   - separator
   - electrolyte volume
   - glovebox H2O/O2
   - exact 1 C basis and rate sequence
4. Original numerical first-cycle voltage profiles if recoverable.
5. Final XPS inclusion/exclusion decision.
6. Recheck pristine/post-cycle SEM placement.
7. Final numbering/reference audit after structural SI insertion.

---

# Immediate next task

**Do not start by editing prose.**

Next session should begin from the Figure 6 physics:

1. Decide the final modeled “accessible reaction” observable:
   - retain normalized passed charge Q, supported by the voltage-headroom robustness;
   - or augment/replace it with final converted-state fraction C as a more direct conversion-extent descriptor.
2. Decide whether the voltage-headroom audit belongs:
   - in Main Figure 6;
   - as a small inset;
   - or in the SI only.
3. Freeze the minimum Figure 6 claim as an existence/consistency test.
4. Only after that, revise:
   - Section 2.5
   - Figure 6 caption
   - Abstract
   - Conclusion
   - SI S21–S24 if needed.

The working principle is:

**Experiment first; model only supports physical possibility. Do not infer a microscopic BM mechanism that the data do not identify.**
