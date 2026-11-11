# HEO — Same-cell GITT cycles 1–3, initial raw-data audit (2026-11-11)

**Status: INTERNAL EXPLORATORY ANALYSIS — NOT AUTHOR-APPROVED MAIN-TEXT CLAIM.** The PI proposed asking whether first-lithiation t63-defined R1–R4 response changes are carried into the subsequent delithiation/lithiation cycles. Keep the computational complexities here; present only the physically meaningful robust summary in the manuscript if warranted. **No Word manuscript, Figure, Abstract or locked Introduction is modified by this note.**

## Source and provenance

- Incoming file: `[GITT try 2_031].xlsx`, raw WonATech/Zive General Data Report.
- `Information_1` lists `HEO GITT TRY 4_cyc`, original 2022-12-15 run path `GITT try 2_031.wrd`, **1,264,853 actual records**; columns Index, Test Time(s), Voltage(V), Current(A). Two data sheets, continuous indices 1…1,264,853.
- Direct extraction of this attached file revealed 3 complete negative/positive-current cycles and 14 full-pulse negative-current steps of partial cycle 4. The archived `HEO GITT 로우 데이터.xlsx` matches its raw voltage/current sampled points (row 1, 199,999, 399,999, 599,999, 799,999, 999,999 checked; time has a constant original-export offset). This is consistent with previously adopted pristine-HEO first-lithiation **65 full pulses plus one terminal partial pulse**.
- Existing four files already present in the working material: `HEO GITT 로우 데이터.xlsx`, `BM HEO 3 GITT 로우 데이터.xlsx`, `HEO 3 Mg 로우 데이터.xlsx`, `BM HEO 3 Mg 로우 데이터.xlsx`. The archived / previously extracted pulsewise segment audit `heo_gitt_pulsewise_audit.json` for all four records provides actual pulse durations, 3600-second rests, 3s-to-rest-end deltaE, first-crossing t63 and 60min QOCV. The supplied source report and GitHub [four-sample first-cycle authority](../manuscript/HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md) provide first-cycle regions.
- All 4 datasets consist of **three complete cycles**, followed by **incomplete fourth lithiation**. Do NOT treat fourth-cycle partial data as a complete cycle or compute a fourth-cycle capacity-retention figure. All cycle capacities below include the terminal cutoff partial pulse, unlike earlier paper's first-cycle **complete-pulse-only** R1–R4 allocation.
- For capacity, integrate the nominal 100 mA g−1 current over each pulse's actual duration including terminal partial cutoff pulse: `Q [mAh/g] = 100 * Σ(duration_s) / 3600`. Note: validate actual schedule and mass normalization before publication; the extracted nominal report uses 100 mA/g.
- Negative-current halfcycle is labeled lithiation, positive-current delithiation, subject to the final tester sign and cell-configuration record check. Never automatically equate these GITT charge totals with the independently measured conventional 0.1-C GCD numbers in Figure 3.
- 1 s sample cadence for HEO and BM-HEO; 3 s cadence for Mg-HEO and BM-Mg-HEO. t63 uses 3s post-current-off and rest-end (3600 s), operational 63.2% first crossing; not a unique rate constant or chemical attribution.

## 1. Exact three-cycle GITT capacity summary (nominal mAh g−1, terminal partial pulses INCLUDED)

| Sample | Lith C1 | Delith C1 | Lith C2 | Delith C2 | Lith C3 | Delith C3 | Lith C1→C2 | Lith C2→C3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HEO | 1094.222 | 762.278 | 715.000 | 746.278 | 710.472 | 742.917 | −34.7% | −0.6% |
| BM-HEO | 1278.500 | 858.528 | 860.889 | 840.806 | 844.389 | 827.583 | −32.7% | −1.9% |
| Mg-HEO | 814.250 | 515.667 | 476.083 | 495.167 | 462.750 | 478.500 | −41.5% | −2.8% |
| BM-Mg-HEO | 948.167 | 583.167 | 577.583 | 563.417 | 549.583 | 543.500 | −39.1% | −4.8% |

Cycle 1 total includes terminal partial pulse: HEO 65 full + one 392s partial; BM-HEO 76 full + terminal partial; Mg-HEO 48 full + terminal partial; BM-Mg 56 full + terminal partial. **This is why Lith C1 1094.2/1278.5/814.25/948.17 differs from established full-pulse totals 1083.3/1266.7/800/933.3**. It is NOT an error requiring replacing the locked first-cycle regional analysis.

