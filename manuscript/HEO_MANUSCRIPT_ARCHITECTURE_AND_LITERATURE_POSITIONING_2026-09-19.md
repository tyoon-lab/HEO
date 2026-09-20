# HEO Manuscript Architecture and Literature Positioning

**Date:** 2026-09-20
**Purpose:** Gate-A / Gate-B note for the figure-aligned HEO manuscript, following the Yoon Lab Publication Toolkit.

## Manuscript type

Hybrid **material-development + mechanism-discrimination** paper.

The paper should not be positioned primarily as:
- a new GITT method paper;
- a phase-field parameter-identification paper;
- a pure performance paper.

The central contribution is the mechanistic separation of synthesis-sensitive electrochemical coordinates in a conversion-type spinel HEO anode.

## Abstract logic

1. Phase-evolving HEO anodes cannot be interpreted reliably by a single apparent transport parameter.
2. A 2 × 2 comparison separates ball milling from Mg incorporation.
3. Ball milling raises accessibility/capacity but does not accelerate long-rest relaxation; its conversion-associated response becomes lower and broader.
4. The GITT excess peak tracks the first-cycle cathodic dQ/dV conversion feature within 18–32 mV across all four samples.
5. Mg shifts the conversion feature to lower potential, lowers accessible capacity, and strongly suppresses the excess response without shortening relaxation.
6. A reduced spatial model of conversion-associated state evolution remains directionally consistent without parameter refitting.
7. Main implication: accessibility, conversion extent/distribution, and relaxation time are distinct synthesis-sensitive coordinates.

## Introduction logic

1. Establish the five-cation spinel HEO family and its relevance to conversion-type lithium storage [1–4].
2. Establish that lithiation is structurally reconstructive rather than diffusion through an invariant host [5,7].
3. Introduce ball milling and Mg incorporation as physically different perturbations, using the closest direct precedents [6,8–12].
4. Define the diagnostic limitation: conventional GITT often compresses a phase-evolving transient into one apparent D [6,15], while current interruption preserves independent amplitude/time information [16].
5. Treat spinel-to-rock-salt evolution as part of the broader conversion-associated structural evolution rather than as the only reaction event.
6. State the unresolved question: do BM and Mg alter the same kinetic coordinate, or different coordinates of accessibility, conversion extent/distribution, and relaxation?
7. State the 2 × 2 strategy and the mechanism-sufficiency role of the reduced conversion-associated spatial model.

## Background deliberately omitted or minimized

- generic long history of high-entropy materials;
- broad battery-anode performance comparisons unrelated to the mechanistic question;
- generic advantages of nanosizing;
- extended GITT theory beyond what is needed to motivate the current-off analysis;
- detailed phase-field theory in the Introduction.

## Unresolved gap emphasized

Same-family HEO/BM studies and conventional GITT already exist [6], and structural phase evolution is established [5,7]. Mg stabilization precedents also exist [8–10]. What remains unresolved is whether synthesis-driven changes in capacity and polarization reflect one transport parameter or independent changes in **accessibility, conversion extent/distribution, and relaxation time**.

## Abstract headline result

Ball milling increases capacity while broadening/lowering the conversion-associated response and lengthening relaxation; Mg shifts conversion to lower potential and suppresses both the conversion-associated response and accessible capacity without faster relaxation.

## Closest prior work and manuscript differentiation

### [6] Xiao et al., Nano Energy 2022
Already showed:
- same five-cation HEO family;
- ball-milled comparison;
- conventional GITT-derived diffusivity.

Current manuscript adds:
- direct current-off separation of fast polarization, finite-window relaxation amplitude, and relaxation time;
- state-localized transition-associated excess response;
- a 2 × 2 comparison including Mg;
- explicit separation of accessibility, transformation extent/distribution, and relaxation time.

### [7] Jin et al., Materials Today Chemistry 2025
Already showed:
- spinel -> mixed spinel/rock-salt -> rock-salt evolution in the same five-cation family.

Current manuscript adds:
- the electrochemical relaxation/polarization signature associated with this phase-evolving region;
- synthesis-dependent redistribution/suppression of that signature.

### [8–10] Mg-containing HEO studies
Already showed:
- inactive Mg-containing components can support structural retention/stabilization during conversion.

Current manuscript adds:
- the experimentally specific combination of lower capacity + much smaller transition-associated polarization + non-shortened relaxation;
- distinction between reduced transformation extent and faster Li transport.

### [11,12,20] Milling/fragmentation/size precedents
Already showed:
- milling can alter spinel/rock-salt balance;
- fragmentation can increase conversion reversibility/interfacial utilization;
- smaller spinel HEOs can show lower polarization and more complete conversion.

Current manuscript adds:
- direct quantification of lower peak + broader transition-associated response together with longer long-rest relaxation.

### [15–17] GITT/current-interruption/phase-transition physics
Already showed:
- apparent GITT diffusivity is model- and assumption-sensitive;
- current interruption supports early sqrt(t)-based analysis;
- nucleation can contribute substantially to phase-transition overpotential.

Current manuscript adds:
- application of these concepts to discriminate processing and compositional effects in a phase-evolving HEO.

## Literature-use boundaries

- [7] is the primary source for exact spinel -> mixed spinel/rock-salt -> rock-salt wording.
- [8–10] are Mg mechanistic precedents, not direct proof of Mg site/function in the present spinel sample.
- [18,19] are general coherent-nucleation physics and should not be presented as direct proof for this HEO.
- [20] is a close size-effect precedent, but its ~15 nm primary particles must not be equated with the present ball-milled morphology.
- [15,16] support analysis boundaries; they do not establish the microscopic origin of the present transient.

## Manuscript-writing rules for the current revision

- Preserve the Figure 1 -> Figure 5 causal sequence.
- Keep model parameters secondary to the experimental mechanism.
- Avoid first person where unnecessary.
- Avoid "framework", vague "scaling", promotional language, and repeated defensive caveats.
- Do not use "Taken together" as a default transition.
- Do not assign a unique microscopic process to an operational current-off descriptor.
- Do not manufacture missing experimental metadata.
- Mark collaborator-dependent items explicitly as YOO GROUP INPUT REQUIRED.
- Mark local electrochemistry metadata as YOON LAB INPUT REQUIRED.

## 2026-09-20 Figure 4 / Figure 5 conversion update

New experimental cross-check:
- profile-derived cathodic dQ/dV peaks: HEO 0.545 V, BM-HEO 0.589 V, Mg-HEO 0.419 V, BM-Mg-HEO 0.485 V;
- GITT excess peaks: 0.527, 0.618, 0.387, and 0.503 V, respectively;
- absolute mismatch: 18–32 mV.

This makes the conversion assignment an experimental part of the paper rather than a literature-only inference.

Figure 4 main-text role is now: **independent voltage localization of the GITT excess to the first-cycle conversion window + redistribution/suppression map**.

Figure 5 main-text role is now: **reduced conversion-associated internal-state visualization**. The frozen model requires no refitting after the reassignment and preserves the relative onset/peak order. phi is an effective conversion-associated state variable, not a measured phase fraction or complete conversion stoichiometry.

Current journal target: **Advanced Functional Materials**. Keep the manuscript materials-centered; do not turn the conversion reassignment into a methods paper.
