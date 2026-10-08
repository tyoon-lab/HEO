# HEO Reaction-Fingerprint Story Lock — 2026-10-08

## Status

This file records the newly adopted manuscript story after the 2026-10-03 polarization/t63 pivot and the subsequent region-resolved GITT analysis.

The prior capacity–kinetics mismatch manuscript architecture is no longer the default Main-text direction.

## New paper identity

Working title:

**GITT Relaxation Fingerprints Resolve Material-Specific Perturbations of Conversion Lithiation in Spinel High-Entropy Oxide Anodes**

Working target remains **Advanced Functional Materials (AFM)** unless journal positioning changes later.

The manuscript remains a materials/conversion paper. GITT is the diagnostic used to map material-specific perturbations; the paper should not become a generic GITT-method paper.

## Central scientific chain

The new story is:

1. Conventional electrochemistry establishes how much lithiation is accessible in each material.
2. State-resolved GITT relaxation fingerprints divide first lithiation into reproducible electrochemical regimes.
3. The regions are defined from electrochemical fingerprints first, then assigned broad physical meaning using Q–OCV behavior and established conversion literature.
4. Ball milling and Mg incorporation perturb different aspects of the conversion response.
5. The 2 × 2 comparison separates reaction accessibility from relaxation persistence.

Preferred central statement:

> **Ball milling redistributes where conversion proceeds and prolongs the relaxation of the resulting reconstructed states, whereas Mg incorporation primarily limits access to the late conversion-associated state.**

Broader conceptual statement:

> **Accessible reaction extent and relaxation persistence are related but non-equivalent material properties of reconstructive conversion.**

## Fingerprint descriptors

Primary state-resolved descriptors:

- `t63`: first time required to complete 63.2% of the measured 3 s-to-60 min current-off voltage relaxation; no single-exponential fit is assumed.
- `Delta E_rest = |E_rest,60min - E_rest,3s|`: operational current-off relaxation magnitude.
- relaxed-voltage / Q–OCV profile: 60 min rest-end voltage as the state coordinate.

`t63` is treated as the primary timescale fingerprint.

`Delta E_rest` is an amplitude-like descriptor that can contain kinetic, thermodynamic-slope, reconstruction, and other contributions; it is not treated as a pure elementary overpotential.

## Reaction landmarks and regions

The current region skeleton is:

- `L1`: early transition out of the initial response.
- `L3`: central conversion-associated landmark; t63 minimum/trough accompanied by a nearby Delta E_rest minimum and conversion-centered Q–OCV response.
- `L4`: end of the broad relaxed-voltage plateau / transition to the steeper post-plateau branch.

These define:

- `R1 = start -> L1`
- `R2 = L1 -> L3`
- `R3 = L3 -> L4`
- `R4 = L4 -> end`

Intermediate extrema such as the earlier L2 and terminal L5 remain within-region kinetic landmarks and are not promoted to separate reaction boundaries.

### Physical assignments

Assignments are made **after** electrochemical region definition.

- **R1:** early lithiation / pre-main-conversion processes.
- **R2:** conversion onset and progression; spinel destabilization and progressive multication reduction are literature-consistent interpretations.
- **R3:** late conversion-associated reconstructed-state evolution; continued conversion/reconstruction before the relaxed-voltage plateau ends.
- **R4:** post-main-conversion / post-plateau deep lithiation; residual/final conversion-like processes and deeper lithiation of reconstructed products.

Do not assign one specific cation or one unique elementary reaction to an R1–R4 boundary without direct evidence.

## Main 2 × 2 result

### Ball milling

In both Mg-free and Mg-containing comparisons, ball milling produces the same qualitative regional redistribution:

- `R1 up`
- `R2 up`
- `R3 down`
- `R4 up`

and the same relaxation-timescale direction:

- `t63` decreases in R1;
- `t63` increases over R2–R4.

Manuscript-facing interpretation:

> Ball milling does not uniformly accelerate lithiation. It broadens and redistributes the accessible conversion response and makes post-onset relaxation more persistent.

