# Supporting Information

## Contrasting Roles of Mg Incorporation and Ball Milling in Spinel High-Entropy Oxide Anodes: Phase Evolution, Polarization, and Electrochemical Utilization

**Date:** 2026-09-19  
**Status:** SI draft aligned to `HEO_MANUSCRIPT_V3_POLISHED_2026-09-19.md`  
**Purpose:** technical completeness, auditability, robustness tests, and claim-boundary support for the main manuscript.

> Values below are included only where they are already verified from the project source files. Missing historical or collaborator-generated metadata are explicitly marked and are not inferred.

---

# S1. Additional structural and compositional characterization

## S1.1. XRD refinement and lattice parameters

The main text uses the current XRD peak positions only to establish a modest Mg-associated lattice perturbation and milling-induced peak broadening. Final phase fractions, refined lattice parameters, and uncertainty should be reported here after the collaborator dataset is frozen.

**[[YOO GROUP INPUT REQUIRED — Table S1: nominal composition, ICP-OES composition, refined lattice parameter, phase assignment/phase fraction, and refinement statistics for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO.]]**

**[[YOO GROUP INPUT REQUIRED — Figure S1: full XRD patterns and final Rietveld/refinement comparison.]]**

The present manuscript does not assign Mg to a unique crystallographic site from the small peak shift alone.

## S1.2. Microscopy and elemental analysis

**[[YOO GROUP INPUT REQUIRED — Figure S2: additional SEM/TEM images and particle/domain-size statistics.]]**

**[[YOO GROUP INPUT REQUIRED — Figure S3: final HRTEM/SAED indexing and corresponding lattice-spacing table.]]**

**[[YOO GROUP INPUT REQUIRED — Figure S4: EDS elemental maps for all four compositions.]]**

The preliminary CoGa2O4 HRTEM assignment is not chemically applicable to the Ga-free synthesis and must not be included.

## S1.3. XPS

**[[YOO GROUP INPUT REQUIRED — Figure S5 and Table S2: final XPS spectra, fitting model, binding energies, and compositional comparison if XPS is retained in the final paper.]]**

The batch-dependent Cr6+ feature should not be interpreted mechanistically unless its remeasurement and fitting are reproducible.

## S1.4. N2 adsorption/desorption and BET analysis

**Figure S6.** Full N2 adsorption/desorption isotherms and BET fitting ranges for the four samples.

Verified BET surface areas used in the main text:

| Sample | BET surface area (m2 g-1) |
|---|---:|
| HEO | 3.94 |
| BM-HEO | 18.159 |
| Mg-HEO | 6.49 |
| BM-Mg-HEO | 16.64 |

---

# S2. Electrochemical controls and additional performance data

## S2.1. Interfacial-capacitance comparison

Cyclic voltammetry was acquired in the nominal non-faradaic region of 3.0-3.3 V at 10, 20, 40, 60, 80, and 100 mV s-1. The original calculation converted double-layer capacitance to a nominal interface area using 40 uF cm-2. Because this specific capacitance is not independently established for the porous composite electrode, the resulting values are used only as a relative interfacial-accessibility metric.

| Sample | Nominal relative interface metric (cm2) |
|---|---:|
| HEO | 4.18 |
| BM-HEO | 30.17 |
| Mg-HEO | 6.56 |
| BM-Mg-HEO | 39.68 |

**Figure S7.** Current versus scan-rate regressions used for the relative interfacial-capacitance comparison.

**Table S3.** Fitted slopes, goodness of fit, and sensitivity of nominal area to the assumed specific capacitance.

## S2.2. First-cycle profiles and half-cycle convention

Instrument-reported first-cycle capacity pairs and initial Coulombic efficiencies:

