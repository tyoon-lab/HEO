# HEO Manuscript Draft v0.1 — Part 3

**Scope:** GITT current-off analysis + phase-transition interpretation + mechanistic contrast of ball milling and Mg incorporation  
**Date:** 2026-09-18

> Drafting rule: direct observables are stated first. The phase-transition assignment is intentionally assertive but bounded by literature support. A single apparent diffusivity is not used as the causal explanation for the synthesis-dependent response. The latest 2026-09-17 rate dataset is used to constrain interpretation of the GITT relaxation.

---

# 3. Results and Discussion

## 3.3. Current interruption separates polarization magnitude from relaxation time

The larger capacity of BM-HEO does not coincide with uniformly lower polarization or faster relaxation. This distinction is most directly examined during the current-off portion of GITT. During the 10 min current pulse, the measured voltage contains both polarization and the change in equilibrium potential associated with continued lithiation. Once the current is interrupted, additional charge insertion stops and the subsequent voltage evolution predominantly reflects relaxation of the nonequilibrium state generated during the pulse. The current-off response was therefore analyzed directly rather than being reduced only to a conventional apparent diffusion coefficient.

The early current-off region is well represented by a linear dependence of voltage on the square root of time over 3–30 s. The median coefficients of determination are 0.996–0.999 across the four samples, supporting extrapolation to t -> 0 as an empirical current-interruption descriptor. The extrapolated voltage jump was divided by the absolute pulse current to define an apparent instantaneous current-off resistance. This quantity should not be interpreted as a uniquely ohmic resistance because the unresolved earliest response can include electronic, ionic, charge-transfer, and other sub-3-s contributions.

A pronounced ball-milling effect appears during the earliest stage of the first lithiation. Below 200 mAh g−1, the median apparent current-off resistance increases from 296 Ω for HEO to 575 Ω for BM-HEO. The corresponding values are much smaller for the Mg-containing electrodes, 43 Ω for Mg-HEO and 76 Ω for BM-Mg-HEO. The unusually large initial response of BM-HEO is therefore concentrated in the early formation/activation region rather than being a persistent resistance penalty throughout lithiation. Over the common 200–800 mAh g−1 interval, HEO and BM-HEO exhibit nearly identical median apparent current-off resistances of 104 and 103 Ω, respectively. Mg incorporation lowers the same descriptor to 40 Ω for Mg-HEO and 33 Ω for BM-Mg-HEO.

These results rule out a simple explanation in which the additional capacity of BM-HEO originates from uniformly faster interfacial or transport kinetics. Ball milling increases accessible capacity even though the fast current-off response is larger at the beginning of lithiation and essentially unchanged from HEO over the main 200–800 mAh g−1 interval. Conversely, Mg strongly reduces the fast current-off polarization while lowering, rather than increasing, the accessible capacity. The magnitude of the fast polarization is therefore not sufficient to explain the capacity trends.

The longer-time relaxation produces an additional contrast. Over 200–800 mAh g−1, the median 3 s-to-60 min relaxation amplitudes are 160.9, 174.1, 109.3, and 142.3 mV for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO, respectively. Ball milling therefore slightly increases the relaxation amplitude in both composition pairs. Mg incorporation reduces the relaxation amplitude by approximately 32% in the unmilled pair and 18% in the ball-milled pair.

The characteristic relaxation times move differently from the amplitudes. The model-free t63 values over the same capacity interval are 8.68 min for HEO, 11.61 min for BM-HEO, 11.01 min for Mg-HEO, and 13.00 min for BM-Mg-HEO. The corresponding t50 values are 4.28, 6.05, 5.60, and 7.09 min, while t90 remains long for all samples at 34.9–40.3 min. Ball milling thus lengthens the characteristic relaxation despite increasing accessible capacity and maintaining higher galvanostatic capacity across the tested rate sequence. More importantly, Mg lowers the polarization amplitude without shortening the relaxation time. Relative to HEO, Mg-HEO decreases the median relaxation amplitude by ~32% while increasing t63 by ~27%. The same decoupling persists after ball milling, where Mg decreases the amplitude by ~18% but increases t63 by ~12%.

