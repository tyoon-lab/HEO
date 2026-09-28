# HEO Figure 6 Artwork Final Note — 2026-09-27

**Status:** scientific role frozen; main-panel architecture simplified after artwork review.

## Figure-level question

**Does the conversion-associated relaxation remain a fixed first-cycle feature, or does it evolve with reaction history?**

Figure 6 is a history-dependence figure. It is not another conversion-localization figure and it should not repeat the full state-resolved profile display already used in Figure 5.

## Final main-panel architecture

### (a) Conversion-associated peak state versus cycle

Plot the state coordinate of the excess-relaxation maximum, $z_{\mathrm{peak}}$, for cycles 1–3.

Values:
- HEO: 0.7692 → 0.5476 → 0.5476
- BM-HEO: 0.6711 → 0.5098 → 0.5400
- Mg-HEO: 0.7917 → 0.5000 → 0.5556
- BM-Mg-HEO: 0.6607 → 0.5000 → 0.5313

Role:
show directly that the late first-cycle feature shifts toward a common earlier reaction-state region after cycling.

The full cycle-resolved excess profiles remain in the Supporting Information.

### (b) Excess peak amplitude versus cycle

Plot the conversion-associated excess peak amplitude for cycles 1–3.

Values, mV:
- HEO: 71.2 → 23.4 → 31.0
- BM-HEO: 44.8 → 17.2 → 22.4
- Mg-HEO: 15.9 → 19.3 → 27.0
- BM-Mg-HEO: 21.1 → 12.6 → 20.8

Role:
show that the magnitude of the conversion-associated relaxation is strongly history dependent and changes differently among the four materials.

Do not interpret amplitude as an intrinsic rate.

### (c) Median $t_{63}$ versus cycle

Plot the median $t_{63}$ over the common lithiation interval $z=0.4$–0.9.

Values, min:
- HEO: 10.37 → 9.43 → 9.57
- BM-HEO: 13.02 → 11.18 → 11.33
- Mg-HEO: 10.53 → 9.83 → 9.53
- BM-Mg-HEO: 12.70 → 10.90 → 10.73

Role:
pair directly with panel (b) to show that the effective relaxation timescale changes much less than the response magnitude.

### (d) Normalized amplitude-change versus timescale-change map

Plot:
- x = $t_{63,3}/t_{63,1}$
- y = $A_3/A_1$

with unity reference lines.

Values:
- HEO: (0.9229, 0.4354)
- BM-HEO: (0.8702, 0.5000)
- Mg-HEO: (0.9050, 1.6981)
- BM-Mg-HEO: (0.8449, 0.9858)

Role:
compactly show that the four materials occupy a narrow timescale-change range but a much broader amplitude-change range.

## Why panel (a) was simplified

An earlier architecture used full C1/C2/C3 excess profiles in panel (a). The publication artwork review showed that this repeated curve-level information already established in Figure 5 and made Figure 6 visually dense.

The peak-state plot is preferable because:
1. the new information in Figure 6 is **history dependence**;
2. the C1-to-later-cycle state shift is expressed directly and quantitatively;
3. panels (a)–(c) now use the same cycle axis and form a compact descriptor sequence;
4. full profile shapes and later-cycle background sensitivity remain available in the SI.

## Main message

**The conversion-associated relaxation is history dependent: its state location and magnitude evolve strongly with cycling, while its effective relaxation timescale changes comparatively modestly.**

A second material-level constraint remains in the text/SI:
- BM retains greater later-cycle accessible capacity while $t_{63}$ remains longer than HEO;
- Mg retains lower later-cycle accessible capacity while later-cycle $t_{63}$ approaches Mg-free values.

Do not promote later-cycle capacity to another main panel; Figure 6 should remain focused on relaxation history.

## Claim boundaries

Supported:
- the conversion-associated response changes with cycle history;
- peak state converges toward an earlier normalized reaction-state region after the first cycle;
- response magnitude changes much more strongly than $t_{63}$;
- the first-cycle excess feature is not a stationary relaxation fingerprint.

Do not claim:
- a unique structural origin for the cycle evolution;
- that amplitude is a conversion rate or phase fraction;
- that the common later-cycle $z_{\mathrm{peak}}$ identifies a unique phase boundary;
- that $t_{63}$ is a microscopic forward reaction constant.

## Artwork rules

Use the common HEO sample styling and order.
- normal-weight panel labels (a)–(d);
- left/bottom ticks only;
- cycles shown as 1, 2, 3;
- one shared legend is sufficient;
- no panel titles;
- panel (d) unity lines are references, not fit lines.

## Numeric authority

Main panel data:
`modeling/HEO_FIGURE6_PANEL_DATA_2026-09-27.csv`

Underlying audit:
`modeling/HEO_CYCLE_RESOLVED_GITT_AND_BACKGROUND_AUDIT_2026-09-23.md`

Compact earlier descriptor table:
`modeling/HEO_CYCLE_HISTORY_DESCRIPTORS_2026-09-23.csv`


## Final manuscript caption — 2026-09-28

**Figure 6. Conversion-associated relaxation evolves with cycle history.** (a) Cycle dependence of the normalized lithiation state at the excess-relaxation peak, $z_{\mathrm{peak}}$. (b) Corresponding excess-peak amplitude during cycles 1–3. (c) Median characteristic relaxation time, $t_{63}$, over the common lithiation-state interval. (d) Relative change in excess-peak amplitude, $A_3/A_1$, plotted against the corresponding change in relaxation timescale, $t_{63,3}/t_{63,1}$, from cycle 1 to cycle 3. Dashed lines denote unity. Cycling produces substantially larger changes in the magnitude and state location of the conversion-associated response than in its characteristic relaxation timescale.