| Sample | First half-cycle pair (mAh g-1) | ICE (%) |
|---|---:|---:|
| HEO | 901.25 / 609.12 | 67.59 |
| BM-HEO | 1056.10 / 782.08 | 74.05 |
| Mg-HEO | 731.15 / 458.91 | 62.77 |
| BM-Mg-HEO | 944.07 / 580.83 | 61.52 |

**[[YOON LAB INPUT REQUIRED — verify WonATech charge/discharge convention before replacing the neutral “half-cycle pair” terminology with lithiation/delithiation labels.]]**

**Figure S8.** Full first-cycle and selected-cycle voltage profiles.

## S2.3. FEC control, rate capability, dQ/dV, and cycling EIS

**Figure S9.** Cycling comparison with and without 10 wt% FEC. The no-FEC control is used to show the increased interphase burden of the higher-area BM material rather than to assign a unique SEI chemistry.

**Figure S10.** Detailed rate-capability profiles and recovery at 0.1 C.

**[[YOON LAB INPUT REQUIRED — exact C-rate sequence, cycles per rate, and 1 C capacity basis.]]**

**Figure S11.** dQ/dV evolution if retained in the final SI.

**Figure S12.** Cycling EIS series with state-matching/outlier note. The EIS data are supporting evidence only because several spectra are unstable or outlying and do not support one uniquely defensible equivalent-circuit parameter series.

**Figure S13.** Additional post-cycle SEM.

---

# S3. Current-off analysis: operational definitions and robustness

## S3.1. Common GITT protocol

- First-lithiation GITT block.
- Applied current: 100 mA g-1.
- Pulse duration: 600 s.
- Open-circuit rest: 3600 s.
- Nominal capacity increment per pulse: 16.667 mAh g-1.
- Common current-off reference: 3 s.
- Early current-off fit: 3-30 s after current interruption.

The Mg-free datasets are sampled at approximately 1 s in the GITT region, whereas the Mg-containing datasets are sampled at approximately 3 s. A common 3 s reference is therefore used for the finite-window relaxation descriptors.

## S3.2. Early current-off fit

The early current-off voltage is represented empirically as

\[
E(t)=a+b\sqrt{t}.
\]

The intercept \(a\) is extrapolated to \(t\rightarrow 0\), and the apparent fast current-off resistance is defined as

\[
R_{\mathrm{off,app}}
=
\frac{a-E_{\mathrm{pulse,end}}}{|I|}.
\]

This quantity is an operational descriptor. It is not assigned uniquely to ohmic resistance, charge-transfer resistance, or intrinsic solid-state diffusion.

Median \(R^2\) values of the 3–30 s \(E\)-versus-\(\sqrt{t}\) fit are:

| Sample | Median \(R^2\) |
|---|---:|
| HEO | 0.9995 |
| BM-HEO | 0.9992 |
| Mg-HEO | 0.9994 |
| BM-Mg-HEO | 0.9985 |

**Figure S14.** Representative \(E\) versus \(\sqrt{t}\) fits at selected states for the four samples.

## S3.3. Finite-window relaxation descriptors

The finite-window relaxation amplitude is

[
Delta E_{mathrm{relax}}
=
E_{60,mathrm{min}}-E_{mathrm{off},3,mathrm{s}}.
]

Model-free (t_{50}), (t_{63}), and (t_{90}) are defined as the first times at which 50%, 63.2%, and 90% of the observed 3 s-to-60 min voltage recovery are reached. These descriptors do not assume single-exponential relaxation.

Raw-reconstructed medians:

| Sample | Roff, 0-200 mAh g-1 (ohm) | Roff, 200-800 mAh g-1 (ohm) | DeltaErelax, 200-800 (mV) | t63, 200-800 (min) |
|---|---:|---:|---:|---:|
| HEO | 308.1 | 106.4 | 160.9 | 8.68 |
| BM-HEO | 592.7 | 106.5 | 176.3 | 11.57 |
| Mg-HEO | 44.5 | 40.2 | 109.5 | 11.01 |
| BM-Mg-HEO | 93.8 | 33.0 | 144.3 | 12.99 |

