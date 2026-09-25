# Supporting Information v4 — Capacity–Relaxation/Microkinetic Draft

## Ball Milling and Mg Incorporation Reshape Conversion Dynamics in Spinel High-Entropy Oxide Anodes

**Date:** 2026-09-20  
**Status:** collaborator-review SI aligned to `HEO_MANUSCRIPT_V4_AFM_CONVERSION_2026-09-20.md`  
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


# S6. Cycle-resolved conversion-associated relaxation

The main-text Figure 6 compares the conversion-associated GITT response over repeated lithiation cycles. The analysis uses the same operational definition of the 3 s-to-60 min relaxation and the same normalized reaction-state interval, $z=0.4$–0.9, for all four materials.

## S6.1. Cycle-resolved lithiation descriptors

Median lithiation descriptors over $z=0.4$–0.9 are:

| Sample | C1 $\Delta E_{\mathrm{relax}}$ / $t_{63}$ | C2 $\Delta E_{\mathrm{relax}}$ / $t_{63}$ | C3 $\Delta E_{\mathrm{relax}}$ / $t_{63}$ |
|---|---|---|---|
| HEO | 168.5 mV / 10.37 min | 129.2 / 9.43 | 138.4 / 9.57 |
| BM-HEO | 160.5 / 13.02 | 125.7 / 11.18 | 133.5 / 11.33 |
| Mg-HEO | 111.3 / 10.53 | 127.9 / 9.83 | 140.9 / 9.53 |
| BM-Mg-HEO | 135.2 / 12.70 | 126.7 / 10.90 | 142.6 / 10.73 |

The conversion-associated excess peak evolves as:

| Sample | C1 peak | C2 peak | C3 peak | $z_{\mathrm{peak}}$, C1→C3 |
|---|---:|---:|---:|---:|
| HEO | 71.2 | 23.4 | 31.0 mV | 0.77→0.55 |
| BM-HEO | 44.8 | 17.2 | 22.4 | 0.67→0.54 |
| Mg-HEO | 15.9 | 19.3 | 27.0 | 0.79→0.56 |
| BM-Mg-HEO | 21.1 | 12.6 | 20.8 | 0.66→0.53 |

The first-cycle late feature therefore shifts toward a common earlier reaction-state region after cycling.

## S6.2. Amplitude–timescale change

Cycle-1 to cycle-3 normalized changes are:

| Sample | $A_3/A_1$ | amplitude change | $t_{63,3}/t_{63,1}$ | $t_{63}$ change |
|---|---:|---:|---:|---:|
| HEO | 0.435 | -56.5% | 0.923 | -7.7% |
| BM-HEO | 0.500 | -50.0% | 0.870 | -13.0% |
| Mg-HEO | 1.698 | +69.8% | 0.905 | -9.5% |
| BM-Mg-HEO | 0.986 | -1.4% | 0.845 | -15.5% |

Thus the amplitude ratio spans 0.435–1.698, whereas the timescale ratio remains within 0.845–0.923. The amplitude–timescale change map in Figure 6d is based directly on these ratios.

## S6.3. Later-cycle reversible reaction extent

Approximate GITT capacities obtained by pulse counting are:

| Sample | C1 lithiation | C2 lithiation | C3 lithiation | C3 delithiation |
|---|---:|---:|---:|---:|
| HEO | 1083 | 700 | 700 | 733 |
| BM-HEO | 1267 | 850 | 833 | 817 |
| Mg-HEO | 800 | 467 | 450 | 467 |
| BM-Mg-HEO | 933 | 567 | 533 | 533 |

These values are used only as approximate reversible-reaction descriptors and not as exact Coulombic efficiencies. They show that the higher accessible reaction extent after milling and the lower accessible reaction extent after Mg incorporation persist after the first cycle.

## S6.4. Later-cycle background sensitivity

For cycles 2–3, the nominal exponential background approaches the linear limit. Exponential and linear backgrounds produce peak-amplitude differences below 0.012%, identical peak positions, and maximum background differences below 0.0016 mV. The fitted exponential background constants are approximately $2.4\times10^3$–$5.4\times10^3$ in normalized-$z$ units, making the background numerically almost linear over the analysis window.

The first-cycle analysis retains the exponential background because the first-cycle background remains visibly curved.

**Figure S20.** Cycle-resolved conversion-associated relaxation and background-sensitivity comparison.

