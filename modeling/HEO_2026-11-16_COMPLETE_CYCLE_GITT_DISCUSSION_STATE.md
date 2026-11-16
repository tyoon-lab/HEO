# HEO — cumulative C1–C3 GITT research discussion and handoff (2026-11-16)

> **START HERE for the current GITT / hump / R1–R4 discussion.**
> This note records the PI's exploratory analysis and all major decisions through the discussion of FEM simulation (2026-11-14). It does **not** amend the accepted manuscript, Abstract, Introduction, first-lithiation R1–R4 definitions, SI, original Excel measurements, figure numbers or native Word comments. The FEM simulation question remains a **proposal**, not completed work. The user explicitly instructed: **update GitHub ONLY when requested** (a fresh explicit GitHub save request was made on 2026-11-16).

## 0. Source authority and guardrails

- First read the [main START_HERE](../START_HERE_CURRENT_STATE_2026-10-12.md) and [PI-locked Abstract/Introduction](../manuscript/HEO_2026-11-11_PI_LOCKED_ABSTRACT_INTRODUCTION_AND_DECISION_LOG.md). The [November 10 science authority](../manuscript/HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md) remains authoritative for figure science, text claim limits, characterization and manuscript status. The older author/review DOCX must not be silently overwritten.
- Four conditions: pristine HEO, BM-HEO, Mg-HEO and BM-Mg-HEO; **matched 2×2 ball milling / Mg incorporation**. Same cell examined using GITT across **three complete lithiation/delithiation cycles** in the four original raw XLSX reports. A direct sign reversal at a cutoff is not a rest; handle duplicated workbook-sheet edge rows and actual current signs. The corrected audit demonstrates that C3 delithiation is present for all four materials (earlier sparse C3 plots were parser artifacts).
- GITT current-pulse charge approximately **16.67 mAh g⁻¹ per complete 600s pulse**; nominal rest up to 3600s; authors' reported \`t63\` is an operational characteristic voltage-recovery time, and \`ΔErest\` is the measured finite-window relaxation amplitude. **Partially completed terminal cutoff pulses may be included in a cycle-total audit but not in the first-lithiation locked *full-pulse* region counts**; quote the denominator explicitly. C2/C3 are sequential cycles of the *same cell*, not independent replicates.
- **User's standing scientific instructions**: first-lithiation t63-defined regions remain **R1–R4**; do not force these boundaries onto later lithiation or delithiation. The hump of \`|ΔErest|\` is an **observable comparison fiducial/anchor, not a charge maximum, unique reaction fingerprint, or proven phase boundary**. A *possibly shared predominant process* may change its amplitude, charge contribution, QOCV and relaxation spectrum between samples/cycles. Explicitly separate measured quantities, phenomenological assignments and proposed chemical pathways.
- **No automatic GitHub updates**, Word creation/editing, manuscript text changes or manuscript claim promotion without explicit PI request.

## 1. Locked first-lithiation regional analysis (unchanged)

First-cycle C1 lithiation regional charges (mAh/g, **complete pulses**):

| Material | R1 | R2 | R3 | R4 | C1 total |
|---|---:|---:|---:|---:|---:|
| HEO | 100.0 | 316.7 | 500.0 | 166.7 | 1083.3 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 |
| Mg-HEO | 116.7 | 283.3 | 300.0 | 100.0 | 800.0 |
| BM-Mg-HEO | 150.0 | 433.3 | 183.3 | 166.7 | 933.3 |

Boundaries by complete-pulse index (R1/R2, R2/R3, R3/R4): HEO **6/25/55**; BM-HEO **9/38/60**; Mg-HEO **7/24/42**; BM-Mg-HEO **9/35/46**. Boundaries expressed in Q = pulse × 16.67 mAh/g. The largest **ball-milling gain** is in **R2** (+166.7 mg-free; +150 with Mg) and largest **Mg incorporation loss** in **R3** (−200 without BM; −183.3 with BM). These regional charges and signs are valid as *operational t63-derived* contrasts, not reaction-specific charge proved by spectroscopy.

