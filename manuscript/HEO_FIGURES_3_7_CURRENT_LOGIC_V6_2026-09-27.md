# HEO Figures 3–7 — Current Logic, 2026-09-27 (v6, abstract/Figure-4 aligned)

## Manuscript question

**Can higher accessible conversion capacity coexist with slower conversion-associated kinetics, and does conventional GITT apparent diffusivity preserve the same kinetic ordering?**

The paper uses BM and Mg as complementary modifications that respectively increase and decrease accessible conversion capacity, with GITT relaxation as the kinetic probe.

## Figure 3 — Accessible capacity

Purpose:
Establish the capacity differences before interpreting kinetics. Keep Figure 3 strictly on the question **how much reaction is accessed?**

Final main-panel architecture:
- (a) first-cycle voltage profiles for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO;
- (b) first- and second-half-cycle capacity summary with initial Coulombic efficiency;
- (c) absolute specific capacity during 0.1 C cycling under the common electrolyte condition;
- (d) absolute rate capability over the 0.1–5 C sequence and recovery at 0.1 C.

Main result:
- BM increases accessible capacity in Mg-free and Mg-containing HEOs.
- Mg lowers accessible capacity.
- Absolute high-rate capacity and normalized retention must not be conflated.
- First-cycle second-half capacity changes are approximately +28.4% for HEO → BM-HEO, -24.7% for HEO → Mg-HEO, and +26.6% for Mg-HEO → BM-Mg-HEO.

Panel-allocation boundary:
- do not use cycle-resolved $dQ/dV$ as a main Figure 3 panel;
- first-cycle cathodic $dQ/dV$ is reserved for Figure 5, where it has a specific conversion-localization role;
- cycle-resolved $dQ/dV$ evolution belongs in the Supporting Information;
- Coulombic-efficiency evolution and normalized rate retention remain Supporting Information metrics.

Main message:
**Capacity defines how much reaction is accessed; it does not by itself establish the intrinsic conversion rate.**

## Figure 4 — Distinct relationships among accessible capacity, relaxation magnitude, relaxation timescale, and apparent diffusivity

Use:
- $\Delta E_{\mathrm{relax}}$ = 3 s to 60 min recovery
- $t_{63}$ = model-free 63.2% relaxation time
- state-matched relative conventional $D_{\mathrm{app}}$ only for the compositionally identical HEO/BM-HEO pair in the main panel

Panel logic:
- (a) representative measured HEO GITT pulse/rest definition
- (b) conventional $D_{\mathrm{app}}$ ratio versus direct relaxation-rate ratio for HEO/BM-HEO
- (c) median $\Delta E_{\mathrm{relax}}$ versus median $t_{63}$ for all four materials
- (d) first-cycle second-half capacity versus median $t_{63}$ for all four materials

Core values over the common 200–800 mAh g⁻¹ interval:
- HEO: $\Delta E_{\mathrm{relax}}=160.9$ mV, $t_{63}=8.68$ min
- BM-HEO: $176.3$ mV, 11.57 min
- Mg-HEO: $109.5$ mV, 11.01 min
- BM-Mg-HEO: $144.3$ mV, 12.99 min

First-cycle second-half capacities:
- HEO 609.12 mAh g⁻¹
- BM-HEO 782.08 mAh g⁻¹
- Mg-HEO 458.91 mAh g⁻¹
- BM-Mg-HEO 580.83 mAh g⁻¹

Interpretation:
- BM is the primary contradiction: capacity increases while $t_{63}$ lengthens.
- Mg is not a second capacity–rate contradiction: lower capacity and longer $t_{63}$ are directionally consistent with slower relaxation, but the relaxation voltage change simultaneously becomes smaller.
- The Mg result therefore constrains relaxation magnitude and relaxation rate/timescale as non-equivalent information.
- Conventional $D_{\mathrm{app}}$ gives a conflicting indication for BM: $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}}>1$ at 37/37 matched states (median 1.78), whereas $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}}<1$ at 35/37 states (median 0.762).

Main message:
**Ball milling separates accessible capacity from relaxation timescale, Mg separates relaxation magnitude from relaxation timescale, and conventional apparent diffusivity fails to preserve the directly measured BM fast–slow ordering.**

Important:
- Do not call Mg a capacity–kinetics contradiction.
- Do not infer a kinetic rate from relaxation magnitude alone.
- Do not state that diffusion is absent or that GITT is invalid.
- The main $D_{\mathrm{app}}$ panel remains the compositionally identical HEO/BM-HEO comparison.
- A preliminary HEO/Mg-HEO cross-composition $D_{\mathrm{app}}$ check is retained as a robustness note/SI candidate only because composition-dependent prefactors enter.

## Figure 5 — Localization of the excess current-off relaxation

Purpose:
Answer only the question **is the excess GITT current-off response associated with conversion?**

