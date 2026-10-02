# HEO cycle-resolved conversion-polarization–t63 audit — 2026-10-03

## Purpose

Test whether the new first-cycle conclusion — conversion-region polarization magnitude and post-interruption relaxation timescale are non-equivalent response coordinates — survives electrochemical history.

This audit reparses the original GITT workbooks for lithiation cycles 1–3 using the same definitions adopted in:

`modeling/HEO_CONVERSION_POLARIZATION_T63_AUDIT_2026-10-03.md`

---

## Definitions

Operational 60-min recoverable polarization:

[
Delta E_{mathrm{pol,60}}
=
|E_{mathrm{rest,60,min}}-E_{mathrm{pulse,end}}|.
]

Slower current-off relaxation magnitude:

[
Delta E_{mathrm{relax}}
=
|E_{mathrm{rest,60,min}}-E_{mathrm{rest,3,s}}|.
]

Characteristic timescale:

[
t_{63}
]

defined from the 3 s-to-60 min relaxation.

All cycle summaries use the common normalized lithiation window (z=0.40)–0.90.

The final cutoff-truncated pulse of each lithiation is excluded.

---

## Validation against the previous cycle-history authority

The re-parsed cycle-resolved (Delta E_{mathrm{relax}}) and (t_{63}) medians reproduce the previous cycle-history values:

| Sample | Cycle | Delta E_relax (mV) | t63 (min) |
|---|---:|---:|---:|
| HEO | 1 | 168.5 | 10.37 |
| HEO | 2 | 129.2 | 9.43 |
| HEO | 3 | 138.4 | 9.57 |
| BM-HEO | 1 | 160.5 | 13.02 |
| BM-HEO | 2 | 125.7 | 11.18 |
| BM-HEO | 3 | 133.5 | 11.33 |
| Mg-HEO | 1 | 111.3 | 10.53 |
| Mg-HEO | 2 | 127.9 | 9.83 |
| Mg-HEO | 3 | 140.9 | 9.53 |
| BM-Mg-HEO | 1 | 135.2 | 12.70 |
| BM-Mg-HEO | 2 | 126.7 | 10.90 |
| BM-Mg-HEO | 3 | 142.6 | 10.73 |

This validates the cycle segmentation and permits direct extension to (Delta E_{mathrm{pol,60}}).

---

## Cycle-resolved recoverable polarization

| Sample | Cycle 1 (mV) | Cycle 2 (mV) | Cycle 3 (mV) |
|---|---:|---:|---:|
| HEO | 195.9 | 142.6 | 150.0 |
| BM-HEO | 182.6 | 134.2 | 141.0 |
| Mg-HEO | 126.4 | 140.1 | 153.7 |
| BM-Mg-HEO | 148.2 | 135.6 | 151.0 |

Corresponding (t_{63}):

| Sample | Cycle 1 (min) | Cycle 2 (min) | Cycle 3 (min) |
|---|---:|---:|---:|
| HEO | 10.37 | 9.43 | 9.57 |
| BM-HEO | 13.02 | 11.18 | 11.33 |
| Mg-HEO | 10.53 | 9.83 | 9.53 |
| BM-Mg-HEO | 12.70 | 10.90 | 10.73 |

---

## Cycle-3 / cycle-1 ratios

| Sample | Delta E_pol,60 C3/C1 | polarization change | t63 C3/C1 | t63 change |
|---|---:|---:|---:|---:|
| HEO | 0.766 | -23.4% | 0.923 | -7.7% |
| BM-HEO | 0.772 | -22.8% | 0.870 | -13.0% |
| Mg-HEO | 1.216 | +21.6% | 0.905 | -9.5% |
| BM-Mg-HEO | 1.019 | +1.9% | 0.844 | -15.6% |

### Key observation

The history-induced directions are not universal:

- HEO and BM-HEO: polarization decreases while t63 also decreases, but by substantially different relative amounts.
- Mg-HEO: polarization **increases by about 22% while t63 decreases by about 9.5%**.
- BM-Mg-HEO: polarization is nearly unchanged while t63 decreases by about 16%.

Therefore a change in polarization magnitude does not uniquely predict either the sign or magnitude of the change in relaxation timescale.

The Mg cycle-history result is especially useful because it gives an opposite-direction change within the **same material**, avoiding a purely cross-composition interpretation.

---

## Fast versus slower recovery components

For reference, the 0–3 s recoverable component decreases from cycle 1 to cycle 3 in all four materials.

Approximate C3/C1 ratios:

- HEO: 0.442
- BM-HEO: 0.361
- Mg-HEO: 0.825
- BM-Mg-HEO: 0.649

The 3 s-to-60 min relaxation magnitude behaves differently:

- HEO: 0.821
- BM-HEO: 0.832
- Mg-HEO: 1.266
- BM-Mg-HEO: 1.055

This further shows that the current-off voltage response changes in both amplitude distribution and characteristic timescale with cycling.

Do not assign the fast component uniquely to ohmic or charge-transfer resistance.

---

## Preferred Figure 6 role

The cycle-history result can replace the former capacity-based microkinetic model as the Main Figure 6 endpoint.

Recommended conceptual message:

> **Electrochemical history changes conversion-region polarization magnitude and relaxation timescale in different directions and by different amounts, confirming that the two descriptors are not reducible to one scalar kinetic coordinate.**

This provides a fully experimental robustness test and avoids requiring a microscopic model assignment.

---

## Recommended Figure 6 architecture

### Panel (a)
Median (Delta E_{mathrm{pol,60}}) over (z=0.40)–0.90 versus cycle (1–3), four materials.

### Panel (b)
Median (t_{63}) over the same window versus cycle.

### Panel (c)
Normalized C3/C1 change map:
- x = (t_{63,3}/t_{63,1})
- y = (Delta E_{mathrm{pol,60},3}/Delta E_{mathrm{pol,60},1})
- unity lines.

This compactly shows:
- Mg: polarization up / t63 down;
- BM-Mg: polarization nearly unchanged / t63 down;
- HEO/BM: both down but with different relative magnitudes.

### Panel (d)
Optional decomposition or state-resolved trajectory:
- either fast 0–3 s versus slower 3 s–60 min recovery components across cycles;
- or cycle-resolved polarization–t63 trajectories with normalized state (z) encoded.

Choose the cleaner option after artwork testing.

---

## Claim boundary

Safe:
- polarization magnitude and relaxation timescale respond differently to both material modification and electrochemical history;
- the Mg cycle-history trajectory directly demonstrates opposite-direction amplitude/timescale evolution within one material;
- Figure 6 can serve as experimental robustness for the Figure 4 conclusion.

Not safe:
- cycling changes one unique elementary rate;
- increased polarization necessarily means slower kinetics;
- reduced polarization necessarily means faster kinetics;
- the fast 0–3 s component is purely ohmic/charge-transfer;
- the observed history dependence identifies a unique structural mechanism.

---

## Consequence

A dedicated Main-text microkinetic model is no longer necessary to establish the central experimental conclusion.

The former Q-based R2/R3 model may remain as archived/optional SI material, but it should not determine the paper narrative.
