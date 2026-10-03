# HEO conversion-peak-area audit — 2026-10-03

## Purpose

Test the revised idea that the manuscript should compare **conversion-peak charge** rather than total first-lithiation capacity when relating accessible conversion extent to relaxation timescale.

The goal is specifically to remove the 0.005 V cutoff from the central comparison.

---

## Source and provenance

Source:
\`HEO 진행상황 (20260917).pptx\`, slide 10.

The first-cycle voltage and dQ/dV curves are embedded as Origin vector objects.

The voltage-profile vector reconstruction reproduces the plotted first-lithiation terminal capacities:

- HEO: 901.1396 mAh g^-1
- BM-HEO: 1055.8404
- Mg-HEO: 731.0541
- BM-Mg-HEO: 943.8746

These match the existing Figure 5 provenance audit and confirm that the vector geometry was recovered correctly.

Important:
the original continuous numerical source is still preferable for final submission. The present result is a vector-source audit.

---

## Operational conversion-peak charge

Use the cathodic first-cycle dQ/dV response and define a baseline-subtracted peak-area descriptor

\[
Q_{\mathrm{conv,peak}}
=
\int_{0.20\,V}^{0.90\,V}
\max\left[
-\frac{dQ}{dV}-b(V),0
\right]dV
\]

where \(b(V)\) is the linear baseline connecting the dQ/dV values at the two window boundaries.

Rationale for the nominal 0.20–0.90 V window:

- contains the first-cycle conversion feature of all four materials;
- lies far above the 0.005 V cutoff;
- excludes most of the higher-voltage sloping/insertion response;
- is wide enough not to penalize the broader BM conversion feature.

The vector dQ/dV curve was binned on a 2 mV grid. A mild common smoothing was used only to stabilize the baseline/area calculation. HEO/BM results are insensitive to 5–30 mV smoothing.

This quantity should be described as **conversion-peak charge** or **conversion-peak area**, not as a unique intrinsic conversion capacity.

---

## Nominal first-cycle result

Using 0.20–0.90 V and common mild smoothing:

| sample | Q_conv,peak (mAh g^-1) | first-cycle total lithiation (mAh g^-1) |
|---|---:|---:|
| HEO | ~249 | 901.14 |
| BM-HEO | ~309 | 1055.84 |
| Mg-HEO | ~163 | 731.05 |
| BM-Mg-HEO | ~121 | 943.87 |

For the compositionally identical HEO/BM pair:

\[
Q_{\mathrm{conv,peak,BM}}/Q_{\mathrm{conv,peak,HEO}}
\approx 1.24
\]

Thus ball milling increases the integrated conversion-peak charge by approximately 24% under the nominal definition.

This result is not a terminal-cutoff effect because the integration is restricted to 0.20–0.90 V.

---

## HEO/BM robustness audit

A window/smoothing sensitivity audit was run over:

- lower boundary: 0.15–0.30 V;
- upper boundary: 0.75–1.00 V;
- smoothing scale: 5–30 mV.

Total tested conditions: 462.

Result:

- BM conversion-peak area > HEO in **461/462** conditions;
- BM/HEO area-ratio range: ~0.996–1.638;
- median BM/HEO ratio: ~1.289.

Therefore the HEO/BM direction is robust to reasonable conversion-peak integration choices.

The one near-unity reversal is not physically meaningful enough to alter the directional conclusion.

---

## Raw-window charge cross-check

Without baseline subtraction, simply integrating the charge traversed between 0.20 and 0.90 V gives approximately:

- HEO: 756.8 mAh g^-1
- BM-HEO: 790.5 mAh g^-1

BM/HEO = ~1.045.

Thus the same direction is present even before baseline subtraction, although the contrast is much smaller because the raw window includes substantial non-peak background charge.

This supports using the baseline-subtracted peak area as the cleaner conversion-associated descriptor.

---

## Conversion-region t63 cross-check

Using first-cycle GITT states whose 60 min rest-end voltage lies within the same 0.20–0.90 V conversion window:

- HEO median t63 = 10.37 min
- BM-HEO median t63 = 11.92 min

Thus

\[
t_{63,\mathrm{BM}}/t_{63,\mathrm{HEO}}\approx 1.15
\]

A voltage-window sensitivity audit over 0.15–0.30 V lower boundaries and 0.75–1.00 V upper boundaries gives BM t63 > HEO t63 in **77/77** tested windows.

Therefore the central HEO/BM observation survives when both observables are restricted to the conversion voltage domain:

\[
Q_{\mathrm{conv,peak}}\uparrow
\qquad\text{and}\qquad
t_{63}\uparrow.
\]

---

## Interpretation

Safe:

**At the same nominal current and for the same nominal composition, ball milling increases the charge associated with the first-lithiation conversion peak while lengthening the conversion-region post-interruption relaxation timescale.**

Preferred physical interpretation:

**Greater accessible conversion extent under the measurement protocol does not necessarily imply faster post-interruption relaxation.**

Do not write:

- conversion-peak area is an intrinsic rate constant;
- larger peak area proves universally faster conversion kinetics;
- t63 is the unique conversion rate constant.

The peak area is an extent/accessibility descriptor measured under a fixed protocol, while t63 is a relaxation-timescale descriptor.

---

## Mg-containing pair

The Mg-HEO/BM-Mg-HEO conversion-peak area comparison is **not robust** to the same window/background choices because the cathodic dQ/dV response contains more strongly overlapping features.

Across the 462-condition audit:

- BM-Mg/Mg area ratio spans a wide range;
- only 203/462 conditions give BM-Mg > Mg;
- the median ratio is ~0.93.

Therefore do **not** use the Mg pair as an independent replication of the HEO/BM conversion-peak-area increase.

Mg can remain a complementary perturbation for relaxation magnitude/timescale and conversion-peak position, but not for a robust peak-area claim unless a better deconvolution is independently justified.

---

## Consequence for manuscript story

The strongest current comparison is the compositionally identical HEO/BM pair:

1. ball milling changes material state/morphology;
2. the baseline-subtracted first-lithiation conversion peak carries ~24% more charge;
3. the conversion-region t63 is nevertheless longer;
4. Figure 5 independently localizes the excess current-off response to the conversion region.

This recovers the useful “more accessible conversion / slower relaxation” mismatch **without invoking total capacity or terminal cutoff**.

The paper should not yet be globally rewritten until this definition is discussed and frozen.
