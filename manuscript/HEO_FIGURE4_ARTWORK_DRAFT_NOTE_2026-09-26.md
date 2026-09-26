# HEO Figure 4 Artwork Draft — Source and Panel Audit

**Date:** 2026-09-26  
**Status:** artwork draft v4; panel logic follows `HEO_FIGURES_3_7_CURRENT_LOGIC_V5_2026-09-26.md`

## Figure-level question

Does the larger accessible capacity produced by ball milling correspond to faster kinetics, and does conventional GITT apparent diffusivity preserve the same fast–slow ordering as the directly observed current-off relaxation?

## Panel (a): operational definition from a real HEO pulse

Source workbook recovered from the HEO Drive data folder:

- `[GITT try 2_031].xlsx`
- workbook information identifies the test path as `HEO GITT TRY 4_cyc`
- test date recorded in the workbook: 2022-12-15
- raw acquisition: 1 s sampling in the relevant region

Representative trace:

- HEO pulse 48
- pulse onset: 219001 s
- pulse duration: 600 s
- subsequent rest: 3600 s
- pre-pulse relaxed voltage: 0.552861 V
- common current-off reference: 3 s after interruption
- (E_{3s}=0.357617) V
- end-of-rest voltage: 0.545217 V
- (Delta E_{m relax}=187.60) mV
- model-free (t_{63}=12.50) min

The compact committed trace is:

`modeling/HEO_FIGURE4_PANEL_A_PULSE48_COMPACT_2026-09-26.csv`

The panel is illustrative of the operational definitions only; the paper-level statistics are not inferred from this single pulse.

## Panel (b): decisive state-matched ranking inversion

Authoritative source:

`modeling/HEO_TY10_HEO_BM_STATE_MATCHED_RATIOS_2026-09-26.csv`

State range:

- pulses 12–48
- approximately 200–800 mAh g⁻¹
- 37 matched states

Result:

- (D_{m app,BM}/D_{m app,HEO}>1) at 37/37 states
- median (D_{m app,BM}/D_{m app,HEO}=1.7817)
- direct relaxation-rate ratio is plotted as (t_{63,m HEO}/t_{63,m BM}), so values above unity also mean faster BM-HEO
- (t_{63,m HEO}/t_{63,m BM}<1) at 35/37 states
- median (t_{63,m HEO}/t_{63,m BM}=0.7622)

Thus the two ratios are intentionally oriented to the same visual rule:

> above 1 = BM-HEO ranked faster.

The inversion is therefore read directly around the unity line.

## Panel (c): four-material relaxation comparison

Median (t_{63}) over the common 200–800 mAh g⁻¹ interval:

- HEO: 8.68 min
- BM-HEO: 11.57 min
- Mg-HEO: 11.01 min
- BM-Mg-HEO: 12.99 min

This panel shows that milling lengthens the effective current-off relaxation in both composition pairs.

## Panel (d): accessible capacity versus relaxation

First-cycle reversible capacities:

- HEO: 609.12 mAh g⁻¹
- BM-HEO: 782.08 mAh g⁻¹
- Mg-HEO: 458.91 mAh g⁻¹
- BM-Mg-HEO: 580.83 mAh g⁻¹

The pairwise arrows show the ball-milling perturbation. In both pairs, milling moves the material toward higher reversible capacity and longer (t_{63}).

## Artwork script

`modeling/heo_figure4_capacity_kinetics_mismatch.py`

The current implementation follows the Yoon Lab Figure Standard:

- normal font weight;
- left/bottom ticks only;
- legends inside;
- panel labels outside the axes;
- compact 2 × 2 reading order;
- no panel titles that repeat the caption.

## Remaining pre-submission gate

The Figure 4 artwork is scientifically usable as a draft, but the central relative-(D_{m app}) claim remains subject to the manuscript audit blocker:

**verify the final HEO and BM-HEO geometric electrode areas and recorded active masses before submission.**

The current relative audit assumes a common geometric electrode area. No absolute diffusivity is reported.
