# Minimal Conversion Microkinetics — 2026-09-23

## Purpose

Provide a minimal mechanistic interpretation for Figures 5–6 without claiming a uniquely identified microscopic RDS.

The model asks whether a multi-step conversion network can naturally explain:
- amplitude–timescale decoupling;
- prolonged current-off relaxation;
- cycle-history dependence;
- BM: higher reversible capacity with longer effective t63;
- Mg: lower reversible capacity while later-cycle t63 approaches HEO-like values.

The model is **not** intended to extract unique microscopic rate constants.

## Effective reaction network

R1 — electrochemical activation:

A + Li+ + e- <-> B

R2 — effective nucleation/activity evolution:

B -> N

R3 — electrochemical phase growth/conversion:

B + Li+ + e- <-> P

A/B/N/P are effective kinetic states, not atomistically identified species.

## State variables

A minimal implementation uses:
- b = activated precursor fraction
- p = converted product fraction
- n = nucleation/activity coordinate
- a = 1 - b - p

R1 and R3 carry Faradaic current.

## Current-on condition

j_ext = r1 + r3

The applied galvanostatic pulse determines the potential needed to satisfy this current balance while the internal states evolve.

## Current-off condition

At open circuit:

j_ext = r1 + r3 = 0

but this does not require:

r1 = r3 = 0.

Internal counter-current is possible:

r1 = -r3 != 0.

Therefore electrochemical/structural conversion-state evolution can continue while external current is zero, allowing a prolonged OCV relaxation.

This is the key conceptual improvement over a simple single-step RC picture.

## Linearized interpretation

Near a local cycled state, a multi-state kinetic system can be linearized:

d(delta x)/dt = J delta x

which yields:

E(t)-E_eq = sum_i B_i exp(-t/tau_i).

Interpretation:
- B_i depends on the excitation/population of a mode and the voltage sensitivity to that mode;
- tau_i derives from the kinetic eigenvalue.

Therefore relaxation amplitude and relaxation timescale need not co-vary.

This directly rationalizes:
- Mg: large changes in hump amplitude with modest t63 change;
- BM: higher capacity while the ensemble t63 remains longer.

Do not call B_i or tau_i directly measured microscopic eigenmodes.

## Simple single-step RC as a negative control

A single charge-transfer/RC element gives a much more constrained response and cannot naturally account for the observed long, history-dependent amplitude–timescale behavior by itself.

Safe statement:

**A simple single-step RC description is insufficient.**

Do not write:
- charge transfer is absent;
- the hump proves nucleation;
- the hump proves phase-boundary growth.

## Synthetic regime test

Two effective parameter regimes were constructed:
- nucleation-dominant
- electrochemical-growth-dominant

They can be tuned to have almost identical response at one reference pulse current:

| regime | residual relaxation at 3 s | t63 |
|---|---:|---:|
| nucleation-dominant | 24.82 mV | 13.66 min |
| electrochemical-growth-dominant | 24.13 mV | 13.70 min |

This shows that the model should not be used to claim a unique RDS from the present relaxation trace.

Main-text handling:
do not foreground “non-identifiable” or state that new experiments are required. Instead say that the model tests mechanistic consistency and demonstrates physically plausible internal-state routes to the observed behavior.

If a limitation sentence is needed in Methods/SI:

**The model is intended to test mechanistic consistency rather than to assign a unique elementary rate-limiting step.**

## Current-dependence model prediction

In the current synthetic implementation, the two matched regimes separate when pulse current is changed, especially in t63(J).

This is a model prediction/future route for mechanism discrimination.

Do not present it as a required experiment for the present manuscript.

Potential future study:
- multiple pulse currents at matched reaction state;
- compare amplitude, t63, and pulse polarization;
- expand to oxide vs sulfide conversion chemistries.

## Figure 7 role — frozen architecture

Preferred title:

**Microkinetic interpretation of history-dependent conversion relaxation**

The main-text figure is an interpretation figure, not a parameter-fitting or RDS-identification figure.

### Frozen panels

**(a) Effective multi-step conversion network.** Show R1: A + Li+ + e- <-> B, R2: B -> N, and R3: B + Li+ + e- <-> P. Label A/B/N/P explicitly as effective kinetic states rather than atomistically identified phases or species.

**(b) Current interruption and internal counter-current.** Show the galvanostatic condition j_ext = r1 + r3 during the pulse and the open-circuit condition j_ext = 0 after interruption. Include one illustrative simulation of the current-off period showing that r1 and r3 remain finite and opposite while r1+r3 remains zero, together with the continuing voltage relaxation. This is a mechanistic-consistency demonstration, not a fit to any one HEO sample. The compact reproducibility dataset is saved as `HEO_MICROKINETIC_CURRENT_OFF_BALANCE_2026-09-23.csv`.

For the illustrative regime, immediately after interruption r1 ~ -5.0e-5 and r3 ~ +5.0e-5 while r1+r3 is numerically ~1e-18. The internal counter-current then decays during the 3600 s rest while the residual voltage relaxation decreases from ~24.9 mV to zero by the experimental end-reference.

**(c) Multi-state amplitude–timescale separation.** Present the local linearization d(delta x)/dt = J delta x and E(t)-E_eq = sum_i B_i exp(-t/tau_i). Visually separate B_i (state excitation/population and voltage sensitivity) from tau_i (kinetic eigen-timescale). The purpose is to explain why a large change in relaxation amplitude does not require a comparable change in t63. Do not present B_i or tau_i as experimentally measured microscopic eigenmodes.

**(d) Experimental constraints and compatible interpretation.** Tie the model back to Figures 5–6 using three experimentally established constraints: (i) cycling changes conversion-associated amplitude much more strongly than t63; (ii) ball milling increases accessible reversible reaction extent while effective relaxation remains longer; and (iii) Mg lowers accessible reversible reaction extent while later-cycle t63 approaches the undoped HEO. Summarize these as distinct coordinates—accessible reaction extent, relaxation excitation/amplitude, and effective timescale—rather than a single fast/slow kinetic axis.

### Main vs SI boundary

Keep the synthetic current-dependence discrimination out of the main Figure 7. It is useful as an SI/future-direction result because two regimes matched at one reference current separate when current is varied, but putting it in the main figure would shift attention toward RDS identification and invite an unnecessary additional-current experimental requirement.

Likewise, do not make a single-step RC negative-control fit a main panel. The main-text claim is only that a simple single-step RC description is insufficient to account for the full long, history-dependent amplitude–timescale behavior.

The Figure 7 endpoint is therefore:
**multi-step conversion kinetics provides a physically consistent explanation for independent evolution of accessible reaction extent, relaxation excitation, and effective relaxation timescale without assigning a unique microscopic RDS.**

## Main paper-level conclusion supported by the model

**Conversion dynamics cannot be reduced to a single fast–slow kinetic descriptor; the amount of reversible reaction accessed, the population of excited conversion-associated states, and their effective relaxation timescales can evolve as distinct but coupled quantities.**
