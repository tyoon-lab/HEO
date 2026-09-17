# HEO Electrochemistry Analysis and Manuscript Strategy

**Date:** 2026-09-18

## 1. Scope of the electrochemistry section

The manuscript remains synthesis-centered. The electrochemistry section should not be written as a standalone methods paper. Its role is to explain how the synthesis variables — Mg incorporation and ball milling — alter electrochemical utilization, polarization, relaxation, and cycling stability.

The four-sample matrix is:

- HEO
- BM-HEO
- Mg-HEO
- BM-Mg-HEO

The main electrochemical question is:

> How do Mg incorporation and ball milling alter the accessible conversion capacity and the polarization/relaxation associated with lithiation-induced phase evolution?

The principal mechanistic interpretation should be slightly assertive, but remain anchored to published HEO/spinel literature showing lithiation-induced spinel-to-rock-salt/conversion-type phase evolution and the known contribution of nucleation/phase-boundary processes to overpotential.

---

## 2. Core manuscript story

### 2.1 Ball milling

Working interpretation:

- Ball milling increases electrochemically accessible capacity at low rate.
- The increase in capacity is not explained by uniformly lower resistance or faster apparent diffusion.
- Early first-lithiation current-off polarization is larger after ball milling, especially below approximately 200 mAh g^-1.
- At intermediate capacity the fast current-off resistance difference between HEO and BM-HEO becomes much smaller.
- The late-stage relaxation hump is lower in peak amplitude but broader in capacity after ball milling.
- This is interpreted as broadening/distribution of the lithiation-induced phase-transition interval, together with partial reduction of the peak transformation-associated polarization barrier.
- Ball milling also produces slower overall relaxation / more slow polarization, so the low-rate capacity advantage can be lost rapidly as rate increases and accumulated polarization drives the electrode to cutoff earlier.

Working causal chain:

`ball milling -> structural disorder / broadened local environments -> phase transformation distributed over a broader capacity interval -> lower local peak transition overpotential + larger accessible low-rate capacity -> slower residual relaxation / weaker rate capability`

The manuscript should avoid the simplistic statement `ball milling improves Li diffusion`.

### 2.2 Mg incorporation

Working interpretation:

- Mg strongly suppresses the fast current-off polarization and the long-rest relaxation amplitude.
- Mg also substantially suppresses or removes the pronounced late-stage relaxation hump.
- Despite the smaller polarization, Mg-containing samples do not relax faster; model-free t50/t63/t90 are not reduced and are often longer.
- Therefore the reduced polarization is not most naturally explained by faster Li transport.
- The preferred interpretation is that Mg stabilizes the parent oxide/spinel-derived structure and suppresses the extent of the late-stage spinel-to-rock-salt/conversion transformation.
- Suppressing that transformation reduces both the transformation-associated overpotential and the additional conversion capacity.

Working causal chain:

`Mg incorporation -> structural stabilization / reduced extent of conversion-type phase evolution -> smaller transformation-associated polarization -> lower accessible conversion capacity`

Recommended manuscript wording direction:

> Mg incorporation predominantly suppresses the late-stage spinel-to-rock-salt/conversion transformation rather than simply accelerating Li transport.

This should be followed by the evidence: reduced late-stage hump, reduced relaxation amplitude, lower accessible capacity, and absence of faster t63/t90.

Alternative mechanisms should be acknowledged after the preferred interpretation:

- Faster Li diffusion alone is less consistent because relaxation times do not become shorter.
- Pure ohmic/electronic resistance reduction can explain a smaller fast jump but not the selective disappearance of the late-stage hump and the lower capacity.
- Reduced surface accessibility can lower capacity but does not naturally explain the strongly state-dependent suppression of the late-stage relaxation feature.
- SEI/side-reaction differences may affect early first-cycle response but are unlikely to be the most economical explanation of the approximately 0.5 V-centered late-stage feature.

---

## 3. GITT analysis strategy for the manuscript

### 3.1 Prefer current-off / rest analysis over current-on analysis

During the pulse, the equilibrium potential changes with inserted charge:

`E(t) = E_eq(Q(t)) + eta(t)`

Therefore current-on and pulse-period voltage changes mix reversible capacity/thermodynamic evolution with polarization.

For the main manuscript, prioritize current-off and rest quantities where additional charge is no longer inserted.

Primary descriptors:

- extrapolated current-off instantaneous jump / apparent fast resistance;
- fixed-window relaxation amplitude;
- model-free relaxation times t50, t63, t90;
- early relaxation slope;
- terminal/late relaxation slope;
- cumulative specific capacity as the principal state coordinate.

The current-on/pulse quantities can remain in the analysis archive or Supporting Information as consistency checks, but they should not carry the main mechanistic argument.

### 3.2 ICI-style current-off decomposition

Instead of treating the first available 3 s point as a pure IR drop, fit the early rest region using the established current-interruption form:

`E(t) = a + b sqrt(t)`

