# Electrochemistry Section Backbone

**Date:** 2026-09-18

## Purpose

Build the electrochemistry section around one simple apparent paradox:

**ball milling increases conversion-related capacity, yet the conversion-associated relaxation is not faster and is often slower.**

Mg incorporation provides the complementary case: it lowers accessible conversion capacity without a proportional change in the relaxation timescale.

The section should first make this mismatch visually obvious, then use cycle-resolved GITT and minimal microkinetics to explain why reaction extent and relaxation kinetics need not change together. Do not overload the synthesis-centered manuscript with a separate GITT-method narrative.

## Proposed result flow

### Figure / Section 1 — Electrochemical utilization and rate/cycling behavior

Core panels:

- first-cycle voltage profiles for HEO, BM-HEO, Mg-HEO, BM-Mg-HEO;
- first-cycle capacity and ICE summary;
- low-rate cycling;
- rate performance.

Questions answered:

- Which treatment increases accessible low-rate capacity?
- Which treatment lowers capacity?
- Which capacity advantages survive increasing rate?

Working interpretation:

- Ball milling increases accessible low-rate capacity but the advantage is rate-sensitive.
- Mg lowers accessible capacity.
- These trends are not adequately explained by a simple monotonic D_GITT trend.

### Figure / Section 2 — Current-off polarization and relaxation

Use cumulative specific capacity as the main state coordinate.

Preferred panels:

A. Representative current interruption and definition of metrics.

B. Apparent instantaneous current-off jump / resistance from early `E = a + b sqrt(t)` fitting.

C. `Delta E_relax` over the common 3 s to 60 min window.

D. Model-free `t63`; optionally t50/t90 in Supporting Information.

E. Late-stage transition-associated excess relaxation after background subtraction.

Key interpretation:

- Ball milling produces a large early first-lithiation polarization penalty but the fast resistance difference largely disappears at intermediate capacity.
- Ball milling broadens the late-stage transformation-associated polarization and lowers its local peak amplitude.
- Mg strongly suppresses the late-stage transformation-associated response.
- Mg lowers polarization amplitude without shortening relaxation time, so the reduced polarization cannot be explained simply by faster diffusion.

### Figure / Section 3 — Synthesis-dependent phase-evolution mechanism

Integrate electrochemistry with the structural/synthesis narrative.

Preferred model:

- HEO: relatively concentrated spinel-to-rock-salt/conversion transition -> pronounced low-voltage polarization hump.
- BM-HEO: milling-induced disorder / heterogeneous local environments -> transformation distributed over a broader capacity interval -> lower peak transition polarization and larger accessible low-rate capacity, but slower residual relaxation and poor rate retention.
- Mg-HEO: Mg-induced structural stabilization -> suppressed conversion/phase-transition extent -> reduced phase-transition overpotential and reduced conversion capacity.
- BM-Mg-HEO: ball milling increases slow polarization but does not fully restore the transition response suppressed by Mg.

This section should use relevant spinel-HEO / conversion-electrode literature as mechanistic support rather than requesting additional operando structural experiments.

## Main-text versus Supporting Information

### Main text

Keep:

- first-cycle capacity / cycling / rate behavior;
- ICI-style current-off jump or apparent fast resistance;
- Delta E_relax vs capacity;
- t63 vs capacity;
- transition-hump height/width/area or a compact summary;
- mechanistic link to spinel-to-rock-salt/conversion phase evolution.

### Supporting Information

Move:

- t50 and t90 full curves;
- early and terminal slopes;
- conventional apparent D_GITT curves;
- current-on/pulse descriptors;
- fitting-window sensitivity;
- optional D-only / D+compact relaxation / distributed-response audit.

## Role of `D-only -> D+RC -> distributed relaxation`

This hierarchy is valuable scientifically but currently does not provide a clean synthesis-dependent parameter for the HEO manuscript.

What it shows:

- a diffusion-only compact model is insufficient to reproduce the full rest transient;
- adding one exponential mode can absorb most residual mismatch;
- distributed relaxation gives an even closer descriptive fit;
- compact parameters are not necessarily identifiable because finite diffusion itself has an eigenmode spectrum and the added exponential can overlap it.

Therefore this comparison is best treated as:

- an internal model-identifiability audit;
- possible SI sensitivity material;
- useful groundwork for the separate GITT/EKF project.

Do **not** make it a central HEO manuscript result unless a robust parameter emerges that clearly separates HEO/BM/Mg effects and is stable to fitting-window and initialization choices.

## Central electrochemistry message

The strongest manuscript-level message is the apparent mismatch between **how much conversion is accessed** and **how fast the conversion-associated state relaxes**.

- **Ball milling:** higher surface area/accessibility allows more conversion and higher capacity, yet t63 is not shortened and is often longer. More conversion therefore does not require faster conversion-associated relaxation.
- **Mg incorporation:** accessible conversion capacity is reduced, but t63 does not change in proportion to that reduction. Lower capacity therefore does not simply mean slower or faster relaxation.

A shorter t63 remains consistent with faster conversion-related relaxation kinetics, but t63 is not identical to the forward conversion rate. Capacity can be changed through reaction accessibility, surface area, and state population independently of the internal rates controlling post-interruption relaxation.

Figure 7 should resolve this apparent contradiction using a minimal multi-step microkinetic picture in which:
- reaction accessibility/state population controls how much conversion can be reached;
- kinetic eigen-timescales control how the resulting state relaxes;
- additional accessible reaction population can include slower-relaxing states.

This phenomenon is not claimed to be HEO-exclusive. Rather, the multication, heterogeneous, reconstructive nature of HEO conversion makes the separation between reaction accessibility and internal relaxation particularly plausible and experimentally visible.

Detailed current wording authority: `manuscript/HEO_ELECTROCHEMISTRY_CORE_STORY_2026-09-23.md`.
