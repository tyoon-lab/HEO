# Electrochemistry Section Backbone

**Date:** 2026-09-18

## Purpose

Build the electrochemistry section around direct observables that explain the roles of ball milling and Mg incorporation, without overloading the synthesis-centered manuscript with a separate GITT-method narrative.

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

The strongest manuscript-level message is not that one sample has a larger or smaller apparent Li diffusivity. It is that **ball milling and Mg incorporation alter different parts of the phase-evolving electrochemical response**:

- ball milling increases accessible capacity while broadening the late-stage phase-transition response and slowing residual relaxation;
- Mg suppresses the late-stage phase-transition-associated polarization and lowers conversion capacity, without producing faster relaxation.

This distinction explains why polarization amplitude, relaxation time, rate capability, and accessible capacity do not change in parallel and why a single apparent GITT diffusivity is insufficient as the main mechanistic descriptor.
