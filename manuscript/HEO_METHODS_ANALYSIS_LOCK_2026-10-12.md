# HEO Methods and Analysis Lock — 2026-10-12

## Purpose

This file preserves the current operational definitions, analysis boundaries, and numerical guardrails so later manuscript edits do not silently change the scientific meaning.

## GITT protocol

Working protocol from the current raw data / manuscript:

- current: 100 mA g-1
- pulse: 600 s
- rest: 3600 s
- Mg-free sampling: approximately 1 s
- Mg-containing sampling: approximately 3 s
- common cross-sample post-interruption reference: 3 s

Do not revert to the older slide annotation suggesting a 60 s rest; the working raw-data protocol uses 60 min rest.

## Relaxation descriptors

### t63

First time required to complete 63.2% of the measured 3 s-to-60 min voltage relaxation.

Use as an operational characteristic relaxation time.

It avoids assuming a single-exponential fit.

Do **not** call it model-free in the sense of assumption-free physics and do not interpret it as one elementary microscopic rate constant.

### Delta Erest

|Erest,60 min - Erest,3 s|

Operational relaxation magnitude.

Do not call it a pure kinetic overpotential. It can contain thermodynamic-slope, reconstruction, kinetic, and other contributions.

### Relaxed voltage

60 min rest-end voltage.

Use as a state coordinate and independent support for region transitions.

## Region definition

Current boundaries:

- L1: transition out of initial response
- L3: central conversion-associated landmark
- L4: end of broad relaxed-voltage plateau / transition to steeper low-voltage branch

Regions:

- R1 start -> L1
- R2 L1 -> L3
- R3 L3 -> L4
- R4 L4 -> end

Intermediate extrema remain within-region features.

Before publication, standardize L4 with the same Q–OCV-based rule across all four samples.

## Physical assignment rule

Define regions electrochemically first.

Then use independent relaxed-voltage behavior plus established conversion literature for broad assignment.

Allowed broad language:

- R1 early lithiation
- R2 conversion onset/progression; oxide destabilization/reconstruction
- R3 late conversion; continued evolution toward reduced metal/Li2O-derived states
- R4 post-plateau deep lithiation

Not established:

- unique individual-cation sequence at each boundary
- direct detection of M–O bond breaking by GITT
- unique reconstructed intermediate
- exact Mg site/bond mechanism
- four elementary microscopic steps

## Capacity partition

Regional capacity is currently protocol-derived from pulse count/setpoint.

The total GITT scale and separate GCD first-cycle capacity are not identically normalized.

Therefore Main-text preference:

**regional fraction (%)**

If absolute regional mAh g-1 is later reported, label it as protocol-derived unless direct raw-current integration is completed.

## Current headline regional changes

BM, Mg-free:
- R2 ~29% -> ~38%: largest positive change
- R3 ~48% -> ~29%: reduced relative contribution

Mg, unmilled:
- R3 ~48% -> ~31%: dominant suppression

Full R1/R2/R3/R4 patterns remain available for Results/SI, but the Abstract should emphasize the dominant stage.

## Sensitivity audit

L1/L3/L4 independently shifted +/-1 GITT step.

Internal result:
- BM capacity pattern R1+, R2+, R3-, R4+ robust in 100% tested combinations.
- BM t63 pattern R1-, R2+, R3+, R4+ robust in 100%.
- Mg R3 capacity decrease robust in 100%.
- R3 most negative Mg change robust in 100%.
- R3 dominates Mg capacity loss essentially completely.
- Mg R3 |Delta t63| <= 1.5 min in 100%.

Use for reviewer defense or SI only if needed.

## Secondary analyses

Conventional GITT Dapp, relaxation-shape fits, alternate percentiles, and earlier microkinetic models are secondary/supporting.

Do not let them redefine the Main story unless new evidence changes the scientific question.

## Data availability note for future chats

The 2026-10-12 working environment contained the four raw GITT xlsx files and derived CSVs/plots used for the stage-resolved analysis.

GitHub restart files preserve the conclusions and operational definitions, but large raw uploads may not be available automatically in every future chat. If exact raw re-integration is required and the files are unavailable, re-upload the four raw GITT workbooks rather than reconstructing exact values from prose.
