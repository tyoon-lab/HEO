# HEO — Current State, 2026-10-08

## Read this first

This is the authoritative restart point for the HEO manuscript.

A new chat/session should be able to resume from this file alone without a separate handoff.

## New manuscript direction — reaction-fingerprint mapping

The manuscript has moved beyond the 2026-10-03 polarization/t63 pivot.

The adopted paper identity is now:

> **Use state-resolved GITT relaxation fingerprints to divide first lithiation into electrochemically distinct reaction regions, assign broad physical meaning by integrating the relaxed-voltage response with established HEO conversion literature, and determine how ball milling and Mg incorporation perturb those regions differently.**

Working title:

**GITT Relaxation Fingerprints Resolve Material-Specific Perturbations of Conversion Lithiation in Spinel High-Entropy Oxide Anodes**

Working target: **Advanced Functional Materials (AFM)**.

## Read next

1. `manuscript/HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md`
2. `manuscript/HEO_MANUSCRIPT_V18_REACTION_FINGERPRINT_2026-10-08.md`
3. `references/HEO_REACTION_FINGERPRINT_LITERATURE_POSITIONING_2026-10-08.md`

The old v17 manuscript and v14 SI remain historical sources for details not yet ported, but their capacity–kinetics/four-step-model narrative is no longer authoritative.

## Central result

Preferred manuscript-facing statement:

> **Ball milling redistributes where conversion proceeds and prolongs the relaxation of the resulting reconstructed states, whereas Mg incorporation primarily limits access to the late conversion-associated state.**

Broader concept:

> **Accessible reaction extent and relaxation persistence are related but non-equivalent material properties of reconstructive conversion.**

## Core descriptors

For each GITT pulse/rest step:

- `Delta E_rest = |E_rest,60min - E_rest,3s|`
- `t63` = first time required to complete 63.2% of the measured 3 s-to-60 min relaxation
- `E_rest,60min` = relaxed-voltage / Q–OCV state coordinate

Primary fingerprint: **t63**.

Delta E_rest is a response amplitude, not a pure microscopic overpotential.

## Region definition

Three major landmarks define four regions:

- `L1`: early transition out of the initial response
- `L3`: central conversion-associated landmark
- `L4`: end of the broad relaxed-voltage plateau / start of the steeper post-plateau branch

Regions:

- **R1:** start -> L1
- **R2:** L1 -> L3
- **R3:** L3 -> L4
- **R4:** L4 -> end

Intermediate extrema L2/L5 are internal kinetic landmarks, not reaction boundaries.

## Broad physical assignment

Assignment is made only **after** fingerprint-based electrochemical definition.

- **R1:** early lithiation / pre-main-conversion
- **R2:** conversion onset and progression
- **R3:** late conversion-associated reconstructed-state evolution
- **R4:** post-main-conversion / post-plateau deep lithiation

Do not assign exact individual-cation reactions to the boundaries without direct evidence.

## 2 × 2 material result

### Ball milling effect

Repeated with and without Mg:

- R1 up
- R2 up
- R3 down
- R4 up
- t63 down in R1
- t63 up in R2–R4

Interpretation:

> BM broadens and redistributes the accessible conversion response and makes post-onset relaxation more persistent.

Link to disorder/amorphization/interface diversity only to the extent supported by final Figures 1–2.

### Mg effect

Repeated with and without BM:

- strongest loss of accessible reaction extent occurs in R3
- R3 t63 changes only weakly
- relaxed voltage shifts lower
- relaxation magnitude is reduced strongly in the unmilled comparison

Interpretation:

> Mg primarily suppresses access to the late conversion-associated state rather than simply slowing the remaining R3 relaxation.

This is consistent with known inactive/oxide-stabilizing Mg concepts but does not prove a unique Mg site or bond-level mechanism.

## Internal sensitivity audit — do not publish yet

L1/L3/L4 were independently shifted ±1 GITT step for each sample pair (729 combinations per comparison).

Robustness:

- BM `R1+, R2+, R3-, R4+` capacity pattern: 100% with and without Mg
- BM `R1-, R2+, R3+, R4+` t63 pattern: 100% with and without Mg
- Mg R3 capacity decrease: 100%
- Mg R3 = most negative capacity change: 100%
- R3 dominates Mg capacity loss: 100% unmilled, 99.45% milled
- Mg R3 |Delta t63| <= 1.5 min: 100%

Decision: internal reviewer-defense information only unless later needed.

## Capacity normalization caveat