**Figure S15.** Full first-lithiation GITT traces.

**Figure S16.** (t_{50}), (t_{63}), and (t_{90}) versus cumulative capacity.

**Table S4.** Current-off descriptors by selected capacity interval.

---

# S4. Late-stage transition-associated excess analysis

## S4.1. State normalization and background definition

For the background-sensitivity analysis, the common state coordinate is normalized first-lithiation capacity,

\[
z=Q/Q_{\max}.
\]

A smooth exponential background is fitted independently to each sample using the two state windows

\[
z=0.20-0.40
\]

and

\[
z=0.90-1.00.
\]

The background form is

\[
\eta_{\mathrm{bg}}(z)
=
c+a\exp(-z/\tau).
\]

The late-stage transition-associated excess response is defined over \(0.40\le z\le0.90\) as

\[
\eta_{\mathrm{excess}}(z)
=
\max\left[\Delta E_{\mathrm{relax}}(z)-\eta_{\mathrm{bg}}(z),0\right].
\]

This definition excludes the dominant early first-lithiation formation/activation response and isolates the late-stage feature discussed in the main text.

## S4.2. Extracted metrics

| Sample | Peak excess polarization (mV) | FWHM-like width (mAh g-1) | Normalized excess area (mV) | Capacity-weighted excess metric (mV mAh g-1) |
|---|---:|---:|---:|---:|
| HEO | 70.77 | 354.13 | 22.07 | 23909.67 |
| BM-HEO | 44.07 | 430.17 | 14.13 | 17901.01 |
| Mg-HEO | 15.91 | 250.29 | 4.94 | 3955.99 |
| BM-Mg-HEO | 21.10 | 391.78 | 7.58 | 7077.32 |

The capacity-weighted excess quantity is a comparative polarization descriptor, not a dissipated-energy measurement.

**Figure S17.** Background fits and background-subtracted excess curves for each sample.

**Figure S18.** Sensitivity of peak amplitude, width, and area to reasonable background/window choices.

**Table S5.** Peak/width/area values and sensitivity ranges after the final background audit.

The GITT signal itself does not uniquely separate nucleation, phase-boundary motion, strain, or other microscopic contributions. The late-stage feature is assigned primarily to the spinel-to-rock-salt/conversion transformation from its voltage/state localization together with independent structural literature on the same five-cation HEO family.

---

# S5. Single-diffusivity comparator

The main text uses the Mg response as a directional contradiction to a one-parameter diffusion interpretation. The numerical comparison below is illustrative rather than a fit.

For otherwise comparable geometry and pulse conditions, use the common short-time directions

\[
\eta_D\propto D^{-1/2},
\qquad
\tau_D\propto D^{-1}.
\]

HEO and Mg-HEO have median relaxation amplitudes of 160.9 and 109.5 mV, respectively. If this amplitude decrease were attributed entirely to faster diffusion,

\[
\frac{D_{\mathrm{Mg}}}{D_{\mathrm{HEO}}}
\approx
\left(\frac{160.9}{109.5}\right)^2
\approx2.16.
\]

The corresponding diffusion-time prediction would be

\[
t_{63,\mathrm{Mg}}
\approx
\frac{8.68}{2.16}
\approx4.0\ \mathrm{min},
\]

which is opposite to the measured 11.01 min.

Conversely, matching the measured relaxation-time increase gives

\[
\frac{D_{\mathrm{Mg}}}{D_{\mathrm{HEO}}}
\approx
\frac{8.68}{11.01}
\approx0.79,
\]

which would predict a larger diffusion-associated polarization of approximately 181 mV rather than the measured 109.5 mV.

This test does not prove that diffusion is absent. It shows that one varying \(D\) cannot simultaneously explain the observed directions of polarization amplitude and relaxation time.

