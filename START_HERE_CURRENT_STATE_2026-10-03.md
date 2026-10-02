# HEO — Current State, 2026-10-03

## Read this first

This is the authoritative restart point for the HEO manuscript.

A new chat/session should be able to resume from this file alone without a separate handoff.

## Latest scientific decision — polarization/t63 pivot

The manuscript will **not** interpret sample-to-sample accessible capacity as a direct conversion-kinetic speed coordinate.

The former capacity-driven question has been replaced by:

> **Does conversion-region polarization magnitude track the timescale of post-interruption relaxation?**

Raw GITT re-analysis shows that it does not do so universally.

Read next:

`manuscript/HEO_POLARIZATION_T63_PIVOT_LOCK_2026-10-03.md`

Numerical authority:

`modeling/HEO_CONVERSION_POLARIZATION_T63_AUDIT_2026-10-03.md`

`modeling/HEO_CONVERSION_POLARIZATION_T63_SUMMARY_2026-10-03.csv`

The previous Figure 6 reassessment and Q-based model files remain an audit trail, but they are no longer the default manuscript direction.

---

# Paper identity

Working target: **Advanced Functional Materials (AFM)**.

The current working title,

**Mismatch between Capacity and Conversion Kinetics in Spinel High-Entropy Oxide Anodes**

is now **under revision** because capacity is no longer the central kinetic coordinate.

The paper remains a materials/conversion paper using GITT-derived direct response descriptors. It should not become a general GITT-method paper.

---

# Text authorities

Main manuscript authority remains:

`manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`

SI authority remains:

`manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`

These files have **not yet been rewritten** after the polarization/t63 pivot.

Do not treat the capacity-based Section 2.5 / Figure 6 interpretation in v17 as frozen.

---

# New central experimental definitions

For each GITT pulse, define the operational 60-min recoverable polarization:

[
Delta E_{mathrm{pol,60}}
=
|E_{mathrm{rest,60,min}}-E_{mathrm{pulse,end}}|.
]

This compares the end-of-pulse voltage with the subsequent rest endpoint at the same post-pulse lithiation state.

Important terminology boundary:

- use **operational conversion polarization** or **60-min recoverable polarization**;
- do not call this the exact equilibrium overpotential because the 60 min rest endpoint is not proven to be the true equilibrium potential.

The existing slower current-off relaxation magnitude is:

[
Delta E_{mathrm{relax}}
=
|E_{mathrm{rest,60,min}}-E_{mathrm{rest,3,s}}|.
]

The characteristic time (t_{63}) remains defined from the 3 s-to-60 min relaxation.

Thus:
- polarization magnitude = amplitude-like response;
- (t_{63}) = timescale-like response.

---

# First-cycle conversion-window result

Common normalized first-lithiation window: (z=0.40)–0.90.

| Sample | Delta E_pol,60 (mV) | Delta E_relax (mV) | t63 (min) |
|---|---:|---:|---:|
| HEO | 195.9 | 168.5 | 10.37 |
| BM-HEO | 182.6 | 160.5 | 13.02 |
| Mg-HEO | 126.4 | 111.3 | 10.53 |
| BM-Mg-HEO | 148.2 | 135.2 | 12.70 |

The re-parsed Delta E_relax and t63 values reproduce the existing v17 numerical authority, validating the pulse/rest segmentation.

## Material-modification directions

HEO -> BM-HEO:
- polarization slightly decreases: ratio 0.932;
- t63 increases: ratio 1.256.

HEO -> Mg-HEO:
- polarization strongly decreases: ratio 0.645;
- t63 is nearly unchanged: ratio 1.015.

Mg-HEO -> BM-Mg-HEO:
- polarization increases: ratio 1.172;
- t63 increases: ratio 1.207.

Therefore:

> **Conversion-region polarization magnitude and post-interruption relaxation timescale do not collapse onto one material-independent fast–slow coordinate.**

Do not use a four-sample Pearson/Spearman coefficient as the central evidence. The directional material contrasts are the primary result.

---

# Conversion localization under the new definition

Using the same first-cycle exponential-background protocol as the existing Figure 5 analysis, the background-subtracted Delta E_pol,60 excess gives:

| Sample | excess peak (mV) | z_peak | rest-end V at peak (V) | cathodic dQ/dV peak (V) | offset |
|---|---:|---:|---:|---:|---:|
| HEO | 72.5 | 0.754 | 0.537 | 0.545 | -7.5 mV |
| BM-HEO | 49.3 | 0.671 | 0.618 | 0.589 | +28.4 mV |
| Mg-HEO | 16.9 | 0.792 | 0.387 | 0.419 | -31.8 mV |
| BM-Mg-HEO | 22.0 | 0.661 | 0.503 | 0.485 | +18.0 mV |

All nominal offsets remain within approximately 32 mV.

Therefore the previous Figure 5 localization logic survives the pivot:

> **The additional recoverable polarization is localized to the conversion region, but its magnitude does not uniquely determine the relaxation timescale.**

---

# Capacity role after the pivot

Figure 3 can retain capacity/performance data.

Safe statements:
- ball milling increases accessible capacity;
- Mg incorporation decreases accessible capacity;
- the material modifications therefore change electrochemical utilization/performance.

