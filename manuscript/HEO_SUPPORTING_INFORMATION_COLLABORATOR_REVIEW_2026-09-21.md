# Supporting Information

## Structural Modification Reshapes Conversion and Relaxation in Spinel High-Entropy Oxide Anodes

# S1. Additional structural and compositional characterization

## S1.1. XRD refinement and lattice parameters

The main text uses the current XRD peak positions only to establish a modest Mg-associated lattice perturbation and milling-induced peak broadening. Final phase fractions, refined lattice parameters, and uncertainty should be reported here after the collaborator dataset is frozen.

**[[COLLABORATOR INPUT — Table S1: nominal composition, ICP-OES composition, refined lattice parameter, phase assignment/phase fraction, and refinement statistics for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO.]]**

**[[COLLABORATOR INPUT — Figure S1: full XRD patterns and final Rietveld/refinement comparison.]]**

The present manuscript does not assign Mg to a unique crystallographic site from the small peak shift alone.

## S1.2. Microscopy and elemental analysis

**[[COLLABORATOR INPUT — Figure S2: additional SEM/TEM images and particle/domain-size statistics.]]**

**[[COLLABORATOR INPUT — Figure S3: final HRTEM/SAED indexing and corresponding lattice-spacing table.]]**

**[[COLLABORATOR INPUT — Figure S4: EDS elemental maps for all four compositions.]]**

The preliminary CoGa2O4 HRTEM assignment is not chemically applicable to the Ga-free synthesis and must not be included.

## S1.3. XPS

**[[COLLABORATOR INPUT — Figure S5 and Table S2: final XPS spectra, fitting model, binding energies, and compositional comparison if XPS is retained in the final paper.]]**

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

**Figure S8.** Full first-cycle and selected-cycle voltage profiles.

## S2.3. FEC control, rate capability, dQ/dV, and cycling EIS

**Figure S9.** Cycling comparison with and without 10 wt% FEC. The no-FEC control is used to show the increased interphase burden of the higher-area BM material rather than to assign a unique SEI chemistry.

**Figure S10.** Detailed rate-capability profiles and recovery at 0.1 C.

**Figure S11.** Full/selected-cycle dQ/dV evolution supporting the compact main-text panel.

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

The finite-window relaxation amplitude is defined as

\[
\Delta E_{\mathrm{relax}}
=
E_{60\,\mathrm{min}}-E_{\mathrm{off},3\,\mathrm{s}}.
\]

Model-free \(t_{50}\), \(t_{63}\), and \(t_{90}\) are defined as the first times required to reach 50%, 63.2%, and 90% of the observed 3 s-to-60 min voltage recovery, respectively. These descriptors do not assume single-exponential relaxation. In particular, \(t_{63}\) equals a conventional time constant only for an ideal single exponential.

Raw-reconstructed medians are:

| Sample | \(R_{\mathrm{off,app}}\), 0–200 mAh g⁻¹ (Ω) | \(R_{\mathrm{off,app}}\), 200–800 mAh g⁻¹ (Ω) | \(\Delta E_{\mathrm{relax}}\), 200–800 (mV) | \(t_{63}\), 200–800 (min) |
|---|---:|---:|---:|---:|
| HEO | 308.1 | 106.4 | 160.9 | 8.68 |
| BM-HEO | 592.7 | 106.5 | 176.3 | 11.57 |
| Mg-HEO | 44.5 | 40.2 | 109.5 | 11.01 |
| BM-Mg-HEO | 93.8 | 33.0 | 144.3 | 12.99 |

**Figure S15.** Full first-lithiation GITT traces.

**Figure S16.** \(t_{50}\), \(t_{63}\), and \(t_{90}\) versus cumulative capacity.

**Table S4.** Current-off descriptors by selected capacity interval.

# S4. Late-stage conversion/transformation-associated excess analysis

## S4.1. State normalization and nominal background definition

The common state coordinate is normalized first-lithiation capacity,

\[
z=Q/Q_{\max}.
\]

