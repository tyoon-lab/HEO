# HEO — Hump-anchored lithiation C1/C2/C3 comparison (2026-11-13)

**Status:** exploratory PI-requested reaction-identity *working hypothesis*; **do not update manuscript, locked Abstract/Introduction, Figures or first-lithiation R1–R4 boundaries**. User explicitly requests studying a *dominant process* rather than requiring cycle-to-cycle equality of kinetic amplitude, potential or chemical state. This is a hypothesis test, not chemical proof.

## Research question
Suppose the mid/late lithiation hump in the magnitude of GITT voltage relaxation |ΔErest| is an observable of a broadly similar dominant conversion process on C1 and C2/C3. Does hump-anchoring separate an extra first-cycle *pre-hump charge contribution* from a subsequently recurring *post-hump portion*? How do those differences relate to the PI-locked R1–R4 charge changes under ball milling and Mg incorporation?

## Source/procedure
- Use local, complete-full-pulse GITT `HEO_GITT_C1_C3_joined_lith_delith_throughput.csv`, all four materials with C1/C2/C3 lithiation, based on same-cell 600s pulse/3600s rest.
- For each sample and cycle, identify the broad mid/late local `|ΔErest|` peak. HEO and Mg-HEO C1/C2/C3 peaks are **unambiguous**: Savitzky–Golay windows 5/7/9/11/13 pulses all select *exactly the same pulse*.
- BM-HEO C1 has **no true mid/late local maximum**, only a broad flat shoulder; provisional *visual landmark* ~750 mAh/g. BM-Mg-HEO C1 has no maximum; a weaker, sloping shoulder ~600 mAh/g is a provisional landmark. BM-Mg C2 also has a weak shoulder ~250 mAh/g. These positions must NOT be advertised as objectively identified peaks, and their quantitative first-cycle capacities are **anchor-choice sensitive**.
- For each halfcycle, define `Qrelative = Qpulse − Qanchor`, making the landmark `Qrelative=0`. **Do not force vertical/amplitude overlap**; different magnitudes, potentials, t63 values are permissible under the PI's dominant-process hypothesis.
- Cutoff partial pulses omitted (this is pulse-resolved time/characteristic response), so totals differ slightly from earlier partial-pulse-inclusive total Q. Same-cell C2/C3 are sequential, not replicate cells.
- First-lithiation region boundaries remain HEO 6/25/55, BM-HEO 9/38/60, Mg-HEO 7/24/42, BM-Mg-HEO 9/35/46, and must not be redefined by hump alignment.

## Hump anchor positions (nominal mAh/g, relative lithiation charge)
| sample | C1 Q anchor and confidence | C2 Q anchor | C3 Q anchor | C1% of full Q | C2% | C3% |
|---|---|---:|---:|---:|---:|---:|
| HEO | **816.7 clear peak** | 366.7 clear | 350.0 clear | 75.4 | 52.4 | 50.0 |
| BM-HEO | **~750 broad shoulder, tentative** | 400 weak peak | 400 weak peak | ~59.2 | 47.1 | 48.0 |
| Mg-HEO | **633.3 clear peak** | 233.3 clear | 233.3 clear | 79.2 | 50.0 | 51.9 |
| BM-Mg-HEO | **~600 sloping shoulder, tentative** | ~250 weak shoulder | 266.7 weak peak | ~64.3 | ~44.1 | 50.0 |

**Robust observation:** Later-cycle identifiable hump/shoulder occurs in the vicinity of **44–52% of C2/C3 lithiation charge** across four samples. This does **not** prove that most charge passes through the hump: a voltage-recovery-amplitude feature is not a chemical reaction rate or local charge-density maximum.

The two confidently located C1 peaks are **inside the first-lithiation R3 interval** (HEO R3 416.7–916.7 mAh/g; Mg-HEO R3 400–700). The provisional BM first-cycle shoulders happen near early R3 but that regional correspondence must not be made a hard claim.

## Charge split if the hump is a same-dominant-process anchor
C2/C3 baseline is their arithmetic mean. `Qbefore = Qanchor`, `Qafter = Qtotal − Qanchor` (full-rest complete-pulse totals).

| sample | C1 pre-hump | C2/C3 mean pre | **C1 extra pre** | C1 post-hump | C2/C3 mean post | **C1 extra post** | total C1 extra |
|---|---:|---:|---:|---:|---:|---:|---:|
| HEO | 816.7 | 358.3 | **+458.3** | 266.7 | 341.7 | **−75.0** | +383.3 |
| BM-HEO [tentative C1 shoulder] | ~750.0 | 400.0 | **~+350.0** | ~516.7 | 441.7 | **~+75.0** | +425.0 |
| Mg-HEO | 633.3 | 233.3 | **+400.0** | 166.7 | 225.0 | **−58.3** | +341.7 |
| BM-Mg-HEO [tentative C1 shoulder] | ~600.0 | 258.3 | **~+341.7** | ~333.3 | 291.7 | **~+41.7** | +383.3 |

