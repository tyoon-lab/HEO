# HEO Introduction Lock — 2026-09-28

## Status

PI line-by-line review of the Introduction is provisionally complete for the current manuscript round.

Authority:
- Main manuscript: `HEO_MANUSCRIPT_V16_AFM_CAPACITY_KINETICS_2026-09-28.md`
- Abstract: `HEO_ABSTRACT_LOCK_2026-09-28.md`
- This file records the Introduction text and the reasoning decisions that should survive a chat/session restart.

Reopen the Introduction only if new data, a body-section review, or journal positioning changes one of its scientific premises.

## Reviewed Introduction

# 1. Introduction

Conversion-type anodes can achieve high theoretical capacities by accommodating multiple Li ions and electrons through conversion reactions. This high capacity, however, comes with extensive structural and chemical reconstruction during conversion, involving bond rearrangement, nucleation and growth of new phases, and redistribution of cations and oxygen. These coupled processes can introduce substantial kinetic limitations, leading to polarization, incomplete reaction, and rate-dependent capacity. Understanding how material modifications affect these kinetics is therefore important for interpreting their influence on electrochemical performance.

The galvanostatic intermittent titration technique (GITT) is widely used to estimate apparent Li-ion diffusion coefficients, $D_{\mathrm{app}}$, from the voltage response to a current pulse and subsequent relaxation. These $D_{\mathrm{app}}$ values are often compared across compositions, structures, and processing conditions as kinetic descriptors, including for conversion-type electrodes and high-entropy oxides (HEOs).[1–5] However, conventional GITT diffusion analysis relies on assumptions that can be distorted by finite reaction kinetics, phase transformation, or other non-diffusive contributions.[6–9] For reconstructive conversion reactions, the resulting $D_{\mathrm{app}}$ may therefore not track the directly observed relaxation rate.

The GITT relaxation can also be examined directly without converting the measured voltage response into a diffusion coefficient. Two readily accessible quantities are the magnitude of the voltage relaxation, $\Delta E_{\mathrm{relax}}$, and a characteristic relaxation time, which quantify the extent and timescale of the current-off voltage response, respectively. Such quantities do not require specification of a solid-state diffusion model and can therefore provide complementary information when the origin of the transient is not purely diffusional. Accessible capacity provides a separate measure of how much conversion is reached under load. Comparing accessible capacity with these direct relaxation descriptors therefore provides a simple test of whether a modification that increases the accessible extent of conversion also produces faster relaxation kinetics.

Spinel HEOs provide a useful material system for examining this relationship. Spinel (FeCoNiCrMn)₃O₄ is a conversion-type anode in which multiple redox-active cations share a common oxide structure.[1,10–13] Its lithiation involves substantial reconstruction, including progressive formation of metallic species, Li₂O, and rock-salt-like phases accompanied by cation and oxygen rearrangement.[14–16] Ball milling and Mg incorporation provide complementary modifications of this conversion behavior. Milling increases surface area and has been associated with enhanced conversion reversibility,[1,17] whereas Mg-containing HEOs have been reported to exhibit greater structural retention but lower accessible capacity.[18–20] Because these modifications change accessible conversion in opposite directions, they provide a useful basis for testing whether capacity changes are accompanied by corresponding changes in relaxation kinetics.

Here, pristine HEO, ball-milled HEO (BM-HEO), Mg-containing HEO (Mg-HEO), and BM-Mg-HEO are compared to determine the relationships among accessible conversion capacity, GITT relaxation, and conventional GITT-derived apparent diffusivity. The apparent diffusivity is compared with the directly measured relaxation to determine whether the two indicate the same kinetic trend. Differential-capacity analysis identifies whether the anomalous relaxation is associated with conversion, and a literature-grounded four-step microkinetic model tests whether higher accessible capacity and slower relaxation can coexist within a homogeneous multistep conversion network.

## Paragraph architecture

### P1 — physical problem before method
Establish why conversion anodes can deliver high capacity and why reconstructive conversion creates kinetic limitations.