**Figure S19.** Conventional apparent \(D_{\mathrm{GITT}}\) comparison, if included, should be shown only as a conventional comparator and not as the central causal descriptor.

# S6. Spatial phase-field mechanism-sufficiency model

## S6.1. Governing equations

The dimensionless free-energy density is

\[
f=
c\ln c +(1-c)\ln(1-c)
+W\phi^2(1-\phi)^2
+K(c^*-c)\phi
+G_{\mathrm{Mg}}\phi
+\frac{1}{2}B_{\mathrm{el}}q_{\mathrm{el}}(r)\phi^2
-S_{\mathrm{surf}}w_{\mathrm{surf}}(r)\phi
+\frac{\kappa}{2}|\nabla\phi|^2.
\]

The reduced spatial weights are

\[
q_{\mathrm{el}}(r)
=
1-\exp[-(1-r)/\ell_{\mathrm{relief}}],
\]

\[
w_{\mathrm{surf}}(r)
=
\exp[-(1-r)/\ell_{\mathrm{wet}}].
\]

Li chemical potential:

\[
\mu_c
=
\ln\frac{c}{1-c}-K\phi.
\]

Conserved Li dynamics:

\[
\frac{\partial c}{\partial t}
=
-\nabla\cdot J,
\qquad
J=-D_{\mathrm{eff}}\nabla\mu_c.
\]

Nonconserved structural dynamics:

\[
\frac{\partial\phi}{\partial t}
=
-M_\phi\frac{\delta G}{\delta\phi}.
\]

The coherency term is a reduced energetic coordinate rather than a full mechanical-equilibrium elasticity solution.

## S6.2. Numerical protocol

- Spherical finite-volume radial model.
- Radial cells in frozen directional gate: \(N=18\).
- Diffuse-interface parameter: \(\kappa=0.002\).
- 600 s inward Li-flux pulse.
- 3600 s zero-flux rest.
- 50 pulse/rest states.
- Dimensionless inward flux: \(j=9\times10^{-6}\).
- Median \(\Delta\bar c\) per pulse: approximately 0.0162.
- BDF primary stiff solver with Radau fallback for sharp transition events.
- Two voltage-like readouts tested:
  \[
  V_{\mathrm{vol}}\propto-\langle\mu_c\rangle_V,
  \qquad
  V_{\mathrm{surf}}\propto-\mu_c(r=R).
  \]

The model is a directional mechanism-sufficiency test and not an absolute voltage fit. No formal inverse parameter identification is claimed. Parameters were selected through constrained directional tests and frozen once the required ordering was reproduced.

## S6.3. Frozen effective coordinates

| Sample | \(D_{\mathrm{eff}}/R^2\) | \(M_\phi\) | \(W\) | \(K\) | \(G_{\mathrm{Mg}}\) | \(B_{\mathrm{el}}\) | \(S_{\mathrm{surf}}\) | \(\ell_{\mathrm{relief}}\) | \(\ell_{\mathrm{wet}}\) |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| HEO | 0.0015 | 0.015 | 0.60 | 1.80 | 0 | 0.20 | 0.08 | 0.08 | 0.06 |
| Mg-HEO | 0.0015 | 0.0006 | 0.80 | 1.80 | 0.38 | 0.20 | 0.08 | 0.08 | 0.06 |
| BM-HEO | 0.0030 | \(0.008\exp(-0.6x)\) | 0.50 | 1.60 | 0 | 0.25 | \(0.15+0.06x\) | 0.20 | 0.12 |
| BM-Mg-HEO | 0.0030 | \(0.0008\exp(-0.6x)\) | 0.70 | 1.70 | 0.30 | 0.25 | \(0.22+0.075x\) | 0.20 | 0.12 |

For BM-HEO and BM-Mg-HEO, \(x\sim N(0,1)\) is represented by 11 equal-probability Gaussian quantiles.

These coordinates are effective, non-unique, hypothesis-level quantities. They should not be interpreted as independently measured microscopic constants.

