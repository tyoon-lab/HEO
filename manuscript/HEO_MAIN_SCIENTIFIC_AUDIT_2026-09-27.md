# HEO Main Scientific Audit — 2026-09-27

**Scope:** delta audit after PI abstract review, Figure 4 redesign/integration, Mg composition recovery, and conventional-GITT follow-up.

## MUST FIX before submission

### 1. Figures 1–2 collaborator package
Freeze the structural/compositional/morphological evidence before finalizing Section 2.1.

Required:
- final XRD/refinement and phase assignment
- final ICP-OES composition
- final TEM/SAED/EDS/HRTEM indexing
- particle/domain-size statistics if used
- final XPS inclusion decision
- remove the chemically incompatible preliminary CoGa2O4 indexing

### 2. Mg synthesis and nominal composition
Historical ICP shows Mg-HEO3 contains Mg at approximately equimolar abundance with the other principal cations, but the synthesis metadata are incomplete.

Required:
- Mg precursor
- precursor amount / metal ratio
- whether Mg was added or substituted by design
- final nominal formula
- collaborator-confirmed ICP table

Do not write “small Mg substitution/doping” without support.

### 3. Final cell/electrode metadata
Still needed:
- current collector
- vacuum-drying temperature/time
- active loading
- electrode thickness
- separator model
- electrolyte volume
- glovebox H2O/O2
- capacity basis defining 1 C
- exact rate sequence / cycles per rate

### 4. First-cycle dQ/dV source
Current Figure 5 peak positions come from reconstruction of the latest vector voltage-profile plots.

Preferred:
recover the original numerical first-cycle voltage profiles and regenerate dQ/dV.

Fallback:
freeze the vector-reconstruction workflow and provenance explicitly.

### 5. WonATech half-cycle convention
Until the instrument convention is verified, keep neutral language such as “first/second half-cycle” or “first-cycle second-half capacity” where needed.

## RESOLVED since 2026-09-26 audit

### HEO/BM geometric electrode area
The HEO and BM-HEO GITT cells use the same geometric electrode area. The main relative apparent-$D$ comparison can therefore use a common area term.

Remaining caveat:
exact active masses and molar-volume metadata remain desirable if absolute $D$ values are ever reported. Absolute $D$ is not required for the current paper claim.

### Figure 4 architecture
Figure 4 is now scientifically closed for the current round:

- (a) measured GITT definition
- (b) HEO/BM apparent-$D$ versus direct relaxation-rate comparison
- (c) relaxation magnitude–timescale map
- (d) accessible capacity–timescale map

### Abstract
The PI-reviewed abstract is frozen in `HEO_ABSTRACT_LOCK_2026-09-27.md`.

## WORTH FIXING

### Main/SI consistency
When final artwork is assembled, verify all panel references, caption terminology, and first-/second-half-cycle labels against Main v12 and SI v10.

### Cross-composition Mg apparent-D check
The development check is interesting but should remain outside the decisive main evidence unless the composition/density/active-mass prefactor is fully frozen and a state-by-state reproducible audit is committed.

### Figure 7 reproducibility
The microkinetic numerical authority is committed, but the local Figure 7 artwork plotting code was not committed at the time the current draft image was produced. Commit/regenerate the final Figure 7 artwork script before submission.

## OPTIONAL PRECISION

- Replace “relaxation magnitude” with “relaxation voltage-change magnitude” at first use when reader clarity benefits.
- Prefer “conflicting indication/trend” over repeated “ranking” language in narrative prose.
- Keep $t_{63}$ identified as an effective relaxation timescale rather than a microscopic time constant.

## Current claim boundary

The paper supports:

**Ball milling can increase accessible conversion capacity while the conversion-associated current-off relaxation becomes slower, and conventional apparent GITT diffusivity can indicate the opposite fast–slow ordering.**

The Mg result adds:

**A smaller relaxation voltage-change magnitude can coexist with a longer relaxation timescale.**

The microkinetic model supports physical consistency of these combinations, not a unique microscopic assignment.
