# HEO — Simulation / FEM decision gate following C1–C3 GITT discussion (2026-11-16)

> **Open PI question (2026-11-14):** “시뮬레이션을 추가하는건 어떤가 fem이나?” — Is it worthwhile to add simulation, perhaps FEM?
>
> **STATUS: NOT DECIDED, NOT RUN.** The user requested on 2026-11-16 to save the accumulated discussion to GitHub. This note preserves the simulation question and proposes a lean evaluation plan. It **does not** assert that any simulations have been performed, fitted, validated, approved for the HEO manuscript or added to its figures.

## Scientific motivation (from source GITT analysis)

- First lithiation begins in pristine spinel and shows complex t63 trends/humps, additional ~342–425 mAh/g charge relative to subsequent lithiation, and larger/slower full-window voltage recovery.
- Second and third lithiation show almost identical QOCV- and time-dependent relaxation profiles, with a persisting |ΔErest| hump and QOCV-derived differential-capacity feature around ~0.9 V. The t63 first-cycle hump largely disappears while amplitude hump persists.
- First delithiation already resembles later delithiation in normalized QOCV-capacity shape but differs by a ~60–120mV offset and retains kinetic differences.
- First-lithiation R1–R4 defined by changes of t63 have meaningful **operational electrochemical boundaries**. Full normalized E(t) varies **smoothly** around R2→R3. This does not establish discrete chemical phases.
- A shared hump *could* track a broadly recurring predominant process under different sample/cycle contributions; Mg affects later-cycle local QOCV charge fraction and |ΔErest| amplitude, but its initial R3 effect cannot yet be uniquely tagged to the later ~0.9V region.
- The core modeling question is **whether one coherent history-dependent reaction / transport model reproduces all of these observations**, rather than whether a FEM simulation can draw a plausible first-cycle GITT curve.

## Recommended hierarchy: physical hypothesis before spatial simulation

### Level 0 — null/reduced phenomenological model (first comparison, no FEM)

Represent GITT rest response as a smooth, nonnegative mixture of a few exponentials with **cycle-independent characteristic times** and potential-dependent *weights*; allow a generic voltage-capacity curve and one uniform first-cycle extra charge. Ask whether this already reproduces first-cycle and later-cycle response differences. Constrain model complexity and use same parameters outside training windows; otherwise a flexible exponential model can overfit to tiny normalized RMSE without mechanism identification.

Competing simple explanation: the disappearance of t63 hump can occur from gradual redistribution of relaxation weights while the |ΔErest| hump persists; a distinct new phase or discrete R boundary may be unnecessary.

### Level 1 — minimal history-dependent reaction model (preferred first mechanistic attempt)

Treat first-cycle pristine spinel-specific evolution and subsequent conversion as separate **state variables**, avoiding hard claims about their microscopic unique identity:

