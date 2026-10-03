# HEO conversion-peak-area audit — 2026-10-03

**STATUS: REVISED / DO NOT USE THE EARLIER 249 → 309 mAh g^-1 RESULT AS A PHYSICAL CONVERSION-CHARGE CLAIM**

## Why this note was revised

The initial audit integrated a binned reconstruction of the **displayed dQ/dV Origin vector artwork** from \`HEO 진행상황 (20260917).pptx\`, slide 10. That procedure gave approximately 249 mAh g^-1 for HEO and 309 mAh g^-1 for BM-HEO after linear-baseline subtraction over 0.20–0.90 V.

A second audit reconstructed the underlying **first-cycle voltage–capacity vector profiles** from the same slide. These profiles reproduce the plotted terminal capacities to ~0.03%, so their integrated charge is internally constrained. When dQ/dV is re-derived from those voltage profiles and the same linear-baseline idea is applied, the HEO/BM peak-area ordering reverses.

Therefore the displayed dQ/dV vector is suitable for **peak-position localization**, but its reconstructed line geometry is not a quantitatively area-preserving source for conversion charge.

---

## Source consistency check

First-lithiation capacities reconstructed from the voltage-profile vectors:

- HEO: 901.1396 mAh g^-1
- BM-HEO: 1055.8404 mAh g^-1
- Mg-HEO: 731.0541 mAh g^-1
- BM-Mg-HEO: 943.8746 mAh g^-1

These agree with the plotted capacities and remain the preferred vector-source authority until the original continuous numerical GCD files are recovered.

---

## Why the displayed dQ/dV area is not reliable

### 1. Binned displayed dQ/dV artwork

Using a 2 mV binning of the first-cycle displayed cathodic dQ/dV vector and a linear baseline over 0.20–0.90 V gives approximately:

- HEO: 249 mAh g^-1
- BM-HEO: 311 mAh g^-1

This reproduces the earlier apparent BM > HEO peak-area result.

However, the raw integral of the binned displayed dQ/dV over 0.20–0.90 V is only approximately:

- HEO: 381 mAh g^-1
- BM-HEO: 562 mAh g^-1

whereas the charge obtained directly from the voltage–capacity profiles over the same voltage interval is:

- HEO: 756.98 mAh g^-1
- BM-HEO: 790.74 mAh g^-1

Thus the reconstructed displayed dQ/dV geometry does **not** conserve the actual charge area. Near the flat first-lithiation plateau, repeated/near-repeated voltage values generate narrow or quasi-vertical differential-capacity features whose quantitative area is not preserved by the exported vector artwork and subsequent binning.

### 2. dQ/dV re-derived from the voltage–capacity profile

When the differential-capacity response is re-derived from the voltage-profile vector and a common Savitzky–Golay-type smoothing is applied, the same nominal 0.20–0.90 V linear-baseline subtraction gives the **opposite HEO/BM ordering**.

Representative result:

- HEO excess area: ~630 mAh g^-1
- BM-HEO excess area: ~520 mAh g^-1

Across reasonable 5–100 mV voltage-domain smoothing, BM/HEO remains approximately 0.79–0.82.

The exact numerical values are processing-dependent, but the important result is that the **ordering itself depends on representation/processing**.

Therefore a baseline-subtracted dQ/dV peak area cannot presently serve as a frozen main-text descriptor.

---

## Baseline-free fixed-voltage-window charge

The physically unambiguous quantity is simply the charge passed through a chosen voltage interval:

\[
Q_{V_1-V_2}=Q(V_1)-Q(V_2)
\]

For 0.20–0.90 V:

- HEO: 756.98 mAh g^-1
- BM-HEO: 790.74 mAh g^-1
- BM/HEO = 1.0446

Thus BM passes about 4.5% more charge through this broad conversion-dominated voltage interval.

Window sensitivity using:

- lower boundary: 0.15–0.30 V
- upper boundary: 0.75–1.00 V

gives BM > HEO in 407/416 tested windows, with BM/HEO spanning ~0.992–1.072.

The direction is usually BM > HEO, but the contrast is modest and becomes near-unity or slightly reversed for narrower core-peak windows. Examples:

| voltage interval | HEO (mAh g^-1) | BM-HEO (mAh g^-1) | BM/HEO |
|---|---:|---:|---:|
| 0.20–0.90 V | 756.98 | 790.74 | 1.045 |
| 0.25–0.85 V | 733.9 | 752.0 | 1.025 |
| 0.30–0.80 V | 708.5 | 712.7 | 1.006 |
| 0.35–0.75 V | 676.6 | 668.8 | 0.988 |
| 0.40–0.75 V | 635.3 | 632.1 | 0.995 |

This means the large total-capacity increase after ball milling is **not concentrated uniquely in the core conversion dQ/dV peak**.

---

## Consequence

Do **not** currently claim:

- BM has ~24% larger conversion capacity based on dQ/dV peak area;
- a baseline-subtracted peak area is a robust conversion-extent descriptor;
- the HEO/BM central contradiction is proven by conversion-peak area.

Safe current statements:

1. The first-cycle cathodic dQ/dV peak localizes the relevant electrochemical feature to the conversion region.
2. BM-HEO has higher total accessible capacity under the common protocol.
3. Within a broad 0.20–0.90 V conversion-dominated interval, BM-HEO passes slightly more charge (~4.5%), but the difference is not robustly large in narrower peak-centered windows.
4. BM-HEO nevertheless has a longer conversion-region t63.

If the original continuous first-cycle numerical GCD data are recovered, quantitative peak-area analysis may be revisited using an area-conserving differentiation/deconvolution workflow and explicit baseline sensitivity.

Until then, **peak position is suitable for Figure 5 localization; peak area should not be used as a main quantitative claim.**
