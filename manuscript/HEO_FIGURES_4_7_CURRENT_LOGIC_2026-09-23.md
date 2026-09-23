# HEO Figures 4–7 — Current Logic, 2026-09-23

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
**a multi-step conversion network provides a physically consistent origin for the amplitude–timescale decoupling and its cycle dependence; a simple single-step RC description is insufficient.**

Do not claim a unique RDS.

## Final logical chain

Figure 4:
What is observed? Magnitude and timescale decouple.

→ Figure 5:
Where does the distinctive signal occur? In the conversion-associated region.

→ Figure 6:
Is that response a fixed material kinetic fingerprint? No; it evolves strongly with cycle history, mainly through amplitude/population rather than comparable t63 change.

→ Figure 7:
Why is that possible? A multi-step conversion network naturally separates state excitation/population from relaxation eigen-timescale.

## Closing mechanistic statement candidate

**Ball milling and Mg incorporation do not simply accelerate or retard conversion. Their electrochemical effects are expressed through different combinations of reversible reaction extent and history-dependent conversion-associated relaxation.**

More explicit follow-on sentence:

**Ball milling increases reversible capacity despite longer effective relaxation, whereas Mg suppresses reversible capacity while the later-cycle relaxation timescale approaches that of the undoped HEO.**

Final broad statement:

**Conversion dynamics therefore cannot be reduced to a single fast–slow kinetic descriptor.**
