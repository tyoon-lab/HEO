# HEO Kinetic Interpretation Decision Lock — 2026-09-26

**Status:** authoritative interpretation lock after TY10, early-cycle EIS review, and Mg-like microkinetic directional closure.

## 1. Experimental facts that define the paper

### Ball milling — primary contradiction

For the Mg-free pair:

- accessible first-cycle capacity increases after ball milling;
- median current-off \(t_{63}\) over the common 200–800 mAh g\(^{-1}\) interval increases from **8.68 min (HEO)** to **11.57 min (BM-HEO)**;
- the same capacity-up / longer-\(t_{63}\) direction is also present in the Mg-containing pair, 11.01 → 12.99 min.

Therefore the primary experimental event is:

> **Ball milling increases accessible conversion capacity while the conversion-associated effective kinetics become slower.**

### Mg incorporation — complementary constraint

Relative to HEO:

- accessible capacity decreases;
- median relaxation amplitude \(\Delta E_{\rm relax}\) decreases from **160.9 to 109.5 mV**;
- median \(t_{63}\) increases from **8.68 to 11.01 min**.

Therefore the Mg result is not a second headline contradiction of the same type as BM. Its role is to show that reaction extent, relaxation amplitude, and relaxation timescale do not collapse onto one scalar kinetic coordinate.

### Conversion localization

The first-cycle GITT excess-relaxation peak and cathodic \(dQ/dV\) peak occur within **32 mV** for all four materials.

This supports a **conversion-associated** assignment of the excess current-off response.

It does **not** uniquely assign the response to nucleation, phase-boundary motion, oxygen migration, metal/Li\(_2\)O formation, or another single microscopic elementary step.

### Conventional-GITT ranking inversion — TY10

For state-matched HEO/BM-HEO points over 200–800 mAh g\(^{-1}\):

- \(D_{\rm app,BM}/D_{\rm app,HEO}>1\) at **37/37** states;
- median \(D_{\rm app,BM}/D_{\rm app,HEO}=1.78\);
- the direct relaxation-rate ratio \(t_{63,\rm HEO}/t_{63,\rm BM}<1\) at **35/37** states;
- median \(t_{63,\rm HEO}/t_{63,\rm BM}=0.762\).

Thus conventional \(D_{\rm app}\) ranks BM-HEO as faster while the directly observed conversion-region relaxation is predominantly slower.

The bounded conclusion is:

> **Conversion kinetics cannot, in general, be ranked by apparent GITT diffusivity alone.**

Do not broaden this to “GITT is invalid” or “Li diffusion is absent.”

---

## 2. How the manuscript uses the term “conversion kinetics”

The manuscript may use **conversion kinetics** or **conversion-associated kinetics** in the conceptual message because the anomalous GITT relaxation is independently localized to the conversion region by \(dQ/dV\).

Operationally, however, the measured kinetic descriptor is:

> **the effective current-off relaxation timescale \(t_{63}\)**

Therefore:

### Supported manuscript-level statement

> **Higher accessible conversion capacity can coexist with slower conversion-associated kinetics.**

### Not supported

- \(t_{63}\) is the forward conversion rate constant;
- \(t_{63}\) is a microscopic diffusion time;
- ball milling uniquely slows bulk phase-boundary velocity;
- one specific elementary conversion step is identified as the cause of the longer \(t_{63}\).

The manuscript should distinguish the experimentally observed **effective conversion-associated kinetics** from any unique microscopic rate constant.

---

## 3. Final EIS decision

Early-cycle EIS was reviewed to test whether it could help separate interfacial and bulk contributions.

The available spectra have several limitations:

- some early-cycle HEO spectra are unstable/outlying;
- equal voltage endpoints do not guarantee equal conversion extent between HEO and BM-HEO;
- overlapping impedance contributions do not support one uniquely defensible equivalent-circuit parameter series;
- the EIS result is not needed to establish the central capacity–kinetics contradiction.

### Locked decision

> **Cycling EIS is excluded from the manuscript evidence chain and from the final SI figure set.**

No kinetic or mechanistic claim in the HEO paper should depend on the EIS data.

The primary kinetic evidence is:

1. GITT current-off relaxation;
2. \(dQ/dV\) localization of the excess relaxation to the conversion region;
3. TY10 state-matched conventional-\(D_{\rm app}\) ranking audit;
4. cycle-history analysis.

EIS may remain in the repository as internal/reviewer-response material only.

---

## 4. Microkinetic model — final scientific role