**Table S6.** Cycle-resolved amplitude, effective timescale, peak position, and reversible-capacity descriptors.


# S7. Literature-informed conversion microkinetic model and robustness

The model is used as a mechanistic-consistency test for the experimentally observed capacity–kinetics mismatch. It is not fitted to obtain unique microscopic rate constants, assign a unique rate-determining step, or identify the effective states with one crystallographic phase.

## S7.1. Coarse-grained reaction network

The current model contains

\[
O+\nu_1\mathrm{Li}^{+}+\nu_1e^-\rightleftharpoons I,
\]

\[
I\rightleftharpoons I^*,
\]

\[
I^*+\nu_3\mathrm{Li}^{+}+\nu_3e^-\rightleftharpoons C.
\]

Here, \(O\), \(I\), \(I^*\), and \(C\) denote effective oxide-derived, reduced/lithiated, structurally reconstructed/conversion-active, and more deeply converted metal/Li2O-containing states. \(R_1\) and \(R_3\) are reversible Faradaic steps; \(R_2\) is a reversible non-Faradaic reconstruction coordinate that coarse-grains structural rearrangement, cation/oxygen redistribution, nucleation, and conversion-interface evolution.

For the normalized illustrative calculation,

\[
r_1=k_1\left[a_Oe^{u/2}-\frac{a_I}{K_1}e^{-u/2}\right],
\]

\[
r_2=k_{2,f}a_I-k_{2,r}a_{I^*},
\]

\[
r_3=k_3\left[a_{I^*}e^{(u-u_3)/2}-\frac{a_C}{K_3}e^{-(u-u_3)/2}\right].
\]

The state balances are

\[
\frac{dx_I}{dt}=r_1-r_2,\qquad
\frac{dx_{I^*}}{dt}=r_2-r_3,\qquad
\frac{dx_C}{dt}=r_3,
\]

with \(x_O=1-x_I-x_{I^*}-x_C\).

Representative illustrative parameters:

| parameter | value |
|---|---:|
| \(k_1\) | \(2.0\times10^{-2}\) |
| \(k_{2,f}\) | \(8.4834\times10^{-4}\) |
| \(k_{2,r}\) | \(4.2417\times10^{-4}\) |
| \(k_3\) | \(1.0\times10^{-2}\) |
| \(u_3\) | -3.0 |
| \(K_1\) | 1.0 |
| \(K_3\) | 1.0 |
| reference normalized current \(J_{\mathrm{ref}}\) | \(2.0\times10^{-4}\) |

These values are illustrative and were not fitted to HEO, BM-HEO, Mg-HEO, or BM-Mg-HEO.

## S7.2. Current-off internal redistribution at conserved overall lithiation

The external Faradaic current is

\[
j_{\mathrm{ext}}=F(\nu_1r_1+\nu_3r_3).
\]

After interruption,

\[
j_{\mathrm{ext}}=0,
\]

which constrains the sum of the Faradaic partial currents but does not require each internal rate to vanish.[32] For \(\nu_1=\nu_3=1\),

\[
r_1=-r_3\neq0
\]

is allowed while \(r_2\) can also remain finite.

Define the normalized overall lithiation coordinate

\[
q=x_I+x_{I^*}+2x_C.
\]

Then

\[
\frac{dq}{dt}=r_1+r_3.
\]

Thus, at open circuit,

\[
\frac{dq}{dt}=0,
\]

while \(O/I/I^*/C\) populations can continue to redistribute.

Immediately after current interruption in the representative calculation:

| quantity | value |
|---|---:|
| \(r_1\) | \(-4.9369\times10^{-5}\) |
| \(r_2\) | \(+6.8330\times10^{-5}\) |
| \(r_3\) | \(+4.9369\times10^{-5}\) |
| \(r_1+r_3\) | \(\approx0\) |
| 3 s-to-3600 s relaxation | 24.01 mV |
| \(t_{63}\) | 13.78 min |

**Figure S21.** Representative current-off internal redistribution showing finite opposing Faradaic partial rates and continuing structural redistribution at zero external current, together with the corresponding voltage relaxation.

## S7.3. Local relaxation modes

Near an equilibrated state,

\[
\frac{d\,\delta\mathbf{x}}{dt}=\mathbf{J}\delta\mathbf{x},
\]

giving

\[
E(t)-E_{\mathrm{eq}}=\sum_iB_i\exp(-t/\tau_i).
\]