- Structural variable \`s(t)\`: fraction or progress proxy for **pristine spinel → reconstructed oxide**, largely advanced during C1 lithiation and incompletely reversed on delithiation. This is a *hypothesis* linked to published conversion oxide phase pathways, not direct microscopy proof in the four HEO samples.
- Repeatable conversion-state variable \`c(t)\`: electrochemical conversion/intermediate-oxide ↔ metal/Li2O-related response, with finite overpotential and possible hysteresis; do not force identical forward/backward voltages.
- Optional reversible/interfacial storage channel or irreversible loss channel only if required by training-free predictions; avoid unconstrained number of states.
- Measured electrode \`V(t)\` is driven by a coupled equilibrium-like QOCV/history relation and one or two kinetic/transport overpotentials. Predict **full pulse+rest E(t)**, not merely fit t63 and |ΔErest| separately.

**Ask whether fixed or lightly history-dependent parameters**, once fitted on selected C1 data and independent structural priors, predict C1 delithiation and C2/C3 lithiation/delithiation trajectories. More importantly, test the model **against null Level 0** using withheld data and equal observables.

### Level 2 — one-dimensional particle transport (only if Level 1 inadequate)

Spherical or effective one-dimensional radial transport \`∂c/∂t = ∇·(D(c,s)∇c)\` plus interfacial kinetics; reconstruct with finite surface kinetics and a history-dependent reaction pathway. A change of **particle size / agglomerate geometry under milling** may matter, but the measured BET gas-accessible surface area is **not equivalent to electrochemically active area**. Mg incorporation changes composition and potentially equilibrium-potential landscape; its exact lattice substitution site was **not demonstrated** by Mg 1s XPS alone. Fit only identifiable parameter combinations.

Numerical implementation can use Python SciPy \`solve_ivp\` with radial finite volumes / method of lines, or a relevant PyBaMM model if appropriate. These are **not automatically FEM**; a 1D finite-volume or PDE solver may be enough to falsify an alternative.

### Level 3 — 2D/3D FEM or porous electrode (conditional, not default)

Use COMSOL, FEniCSx/dolfinx or another FEM package only if a **specific spatial heterogeneity question** cannot be answered by Level 1/2:

- particle-size distributions, core–shell conversion fronts, interfacial polarization, or morphology-driven tortuous transport;
- contrast pristine agglomerates vs milled fines with *measured* size distribution, shape, loadings, electrode porosity/thickness and current density;
- examine whether spatial relaxation changes produce t63 extrema with smooth full-rest profiles and why |ΔErest| hump recurs after first cycle.

Do **not** add FEM merely to visually recreate R1–R4 or a hump. A finite-element result conditioned on arbitrary \(D\), kinetic parameters and morphology does not uniquely assign a reaction.

## Prioritized, discriminating predictions

A minimal simulator is useful only if it explains, **with the same calibrated physical assumptions**, more than one of the following:
1. C1 nonmonotonic \`t63(Q)\`, then smoother, mostly increasing C2/C3 \`t63(Q)\`.
2. Persistence of a **|ΔErest| hump** and broad ~0.90V C2/C3 QOCV differential-capacity feature despite disappearance of C1 t63 hump.
3. Actual normalized 3–3500/3600s rest E(t) shift from C1 slower recovery to C2/C3 faster recovery; C2≈C3 in the same cell.
4. First delithiation already similar to C2/C3 in QOCV(shape), but requiring ~60–120mV potential-axis offset and showing residual t63/|ΔErest| difference.
5. Directionally correct **matched BM gains in first R2**, **matched Mg reductions in first R3**, and preserved net gain/loss in C2/C3, **without** forcing empirical R1–R4 to be discrete chemical phases.
6. Parameter sensitivity: are observed effects explained almost entirely by generic D/area/polarization scaling, or is an *initial-only restructuring state* required? Include a no-history control to challenge that narrative.
7. Identifiability: can different parameter sets predict the same GITT current-pulse/rest curves but diverge on subsequent delithiation or cycling? If so, describe limitations and favor model comparisons, not definitive microscopic parameter estimates.

**Prediction must be assessed blind to the target holdout**. Recommended calibration on C1 lithiation plus selected independent prior literature/physical characterization; test C1 delithiation and at least C2/C3 without re-fitting per-cycle free amplitude/time curves. Alternatively calibrate on one material and test another with measured intervention parameters only. If the model merely refits all observed cycles, it is illustrative, not validation.

## Minimum required inputs / data gaps (before launching FEM)

From original experimental records and characterization, audit and record:
- exact GITT pulse/rest profile, applied current densities and polarity, cutoff, pulse duration, rest duration and temperature per cell, including all sign-changing boundaries;
- active-material masses, areal loadings, electrode thickness and porosity, electrode/electrolyte geometry and reference type; do not infer these numbers from BET;
- SEM particle/aggregate size distributions, and actual BET as independent morphology measurements (HEO 3.94, BM-HEO 18.16, Mg-HEO 6.49, BM-Mg-HEO 16.64 m² g⁻¹);
- starting composition/phase and ex situ/operando evidence for first-cycle structural reconstruction. Currently Mg 1s XPS near 1303 eV supports Mg surface presence, **not unique lattice-site substitution**;
- baseline GITT C1/C2/C3 pulsewise QOCV, signed ΔErest and entire E(t) and partial-cutoff pulse bookkeeping, with full-pulse and total-capacity definitions separated;
- nominal reversible capacity and Coulombic efficiency on the same GITT cells, not substituted with separate 0.1C GCD tests;
- nonuniqueness, uncertain E(t) reference/start time (3 vs 10 s), finite rest window 3500 vs 3600 s, and pulse resolution.

If the original xlsx files are not accessible in a future container, **recover/re-upload exact workbooks** before numerical calibration; conversation descriptions, screenshots and GitHub Markdown tables are insufficient as a replacement for raw E(t).

## Editorial decision gates

**Gate A:** write the simplest physically explicit model and at least one null model; choose predeclared observables and holdouts.

**Gate B:** demonstrate that a history-dependent model adds **out-of-sample explanatory value** beyond area/D shifts and free empirical curve fitting. Only then consider 1D radial transport.

**Gate C:** use true 2D/3D FEM only if measured spatial scales can constrain heterogeneity and the FEM predicts a discriminator absent in simpler models. Compare computation/figure burden with the paper's core contribution.

**Gate D:** include in manuscript only if simulation supports the central question — *which electrochemical intervals and subsequent behavior respond to morphological vs compositional intervention?* Otherwise preserve it as separate future research. PI decides before implementation and manuscript changes.

## State of decision

This file is **not** a commitment to build a FEM model, an endorsement of any specific FEM output, or a claim of new simulation evidence. It records the previously asked but not yet resolved simulation question and a recommended minimal-science-first modeling sequence. GitHub updates remain **request-only**.

Reference analysis: [full C1–C3 discussion](HEO_2026-11-16_COMPLETE_CYCLE_GITT_DISCUSSION_STATE.md).