For the nominal analysis, a smooth exponential background is fitted independently to each sample using

\[
0.20\le z\le0.40
\]

and

\[
0.90\le z\le1.00.
\]

The background form is

\[
\eta_{\mathrm{bg}}(z)
=
c+a\exp(-z/\tau).
\]

The late-stage conversion/transformation-associated excess response is defined over \(0.40\le z\le0.90\) as

\[
\eta_{\mathrm{excess}}(z)
=
\max\left[
\Delta E_{\mathrm{relax}}(z)-\eta_{\mathrm{bg}}(z),\,0
\right].
\]

The selected state interval excludes the dominant early first-lithiation formation/activation response and isolates the late-stage feature discussed in the main text.

## S4.2. Nominal extracted metrics

| Sample | Peak excess polarization (mV) | FWHM-like width (mAh g⁻¹) | Normalized excess area (mV) | Capacity-weighted excess metric (mV·mAh g⁻¹) |
|---|---:|---:|---:|---:|
| HEO | 70.77 | 354.13 | 22.07 | 23909.67 |
| BM-HEO | 44.07 | 430.17 | 14.13 | 17901.01 |
| Mg-HEO | 15.91 | 250.29 | 4.94 | 3955.99 |
| BM-Mg-HEO | 21.10 | 391.78 | 7.58 | 7077.32 |

The capacity-weighted quantity is a comparative polarization descriptor. It is not a dissipated-energy measurement because the voltage recovery is sampled at discrete GITT states rather than integrated as a continuous operating overpotential.

**Figure S17.** Sample-wise background fits and background-subtracted excess curves.

## S4.3. Background/window sensitivity audit

The nominal background choice was challenged using a grid of 105 alternative analyses. The early-background window was varied among 0.15–0.35, 0.15–0.40, 0.20–0.35, 0.20–0.40, 0.20–0.45, 0.25–0.40, and 0.25–0.45. The late-background lower bound was varied among \(z=0.88\), 0.90, and 0.92 with the upper bound fixed at 1.00. The excess-evaluation interval was varied among 0.38–0.90, 0.40–0.90, 0.42–0.90, 0.40–0.88, and 0.40–0.92.

Across all 105 combinations, the principal synthesis trends used in the main text were invariant:

| Directional criterion | Passed / tested |
|---|---:|
| BM-HEO peak < HEO peak | 105 / 105 |
| BM-HEO width > HEO width | 105 / 105 |
| Mg-HEO peak < HEO peak | 105 / 105 |
| BM-Mg-HEO peak < HEO peak | 105 / 105 |
| BM-Mg-HEO peak > Mg-HEO peak | 80 / 105 |

The corresponding peak-amplitude and width ranges were:

| Sample | Peak range (mV) | FWHM-like width range (mAh g⁻¹) |
|---|---:|---:|
| HEO | 60.7–74.7 | 306–379 |
| BM-HEO | 36.7–51.0 | 379–497 |
| Mg-HEO | 13.0–18.6 | 192–351 |
| BM-Mg-HEO | 12.6–27.6 | 233–872 |

The BM-HEO peak-down/width-up result and the strong suppression of both Mg-containing peaks relative to HEO are therefore robust to the tested background and window choices. By contrast, the small nominal difference between BM-Mg-HEO and Mg-HEO peak amplitudes is not invariant. The main-text interpretation consequently treats BM-Mg-HEO as remaining strongly suppressed relative to HEO; any amplitude recovery relative to Mg-HEO is described only as nominal/background-sensitive. The particularly broad width range for BM-Mg-HEO reflects the shallow excess feature and is not used as a quantitative mechanistic discriminator.

**Figure S18.** Background/window sensitivity of peak amplitude and FWHM-like width, including the directional pass/fail criteria above.

**Table S5.** Nominal excess metrics, tested window definitions, sensitivity ranges, and directional pass counts.

## S4.4. Cross-check against the first-cycle cathodic differential-capacity feature