The robust HEO/Mg-HEO result is especially informative: **before** the selected hump, the first cycle passes ~400–458 mAh/g additional charge, while **after** the hump it has ~58–75 mAh/g *less* charge than the later-cycle average. Therefore first-cycle total extra charge is not identical to a single local early reaction, and the late reaction has changed in size too.

For first-cycle BM shoulder anchors, a ±50–100 mAh/g movement changes the pre/post split by the same amount. These numbers are hypotheses, not objective charge assignments.

## Relation to first-lithiation modification contrasts and later recurring capacities
First-C1 R1–R4 full-pulse charges (mAh/g):
- HEO: R1 100, R2 316.7, R3 500, R4 166.7.
- BM-HEO: R1 150, R2 483.3, R3 366.7, R4 266.7.
- Mg-HEO: R1 116.7, R2 283.3, R3 300, R4 100.
- BM-Mg-HEO: R1 150, R2 433.3, R3 183.3, R4 166.7.

Exploratory **later-cycle post-hump** charge differences (mAh/g) versus key C1 modification-induced regional change:
| matched modification comparison | C1 change in main affected region | C2/C3 post-hump charge difference |
|---|---|---|
| BM-HEO − HEO | R2 +166.7 | +100.0 |
| BM-Mg-HEO − Mg-HEO | R2 +150.0 | +66.7 |
| Mg-HEO − HEO | R3 −200.0 | −116.7 |
| BM-Mg-HEO − BM-HEO | R3 −183.3 | −150.0 |

**Signs agree**, a promising directional relationship between material modification in C1 and later *post-hump charge capacity*. **This is a hypothesis-generating comparison only:** the first-cycle R2/R3 charge is not mapped one-to-one to later post-hump charge; the hump anchors mark different stoichiometries/voltages, C2/C3 post-hump charge is not necessarily a chemically isolated conversion step; R1/R4 and entire C1 paths may also contribute.

## Measured differences at the selected anchors
| sample | C1 / C2 / C3 ΔErest magnitude (mV) | C1 / C2 / C3 t63 (s) | C1 / C2 / C3 QOCV (V) |
|---|---|---|---|
| HEO | 188 / 137 / 150 | 774 / 556 / 568 | 0.537 / 0.847 / 0.859 |
| BM-HEO | 161 / 144 / 152 | 718 / 587 / 605 | 0.672 / 0.873 / 0.860 |
| Mg-HEO | 115 / 137 / 148 | 735 / 585 / 579 | 0.387 / 0.762 / 0.774 |
| BM-Mg-HEO | 133 / 144 / 155 | 738 / 582 / 600 | 0.516 / 0.837 / 0.809 |

These differing QOCVs and t63s at hump *do not invalidate a repeatable dominant-process hypothesis* because the material and pathway may differ, but they prevent claiming the peaks correspond to an identical phase or thermodynamic state. In most samples the post-hump |ΔErest| values converge toward cutoff and post-hump QOCV curves trend toward common cutoff conditions, while the t63 absolute shift remains.

## Local visualizations created in conversation runtime (not committed to GitHub binaries)
- `HEO_hump_anchor_deltaErest_zoom_2x2.png` (hump-focused); `HEO_hump_anchor_deltaErest_2x2.png` (full signal).
- `HEO_hump_anchor_t63_2x2.png`, `HEO_hump_anchor_QOCV_2x2.png`, `HEO_hump_anchor_dQdV_2x2.png`, `HEO_hump_anchor_before_after_capacity_2x2.png`.
- Source pulse CSV `HEO_hump_anchor_C1_C3_pulsewise.csv` and summary `HEO_hump_anchor_C1_C3_summary.csv`, pre/post `HEO_hump_anchor_pre_post_capacity_differences.csv`, reproducibility Python `HEO_hump_anchor_cycle_comparison.py`.
- Figures use the same within-halfcycle capacity coordinates, x=Q−Qanchor; C1 R2/R3 and R3/R4 boundaries shown in gray when visible. Only C1 lithiation is region-labelled; C2/C3 are **not** force-segmented.

