# HEO R3 ΔErest hump: cross-chemistry literature audit (2026-11-06)

**Research scope:** conversion FeF3, FeF2, Fe3O4, MnO, SnO2, Si/SiOx/SiO–graphite (conversion+alloying), LiFePO4 and graphite (two-phase/staging). Search goal: distinguish a state-dependent *hump in finite-window rest-voltage recovery amplitude* ΔErest(Q) from (i) nonmonotonic single-rest voltage, (ii) a voltage bump on cycling following rest, (iii) charge/discharge hysteresis, (iv) a peak in dQ/dV or heat and (v) phase transitions that simply happen during rest.

## Central HEO source fact (original GITT, user approved t63 regions)
Pristine HEO R3 pulse 26→50: ΔErest(3s→end60min) 145.1→189.3 mV (+44.2), partitioned 3–60s −9.8, 1–10min +16.5, 10–60min +37.5 mV. Mg-HEO small within-R3 hump +8.6mV; BM variants have no interior R3 maximum. t63 rises throughout R3 in all four; amplitude and timescale encode different observables. The largest nominal region-charge loss across material contrasts remains R3; this is an operational region rather than chemically unique species. Hump is a peak across **pulse states**, NOT nonmonotonic V(t) during one rest.

## Closest directly comparable published observables

1. **Li et al. JACS 2016 FeF3**: *Origins of Large Voltage Hysteresis in High-Energy-Density Metal Fluoride Lithium-Ion Battery Conversion Electrodes*. DOI 10.1021/jacs.6b00061. Fig 4(c) **voltage change during 4-hour GITT rest plotted versus state of lithiation** for microwire and nanowire. Larger microwire relaxation in state range of FeF3→FeF2/LiF→Fe/LiF interpreted with in situ TEM/XAS as heterogeneous spatial progression, phase population imbalance. **Very close metric**. Different shape and time window; not exact evidence of same numerical hump.

2. **Jo et al. Nature Communications 2025 FeF3**: *Guided phase transition for mitigating voltage hysteresis of iron fluoride positive electrodes in lithium-ion batteries*. DOI 10.1038/s41467-025-63676-9. Fig 3(c) **GITT relaxation voltage change versus reaction state** in two FeF3 structures; Fig 3(b) distinguishes persistent charge/discharge gap after long rest from transient relaxation/polarization. Phase pathway and compositional inhomogeneity differ; structural change can alter hysteresis without a proportional change in relaxation voltage. **Close comparison but crucial disambiguation**: relaxation amplitude is not equivalent to residual hysteresis or phase barrier.

3. **Fu et al. JES 2024 SiO–graphite**: *Relaxation Analysis of Silicon Monoxide-Graphite Composite Anode*. DOI 10.1149/1945-7111/ad2956. During zero-current rest, XRD shows graphite LiC6 stage I → stage II; Li migrates from graphite to the more slowly reacting SiO, proving cross-component re-equilibration after stopping current. In later 2024 J Ceramic Soc Japan DOI 10.2109/jcersj2.24051, Li-migration magnitude changes with cycling; in 2025 DOI 10.2109/jcersj2.24104 same phenomenon for nano-Si/graphite. **Direct structure-rest evidence, not demonstrated amplitude hump.**

4. **Skurtveit et al. ACS Materials Lett 2025 graphite and LFP**: *Stepwise Structural Relaxation in Battery Active Materials*. DOI 10.1021/acsmaterialslett.4c02058. Operando XRD with ~1.24s resolution captures graphite Li rearrangement in 3 stages and much slower structural reorganization of LiFePO4 after current interruption. Both insertion/staging and phase-separating material have structural relaxation; distinct kinetic windows do not uniquely identify atomic redox.

5. **Köbbing et al. AFM 2024 silicon**: *Voltage Hysteresis of Silicon Nanoparticles: Chemo-Mechanical Particle-SEI Model*. DOI 10.1002/adfm.202308818. Chemo-mechanical shell model reproduces GITT-rest persistent hysteresis by visco-elastoplastic stress relaxation of Si/SEI; later *Slow Voltage Relaxation of Silicon Nanoparticles with a Chemo-Mechanical Core–Shell Model*, ACS AMI 2024 DOI 10.1021/acsami.4c12976. Long relaxation can reflect mechanical relaxation even without a distinct late chemical step. **Alternative mechanism, not exact hump match.**

6. **Lu et al. JES 2018 SiO**: *Calendar and Cycle Life of Lithium-Ion Batteries Containing Silicon Monoxide Anode*. DOI 10.1149/2.0631810jes. SiO half-cell OCV first decreases during rest then increases as parasitic Li consumption overtakes shorter-time relaxation; **nonmonotonic V(t) within one rest**, fundamentally different shape from HEO ΔErest(Q) hump across consecutive steps. Still warns against assuming all slow recovery = internal phase change.

## Broader phase/conversion precedents