For the representative parameter set, local linearization gives two finite modes:

| mode | \(\tau\) |
|---|---:|
| fast finite mode | 0.50 min |
| slow finite mode | 14.27 min |
| conserved-state/SOC mode | infinite |

The slow model eigen-timescale lies close to the illustrative \(t_{63}\), but experimental \(t_{63}\) is treated only as an ensemble-level descriptor and is not equated to one microscopic eigenmode.

## S7.4. State-excitation amplitude versus relaxation timescale

With all rate constants fixed, changing only the pulse current strongly changes the relaxation amplitude while changing \(t_{63}\) only modestly:

| relative pulse current | residual relaxation at 3 s (mV) | \(t_{63}\) (min) |
|---:|---:|---:|
| 0.25 | 11.93 | 13.78 |
| 0.50 | 16.95 | 13.78 |
| 1.00 | 24.01 | 13.78 |
| 2.00 | 33.18 | 13.95 |
| 4.00 | 45.77 | 14.12 |

This calculation supports the Figure 6 interpretation that the magnitude of a conversion-associated nonequilibrium response can evolve more strongly than its effective relaxation timescale.

## S7.5. Capacity–kinetics coupling: homogeneous control

Capacity is itself kinetic-dependent. To establish the conventional baseline, a single homogeneous population was discharged galvanostatically to a fixed model voltage cutoff while all kinetic rate constants were scaled together.

| global rate scale | normalized cutoff capacity | matched-state \(t_{63}\) (min) |
|---:|---:|---:|
| 0.50 | 0.2993 | 22.45 |
| 0.75 | 0.4187 | 17.12 |
| 1.00 | 0.5585 | 13.45 |
| 1.50 | 0.7399 | 9.12 |
| 2.00 | 0.8322 | 6.95 |

Thus,

\[
\text{uniformly faster kinetics}
\Rightarrow
Q_{\mathrm{cutoff}}\uparrow,\quad t_{63}\downarrow.
\]

The experimental BM trend is therefore not interpreted as an absence of kinetic coupling.

## S7.6. Heterogeneous-accessibility existence proof

A second calculation retains the full reference fast population (weight 0.65) and adds an additional accessible population (weight 0.15) with the same reaction topology and thermodynamic parameters but a ten-times-slower \(R_2\) reconstruction rate.

| case | normalized cutoff capacity | matched-state \(t_{63}\) (min) |
|---|---:|---:|
| reference fast population | 0.55845 | 13.45 |
| fast + added slower-reconstructing population | 0.65714 | 15.28 |

The added population increases cutoff capacity by 17.67% while increasing \(t_{63}\) by 13.63%. Therefore,

\[
Q_{\mathrm{cutoff}}\uparrow,\quad t_{63}\uparrow
\]

is physically possible within the same multistep kinetic framework.

This calculation is an existence proof only. It does not establish that ball milling creates a population with a ten-times-slower \(R_2\), and the population weights are not measured phase fractions.

**Figure S22.** Microkinetic capacity–relaxation validation: homogeneous global-rate control and heterogeneous-accessibility existence proof.

## S7.7. Interpretation boundaries

The model supports the following statement:

**Capacity and post-interruption relaxation are kinetically linked through the same conversion network but are not kinetically equivalent observables.**

The model does not uniquely determine:
- microscopic identities of \(I\) or \(I^*\);
- unique elementary rate constants for the HEO samples;
- a unique rate-determining step;
- a unique nucleation or phase-growth mechanism;
- a quantitative conversion fraction from relaxation amplitude;
- a direct equality between \(t_{63}\) and the forward conversion rate;
- a unique one-to-one mapping of BM or Mg incorporation onto a specific model parameter.

**Table S7.** Representative model parameters, current-off current balance, eigenmodes, pulse-current sweep, homogeneous rate-scaling control, and heterogeneous-accessibility validation.

# S8. Literature basis for the GITT/current-off interpretation

The GITT/current-off analysis is used here to resolve the electrochemical consequences of ball milling and Mg incorporation in the HEO system; it is not presented as the primary methodological contribution of the paper. Several prior studies establish the physical basis for analyzing intermittent transients beyond a single apparent diffusion coefficient.