### Matched modification effect persists into later lithiation/delithiation

| Comparison | Δ lith C1 | Δ lith C2 | Δ lith C3 | Δ delith C1 | Δ delith C2 | Δ delith C3 |
|---|---:|---:|---:|---:|---:|---:|
| BM−HEO | +184.3 | +145.9 | +133.9 | +96.3 | +94.5 | +84.7 |
| BM-Mg−Mg | +133.9 | +101.5 | +86.8 | +67.5 | +68.3 | +65.0 |
| Mg−HEO | −280.0 | −238.9 | −247.7 | −246.6 | −251.1 | −264.4 |
| BM-Mg−BM | −330.3 | −283.3 | −294.8 | −275.4 | −277.4 | −284.1 |

The signed **BM positive / Mg negative** matched effect remains in all three lithiation and delithiation halfcycles. Therefore first-lithiation region-resolved effects are connected to persistent materials-performance differences, **not merely a first-cycle-only total-capacity artifact**. However, this does not prove a specific R2 or R3 charge amount itself carries over as an identical reaction/process in later cycles.

### Other core observations

- Lith C1→C2 nominal capacity falls ~33–42% (largest for Mg-containing). **Lith C2→C3** changes only ~0.6–4.8%, comparatively modest. Thus first lithiation produces a strong history-dependent change followed by a relatively repeatable response; avoid claim of proven phase-state stabilization or quantifiable kinetic irreversibility without mechanism evidence.
- Delith C1→C3 varies much less than Lith C1→C3: HEO 762.3→742.9, BM 858.5→827.6, Mg 515.7→478.5, BM-Mg 583.2→543.5 mAh/g. This is consistent with a large first-lithiation-only charge component, but its reaction identity remains undetermined.
- Some C2/C3 integrated delithiation totals slightly exceed same-cycle lithiation. **Do not calculate or advertise >100% Coulombic efficiency as a material benefit**: three-cycle sequential cutoff/history and source program/protocol need review. The table reports halfcycle-integrated delivered nominal charges, nothing more.
- 2nd→3rd lithiation t63 curves (vs matched within-halfcycle normalized nominal charge) are similar. Average absolute t63 difference across central 5–95%: HEO 23.7 s, BM 16.5 s, Mg 17.0 s, BM-Mg 18.0 s. For QOCV: HEO 6.1 mV, BM 10.0 mV, Mg 31.5 mV, BM-Mg 36.5 mV. Mg-containing electrodes show somewhat greater voltage-curve drift; **not statistical repeatability**, same single cell cycle history. Third delithiation vs second delithiation median t63 similarly close, with mean t63 curve errors 9.2/6.7/11.4/10.5 s (HEO/BM/Mg/BM-Mg).

## 2. Internal first-cycle R1–R4 landmark voltage-window cross-cycle check (NOT direct chemical region transfer)

The PI-approved R1–R4 were determined from **t63 changes on first lithiation only**. To test whether an associated voltage feature persists, define for each sample three **first-cycle QOCV threshold values** at the final after-pulse indices (L1,L3,L4), and partition subsequent cycle charge into the corresponding **fixed 60min-rest QOCV windows**. These are **matched voltage windows**, **not measured second- or third-cycle R1–R4 boundaries or phase assignments**. The latter would need independently picked t63 change points each cycle.

| Sample | L1/L3/L4 pulse | Initial 60min QOCV boundary values (V) |
|---|---|---|
| HEO | 6/25/55 | 0.8631 / 0.6473 / 0.4539 |
| BM-HEO | 9/38/60 | 1.1634 / 0.7145 / 0.4718 |
| Mg-HEO | 7/24/42 | 0.8921 / 0.5154 / 0.2951 |
| BM-Mg-HEO | 9/35/46 | 1.0106 / 0.5292 / 0.3192 |

Q at QOCV threshold obtained by piecewise-linear interpolation of each within-cycle monotone 60min QOCV versus cumulative nominal pulse charge. The initial full-pulse region Q values are derived from same cutoff indices; terminal partial pulse falls after last accepted boundary.

| Sample | Region-like **fixed potential** interval of first-cycle R3 (V) | C1 charge (mAh/g) | C2 matched-QOCV-window charge | C3 matched-QOCV-window charge |
|---|---|---:|---:|---:|
| HEO | 0.6473→0.4539 | 500.0 | 97.5 | 94.2 |
| BM-HEO | 0.7145→0.4718 | 366.7 | 130.9 | 131.4 |
| Mg-HEO | 0.5154→0.2951 | 300.0 | 74.6 | 71.1 |
| BM-Mg-HEO | 0.5292→0.3192 | 183.3 | 81.6 | 76.9 |