The opposite movement of response amplitude and characteristic time is inconsistent with a single explanation based on accelerated Li diffusion. A smaller polarization does not necessarily indicate a faster relaxing state, and a longer relaxation time does not by itself imply poorer practical rate utilization. In the present HEOs, Mg changes how much nonequilibrium polarization is generated more strongly than how rapidly the remaining polarization disappears. Ball milling, in contrast, increases electrochemical utilization while shifting the long-rest response toward longer characteristic times. This separation between polarization magnitude, relaxation time, and galvanostatic capacity provides the basis for identifying the structural reaction that dominates the late-stage response.

## 3.4. Late-stage polarization is assigned to the spinel-to-rock-salt/conversion transition

The state dependence of the relaxation amplitude provides a more specific mechanistic signature than the average kinetic descriptors. After the large first-lithiation response at low capacity, the HEO relaxation amplitude decreases to approximately 145 mV near 430–450 mAh g−1 and then rises progressively to approximately 189 mV near 820–830 mAh g−1 before decreasing again toward the lower cutoff. The strongest excess response spans approximately the 0.6–0.4 V region of the relaxed GITT trajectory. This late-stage hump is not reproduced as a similarly concentrated feature in BM-HEO and is strongly suppressed in both Mg-containing samples.

The pronounced HEO hump is assigned primarily to the spinel-to-rock-salt/conversion phase transformation. This assignment is supported by two independent bodies of literature. First, in-situ XRD and ex-situ TEM studies on compositionally matching or closely related Fe–Co–Cr–Ni–Mn spinel HEO anodes have directly established lithiation-induced structural evolution from the initial spinel phase through mixed spinel/rock-salt configurations toward a rock-salt-dominated state. Second, phase-transforming battery electrodes are known to require additional overpotential for nucleation, phase-boundary propagation, strain accommodation, and structural reorganization. The coincidence of the present excess polarization with the low-voltage conversion region therefore makes phase evolution a more coherent explanation than a state-independent resistance or a monotonic change in solid-state diffusivity.

A common background-subtraction procedure was used to compare the shape of the late-stage excess relaxation feature across the four samples. The current working quantification gives an excess peak amplitude of approximately 71 mV for HEO and 46 mV for BM-HEO, while the FWHM-like capacity width increases from approximately 350 to 417 mAh g−1 after ball milling. The corresponding capacity-weighted excess-polarization area decreases from approximately 24.1 to 19.0 mWh g−1-equivalent. Because the integrated quantity is constructed from discrete GITT relaxation amplitudes rather than the continuous operating overpotential, it is used only as a comparative capacity-weighted descriptor and is not interpreted as a rigorous dissipated energy.

The combination of lower peak height and broader capacity width indicates that ball milling does not simply remove the transformation. Instead, the transformation-associated polarization is distributed over a wider lithiation interval and becomes less concentrated at a single state. This behavior is consistent with the much larger BET area, milling-induced disorder, strain, and heterogeneous local environments. High-energy milling has also been reported to perturb the spinel/rock-salt structural balance directly in related HEOs, while particle fragmentation in (FeCoNiCrMn)3O4 increases conversion reversibility and interfacial storage during cycling. The present data therefore support a picture in which ball milling broadens the range of local states that participate in conversion and lowers the local maximum of the transition-associated polarization, enabling a larger fraction of the material to be accessed electrochemically.

The broader transformation response is accompanied by slower long-rest relaxation. BM-HEO shows a longer t63 than HEO despite nearly identical fast current-off resistance over 200–800 mAh g−1. The latest rate-capability data nevertheless show that BM-HEO maintains a higher absolute capacity than HEO across the tested C-rate sequence. This contrast is informative rather than contradictory: the characteristic time extracted from a 60 min current interruption reflects recovery of a distributed electrochemical/structural state, whereas rate capability reflects how much charge can be accessed under a continuously driven voltage window. Ball milling can therefore increase accessible interface and reaction utilization while simultaneously producing a broader structural relaxation that requires longer to equilibrate after the current is removed.

## 3.5. Mg suppresses the extent of the conversion transition rather than accelerating Li transport