Region absolute capacity is currently protocol-derived from the GITT setpoint (100 mA g^-1 × 600 s per pulse).

The GITT total and separate GCD first-lithiation capacity show a common normalization mismatch in HEO/BM-HEO.

Therefore:

- region **fraction (%)** is the preferred Main metric;
- absolute regional values, if used, must be labeled `protocol-derived GITT specific capacity`;
- direct raw-current integration should be used if exact publication-grade absolute regional mAh g^-1 is required.

## Figure architecture — current lock

### Figures 1–2
Materials structure/composition/morphology.

### Figure 3
**Material modifications alter accessible first-lithiation response.**

Conventional electrochemical outcome only; no kinetic-speed inference from capacity.

### Figure 4
**GITT relaxation fingerprints resolve four lithiation regimes.**

Reference HEO; t63, Delta E_rest, Q–OCV; L1/L3/L4; R1–R4; literature-supported physical assignment.

### Figure 5
**Ball milling redistributes conversion extent and prolongs post-onset relaxation.**

HEO vs BM-HEO; regional capacity fraction; regional median t63; structural interpretation constrained by Figures 1–2.

### Figure 6
**Mg selectively suppresses late-conversion accessibility and closes the 2 × 2 comparison.**

HEO vs Mg-HEO + Mg-HEO vs BM-Mg-HEO + final conceptual synthesis.

## Results architecture

- 2.1 Structural and morphological perturbations introduced by ball milling and Mg incorporation
- 2.2 Ball milling and Mg incorporation alter accessible lithiation in opposite ways
- 2.3 GITT relaxation fingerprints resolve four lithiation regimes
- 2.4 Ball milling redistributes the conversion response and prolongs post-onset relaxation
- 2.5 Mg incorporation selectively limits the late conversion-associated response
- 2.6 The 2 × 2 comparison separates reaction accessibility from relaxation persistence

## Literature gate

Already established in prior work:

- multistage/reconstructive HEO conversion
- progressive cation reduction / conversion products in related spinel HEOs
- ball-milling/particle-size effects on HEO electrochemical performance
- Mg/inactive-cation stabilization concepts
- conventional GITT Dapp limitations
- state-dependent voltage-relaxation time constants in NMC811

Therefore the novelty is **not** discovery of these pieces individually.

Current novelty:

> **Use of a GITT-relaxation reaction-state map to identify where different materials modifications perturb conversion lithiation, separating reaction accessibility from relaxation persistence.**

## Retired / superseded Main stories

### Capacity–kinetics mismatch
Still true as an observation but no longer the paper identity.

### Capacity as direct kinetic-speed coordinate
Rejected.

### Polarization–t63 non-equivalence as final endpoint
Still valid supporting context, but superseded by the more specific region-resolved fingerprint story.

### Conventional Dapp conflict as Main novelty
Move to SI or brief secondary discussion.

### Four-step microkinetic model as Main Figure 6
Retired from Main. Keep only as historical/optional SI existence-test material.

### Exact four-step microscopic reaction assignment
Do not map old model R1–R4 onto experimental fingerprint R1–R4. The experimental regions are defined independently.

## New manuscript authority

Main draft:

`manuscript/HEO_MANUSCRIPT_V18_REACTION_FINGERPRINT_2026-10-08.md`

Story decision authority:

`manuscript/HEO_REACTION_FINGERPRINT_STORY_LOCK_2026-10-08.md`

Literature positioning:

`references/HEO_REACTION_FINGERPRINT_LITERATURE_POSITIONING_2026-10-08.md`

Historical text authorities:

- `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`
- `manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`

Use those only for unported experimental/method/SI details, not for the current scientific story.

## Immediate next task

PI line-by-line review should start from the **v18 Abstract** as the control surface, following the Yoon Lab Publication Toolkit abstract-first protocol.

After provisional Abstract lock:

1. propagate changes into Introduction;
2. review Results section-by-section against Figure 3–6 architecture;
3. freeze Figure captions and physical assignment wording;
4. rebuild SI around robustness/secondary analyses;
5. final reference and metadata audit.

## Remaining blockers

1. Final Figures 1–2 collaborator structural/compositional package.
2. Final Mg synthesis recipe and collaborator-verified composition.
3. Missing cell/electrode metadata.
4. Original numerical first-cycle GCD profiles if recoverable.
5. XPS inclusion/exclusion decision.
6. Exact regional absolute-capacity normalization if needed.
7. Full Main/SI synchronization after PI line-by-line review.