**New caution from full E(t) audit:** at R2→R3, t63 has a minimum or turning/slope-change behavior, not a step-discontinuity. Normalized adjacent complete-relaxation curves show relatively **small** shape change at the boundary: approximately bottom **9%, 23%, 9%, 7%** in each electrode's adjacent-step distribution (HEO/BM/Mg/BM-Mg). Thus first-cycle t63 regions are a reproducible electrochemical **partition of a continuous response**, not naturally discrete phases. Neither this nor an overlapping dominant reaction disproves the pragmatic R1–R4 segmentation. The mechanistic annotation of each interval remains *inferred from prior spinel/conversion oxide literature*, not uniquely inverted from E(t).

## 2. Why compare later cycles; first-vs-later changes

First C1 lithiation has multiple humps and nonmonotonic t63; C2/C3 lithiation becomes more nearly monotonic and the first-cycle complex t63 profile largely vanishes. **The |ΔErest| hump persists** in C2/C3, despite the loss of t63's first-cycle hump. C2/C3 lithiation QOCV, dQ/dV and normalized entire-rest E(t) are much more similar to each other than to C1.

Working mechanism proposed by PI: the first lithiation begins at *pristine spinel*, involves Li insertion, cation migration, oxide reconstruction and conversion-product creation; the first delithiation need not restore the original spinel, so C2/C3 begin from *reconstructed oxide/residual products*. This could remove first-cycle-only initial contributions while some shared predominant conversion response remains. **This is a plausible mechanistic hypothesis, not directly proved chemical identity.** Do not state that initial additional charge is completely localized in R1+R2 or follows uniquely from one reaction.

Complete-pulse first-cycle vs later-charge balance:

| Sample | C1 lith Q | mean C2/C3 lith Q | **extra C1 lith** | C1 delith Q | **C1 lith−C1 delith** |
|---|---:|---:|---:|---:|---:|
| HEO | 1083.3 | 700.0 | **383.3** | 750.0 | **333.3** |
| BM-HEO | 1266.7 | 841.7 | **425.0** | 850.0 | **416.7** |
| Mg-HEO | 800.0 | 458.3 | **341.7** | 500.0 | **300.0** |
| BM-Mg-HEO | 933.3 | 550.0 | **383.3** | 566.7 | **366.7** |

All units mAh/g. The first lithiation's additional capacity is similar in magnitude to the apparent C1 irreversibility, but not equal; **SEI, conversion, structural transformation, partially reversible paths and changed cutoff/QOCV histories overlap**.

## 3. Hump as a comparative anchor — PI-approved *research strategy*, not paper mechanism

