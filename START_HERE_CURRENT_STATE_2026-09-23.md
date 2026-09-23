# HEO — START HERE / Current Project State

**Last consolidated:** 2026-09-23  
**Purpose:** single authoritative restart point for the HEO manuscript/project. A new chat should be able to resume from this repository alone, without a separate handoff message.

---

# 0. Restart protocol

Read these files in order:

1. `START_HERE_CURRENT_STATE_2026-09-23.md` — this file; authoritative current state
2. `manuscript/HEO_FIGURES_4_7_CURRENT_LOGIC_2026-09-23.md` — current Figures 4–7 logic
3. `modeling/HEO_CYCLE_RESOLVED_GITT_AND_BACKGROUND_AUDIT_2026-09-23.md` — Figure 6 evidence and robustness
4. `modeling/HEO_CONVERSION_MICROKINETICS_2026-09-23.md` — Figure 7 model logic
5. `modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_MAP_2026-09-23.md` — literature positioning
6. `manuscript/HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md` — current manuscript scientific/text authority before the 9/23 Figure 6–7 insertion
7. `manuscript/HEO_SUPPORTING_INFORMATION_V3_REVIEW_READY_2026-09-20.md`
8. `manuscript/HEO_FIGURE_ARCHITECTURE_AND_CAPTIONS_V2_CONVERSION_2026-09-20.md`

Do not ask the user for a separate handoff. Continue from Section 15.

---

# 1. Manuscript identity

Working title direction:

**Ball Milling and Mg Incorporation Reshape Conversion Dynamics in Spinel High-Entropy Oxide Anodes**

Target: **Advanced Functional Materials (AFM)**.

Paper identity: **materials/mechanism paper**, not a GITT-method paper.

Preferred hierarchy:

**synthesis/compositional modification → structure/morphology → conventional electrochemistry → state-resolved conversion relaxation → cycle evolution → minimal microkinetic interpretation**

The old free-parameter spatial/phase-field model remains removed from the manuscript.

---

# 2. Figures 1–3: fixed context

Figures 1–2: structural/compositional/morphological collaborator characterization; still provisional until Yoo-group input is frozen.

Figure 3: conventional electrochemistry.

Current first-cycle capacity pair / ICE:

| Sample | first-cycle pair (mAh g^-1) | ICE |
|---|---:|---:|
| HEO | 901.25 / 609.12 | 67.59% |
| BM-HEO | 1056.10 / 782.08 | 74.05% |
| Mg-HEO | 731.15 / 458.91 | 62.77% |
| BM-Mg-HEO | 944.07 / 580.83 | 61.52% |

Core:
- ball milling increases accessible capacity/utilization;
- Mg lowers accessible capacity;
- normalized rate retention alone is not proof of faster kinetics;
- use absolute rate capacity when discussing rate performance.

Historical rate-cell sequence recovered from the 2026-05-08 deck:

**0.1C → 0.3C → 0.5C → 1C → 3C → 5C → 0.1C recovery**

Mean normalized 5-cycle-block retentions:

| Rate | HEO | BM | Mg | BM-Mg |
|---|---:|---:|---:|---:|
| 0.1C | 96.34 | 97.66 | 94.45 | 94.90 |
| 0.3C | 85.43 | 87.07 | 82.06 | 81.47 |
| 0.5C | 75.10 | 78.97 | 75.64 | 74.33 |
| 1C | 61.23 | 67.72 | 66.18 | 63.46 |
| 3C | 34.42 | 44.65 | 48.40 | 42.38 |
| 5C | 14.05 | 27.62 | 35.92 | 30.02 |
| recovery 0.1C | 85.22 | 89.44 | 87.19 | 86.51 |

Using the historical rate-cell first-cycle discharge capacities (HEO 558.8, BM 699.2, Mg 514, BM-Mg 590.3 mAh g^-1), approximate absolute capacities are:

| Rate | HEO | BM | Mg | BM-Mg |
|---|---:|---:|---:|---:|
| 0.5C | 420 | 552 | 389 | 439 |
| 1C | 342 | 474 | 340 | 375 |
| 3C | 192 | 312 | 249 | 250 |
| 5C | 79 | 193 | 185 | 177 |

Important:
- BM > HEO at all measured rates in both normalized retention and absolute capacity.
- Mg high-rate advantage is real for HEO vs Mg: at 5C, ~79 vs ~185 mAh g^-1.
- Mg high-rate advantage is not universal after milling: BM ~193 vs BM-Mg ~177 mAh g^-1 at 5C.
- do not equate these capacity trends directly with GITT t63.