## S6.4. Why Mg requires two coordinates

A (G_{mathrm{Mg}})-(M_phi) scan showed:

- stabilization alone suppresses the transformed fraction but can make residual relaxation too fast;
- low structural mobility alone slows relaxation but does not sufficiently suppress the transition response;
- combined stabilization and lower residual structural mobility reproduce the required direction of small transition response, reduced transformed fraction, and slower relaxation.

## S6.5. Why BM requires a distribution

A single ball-milled particle with only shorter effective transport length or easier surface transformation does not reproduce all experimental directions. The accepted BM representation uses a joint distribution of local transition/surface condition and structural mobility. This permits easier local transformation and slow ensemble relaxation to coexist.

---

# S7. Model convergence, readout robustness, and claim boundaries

## S7.1. Gaussian-quantile convergence

For BM-HEO:

| Quantiles | Peak proxy | Moment width in c-bar | Peak t63 (min) |
|---:|---:|---:|---:|
| 7 | 0.1905 | 0.0838 | 26.91 |
| 11 | 0.1824 | 0.0847 | 26.91 |

The surface-chemical-potential readout gives similarly stable moment widths. Eleven probability quantiles are therefore sufficient for the frozen directional model.

## S7.2. Frozen four-sample directional result

Volume-(mu) readout:

| Sample | Peak / HEO | Moment width | t63 at peak (min) | Final transformed-state proxy |
|---|---:|---:|---:|---:|
| HEO | 1.000 | 0.0683 | 22.03 | 1.000 |
| BM-HEO | 0.237 | 0.0847 | 26.91 | 1.000 |
| Mg-HEO | 0.136 | 0.0308 | 40.17 | 0.214 |
| BM-Mg-HEO | 0.188 | 0.0498 | 40.17 | 0.824 |

The same directional ordering is obtained with the surface-(mu) readout.

Directional criteria:

- BM peak < HEO.
- BM distributed width > HEO.
- BM (t_{63}) > HEO.
- Mg peak < HEO.
- Mg (t_{63}) > HEO.
- Mg transformed-state proxy < HEO.
- BM-Mg peak > Mg but < HEO.
- Mg transformed-state proxy < BM-Mg < HEO.

## S7.3. Pulse-end structural maps and rest evolution

Main Figure 5 shows the pulse-end radial structural order parameter over the late-stage model window. For ball-milled samples, the circular maps are ensemble-averaged radial states and are not simulated heterogeneous two-dimensional particles.

**Figure S20.** Model-predicted \(\Delta\bar\phi_{\mathrm{rest}}\) during the subsequent 60 min zero-flux interval. This quantity is an internal-state descriptor and is not numerically equated with the measured voltage relaxation \(\Delta E_{\mathrm{relax}}\).

## S7.4. Identifiability and interpretation boundaries

The model does not uniquely determine:

- absolute interfacial energy;
- absolute elastic modulus or coherency strain;
- unique Mg crystallographic site;
- unique (M_phi);
- true particle radius after milling;
- absolute experimental phase fraction;
- absolute voltage;
- unique probability distribution of local transition barriers.

The model supports **mechanistic sufficiency**, not unique microscopic identification.

The MATLAB spatial translation (`HEO_Spatial_PhaseField_Model_Final.m`) preserves the frozen Python equations and directional assertions but has not yet been runtime-verified in local MATLAB. The first local run should check the directional unit tests before any parameter adjustment.

---


# S8. Relation to prior GITT relaxation and phase-transformation analyses

The present analysis builds on several established directions in intermittent electrochemical characterization but combines them for a different purpose. The closest precedents fall into four groups.

## S8.1. Separation of kinetic contributions within intermittent measurements

Heubner et al. introduced StairCase-GITT, in which short current steps preceding the titration pulse are fitted to a modified Butler-Volmer description to separate ohmic resistance, exchange current density, and charge-transfer coefficient.[23] This establishes that a GITT-type protocol can be deliberately partitioned to obtain more than a single apparent diffusivity.