PI proposed: treat the visually prominent \`|ΔErest|\` hump as a **same-predominant-process candidate**, while allowing its contribution, potential and kinetics to vary. Place each C1/C2/C3 hump at relative charge zero and compare **both sides**. Later-cycle humps often occur near **half of total C2/C3 lithiation Q**; this alone does **not** imply maximum capacity occurs at hump.

Selected anchors (full-rest pulse Q in mAh/g):
- **HEO** C1 816.7 (clear peak) / C2 366.7 / C3 350.0. C1 peak ~75% of first lithiation capacity, inside C1 R3.
- **BM-HEO** C1 ~750 (**broad shoulder/tentative**) / C2 400 / C3 400; C1 ~59%.
- **Mg-HEO** C1 633.3 (clear) / C2 233.3 / C3 233.3; C1 ~79%, inside C1 R3.
- **BM-Mg-HEO** C1 ~600 (**sloping shoulder/tentative**) / C2 ~250 weak shoulder / C3 266.7; C1 ~64%.

C1 minus C2/C3-mean charge split **before** vs **after** selected marker (mAh/g):

| Material | C1 extra before hump | C1 difference after hump | Total C1 extra |
|---|---:|---:|---:|
| HEO | **+458.3** | **−75.0** | +383.3 |
| BM-HEO (tentative marker) | ~+350.0 | ~+75.0 | +425.0 |
| Mg-HEO | **+400.0** | **−58.3** | +341.7 |
| BM-Mg-HEO (tentative) | ~+341.7 | ~+41.7 | +383.3 |

The first cycle has large additional **pre-hump** charge, while the post-hump contribution itself changes. **Do not equate C1 pre-hump extra charge with R1+R2 or with one irreversible reaction.** Especially in BM electrodes, R1+R2 (633.3/583.3) exceeds selected first-extra-pre-hump charge (~350/~342) by 240–280 mAh/g, and the tentative shoulder moves the split.

Earlier hypothesis \`Q_aligned,C1 = Q_C1 − ΔQ\` with one ΔQ=200–450 mAh/g improved some curve registrations, but **did not align absolute t63, |ΔErest| and QOCV simultaneously**. Joint optimum shift HEO ~200 (search lower bound), BM ~325, Mg ~285, BM-Mg ~325 mAh/g; property-specific optima disagree. This is evidence against the strongest 'simply remove an initial block, everything else is an identical trajectory' model. **It does not contradict recurring contribution of a predominant process.**

## 4. Independent later-cycle landmarks and broad QOCV commonality

For C2/C3, a local QOCV-derived \`|dQ/dV|\` maximum consistently occurs about **17–67 mAh/g *before* the |ΔErest| hump**; hump is not the derivative-charge maximum. The corresponding local peak QOCV across eight sample-cycle traces is ~**0.880–0.913 V**. Local peak positions change by at most one full pulse between C2/C3. Thus the **~0.90 V charge-response feature → later relaxation-amplitude hump** may define a *broad repeated response interval*, not a sharp phase boundary. Independent descriptions are based on **the same GITT voltage/charge source**, so avoid overstating evidential independence.

Broad 0.5–1.3 V QOCV-matched normalized raw-rest comparison found **minimum between-material normalized full-curve differences at ~0.9–1.0 V**; between-material mean RMSE ~0.0075–0.0079 and t63 between-material SD ~11–13s, versus larger deviations at 0.5–0.7 and 1.2–1.3 V. Within each electrode C2/C3 raw-rest shapes are highly alike **across the full 0.5–1.3 V range**: later-cycle similarity is general, not exclusive to a single 'hump reaction'. Cross-material resemblance could reflect common generic finite-window relaxation kernel/transport and does not prove a unique phase.

QOCV 0.85–0.95 V fixed-window C2/C3 mean charge (mAh/g): **HEO 79.36, BM 97.39, Mg 46.27, BM-Mg 57.76**. Window as % of total: **11.34, 11.57, 10.10, 10.51%** respectively. Ball milling's absolute increase is largely explained by scaling total Q. Mg effect retains a modest **~1.0–1.2 percentage point *relative* depletion**, amounting to ~−5.7 to −5.9 mAh/g beyond simple total-capacity scaling in this window. This difference is *smaller than one nominal full GITT pulse*; interpolation/single-cell uncertainty prevents assigning exact reaction capacity.

Amplitude-shape control: compare \`A_mod(V)−k*A_ref(V)\`, with a **single** k globally fitted across 0.5–1.3 V. At 0.90 V Mg minus HEO residual is ~**−13.0 mV** and BM-Mg minus BM ~**−11.6 mV**. Signs repeat for C2/C3, 600/1800/3500s rest endpoints, and 3/10s start references. The general 0.9–1.0 V normalized relaxation times can converge even while Mg changes **amplitude-versus-potential** and local fraction of charge. No unique mechanism follows directly. Local QOCV slope |dV/dQ| rises ~1.7-fold with Mg at 0.90V but this alone cannot account for measured A(V). Derived \`A/(|dV/dQ| Qtotal)\` is a diagnostic **not a measured migrated charge** or independent chemical evidence.

**Key null model:** hump-based apparent '70–73% of ball milling's later-cycle advantage occurs post-hump' is substantially **capacity-scaling and anchor-choice sensitive**. A null model where modification proportionally scales all later charge *cannot clearly be rejected* within ±one-pulse anchor sensitivity. Do not claim R2→post-hump or R3→post-hump causal quantitative transfer. The tendency of BM-positive/Mg-negative later capacity is robust; its specific chemistry is not.

## 5. Actual full-rest E(t) and multiple relaxation time components

At hump±3 complete pulses, normalized **fraction of voltage recovery by 300s** shifts from C1 to C2/C3:
- HEO 41.6% → ~50.2%;
- BM 44.1% → ~48.6%;
- Mg 44.5% → ~49.7%;
- BM-Mg 43.8% → ~49.0%.
Normalized recovery after ~1200s decreases concurrently. Thus the **time-dependent voltage-recovery shape** changes, not merely its amplitude or calculated t63. C2/C3 normalized E(t) agree very closely; the difference from C1 is preserved if the hump anchor is shifted ±3 pulses.

NNLS-style smooth nonnegative exponential mixture over 3–3600s can reproduce curves more closely than 1–2 exponentials (single exp RMSE ~0.068–0.090, two exponentials ~0.010–0.013, flexible kernel ~0.0002–0.001 on normalized curves). **Do not interpret flexibly fitted individual τ peaks or weights as proven independent physical mechanisms**, especially for τ longer than rest window; lower RMSE of a higher-capacity inverse model is not independent physical validation.

Relative model-assigned slow τ≥1000s weight tends to decrease after first lithiation (~43→35% HEO, ~41→36 BM, ~42→36 Mg/BM-Mg). This direction survives regularization sensitivity, but exact weights shift with assumed kernel and bounds. The directly observed time-band recovery ratios are the firmer result.

At C1 R2→R3, complete E(t) shapes vary **smoothly**. The change in t63 slope or minimum identifies an operational domain but not a sharp switch to a distinct chemical process. The **|ΔErest| hump remains in C2/C3 even when t63's C1 hump vanishes**, consistent with amplitude and time composition changing separately. PI wanted hump treated as anchor, not necessarily new segmentation.

## 6. First delithiation: the additional key comparison

C1 delithiation capacity is only ~**16.7 mAh/g higher than C2 delithiation** for each electrode using full-pulse nominal Q; by comparison C1 lithiation has hundreds of extra mAh/g. The **normalized QOCV(Q) and |ΔErest|(capacity fraction)** profiles for C1 delithiation are **already broadly similar to C2/C3** despite offsets.

At matched normalized delithiation progress, **C1 QOCV is typically lower** than later delithiation by roughly **92, 60, 119, 87 mV** for HEO, BM, Mg, BM-Mg respectively. Adding a constant electrode-specific voltage shift to C1 brings the *QOCV-vs-capacity shape* closer (residual RMSE ~19, 8, 28, 15 mV), but does **NOT** bring the independent kinetic descriptors into coincidence: applying this same potential shift to \`|ΔErest|(V)\` makes RMSE *worse* (HEO 8.5→11.7 mV, BM 4.1→10.9, Mg 5.7→16.9, BM-Mg 4.2→15.0). t63 also does not consistently improve.

Matched QOCV 0.3–1.7 V: C1 delithiation \`t63\` C1-vs-(C2/C3)-mean RMSE ~**45.3, 17.9, 51.3, 35.4s** (HEO/BM/Mg/BM-Mg), whereas within-cell C2-vs-C3 RMSE ~**10.9, 7.4, 21.4, 24.7s**. First delithiation therefore resembles later *pattern* but is dynamically nonidentical; electrochemical conditioning continues. Both same QOCV and normalized-capacity comparisons must be kept because potentials and stoichiometries differ.

In a common 0.3–1.7V delithiation range, C1 has ~**+81, +60, +61, +54 mAh/g** more Q than C2/C3 (HEO/BM/Mg/BM-Mg) even though whole-delith Q differs by only ~17–25 mAh/g. Hence **voltage redistribution**, not evidence that one particular first-lithiation packet is or is not recovered at a specific later potential. Avoid one-to-one charge tagging across path-dependent lithiation/delithiation.

**Scientific working interpretation**: first lithiation forms new reaction history/product structure; first delithiation already uses a roughly recurring path; C2/C3 converge further. Neither the charge balance nor raw E(t) proves exact reversible phases, SEI size, or correspondence of C1 R1–R4 to delithiation regions.

## 7. Matched modification persistence and what remains unresolved

From full-pulse totals, modified minus matched reference first vs mean C2/C3 lithiation effects (mAh/g):

| Matched change | C1 total ΔQ | C2/C3 total ΔQ | Difference in effect sizes |
|---|---:|---:|---:|
| BM-HEO − HEO | +183.3 | +141.7 | +41.7 |
| BM-Mg − Mg | +133.3 | +91.7 | +41.7 |
| Mg − HEO | −283.3 | −241.7 | −41.7 |
| BM-Mg − BM | −333.3 | −291.7 | −41.7 |

This shows that **net modification effects largely persist in later lithiation**, while the larger C1 additional charge is not a one-to-one marker of first R1+R2. The repeated ±41.7 mAh/g arithmetic difference is only ~2.5 complete pulses, and not a demonstrated conserved physical quantity.

- PI's core value proposition remains: **rather than only total GCD/GITT capacity, compare which *electrochemically defined C1 intervals* gain/lose charge under different interventions**, with literature-inferred chemical contributions.
- More ambitious follow-up: map first-cycle region effects into *later response persistence* without implying unique electron/phase bookkeeping.
- Hump anchor as a candidate recurring dominant-process observational index is promising especially for HEO and Mg-HEO; BM first-cycle shoulders are subjective, and later post-hump effects may be simple total-Q scaling.
- **Current evidence does not prove that t63-defined R1–R4 are chemical phase boundaries or that hump should replace them.** Do not rewrite first-cycle main narrative from this preliminary analysis without PI approval.

## 8. Chronological decisions (PI intent)

1. Review manuscript §2.1–2.2 and Figure3 with source-grounded corrections, no new Word unless requested; PI preferred two body paragraphs, removal of absolute 'featureless plateau', verification of 100-cycle and rate return source, and careful XPS Mg/site/oxygen interpretations. Earlier GitHub manuscript/figure audit governs these edits.
2. Realized GITT measured three cycles in **the same cells**; compare **first lithiation, first delithiation, second lithiation, second delithiation, third lithiation, third delithiation** for all four materials.
3. Plot full pulsewise t63, |ΔErest|, QOCV and QOCV-derived dQ/dV, initially normalized progress, then **absolute Q** 2×2 0–900 mAh/g for visual discrimination. Corrected false missing C3 halfcycles caused by source XLSX parsing.
4. PI noted **|ΔErest| hump persists C2/C3 while t63 becomes monotone**; hypothesized first pristine-spinel-specific process then recurring conversion. Do not equate monotone t63 with a one-phase/one-process reaction.
5. Tried capacity-axis horizontal-shift ΔQ test; absolute triple-observable matching fails -> retain *dominant-process, different contributions/time scales* hypothesis instead of imposing identical curve.
6. Aligned to **|ΔErest| hump**, later combined QOCV ~0.90 V local dQ/dV feature, broad potential and normalized raw E(t) shape. User emphasized hump is a **visible fiducial**, not a capacity maximum.
7. Challenged special-region claims by total-capacity scaling, one-pulse anchor sensitivity, rest-window sensitivity, common QOCV slope and general 0.5–1.3 V curve similarity. Net BM/Mg capacities remain changed; Mg shows some local amplitude/charge-fraction evidence, but single-reaction causality remains unproven.
8. Examined full C1 R1–R4 normalized E(t) across boundaries; no abrupt phase change. Keep C1 operational regions, caution against unique chemistry labeling.
9. Reconciled first C1 extra capacity vs R1+R2, C1 irreversible charge and C1 first-delithiation QOCV/t63/|ΔErest|. Initial reaction-history interpretation remains plausible, first delithiation resembling later response from earliest cycle.
10. **Most recent scientific question from PI (2026-11-14): 'Would adding simulation, e.g. FEM, improve the work?'** No FEM was run or approved. Simulation options and discriminating hypotheses are an *open planning decision*, linked in [simulation decision note](HEO_2026-11-16_SIMULATION_FEM_MODEL_SELECTION_GATE.md).

## 9. Reproducing, source files, known local outputs

Original raw files (conversation-attachment aliases; **not committed via this note**, may need re-upload/recovery in a new container):
- \`HEO GITT 로우 데이터.xlsx\`
- \`BM HEO 3 GITT 로우 데이터.xlsx\`
- \`HEO 3 Mg 로우 데이터.xlsx\`
- \`BM HEO 3 Mg 로우 데이터.xlsx\`

Important intermediate audit (existing local working-session file, not a GitHub-hosted dataset): \`HEO_GITT_C1_C3_joined_lith_delith_throughput.csv\` (pulsewise sample, signed halfcycle, cycle, Q, t63, QOCV, ΔErest).

Latest full-rest C1 region files:
- \`HEO_C1_R1_R4_boundary_continuity.csv\`
- \`HEO_C1_all_R1_R4_rest_shape_metrics.csv\`
- \`HEO_C1_region_boundary_full_relaxation_audit.py\`
- Figures: \`HEO_C1_R1_R4_t63_2x2.png\`, \`HEO_C1_R1_R4_F_shape_steps_2x2.png\`.

Capacity accounting and first/later comparison:
- \`HEO_C1_region_vs_hump_early_excess_balance.csv\`
- \`HEO_C1_Rregion_vs_later_matched_pair_contrasts.csv\`
- \`HEO_C1_region_charge_boundary_shift_identities.csv\`
- \`HEO_first_delithiation_cycle_metrics.csv\`
- \`HEO_first_delithiation_voltage_bin_charge.csv\`
- \`HEO_delith_C1C3_relaxation_metric_comparisons.csv\`
- \`HEO_delith_independent_QOCV_shift_kinetics_control.csv\`
- \`HEO_hump_direct_time_band_recovery.csv\`, \`HEO_hump_exponential_mixture_sensitivity.csv\`, \`HEO_hump_single_vs_two_exponential_test.csv\`
- Scripts: \`HEO_C1_Rregions_to_later_hump_charge_audit.py\`, \`HEO_first_delithiation_cycle_comparison.py\`, \`HEO_delith_C1C3_relaxation_compare.py\`, \`HEO_hump_relaxation_spectrum_internal.py\`.
- Key plot series: \`HEO_C1_Rregions_vs_later_hump_aligned_charge_2x2.png\`, \`HEO_C1_early_charge_mass_balance_two_tests.png\`, \`HEO_C1_Rregion_vs_C2C3_hump_voltage_effects.png\`, \`HEO_C1_vs_C2C3_net_modification_charge_balance.png\`, \`HEO_delith_C1C3_t63_vs_QOCV_2x2.png\`, \`HEO_delith_C1C3_dErest_vs_QOCV_2x2.png\`, \`HEO_delith_C1_QOCV_offset_registration_2x2.png\`.

**These names are an audit manifest, not verified GitHub links.** The science tables and reasoning are preserved in GitHub Markdown, while numerous PNG/CSV/Python artifacts generated in conversation containers are **not automatically present in GitHub**. Reproduce from original source workbooks where available; uploaded assets from earlier conversations may expire.

## 10. Existing detailed GitHub internal reports and manuscript authority

- [Cycle-1→later horizontal shift test](HEO_2026-11-13_C1_TO_C2_C3_LITHIATION_HORIZONTAL_SHIFT_TEST.md)
- [Hump-aligned charge decomposition and independent dQ/dV marker](HEO_2026-11-13_HUMP_ANCHORED_CYCLE_COMPARISON_INTERNAL.md)
- [QOCV=0.90 V actual E(t), C1–C3](HEO_2026-11-13_COMMON_QOCV_REST_RELAXATION_CONTROL.md)
- [Broad 0.5–1.3 V QOCV and E(t) control](HEO_2026-11-13_BROAD_QOCV_REST_SHAPE_CONTROL.md)
- [Whole-capacity and rest-amplitude gain controls; Mg sensitivity](HEO_2026-11-13_LOCAL_QOCV_MODIFICATION_SELECTIVITY_CONTROL.md)
- [Earlier same-cell source audit](HEO_SAME_CELL_GITT_THREE_CYCLES_PRELIMINARY_AUDIT_2026-11-11.md)
- [Authoritative manuscript science, separate from exploratory results](../manuscript/HEO_2026-11-10_AUTHORITATIVE_SCIENCE_MANUSCRIPT_STATE.md)

## 11. Immediate next-work decision

**Do not automatically generate a manuscript update or start heavy FEM.** First agree a minimal model-based falsification test for the first-cycle-specific vs recurring-path hypothesis; see [simulation decision gate](HEO_2026-11-16_SIMULATION_FEM_MODEL_SELECTION_GATE.md). The most discriminating observable targets are the **disappearance of C1-specific t63 complexity**, **survival of |ΔErest| hump**, and **already similar first delithiation profiles**, under shared physically consistent parameters. If no additional explanatory/predictive value beyond a simple model and known observations, exclude FEM from main paper. GitHub should be edited again **only after PI explicitly requests**.