Mg incorporation produces a fundamentally different modification of the GITT response. In Mg-HEO, the pronounced late-stage excess feature observed in HEO is nearly eliminated. The current background-subtracted analysis gives an excess peak of only ~16 mV and a capacity-weighted excess area of ~4.0 mWh g−1-equivalent, compared with ~71 mV and ~24.1 mWh g−1-equivalent for HEO. Ball milling of the Mg-containing material increases the broad excess response only modestly, to ~21 mV and ~7.1 mWh g−1-equivalent, and does not restore an HEO-like transition hump. Mg therefore alters the underlying reaction pathway more strongly than ball milling can reverse it.

The most consistent interpretation is that Mg stabilizes the oxide/spinel-derived structure and suppresses the extent of the late-stage spinel-to-rock-salt/conversion transformation. This assignment simultaneously explains three observations: the lower accessible capacity, the much smaller transition-associated polarization, and the absence of faster relaxation. Operando synchrotron X-ray microscopy studies on Mg-containing HEO conversion anodes have independently shown that Mg promotes structural retention and mitigates pulverization, while Mg-free compositions can provide higher capacity at the expense of structural stability. Related HEO studies describe electrochemically inactive Mg-derived species as spectator or buffering components during conversion. Although the exact local Mg configuration in the present spinel remains to be finalized from the structural characterization, these established roles provide a physically consistent basis for interpreting the electrochemical response.

Alternative explanations are less complete. Faster Li diffusion could lower polarization but should also tend to shorten the observed relaxation; t63 and t90 do not show this trend. A decrease in purely ohmic or electronic resistance can account for a smaller fast current-off jump but cannot explain the selective disappearance of the late-stage hump together with the loss of conversion capacity. Reduced geometric surface area is also inconsistent with the BET data because Mg-HEO has a larger surface area than HEO before ball milling. SEI differences can contribute substantially to the earliest first-lithiation response, but they do not naturally account for the state-localized suppression of a feature occurring in the established conversion/phase-evolution voltage range. Phase-transition suppression therefore provides the most coherent explanation of the combined data, while the exact microscopic role of Mg within the evolving multiphase structure remains a structural question.

The two synthesis variables consequently act on different aspects of the conversion reaction. Ball milling increases accessible interface and electrochemical utilization while distributing the transition-associated response over a broader capacity interval and lengthening the subsequent long-rest relaxation. Mg incorporation primarily reduces the extent of the conversion-type phase evolution, lowering both the associated polarization and the capacity that it contributes. The comparison shows that accessible capacity, practical rate utilization, polarization amplitude, and relaxation time are distinct observables. Their synthesis-dependent changes cannot be represented adequately by a single monotonic picture of Li diffusivity.

---

# Proposed Figure for Part 3

## Figure X. Current-off polarization and phase-transition relaxation

Suggested main-text panels:

- **a.** Representative GITT pulse/rest with definitions of the current-off intercept, ΔE_relax, and t63.
- **b.** Apparent instantaneous current-off resistance vs cumulative capacity for all four samples.
- **c.** 3 s-to-60 min relaxation amplitude vs cumulative capacity.
- **d.** t63 vs cumulative capacity.
- **e.** Background-subtracted late-stage excess relaxation vs normalized capacity or cumulative capacity.
- **f.** Summary of excess peak amplitude and width, optionally with capacity-weighted excess area.

Supporting Information:

- t50 and t90 vs capacity.
- Early 3–30 s E vs sqrt(t) fit quality and representative fits.
- Terminal-slope descriptor.
- Conventional apparent D_GITT comparison.
- Sensitivity of transition-hump peak/width/area to the background definition before final numerical freeze.

---

# Numerical source table used in this draft

Median values over the common first-lithiation interval 200–800 mAh g−1:

| Sample | Apparent current-off R (Ω) | ΔE_relax (mV) | t50 (min) | t63 (min) | t90 (min) |
|---|---:|---:|---:|---:|---:|
| HEO | 104.0 | 160.9 | 4.28 | 8.68 | 34.87 |
| BM-HEO | 102.9 | 174.1 | 6.05 | 11.61 | 38.97 |
| Mg-HEO | 40.2 | 109.3 | 5.60 | 11.01 | 38.48 |
| BM-Mg-HEO | 33.0 | 142.3 | 7.09 | 13.00 | 40.25 |

Initial 0–200 mAh g−1 apparent current-off resistance:

| Sample | Apparent current-off R (Ω) |
|---|---:|
| HEO | 296 |
| BM-HEO | 575 |
| Mg-HEO | 43 |
| BM-Mg-HEO | 76 |

The 3–30 s E vs sqrt(t) median R2 values are approximately 0.996–0.999 across the four samples.

---

# Literature anchors for Part 3

1. Jia, M.; Zhang, W.; Cai, X.; Zhan, X.; Hou, L.; Yuan, C.; Guo, Z. *Re-understanding the galvanostatic intermittent titration technique: Pitfalls in evaluation of diffusion coefficients and rational suggestions.* **J. Power Sources** 2022, 543, 231843. DOI: 10.1016/j.jpowsour.2022.231843.
2. Chien, Y.-C.; Liu, H.; Menon, A. S.; Brant, W. R.; Brandell, D.; Lacey, M. J. *Rapid determination of solid-state diffusion coefficients in Li-based batteries via intermittent current interruption method.* **Nat. Commun.** 2023, 14, 2289. DOI: 10.1038/s41467-023-37989-6.
3. Jin, G.; Luo, C.; Wang, Z.; Jia, S.; Yu, H.; Zhang, C.; Wang, Q.; Zhang, B.; Wang, Z. *Unraveling phase transition pathway of spinel (FeCoCrNiMn)3O4 high-entropy oxide anodes for long-life Li-ion batteries.* **Mater. Today Chem.** 2025, 48, 102949. DOI: 10.1016/j.mtchem.2025.102949.
4. Komayko, A. I.; Nazarov, E. E.; Tyablikov, O. A.; Fedotov, S. S.; Antipov, E. V.; Nikitina, V. A. *Unraveling the contribution of nucleation to the intercalation energy barrier for phase-transforming Li-ion battery materials.* **J. Power Sources** 2024, 624, 235589. DOI: 10.1016/j.jpowsour.2024.235589.
5. Zheng, Y.; Wu, X.; Lan, X.; Hu, R. *A Spinel (FeNiCrMnMgAl)3O4 High Entropy Oxide as a Cycling Stable Anode Material for Li-Ion Batteries.* **Processes** 2022, 10, 49. DOI: 10.3390/pr10010049.
6. Zhai, F.; Zhu, X.; Zhang, W.; Cao, G.; Zhang, H.; Xing, Y.; Xiang, Y.; et al. *Insight of the evolution of structure and energy storage mechanism of (FeCoNiCrMn)3O4 spinel high entropy oxide in life-cycle span as lithium-ion battery anode.* **J. Power Sources** 2024, 603, 234418. DOI: 10.1016/j.jpowsour.2024.234418.
7. Wang, S.-Y.; Chen, T.-Y.; Kuo, C.-H.; Lin, C.-C.; Huang, S.-C.; Lin, M.-H.; Wang, C.-C.; Chen, H.-Y. *Operando synchrotron transmission X-ray microscopy study on (Mg, Co, Ni, Cu, Zn)O high-entropy oxide anodes for lithium-ion batteries.* **Mater. Chem. Phys.** 2021, 274, 125105. DOI: 10.1016/j.matchemphys.2021.125105.

---

# Drafting decisions / remaining checks

- The current-off resistance values in this draft were recalculated directly from the raw GITT files using a 3–30 s E vs sqrt(t) extrapolation and the actual absolute pulse current for each electrode.
- t50/t63/t90 were recalculated from a common 3 s reference to minimize the original 1 s vs 3 s sampling difference between Mg-free and Mg-containing datasets.
- The phase-transition assignment is the preferred mechanistic explanation, not a claim that GITT uniquely measures phase fraction or a microscopic nucleation barrier.
- The current peak/width/area values are retained as working quantitative results. The baseline-sensitivity audit should be completed before final figure numerical freeze.
- The earlier inference that slower BM relaxation necessarily causes poorer rate capability has been removed because the latest 2026-09-17 rate plot shows higher BM-HEO capacity across the tested rate sequence. The revised interpretation treats long-rest relaxation and practical rate utilization as distinct observables.
- Do not move the exploratory D-only -> D + one compact relaxation mode -> distributed-relaxation analysis into this HEO manuscript unless it later yields a robust synthesis-dependent parameter. That analysis belongs primarily to the separate GITT/EKF study.