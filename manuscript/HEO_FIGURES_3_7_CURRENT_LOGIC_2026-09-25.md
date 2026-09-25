# HEO Figures 3–7 — Current Logic, 2026-09-25

## Manuscript question

**Does higher accessible conversion capacity necessarily indicate faster conversion-associated kinetics?**

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

## Figure 4 — Capacity–kinetics mismatch

Use:
- Delta E_relax = 3 s to 60 min recovery
- t63 = model-free 63.2% relaxation time

Result:
- BM: capacity up, t63 longer
- Mg: relaxation magnitude down, t63 not proportionally shorter

Main message:
**The four materials cannot be placed on one global fast–slow conversion axis.**

Important:
This does not mean capacity and kinetics are unrelated.

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
**Conversion-associated kinetics evolves with reaction history, and capacity and t63 remain non-monotonic across cycling.**

## Figure 7 — Microkinetic resolution

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

## Final logical chain

Figure 3:
**How much reaction is accessible?**

→ Figure 4:
**Does more accessible reaction mean faster kinetics? No simple monotonic relationship is observed.**

→ Figure 5:
**Is the anomalous kinetic response actually conversion-associated? Yes.**

→ Figure 6:
**Is it a fixed first-cycle artifact? No; it evolves with cycling while the mismatch persists.**

→ Figure 7:
**Why is this possible? Because capacity and relaxation share the same multistep kinetic network but are not kinetically equivalent observables.**

## Final mechanistic statement

**Capacity and GITT relaxation are kinetically linked, but a heterogeneous multistep conversion network prevents them from being reduced to a single fast–slow kinetic descriptor.**