The present work uses a different separation. No modified current staircase is imposed. Instead, the measured current-off response is represented by (i) an early fast-response descriptor from the 3-30 s (E)-versus-(sqrt{t}) intercept, (ii) the finite-window relaxation amplitude, and (iii) model-free (t_{50}), (t_{63}), and (t_{90}). These observables are kept operational rather than assigned one-to-one to unique microscopic processes.

A recent full-cell study by Jorkesh et al. independently supports the usefulness of time-domain separation: derivative-based segmentation followed by a bi-exponential fit resolved fast and slow voltage-relaxation regimes whose characteristic times vary with SOC and temperature.[29] That work is oriented toward OCV/SOC estimation in commercial NMC811 cells and does not assign a structural phase-transition coordinate.

## S8.2. Fitting the complete pulse/rest transient

Horner et al. fitted an entire GITT current pulse and subsequent relaxation directly to a one-dimensional non-ideal electrochemical model.[24] Their approach extracted transport parameters from FeS2 intercalation data and then tested the fitted diffusivity by forward discharge prediction. This provides a strong precedent for using the full pulse/rest shape rather than only the classical GITT algebraic expression.

The present HEO study does not use unrestricted fitting of each GITT pulse to determine unique microscopic parameters. The current-off observables first establish experimental constraints, and the later spatial model is required only to reproduce their directional relationships across the four synthesis conditions.

## S8.3. GITT applied directly to phase-transformation kinetics

The closest direct precedent is the phase-transformation GITT/PITT method of Zhu and Wang.[21] By combining intermittent titration with a mixed-control phase-transformation model, that work extracted both Li diffusivity and phase-interface mobility in the two-phase region of LiFePO4. Chen et al. later used GITT polarization and rest-to-equilibrium behavior to compare phase-transformation kinetics at different reaction states and C-rates in LiFePO4 nanoparticles.[22]

These studies establish that phase-transition kinetics can be inferred from intermittent electrochemical experiments. Accordingly, the present manuscript does **not** claim the first extraction of a phase-transition kinetic parameter from GITT.

The present analysis differs in three ways:

1. The experimental conclusion is first built from independent current-off observables rather than from a unique mixed-control parameter fit.
2. The late-stage transition-associated contribution is isolated as a state-localized excess response and compared across a 2 × 2 synthesis matrix.
3. The spatial-model parameters are treated as effective, non-unique mechanism coordinates rather than as uniquely measured interface mobilities or thermodynamic constants.

## S8.4. Structural relaxation and ensemble heterogeneity during rest

Fath et al. showed with an extended Doyle-Fuller-Newman model that a particle-size distribution can modify GITT rest-phase voltage, produce delayed relaxation/tailing, and bias apparent diffusivity extracted from a single-particle representation.[25] This is directly relevant to the interpretation of BM-HEO, where the broader distribution of local environments is allowed to produce slower ensemble relaxation even when local accessibility increases.

Skurtveit et al. provided direct structural evidence that the state of an electrode can continue to evolve after current interruption.[26] Operando XRD resolved multiple stages of structural relaxation in graphite and much slower relaxation in LiFePO4; kinetic analysis and atomistic simulations linked the relaxation to Li redistribution and structural reorganization. This result supports the central caution of the present paper: GITT relaxation in a phase-evolving electrode should not automatically be interpreted as pure Fickian diffusion.

## S8.5. Phase-field connection

Han et al. used a phase-field model to demonstrate that non-Fickian phase-separating dynamics can bias conventional GITT/PITT diffusion interpretation,[27] while Singh et al. developed a continuum phase-field description in which conserved Li transport and phase-transformation dynamics produce behavior distinct from a classical diffusion-limited shrinking-core picture.[28]

