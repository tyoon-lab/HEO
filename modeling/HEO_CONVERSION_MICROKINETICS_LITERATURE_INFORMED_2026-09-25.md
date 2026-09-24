# HEO Conversion Microkinetics — Literature-Informed Model

**Date:** 2026-09-25  
**Status:** current Figure 7 model authority; supersedes the earlier A/B/N/P phenomenological network for main-text use.

## 1. Scientific purpose

The model is a **literature-informed coarse-grained conversion microkinetic model** used to test mechanistic consistency of the observed capacity–relaxation mismatch.

It is **not**:
- an atomistically unique conversion mechanism;
- a fit of microscopic rate constants to a specific HEO sample;
- a unique rate-determining-step assignment;
- proof that the effective intermediate states correspond to one experimentally identified phase.

The experimental question is:

> How can more accessible conversion coexist with slower post-interruption relaxation?

## 2. Literature basis

Two precedents are especially important.

1. **Ng et al., J. Mater. Chem. A 2021, 9, 523; DOI 10.1039/D0TA09683K.**  
   NiO conversion was analyzed using GITT together with Butler–Volmer / Marcus–Hush–Chidsey kinetics. The conversion pathway was treated as coupled electrochemical and chemical steps rather than one rate constant.

2. **Alsaç et al., ACS Appl. Mater. Interfaces 2026, 18, 1626–1640; DOI 10.1021/acsami.5c20956.**  
   Sulfur, FeS2, and FeF3 conversion cathodes were modeled using coupled reaction networks with intermediate-state evolution.

The open-circuit current-balance interpretation follows the standard mixed-potential principle: zero total current does not require every partial current to be zero. See R. Parsons, Pure Appl. Chem. 1974, 37, 499–516; DOI 10.1351/pac197437040499.

## 3. Current effective network

\[
O+\nu_1 Li^+ + \nu_1e^- \rightleftharpoons I
\]

\[
I \rightleftharpoons I^*
\]

\[
I^*+\nu_3 Li^+ + \nu_3e^- \rightleftharpoons C
\]

Interpretation:
- \(O\): oxide-derived state;
- \(I\): reduced/lithiated oxide intermediate;
- \(I^*\): structurally reconstructed / conversion-active intermediate;
- \(C\): metal/Li2O-containing converted state.

The \(I\leftrightarrow I^*\) step is intentionally coarse-grained and may include M–O rearrangement, oxygen/cation redistribution, nucleation, and conversion-interface evolution.

This replaces the older manuscript notation A <-> B, B -> N, B <-> P. The old N variable was a phenomenological activity/nucleation variable, not a mass-balanced chemical species, so writing B -> N as a reaction was physically ambiguous.

## 4. Rate structure

R1 and R3 are reversible Faradaic Butler–Volmer-type steps. R2 is a reversible non-Faradaic reconstruction step.

For the illustrative normalized calculation with symmetric transfer coefficients:

\[
r_1=k_1\left[a_O e^{u/2}-\frac{a_I}{K_1}e^{-u/2}\right]
\]

\[
r_2=k_{2,f}a_I-k_{2,r}a_{I^*}
\]

\[
r_3=k_3\left[a_{I^*}e^{(u-u_3)/2}-\frac{a_C}{K_3}e^{-(u-u_3)/2}\right].
\]

State balances:

\[
\frac{dx_I}{dt}=r_1-r_2
\]

\[
\frac{dx_{I^*}}{dt}=r_2-r_3
\]

\[
\frac{dx_C}{dt}=r_3
\]

with

\[
x_O=1-x_I-x_{I^*}-x_C.
\]

## 5. Current-on and current-off condition

General Faradaic current balance:

\[
j_{\rm ext}=F(\nu_1r_1+\nu_3r_3).
\]

At current interruption:

\[
j_{\rm ext}=0
\]

does not imply

\[
r_1=r_3=0.
\]

For the normalized illustrative case \(\nu_1=\nu_3=1\),

\[
r_1=-r_3\neq0
\]

is allowed while \(r_2\) can also remain finite.

The corresponding overall lithiation coordinate

\[
q=x_I+x_{I^*}+2x_C
\]

satisfies

\[
\frac{dq}{dt}=r_1+r_3=0
\]