---

# 3. Figure 4 — GITT relaxation magnitude vs effective timescale

Protocol:
- 100 mA g^-1
- 600 s current pulse
- 3600 s OCV rest
- current-off reference = 3 s

Definitions:
- `Delta E_relax = E_60min - E_off,3s`
- `t63` = first time to complete 63.2% of the observed 3 s→60 min recovery
- t63 is model-free and should now be called an **ensemble/state-resolved effective relaxation timescale**, not a local single-process time constant.

First-cycle medians over common 200–800 mAh g^-1:

| Sample | Delta E_relax (mV) | t63 (min) |
|---|---:|---:|
| HEO | 160.9 | 8.68 |
| BM-HEO | 176.3 | 11.57 |
| Mg-HEO | 109.5 | 11.01 |
| BM-Mg-HEO | 144.3 | 12.99 |

Core:
- relaxation magnitude and timescale are distinct observables;
- BM raises capacity without shortening relaxation;
- Mg lowers relaxation magnitude without shortening t63;
- smaller Delta E_relax must not be described as automatically faster kinetics.

---

# 4. Figure 5 — first-cycle conversion-associated hump

Nominal background-subtracted excess:
`eta_peak(z)=max[Delta E_relax(z)-eta_bg(z),0]`, evaluation z=0.40–0.90.

Independent first-cycle dQ/dV localization:

| Sample | dQ/dV peak (V) | GITT excess peak (V) | difference |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | -0.018 |
| BM-HEO | 0.589 | 0.618 | +0.029 |
| Mg-HEO | 0.419 | 0.387 | -0.032 |
| BM-Mg-HEO | 0.485 | 0.503 | +0.018 |

All within 32 mV.

Nominal first-cycle excess:

| Sample | peak (mV) | width (mAh g^-1) | normalized excess area (mV) |
|---|---:|---:|---:|
| HEO | 70.77 | 354.13 | 22.07 |
| BM-HEO | 44.07 | 430.17 | 14.13 |
| Mg-HEO | 15.91 | 250.29 | 4.94 |
| BM-Mg-HEO | 21.10 | 391.78 | 7.58 |

105-window robustness already established for the first-cycle ordering.

Interpretation boundaries:
- call it **conversion-associated relaxation**;
- amplitude ≠ conversion fraction;
- width ≠ measured microscopic phase/threshold distribution;
- area ≠ energy;
- do not assign the hump uniquely to nucleation, Li2O, metal nanoparticles, strain, etc.

---

# 5. Key new result: cycle-resolved GITT

Raw GITT contains multiple lithiation/delithiation cycles. Correct pulse/rest filtering gives stable 2nd/3rd-cycle states.

For lithiation, using common normalized z=0.4–0.9:

| Sample | C1 Delta E / t63 | C2 Delta E / t63 | C3 Delta E / t63 |
|---|---|---|---|
| HEO | 168.5 mV / 10.37 min | 129.2 / 9.43 | 138.4 / 9.57 |
| BM-HEO | 160.5 / 13.02 | 125.7 / 11.18 | 133.5 / 11.33 |
| Mg-HEO | 111.3 / 10.53 | 127.9 / 9.83 | 140.9 / 9.53 |
| BM-Mg-HEO | 135.2 / 12.70 | 126.7 / 10.90 | 142.6 / 10.73 |

The strongest new message is not simply that the Figure 5 decoupling repeats. It is that the **conversion-associated relaxation itself evolves with cycling**.

Conversion-associated peak amplitude, using the same first-cycle-style background definition as an exploratory cycle comparison:

| Sample | C1 peak | C2 peak | C3 peak | z_peak C1→C3 |
|---|---:|---:|---:|---:|
| HEO | 71.2 | 23.4 | 31.0 mV | 0.77→0.55 |
| BM-HEO | 44.8 | 17.2 | 22.4 | 0.67→0.54 |
| Mg-HEO | 15.9 | 19.3 | 27.0 | 0.79→0.56 |
| BM-Mg-HEO | 21.1 | 12.6 | 20.8 | 0.66→0.53 |

Cycle-1 → cycle-3 normalized changes:

| Sample | A3/A1 | amplitude change | t63,3/t63,1 | t63 change |
|---|---:|---:|---:|---:|
| HEO | 0.435 | -56.5% | 0.923 | -7.7% |
| BM-HEO | 0.500 | -50.0% | 0.870 | -13.0% |
| Mg-HEO | 1.698 | +69.8% | 0.905 | -9.5% |
| BM-Mg-HEO | 0.986 | -1.4% | 0.845 | -15.5% |

Thus:
- relaxation amplitude/history changes strongly;
- t63 changes much more modestly;
- first-cycle hump is not a stationary material kinetic fingerprint;
- cycle history appears to change how strongly conversion-associated modes are populated/excited much more than their ensemble effective timescale.

Safe wording:
**The population/excitation of conversion-associated relaxation modes evolves more strongly with cycling than their effective relaxation timescale.**

Do not claim a measured eigenmode decomposition; `mode` here is a reduced microkinetic interpretation.

---

# 6. Reversible reaction extent in later cycles

Approximate GITT lithiation capacities from pulse counting:

| Sample | C1 | C2 | C3 |
|---|---:|---:|---:|
| HEO | 1083 | 700 | 700 |
| BM-HEO | 1267 | 850 | 833 |
| Mg-HEO | 800 | 467 | 450 |
| BM-Mg-HEO | 933 | 567 | 533 |

Third-cycle delithiation capacities:

| Sample | C3 delithiation |
|---|---:|
| HEO | 733 |
| BM-HEO | 817 |
| Mg-HEO | 467 |
| BM-Mg-HEO | 533 |

Paired cycle-2/3 lithiation/delithiation ratios are ~1, so after the first cycle the repeated reaction is largely reversible. Do not call the coarse pulse-count ratio exact Coulombic efficiency.

Key effect:
- Mg suppresses stable later-cycle accessible reversible reaction extent by ~35–36% in both non-BM and BM pairs.
- BM increases later-cycle accessible extent by ~15–20%.

This is important because Mg first-cycle hump suppression does not remain as a comparable later-cycle t63 difference, whereas the lower reversible capacity persists.

Safe summary:
- **BM:** reversible capacity/extent ↑ while effective relaxation remains slower.
- **Mg:** reversible capacity/extent ↓ strongly while later-cycle t63 approaches HEO-like values.

Use **reversible capacity / accessible reversible reaction extent**, not `conversion fraction`.

---

# 7. Delithiation GITT direction asymmetry

Correctly filtered later-cycle delithiation medians over z=0.4–0.9:

| Sample | C2 Delta E / t63 | C3 Delta E / t63 |
|---|---|---|
| HEO | 170.6 mV / 6.50 min | 182.6 / 6.63 |
| BM-HEO | 196.1 / 8.34 | 197.9 / 8.25 |
| Mg-HEO | 171.9 / 7.05 | 181.3 / 7.05 |
| BM-Mg-HEO | 214.1 / 7.88 | 219.8 / 7.80 |

Later-cycle delithiation t63 is generally shorter than lithiation t63. This establishes direction asymmetry, but do not use it alone to uniquely assign a mechanism.

---

# 8. Figure 6 background-sensitivity audit — PASSED

For cycles 2–3, the nominal exponential background becomes numerically almost linear.

Exponential vs linear peak amplitudes:

| Sample | Cycle | exponential | linear |
|---|---:|---:|---:|
| HEO | 2 | 23.247 | 23.246 mV |
| HEO | 3 | 30.751 | 30.750 |
| BM-HEO | 2 | 17.012 | 17.011 |
| BM-HEO | 3 | 22.125 | 22.124 |
| Mg-HEO | 2 | 19.258 | 19.258 |
| Mg-HEO | 3 | 26.854 | 26.854 |
| BM-Mg-HEO | 2 | 12.382 | 12.381 |
| BM-Mg-HEO | 3 | 20.580 | 20.578 |

Audit result:
- amplitude difference < 0.012% for every cycle-2/3 case;
- peak z is identical for exponential and linear backgrounds;
- maximum background difference < 0.0016 mV;
- fitted exponential background tau in z is ~2.4e3–5.4e3, i.e. effectively the linear limit.

Therefore the cycle-evolution conclusion is not a later-cycle background artifact.

Important:
- keep **exponential background** for Figure 5 first cycle;
- for Figure 6 later cycles use the same nominal method, with the linear-baseline sensitivity check in SI;
- do not force a linear baseline onto first-cycle Figure 5.

---

# 9. Figure 6 current role

