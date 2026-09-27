# HEO Figure 7 Artwork Final Note — 2026-09-27

**Status:** main scientific role and four-panel architecture frozen for the current manuscript round.

## Figure-level question

**Can the experimentally observed capacity–relaxation mismatch arise within a multistep conversion network without assigning a unique microscopic mechanism to ball milling?**

Figure 7 is a **microkinetic existence proof**. It is not a material-specific fit.

## Final main-panel architecture

### (a) Coarse-grained conversion network

Show

$O \rightleftharpoons I \rightleftharpoons I^* \rightleftharpoons C$

with:
- R1 and R3 labeled Faradaic;
- R2 labeled structural/reconstruction;
- the states explicitly identified as **effective kinetic states, not uniquely assigned phases**.

Main purpose:
establish the minimum multistep structure required for the argument.

Do not map any state uniquely onto one experimental crystallographic phase.

### (b) Current-off internal redistribution

Show the open-circuit balance

$j_{\rm ext}=F(\nu_1r_1+\nu_3r_3)=0$

while allowing

$\nu_1r_1=-\nu_3r_3\ne0$

and finite $r_2$.

Main purpose:
zero external current does not require every internal process to stop. Internal populations can continue redistributing while voltage relaxes.

Keep this panel schematic. The exact illustrative partial-current trajectory and numerical rates remain in the SI/model audit rather than being presented as measured quantities.

### (c) Homogeneous global-rate control

Use the homogeneous single-population control with all kinetic rates scaled together:

| Global rate scale | $Q_{\rm cutoff}$ | matched-state $t_{63}$ (min) |
|---:|---:|---:|
| 0.50 | 0.2993 | 22.45 |
| 0.75 | 0.4187 | 17.12 |
| 1.00 | 0.5585 | 13.45 |
| 1.50 | 0.7399 | 9.12 |
| 2.00 | 0.8322 | 6.95 |

Plot $t_{63}$ against $Q_{\rm cutoff}$ and annotate the direction of globally faster kinetics.

Main message:

$\text{globally faster}\Rightarrow Q_{\rm cutoff}\uparrow,\;t_{63}\downarrow$.

This panel is essential because it shows that capacity remains kinetically coupled and prevents the model from being interpreted as saying that capacity and relaxation are unrelated.

### (d) Heterogeneous-accessibility existence proof

Use the same axes as panel (c), and retain the homogeneous-control trajectory as a light dashed reference.

Reference model:
- $Q_{\rm cutoff}=0.55845$;
- $t_{63}=13.45$ min.

Illustrative heterogeneous-accessibility case:
- retain the reference accessible branch;
- add an additional accessible model branch with a slower R2;
- $Q_{\rm cutoff}=0.65714$;
- $t_{63}=15.28$ min.

Main message:

$Q_{\rm cutoff}\uparrow,\;t_{63}\uparrow$

is physically admissible in a heterogeneous multistep conversion network.

Main artwork should label the perturbation only as an **illustrative added accessible slow branch**. Do not label it “BM-like” and do not place the 0.65/0.15 population weights or 10× R2 ratio on the main figure. Those implementation parameters remain in the SI/model audit.

## Why panels (c) and (d) share the same axes

The common axis scale is deliberate. It prevents the heterogeneous shift from being visually exaggerated and makes the logical comparison explicit:

- panel (c): one global fast–slow coordinate gives capacity up / relaxation faster;
- panel (d): a heterogeneous accessibility change moves away from that one-dimensional trajectory and permits capacity up / relaxation slower.

## Main/SI boundary

Main Figure 7 retains only:
- network topology;
- current-off balance principle;
- homogeneous global-rate control;
- heterogeneous-accessibility existence proof.

Supporting Information / model audit retains:
- exact illustrative rate constants;
- population weights;
- the tenfold R2 change of the added branch;
- current-sweep amplitude/timescale separation;
- local eigenmodes;
- numerical current-off partial-current values;
- the Mg-like directional test.

## Claim boundary

Supported:
- conversion can be represented by coupled electrochemical and structural/reconstruction coordinates;
- zero external current can coexist with finite internal redistribution;
- a homogeneous global acceleration gives the conventional capacity-up / relaxation-faster relation;
- heterogeneous accessibility plus a distribution of internal timescales can give capacity-up / relaxation-slower behavior;
- therefore accessible capacity and current-off relaxation are coupled but need not vary monotonically along one scalar fast–slow coordinate.

Not supported:
- BM experimentally creates the illustrated slow branch;
- the chosen branch weights are measured phase fractions;
- R2 is one uniquely identified microscopic process;
- the tenfold illustrative R2 contrast is a fitted rate ratio;
- Mg maps uniquely to a model parameter;
- $t_{63}$ is one elementary rate constant.

## Numeric authority

Primary validation:
- `modeling/HEO_CAPACITY_RELAXATION_MICROKINETIC_VALIDATION_2026-09-25.csv`
- `modeling/HEO_CAPACITY_RELAXATION_MICROKINETIC_VALIDATION_2026-09-25.md`

Current-off balance:
- `modeling/HEO_MICROKINETIC_CURRENT_OFF_BALANCE_LITERATURE_INFORMED_2026-09-25.csv`

Model authority:
- `modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_INFORMED_2026-09-26.md`

Mg-like SI test:
- `modeling/HEO_MG_LIKE_MICROKINETIC_DIRECTIONAL_TEST_2026-09-26.md`