at open circuit. Thus total lithiation/SOC is conserved while internal populations redistribute. This is the physical meaning of the current-off internal counter-current.

## 6. Numerical validation

Representative parameter set in:

modeling/heo_conversion_microkinetics_electrochemical_growth.py

Reference protocol:
- normalized reference current: \(J_{\rm ref}=2\times10^{-4}\);
- pulse: 600 s;
- rest: 3600 s;
- same 3 s current-off reference used experimentally.

Immediately after interruption:
- \(r_1=-4.9369\times10^{-5}\);
- \(r_3=+4.9369\times10^{-5}\);
- \(r_1+r_3\approx-1.25\times10^{-18}\);
- \(r_2=+6.8330\times10^{-5}\).

Therefore zero external Faradaic current coexists with finite internal reaction rates.

Experimental-style relaxation:
- 3 s-to-3600 s residual relaxation: **24.01 mV**;
- \(t_{63}\): **13.78 min**.

Local linearization near the equilibrated state gives:
- finite mode 1: **0.50 min**;
- finite mode 2: **14.27 min**;
- one conserved-state/SOC mode.

The slow finite eigenmode is therefore naturally close to the model \(t_{63}\), while \(t_{63}\) remains an ensemble descriptor rather than a microscopic elementary-step constant.

## 7. Amplitude–timescale separation

With the same rate constants, changing only the pulse current gives:

| Relative pulse current | 3 s relaxation amplitude (mV) | \(t_{63}\) (min) |
|---:|---:|---:|
| 0.25 | 11.93 | 13.78 |
| 0.50 | 16.95 | 13.78 |
| 1.00 | 24.01 | 13.78 |
| 2.00 | 33.18 | 13.95 |
| 4.00 | 45.77 | 14.12 |

Thus state excitation / relaxation amplitude can change nearly fourfold while the dominant effective timescale changes very little. This is a direct model-level demonstration of the central experimental logic.

Keep this current sweep in SI / internal mechanistic validation, not as the main Figure 7 claim.

## 8. Figure 7 interpretation

Preferred panel architecture:

**(a) Literature-informed conversion network**  
\(O \rightleftharpoons I \rightleftharpoons I^* \rightleftharpoons C\), with R1/R3 Faradaic and R2 structural/reconstruction.

**(b) Current interruption**  
Show \(j_{\rm ext}=F(\nu_1r_1+\nu_3r_3)=0\) with finite opposing R1/R3 partial currents and finite R2 during early relaxation.

**(c) Amplitude vs eigen-timescale**  
Use
\[
d\delta x/dt=J\delta x
\]
and
\[
E(t)-E_{\rm eq}=\sum_iB_i e^{-t/\tau_i}.
\]
The representative model has finite modes near 0.50 and 14.3 min.

**(d) Experimental constraints**  
- BM: higher accessible reversible reaction extent but longer effective relaxation;
- Mg: lower accessible reversible reaction extent while later-cycle \(t_{63}\) approaches Mg-free values;
- cycling: amplitude changes much more than \(t_{63}\).

## 9. Claim boundaries

Safe:
- conversion contains coupled electrochemical and structural/reconstruction steps;
- zero external current can coexist with finite opposing internal partial currents;
- accessible reaction extent, relaxation excitation amplitude, and relaxation eigen-timescale are distinct but coupled quantities;
- the model is consistent with the observed capacity–relaxation mismatch.

Do not claim:
- \(I\) or \(I^*\) is one uniquely identified phase;
- one elementary RDS has been measured;
- BM maps uniquely to one \(k_i\);
- Mg maps uniquely to one \(k_i\);
- \(t_{63}\) equals one elementary rate constant;
- this decoupling is unique to HEOs.

## 10. Current numerical outputs

- modeling/HEO_MICROKINETIC_CURRENT_OFF_BALANCE_LITERATURE_INFORMED_2026-09-25.csv
- modeling/HEO_MICROKINETIC_CURRENT_SWEEP_LITERATURE_INFORMED_2026-09-25.csv
- modeling/HEO_MICROKINETIC_EIGENMODES_LITERATURE_INFORMED_2026-09-25.csv
- modeling/heo_conversion_microkinetics_electrochemical_growth.py