The latest first-cycle voltage profiles from the 2026-09-17 HEO progress presentation were stored as vector graphics and reconstructed at high resolution. The reconstructed terminal capacities agree with the plotted first-cycle values to within approximately 0.03%.

A common Savitzky–Golay differentiation/smoothing procedure was applied to all four reconstructed profiles.

| Sample | Cathodic dQ/dV peak (V) | GITT excess peak (V) | Difference (V) |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | −0.018 |
| BM-HEO | 0.589 | 0.618 | +0.029 |
| Mg-HEO | 0.419 | 0.387 | −0.032 |
| BM-Mg-HEO | 0.485 | 0.503 | +0.018 |

All four peak pairs are localized within 32 mV. The dQ/dV peak locations remain stable over smoothing windows of 20–60 mAh g⁻¹: HEO 0.544–0.547 V, BM-HEO approximately 0.589 V, Mg-HEO 0.408–0.419 V, and BM-Mg-HEO 0.485–0.486 V.

This correspondence supports the conversion/transformation-associated assignment of the GITT excess feature while not identifying one unique microscopic elementary step.

**Data-source boundary.** Numerical continuous-GCD source files corresponding to these latest profiles are not currently available. The present values were reconstructed from the user's own vector voltage-profile plots, not from raster digitization. The original numerical profiles should replace this source if recovered before submission. The older first-cycle dataset affected by a power interruption is not used for this assignment.

**Figure S19.** First-cycle dQ/dV reconstruction, smoothing-window sensitivity, and comparison with the GITT excess-peak voltages.

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

The conventional apparent \(D_{\mathrm{GITT}}\) curve is not required in the final SI. The algebraic comparator above is sufficient to establish the directional inconsistency of a one-parameter diffusion explanation without redirecting the manuscript toward diffusivity extraction.

# S6. Reduced spatial model of conversion-associated state evolution

The model variable \(\phi\) represents the local extent of conversion. Values near zero correspond to an oxide-derived parent/intermediate state, whereas larger values represent progression toward a more deeply converted state. It is not interpreted as the experimentally measured fraction of any specific rock-salt, metallic, Li2O, or other microscopic phase. The model is not a stoichiometrically complete conversion-reaction model.

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

**Table S6.** Frozen effective coordinates of the reduced spatial model.

## S6.4. Why Mg requires two coordinates

A \(G_{\mathrm{Mg}}\)–\(M_\phi\) scan showed:

- stabilization alone suppresses the converted-state proxy but can make residual relaxation too fast;
- low structural mobility alone slows relaxation but does not sufficiently suppress the conversion-associated response;
- combined stabilization and lower residual structural mobility reproduce the required direction of a small conversion-associated response, reduced converted-state proxy, and slower relaxation.

## S6.5. Why BM requires a distribution

A single ball-milled particle with only shorter effective transport length or easier surface conversion does not reproduce all experimental directions. The accepted BM representation uses a joint distribution of local conversion/surface condition and structural mobility. This permits easier local conversion and slow ensemble relaxation to coexist.

---

# S7. Model convergence, readout robustness, and claim boundaries

## S7.1. Gaussian-quantile convergence

For BM-HEO:

| Quantiles | Peak proxy | Moment width in \(\bar c\) | Peak \(t_{63}\) (min) |
|---:|---:|---:|---:|
| 7 | 0.1905 | 0.0838 | 26.91 |
| 11 | 0.1824 | 0.0847 | 26.91 |

The surface-chemical-potential readout gives similarly stable moment widths. Eleven equal-probability Gaussian quantiles are therefore sufficient for the frozen directional model. The model moment width is a state-space second-moment descriptor and is not numerically equivalent to the experimental FWHM-like capacity width used in Figure 5; only the directional broadening/narrowing is compared.

## S7.2. Frozen four-sample directional result

Volume-\(\mu\) readout:

| Sample | Peak / HEO | Moment width | \(t_{63}\) at peak (min) | Final converted-state proxy |
|---|---:|---:|---:|---:|
| HEO | 1.000 | 0.0683 | 22.03 | 1.000 |
| BM-HEO | 0.237 | 0.0847 | 26.91 | 1.000 |
| Mg-HEO | 0.136 | 0.0308 | 40.17 | 0.214 |
| BM-Mg-HEO | 0.188 | 0.0498 | 40.17 | 0.824 |

The same directional ordering is obtained with the surface-\(\mu\) readout.

Directional criteria are:

- BM peak < HEO;
- BM distributed width > HEO;
- BM \(t_{63}\) > HEO;
- Mg peak < HEO;
- Mg \(t_{63}\) > HEO;
- Mg converted-state proxy < HEO;
- BM-Mg peak < HEO;
- Mg converted-state proxy < BM-Mg < HEO.

The experimental BM-Mg-versus-Mg excess-amplitude difference is background-sensitive and is therefore not used as a required model-acceptance criterion.

## S7.3. No-refit conversion-ordering cross-check

After the experimental Figure 5 excess feature was reassigned from a generic late-stage transition to conversion-associated electrochemistry, the frozen v4 model was recalculated **without refitting any parameter**.

Using either the volume-averaged or surface chemical-potential readout, the model relaxation maxima occur at:

| Sample | \(\bar c\) at model relaxation maximum |
|---|---:|
| BM-HEO | 0.5860 |
| HEO | 0.6184 |
| BM-Mg-HEO | 0.7966 |
| Mg-HEO | 0.9100 |

The same earlier-to-later sequence is obtained from pulse-end \(\bar\phi\) onset thresholds:

| Pulse-end \(\bar\phi\) threshold | BM-HEO | HEO | BM-Mg-HEO | Mg-HEO |
|---:|---:|---:|---:|---:|
| 0.02 | 0.545 | 0.606 | 0.735 | 0.834 |
| 0.05 | 0.557 | 0.619 | 0.763 | 0.859 |
| 0.10 | 0.570 | 0.620 | 0.779 | 0.889 |

Because the model coordinate \(\bar c\) increases with lithiation while the experimental electrode potential decreases, the model ordering BM-HEO → HEO → BM-Mg-HEO → Mg-HEO is directionally consistent with the experimental higher-to-lower conversion-feature voltage ordering. This agreement is used only as an ordering test. Model \(\bar c\) is not calibrated numerically to experimental \(Q/Q_{\max}\) or voltage.

**Figure S20.** Model convergence/readout robustness and the no-refit conversion-ordering cross-check.

**Table S7.** Model convergence, readout robustness, frozen directional criteria, and no-refit onset/peak ordering.

## S7.4. Pulse-end structural maps and rest evolution

Main Figure 6 shows the pulse-end radial conversion state over the late-stage model window. For ball-milled samples, the circular maps are ensemble-averaged radial states and are not simulated heterogeneous two-dimensional particles.

**Figure S21.** Model-predicted \(\Delta\bar\phi_{\mathrm{rest}}\) during the subsequent 60 min zero-flux interval. This quantity is an internal-state descriptor and is not numerically equated with the measured voltage relaxation \(\Delta E_{\mathrm{relax}}\).

## S7.5. Identifiability and interpretation boundaries

The model does not uniquely determine:

- absolute interfacial energy;
- absolute elastic modulus or coherency strain;
- unique Mg crystallographic site;
- unique \(M_\phi\);
- true particle radius after milling;
- absolute experimental phase fraction;
- absolute voltage;
- unique probability distribution of local conversion barriers.

The model supports mechanistic sufficiency, not unique microscopic identification.

