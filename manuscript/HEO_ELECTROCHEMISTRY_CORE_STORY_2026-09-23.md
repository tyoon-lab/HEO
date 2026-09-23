# HEO Electrochemistry Core Story — 2026-09-23

## One-sentence thesis

**Ball milling and Mg incorporation change conversion capacity and conversion-associated relaxation in different directions, revealing that how much conversion is accessed and how fast the converted state relaxes are not governed by a single kinetic axis.**

## The apparent paradox

The simplest experimental observation is:

- ball milling increases accessible conversion-related capacity;
- however, the conversion-associated effective relaxation time, t63, does not become shorter and is often longer.

This creates the central apparent paradox:

**If more conversion is accessed after ball milling, why is the conversion-associated relaxation not faster?**

The answer should not be that capacity and kinetics are unrelated. Rather:

- a shorter t63 is still consistent with faster conversion-related kinetics;
- but t63 is an effective current-off relaxation descriptor, not the forward conversion rate itself;
- conversion capacity can increase because more material/reaction sites become accessible, even when the internal relaxation of the resulting converted states remains slow.

Thus:

**more conversion does not necessarily require faster relaxation.**

## Ball-milling role

Ball milling should be described first in the simplest materials language:

1. particle refinement / surface-area increase raises electrochemically accessible reaction area and conversion accessibility;
2. this increases the amount of conversion that can be accessed and therefore increases capacity;
3. the additional accessible conversion population can include heterogeneous or slower-relaxing internal states;
4. therefore higher capacity can coexist with a longer ensemble effective relaxation time.

Safe conceptual shorthand:

**BM: more conversion, not necessarily faster conversion-associated relaxation.**

Do not claim that ball milling increases capacity because it accelerates the intrinsic elementary conversion kinetics.

## Mg role

Mg provides the complementary perturbation:

1. Mg incorporation lowers the accessible conversion-related capacity;
2. the first-cycle conversion-associated relaxation amplitude is strongly suppressed;
3. however, t63 does not shorten or lengthen in proportion to the capacity loss;
4. in later cycles, Mg-containing and Mg-free samples can approach similar t63 values while their reversible capacities remain very different.

Safe conceptual shorthand:

**Mg: less accessible conversion without a proportional change in conversion-associated relaxation timescale.**

Therefore BM and Mg reveal the same underlying principle from opposite directions.

## Why Figure 7 is needed

Figure 7 should answer one simple question:

**How can more conversion coexist with slower relaxation?**

A multi-step conversion network naturally separates:

- the amount of reaction/state population that becomes accessible during the pulse;
- the internal kinetic rates that control post-interruption relaxation.

In a multi-state system,

d(delta x)/dt = J delta x

and

E(t)-E_eq = sum_i B_i exp(-t/tau_i).

The amplitudes B_i depend on which internal states are populated/excited and how strongly they affect voltage, whereas tau_i are set by kinetic eigen-timescales. Increasing the accessible population can therefore increase capacity while also increasing the contribution of slower-relaxing states.

At open circuit,

j_ext = r1 + r3 = 0

does not require r1 = r3 = 0. Internal counter-current, r1 = -r3 != 0, allows the conversion network to continue reorganizing after the external current is interrupted.

The model is used to establish mechanistic consistency, not to identify a unique RDS or fit unique microscopic rate constants.

## Figure 4–7 narrative

**Figure 4 — first sign of the paradox**
Ball milling raises accessible capacity but does not shorten t63; Mg lowers relaxation magnitude without a corresponding shortening of t63.

**Figure 5 — identify where the unusual relaxation belongs**
The excess relaxation is independently localized to the first-cycle conversion region by dQ/dV. The issue is therefore specifically connected to conversion-associated dynamics rather than to a generic cell relaxation.

**Figure 6 — show that the relaxation is history-dependent**
The conversion-associated amplitude changes strongly between cycles, whereas t63 changes much less. The converted-state relaxation is therefore not a fixed fingerprint determined solely by the initial material.

**Figure 7 — resolve the paradox**
A multi-step microkinetic network shows how reaction accessibility/state population and relaxation timescale can change independently enough that more conversion can coexist with slower relaxation.

## HEO-specific positioning

The capacity–relaxation decoupling is **not claimed to be unique to HEOs**. Multi-step conversion electrodes in general can exhibit different controls over reaction extent and relaxation kinetics.

The HEO relevance is that spinel HEO conversion is especially well suited to expose this behavior because it contains:

- multiple redox-active cations;
- chemically diverse local coordination environments;
- reconstructive conversion involving multiple intermediates/products;
- cation/oxygen rearrangement and heterogeneous local reaction pathways;
- entropy-related structural stabilization/sluggish rearrangement reported in HEO literature.

Therefore the manuscript should position the system as:

**a multicomponent conversion electrode in which the general separation between conversion extent and relaxation kinetics becomes particularly visible.**

Avoid claiming that the decoupling exists only because the material is a HEO.

## Preferred manuscript language

Simple main-text wording:

**Ball milling increases the amount of conversion that can be accessed without accelerating the conversion-associated relaxation, whereas Mg incorporation suppresses accessible conversion without a proportional change in the relaxation timescale.**

Then introduce Figure 7:

**This apparent mismatch between conversion extent and relaxation kinetics motivates a multi-step microkinetic interpretation.**

HEO positioning sentence:

**Although such decoupling is not unique to high-entropy oxides, the multication and structurally heterogeneous nature of HEO conversion provides a natural setting in which reaction accessibility and internal relaxation can become strongly separated.**

## Language boundaries

Use:
- accessible conversion / accessible reaction extent;
- conversion-associated relaxation;
- effective relaxation timescale;
- conversion-related kinetics when explicitly defined through t63.

Avoid:
- t63 = conversion rate;
- more capacity = faster kinetics;
- smaller relaxation amplitude = faster kinetics;
- unique RDS assignment;
- HEO-exclusive mechanism;
- atomistic identification of the effective microkinetic states without direct evidence.
