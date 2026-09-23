# Cycle-Resolved GITT and Figure 6 Background Audit — 2026-09-23

## Purpose

This note records the final experimental basis for Figure 6.

The new information added by cycles 2–3 is **not merely a repetition** of the Figure 5 conclusion that relaxation magnitude, timescale, and capacity do not map one-to-one.

The new result is that the **conversion-associated relaxation itself evolves with cycling**.

## Core cycle-resolved result

For lithiation over common normalized z=0.4–0.9:

| Sample | C1 Delta E / t63 | C2 Delta E / t63 | C3 Delta E / t63 |
|---|---|---|---|
| HEO | 168.5 mV / 10.37 min | 129.2 / 9.43 | 138.4 / 9.57 |
| BM-HEO | 160.5 / 13.02 | 125.7 / 11.18 | 133.5 / 11.33 |
| Mg-HEO | 111.3 / 10.53 | 127.9 / 9.83 | 140.9 / 9.53 |
| BM-Mg-HEO | 135.2 / 12.70 | 126.7 / 10.90 | 142.6 / 10.73 |

Conversion-associated hump peaks:

| Sample | C1 | C2 | C3 | z_peak C1→C3 |
|---|---:|---:|---:|---:|
| HEO | 71.2 | 23.4 | 31.0 mV | 0.77→0.55 |
| BM-HEO | 44.8 | 17.2 | 22.4 | 0.67→0.54 |
| Mg-HEO | 15.9 | 19.3 | 27.0 | 0.79→0.56 |
| BM-Mg-HEO | 21.1 | 12.6 | 20.8 | 0.66→0.53 |

The first-cycle late feature around z~0.66–0.79 shifts to a common earlier region around z~0.50–0.56 in later cycles.

## Amplitude vs timescale evolution

Cycle-1 to cycle-3:

| Sample | A3/A1 | amplitude change | t63,3/t63,1 | timescale change |
|---|---:|---:|---:|---:|
| HEO | 0.435 | -56.5% | 0.923 | -7.7% |
| BM-HEO | 0.500 | -50.0% | 0.870 | -13.0% |
| Mg-HEO | 1.698 | +69.8% | 0.905 | -9.5% |
| BM-Mg-HEO | 0.986 | -1.4% | 0.845 | -15.5% |

Interpretation:
- cycle history strongly changes the magnitude/population of the conversion-associated relaxation;
- the ensemble effective timescale changes much less;
- therefore the first-cycle hump is not a stationary kinetic fingerprint.

This is stronger than simply repeating “amplitude and t63 are different observables.”

## Persistent reversible-capacity differences

Third-cycle approximate GITT lithiation/delithiation capacities:

| Sample | lithiation | delithiation |
|---|---:|---:|
| HEO | 700 | 733 |
| BM-HEO | 833 | 817 |
| Mg-HEO | 450 | 467 |
| BM-Mg-HEO | 533 | 533 |

Mg suppresses later-cycle accessible reversible reaction extent by ~35–36%, while later-cycle HEO/Mg t63 values are similar.

BM increases later-cycle accessible extent while t63 remains longer than the corresponding non-BM sample.

This provides a strong material-level constraint for Figure 7.

## Delithiation asymmetry

Third-cycle delithiation t63:
- HEO 6.63 min
- BM-HEO 8.25 min
- Mg-HEO 7.05 min
- BM-Mg-HEO 7.80 min

These are generally shorter than third-cycle lithiation t63 (~9.5–11.3 min), establishing direction asymmetry.

Do not uniquely assign this asymmetry to a microscopic mechanism.

## Background-sensitivity audit

Nominal later-cycle background:
same exponential form used for first cycle.

Alternative:
linear background over the same background windows.

Results:

| Sample | Cycle | exp peak | linear peak | z_peak exp = linear |
|---|---:|---:|---:|---:|
| HEO | 2 | 23.247 | 23.246 mV | 0.5476 |
| HEO | 3 | 30.751 | 30.750 | 0.5476 |
| BM-HEO | 2 | 17.012 | 17.011 | 0.5098 |
| BM-HEO | 3 | 22.125 | 22.124 | 0.5400 |
| Mg-HEO | 2 | 19.258 | 19.258 | 0.5000 |
| Mg-HEO | 3 | 26.854 | 26.854 | 0.5556 |
| BM-Mg-HEO | 2 | 12.382 | 12.381 | 0.5000 |
| BM-Mg-HEO | 3 | 20.580 | 20.578 | 0.5313 |

Quantitative audit:
- peak-amplitude difference <0.012% in every C2/C3 case;
- peak z identical;
- max background difference <0.0016 mV;
- exponential background tau_z ~2.4e3–5.4e3, i.e. effectively linear.

Conclusion:
**The cycle-dependent hump evolution is not an artifact of later-cycle background selection.**

Figure 5 first-cycle analysis should retain the exponential background; the first-cycle background is genuinely curved and should not be forced into the later-cycle linear limit.

## Figure 6 role

Preferred scientific message:

**Cycling strongly redistributes the magnitude of the conversion-associated relaxation while producing only modest changes in its effective timescale.**

Possible stronger second sentence:

**The first-cycle relaxation hump is therefore not a stationary kinetic fingerprint, but a history-dependent response whose excitation evolves as the cycled conversion state is established.**

Avoid `reconstructed state` unless structural reconstruction is independently demonstrated. Use `cycled state` or `post-first-cycle state`.

## Candidate panels

- (a) cycle-resolved excess profiles or selected C1/C2/C3 comparison
- (b) hump amplitude vs cycle
- (c) t63 vs cycle
- (d) persistent reversible capacity / summary map

The exact panel-d design can still be optimized without changing the scientific message.