These studies provide the theoretical precedent for using separate conserved transport and structural-order coordinates. The present model is intentionally simpler and is used only as a mechanism-sufficiency visualization for the HEO synthesis comparison.

## S8.6. Closest-precedent matrix

| Prior approach | Main quantity extracted/interpreted | Uses current-off/rest? | Explicit phase transformation? | Spatial/phase-field simulation? | Main distinction from present HEO work |
|---|---|---|---|---|---|
| Zhu & Wang 2010 [21] | Diffusivity + interface mobility | Yes | Yes | Mixed-control moving-interface model | Unique phase-transformation model fit; not multi-observable synthesis discrimination |
| Chen et al. 2017 [22] | Relative phase-transformation kinetics | Yes | Yes | No | State/rate comparison in LFP; no independent amplitude/time decomposition |
| Heubner et al. 2016 [23] | Ohmic R, exchange current, transfer coefficient | Primarily pulse staircase | No | No | Separates electrochemical kinetics by imposed current sequence |
| Horner et al. 2021 [24] | Non-ideal diffusivity | Yes, full pulse + rest fit | No in fitted regime | 1D electrochemical model | Direct fit/prediction of transport rather than phase-state discrimination |
| Fath et al. 2024 [25] | Rest-shape/PSD effect, apparent diffusivity | Yes | No | Extended DFN | Demonstrates ensemble-induced tailing/heterogeneity |
| Skurtveit et al. 2025 [26] | Structural relaxation stages/rates | Current interruption | Yes/structural | Atomistic simulation + operando XRD | Direct structure, not voltage-component decomposition |
| Han et al. 2004 [27] | Non-Fickian effect on GITT/PITT interpretation | Simulated GITT/PITT | Yes | Phase field | Theoretical model-system analysis |
| Singh et al. 2008 [28] | Phase-transformation dynamics/waves | General electrochemical dynamics | Yes | Phase field | General theory rather than GITT-constrained inverse interpretation |
| Jorkesh et al. 2026 [29] | Fast/slow voltage time constants | Yes | No | Bi-exponential time-domain model | Full-cell OCV/SOC application; no phase-transition coordinate |
| Present HEO study | fast-response descriptor + relaxation amplitude + model-free times + transition excess + directional internal-state coordinates | Yes | Yes, inferred from state/literature | Reduced radial phase field | Combines multi-observable current-off constraints with a 2 × 2 synthesis comparison and non-unique spatial internal-state visualization |

## S8.7. Bounded novelty statement

Within the literature reviewed for this manuscript, no direct precedent was identified that combines the following sequence in one phase-evolving conversion-electrode study:

**fast current-off response + \(\Delta E_{\mathrm{relax}}\) + model-free \(t_{50/63/90}\)**  
→ **state-localized transition-associated excess polarization**  
→ **synthesis-variable discrimination**  
→ **spatial internal-state visualization constrained by those experimental directions**.

This statement is intentionally narrower than a priority claim. Prior studies already establish GITT-based phase-transformation kinetics, interface-mobility extraction, multi-timescale relaxation analysis, and phase-field simulation separately.[21–29]



# S9. SI figure/table checklist before submission

## Figures

- Figure S1: full XRD/refinement.
- Figure S2: additional SEM/TEM + size statistics.
- Figure S3: HRTEM/SAED indexing.
- Figure S4: full EDS maps.
- Figure S5: final XPS.
- Figure S6: N2 adsorption/desorption/BET fits.
- Figure S7: interfacial-capacitance scan-rate regressions.
- Figure S8: full first-/selected-cycle profiles.
- Figure S9: no-FEC cycling control.
- Figure S10: detailed rate capability.
- Figure S11: dQ/dV, if retained.
- Figure S12: cycling EIS and state/outlier note.
- Figure S13: additional post-cycle SEM.
- Figure S14: representative early current-off fits.
- Figure S15: full GITT traces.
- Figure S16: t50/t63/t90.
- Figure S17: background fits and transition excess.
- Figure S18: background/window sensitivity.
- Figure S19: conventional apparent DGITT comparator, if retained.
- Figure S20: model (Deltaarphi_{mathrm{rest}}).

