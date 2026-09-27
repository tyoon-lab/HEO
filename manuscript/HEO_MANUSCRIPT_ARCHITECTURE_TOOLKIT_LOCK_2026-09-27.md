# HEO Manuscript Architecture — Toolkit-Aligned Story Lock

**Date:** 2026-09-27  
**Status:** current scientific/story authority after PI abstract review and Figure 4 integration.

## Scientific event that creates the paper

Ball milling increases accessible conversion capacity while the effective GITT relaxation becomes slower.

This remains the primary contradiction.

Mg incorporation is complementary but different: lower accessible conversion is accompanied by slower relaxation, which is directionally conventional, while the relaxation voltage-change magnitude simultaneously becomes smaller. Mg therefore constrains the relation between response magnitude and relaxation timescale rather than providing a second capacity–rate contradiction.

## Current central statements

**Experimental statement**

> Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics, while conventional GITT-derived apparent diffusivity indicates faster BM behavior despite the slower directly measured relaxation.

**Mechanistic statement**

> Microkinetic analysis shows that these combinations can arise naturally from the multistep character of conversion.

**General implication**

> GITT-derived apparent diffusivity should not be used alone to infer overall conversion kinetics.

## Evidence hierarchy

### Figures 1–2 — Define materials modifications

Question: Are HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO materially distinct before electrochemical interpretation?

Role: structural/compositional/morphological context only.

Current known composition note:
- historical ICP for the HEO3 set shows Mg-HEO3 is not a trace-doped material; Mg is approximately equimolar with the other principal cations.
- current manuscript must therefore avoid wording such as “small Mg substitution” unless collaborator synthesis/refinement data establish it.
- final Mg precursor, nominal formula, and synthesis details remain a collaborator input.

### Figure 3 — Accessible reaction extent

Question: How do BM and Mg change the amount of reaction accessed?

Answer:
- BM increases accessible capacity.
- Mg decreases accessible capacity.

No kinetic rate is inferred from capacity.

### Figure 4 — Decisive mismatch figure

Panel (a): define measured GITT relaxation quantities.

Panel (b): HEO/BM state-matched conventional $D_{\mathrm{app}}$ versus direct relaxation-rate comparison.

Panel (c): $\Delta E_{\mathrm{relax}}$–$t_{63}$ map.

Panel (d): first-cycle second-half capacity–$t_{63}$ map.

Scientific roles:
- BM: capacity ↑ and $t_{63}$ ↑ → primary capacity–kinetics contradiction.
- Mg: capacity ↓ and $t_{63}$ ↑ are directionally consistent with slower relaxation, but $\Delta E_{\mathrm{relax}}$ ↓ at the same time → response magnitude does not encode relaxation rate.
- conventional $D_{\mathrm{app}}$: BM/HEO >1 at 37/37 matched states, while direct BM relaxation-rate ratio is <1 at 35/37 states.

Figure 4 is the paper's decisive figure.

### Figure 5 — Localize the phenomenon

Question: Is the excess GITT relaxation associated with conversion?

Answer: GITT-excess and cathodic $dQ/dV$ peak positions agree within 32 mV for all four materials.

Claim boundary: conversion-associated, not uniquely assigned to nucleation, phase-boundary motion, oxygen migration, one cation, or one product-forming step.

### Figure 6 — History dependence

Question: Is the mismatch merely a first-cycle artifact?

Answer: No. The conversion-associated response evolves with cycle history, while BM retains higher accessible reaction extent together with longer $t_{63}$.

Role: robustness/history constraint, not a new headline.

### Figure 7 — Physical possibility / mechanistic consistency

Question: Can the observed combinations arise within a coupled multistep conversion network?

Answer:
- homogeneous global speed control recovers the conventional direction: faster → cutoff capacity ↑, $t_{63}$ ↓.
- heterogeneous-accessibility example gives capacity ↑ together with $t_{63}$ ↑.
- separate Mg-like SI existence test gives capacity ↓, relaxation magnitude ↓, and $t_{63}$ ↑.

Role: existence proof only. Do not map BM or Mg uniquely onto individual model parameters.

## Abstract lock

The PI-reviewed abstract is frozen in:

`manuscript/HEO_ABSTRACT_LOCK_2026-09-27.md`

Important wording decisions:
- begin with “Faster conversion kinetics…”
- BM/Mg are “complementary modifications that respectively increase and decrease accessible conversion capacity”
- GITT is introduced before the observed BM/Mg mismatches
- keep the bridge sentence “The two modifications produce different mismatches among these observables.”
- BM is the capacity–rate contradiction
- Mg is the magnitude–timescale constraint
- avoid “ranking” in the abstract
- use “can arise within a multistep conversion network,” not “physically admissible”

## Interpretation boundary

Supported:
- “conversion-associated kinetics” after Figure 5 localization
- $t_{63}$ as a model-free effective current-off relaxation timescale
- $\Delta E_{\mathrm{relax}}$ as relaxation voltage-change magnitude
- conventional apparent $D$ can fail to preserve the direct fast–slow ordering

Not supported:
- diffusion is absent
- GITT is invalid
- $t_{63}$ is the forward conversion rate
- smaller relaxation magnitude means faster kinetics
- ball milling uniquely slows a particular microscopic reconstruction step
- Mg uniquely changes one microkinetic parameter
- illustrative model population weights are measured phase fractions

## EIS decision

Cycling EIS remains excluded from the manuscript evidence chain because of state-matching/outlier/process-overlap limitations. It is not required for the central claim.

## Main/SI split for conventional diffusivity

Main text:
- use the compositionally identical HEO/BM-HEO pair only.

Reason:
- this is the cleanest test because composition-dependent $V_M/M_B$ factors cancel.

Exploratory/SI candidate:
- HEO/Mg-HEO cross-composition calculation.
- preliminary reanalysis also gives apparent $D$ faster for Mg while direct relaxation is slower.
- retain as robustness only unless the composition/density/molar-volume treatment is fully frozen and reproduced.

## Current authoritative manuscript-facing files

- Main: `manuscript/HEO_MANUSCRIPT_V12_AFM_CAPACITY_KINETICS_2026-09-27.md`
- Figure logic: `manuscript/HEO_FIGURES_3_7_CURRENT_LOGIC_V6_2026-09-27.md`
- Abstract lock: `manuscript/HEO_ABSTRACT_LOCK_2026-09-27.md`
- Figure 4 lock: `manuscript/HEO_FIGURE4_ARTWORK_FINAL_NOTE_2026-09-27.md`

## Remaining submission blockers

1. Final Figures 1–2 collaborator package and text.
2. Mg synthesis details / nominal composition / final ICP interpretation.
3. Cell/electrode metadata: current collector, drying, loading, thickness, separator, electrolyte volume, glovebox conditions, 1 C basis, exact rate sequence.
4. WonATech first-half/second-half convention before using definitive lithiation/delithiation labels.
5. Original first-cycle numerical voltage-profile data for the final $dQ/dV$ source, if recoverable.
6. Final active-mass/molar-volume metadata if absolute $D$ or cross-composition $D$ is ever promoted; absolute $D$ is not required for the current claim.