Final main-panel architecture:
- (a) state-resolved first-cycle relaxation with the smooth background used to define the late-stage excess;
- (b) background-subtracted GITT excess and first-cycle cathodic $dQ/dV$ compared on a common voltage axis for all four materials;
- (c) $V_{\mathrm{peak},dQ/dV}$ versus $V_{\mathrm{peak,GITT}}$ with the one-to-one relation.

Nominal peak pairs, with the GITT coordinate defined as the 60 min rest-end voltage at the excess-peak state:
- HEO: 0.545 / 0.527 V;
- BM-HEO: 0.589 / 0.618 V;
- Mg-HEO: 0.419 / 0.387 V;
- BM-Mg-HEO: 0.485 / 0.503 V.

All nominal GITT-excess / $dQ/dV$ peak pairs are within 32 mV. Across the 105 background/window definitions, HEO and Mg peak states are invariant, BM remains narrowly localized, and BM-Mg has a broader peak-position range because its excess is shallow. The robust result is that all three material-induced peak-shift directions are invariant and concordant with $dQ/dV$.

Main message:
**The excess current-off relaxation feature is localized to the conversion region, with material-induced voltage shifts concordant with the first-cycle cathodic $dQ/dV$ shifts.**

Main/SI boundary:
- the peak-amplitude versus FWHM-like-width map is moved to the Supporting Information;
- the 105-condition background/window sensitivity audit, including peak-location sensitivity, remains in the Supporting Information;
- BM-HEO peak-down/width-up and Mg-related excess suppression can be mentioned as secondary descriptors, but amplitude and width are not kinetic rates;
- do not use the shallow, background-sensitive BM-Mg-HEO width as a mechanistic discriminator.

Claim boundary:
conversion-associated, not uniquely assigned to one microscopic conversion step.

## Figure 6 — History dependence

Final main-panel architecture:
- (a) conversion-associated peak state $z_{\mathrm{peak}}$ versus cycle;
- (b) excess peak amplitude versus cycle;
- (c) median $t_{63}$ over $z=0.4$–0.9 versus cycle;
- (d) normalized $A_3/A_1$ versus $t_{63,3}/t_{63,1}$ change map.

The full C1/C2/C3 excess profiles are retained in the Supporting Information rather than repeated in the main figure.

Result:
- peak state shifts from the late first-cycle region ($z\approx0.66$–0.79) toward a common later-cycle region ($z\approx0.50$–0.56);
- amplitude changes strongly;
- $t_{63}$ changes modestly;
- BM capacity-up / longer-$t_{63}$ persists;
- Mg lower reversible capacity persists while later-cycle $t_{63}$ approaches Mg-free values.

Main message:
**Conversion-associated relaxation evolves with reaction history: its state location and magnitude change strongly, whereas its effective relaxation timescale changes comparatively modestly.**

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

while

\[
\nu_1r_1=-\nu_3r_3\neq0
\]

is allowed and R2 can remain finite.

Overall lithiation is conserved while internal populations redistribute. Keep the main panel schematic; numerical partial-current trajectories remain in the SI/model audit.

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
- retain the reference accessible model branch;
- add an additional accessible branch with a slower R2.

Result:
- Qcut 0.65714 (+17.67%)
- t63 15.28 min (+13.63%)

Main message:

\[
Q_{\rm cutoff}\uparrow,\quad t_{63}\uparrow
\]

is physically possible in a heterogeneous multistep conversion network.

Artwork rule:
- panels (c) and (d) use the same axes;
- panel (d) retains the homogeneous-control trajectory as a light dashed reference;
- do not label the added branch “BM-like” in the main artwork;
- keep population weights and the illustrative R2 contrast in the SI/model audit.

Do not infer that BM experimentally creates this exact slow branch or rate ratio.

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
**Does more accessible reaction mean faster kinetics? No. Ball milling raises capacity while relaxation becomes slower. Mg additionally shows that a smaller relaxation voltage change can coexist with slower relaxation, and conventional $D_{\mathrm{app}}$ gives a conflicting BM indication relative to the direct relaxation.**

→ Figure 5:
**Is the excess current-off response conversion-associated? Yes.**

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

> **Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics, while conventional GITT-derived apparent diffusivity indicates faster BM behavior despite the slower directly measured relaxation.**

Bounded mechanistic statement:

> **Microkinetic analysis shows that this behavior can arise naturally from the multistep character of conversion.**

These two statements define the hierarchy of the manuscript:
1. experiment establishes the contradiction;
2. conventional $D_{\mathrm{app}}$ independently fails to preserve the kinetic ordering;
3. conversion localization and cycle history constrain the phenomenon;
4. microkinetics demonstrates physical possibility but does not uniquely identify the microscopic mechanism.


## EIS decision

Cycling EIS is excluded from the manuscript evidence chain. The available spectra contain state-matching and outlier limitations and are not required for the central conclusion. The primary kinetic evidence remains GITT/current-off analysis together with dQ/dV localization.