7. **Sasaki et al., Nat Mater 2013 LFP**, *Memory effect in a lithium-ion battery*, DOI 10.1038/nmat3623; and 2017 *Relaxation-Induced Memory Effect of LiFePO4 Electrodes in Li-Ion Batteries*, ACS AMI DOI 10.1021/acsami.7b05852. Post-rest voltage bump/overshoot during continued cycling arises from many-particle phase-population/chemical-potential redistribution. **A cycling bump, not a hump of ΔErest plotted against lithiation coordinate**.

8. **Asenbauer et al., Adv Sustainable Systems 2022 Sn0.9Fe0.1O2-C**, *Comprehensive Approach to Investigate the De-/Lithiation Mechanism of Fe-Doped SnO2 as Lithium-Ion Anode Material*, DOI 10.1002/adsu.202200102. Operando microcalorimetry + GITT variable temperature separate heat components; phase-linked heat features mark conversion and subsequent alloying; parasitic low-potential heat also matters. **Not a GITT amplitude hump**, but establishes why a visible anomaly need not uniquely label a phase.

9. **Nature Communications 2021 metal oxides**, *Non-equilibrium metal oxides via reconversion chemistry in lithium-ion batteries*, DOI 10.1038/s41467-020-20736-6. MnO GITT at C/20 with 64-hour rests (Fig 7) separates overpotential polarization vs nonzero rest-voltage hysteresis; multistep displacement and ionic mobility limitations. Again persistent OCV gaps not the finite-hour ΔErest hump.

10. **Jiang et al., JES 2020 silicon**, *Voltage hysteresis model for silicon electrodes for lithium ion batteries, including multi-step phase transformations, crystallization and amorphization*, DOI 10.1149/1945-7111/abbbba. Different Li–Si phases and strain-dependent phase transitions give distinct voltage plateaus/voltage hysteresis, but do not establish a comparable hump.

11. **Influence of SEI Formation on the Stability and Lithium Diffusion in Si Electrodes**, ACS Omega 2022, DOI 10.1021/acsomega.2c04415. Many Si GITT rests remain far from equilibrium after 1 hour; extending/predicting toward ~3h alters interpretation; warning about fixed 60min HEO finite-window descriptors.

12. **Fe3O4 magnetite phase-change**: *Simulations of Lithium-Magnetite Electrodes Incorporating Phase Change*, Electrochim Acta 2017, DOI 10.1016/j.electacta.2017.04.041; related *Visualizing non-equilibrium lithiation of spinel oxide via in situ transmission electron microscopy*, Nat Commun 2016 DOI 10.1038/ncomms11441. Multiple coexisting lithiated phases, delayed structural rearrangement and sharp fronts support heterogeneity but not a proven HEO-specific phase.

## Mechanistic discrimination / relevance
Working hierarchy of candidate mechanisms for pristine HEO R3:
**H1 strongest supported analogue**: SOC-dependent population of locally dissimilar conversion states/domains leaves a larger delayed Li/phase re-equilibration during rest. FeF3 Fig4c and SiO/graphite structural Li migration are especially useful analogues.
**H2**: mechanical stress / SEI viscoelastic relaxation can contribute to late voltage (Si); HEO lacks a direct mechanical measurement, so keep as alternative.
**H3**: nonuniform quasi-equilibrium voltage slope dQOCV/dQ amplifies a given Li redistribution; HEO previous common-QOCV comparison at 0.50V (HEO 185.5mV > BM 142.6mV despite |slope| HEO < BM) suggests slope **alone** cannot explain that pair if redistributed Li increments equal, but redistribution increments are not measured.
**H4**: parasitic chemistry/finite-rest drift (SiO 2018) can mimic/bias slow recovery; require sign and endpoint/time-window diagnostics.

**Do not claim**: a phase-boundary peak, a new uniquely identified late time constant, specific metal reduction from a hump, equivalence of the LFP memory bump to HEO ΔErest(Q), or proof that Mg/milling homogenizes conversion by the same route.

## Manuscript-ready recommendation
Keep region charge the main result. Following quantified R3 hump+window decomposition, cite Li JACS2016 and Jo NatComm2025 as direct ΔVrest(state) precedents, and Fu JES2024 + Skurtveit ACSML2025 as demonstrations that current interruption allows Li redistribution/structural relaxation. Add one sentence that Si nanoparticle models and SiO rest show mechanical/parasitic competing relaxation; avoid stacking every citation in the main article; SI note can compare all materials. No manuscript modifications were requested in this turn.

## Testable analysis with existing GITT
- Plot late component ΔE(10–60 min) vs *common QOCV* and cumulative pulse charge; subtract smooth potential trend to quantify excess HEO hump.
- Compare normalized (E(t)) at matched QOCV rather than same pulse number and quantify 1–10 / 10–60 min fractions.
- Compare rest-curve end slopes (`dE/dlog(t)` at 30–60 min) to check truncation at 60 min; steep end slope suggests state-dependent right-censoring of slow tail.
- Fit non-negative multi-exponential spectra only after checking sensitivity to cutoff and regularization; no unique reaction/mode assignment.
- No additional operando experiment required for above checks, but direct chemical-phase assignment would require structural spectroscopy.

Research summary prepared from cited public literature on 2026-11-06.
