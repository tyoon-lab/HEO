# HEO Figure 6 reassessment lock — 2026-10-03

## Why Figure 6 was reopened

The current v17 manuscript uses a four-step model to show that higher accessible capacity and slower post-interruption relaxation can coexist. During PI review, the physical meaning of the modeled capacity was questioned because the experimental conversion voltage is around the several-hundred-mV range while the cell cutoff is only 0.005 V.

The central concern was:

> Does the model generate the anomalous Q-up / t63-up ordering only because its operating voltage is artificially close to the cutoff, so that polarization strongly controls modeled capacity?

This note records the new checks and the revised claim boundary.

---

## 1. Experimental first-lithiation pulse-voltage audit

Raw GITT data for all four samples were re-parsed.

Key result:
- no sample shows a growth of the pulse-voltage excursion near the lithiation cutoff;
- Delta E_tau and the total pulse excursion decrease from z=0.80–0.90 to z=0.90–0.98 in all four samples.

Representative terminal-window medians:

| sample | Delta E_tau, z=0.80–0.90 (mV) | Delta E_tau, z=0.90–0.98 (mV) |
|---|---:|---:|
| HEO | 185.6 | 147.8 |
| BM-HEO | 139.2 | 119.3 |
| Mg-HEO | 136.2 | 128.1 |
| BM-Mg-HEO | 132.1 | 119.9 |

Therefore the experimental traces do not support a picture in which an increasingly large terminal polarization pushes the electrode into the 0.005 V cutoff.

Authority:
- `modeling/HEO_TERMINAL_POLARIZATION_AUDIT_2026-10-03.md`
- `modeling/HEO_TERMINAL_POLARIZATION_SUMMARY_2026-10-03.csv`

---

## 2. Local kinetic-sensitivity test

A reconstructed version of the frozen four-step model was checked against the existing SI numerical results and then perturbed by +/-1% in each kinetic scale around the reference point.

Local log sensitivities:

| step | d ln Q / d ln k | d ln t63 / d ln k |
|---|---:|---:|
| R1 | +0.0116 | -0.0025 |
| R2 | +0.2099 | -0.2768 |
| R3 | +0.3475 | -0.5976 |
| R4 | +0.0103 | +0.0079 |

Cosine similarity between the Q-sensitivity vector and minus the t63-sensitivity vector is approximately 0.993.

### Consequence

The strong statement

> “capacity and relaxation locally probe different elementary kinetic directions”

is NOT supported near the reference state.

For small perturbations, the model remains almost scalar-like:
- changes that increase accessible capacity generally shorten t63;
- the conventional capacity-relaxation ordering is locally preserved.

Authority:
- `modeling/HEO_FOUR_STEP_LOCAL_SENSITIVITY_2026-10-03.csv`

---

## 3. Finite step-selective perturbation remains possible

The existing representative finite perturbation is:

- R2 x 0.465
- R3 x 50

Individual effects in the reconstructed model:

| perturbation | Q/Q0 | t63/t0 |
|---|---:|---:|
| R2 x 0.465 only | ~0.755 | ~1.373 |
| R3 x 50 only | ~1.355 | ~0.528 |
| both | ~1.111 | ~1.087 |

Thus:
- R2 slowing alone gives lower capacity / slower relaxation;
- R3 acceleration alone gives higher capacity / faster relaxation;
- together, the capacity gain from the R3 change remains larger than the capacity loss from the R2 change, while the relaxation slowing from the R2 change becomes larger than the relaxation acceleration from the R3 change.

The anomalous Q-up / t63-up region is therefore a finite nonlinear crossover, not a generic local property of a multistep system.

### Important claim boundary

Do NOT state that ball milling actually:
- slows R2;
- accelerates R3;
- redistributes specific microscopic barriers in this way.

The R2/R3 perturbation is only a representative existence/consistency test.

---

## 4. Operating-polarization audit

An exploratory reconstructed-model audit separated:

E_on(x,Q) from E_0(x,Q) at the same internal state.