The model is a **mechanistic-consistency / existence-proof model**, not a fit of microscopic parameters to HEO, BM-HEO, or Mg-HEO.

### Homogeneous control

Global acceleration of all rates gives:

\[
Q_{\rm cutoff}\uparrow,\qquad t_{63}\downarrow.
\]

This reproduces the conventional expectation that faster kinetics increases cutoff-limited capacity and shortens relaxation.

### BM-like existence proof

A heterogeneous-accessibility example gives:

\[
Q_{\rm cutoff}\uparrow,\qquad t_{63}\uparrow.
\]

Current representative result:

- \(Q_{\rm cutoff}\): 0.55845 → 0.65714;
- \(t_{63}\): 13.45 → 15.28 min.

This demonstrates that the BM experimental direction is physically admissible in a heterogeneous multistep conversion network.

It does **not** establish that BM literally creates the illustrative slow population or the chosen \(R_2\) rate difference.

### Mg-like directional existence proof

A secondary SI-only test gives:

\[
Q_{\rm cutoff}\downarrow,\qquad
\Delta E_{\rm relax}\downarrow,\qquad
t_{63}\uparrow.
\]

Current reproducible illustrative result:

- \(Q_{\rm cutoff}\): 0.55845 → 0.39339;
- \(\Delta E_{\rm relax}\): 33.02 → 28.64 mV;
- \(t_{63}\): 13.78 → 16.78 min.

This shows that the Mg experimental combination is physically admissible.

It does **not** map Mg incorporation uniquely onto \(u_3\), \(R_2\), or any microscopic parameter.

### Locked model statement

> **Microkinetic analysis shows that the experimentally observed non-monotonic combinations of accessible conversion, relaxation amplitude, and relaxation timescale can arise naturally from a multistep conversion network.**

---

## 5. Evidence hierarchy and figure logic

### Figure 3
Establish accessible reaction extent:
- BM increases capacity;
- Mg suppresses capacity.

### Figure 4
Establish the primary contradiction and TY10 ranking inversion:
- BM: capacity up, \(t_{63}\) longer;
- conventional \(D_{\rm app}\) ranks BM faster;
- Mg provides the amplitude/timescale complementary constraint.

### Figure 5
Localize the excess GITT response to the conversion region using \(dQ/dV\).

### Figure 6
Show history dependence and persistence of the capacity–kinetics mismatch beyond the first cycle.

### Figure 7
Show physical admissibility:
- homogeneous global-rate control;
- heterogeneous BM-like existence proof.

The Mg-like model remains in SI/model audit rather than becoming a coequal main Figure 7 panel.

---

## 6. Locked manuscript-facing message

### Primary experimental statement

> **Ball milling reveals that higher accessible capacity can coexist with slower conversion-associated kinetics, while conventional GITT analysis gives the opposite kinetic ranking.**

### Complementary Mg statement

> **Mg incorporation suppresses accessible conversion and relaxation amplitude while the effective conversion-associated relaxation remains slower rather than faster.**

### Mechanistic-consistency statement

> **Microkinetic analysis shows that such behavior is physically admissible within a heterogeneous multistep conversion network.**

### General implication

> **Capacity, relaxation amplitude, effective conversion timescale, and apparent diffusivity should not be collapsed onto a single fast–slow kinetic coordinate.**

---

## 7. Current authoritative files

- Main manuscript: \`manuscript/HEO_MANUSCRIPT_V11_AFM_CAPACITY_KINETICS_2026-09-26.md\`
- Supporting Information: \`manuscript/HEO_SUPPORTING_INFORMATION_V9_CAPACITY_KINETICS_2026-09-26.md\`
- Figure logic: \`manuscript/HEO_FIGURES_3_7_CURRENT_LOGIC_V5_2026-09-26.md\`
- TY10 audit: \`modeling/HEO_TY10_CONVENTIONAL_GITT_AUDIT_2026-09-26.md\`
- Microkinetic authority: \`modeling/HEO_CONVERSION_MICROKINETICS_LITERATURE_INFORMED_2026-09-26.md\`
- Mg-like directional audit: \`modeling/HEO_MG_LIKE_MICROKINETIC_DIRECTIONAL_TEST_2026-09-26.md\`

## 8. Reopening rule

Do not reopen the EIS interpretation or redefine \(t_{63}\) as a microscopic rate unless new independent data directly separate the relevant processes.

Future manuscript work should focus on:
- final Figure 1–2 collaborator characterization package;
- remaining Methods metadata;
- final numerical source/provenance freeze for \(dQ/dV\);
- final figure artwork and prose polishing.
