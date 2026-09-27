# HEO Figure 5 Source Provenance Audit — 2026-09-27

## Current status

The Figure 5 **GITT excess analysis is raw-data based and scientifically frozen** for the current manuscript round.

The Figure 5 **first-cycle $dQ/dV$ comparator is a faithful vector reconstruction from the latest 2026-09-17 voltage-profile artwork**, not yet the original continuous numerical acquisition/source export.

Thus the conversion-localization conclusion is currently well constrained, but final $dQ/dV$ artwork provenance remains a submission-quality source-recovery item.

## GITT side

The first-lithiation GITT analysis uses the four HEO-series datasets with the common protocol:
- 600 s current pulse;
- 3600 s open-circuit rest;
- common current-off reference at 3 s;
- $\Delta E_{\mathrm{relax}}=E_{60\,\mathrm{min}}-E_{3\,\mathrm{s}}$;
- normalized first-lithiation state $z=Q/Q_{\max}$.

Nominal excess definition:
- early background window: $z=0.20$–0.40;
- late background window: $z=0.90$–1.00;
- exponential background $c+a\exp(-z/\tau)$;
- excess evaluated over $z=0.40$–0.90.

The current SI records the nominal metrics and a 105-condition background/window audit. The central HEO/BM and Mg-suppression amplitude directions are invariant over the tested definitions.

For voltage localization, the excess peak is first identified in state space and then assigned the **60 min rest-end voltage of the same GITT state**. This rest-end voltage is used as a quasi-relaxed state coordinate; it is not identified with an exact equilibrium potential. Raw-data reconstruction confirms that the current nominal GITT peak voltages (0.527, 0.618, 0.387, and 0.503 V) are 60 min rest-end voltages.

Legacy source notes remain useful for audit history:
- `manuscript/FIGURE4_RAW_REANALYSIS_NOTE_2026-09-18.md`
- `FIGURE4_CONVERSION_ASSIGNMENT_CHECK_2026-09-20.md`

Their old Figure numbers reflect earlier manuscript architectures; the same analysis now supports current **Figure 5**.

## First-cycle voltage-profile / dQ/dV side

Preferred current working source:
`HEO 진행상황 (20260917).pptx`, slide 10.

The first-cycle voltage profiles are embedded as Origin vector objects. High-resolution reconstruction gave terminal first-cycle capacities:
- HEO: 901.139552 mAh g$^{-1}$;
- BM-HEO: 1055.840412;
- Mg-HEO: 731.054107;
- BM-Mg-HEO: 943.874605.

These agree with the corresponding plotted values (901.25, 1056.10, 731.15, 944.07 mAh g$^{-1}$) to within approximately 0.03%, supporting faithful reconstruction.

A common Savitzky–Golay differentiation/smoothing procedure was applied to all four reconstructed profiles.

Nominal peak authority:

| Sample | $dQ/dV$ peak (V) | GITT excess peak, 60 min rest-end V (V) | difference (V) | $dQ/dV$ range over 20–60 mAh g$^{-1}$ smoothing |
|---|---:|---:|---:|---|
| HEO | 0.544575 | 0.527481 | -0.017094 | 0.544–0.547 |
| BM-HEO | 0.589146 | 0.617535 | +0.028389 | 0.589–0.589 |
| Mg-HEO | 0.418819 | 0.386972 | -0.031847 | 0.408–0.419 |
| BM-Mg-HEO | 0.484822 | 0.502865 | +0.018043 | 0.485–0.486 |

Under the nominal background definition, all four rest-end / $dQ/dV$ peak pairs lie within 32 mV.

The 105-condition background/window audit gives the following GITT rest-end peak-location ranges:
- HEO: 0.527481 V (invariant);
- BM-HEO: 0.592919–0.628391 V;
- Mg-HEO: 0.386972 V (invariant);
- BM-Mg-HEO: 0.453175–0.618300 V.

Thus the exact BM-Mg-HEO peak position is background-sensitive and the 32 mV statement is nominal rather than universal. However, the directions HEO → BM-HEO higher, HEO → Mg-HEO lower, and Mg-HEO → BM-Mg-HEO higher are preserved across all tested GITT definitions and match the corresponding $dQ/dV$ shifts.

Nominal compact authority:
`manuscript/HEO_FIGURE5_DQDV_GITT_PEAK_CHECK_2026-09-27.csv`

Voltage-coordinate/sensitivity authority:
`manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_AUDIT_2026-09-27.md`
`manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_SENSITIVITY_2026-09-27.csv`

## Why the older first-cycle source is not substituted

A May 8, 2026 data-transfer email explicitly reported an interruption artifact in an earlier first-cycle specific-capacity/voltage-profile dataset caused by a campus power outage and measurement restart.

That older source should not replace the current September profile merely because it is easier to locate.

## Final submission preference

If the original numerical source underlying the September voltage profiles is recovered:
1. regenerate the first-cycle $dQ/dV$ curves from that numerical source;
2. apply one common differentiation/smoothing workflow to all four materials;
3. verify that the four peak positions remain within the present smoothing-sensitivity ranges;
4. regenerate Figure 5(b,c);
5. update the compact CSV and provenance note.

If the source cannot be recovered, retain explicit provenance that the final comparator is reconstructed from the user's own vector Origin artwork and preserve the demonstrated capacity-reconstruction and smoothing-sensitivity checks.

Do not use raster digitization or the known power-interrupted older first-cycle dataset as a replacement.