For the original representative model, the BM-like case had only a modestly smaller instantaneous current polarization, whereas most of the voltage headroom at the reference cutoff charge came from a changed internal-state voltage trajectory.

This result argues against interpreting the model capacity difference as a simple polarization reduction.

However:
- the original production script was not committed;
- the audit is a reconstructed-model diagnostic, not a submission-level numerical authority.

Authority:
- `modeling/HEO_FOUR_STEP_OPERATING_POLARIZATION_AUDIT_2026-10-01.md`

---

## 5. Realistic voltage-headroom test

The strongest concern was tested directly.

Method:
- keep the four-step kinetics unchanged;
- shift the model voltage reference so that the reference loaded voltage at DeltaQ=0.30 is assigned a selected conversion anchor;
- keep the experimental cutoff at 0.005 V;
- compare the reference and R2 x 0.465 / R3 x 50 cases.

At a 0.50 V conversion anchor:

- Q_ref = 1.650904
- Q_pert = 1.775121
- Q_pert/Q_ref = 1.075242
- terminal converted-state fraction C_ref = 0.780904
- C_pert = 0.905121
- C_pert/C_ref = 1.159068

The result saturates for conversion anchors >=0.2 V:
- Q ratio remains ~1.075;
- converted-state ratio remains ~1.159.

### Consequence

The Q-up direction does NOT disappear when the conversion voltage is separated strongly from the cutoff.

Therefore the model anomaly is not solely a near-cutoff polarization artifact.

Under large voltage headroom, the more useful interpretation is:
- both cases nearly exhaust the oxide-derived state;
- the perturbed case progresses farther through the multistep sequence toward the final converted state;
- the remaining charge difference reflects different accessible conversion extent / internal-state progression rather than a growing terminal polarization.

Authority:
- `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.md`
- `modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.csv`

---

## 6. What Figure 6 can safely claim now

Strongest safe experimental statement:

> BM-HEO exhibits higher accessible capacity together with slower post-interruption relaxation.

Strongest safe model statement:

> A minimal multistep conversion network can reproduce the same qualitative ordering under finite step-selective kinetic changes, and the ordering survives when the model conversion voltage is placed far above the experimental cutoff.

The model can therefore be used as an existence/mechanistic-consistency test.

It does NOT establish:
- the actual microscopic pathway modified by ball milling;
- a unique R2/R3 assignment;
- that capacity is controlled by terminal polarization;
- that different observables always probe different elementary steps locally;
- that the model quantitatively reproduces the experimental BM magnitude.

---

## 7. Current preferred physical language

Prefer:
- accessible conversion extent
- progression through the multistep conversion sequence
- post-interruption relaxation
- finite step-selective perturbation
- mechanistic-consistency / existence test

Avoid:
- “ball milling slows R2 and accelerates R3”
- “ball milling lowers the operating polarization”
- “easier to drive but slower to equilibrate” as a demonstrated experimental mechanism
- “capacity is cutoff-polarization limited”
- “multistep kinetics necessarily gives independent observables”

---

## 8. Manuscript status

Do NOT immediately rewrite the whole paper around the exploratory model discussion.

Main v17 and SI v14 remain the text authorities, but Section 2.5/Figure 6 language should be revised after the Figure 6 architecture is re-frozen.

Likely edits after the next decision:
- remove or soften language implying that greater modeled reaction throughput is caused by approaching the voltage cutoff;
- emphasize accessible conversion extent rather than terminal polarization;
- retain the model only as a qualitative possibility test;
- preserve the experimental BM capacity-up / t63-up observation as the primary result.

---

## 9. Immediate next task

Before editing Main v17:

1. decide the final Figure 6 observable:
   - retain normalized modeled charge but interpret it as accessible conversion extent under the tested voltage-headroom robustness;
   - or replace/augment it with final converted-state fraction C;
2. decide whether Figure 6 should include a voltage-headroom robustness panel or move that audit to the SI;
3. freeze the minimal main-text claim;
4. only then revise Section 2.5, Abstract, Conclusion, and the Figure 6 caption consistently.
