# HEO Figures 3–7 — Current Logic, 2026-09-26 (v4, TY10 + Mg directional closure)

## Manuscript question

**Can higher accessible conversion capacity coexist with slower conversion-associated kinetics, and does conventional GITT apparent diffusivity preserve the same kinetic ordering?**

The paper uses BM and Mg as complementary materials perturbations and GITT relaxation as the kinetic probe.

## Figure 3 — Accessible reaction extent

Purpose:
Establish the capacity differences before interpreting kinetics.

Main result:
- BM increases accessible capacity in Mg-free and Mg-containing HEOs.
- Mg lowers accessible capacity.
- Absolute high-rate capacity and normalized retention must not be conflated.

Main message:
**Capacity defines how much reaction is accessed; it does not by itself establish the intrinsic conversion rate.**

## Figure 4 — Primary contradiction: capacity up, conversion-associated kinetics slower; conventional GITT ranks the opposite

Use:
- $\Delta E_{\mathrm{relax}}$ = 3 s to 60 min recovery
- $t_{63}$ = model-free 63.2% relaxation time
- state-matched relative conventional $D_{\mathrm{app}}$ only for the compositionally identical HEO/BM-HEO pair

Panel logic:
- (a) GITT pulse/rest definition
- (b) conventional $D_{\mathrm{app}}$ ratio versus direct relaxation-rate ratio
- (c) median $t_{63}$ for all four materials
- (d) accessible capacity versus median $t_{63}$

Result:
- BM: capacity up, $t_{63}$ longer
- conventional $D_{\mathrm{app}}$: BM/HEO > 1 at all 37 matched states, median 1.78
- direct relaxation-rate ratio: median 0.762 and < 1 at 35/37 states
- Mg: accessible capacity down, relaxation magnitude down, and $t_{63}$ longer rather than shorter

Main message:
**A conventional apparent diffusivity ranks BM-HEO as faster even while its conversion-associated current-off kinetics are slower. Higher accessible capacity and higher apparent $D$ therefore do not establish uniformly faster conversion kinetics.**

Important:
This does not mean diffusion is absent. It means the conversion response cannot be reduced to one apparent transport parameter.

## Figure 5 — Conversion localization

Compare GITT excess relaxation with first-cycle cathodic dQ/dV.

All GITT-excess / dQ/dV peak pairs are within 32 mV.

Main message:
**The anomalous kinetic response is localized to the conversion region.**

Claim boundary:
conversion-associated, not uniquely assigned to one microscopic conversion step.

## Figure 6 — History dependence

Track C1/C2/C3.

Result:
- amplitude changes strongly;
- t63 changes modestly;
- peak state shifts toward a common later-cycle region;
- BM capacity-up / longer-t63 persists;
- Mg lower reversible capacity persists while later-cycle t63 approaches Mg-free values.

Main message:
**Conversion-associated kinetics evolves with reaction history, and capacity and t63 do not vary in parallel across cycling.**

## Figure 7 — Microkinetic existence proof

### (a) Coarse-grained conversion network

\[
O\rightleftharpoons I\rightleftharpoons I^*\rightleftharpoons C
\]

R1/R3 are Faradaic; R2 is a coarse-grained structural/reconstruction coordinate.

### (b) Current-off redistribution

At OCV:

\[
j_{\rm ext}=F(\nu_1r_1+\nu_3r_3)=0
\]

but finite opposing partial currents and R2 can remain.

Overall lithiation is conserved while internal populations redistribute.

### (c) Homogeneous kinetic control

All rates scaled together:

- rate scale 0.5: Qcut 0.2993, t63 22.45 min
- rate scale 1.0: Qcut 0.5585, t63 13.45 min
- rate scale 2.0: Qcut 0.8322, t63 6.95 min

Main message:

\[
\text{uniformly faster kinetics}
\Rightarrow
Q_{\rm cutoff}\uparrow,\quad t_{63}\downarrow
\]

Thus capacity remains kinetic-dependent.

### (d) Heterogeneous-accessibility existence proof

Reference:
- fast population weight 0.65
- Qcut 0.55845
- t63 13.45 min

Illustrative modified case:
- retain fast population
- add accessible population weight 0.15
- slower R2 only for the added illustrative population

Result:
- Qcut 0.65714 (+17.67%)
- t63 15.28 min (+13.63%)

Main message:

\[
Q_{\rm cutoff}\uparrow,\quad t_{63}\uparrow
\]

is physically possible in a heterogeneous multistep conversion network.

Do not infer that BM experimentally creates this exact slow population or rate ratio.

### Mg-like directional test — SI only

A secondary calculation uses the same network to test the complementary Mg combination. An illustrative perturbation that suppresses deeper conversion while lengthening the reconstruction timescale gives

\[
Q_{\rm cutoff}\downarrow,\qquad
\Delta E_{\rm relax}\downarrow,\qquad
t_{63}\uparrow.
\]

This is kept in the SI / model audit rather than added as another main Figure 7 panel. It demonstrates physical admissibility only and is not a parameter mapping for Mg incorporation.

## Final logical chain

Figure 3:
**How much reaction is accessible?**

→ Figure 4:
**Does more accessible reaction mean faster kinetics? No. Ball milling raises capacity while the conversion-associated relaxation becomes slower, and conventional $D_{\mathrm{app}}$ gives the opposite kinetic ranking from the direct relaxation.**

→ Figure 5:
**Is the anomalous kinetic response actually conversion-associated? Yes.**

→ Figure 6:
**Is it a fixed first-cycle artifact? No; it evolves with cycling while the mismatch persists.**

→ Figure 7:
**Why is this possible? Because capacity and relaxation share the same multistep kinetic network but are not kinetically equivalent observables.**

## Final mechanistic statement

**Microkinetic analysis shows that the observed capacity–kinetics mismatch can arise naturally from multistep conversion. Capacity, relaxation amplitude, effective conversion timescale, and apparent diffusivity should not be collapsed onto a single fast–slow kinetic coordinate.**


## Literature-positioning implication added in v2

Performance-oriented conversion-anode and HEO literature commonly uses conventional GITT-derived $D_{\mathrm{Li}}$ as a kinetic comparator. The manuscript now distinguishes this common practice from the present state-matched finding that $D_{\mathrm{app}}$ and direct current-off relaxation give opposite kinetic rankings.

Final general statement:

**Conversion kinetics cannot, in general, be ranked by apparent GITT diffusivity alone.**

Claim boundary:
- do not state that GITT is invalid for conversion electrodes;
- do not state that diffusion is absent;
- do not state that all prior conversion-anode interpretations are wrong;
- treat $D_{\mathrm{app}}$ as an operational transport descriptor whose relation to overall conversion kinetics requires independent validation.


## Locked manuscript-facing message

Primary experimental statement:

> **Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics, while conventional GITT analysis gives the opposite kinetic ranking.**

Bounded mechanistic statement:

> **Microkinetic analysis shows that this behavior can arise naturally from the multistep character of conversion.**

These two statements define the hierarchy of the manuscript:
1. experiment establishes the contradiction;
2. conventional $D_{\mathrm{app}}$ independently fails to preserve the kinetic ordering;
3. conversion localization and cycle history constrain the phenomenon;
4. microkinetics demonstrates physical possibility but does not uniquely identify the microscopic mechanism.


## EIS decision

Cycling EIS is excluded from the manuscript evidence chain. The available spectra contain state-matching and outlier limitations and are not required for the central conclusion. The primary kinetic evidence remains GITT/current-off analysis together with dQ/dV localization.