**Interpretation:** charge accumulated in the *first-cycle R3-associated rest-voltage interval* contracts strongly in second/third lithiation in all four materials. For pristine, the first 30 complete R3 pulses become only about 5 pulses in that same rest-voltage window in later cycles. It is legitimate to say the first-cycle potential–charge response is profoundly rearranged; **not** legitimate to say R3's chemically identical process disappears, nor that initial R3 charge was all irreversibly consumed. Fixed voltage ≠ fixed stoichiometric state, phase fraction or unique mechanism after conversion hysteresis and reaction-path evolution.

Other bins move in both directions under this mapping. Example pristine HEO:
- Window above 0.8631 V: C1 100.0, C2 354.0, C3 346.7.
- Window 0.8631→0.6473 V: C1 316.7, C2 131.1, C3 138.2.
- Window 0.6473→0.4539 V: C1 500.0, C2 97.5, C3 94.2.
- Window below 0.4539 V incl cutoff pulse: C1 177.6, C2 132.4, C3 131.3.
This is why **not** to call the calculation a direct irreversible-capacity partition by R1–R4.

### Pristine R3 relaxation-amplitude hump

- First-cycle pristine R3 starts near 145.1 mV (pulse 26), peaks near 189.3 mV (pulse 50), and ends 172.5 mV (pulse 55); median t63 trajectory shifts ~425→883 s.
- On second/third lithiation, the same 0.6473–0.4539 V QOCV window has about five pulses and ΔErest ~122→120 mV (C2), ~127→115 mV (C3), without the corresponding first-cycle interior hump. This is consistent with a changed relaxation signature after initial lithiation; caution that equal potential does not mean equal local reaction state.
- Main paper can avoid this complexity unless a concise graph clearly strengthens the story.

## 3. Mechanism hypothesis and low-bloat presentation decision (proposal pending PI)

**Two-level narrative:**
1. **Measured** first-cycle t63 assigns sample-specific R1–R4; ball milling largest positive R2 regional pulse charge; Mg incorporation largest negative R3.
2. **Independent validation with same-cell repeated GITT:** all four electrodes have a large first-to-second lithiation change, stable-ish 2nd/3rd, and preserve BM-positive/Mg-negative matched differences into **third-cycle delithiation**. This establishes **performance persistence of the intervention**, *not unique persistence of a given mechanistically assigned R2/R3 reaction*.
3. **Optional SI:** one panel with C1/C2/C3 QOCV or t63 traces for selected representative HEO and modified comparator(s) + the full 4×3 capacity table; fixed-voltage window reallocation and t63 normalization diagnostics recorded in this internal note, **not added to the manuscript automatically**.
4. **No new experiments** currently required. Prefer existing cell raw data + source program, use concise plot after scientific test.
5. **Possible concise main-text sentence for later author review:** “Repeated GITT measurements on the same cells show that the pronounced capacity changes between the first and second lithiation are followed by relatively similar second- and third-cycle responses, while the opposing effects of ball milling and Mg incorporation remain evident in subsequent delithiation.” This is a candidate sentence ONLY, not an approved manuscript replacement.

## 4. Caveats, next gates

- Confirm source/cell naming (the HEO 2022 `try 2_031` sequence matches first-cycle HEO raw), current density 100mA/g, active loading and whether original cell labels exactly align across figure source versions.
- Ensure 1st-lithiation accepted Figure5 uses **full pulses only** while this cycle comparison includes **terminal partial pulse**. Do not replace the 2026-11-11 locked region values by these first-cycle totals.
- For cross-cycle comparing relaxation/chemical processes, choose matched state carefully: normalized Q, rest-voltage, integrated charge or delith charge can give different comparisons. Avoid assuming voltage alone identifies structure after conversion.
- Same-cell 3 cycles is temporal sequence, not replicate number; no replicate error bars from it.
- Possible further *internal* analysis: find t63 changepoints on cycle2/3 **independently**, check whether t63 partition recurs after the first lithiation, compare delithiation characteristic times; avoid forcing original R1–R4 landmark indices or voltages across future cycles.
- Determine whether cycling rate/FEC protocols match Figure3; these GITT data provide within-cell evidence but do not replace Figure3's independent cycling source.
