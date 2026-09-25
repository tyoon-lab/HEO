# HEO Electrochemistry Core Story — 2026-09-25

## One-sentence thesis

**Accessible capacity and conversion-associated kinetics are linked through the same conversion network, but they are not kinetically equivalent and therefore need not follow a single fast–slow trend.**

## Central scientific question

Battery materials are commonly judged by capacity and kinetics, and higher accessible capacity is often associated with improved kinetics under finite-rate operation.

The HEO result challenges the simplest version of that expectation:

- ball milling increases accessible capacity;
- yet GITT relaxation becomes slower rather than faster;
- Mg incorporation lowers accessible conversion;
- yet the effective relaxation timescale does not change proportionally.

Therefore the paper asks:

**Does higher accessible conversion capacity necessarily indicate faster conversion kinetics in a reconstructive multistep electrode?**

## What GITT means in this paper

GITT relaxation is used as a state-resolved probe of conversion-associated kinetics.

A shorter t63 is consistent with faster relaxation under matched conditions, but:

- t63 is not the forward conversion rate itself;
- t63 is not one microscopic rate constant;
- t63 reflects the ensemble relaxation of the nonequilibrium state created by the preceding pulse.

Forward conversion and current-off relaxation are kinetically connected because they arise from the same reaction network. The central result is therefore not that they are unrelated, but that they are **not kinetically equivalent observables**.

## Experimental logic

### Figure 3 — establish accessible capacity

Ball milling:
- increases BET surface area and accessible capacity;
- increases later-cycle reversible reaction extent.

Mg:
- lowers accessible capacity;
- suppresses later-cycle reversible reaction extent.

Figure 3 does not assign a kinetic rate from capacity alone.

### Figure 4 — reveal the capacity–kinetics mismatch

Ball milling gives higher capacity but longer t63.

Mg lowers relaxation magnitude without producing the proportional timescale change expected from a simple one-rate picture.

Main statement:

**The material trends cannot be described as uniform acceleration or deceleration of a single conversion-rate coordinate.**

### Figure 5 — prove the mismatch belongs to conversion

The GITT excess and cathodic dQ/dV conversion signatures occur within 32 mV for all four samples.

Therefore the anomalous GITT response is conservatively assigned as **conversion-associated**.

Do not assign it uniquely to nucleation, phase-front motion, oxygen rearrangement, metal formation, Li2O formation, or one RDS.

### Figure 6 — show that the kinetic response is history-dependent

The conversion-associated amplitude changes strongly from cycle 1 to cycle 3, while t63 changes much less.

Later-cycle capacity differences remain large.

Therefore the first-cycle relaxation hump is not a stationary kinetic fingerprint, and the capacity–kinetics mismatch is not restricted to first-cycle irreversibility.

### Figure 7 — explain why the mismatch is physically possible

First establish the ordinary expectation:

\[
\text{uniformly faster kinetics}
\Rightarrow
Q_{\rm cutoff}\uparrow,\quad t_{63}\downarrow
\]

The homogeneous microkinetic control reproduces this behavior.

Then use the coarse-grained conversion network:

\[
O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C
\]

to show that a heterogeneous multistep system can instead give:

\[
Q_{\rm cutoff}\uparrow,\quad t_{63}\uparrow
\]

when a modification changes both:
- the amount of reaction population that becomes accessible;
- the distribution of internal kinetic timescales.

The heterogeneous example is an **existence proof**, not a fit to BM-HEO.

## BM and Mg interpretation

### Ball milling

Safe experimental interpretation:

**Ball milling is an accessibility-enhancing perturbation whose capacity increase is not equivalent to uniform kinetic acceleration.**

Do not state as fact that ball milling creates a particular slow microscopic state or specifically slows R2.

### Mg incorporation

Safe experimental interpretation:

**Mg suppresses accessible conversion and strongly changes the relaxation amplitude without a proportional change in the effective relaxation timescale.**

Do not map Mg uniquely onto one rate constant.

## HEO positioning

The effect is not claimed to be unique to HEOs.

Conversion chemistry provides the multistep/reconstructive kinetic structure. HEOs provide a useful materials platform because they combine:
- multiple redox-active cations;
- diverse local coordination environments;
- structural reconstruction;
- cation/oxygen rearrangement;
- strong tunability by composition and particle processing.

Preferred positioning:

**The multication and reconstructive HEO system makes a general capacity–kinetics mismatch in heterogeneous conversion chemistry experimentally visible and tunable.**

## Preferred manuscript language

Use:
- accessible capacity / accessible reversible reaction extent;
- conversion-associated kinetics;
- GITT relaxation kinetics;
- effective kinetic timescale;
- kinetically linked but not kinetically equivalent;
- cannot be reduced to a single fast–slow descriptor.

Avoid:
- capacity and kinetics are independent;
- t63 = forward conversion rate;
- more capacity = faster intrinsic kinetics;
- smaller relaxation amplitude = faster kinetics;
- ball milling creates slow states as an established fact;
- unique RDS;
- HEO-exclusive mechanism.

## Terminology lock — 2026-09-25

Manuscript-facing term:

**capacity–kinetics mismatch**

Use `mismatch` rather than `paradox` or `decoupling` as the primary descriptor.

Reason:
- `paradox` is rhetorically stronger than necessary;
- unqualified `decoupling` can imply that capacity and kinetics are independent;
- the present result instead shows that capacity and relaxation share the same conversion network but do not respond as one global fast–slow variable.

Preferred conceptual statement:

**Capacity and relaxation are kinetically linked but not kinetically equivalent.**

Preferred plain-language statement:

**Higher accessible capacity does not necessarily indicate faster conversion kinetics.**

Terminology level:
- title, headings, and broad discussion: `conversion kinetics` for clarity;
- first methodological definition and precise mechanistic discussion: `conversion-associated kinetics probed by GITT relaxation`;
- `t63` remains an effective relaxation timescale, not the forward conversion rate or one microscopic rate constant.

Avoid as primary framing:
- `paradox`;
- unqualified `decoupling`;
- `partial decoupling` unless explicitly qualified as a trend-level description;
- mathematical terms such as `non-monotonic correspondence` or `non-injective mapping` in the manuscript-facing narrative.