The t -> 0 intercept provides a more defensible apparent instantaneous current-off jump, while the sqrt(t) coefficient represents the early diffusion-like / distributed transport response under the assumptions of ICI-style analysis.

In the current data, the 3–30 s region is highly linear in sqrt(t) for most steps, so this representation is useful and consistent with established current-interruption practice.

Important interpretation boundary:

- call the intercept an `apparent instantaneous resistance/current-off jump`, not a unique ohmic resistance unless independently validated;
- the sqrt(t) term can contain diffusion-like response but should not be assigned uniquely to bulk solid diffusion in a phase-evolving HEO electrode.

### 3.3 Model-free relaxation descriptors

For the 3 s to 60 min rest interval, define t50, t63, and t90 as the times required to reach 50%, 63.2%, and 90% of the observed finite-window relaxation amplitude.

These are not obtained by fitting a single exponential.

`t63` is particularly intuitive because it equals tau only for an ideal single exponential, while remaining a model-free characteristic time for a distributed response.

Use:

- t63 as the main-text characteristic relaxation-time descriptor;
- t50 and t90 in Supporting Information to show early-vs-tail changes;
- late/terminal slope as an unresolved-slow-response indicator.

Key observation:

- Mg lowers polarization amplitude but does not shorten relaxation time.
- Ball milling generally lengthens relaxation.

This separation of response amplitude and response time is central to arguing that a single apparent GITT diffusivity cannot capture the observed behavior.

---

## 4. Late-stage phase-transition relaxation feature

A pronounced late-stage hump is observed in the HEO relaxation-amplitude-versus-capacity profile, centered in the low-voltage conversion region. Related spinel HEO literature reports lithiation-induced spinel-to-rock-salt / conversion-type phase evolution in a similar voltage range, and phase-transforming electrodes are known to develop additional overpotential from nucleation, phase-boundary propagation, strain accommodation, and structural reorganization.

For the manuscript, the preferred assignment is:

> The pronounced late-stage polarization hump is assigned primarily to the spinel-to-rock-salt/conversion phase transformation, for which nucleation, phase-boundary propagation, and associated structural reorganization introduce an additional electrochemical overpotential.

Follow with:

> This assignment is based on the characteristic voltage range and phase-evolution pathways established for compositionally related spinel HEO anodes.

This is intentionally stronger than describing the hump as an unspecified structural relaxation, because no additional operando structural experiment is planned. The support should therefore come from careful literature citation and consistency across voltage, capacity, ball-milling, and Mg effects.

---

## 5. Peak-height / width / area analysis

The late-stage excess relaxation feature can be quantified after subtracting a smooth background relaxation trend:

`eta_tr(Q) = max[DeltaE_relax(Q) - eta_bg(Q), 0]`

Extract:

- peak excess amplitude;
- FWHM-like capacity width;
- integrated excess polarization area on the Q axis;
- integrated excess area on normalized capacity z = Q/Qmax.

Interpretation:

- peak height measures how concentrated the transformation-associated polarization is at its maximum;
- width measures over how broad a capacity interval the transition-associated response is distributed;
- integrated area measures the capacity-weighted magnitude of the excess polarization feature.

Do not call the integrated area a rigorous dissipated energy. Although `integral eta dQ` has energy-per-mass units, `eta` here is a finite-window GITT relaxation descriptor sampled at discrete states rather than the continuous operating overpotential.

Use the phrase `capacity-weighted excess polarization area`.

Current exploratory result:

- BM-HEO: lower peak height, broader width, and somewhat smaller integrated excess area than HEO.
- Mg-HEO: strongly suppressed peak and area.
- BM-Mg-HEO: transition feature remains much smaller than Mg-free samples and is not restored to the HEO-like response.

This supports:

`ball milling -> broader, less concentrated phase-transition polarization`

and

`Mg -> suppression of the phase-transition extent / associated conversion response`.

---

## 6. Recommended electrochemistry section architecture

### Section A. Electrochemical utilization and cycling behavior

Show:

- first-cycle voltage profiles / first charge-discharge capacity / ICE;
- cycling at low rate;
- rate performance.

Main observations:

- ball milling increases initial/low-rate accessible capacity;
- Mg lowers accessible capacity;
- ball-milled samples lose their capacity advantage rapidly as rate increases;
- cycling and rate results should be described first without prematurely assigning transport parameters.

### Section B. Current-interruption and relaxation analysis

Show preferably in one main figure:

1. representative GITT pulse/rest with definitions;
2. apparent instantaneous current-off resistance/jump vs cumulative capacity;
3. 60 min relaxation amplitude vs cumulative capacity;
4. t63 vs cumulative capacity;
5. optionally transition-hump excess profile / peak-width-area summary.

Main mechanistic statements:

- early BM polarization is larger but converges toward the HEO level at intermediate lithiation;
- ball milling broadens and partially lowers the late-stage transition-associated polarization feature;
- Mg sharply suppresses the same late-stage feature;
- polarization magnitude and relaxation time do not co-vary, demonstrating that reduced polarization does not simply imply faster transport.