## Tables

- Table S1: composition/XRD refinement.
- Table S2: final XPS fit parameters, if retained.
- Table S3: Cdl regressions and area-conversion sensitivity.
- Table S4: current-off descriptors by capacity interval.
- Table S5: transition peak/width/area sensitivity.
- Table S6: model effective coordinates.
- Table S7: model convergence/readout/directional-unit-test summary.

---

# S10. Items that remain outside the current HEO paper

The exploratory sequence “D-only -> D + compact relaxation -> distributed relaxation” belongs to the separate GITT/EKF methodology project and should not be introduced into this material-centered manuscript unless a future independent validation creates a synthesis-specific result essential to the HEO story.

---

# References added for GITT relaxation/phase-transformation positioning

[21] Zhu, Y.; Wang, C. *Galvanostatic Intermittent Titration Technique for Phase-Transformation Electrodes.* **J. Phys. Chem. C** 2010, 114, 2830–2841. DOI: 10.1021/jp9113333.

[22] Chen, Y.; Wang, L.; Anwar, T.; Zhao, Y.; Piao, N.; He, X.; Zhu, Q. *Application of Galvanostatic Intermittent Titration Technique to Investigate Phase Transformation of LiFePO4 Nanoparticles.* **Electrochim. Acta** 2017, 241, 132–140. DOI: 10.1016/j.electacta.2017.04.137.

[23] Heubner, C.; Schneider, M.; Michaelis, A. *SoC dependent kinetic parameters of insertion electrodes from StairCase – GITT.* **J. Electroanal. Chem.** 2016, 767, 18–23. DOI: 10.1016/j.jelechem.2016.02.013.

[24] Horner, J. S.; Whang, G.; Ashby, D. S.; Kolesnichenko, I. V.; Lambert, T. N.; Dunn, B. S.; Talin, A. A.; Roberts, S. A. *Electrochemical Modeling of GITT Measurements for Improved Solid-State Diffusion Coefficient Evaluation.* **ACS Appl. Energy Mater.** 2021, 4, 11460–11469. DOI: 10.1021/acsaem.1c02218.

[25] Fath, M.; Heidebrecht, P.; Drechsler, C.; Kamlah, M. *Impact of particle size distribution on the rest phase behavior of LIB cathodes – Model based analysis.* **J. Power Sources** 2024, 596, 234100. DOI: 10.1016/j.jpowsour.2024.234100.

[26] Skurtveit, A.; Tiberg North, E.; Park, H.; Chernyshov, D.; Wragg, D. S.; Koposov, A. Y. *Stepwise Structural Relaxation in Battery Active Materials.* **ACS Mater. Lett.** 2025, 7, 343–349. DOI: 10.1021/acsmaterialslett.4c02058.

[27] Han, B. C.; Van der Ven, A.; Morgan, D.; Ceder, G. *Electrochemical modeling of intercalation processes with phase field models.* **Electrochim. Acta** 2004, 49, 4691–4699. DOI: 10.1016/j.electacta.2004.05.024.

[28] Singh, G. K.; Ceder, G.; Bazant, M. Z. *Intercalation dynamics in rechargeable battery materials: General theory and phase-transformation waves in LiFePO4.* **Electrochim. Acta** 2008, 53, 7599–7613. DOI: 10.1016/j.electacta.2008.03.083.

[29] Jorkesh, S.; Akbari, A.; Ahmed, R.; Habibi, S. *SOC-dependent voltage relaxation and dual time-constant behavior in lithium-ion batteries: A time-domain analysis.* **J. Power Sources** 2026, 682, 240338. DOI: 10.1016/j.jpowsour.2026.240338.