Materials-level origin should be linked only to collaborator-verified structural evidence. Disorder, amorphization, particle/domain refinement, interface density, and local-environment diversity remain candidate origins until Figures 1–2 are frozen.

### Mg incorporation

In both unmilled and milled comparisons, Mg incorporation most strongly suppresses **R3** reaction extent.

Key feature:

- R3 accessible extent decreases strongly.
- The remaining R3 `t63` changes only weakly.
- Delta E_rest is generally reduced in the unmilled Mg comparison.
- The relaxed-voltage response shifts to lower voltage.

Manuscript-facing interpretation:

> Mg primarily suppresses access to the late conversion-associated state rather than simply slowing the relaxation of the fraction that remains accessible.

This is consistent with literature describing Mg as an electrochemically less active / oxide-stabilizing component, but the present work does not uniquely assign Mg site occupancy or bond-level stabilization.

### Combined BM + Mg

Mg limits late-conversion accessibility; BM redistributes the remaining accessible pathway toward R1/R2/R4 while preserving the longer R2–R4 relaxation tendency.

Do not call BM and Mg perfectly orthogonal or fully independent. The capacity partition is highly regular, but relaxation-amplitude interactions remain.

## Sensitivity audit — INTERNAL ONLY

Boundary sensitivity was tested by shifting L1, L3, and L4 independently by ±1 GITT step for each paired sample comparison (729 combinations per pair).

Internal robustness result:

- BM regional capacity pattern `R1+, R2+, R3-, R4+`: 100% robust with and without Mg.
- BM t63 pattern `R1-, R2+, R3+, R4+`: 100% robust with and without Mg.
- Mg-induced R3 capacity loss: 100% negative and 100% the most negative region in both BM states.
- R3 dominates the Mg capacity loss in 100% of unmilled comparisons and 99.45% of milled comparisons.
- Mg-induced R3 t63 change remains small (|Delta t63| <= 1.5 min) in 100% of tested boundary combinations.

Decision: keep this audit as internal reviewer-defense information for now. Do not add it to Main or SI unless needed.

## Region-capacity caveat

Regional capacity is currently derived from the GITT protocol (`100 mA g^-1 × 600 s` per pulse) and is valid in units of mAh g^-1 for the GITT current normalization.

However, the full GITT endpoint and separately measured first-cycle GCD capacity differ by an approximately common normalization factor in HEO/BM-HEO.

Therefore:

- use region **fractions (%)** as the primary partition metric;
- call absolute values `protocol-derived GITT specific capacity` if shown;
- do not present them as exact replacements for the independently measured GCD capacities;
- direct raw-current integration should replace the setpoint-derived absolute values if final publication requires exact regional mAh g^-1 values.

## New Figure architecture

### Figures 1–2
Materials structure/composition/morphology.

Role: establish what BM and Mg physically change before electrochemistry.

### Figure 3
**Material modifications alter accessible first-lithiation response.**

Role: conventional electrochemical outcome only.

- first-cycle voltage profiles;
- lithiation/delithiation capacity summary;
- distributed capacity gain/loss across the voltage trajectory;
- no direct inference that larger capacity means faster conversion kinetics.

### Figure 4
**GITT relaxation fingerprints resolve four lithiation regimes.**

Reference HEO:

- t63(z)
- Delta E_rest(z)
- Q–OCV / relaxed voltage
- L1/L3/L4 and R1–R4
- broad literature-supported physical assignment after electrochemical definition.

### Figure 5
**Ball milling redistributes conversion extent and prolongs post-onset relaxation.**

HEO vs BM-HEO:

- three-signal comparison;
- region-resolved capacity fraction;
- region-resolved median t63;
- physical interpretation schematic constrained by final structural data.

### Figure 6
**Mg selectively suppresses late-conversion accessibility and closes the 2 × 2 comparison.**

- HEO vs Mg-HEO;
- Mg-HEO vs BM-Mg-HEO;
- R3-selective Mg effect;
- final mechanistic synthesis schematic.

