# HEO TY10 — Conventional GITT Apparent-Diffusivity Audit

**Date:** 2026-09-26  
**Role:** raw-data audit supporting Main Figure 4 and SI Section S5  
**Claim boundary:** demonstrates a kinetic-ordering inconsistency between conventional GITT apparent diffusivity and direct current-off relaxation; does not show that Li diffusion is absent.

## Raw data

- HEO: `HEO GITT 로우 데이터.xlsx`
- BM-HEO: `BM HEO 3 GITT 로우 데이터.xlsx`
- GITT program: 100 mA g⁻¹, 600 s pulse, 3600 s rest
- Common analysis reference: 3 s after pulse onset/interruption
- State-matched interval: pulses 12–48, approximately 200–800 mAh g⁻¹
- Number of matched states: 37

The raw workbooks were recovered from the 2026-09-17 HEO data package. The recalculated median $t_{63}$ and $\Delta E_{\mathrm{relax}}$ values reproduce the established manuscript values to within rounding, validating the pulse segmentation.

## Conventional relative diffusivity definition

For the HEO/BM-HEO pair,

\[
D_{\mathrm{GITT}}
\propto
\frac{1}{\tau}
\left(
\frac{m_BV_M}{M_BS}
\right)^2
\left(
\frac{\Delta E_s}{\Delta E_\tau}
\right)^2.
\]

Operational voltage terms:

\[
\Delta E_s
=
\left|
E_{\mathrm{rest,end}}^{(n)}
-
E_{\mathrm{rest,end}}^{(n-1)}
\right|,
\]

\[
\Delta E_\tau
=
\left|
E_{\mathrm{pulse,end}}
-
E_{\mathrm{pulse},3\,\mathrm{s}}
\right|.
\]

The relative HEO/BM comparison uses the common pulse duration and nominal composition. The active-mass term is retained; it is inferred from the applied current and the nominal 100 mA g⁻¹ program pending recovery of the final recorded electrode-mass metadata. A common electrode area is assumed for the current relative plot; absolute $D$ is intentionally not reported.

## Primary result

Across the 37 matched states:

- median $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}} = 1.7817$
- $D_{\mathrm{app,BM}}/D_{\mathrm{app,HEO}} > 1$ at 37/37 states
- median $t_{63,\mathrm{BM}}/t_{63,\mathrm{HEO}} = 1.3120$
- median direct relaxation-rate ratio $t_{63,\mathrm{HEO}}/t_{63,\mathrm{BM}} = 0.7622$
- direct relaxation-rate ratio < 1 at 35/37 states

Thus conventional GITT apparent diffusivity ranks BM-HEO as faster while direct current-off relaxation ranks BM-HEO as slower over nearly the entire common state interval.

## Voltage-term decomposition

Median state-matched ratios:

- $\Delta E_{s,\mathrm{BM}}/\Delta E_{s,\mathrm{HEO}} = 1.8095$
- $\Delta E_{\tau,\mathrm{BM}}/\Delta E_{\tau,\mathrm{HEO}} = 1.1758$

The relaxed state increment grows more strongly than the pulse voltage excursion, increasing $(\Delta E_s/\Delta E_\tau)^2$ and therefore the conventional $D_{\mathrm{app}}$ even though $t_{63}$ becomes longer.

## Pulse-on square-root-time check

For a 3–600 s pulse-on $E$ versus $\sqrt t$ linear fit:

- HEO median $R^2 = 0.7815$
- BM-HEO median $R^2 = 0.9076$

This full-pulse check is distinct from the 3–30 s current-off fit used for $R_{\mathrm{off,app}}$ in the SI.

## Interpretation

Supported:

**Conventional GITT $D_{\mathrm{app}}$ does not preserve the fast–slow kinetic ordering of the conversion-associated current-off relaxation in the HEO/BM-HEO pair.**

Not supported:

- diffusion is absent;
- $t_{63}$ is a microscopic diffusion coefficient or forward conversion rate;
- one unique structural step causes the mismatch;
- absolute $D$ values are quantitatively finalized before electrode geometry and molar-volume metadata are frozen.

## Manuscript placement

- Main Figure 4: relative $D_{\mathrm{app}}$ vs direct relaxation-rate ranking
- Main Section 2.3: opposite kinetic ordering
- SI Section S5 / Figure S23: full conventional-GITT audit and voltage-term decomposition
- Abstract: leave under author review; the final diffusion-coefficient sentence can be retained only after the author freezes wording.
