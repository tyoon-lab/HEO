# HEO Figure 5 Artwork Final Note — 2026-09-27

**Status:** main scientific role and panel architecture frozen for the current manuscript round.

## Figure-level question

**Is the excess GITT current-off relaxation associated with the conversion region?**

Figure 5 is a localization test. It is not the paper's main kinetic contradiction figure and it is not intended to infer a unique microscopic conversion mechanism.

## Final main-panel architecture

### (a) State-resolved first-cycle relaxation and excess definition

Show the first-cycle $\Delta E_{\mathrm{relax}}$ response for HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO together with the smooth sample-specific background used to define the late-stage excess.

Nominal definition:
- state coordinate: $z=Q/Q_{\max}$;
- background-fit windows: $z=0.20$–0.40 and 0.90–1.00;
- excess-evaluation window: $z=0.40$–0.90;
- $\eta_{\mathrm{excess}}=\max[\Delta E_{\mathrm{relax}}-\eta_{\mathrm{bg}},0]$.

Role:
show that the conversion-localization analysis begins from a resolved feature in the measured current-off response rather than from the $dQ/dV$ comparison alone.

### (b) Voltage-localization comparison

Compare the background-subtracted GITT excess with the independently derived first-cycle cathodic $dQ/dV$ response on a common voltage axis for each material.

The GITT excess is identified first in state space. Each GITT state is then mapped to the **60 min rest-end voltage of that same state**. This is a quasi-relaxed state coordinate, not an exact equilibrium potential. Pulse-end and 3 s voltages are not used for localization because they retain the current-induced/immediate current-off polarization under investigation.

For visual localization, each trace family may be normalized to its own peak if needed. Such normalization is graphical only; relative trace amplitudes are not used as kinetic rates.

Preferred display:
- four aligned small multiples sharing the voltage axis, one material per row/mini-panel within panel (b), or another layout that avoids an eight-curve overlay;
- show the GITT-excess peak and $dQ/dV$ peak with subtle vertical markers;
- keep the same material order as Figures 3–4.

### (c) Peak-voltage correspondence

Plot
$V_{\mathrm{peak},dQ/dV}$
against
$V_{\mathrm{peak,GITT}}$
with a one-to-one line.

Nominal authority:

| Sample | cathodic $dQ/dV$ peak (V) | GITT excess peak, 60 min rest-end V (V) | GITT − $dQ/dV$ (V) |
|---|---:|---:|---:|
| HEO | 0.545 | 0.527 | -0.018 |
| BM-HEO | 0.589 | 0.618 | +0.029 |
| Mg-HEO | 0.419 | 0.387 | -0.032 |
| BM-Mg-HEO | 0.485 | 0.503 | +0.018 |

Under the nominal background definition, all four pairs lie within 32 mV of the one-to-one relation.

Peak-location sensitivity across the same 105 background/window definitions used for the SI audit:

| Sample | GITT rest-end peak-V range (V) |
|---|---:|
| HEO | 0.527481–0.527481 |
| BM-HEO | 0.592919–0.628391 |
| Mg-HEO | 0.386972–0.386972 |
| BM-Mg-HEO | 0.453175–0.618300 |

The exact BM-Mg-HEO peak position is therefore background-sensitive because the excess feature is shallow. The robust four-material result is the direction of the modification-induced shifts:
- HEO → BM-HEO: higher potential;
- HEO → Mg-HEO: lower potential;
- Mg-HEO → BM-Mg-HEO: higher potential.

All three GITT shift directions are preserved across the tested definitions and match the corresponding $dQ/dV$ shifts.

Artwork rule for panel (c):
- retain the one-to-one line;
- use nominal peak positions as the central markers;
- show GITT background/window peak-position ranges vertically;
- show $dQ/dV$ smoothing ranges horizontally where visible;
- treat the BM-Mg-HEO broad range as uncertainty, not as a separate mechanistic signal.

## Main/SI boundary

The previous main-panel amplitude-versus-FWHM-like-width map is moved to the Supporting Information.

Reason:
1. Figure 5 has one manuscript-level job: localize the current-off phenomenon to conversion.
2. Figure 4 already carries the decisive magnitude/timescale/capacity mismatch.
3. Excess amplitude and width are secondary response descriptors, not kinetic rates.
4. The BM peak-down/width-up direction is robust, but the shallow BM-Mg response gives a broad background-sensitive width range and should not drive a main-text mechanism claim.

Supporting Information retains:
- nominal excess amplitudes and FWHM-like widths;
- normalized/capacity-weighted excess metrics;
- the 105-condition background/window sensitivity audit;
- GITT peak-location sensitivity across the same 105 definitions;
- smoothing-window sensitivity for the reconstructed $dQ/dV$ peaks.

Robust SI-level findings:
- BM-HEO excess peak < HEO: 105/105 tested backgrounds/windows;
- BM-HEO width > HEO: 105/105;
- Mg-HEO excess peak < HEO: 105/105;
- BM-Mg-HEO excess peak < HEO: 105/105;
- BM-Mg-HEO > Mg-HEO nominal peak amplitude: only 80/105 and therefore not a required trend.

## Claim boundary

Supported:
**the excess current-off relaxation is conversion-associated.**

Not supported by Figure 5 alone:
- one unique microscopic conversion step;
- a unique rate-determining step;
- direct identification of Li$_2$O/metal nucleation, oxygen migration, phase-boundary motion, or one cation's reduction;
- interpreting excess amplitude or width as an intrinsic conversion rate;
- interpreting the GITT excess as dissipated energy.

## Figure 4 → Figure 5 → Figure 6 transition

Figure 4:
**higher accessible capacity can coexist with slower current-off relaxation, and apparent $D$ can give the conflicting direction.**

Figure 5:
**the excess current-off response used in that kinetic interpretation is localized to the conversion region.**

Figure 6:
**the conversion-associated response then changes with cycle history while the BM capacity-up/longer-$t_{63}$ relation persists.**

This question-answer sequence is the intended main-text hierarchy.

## Artwork rules

Use the Yoon Lab figure standard:
- normal font weight;
- panel labels (a)–(c), not bold;
- left/bottom ticks only;
- common sample order and sample styling;
- no redundant panel titles;
- no language such as “rate”, “faster”, or “slower” attached to excess amplitude/width;
- one-to-one line in panel (c) should be a visual reference, not a regression claim.

## Remaining artwork gate

The GITT side of the localization analysis is raw-data based and the background/sensitivity definition is frozen.

The current first-cycle $dQ/dV$ curves are reconstructed from the user's latest vector voltage-profile artwork. The original continuous numerical first-cycle profiles remain preferable for final submission if they can be recovered.

Nominal peak authority:
`manuscript/HEO_FIGURE5_DQDV_GITT_PEAK_CHECK_2026-09-27.csv`

Voltage-coordinate and sensitivity authority:
`manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_AUDIT_2026-09-27.md`
`manuscript/HEO_FIGURE5_VOLTAGE_COORDINATE_SENSITIVITY_2026-09-27.csv`

Source-provenance audit:
`manuscript/HEO_FIGURE5_SOURCE_PROVENANCE_AUDIT_2026-09-27.md`
