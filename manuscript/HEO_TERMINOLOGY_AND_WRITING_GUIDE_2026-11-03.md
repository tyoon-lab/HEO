# HEO terminology and PI writing guide — 2026-11-03

## PI-approved core definitions (AUTHORITATIVE FOR WRITING, NOT AN EXPERIMENTAL CLAIM)

1. **Overlapping reaction processes** = the chemical and structural processes involved in conversion lithiation (Li uptake, transition-metal cation reduction, parent-oxide destabilization/reconstruction, evolution of metal/Li₂O products). Their contributions may overlap in lithiation charge/potential, and relative prominence may change during lithiation. This is the **chemistry/physics** concept.
2. **Electrochemical regions (R1–R4)** = intervals of lithiation *defined by observable electrochemical GITT signatures*, specifically coordinated changes in post-pulse relaxation amplitude ΔErest, operational characteristic recovery time t63, and 60-min rest-end voltage. These are **measured coordinate intervals**, not four chemically isolated elementary steps, a validated phase diagram, or universal reference potentials.
3. **Dominant reaction processes** = the chemically meaningful processes that are relatively more influential within a given electrochemical region, inferred from its signatures **and supported by established operando/ex situ literature**. They may overlap across region boundaries. Stage-specific chemical state assignments are interpretation, not direct structural measurement of these four samples.

**Term hierarchy:** chemical mechanisms = overlapping reaction processes; experimental division = electrochemical regions; literature-guided physical interpretation = dominant reaction processes. Prefer **region** over **stage** for R1–R4. Use multistep conversion only when directly describing preceding literature, not as the paper's core formal division.

## PI writing preferences applied to HEO manuscript
- Avoid sentence-opening or summary **“Together,”**.
- Favor **affirmative, direct sentences** instead of repetitive constructions with “not”, “do not”, “without”, “rather than”, or generic defensive phrasing. Necessary scientifically specific qualifications can remain where important for accuracy, preferably in Results/Methods/internal review notes.
- Neutral and objective overall; make a reasonably bold hypothesis where supported by specific literature; do not overclaim experimental phase assignment.
- Avoid vague language: “controlling lithium storage”, “linking a materials variable to a reaction outcome”, “across successive reaction states”, “along a continuous voltage–capacity profile”, “corresponding response”.
- Explicit chemical and electrochemical nouns; simple transitions and rhythmic sentence structure. Avoid first-person and manuscript titles starting with “Through”.

## Current preferred Introduction (four paragraphs)
P1 HEO background and operando/ex situ evidence for overlapping cation reductions/reconstruction → P2 processing/composition modifications can affect those processes differently, overall capacity fails to allocate signed changes among portions of lithiation → P3 broad voltage plateau and overlapping dQ/dV, directly measured GITT relaxation amplitude/time/rest-end voltage offer changes sufficient to define electrochemical **regions**, Dapp assumptions are problematic → P4 crossed BM/Mg measurements localize region charge and suggest materials-design directions.

Review candidate in [HEO_INTRO_CONSOLIDATED_REACTION_PROCESSES_ELECTROCHEMICAL_REGIONS_2026-11-03.md](HEO_INTRO_CONSOLIDATED_REACTION_PROCESSES_ELECTROCHEMICAL_REGIONS_2026-11-03.md).

## Quantitative and physical control notes (internal)
- ΔErest = absolute voltage recovery from 3s to 3600s during GITT rest; t63 is operational first time to reach 63.2% of the 3s–60min relaxation. Does not represent a unique diffusion time or rate constant.
- L1/L3/L4 are trend landmarks. Different signals can have offset extrema; do not require coincident minima in all four samples. 
- R2: literature-guided conversion onset, oxide reconstruction and overlapping early metal/Li₂O formation; R3: later continued reduction and product development, overlapping with R2; R1 early uptake; R4 deep lithiation.
- In accepted source data BM ΔR2 +166.7 / +133.3 mAh g⁻¹, Mg ΔR3 −266.7 / −283.3 mAh g⁻¹, nominal regional GITT charge (not GCD). BM also reduces R3; avoid claiming that only R2 changes.
- Current kept Abstract, Main v29 Word and SI v17 **remain unchanged** until deliberate integration.