The MATLAB spatial translation (\`HEO_Spatial_PhaseField_Model_Final.m\`) preserves the frozen Python equations and directional assertions but has not yet been runtime-verified in local MATLAB. The first local run should check the directional unit tests before any parameter adjustment. If runtime verification is not completed before submission, the SI should describe the verified Python implementation only and omit any implication of an independently validated MATLAB implementation.

# S8. Literature basis for the GITT/current-off interpretation

The GITT/current-off analysis is used here to resolve the electrochemical consequences of ball milling and Mg incorporation in the HEO system; it is not presented as the primary methodological contribution of the paper. Several prior studies establish the physical basis for analyzing intermittent transients beyond a single apparent diffusion coefficient.

Current-interruption and modified GITT approaches have separated distinct kinetic contributions or fitted the pulse/rest response directly.[16,23,24] Time-domain voltage relaxation has also been represented by multiple characteristic times.[29] For phase-transforming electrodes specifically, Zhu and Wang formulated phase-transformation GITT/PITT to extract Li diffusivity and phase-interface mobility in LiFePO4,[21] while Chen et al. used GITT polarization and rest-to-equilibrium behavior to compare phase-transformation kinetics.[22] These precedents justify treating the present relaxation amplitude and characteristic time as distinct observables rather than forcing the entire response into one apparent \(D\).

The long-rest response can also reflect electrode heterogeneity and structural evolution. Fath et al. showed that a particle-size distribution can alter the GITT rest shape and produce delayed equilibration relative to a single-particle description,[25] while Skurtveit et al. directly observed continued structural relaxation after current interruption using operando diffraction.[26] Phase-field studies likewise show that phase-separating/non-Fickian dynamics can change the interpretation of GITT/PITT transients.[27,28]

Accordingly, the present HEO analysis uses established intermittent-relaxation concepts as supporting tools. The experimental emphasis remains the contrasting response of the four HEO materials: ball milling increases electrochemical accessibility and redistributes the conversion/transformation-associated response, whereas Mg stabilizes the oxide-derived parent/intermediate state and suppresses accessible conversion. The spatial model is used only to visualize internal-state evolution compatible with those HEO observations; its parameters are effective and non-unique and are not claimed as uniquely extracted phase-boundary mobilities or thermodynamic constants.

# S9. SI figure/table checklist before submission

## Figures

- Figure S1: full XRD patterns and final refinement.
- Figure S2: additional SEM/TEM and particle/domain-size statistics.
- Figure S3: final HRTEM/SAED indexing.
- Figure S4: full EDS elemental maps.
- Figure S5: final XPS, only if the final dataset is retained.
- Figure S6: N₂ adsorption/desorption isotherms and BET fits.
- Figure S7: interfacial-capacitance scan-rate regressions.
- Figure S8: additional first-cycle/selected-cycle voltage profiles.
- Figure S9: no-FEC cycling control.
- Figure S10: detailed/normalized rate-capability comparison and 0.1 C recovery.
- Figure S11: full or selected-cycle dQ/dV evolution supporting main Figure 3.
- Figure S12: cycling EIS with state-matching/outlier note.
- Figure S13: additional post-cycle SEM.
- Figure S14: representative early current-off $E$–$\sqrt t$ fits.
- Figure S15: full first-lithiation GITT traces.
- Figure S16: $t_{50}$, $t_{63}$, and $t_{90}$ versus state.
- Figure S17: sample-wise background fits and excess curves.
- Figure S18: background/window sensitivity audit.
- Figure S19: latest first-cycle dQ/dV reconstruction, smoothing sensitivity, and GITT peak-voltage correspondence.
- Figure S20: model convergence/readout robustness and no-refit conversion-ordering validation.
- Figure S21: 60 min $\Delta\bar\phi_{\mathrm{rest}}$.

A standalone conventional apparent $D_{\mathrm{GITT}}$ figure is intentionally omitted unless a later reviewer-specific need arises.

## Tables

- Table S1: nominal composition, ICP-OES, XRD refinement, and phase fractions.
- Table S2: final XPS fit parameters, if XPS is retained.
- Table S3: interfacial-capacitance regressions and area-conversion sensitivity.
- Table S4: current-off descriptors by selected capacity interval.
- Table S5: nominal conversion-associated excess metrics plus background/window sensitivity ranges and directional pass counts.
- Table S6: frozen model effective coordinates.
- Table S7: model convergence/readout robustness and no-refit onset/peak-ordering summary.

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
