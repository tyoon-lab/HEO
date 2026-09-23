# HEO Figures 4–7 — Current Logic, 2026-09-23

## Core electrochemical question

Keep the manuscript-level story simple:

**How can ball milling increase conversion-related capacity while the conversion-associated relaxation becomes slower rather than faster?**

This is the central apparent paradox. Mg incorporation provides the complementary perturbation: it lowers accessible conversion capacity without a proportional change in the relaxation timescale.

Interpretation:
- capacity primarily reports how much reaction becomes accessible;
- t63 is an effective descriptor of conversion-associated current-off kinetics, not the forward conversion rate itself;
- therefore more conversion can coexist with slower relaxation when a modification opens additional reaction population, including slower-relaxing internal states.

This separation is not unique to HEOs, but the multication, heterogeneous, reconstructive nature of HEO conversion provides a natural setting in which reaction accessibility and internal relaxation can become strongly separated.

Detailed wording authority: `manuscript/HEO_ELECTROCHEMISTRY_CORE_STORY_2026-09-23.md`.

## Figure 4 — magnitude and timescale are different observables

Experimental GITT current-off analysis:
- Delta E_relax = 3 s→60 min voltage recovery
- t63 = model-free 63.2% recovery timescale

Result:
BM increases capacity without shorter t63; Mg lowers relaxation magnitude without shorter t63.

Message:
**relaxation magnitude and effective timescale are not interchangeable kinetic descriptors.**

## Figure 5 — first-cycle conversion-associated relaxation

Background-subtracted late-stage GITT excess is independently localized by dQ/dV.

Result:
- BM: smaller peak but broader response
- Mg: strongly suppressed first-cycle peak
- all GITT excess peaks lie within 32 mV of dQ/dV peaks

Message:
**the decoupled relaxation signal is specifically associated with the first-cycle conversion region.**

Do not call the hump a unique “conversion kinetic peak.”

## Figure 6 — cycle-history evolution

Use C1/C2/C3 GITT.

New result:
- hump amplitude/population changes strongly with cycling;
- t63 changes much less;
- first-cycle late hump shifts to an earlier common later-cycle state region;
- Mg first-cycle amplitude suppression largely disappears in later cycles, while lower reversible capacity remains;
- BM higher capacity + longer t63 persists into later cycles.

Message:
**conversion-associated relaxation is history-dependent; cycling changes the excitation/population of the response more strongly than its effective relaxation timescale.**

This is the genuinely new information added by cycles 2–3.

Background audit passed: later-cycle exponential and linear backgrounds are numerically indistinguishable.

### Frozen Figure 6 panel architecture

**(a) Cycle-resolved conversion-associated relaxation profiles.** Plot the background-subtracted excess response for C1, C2, and C3 over the common normalized lithiation coordinate, z = 0.4–0.9, for all four samples. The main visual point is the shift from the late first-cycle feature (z ~ 0.66–0.79) toward a common earlier later-cycle region (z ~ 0.50–0.56).

**(b) Peak amplitude vs cycle.** Show the conversion-associated excess peak amplitude for C1, C2, and C3. This panel carries the strongest direct evidence for history dependence: HEO and BM-HEO decrease strongly, Mg-HEO increases, and BM-Mg-HEO changes comparatively little.

**(c) Effective t63 vs cycle.** Show the median ensemble/state-resolved t63 over z = 0.4–0.9 for C1, C2, and C3. This is intentionally paired with panel (b) to show that the amplitude evolves much more strongly than the effective timescale.

**(d) Normalized amplitude-change vs timescale-change map.** Plot x = t63,3/t63,1 and y = A3/A1, with reference lines at 1. The four samples occupy a narrow x range (0.845–0.923) but a much broader y range (0.435–1.698), providing a compact graphical summary that cycle history redistributes relaxation amplitude far more strongly than it changes the ensemble effective timescale.

Do not replace panel (d) with a reversible-capacity bar in the main figure. Later-cycle reversible capacity remains an important textual/material constraint and may be shown in the SI, but Figure 6 should remain focused on cycle-history evolution of the relaxation response.

## Figure 7 — minimal microkinetic interpretation

Use an effective network:
A <-> B, B -> N, B <-> P, with R1/R3 electrochemical.

At current off:
r1+r3=0, but r1=-r3 !=0 can remain.

Linearized multi-state kinetics gives:
E(t)-Eeq = sum B_i exp(-t/tau_i).

Therefore mode excitation/amplitude and timescale are naturally distinct.

Message:
**a multi-step conversion network provides a physically consistent interpretation of the amplitude–timescale decoupling and its cycle dependence; a simple single-step RC description is insufficient.**

### Frozen Figure 7 panel architecture

Preferred figure title: **Microkinetic interpretation of history-dependent conversion relaxation**

**(a) Effective reaction network.** R1: A + Li+ + e- <-> B; R2: B -> N; R3: B + Li+ + e- <-> P. A/B/N/P are explicitly effective kinetic states.

**(b) Current-off internal counter-current.** Show current-on j_ext=r1+r3 and current-off j_ext=0 with r1=-r3 !=0 allowed. Use one illustrative simulated rest transient to show finite opposing internal currents and continuing voltage relaxation at zero external current. This is not a sample fit.

**(c) Multi-state amplitude–timescale separation.** Show d(delta x)/dt=J delta x and E(t)-E_eq=sum_i B_i exp(-t/tau_i), with B_i identified with excitation/population plus voltage sensitivity and tau_i with kinetic eigen-timescale. The panel explains why amplitude can change strongly while effective t63 changes modestly.

**(d) Experiment-to-model constraint summary.** Connect the model to the three experimental facts: cycle-dependent amplitude >> t63 change; BM gives higher reversible extent with longer effective relaxation; Mg gives lower reversible extent while later-cycle t63 approaches HEO. Present accessible reaction extent, relaxation excitation/amplitude, and effective timescale as distinct but coupled coordinates rather than a single fast/slow axis.

Keep synthetic current-sweep/RDS discrimination in SI or future work, not the main Figure 7. Do not claim a unique RDS.

## Final logical chain

Figure 4:
The apparent paradox first appears: higher accessible capacity does not imply shorter conversion-associated relaxation.

→ Figure 5:
The unusual relaxation is localized to the conversion region, confirming that the paradox belongs to conversion-associated dynamics.

→ Figure 6:
The relaxation is history-dependent: its amplitude changes strongly with cycling while t63 changes much less.

→ Figure 7:
The paradox is resolved mechanistically. A multi-step conversion network allows the amount of reaction/state population accessed during the pulse to change separately from the internal relaxation eigen-timescales after interruption.

BM and Mg should be used as complementary perturbations throughout:
- BM: more accessible conversion, but not faster relaxation;
- Mg: less accessible conversion, without a proportional relaxation-timescale change.

## Closing mechanistic statement candidate

**Ball milling and Mg incorporation do not simply accelerate or retard conversion. Ball milling increases the amount of conversion that can be accessed without accelerating the conversion-associated relaxation, whereas Mg incorporation suppresses accessible conversion without a proportional change in the relaxation timescale.**

More explicit follow-on sentence:

**Ball milling increases reversible capacity despite longer effective relaxation, whereas Mg suppresses reversible capacity while the later-cycle relaxation timescale approaches that of the undoped HEO.**

Final broad statement:

**Conversion dynamics therefore cannot be reduced to a single fast–slow kinetic descriptor.**
