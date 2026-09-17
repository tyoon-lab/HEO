# Figure 4 Raw-Reanalysis Note

**Date:** 2026-09-18  
**Purpose:** Lock the data-processing definition and numerical values used for the phase-transition polarization figure.

## Source
Figure 4 is reconstructed from the first-lithiation current-off descriptors derived directly from the four raw GITT datasets:

- HEO
- BM-HEO
- Mg-HEO
- BM-Mg-HEO

The common state coordinate is normalized first-lithiation capacity:

[
z=Q/Q_{\max}.
]

## Background definition
A smooth exponential background is fitted independently for each sample using the two state windows

[
z=0.20-0.40
]

and

[
z=0.90-1.00.
]

The background form is

[
\eta_{bg}(z)=c+a\exp(-z/\tau).
]

The transition-associated excess response is then defined in the late-stage window (z=0.40-0.90) as

[
\eta_{excess}(z)=\max[\Delta E_{relax}(z)-\eta_{bg}(z),0].
]

This window excludes the large early first-lithiation formation/activation response and isolates the late-stage hump discussed in the manuscript.

## Recalculated transition metrics

| Sample | Peak excess polarization (mV) | FWHM-like width (mAh g-1) | Normalized excess area (mV) | Capacity-weighted excess area (mV mAh g-1) |
|---|---:|---:|---:|---:|
| HEO | 70.77 | 354.13 | 22.07 | 23909.67 |
| BM-HEO | 44.07 | 430.17 | 14.13 | 17901.01 |
| Mg-HEO | 15.91 | 250.29 | 4.94 | 3955.99 |
| BM-Mg-HEO | 21.10 | 391.78 | 7.58 | 7077.32 |

These values reproduce the previously identified qualitative hierarchy and are now the preferred raw-reconstructed working values for Figure 4.

## Interpretation fixed by the figure

### HEO -> BM-HEO
- peak amplitude decreases;
- transition width increases;
- normalized and capacity-weighted excess areas decrease;
- accessible capacity nevertheless increases.

Preferred interpretation:

**Ball milling broadens and redistributes the phase-transforming response while increasing electrochemical accessibility.**

It should not be described as a simple diffusion enhancement.

### HEO -> Mg-HEO
- transition-associated excess peak is strongly suppressed;
- excess area decreases strongly;
- accessible capacity also decreases;
- characteristic relaxation time does not become shorter.

Preferred interpretation:

**Mg predominantly suppresses the extent of the late-stage spinel-to-rock-salt/conversion transformation through structural stabilization rather than accelerating Li transport.**

### BM-Mg-HEO
Ball milling partially broadens/re-introduces a weak excess response relative to Mg-HEO, but the HEO-like concentrated transition is not restored. This is an internal check that processing can increase accessibility without reversing the stronger compositional constraint imposed by Mg on transformation extent.

## Figure 4 architecture

- **(a)** Late-stage raw (Delta E_{relax}) vs normalized capacity, focused on (z \ge 0.30).
- **(b)** Background-subtracted transition-associated excess polarization for (0.40 \le z \le 0.90).
- **(c)** Peak-amplitude vs FWHM-like-width map; marker area is proportional to normalized excess area.
- **(d)** Mechanistic summary: ball milling controls accessibility/distribution, whereas Mg controls transformation extent/stability.

## Manuscript wording boundary
The excess area is a comparative polarization descriptor derived from discrete GITT states. It is **not** a rigorous dissipated-energy measurement. Avoid calling it energy loss.

The late-stage hump is assigned primarily to the spinel-to-rock-salt/conversion transformation based on its state/voltage location and independent literature on the phase-evolution pathway. The GITT signal itself does not uniquely decompose nucleation, phase-boundary propagation, strain, and other microscopic contributions.