PI decisions:
- do not open the Introduction with the same sentence as the Abstract;
- do not begin with GITT;
- do not state the BM mismatch as established background;
- enumerate the major reconstructive processes once, then avoid repeating the same list later.

### P2 — common descriptor and its conditional interpretation
Introduce conventional GITT-derived apparent diffusivity because it is widely used as a kinetic descriptor.

Required logic:
- $D_{\mathrm{app}}$ is an apparent Li-ion diffusion coefficient derived from the pulse/rest voltage response;
- conventional diffusion extraction is assumption dependent and can be distorted by finite reaction kinetics, phase transformation, or other non-diffusive contributions;
- for reconstructive conversion, $D_{\mathrm{app}}$ may not track the directly observed relaxation rate.

Boundary:
- do not say that GITT or $D_{\mathrm{app}}$ is invalid;
- do not imply that diffusion is absent;
- do not imply that slower overall relaxation must automatically produce smaller $D_{\mathrm{app}}$.

### P3 — direct relaxation descriptors and the comparison question
Use the measured GITT relaxation directly rather than immediately converting it to one diffusion coefficient.

Keep the physical roles separate:
- $\Delta E_{\mathrm{relax}}$: magnitude/extent of the current-off voltage response;
- characteristic relaxation time: timescale of the response;
- accessible capacity: how much conversion is reached under load.

Do not call relaxation magnitude a rate. Do not equate an operational relaxation time with one microscopic rate constant.

### P4 — why HEO/BM/Mg provide the test
Introduce the HEO system only after the scientific comparison is clear.

The paragraph establishes:
- reconstructive lithiation of the spinel HEO;
- ball milling and Mg incorporation as complementary material perturbations;
- opposite changes in accessible conversion as useful experimental leverage.

Do not re-list all conversion processes already given in P1.

### P5 — present study without itinerary overload
State the four samples, the three observables being compared, and the minimum analysis route.

PI decisions:
- use `pristine HEO` at first definition; avoid `bare` and `fresh` for the unmodified reference;
- omit unexplained method jargon such as `state-matched` from the Introduction unless it is needed;
- use `literature-grounded four-step microkinetic model` when the model is introduced because the step assignments now have a direct metal-oxide conversion precedent;
- avoid repeating the previous paragraph's statement that BM increases and Mg decreases accessible conversion;
- `same kinetic trend` is clearer here than a bare phrase such as `kinetic ordering`.

## Line-by-line writing decisions reinforced in this review

1. A sentence should add a new logical function, not merely paraphrase the previous sentence.
2. Use `however` where a real contrast occurs, but do not stack repeated contrast markers in adjacent sentences.
3. After a detailed physical list has been given once, use a compact referent such as `coupled processes` rather than re-enumerating it.
4. Prefer plain physical wording over abstract nouns such as `manifestation`, `decoupling`, or `ordering` when the same point can be stated directly.
5. Keep notation consistent: use $D_{\mathrm{app}}$ after first definition rather than alternating with $D_{\mathrm{Li}}$.
6. Avoid a colon construction when a normal sentence is clearer.
7. Use lithiation/delithiation when the electrochemical direction is established; avoid neutral first-/second-half-cycle wording in the current Figure 3 text.
8. Abstract and Introduction must be synchronized in scientific logic but should not read as copied versions of one another.

## Project-specific boundaries

These are HEO-specific and should not be generalized mechanically:
- BM-HEO is the primary capacity-up / slower-relaxation contradiction.
- Mg-HEO is complementary: capacity decreases and relaxation slows, while relaxation magnitude also decreases.
- $D_{\mathrm{app}}$ is challenged by comparison with directly observed relaxation, not dismissed as physically meaningless.
- Figure 5 is needed before using `conversion-associated relaxation` as a localized interpretation.


## Reference synchronization note

The reviewed Introduction is synchronized to the v16 main-reference numbering (24 cited main references). General GITT assumptions/pitfalls are now cited separately from HEO examples.