## Manuscript Results architecture

1. **2.1 Structural and morphological perturbations introduced by ball milling and Mg incorporation**
2. **2.2 Ball milling and Mg incorporation alter accessible lithiation in opposite ways**
3. **2.3 GITT relaxation fingerprints resolve four lithiation regimes**
4. **2.4 Ball milling redistributes the conversion response and prolongs post-onset relaxation**
5. **2.5 Mg incorporation selectively limits the late conversion-associated response**
6. **2.6 The 2 × 2 comparison separates reaction accessibility from relaxation persistence**

## Literature-positioning decision

Existing literature already establishes:

- multistage/reconstructive HEO conversion;
- element-dependent conversion sequences in related spinel HEOs;
- ball-milling/particle-size effects on HEO electrochemical performance;
- Mg/inactive-cation stabilization concepts;
- GITT apparent-diffusivity limitations;
- SOC-dependent voltage-relaxation time constants in insertion-type NMC811 cells.

Therefore, do **not** claim:

- discovery of four previously unknown conversion reactions;
- first use of state-dependent voltage relaxation;
- first observation that Mg can stabilize an HEO;
- first evidence that ball milling can improve HEO capacity/performance.

The defensible novelty is:

> **A GITT-relaxation reaction-state map is used to identify where different materials modifications perturb a multistage conversion reaction, separating changes in reaction accessibility from changes in relaxation persistence.**

## Stories explicitly retired from Main

### Retired: capacity as a direct kinetic-speed coordinate
Do not infer that higher accessible capacity proves faster conversion kinetics or that lower capacity proves slower kinetics.

### Retired: capacity–kinetics mismatch as paper identity
The former headline `higher capacity + slower relaxation` remains a valid observation but is no longer the manuscript's central scientific identity.

### Retired: polarization–t63 non-equivalence as final endpoint
The 2026-10-03 pivot established an important diagnostic boundary, but the new region-resolved fingerprint story is more specific and physically informative. Polarization/t63 non-equivalence remains supporting context rather than the paper endpoint.

### Retired: conventional Dapp conflict as Main novelty
The HEO/BM state-matched conventional GITT Dapp disagreement remains valid and can be retained in SI or a short discussion, but it should not define the paper.

### Retired: four-step microkinetic model as Main Figure 6
The old four-step model and R2/R3 existence tests are historical/optional SI material. They should not be mapped onto BM or Mg and are not required for the current physical interpretation.

### Retired: exact microscopic four-step assignment
Do not use the old O/I/J/K/C four-step sequence as the experimental reaction-region definition.

## Methods status

Main analysis method now includes:

- GITT: 10 min pulse + 60 min rest, 100 mA g^-1;
- common 3 s post-interruption reference due to different early sampling resolutions;
- t63 from 3 s-to-60 min relaxation;
- Delta E_rest from 3 s-to-60 min magnitude;
- 60 min rest-end voltage as relaxed state coordinate;
- fingerprint-derived L1/L3/L4 region boundaries;
- region-resolved capacity fractions and median descriptors.

Supporting/internal methods:

- conventional GITT Dapp audit;
- alternate relaxation percentiles;
- ±1-step region-boundary sensitivity;
- old four-step microkinetic existence tests;
- terminal-polarization audit.

## Current manuscript authority

New Main-text draft:

`manuscript/HEO_MANUSCRIPT_V18_REACTION_FINGERPRINT_2026-10-08.md`

The previous v17 and SI v14 remain historical authorities for material/method details not yet ported, but their capacity–kinetics and four-step-model narrative is superseded by this story lock.

## Remaining blockers

1. Final collaborator Figures 1–2 structural/compositional package.
2. Final Mg synthesis recipe and verified nominal/ICP composition.
3. Missing cell/electrode metadata.
4. Original numerical first-cycle GCD profiles if recoverable.
5. Final XPS inclusion decision.
6. Final exact regional absolute-capacity normalization if needed.
7. Final Main/SI synchronization and reference audit after line-by-line manuscript review.
