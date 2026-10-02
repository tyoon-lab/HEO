# HEO polarization–t63 pivot lock — 2026-10-03

## Decision

The manuscript will no longer use accessible capacity as a direct measure of conversion kinetic speed.

The previous central question,

> Why can higher accessible capacity coexist with slower relaxation?

is replaced by the narrower experimental question,

> Does conversion-region polarization magnitude track the timescale of post-interruption relaxation?

The raw GITT data show that it does not do so universally.

---

## New central physical distinction

Two response dimensions are separated:

1. **polarization magnitude under/after load**
2. **post-interruption relaxation timescale**

Preferred operational polarization:

[
Delta E_{mathrm{pol,60}}
=
|E_{mathrm{rest,60,min}}-E_{mathrm{pulse,end}}|.
]

Preferred timescale:

[
t_{63}
]

from the existing 3 s-to-60 min current-off relaxation.

The first is an amplitude-like response; the second is a timescale-like response.

Do not call Delta E_pol,60 the exact equilibrium overpotential. Use:
- operational conversion polarization;
- 60-min recoverable polarization;
- conversion-associated polarization after background subtraction.

---

## Why this pivot is experimentally justified

Over z = 0.40–0.90:

- HEO: 195.9 mV, 10.37 min
- BM-HEO: 182.6 mV, 13.02 min
- Mg-HEO: 126.4 mV, 10.53 min
- BM-Mg-HEO: 148.2 mV, 12.70 min

Therefore:

- milling in the Mg-free pair lowers/slightly lowers polarization but lengthens t63;
- Mg incorporation strongly lowers polarization but leaves t63 almost unchanged;
- milling in the Mg-containing pair increases both.

A single global fast–slow coordinate cannot represent all three material-modification directions.

---

## Conversion localization survives the new definition

Using the same background protocol as the previous relaxation-hump analysis, the background-subtracted Delta E_pol,60 excess peaks at rest-end voltages:

- HEO: 0.537 V
- BM-HEO: 0.618 V
- Mg-HEO: 0.387 V
- BM-Mg-HEO: 0.503 V

The corresponding dQ/dV peaks are:

- 0.545
- 0.589
- 0.419
- 0.485 V

All offsets are within approximately 32 mV.

Thus Figure 5 can be retained conceptually, but it should be rewritten around **conversion-associated polarization / relaxation response**, not around a capacity-origin argument.

---

## Capacity role after the pivot

Capacity remains in Figure 3 because it is an important material-performance outcome.

However:

- do not infer conversion kinetic speed from capacity;
- do not use capacity as one axis of the kinetic mismatch;
- do not argue that terminal polarization controls the sample-to-sample capacity difference;
- do not require the model to reproduce capacity ordering.

This removes the weakest causal step in the previous manuscript.

---

## Figure 4 direction

Figure 4 should become the direct descriptor figure.

Preferred architecture to test next:

(a) representative pulse/rest definition:
- E_pulse,end
- E_rest,3s
- E_rest,60min
- Delta E_pol,60
- Delta E_relax
- t63

(b) state-resolved Delta E_pol,60 versus z for all four samples

(c) state-resolved t63 versus z for all four samples

(d) polarization–t63 observable map / material-modification arrows

The exact panel design is not yet frozen, but the scientific role is frozen.

---

## Figure 5 direction

Retain conversion localization.

Update the response quantity from the former relaxation-only hump to the conversion-associated polarization/recovery feature if this improves clarity.

The nominal localization remains valid under the Delta E_pol,60 definition.

---

## Figure 6 status

The former Q-based four-step microkinetic model is no longer the default Main Figure 6.

Preferred priority:

1. first test whether existing cycle-history data provide a fully experimental robustness figure for polarization–timescale decoupling;
2. only if needed, build a minimal multistep consistency model for polarization amplitude versus relaxation timescale;
3. keep the old Q-based R2/R3 model as historical/optional SI material, not as the causal explanation of capacity.

---

## Conventional Dapp status

The HEO/BM Dapp conflict remains valid but becomes secondary.

It can remain:
- a compact supporting panel if space and narrative require it; or
- SI-only if the new direct polarization–t63 story is sufficiently complete.

Do not make the paper primarily about failure of conventional GITT.

---

## New minimum paper claim

Preferred form:

> **Material modification changes conversion-region polarization magnitude and post-interruption relaxation timescale in distinct ways, showing that the two responses do not collapse onto a single kinetic fast–slow coordinate.**

A second sentence can state:

> **The polarization feature is localized to the conversion region by its correspondence with the cathodic differential-capacity response.**

Do not add a microscopic cause until independently supported.

---

## Files

Primary numerical audit:

`modeling/HEO_CONVERSION_POLARIZATION_T63_AUDIT_2026-10-03.md`

Summary table:

`modeling/HEO_CONVERSION_POLARIZATION_T63_SUMMARY_2026-10-03.csv`

The existing terminal-polarization and Figure 6 reassessment files remain useful as the audit trail showing why the capacity/polarization interpretation was abandoned.