Current-interruption and modified GITT approaches have separated distinct kinetic contributions or fitted the pulse/rest response directly.[16,23,24] Time-domain voltage relaxation has also been represented by multiple characteristic times.[29] For phase-transforming electrodes specifically, Zhu and Wang formulated phase-transformation GITT/PITT to extract Li diffusivity and phase-interface mobility in LiFePO4,[21] while Chen et al. used GITT polarization and rest-to-equilibrium behavior to compare phase-transformation kinetics.[22] These precedents justify treating the present relaxation amplitude and characteristic time as distinct observables rather than forcing the entire response into one apparent \(D\).

The long-rest response can also reflect electrode heterogeneity and structural evolution. Fath et al. showed that a particle-size distribution can alter the GITT rest shape and produce delayed equilibration relative to a single-particle description,[25] while Skurtveit et al. directly observed continued structural relaxation after current interruption using operando diffraction.[26] Phase-field studies likewise show that phase-separating/non-Fickian dynamics can change the interpretation of GITT/PITT transients.[27,28]

Accordingly, the present HEO analysis uses established intermittent-relaxation concepts as supporting tools. The experimental emphasis remains the contrasting response of the four HEO materials: ball milling increases accessible reaction and capacity without accelerating the conversion-associated relaxation, whereas Mg suppresses accessible conversion without a proportional change in the effective relaxation timescale. The minimal microkinetic model is used only to establish that this apparent mismatch is physically consistent with a multi-step conversion network; its effective states and rate constants are not uniquely identified.


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
- Figure S11: full or selected-cycle $dQ/dV$ evolution supporting main Figure 3.
- Figure S12: cycling EIS with state-matching/outlier note.
- Figure S13: additional post-cycle SEM.
- Figure S14: representative early current-off $E$–$\sqrt t$ fits.
- Figure S15: full first-lithiation GITT traces.
- Figure S16: $t_{50}$, $t_{63}$, and $t_{90}$ versus state.
- Figure S17: sample-wise first-cycle background fits and excess curves.
- Figure S18: first-cycle background/window sensitivity audit.
- Figure S19: first-cycle $dQ/dV$ smoothing sensitivity and GITT peak-voltage correspondence.
- Figure S20: cycle-resolved conversion-associated relaxation and later-cycle background sensitivity.
- Figure S21: representative microkinetic current-off internal redistribution and voltage relaxation.
- Figure S22: homogeneous capacity–kinetics control and heterogeneous-accessibility existence proof.

A standalone conventional apparent $D_{\mathrm{GITT}}$ figure is intentionally omitted unless a reviewer-specific need emerges.

## Tables

- Table S1: nominal composition, ICP-OES, XRD refinement, and phase fractions.
- Table S2: final XPS fit parameters, if XPS is retained.
- Table S3: interfacial-capacitance regressions and area-conversion sensitivity.
- Table S4: current-off descriptors by selected capacity interval.
- Table S5: first-cycle conversion-associated excess metrics and sensitivity ranges.
- Table S6: cycle-resolved amplitude, $t_{63}$, peak-position, and reversible-capacity descriptors.
- Table S7: microkinetic parameters, current-off balance, eigenmodes, pulse-current sweep, and capacity–kinetics validation.

## Readiness classes

**Available from current Yoon-Lab/project files:** S14–S22 in principle; final publication artwork remains to be assembled.

**Available in recent progress material but source/provenance should be frozen before final SI:** S6–S13.

**Yoo-group input required before submission:** S1–S5, especially final ICP/XRD refinement/HRTEM indexing, Mg composition/synthesis metadata, and the decision on XPS.

# S10. Items that remain outside the current HEO paper

The exploratory sequence “D-only -> D + compact relaxation -> distributed relaxation” belongs to the separate GITT/EKF methodology project and should not be introduced into this material-centered manuscript unless a future independent validation creates a synthesis-specific result essential to the HEO story.

The former reduced spatial/phase-field model and the distributed-threshold capacity-prediction model are also historical analyses and are not part of the present HEO manuscript. They may remain in the repository for provenance but should not be cited as current manuscript evidence.

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


[30] Alsaç, E. P.; Sharma, A. K.; Yoon, S. G.; Vishnugopi, B. S.; Wang, C.; Thomas, T. A.; Nelson, D. L.; Eze, U. D.; Jeong, W. J.; Harris, J.; Mukherjee, P. P.; McDowell, M. T. *Linking Pressure to Electrochemical Evolution in Solid-State Conversion Cathode Composites.* **ACS Appl. Mater. Interfaces** 2026, 18, 1626–1640. DOI: 10.1021/acsami.5c20956.
