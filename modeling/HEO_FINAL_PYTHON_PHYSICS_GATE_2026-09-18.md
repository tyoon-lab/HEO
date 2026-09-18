# HEO Final Python Physics Gate — Frozen Mechanistic Model

**Date:** 2026-09-18  
**Status:** Python physics frozen for directional mechanism testing. Ready for MATLAB translation.  
**Important:** This is a mechanism-sufficiency model, not a unique parameter-identification model and not a quantitative voltage fit.

## 1. Purpose

The spatial model was developed to test whether the experimentally observed directions can emerge from coupled Li transport and structural phase evolution:

- Mg-HEO: transition-associated polarization down, conversion capacity down, relaxation slower;
- BM-HEO: accessible conversion remains high, concentrated transition peak down, transition interval broader, residual relaxation slower;
- BM-Mg-HEO: transition response partially re-emerges relative to Mg-HEO but remains far below HEO, while transformed fraction/accessibility partially recovers.

The final model is used only to test mechanistic sufficiency.

## 2. Governing equations

Dimensionless free-energy density:

\[
f = c\ln c + (1-c)\ln(1-c)
+W\phi^2(1-\phi)^2
+K(c^*-c)\phi
+G_{\rm Mg}\phi
+\frac{1}{2}B_{\rm el}q_{\rm el}(r)\phi^2
-S_{\rm surf}w_{\rm surf}(r)\phi
+\frac{\kappa}{2}|\nabla\phi|^2.
\]

Surface/coherency spatial weights:

\[
q_{\rm el}(r)=1-\exp[-(1-r)/\ell_{\rm relief}],
\]

\[
w_{\rm surf}(r)=\exp[-(1-r)/\ell_{\rm wet}].
\]

Li chemical potential:

\[
\mu_c=\ln\frac{c}{1-c}-K\phi.
\]

Conserved Li dynamics:

\[
\frac{\partial c}{\partial t}=-\nabla\cdot J,\qquad
J=-D_{\rm eff}\nabla\mu_c.
\]

Nonconserved structural dynamics:

\[
\frac{\partial\phi}{\partial t}
=-M_\phi\frac{\delta G}{\delta\phi}.
\]

The reduced coherency term is not a full mechanical-equilibrium elasticity solution. It is a hypothesis-level energetic coordinate.

## 3. GITT protocol and numerical state resolution

Final numerical protocol:

- spherical finite-volume radial model;
- diffuse-interface parameter \(\kappa=0.002\), after explicit mesh/interface-resolution testing;
- 600 s inward Li-flux pulse;
- 3600 s zero-flux rest;
- 50 pulse/rest states;
- inward dimensionless flux \(j=9\times10^{-6}\);
- median \(\Delta\bar c\) per pulse \(\approx0.0162\), chosen to match the order of the experimental normalized GITT state increment;
- BDF as primary stiff solver;
- Radau fallback only when BDF fails at a sharp phase-transition event.

The earlier coarse-state model used \(\Delta\bar c\sim0.036\) per pulse and produced unstable FWHM estimates for heterogeneous BM ensembles. This was rejected for the final gate.

## 4. Voltage-observable test

Two voltage-like observables were evaluated independently:

\[
V_{\rm vol}\propto-\langle\mu_c\rangle_V,
\]

and

\[
V_{\rm surf}\propto-\mu_c(r=R).
\]

The mechanistic ordering of peak amplitude and characteristic relaxation time is unchanged between the two observables.

This is a key robustness result: the central mechanism is not an artifact of choosing volume-averaged rather than surface chemical potential.

## 5. Final physical coordinates

### HEO

Reference homogeneous transition:

- \(D_{\rm eff}/R^2=0.0015\)
- \(M_\phi=0.015\)
- \(W=0.60\)
- \(K=1.80\)
- \(G_{\rm Mg}=0\)
- \(B_{\rm el}=0.20\)
- \(S_{\rm surf}=0.08\)

### Mg-HEO

Mg requires two independent changes.

Final hypothesis-level coordinates:

- \(G_{\rm Mg}=0.38\): explicit parent/intermediate-phase stabilization;
- \(M_\phi=6\times10^{-4}\): slower residual structural mobility;
- \(W=0.80\);
- transport scale kept HEO-like.

A \(G_{\rm Mg}\)-\(M_\phi\) grid showed:

- stabilization alone can suppress transformed fraction but can make relaxation too fast;
- low mobility alone does not sufficiently suppress the transition;
- the combined region produces small transition response + reduced transformed fraction + slower relaxation.

### BM-HEO

A single BM particle with only easier surface nucleation / shorter effective transport scale does not reproduce all observables.

The final BM interpretation requires a **joint distribution** of:

1. local transition/surface condition \(S_{\rm surf}\);
2. structural mobility \(M_\phi\).

A latent Gaussian coordinate \(x\sim N(0,1)\) is used:

\[
S_{\rm surf}=0.15+0.06x,
\]

\[
M_\phi=0.008\exp(-0.6x).
\]

Common BM coordinates:

- \(D_{\rm eff}/R^2=0.003\)
- \(W=0.50\)
- \(K=1.60\)
- \(B_{\rm el}=0.25\)
- larger surface-relief length scale.

Interpretation:

ball milling creates a distribution of defect/strain/surface environments and structural mobilities. Easier local transformation and slower heterogeneous structural relaxation are therefore allowed to coexist.

### BM-Mg-HEO

BM-Mg retains Mg stabilization but milling partially disrupts the stabilization in some local domains.

Final hypothesis-level coordinates:

- effective \(G_{\rm Mg}=0.30\), smaller than Mg-HEO \(0.38\) but still positive;
- latent Gaussian heterogeneity:
  \[
  S_{\rm surf}=0.22+0.075x,
  \]
  \[
  M_\phi=8\times10^{-4}\exp(-0.6x);
  \]
- \(D_{\rm eff}/R^2=0.003\);
- \(W=0.70\), \(K=1.70\).

This is interpreted as **partial reopening of the Mg-stabilized conversion pathway**, not elimination of the Mg effect.

## 6. Continuous-distribution convergence

Discrete 5-point / coarse GITT-state ensembles gave unstable FWHM values. The problem was traced to two numerical issues:

1. transition-state sampling was too coarse;
2. FWHM is discontinuous for multimodal/distributed responses.

Corrections:

- GITT state step reduced to \(\Delta\bar c\approx0.0162\);
- continuous Gaussian distributions represented by probability quantiles;
- numerical convergence assessed using polarization-weighted second-moment width rather than FWHM.

For BM, joint-distribution convergence:

| Quantiles | Peak proxy | moment width in \(\bar c\) | peak \(t_{63}\) |
|---:|---:|---:|---:|
| 7 | 0.1905 | 0.0838 | 26.91 min |
| 11 | 0.1824 | 0.0847 | 26.91 min |

Surface-\(\mu\) values are similarly stable (moment width 0.0854 to 0.0862).

Decision: 11 probability quantiles are sufficient for the frozen Python model.

## 7. Final frozen four-sample result

Volume-\(\mu\) readout:

| Sample | peak / HEO | moment width | \(t_{63}\) at peak | final transformed-fraction proxy |
|---|---:|---:|---:|---:|
| HEO | 1.000 | 0.0683 | 22.03 min | 1.000 |
| BM-HEO | 0.237 | 0.0847 | 26.91 min | 1.000 |
| Mg-HEO | 0.136 | 0.0308 | 40.17 min | 0.214 |
| BM-Mg-HEO | 0.188 | 0.0498 | 40.17 min | 0.824 |

The same directional checks pass using the surface-\(\mu\) readout.

Directional criteria satisfied for both readouts:

- BM peak < HEO;
- BM distributed width > HEO;
- BM \(t_{63}\) > HEO;
- Mg peak < HEO;
- Mg \(t_{63}\) > HEO;
- Mg transformed fraction < HEO;
- BM-Mg peak > Mg;
- BM-Mg peak < HEO;
- Mg transformed fraction < BM-Mg transformed fraction < HEO.

## 8. What the final Python model establishes

The model supports the **sufficiency** of three independent physical coordinates:

1. **diffusive/transport scale**;
2. **thermodynamic transformation extent / stabilization**;
3. **structural-mobility and local-transition heterogeneity**.

The experimentally observed trends cannot be represented coherently by a single diffusion parameter.

Mg requires:

\[
G_{\rm Mg}>0,\qquad M_\phi\downarrow.
\]

BM requires:

\[
\text{local transition heterogeneity}\uparrow,\qquad
\text{mobility heterogeneity}\uparrow.
\]

BM-Mg additionally requires partial reduction of the effective Mg stabilization energy in some milled local environments.

## 9. What the model does NOT establish

Do not interpret the frozen coordinates as uniquely measured material constants.

The model does not uniquely determine:

- absolute interfacial energy;
- absolute elastic modulus or coherency strain;
- unique Mg site;
- unique \(M_\phi\);
- true particle radius after milling;
- absolute phase fraction in the experimental electrode;
- absolute voltage;
- unique probability distribution of local barriers.

Multiple parameter combinations can generate similar directional behavior.

## 10. Freeze decision

**Python physics gate: PASSED for directional mechanism testing.**

The model is now frozen for MATLAB translation.

The MATLAB version must reproduce:

- the same governing equations;
- the refined GITT state increment;
- volume and surface chemical-potential readouts;
- Gaussian-quantile joint distributions;
- robust stiff integration;
- the same directional test table.

The existing \`HEO_PhaseTransition_Model_Final.m\` remains a legacy phenomenological port and must not be used as the new spatial implementation.
