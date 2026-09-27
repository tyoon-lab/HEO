# HEO Figure 5 Voltage-Coordinate Audit — 2026-09-27

## Purpose

Freeze the voltage coordinate used to compare the state-resolved GITT excess-relaxation feature with the first-cycle cathodic differential-capacity feature, and test whether the conversion-localization result depends on the background/window definition.

## Raw GITT sources and common protocol

The four first-lithiation GITT datasets were re-read from the 2026-09-17 raw workbooks.

Common protocol:
- current pulse: 600 s;
- open-circuit rest: 3600 s;
- common current-off reference: 3 s;
- relaxation magnitude: $\Delta E_{\mathrm{relax}}=E_{60\,\mathrm{min}}-E_{3\,\mathrm{s}}$;
- normalized first-lithiation state: $z=Q/Q_{\max}$.

The Mg-free files are sampled at approximately 1 s in the GITT region and the Mg-containing files at approximately 3 s. The common 3 s reference is therefore retained.

## Voltage-coordinate definition

The excess peak is identified first in **state space** from

$\eta_{\mathrm{excess}}(z)=\max[\Delta E_{\mathrm{relax}}(z)-\eta_{\mathrm{bg}}(z),0]$.

For Figure 5 voltage localization, each GITT state is then assigned the **60 min rest-end voltage of that same state**. Thus

$V_{\mathrm{peak,GITT}}$

means the 60 min rest-end voltage at the state where $\eta_{\mathrm{excess}}$ is maximal.

This is a quasi-relaxed state coordinate, not a claim of exact thermodynamic equilibrium. The pulse-end and 3 s voltages retain the sample-dependent current-on/current-off polarization that Figure 4 is explicitly interrogating and are therefore not used as the conversion-localization voltage coordinate.

## Nominal raw-data reconstruction

Using the nominal background windows $z=0.20$–0.40 and 0.90–1.00 and the evaluation interval $z=0.40$–0.90:

| Sample | Excess-peak pulse | Peak $z$ | Cathodic $dQ/dV$ peak (V) | Pre-pulse rested V (V) | 60 min rest-end V (V) | 3 s V (V) | Pulse-end V (V) | Rest-end − $dQ/dV$ (mV) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HEO | 50 | 0.769 | 0.544575 | 0.537113 | 0.527481 | 0.338199 | 0.314042 | -17.09 |
| BM-HEO | 51 | 0.671 | 0.589146 | 0.628390 | 0.617535 | 0.458221 | 0.436204 | +28.39 |
| Mg-HEO | 38 | 0.792 | 0.418819 | 0.403485 | 0.386972 | 0.269245 | 0.253955 | -31.85 |
| BM-Mg-HEO | 37 | 0.661 | 0.484822 | 0.516473 | 0.502865 | 0.368167 | 0.355323 | +18.04 |

The nominal rest-end peak voltages reproduce the current Figure 5 authority values to rounding and all four nominal pairs lie within 32 mV.

The pre-pulse rested voltages provide an additional bracket on the same discrete GITT states and remain close to the corresponding conversion region. By contrast, pulse-end and 3 s voltages are substantially lower because they contain the polarization associated with the applied-current pulse and immediate current-off response.

## 105-condition background/window peak-location sensitivity

The same 105-condition grid already used for the excess-amplitude/width audit was applied to peak **location**.

| Sample | Peak pulse(s) across 105 definitions | Count(s) | 60 min rest-end peak-V range (V) | $dQ/dV$ smoothing range (V) |
|---|---|---|---:|---:|
| HEO | 50 | 105 | 0.527481–0.527481 | 0.544–0.547 |
| BM-HEO | 50 / 51 / 53 | 30 / 55 / 20 | 0.592919–0.628391 | 0.589–0.589 |
| Mg-HEO | 38 | 105 | 0.386972–0.386972 | 0.408–0.419 |
| BM-Mg-HEO | 26 / 35 / 37 / 38 / 40 | 10 / 35 / 15 / 15 / 30 | 0.453175–0.618300 | 0.485–0.486 |

Interpretation:
- HEO peak location is invariant.
- Mg-HEO peak location is invariant.
- BM-HEO remains confined to a narrow higher-potential band.
- BM-Mg-HEO has a broad background-sensitive peak-position range because the excess feature is shallow.

Therefore, the statement **“all four pairs lie within 32 mV” is a nominal-analysis statement**, not a background-independent bound.

## Robust modification-induced shift test

Despite the BM-Mg peak-position uncertainty, the **direction** of every material-induced GITT peak shift is invariant across the tested definitions:

- HEO → BM-HEO: GITT peak shifts to higher potential for all tested definitions.
- HEO → Mg-HEO: GITT peak shifts to lower potential for all tested definitions.
- Mg-HEO → BM-Mg-HEO: GITT peak shifts to higher potential for all tested definitions.

These directions match the independently derived cathodic $dQ/dV$ shifts:
- HEO → BM-HEO: higher potential;
- HEO → Mg-HEO: lower potential;
- Mg-HEO → BM-Mg-HEO: higher potential.

This directional concordance is the most robust four-material localization result.

## Figure 5 claim decision

Main-text claim:
**The excess current-off response is localized to the conversion region, and the material-induced voltage shifts of the GITT excess are concordant with the first-cycle cathodic $dQ/dV$ shifts.**

Allowed quantitative statement:
**Under the nominal background definition, all four GITT-rest-end / $dQ/dV$ peak pairs lie within 32 mV.**

Do not state that the 32 mV bound holds for every background/window definition.

## Figure 5(c) artwork decision

Retain the one-to-one peak-voltage comparison because it communicates the localization directly, but:
- plot the nominal peak positions as the central markers;
- show the background/window-derived GITT peak-voltage range as a vertical sensitivity range;
- show the $dQ/dV$ smoothing-derived range as a horizontal sensitivity range when visible;
- visually distinguish the broad BM-Mg-HEO sensitivity without turning the one-to-one line into a regression;
- state in the caption that the central points are nominal values and that modification-induced shift directions are invariant across the tested GITT definitions.

This keeps Figure 5 as a localization test and makes the uncertainty visible rather than hiding it.