Figure 6 should now be an **experimental cycle-evolution figure**, not the earlier distributed-threshold simulation.

Primary conclusion:
**conversion-associated relaxation is history-dependent and evolves with cycling.**

Frozen panels:
- (a) C1/C2/C3 background-subtracted conversion-associated relaxation profiles over common z=0.4–0.9;
- (b) conversion-associated peak amplitude vs cycle;
- (c) median ensemble/state-resolved t63 vs cycle over z=0.4–0.9;
- (d) normalized change map with x=t63,3/t63,1 and y=A3/A1, with unity reference lines.

Panel (d) is intentionally the amplitude-change vs timescale-change map, not a reversible-capacity bar. The four samples occupy a narrow timescale-ratio range (0.845–0.923) but a broad amplitude-ratio range (0.435–1.698), directly summarizing the Figure 6 conclusion. Later-cycle reversible capacity remains a text/SI material constraint.

The scientific role is frozen:
- Figure 5 = first-cycle magnitude/timescale decoupling and conversion localization;
- Figure 6 = cycle-history evolution and persistence/non-persistence of material effects.

Potential sentence:
**Cycling strongly redistributes the magnitude of the conversion-associated relaxation while producing only modest changes in its effective timescale.**

Potential stronger but still safe sentence:
**The first-cycle relaxation hump is therefore not a stationary kinetic fingerprint, but a history-dependent response whose excitation evolves as the conversion state is established.**

Use `cycled state` or `post-first-cycle state`; avoid implying a structurally proven “reconstructed state” unless direct structural evidence is added.

---

# 10. Earlier distributed-threshold Figure 6 model — historical status

The 2026-09-22 model using:
- normalized excess distribution p(zc);
- t63(zc) as effective local relaxation input;
- ensemble response X(z,C);

was explored extensively.

It was useful for showing that reaction-state distribution and relaxation speed need not produce identical trends.

However:
- X is not capacity or phase fraction;
- Q×X is not a valid capacity prediction;
- rate-capability data are not reproduced at high rate;
- the model mostly reformulates a decoupling already visible experimentally;
- the cycle-resolved GITT analysis provides a stronger, more direct Figure 6.

Therefore the distributed-threshold model is **not the current main Figure 6 direction**. Keep it as historical/exploratory analysis only.

---

# 11. Figure 7 — frozen minimal conversion microkinetics

The new direction is not to fit a unique RDS. It is to ask whether a minimal multi-step conversion network can explain:
- amplitude/time decoupling;
- long current-off relaxation;
- cycle-history dependence;
- BM: higher capacity with longer effective relaxation;
- Mg: lower capacity with later-cycle HEO-like t63.

Effective network:

R1:
`A + Li+ + e- <-> B`
electrochemical activation

R2:
`B -> N`
effective nucleation/activity evolution

R3:
`B + Li+ + e- <-> P`
electrochemical phase-growth / conversion step

State variables are effective, not atomistically identified species.

Important current-off condition:
`j_ext = r1 + r3 = 0`

This does **not** require:
`r1 = r3 = 0`.

Internal counter-current is possible:
`r1 = -r3 != 0`,
so internal conversion-state evolution can continue at zero external current.

This is the key conceptual basis for prolonged GITT relaxation in a multi-step conversion network.

Frozen main-text architecture:
- (a) effective R1/R2/R3 reaction network;
- (b) current-on/current-off balance with an illustrative zero-external-current internal counter-current transient;
- (c) local linearized multi-state amplitude–timescale separation, E(t)-E_eq = sum_i B_i exp(-t/tau_i);
- (d) experiment-to-model constraint summary separating accessible reversible reaction extent, relaxation excitation/amplitude, and effective timescale.

The illustrative current-off simulation is a mechanistic-consistency demonstration, not a sample fit. Its compact output is stored in `modeling/HEO_MICROKINETIC_CURRENT_OFF_BALANCE_2026-09-23.csv`.

Do not place the synthetic current-sweep/RDS-discrimination result in the main Figure 7; retain it for SI/future direction.

---

# 12. Figure 7 main interpretation

Linearized internal-state microkinetics generically gives:

`E(t)-E_eq = sum_i B_i exp(-t/tau_i)`

where:
- B_i depends on how strongly a mode/state is populated or excited and on voltage sensitivity;
- tau_i derives from kinetic eigenvalues.

Therefore amplitude and timescale need not co-vary.

