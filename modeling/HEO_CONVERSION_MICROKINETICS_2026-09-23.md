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

## Figure 7 role

Preferred title direction:

**Microkinetic interpretation of conversion-state relaxation**

or

**Microkinetic origin of conversion-associated relaxation**

Preferred panels:
- (a) effective multi-step conversion network
- (b) current-on and current-off current-balance concept; r1+r3=0 at OCV but internal counter-current can remain
- (c) amplitude–timescale separation in the linearized multi-state response
- (d) compatibility/interpretation summary tied to Figure 5–6 observations

A current-dependence prediction may be placed in SI or used as a small secondary panel only if it does not invite unnecessary experimental expansion.

## Main paper-level conclusion supported by the model

**Conversion dynamics cannot be reduced to a single fast–slow kinetic descriptor; the amount of reversible reaction accessed, the population of excited conversion-associated states, and their effective relaxation timescales can evolve as distinct but coupled quantities.**
