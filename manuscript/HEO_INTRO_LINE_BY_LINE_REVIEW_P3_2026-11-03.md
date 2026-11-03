# Introduction line-by-line review — Paragraph 3 (2026-11-04)

**Status:** PI-review recommendation only. Existing full Intro candidate preserved; P1/P2 have separate sentence-level reviews. Main v29 Word, SI v17 and kept Abstract unchanged.

## Review of original P3

1. "Changes in the dominant reaction processes during lithiation can alter the electrode's thermodynamic state and kinetic behavior." Broadly correct but "thermodynamic state" is vague. Use **thermodynamic and kinetic behavior of the electrode**, then specifically introduce slow-rate potential and relaxation time course.
2. "A low-rate voltage profile reflects aspects of the thermodynamics of lithiation..." Concept correct but "aspects" weak. A measured galvanostatic profile combines equilibrium voltage and finite-current polarization, so say it **contains information about reaction thermodynamics**, not that it equals the equilibrium potential. Conversion plateau + overlapping mechanisms may obscure peaks, but **do not** claim all dQ/dV features are absent (source: Luo 2022 had discernible element dependent features).
3. "Changes in kinetics may therefore offer more distinct signatures..." This is a useful hypothesis but overly assertive as universal fact. Replace with **may provide additional contrast where voltage features overlap**.
4. "GITT probes these signatures by measuring..." Retain with plain wording; relaxed voltage and relaxation are separate measured quantities. **Rest-end voltage after 60min is QOCV, not experimentally established equilibrium OCV.**
5. PI-approved phrase retained **verbatim**: "The relaxation amplitude and characteristic relaxation time describe the magnitude and timescale of voltage recovery, respectively, providing complementary information on the evolving electrochemical response."
6. Current text "These relaxation signatures arise from coupled transport, interfacial, and structural processes." Retain physics, integrate with one-sentence diffusion caveat. GITT is kinetic information, but operational t63=first 63.2% of 3s–3600s recovered voltage is **not** an intrinsic single-reaction time constant; ΔErest=|E3600−E3| is finite-window voltage recovery, **not reaction charge or direct resistance**.
7. Diffusivity critique one short sentence with [11–13] only. Kang & Chueh (2021, 10.1149/1945-7111/ac3940), Jia et al. (2022, 10.1016/j.jpowsour.2022.231843), and Zhu & Wang (2010, 10.1021/jp9113333) justify model assumptions and additional mechanisms. Importantly, Zhu & Wang demonstrates special GITT models for phase-transforming electrodes—**avoid blanket "GITT D impossible"**.
8. Final "Direct analysis ... therefore provides a basis..." is defensible if bounded as electrochemical regions (observed landmarks), **not proof of uniquely identified chemical phases**. Link region definition to *regional charge comparison*. NiO precedent was expressly removed per PI decision, so keep out.

## Preferred P3 for discussion

Changes in the dominant reaction processes during lithiation can alter both the thermodynamic and kinetic behavior of the electrode. Low-rate voltage profiles contain information about reaction thermodynamics, but broad conversion plateaus and overlapping reactions often produce similar voltages over substantial charge intervals and poorly separated differential-capacity features [7,23]. Kinetic responses may provide additional contrast where these voltage features overlap. Galvanostatic intermittent titration (GITT) probes this response by recording voltage relaxation after successive current pulses. The voltage at the end of each rest period provides a quasi-open-circuit voltage (QOCV) under the selected protocol. The relaxation amplitude and characteristic relaxation time describe the magnitude and timescale of voltage recovery, respectively, providing complementary information on the evolving electrochemical response. In conversion electrodes, this response includes lithium redistribution, interfacial reactions, and structural relaxation, making estimates based on a single apparent diffusion coefficient difficult to interpret [11–13]. Variations in QOCV and the relaxation descriptors can therefore be used to define electrochemical regions and compare their charge contributions after materials modification.

## Sources (primary/authoritative)
- Luo et al., *Advanced Science* (2022), DOI https://doi.org/10.1002/advs.202201219: operando metal-dependent redox changes and overlapping reactions including broad ~0.5V plateau. A plateau does not imply all electrochemical signatures vanish.
- Kang & Chueh, *JES* (2021), DOI https://doi.org/10.1149/1945-7111/ac3940: reaction overpotentials, non-diffusion-limited transients, interparticle effects on GITT D.
- Jia et al., *JPS* (2022), DOI https://doi.org/10.1016/j.jpowsour.2022.231843: diffusion derivation assumptions.
- Zhu & Wang, *JPCC* (2010), DOI https://doi.org/10.1021/jp9113333: models for phase-transforming GITT electrodes (important counterpoint).
- Kim et al., *J Electrochem Sci Technol* (2022), DOI https://doi.org/10.33961/jecst.2021.00836: GITT yields thermodynamic and kinetic info with finite relaxation periods.

## Internal checks for Results 2.3
- The canonical v28 Results 2.3 currently claims L3 t63 minimum accompanied by a ΔErest minimum. Prior audit shows this is **not true sample-by-sample** (Mg t63 min pulse 24 versus amplitude pulse 18; BM-Mg 34 vs 39). Edit Results to talk of nearby/coherent trend changes, not exact coincident extrema.
- Before treating t63 minima at low amplitude as kinetic landmarks, test **noise sensitivity**: small finite-window ΔErest leads to a small 63.2% threshold and timing uncertainty. Also inspect nonmonotonic rest voltage recovery and interpolation/pulse time resolution.
- Confirm GITT time base in Methods and figures: 10min current pulse, 60min rest; ΔErest = |E(3600s)−E(3s)|; t63 is first crossing of 63.2% of signed E3600−E3 from t=3s, **not** an exponential fitted tau; voltage at t=3600s QOCV.
- Verify electrochemical regions defined using **three coordinated profiles**, not direct chemistry identification. Regional nominal GITT charge distinct from GCD capacity.
- Provisional Intro citations are not numerically aligned with v28 ref list ([22] Wang v28 vs He new, [23] He v28 vs Triolo new); renumber when integrating, not during isolated P3 review.

## Writing preferences
HEO first; no "Together", prefer positive direct language, avoid vague jargon, no first-person; retain *overlapping reaction processes*, *electrochemical regions (R1–R4)*, *dominant reaction processes* as distinct.