This provides a physically coherent interpretation of Figure 5–6:
- Mg can strongly change hump amplitude/population while leaving effective t63 similar;
- BM can access more slow/heterogeneous reaction population and therefore show higher capacity with longer ensemble t63.

Do not claim measured microscopic eigenmodes. The equation is a local linearized interpretation of a multi-state kinetic network.

---

# 13. What Figure 7 may and may not claim

Safe main-text direction:
- a **simple single-step RC description is insufficient** to capture the observed long, history-dependent amplitude–timescale behavior;
- nucleation- and phase-growth-associated internal-state dynamics provide physically consistent routes to the observations;
- multi-step conversion kinetics naturally permits amplitude and timescale to evolve differently.

Avoid in Main:
- “single-current experiment is non-identifiable” as a headline;
- “additional current-dependent GITT is required”;
- a unique RDS assignment;
- fitting k1, kn, kg as if uniquely identifiable physical constants.

If a limitation sentence is needed in Methods/SI:
**The model is intended to test mechanistic consistency rather than to assign a unique elementary rate-limiting step.**

Synthetic model result:
different nucleation-dominant and electrochemical-growth-dominant parameter regimes can be made to produce nearly identical 3-s amplitude and t63 at one reference pulse current. Excitation/current dependence then separates the model regimes. Treat this as a **model prediction / future discrimination route**, not an experimental requirement for the present paper.

---

# 14. Conversion microkinetics literature position

The closest direct precedent identified is a 2026 ACS Applied Materials & Interfaces study (Alsaç et al., DOI: 10.1021/acsami.5c20956) that applies microkinetic modeling to conversion cathodes including S, FeS2, and FeF3, with reaction networks, Butler–Volmer kinetics, species evolution, transport/passivation, and different initial/subsequent pathways.

Other important adjacent references:
- FeF3 GITT / conversion overpotential: JACS 2016, DOI 10.1021/jacs.6b00061
- NiO potential-dependent nucleation / conversion: ACS Nano 2019, DOI 10.1021/acsnano.9b02007
- NiO heterogeneous nucleation / phase-front evolution: Nature Communications article ncomms4358
- FeS2 continuum/P2D conversion model: J. Power Sources 2022, PII S0378775322008783

Current gap of interest:
**elementary-step/RDS-style electrochemical microkinetics linked specifically to current-interruption relaxation and amplitude/timescale evolution** appears much less developed than species-evolution or phase-field/continuum conversion modeling.

Do not claim a universal “first” without a full literature audit.

---

# 15. Immediate next task — start next chat here

The modeling direction is now sufficiently closed.

Next session should move to:
1. Figure 6 architecture is frozen; finalize its caption wording when the plotted panels are assembled;
2. Figure 7 architecture is frozen; finalize its caption wording when the schematic/simulation panels are assembled;
3. write the Results/Discussion transition from Figure 4 → Figure 5 → Figure 6 → Figure 7;
4. then update Main/SI manuscript text.

Do **not** reopen the distributed-threshold capacity-prediction model unless a specific unresolved need emerges.

Do not expand the microkinetic model further in the current paper unless the Figure 7 interpretation fails a clear physics check.

---

# 16. Decisions that must not be accidentally reversed

- Paper remains a materials/mechanism paper, not a GITT-method paper.
- Figure 5 remains the first-cycle experimental mechanistic centerpiece.
- Figure 6 is now cycle-resolved experimental evolution, not the old distributed-threshold simulation.
- Figure 7, if retained, is minimal microkinetic interpretation, not a unique RDS extraction.
- Do not call t63 a local microscopic time constant; use ensemble/state-resolved effective relaxation timescale.
- Do not equate smaller relaxation amplitude with faster kinetics.
- Do not equate hump amplitude with conversion fraction.
- Do not equate hump width with a measured phase/threshold distribution.
- Do not equate excess area with energy.
- Do not call later-cycle capacity directly “conversion fraction”; use reversible capacity or accessible reversible reaction extent.
- Do not use “reconstructed state” as if structurally proven; prefer cycled/post-first-cycle state.
- Do not say charge transfer is absent; say a **simple single-step RC** description is insufficient.
- Do not state a unique nucleation/growth RDS from the current data.
- Do not foreground “non-identifiability” or invite extra experiments in the Main text.
- If model limitations are stated: the model tests mechanistic consistency rather than assigning a unique elementary RDS.
- Keep current-dependent GITT and oxide-vs-sulfide comparison as strong follow-up directions.