Do NOT infer:
- larger capacity = faster conversion kinetics;
- smaller capacity = slower conversion kinetics;
- sample-to-sample capacity is determined by terminal polarization;
- a polarization-limited cutoff mechanism explains the capacity ordering.

The terminal-polarization audit already showed that pulse excursion decreases, rather than grows, toward the end of first lithiation.

Authority:

`modeling/HEO_TERMINAL_POLARIZATION_AUDIT_2026-10-03.md`

---

# Figure architecture now under revision

## Figures 1–2

Materials structure/composition/morphology.

No change in role.

## Figure 3

Electrochemical performance and accessible capacity.

**Outcome only; no direct kinetic inference.**

## Figure 4

Should become the direct descriptor figure.

Preferred architecture to test:

(a) representative GITT pulse/rest definition:
- E_pulse,end
- E_rest,3s
- E_rest,60min
- Delta E_pol,60
- Delta E_relax
- t63

(b) state-resolved Delta E_pol,60 versus z

(c) state-resolved t63 versus z

(d) polarization–t63 observable map with material-modification arrows

Exact artwork is not yet frozen.

## Figure 5

Retain conversion localization.

Recast from a relaxation-only hump toward the broader **conversion-associated polarization/recovery feature** if this improves clarity.

## Figure 6

The preferred Main Figure 6 is now a **fully experimental cycle-history robustness test**.

Raw cycle 1–3 re-analysis reproduces the previous cycle-resolved Delta E_relax and t63 authorities and extends them to Delta E_pol,60.

Cycle 3 / cycle 1:
- HEO: polarization 0.766; t63 0.923
- BM-HEO: polarization 0.772; t63 0.870
- Mg-HEO: polarization 1.216; t63 0.905
- BM-Mg-HEO: polarization 1.019; t63 0.844

The Mg trajectory is particularly strong: polarization increases by ~22% while t63 decreases by ~9.5% within the same material.

Read:
- `manuscript/HEO_FIGURE6_EXPERIMENTAL_HISTORY_LOCK_2026-10-03.md`
- `modeling/HEO_CYCLE_RESOLVED_POLARIZATION_T63_AUDIT_2026-10-03.md`
- `modeling/HEO_CYCLE_RESOLVED_POLARIZATION_T63_SUMMARY_2026-10-03.csv`

The former Q-based R2/R3 model is historical/optional SI material, not the preferred Main Figure 6.

---

# Conventional GITT Dapp

The state-matched HEO/BM result remains valid:

- median Dapp,BM/Dapp,HEO = 1.7817;
- direct relaxation is slower in BM at 35/37 states.

This can remain a secondary diagnostic or move entirely to SI.

Do not let the Dapp disagreement become the central paper identity.

Authority:

`modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md`

`modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`

---

# Former Figure 6 model status

Historical files:

`manuscript/HEO_FIGURE6_REASSESSMENT_LOCK_2026-10-03.md`

`modeling/HEO_FOUR_STEP_HOMOGENEOUS_MICROKINETIC_AUDIT_2026-09-28.md`

`modeling/HEO_FOUR_STEP_LOCAL_SENSITIVITY_2026-10-03.csv`

`modeling/HEO_FOUR_STEP_VOLTAGE_HEADROOM_AUDIT_2026-10-03.md`

The finite R2/R3 Q-up/t63-up result remains a valid mathematical existence test, but it is no longer required to explain the experimental paper.

Do not map ball milling onto R2/R3.

---

# Current minimum claim

Preferred central statement:

> **Material modification changes conversion-region polarization magnitude and post-interruption relaxation timescale in distinct ways, showing that the two responses do not collapse onto a single kinetic fast–slow coordinate.**

Supporting localization statement:

> **The polarization/recovery feature is localized to the conversion region by its correspondence with the cathodic differential-capacity response.**

No microscopic cause is assigned yet.

---

# Remaining submission blockers

1. Final Figures 1–2 collaborator structural/compositional package.
2. Final Mg synthesis recipe and collaborator-verified nominal/ICP composition.
3. Missing cell/electrode metadata:
   - current collector
   - drying temperature/time
   - active loading
   - electrode thickness
   - separator
   - electrolyte volume
   - glovebox H2O/O2
   - exact 1 C basis and rate sequence
4. Original numerical first-cycle voltage profiles if recoverable.
5. Final XPS inclusion/exclusion decision.
6. Recheck pristine/post-cycle SEM placement.
7. Final numbering/reference audit after structural SI insertion.

---

# Immediate next task

**Do not rewrite Main v17 yet.**

Next:

1. rebuild the Figure 4 concept around Delta E_pol,60 and t63;
2. decide whether Figure 5 should display the new background-subtracted polarization excess directly;
3. build/test the experimental cycle-history Figure 6 artwork using the newly locked C1–C3 polarization/t63 result;
4. decide whether conventional Dapp stays in Main or moves to SI;
5. only after Figures 4–6 artwork is frozen, revise Abstract, Introduction endpoint, Sections 2.3–2.5, Conclusions, captions, and SI consistently.

Working principle:

**Capacity is an outcome. Polarization magnitude and relaxation timescale are the direct kinetic-response coordinates. Experiment first; mechanism only where independently supported.**
