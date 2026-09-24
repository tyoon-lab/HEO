# Capacity–Relaxation Microkinetic Validation

**Date:** 2026-09-25  
**Purpose:** test whether the current conversion microkinetic model respects the fact that capacity is kinetic-dependent, and determine the minimum extension required to reproduce higher capacity together with slower relaxation.

## 1. Why this test was needed

Capacity and post-interruption relaxation are not independent quantities. Both are governed by the same conversion network.

At finite current, slower kinetics increases polarization and can cause the electrode to reach the voltage cutoff earlier, thereby lowering accessible capacity. Therefore a valid model must recover the conventional expectation that globally faster kinetics tends to increase cutoff-limited capacity and shorten relaxation.

The experimental BM result is more specific:

- accessible capacity increases;
- conversion-associated effective relaxation becomes longer rather than shorter.

The model should therefore explain a **departure from a one-dimensional global kinetic speed**, not claim that capacity is unrelated to kinetics.

## 2. Homogeneous single-population control

A single homogeneous O–I–I*–C population was discharged galvanostatically to a fixed model voltage cutoff. All kinetic rate constants were scaled together while equilibrium parameters were held fixed.

| Global rate scale | Normalized cutoff capacity | matched-state t63 (min) |
|---:|---:|---:|
| 0.50 | 0.2993 | 22.45 |
| 0.75 | 0.4187 | 17.12 |
| 1.00 | 0.5585 | 13.45 |
| 1.50 | 0.7399 | 9.12 |
| 2.00 | 0.8322 | 6.95 |

Result:

> In a homogeneous network controlled by one global kinetic-speed axis, faster kinetics gives both higher cutoff-limited capacity and shorter relaxation.

Thus capacity is kinetic-dependent, and the model reproduces this expected coupling.

## 3. Minimal heterogeneous-accessibility extension

The reference system contains a fast accessible population with weight 0.65.

The BM-like illustrative case **retains the same fast population** and adds an additional accessible conversion population with weight 0.15. The added population uses the same O–I–I*–C topology and thermodynamics, but its structural reconstruction step R2 is ten times slower. No parameter is fitted to BM-HEO.

Reference:
- fast population weight = 0.65;
- normalized cutoff capacity = 0.55845;
- matched-state t63 = 13.45 min.

Illustrative added-slow-population case:
- original fast population retained at 0.65;
- additional slow population weight = 0.15;
- slow-population R2 rate scale = 0.10;
- normalized cutoff capacity = 0.65714;
- matched-state t63 = 15.28 min.

Relative change:
- cutoff capacity: **+17.67%**;
- t63: **+13.63%**;
- relaxation amplitude at the matched state: **−9.40%**.

This directly demonstrates

\[
Q_{\rm cutoff}\uparrow
\qquad\text{and}\qquad
t_{63}\uparrow
\]

within the same coupled conversion framework.

## 4. Physical interpretation

The heterogeneous extension does not make capacity independent of kinetics.

Instead, two effects act simultaneously:

1. **More material becomes electrochemically accessible.**  
   This increases the amount of reaction that can be reached before the voltage cutoff and therefore increases capacity.

2. **The newly accessible material includes a slower-relaxing conversion population.**  
   This increases the contribution of slow internal redistribution to the current-off response and can lengthen the ensemble effective t63.

Therefore capacity and relaxation remain kinetically coupled, but no longer collapse onto one global fast–slow coordinate.

## 5. What the model does and does not establish

Supported model-level statement:

> A conversion electrode can show higher cutoff-limited capacity together with slower post-interruption relaxation when a materials modification increases accessible reaction population while also changing the distribution of internal kinetic timescales.

Not established experimentally:

- BM specifically creates a slow R2 population;
- the numerical weights 0.65 and 0.15 represent measured phase fractions;
- the tenfold R2 difference is a fitted microscopic rate ratio;
- one particular microscopic process is responsible for the experimental t63 increase.

The two-population calculation is an **existence proof / mechanistic-consistency test**, not a fit.

## 6. Consequence for Figure 7

Figure 7 should explicitly show both levels:

**Conventional single-axis expectation:**  
global kinetics faster → capacity up, relaxation faster.

**Conversion-network result:**  
changing accessibility and the distribution of conversion states can move capacity and relaxation in different directions.

The correct manuscript wording is therefore:

> Capacity and post-interruption relaxation are both governed by conversion kinetics, but they probe different consequences of a heterogeneous multistep reaction network. They are coupled, yet need not vary monotonically with one another.

This replaces any wording implying that capacity and relaxation are independent.