## Next internal research question
1. **C1 hump identity** is the weakest link under BM: distinguish monotonic shoulder caused by morphological broadening from a separate reaction, assess anchor uncertainty without tuning to produce a desired early charge count.
2. Test whether hump anchors correlate with **GITT local dQ/dV feature**, and changes in relaxation spectra beyond a single t63. A ΔErest peak is not itself a capacity-concentration peak.
3. Compare region R2 and R3 perturbation contrasts with later *pre*/*post*-hump charge while controlling for state-of-charge/voltage cutoff and the enormous first-cycle hysteresis. Under this working hypothesis do not demand identical absolute QOCV/t63/ΔErest.
4. If convincing, one concise Results/SI sentence may explain that first-lithiation-specific capacity precedes a reproducible later-cycle relaxation-amplitude feature; **no manuscript change without PI decision**.


## New local QOCV-differential and modification decomposition (2026-11-13 continuation)

PI clarification: the hump is an **observable fiducial marker** for comparing a candidate recurring dominant process; it is **not assumed** to represent a charge maximum, local reaction-rate maximum, or identical time constant. Internal continuation on the same original 12 lithiation traces (C1/C2/C3; four materials), no manuscript change.

### Independent QOCV-derived |dQ/dV| relative to |ΔErest| marker
- QOCV was smoothed with a seven-pulse, quadratic Savitzky–Golay filter before calculating local \`|dQ/dV| = 1/|dQOCV/dQ|\`. Also checked raw, five-pulse and nine-pulse derivatives. Search local \`|dQ/dV|\` maximum only within ±150 mAh/g of the **independently chosen |ΔErest| anchor**; the maximum may lie elsewhere globally. \`|dQ/dV|\` need not peak at the relaxation-amplitude hump.
- In **C2/C3**, the local \`|dQ/dV|\` maxima occur *before* the \`|ΔErest|\` marker: HEO **−33/−17**, BM-HEO **−17/−33**, Mg-HEO **−67/−50**, BM-Mg-HEO **−33/−50 mAh/g**, respectively. These offsets are approximately 1–4 GITT pulses and are stable within one pulse under raw/5/7/9 smoothing choices. Thus the hump is a potentially robust marker around a broad reaction feature, **not the unique maximum of charge concentration**.
- In C1, HEO's local differential-charge maximum is **+83 mAh/g after** its unambiguous |ΔErest| hump, whereas Mg-HEO's is approximately **at** its hump; therefore a fixed relation between the two descriptors is neither expected nor demonstrated. C1 BM hump/shoulder markers remain tentative.
- At the hump itself, t63 is generally still **increasing** with lithiation: for HEO C1 near Qrelative=0, t63 goes ~709 s at −50 mAh/g, 774 s at 0, ~842 s at +50; C2/C3 show a smaller monotone rise. An amplitude hump without t63 hump is entirely consistent with changing amplitude/weights in the relaxation spectrum. This is a hypothesis, not a decomposition of relaxation modes.
- Diagnostic figure locally: \`HEO_hump_anchor_local_dQdV_2x2.png\`; detailed local estimates \`HEO_hump_local_dQdV_t63_dErest_comparison.csv\`. These file binaries have not been pushed to GitHub.

### C2/C3 modification effect split at the hump/shoulder
Use **C2 and C3 average** halfcycle charge and separately derived anchors (no C1 anchor enters this calculation). The total matched capacity effect is decomposed arithmetically into *before marker* and *after marker*:

| Matched contrast | ΔQ before marker | ΔQ after marker | total ΔQ | fraction of total from after marker |
|---|---:|---:|---:|---:|
| BM-HEO − HEO | +41.7 | **+100.0** | +141.7 | **70.6%** |
| BM-Mg-HEO − Mg-HEO | +25.0 | **+66.7** | +91.7 | **72.7%** |
| Mg-HEO − HEO | **−125.0** | **−116.7** | −241.7 | 48.3% |
| BM-Mg-HEO − BM-HEO | **−141.7** | **−150.0** | −291.7 | 51.4% |

All units mAh/g; positive/negative sign is the change in matched sample's GITT lithiation nominal charge (complete pulses). **Exploratory implication:** Ball-milling's additional later-cycle charge is *nominally* more concentrated after the marker, while Mg-associated later-cycle charge reduction spans both sides approximately equally. This is more discriminating than the older statement that only the sign of later post-marker capacity agrees with C1 R2 or R3 effects. Still no causal allocation or quantitative 1:1 inheritance of an initial R2/R3 process.

### Sensitivity and limits
- Moving **either** of the two matched materials' C2/C3 marker by just ±1 pulse (~16.7 mAh/g) can change the estimated after-marker share of ball-milling effects from **47–94% (Mg-free)** or **36–109% (Mg-containing)** under independent worst-case shifts; for Mg effects from **35–62%** (unmilled) or **40–63%** (milled). The BM anchor is weaker than the HEO/Mg peak, so **do not publish the nominal ~71–73% as a precise mechanistic fraction**.
- Each matched comparison derives from one sample trajectory, with no inter-cell replicates, and only two chronological later cycles. The comparisons are not independent confirmatory samples.
- The first-cycle **R2 ball-milling gain** (+166.7 or +150 mAh/g) and **R3 Mg-associated loss** (−200 or −183.3 mAh/g) are assigned by **t63 first-cycle regions**, whereas later marker bins are **|ΔErest| features**. They should be plotted side by side as trends, not treated as chemically identical bins.
- Stronger hypothesis to test: a common *broad reaction window* produces a stable differential-charge peak slightly *ahead* of the later-cycle relaxation-amplitude marker; ball milling changes the charge passed after the marker more than before, whereas Mg incorporation reduces charge on both sides. Validate with raw time-domain relaxation spectral shape, peak/shoulder positioning stability and independent structure evidence before considering a manuscript claim.
- Generated local figures \`HEO_hump_anchor_later_cycle_modification_effects.png\` and \`HEO_hump_anchor_local_dQdV_2x2.png\`, with local CSV \`HEO_hump_anchor_modification_effect_decomposition.csv\` and script \`HEO_hump_effect_decomposition.py\`. No Word or locked manuscript edits.