### Section C. Mechanistic interpretation linking synthesis and electrochemistry

Preferred synthesis-electrochemistry narrative:

- pristine HEO: comparatively concentrated spinel-to-rock-salt/conversion transition -> pronounced late-stage polarization hump;
- BM-HEO: structural disorder / broadened local environments -> transformation distributed over wider capacity -> lower local peak transition barrier and larger low-rate accessible capacity, but slower residual relaxation -> poor rate retention;
- Mg-HEO: structural stabilization -> suppressed transition extent -> lower transformation overpotential but lower conversion capacity;
- BM-Mg-HEO: ball milling increases polarization/slow relaxation but does not restore the strong transition response suppressed by Mg.

The electrochemistry should be used to explain synthesis-dependent response rather than to turn the manuscript into a GITT-method paper.

---

## 7. Role of conventional GITT diffusivity

Do not center the HEO manuscript on D_GITT.

If retained:

- describe it as `apparent GITT diffusivity`;
- state that it shows strong state dependence and no simple monotonic dependence on ball milling or Mg incorporation;
- place detailed D plots in Supporting Information;
- avoid using D as the causal explanation for capacity differences.

The main paper should instead emphasize directly observed current-off polarization and relaxation descriptors.

---

## 8. Compact-model hierarchy: internal audit, not a main HEO result

Exploratory comparison already tested:

`finite-diffusion only -> finite diffusion + one compact relaxation mode -> distributed relaxation`

Observed outcome:

- diffusion-only gives substantially larger residuals;
- adding one compact exponential relaxation mode reduces error dramatically;
- distributed relaxation reduces residuals further;
- however, fitted characteristic times of the finite-diffusion and added relaxation terms can overlap and become parameter-bound / non-unique.

Interpretation:

This analysis is scientifically useful as an **internal model-sufficiency/identifiability audit**, but at present it adds little direct mechanistic information for the synthesis-centered HEO manuscript.

Do not make it a main-text figure unless a later analysis reveals a robust, synthesis-dependent compact parameter that survives fitting-window and initialization tests.

Possible uses:

- Supporting Information sensitivity note;
- future GITT/EKF methods paper;
- evidence motivating distributed-response analysis in the separate kinetic-fingerprint program.

Important conceptual point:

Finite diffusion itself is an exponential eigenmode series, and an added first-order RC-like term is another exponential contribution. Excellent fit quality therefore does not guarantee unique separation of diffusion, interface, and phase-transformation physics.

For this HEO manuscript, the safer and more useful information comes from the model-free current-off descriptors and literature-supported phase-transition assignment.

---

## 9. Separate EKF/GITT research opportunity

HEO is a useful future test case for the GITT-side kinetic-fingerprint program because it provides a 2 x 2 material/process perturbation:

- composition: Mg-free vs Mg-containing;
- processing: pristine vs ball-milled.

Unlike the HEO synthesis paper, the future EKF study may retain the full transient and compare:

`raw transient -> model-free descriptors -> compact models -> distributed relaxation spectrum`

A joint pulse+rest inversion can also be tested later, but this should remain outside the current manuscript unless it yields a uniquely useful and robust result.

Potential state-resolved representation:

`R(q, log tau | Mg, BM, direction, cycle)`

The key future question is whether material/process changes can be distinguished by changes in response amplitude and relaxation-time distribution without collapsing the transient into one D_GITT value.

---

## 10. Immediate next analysis priorities

1. Finalize current-off ICI-style intercept and sqrt(t) coefficient vs cumulative capacity for all four samples.
2. Finalize DeltaE_relax and t50/t63/t90 vs capacity.
3. Quantify the transition hump with peak height, capacity width, and normalized/absolute capacity-weighted excess area.
4. Overlay the transition feature with the GITT relaxed-voltage trajectory to identify its voltage window.
5. Compare these electrochemical features directly with BET/Cdl and synthesis/structure results.
6. Revisit later-cycle EIS/SEM/cycling only after the first-cycle mechanistic picture is fixed.
7. Keep D-only / D+compact-mode / distributed-relaxation analysis in the internal archive unless a robust manuscript-level descriptor emerges.

---

## 11. Claim boundaries

Reasonably strong claims:

- ball milling broadens the late-stage transformation-associated polarization over a wider capacity range;
- Mg strongly suppresses the late-stage transformation-associated electrochemical response;
- reduced polarization after Mg incorporation is not accompanied by faster relaxation and therefore cannot be explained simply by faster Li diffusion;
- accessible capacity, polarization amplitude, and relaxation time are distinct observables and should not be collapsed into a single apparent diffusivity.

Claims to avoid without additional structural experiment:

- exact phase fraction from GITT;
- unique microscopic assignment of every relaxation component;
- a unique intrinsic Li diffusion coefficient for the conversion-type HEO electrode;
- proof that ball milling lowers a thermodynamic phase-transition energy barrier;
- proof that Mg completely eliminates the phase transition.

Use literature-supported `assigned primarily to`, `consistent with`, and `predominantly suppresses` language where appropriate.
