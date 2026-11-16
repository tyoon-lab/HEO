# HEO — 2026-11-16 authoritative CONTINUITY of the Nov 11–14 same-cell GITT discussion

**Status: research working record / internal mechanistic hypotheses, NOT a PI-approved manuscript rewrite.**
This page extends the already-committed Nov 11 and Nov 13 internal raw-source analyses and explicitly records subsequent conversation results. Read alongside the PI-locked Nov 11 Abstract/Introduction and authoritative original R1–R4 data. **The four first-lithiation t63 region definitions remain fixed.** Neither the MS, SI, Word comments nor figure numbering was changed by these explorations. No GitHub changes should be made again without an explicit PI request.

## 0. Immediate scientific objective and the PI's decision

The PI's motivating question: **When ball milling raises first-lithiation charge most in R2 and Mg incorporation lowers charge most in R3, how do those region-specific differences influence later delithiation and lithiation?** The goal is a transferable way of analyzing modified conversion-type HEOs, rather than another report of total capacity change.

The PI explicitly decided to **retain the existing first-lithiation R1–R4 manuscript and Abstract/Introduction**, while testing a more daring **hump-anchor hypothesis** internally. The voltage-rest-amplitude `|ΔErest|` hump is an **observable fiduciary mark** to align first and subsequent lithiation; it is **not** claimed to be the location of maximum capacity, a phase boundary, a reaction-rate maximum, or a uniquely identified chemical reaction. If the same *dominant* chemical process contributes near the landmark, its magnitude, timescale, capacity, phase state and potential may all change by sample and cycle. Scientific uncertainties must not prevent useful falsifiable hypotheses, but hypotheses and observations must remain explicitly differentiated.

## 1. Files, sample and protocol provenance / prevent recurring past mistakes

Four paired materials: `HEO`, `BM-HEO`, `Mg-HEO`, `BM-Mg-HEO`. Raw XLSX source file names previously used in analyses: `HEO GITT 로우 데이터.xlsx`; `BM HEO 3 GITT 로우 데이터.xlsx`; `HEO 3 Mg 로우 데이터.xlsx`; `BM HEO 3 Mg 로우 데이터.xlsx`. Three full lithiation/delithiation cycles from the same cell for each material; some files include the start of cycle 4. Nominal negative-current lithiation (often called first 'charge' in source protocol); positive-current delithiation (called 'discharge' in this discussion). Correct experiment: **600 s current pulse, 3600 s rest** (older slide had mistaken 60 s pulse). The nominal complete-pulse charge in current analysis is `100 mA g^-1 * 600 s = 16.667 mAh g^-1`; verify actual mass/current and test metadata before treating as absolute source-calibrated capacity.

**Correctly parse XLSX split sheets**: don't double-count duplicated edge record; direct sign reversal at cutoff is NOT a rest. An earlier extractor accidentally assigned extra cycle IDs at sign reversal/split boundaries, making HEO C3 delithiation and BM-HEO C3 segments look incomplete; this was a code error, not missing cycling. Corrected extraction identified all 6 half-cycles in all 4 material files. The latest raw reports in the preceding conversation may be unavailable to a brand-new workspace: GitHub Markdown is sufficient to discuss documented conclusions, but re-running computation requires actual raw XLSX/CSV from an accessible source. Do not invent binary `/mnt/data` paths or claim that locally generated figures/scripts were committed.

**Charge accounting caveat:** analyses of full-rest full 600s pulses omit terminal partial cutoff pulse, while separate whole-halfcycle/cycle audit may include terminal partial pulse. Do NOT intermix these totals or describe a GITT pulse sum as first-0.1C GCD capacity. Full-rest GITT results can differ by one pulse (~16.7 mAh/g). Each condition is one experimental cell across consecutive C1/C2/C3; later cycles are repeated *histories*, not independent cell replicates.

## 2. First-lithiation accepted first-cycle R1–R4 segmentation (DO NOT replace)

Fixed t63 after-pulse boundaries (pulses and nominal capacity): HEO **6/25/55** (~100/416.7/916.7); BM-HEO **9/38/60** (~150/633.3/1000); Mg-HEO **7/24/42** (~116.7/400/700); BM-Mg-HEO **9/35/46** (~150/583.3/766.7). End at first GITT cutoff.

Nominal full-pulse C1 regional charges (mAh/g):

| sample | R1 | R2 | R3 | R4 | total full pulses |
|---|---:|---:|---:|---:|---:|
| HEO | 100.0 | 316.7 | 500.0 | 166.7 | 1083.3 |
| BM-HEO | 150.0 | 483.3 | 366.7 | 266.7 | 1266.7 |
| Mg-HEO | 116.7 | 283.3 | 300.0 | 100.0 | 800.0 |
| BM-Mg-HEO | 150.0 | 433.3 | 183.3 | 166.7 | 933.3 |

Principal **first-cycle comparisons**: BM on Mg-free R2 **+166.7**, R3 **−133.3**; BM with Mg R2 **+150**, R3 **−116.7**; Mg vs HEO R3 **−200**; Mg after BM R3 **−183.3**. Region charges and signed perturbations are direct operational GITT results; named reactions are *literature-based inferences*. R1 insertion/structural evolution; R2 oxide reconstruction/early transition metal reduction; R3 later intermediate-oxide reduction and metal/Li2O development; R4 deeper low-voltage residual reactions/possible interfacial contribution. No claim of unique reactions in separate nonoverlapping phases.

Original author paragraph decisions still valid: Article's main novelty is **quantifying where morphology/composition changes cause gains/losses across kinetically defined first-lithiation regions**; the new multi-cycle analysis is currently internal until PI explicitly decides what earns manuscript space.

## 3. Three-cycle four-descriptor visual comparison

Earlier analyses plotted 4 materials each with C1/C2/C3 lithiation and delithiation, initially versus normalized halfcycle progress (0–100%) and then with common **absolute capacity (0–900 mAh/g)** and finally joined lithiation→delithiation throughput. Descriptors: `t63`, `|ΔErest|`, rest-end `QOCV`, `QOCV-derived dQ/dV`. Plot sample 2×2 where useful.

**Observed:** C1 lithiation t63 exhibits complex, nonmonotonic hump/minimum/renewed increase; C2/C3 lithiation t63 is generally simpler/monotone, with C2/C3 largely coincident. The early C1 vs later differences are much greater than late differences, motivating initial-spinel-specific processes. But **|ΔErest| hump remains in C2/C3** — important correction to early inaccurate assistant wording. Its persistence, despite loss of the t63 hump, is central to the PI's hypothesis. Delithiation C1/C2/C3 curves are considerably more similar, already from C1, although amplitude and voltage offsets remain.

**Interpretation:** C1 starts from original spinel and may traverse Li insertion, cation migration, spinel reconstruction and conversion. C2/C3 start from reoxidized/reconstructed oxide and residual products after first delithiation and may share a repeatedly accessible, partly related conversion sequence. The first reaction history can alter *relative relaxation components* even if a characteristic voltage-rest-amplitude feature reappears. “Monotone t63” does NOT imply single-phase or monoexponential chemistry.

## 4. Hump anchors, alignment result, uncertainties

| material | first lithiation nominal peak/shoulder Q (mAh/g) | C2 | C3 | C1 fraction | later typical fraction |
|---|---:|---:|---:|---:|---:|
| HEO | 816.7, **clear local hump** | 366.7 | 350.0 | 75.4% | ~50–52% |
| BM-HEO | ~750, **weak/subjective shoulder** | 400 | 400 | ~59% | ~47–48% |
| Mg-HEO | 633.3, **clear hump** | 233.3 | 233.3 | 79.2% | ~50–52% |
| BM-Mg-HEO | ~600, **sloping/subjective shoulder** | ~250 | 266.7 | ~64% | ~44–50% |

`Q_rel=Q_pulse−Q_hump` makes the observational landmark x=0. The PI explicitly rejects assuming that hump implies concentrated charge, but uses it as a **repeatable observational anchor** and allows cycle/sample changes in contribution of the dominant reaction. BM-C1 and BM-Mg-C2 anchors must retain uncertainty; moving shoulder ±1 pulse or 50–100 mAh/g changes pre/post split.

First-cycle C1 vs C2/C3 mean *extra* GITT charge by selected hump:

| material | C1 extra **before** hump | C1 extra **after** hump | total C1 extra |
|---|---:|---:|---:|
| HEO | +458.3 | −75.0 | +383.3 |
| BM-HEO (tentative shoulder) | ~+350.0 | ~+75.0 | +425.0 |
| Mg-HEO | +400.0 | −58.3 | +341.7 |
| BM-Mg-HEO (tentative shoulder) | ~+341.7 | ~+41.7 | +383.3 |

C1 extra throughput is similar *in scale* to C1 irreversible charge but not a unique irreversible chemical component; some parts of late charge change too. **Do not call all C1 extra 300–400 mAh/g "R1+R2" or a uniquely identified nonreversible oxide transformation.**

### Strong horizontal-shift falsification test

Subtract `ΔQ`=200–450 mAh/g from C1 Q and attempt common curve registration of **all three properties** (t63, |ΔErest|, QOCV) against mean C2/C3, fixed overlapping Q-range. Best joint shift: HEO 200 (lower boundary; expanded search best 185), BM-HEO 325, Mg-HEO 285, BM-Mg-HEO 325 mAh/g. Individual observable optimum shifts are inconsistent and substantial residuals remain; **a rigid horizontal capacity offset cannot turn the entire C1 profile into the C2/C3 profile**. This does not invalidate PI's weaker “shared dominant process with changed weights/voltage” hypothesis.

### Hump vs independent charge-response landmark

C2/C3 local QOCV-derived differential-charge peak (after 5/7/9-pulse smoothing) consistently occurs **1–4 pulses before** |ΔErest| hump (~17–67 mAh/g earlier), with QOCV peak potential near **~0.88–0.913 V** across all 4 electrodes/2 cycles; hump QOCVs differ more strongly by material (~0.76–0.87 V in later cycles). Do NOT claim hump is peak stored charge or equivalent to dQ/dV maximum. Concept: broad **dual-landmark response window** between a common ~0.90V differential-charge feature and later relaxation-amplitude hump, *not* a hard reaction boundary.

## 5. C2/C3 common ~0.9–1.0 V response and modification contrasts

Same-QOCV raw GITT rest curves 0.5–1.3V, all 4 materials, two cycles. At 0.90V, later t63 clusters about 542–586s; F(t) normalized time dependence among materials converges most in broad **0.9–1.0V**, but **C2 vs C3 shapes are similar throughout 0.5–1.3V**, not unique proof of a single mechanism. C1 t63 at the same QOCV: HEO ~630s, BM ~687s, Mg ~746s, BM-Mg ~796s; same potential is not same state of lithiation across cycles. C1 has larger absolute amplitude (~1.8–2.3× C2/C3) and different normalized shape. These are distinct experimental observations.

Later mean total-capacity-normalized charge for 0.85–0.95 V: HEO **11.34%** (79.36 mAh/g), BM **11.57%** (97.39), Mg **10.10%** (46.27), BM-Mg **10.51%** (57.76). Ball milling changes local percentage by only +0.24/+0.41 percentage points; Mg reduces by −1.24/−1.06 percentage points in the two matched comparisons. Mg local excess beyond whole-capacity scaling is only ~−5.7/−5.9 mAh/g (< one 16.7 mAh/g GITT pulse) despite directionally repeating C2/C3. Do NOT equate with a directly resolved chemical phase charge.

Raw 3–3500s rest amplitude after a **global uniform-amplitude gain fit** vs QOCV=0.5–1.3V shows Mg-specific local negative residual at 0.90V: Mg−HEO **−13.0mV** and BM-Mg−BM **−11.6mV**; 1.00V ~−11.3 and −7.5mV. At 0.90V for C2/C3 separately residuals ~−12/−14 and ~−11.6/−11.6mV. This persists for alternative rest endpoints **600, 1800, 3500s**, and 3s vs 10s initial reference. It is stronger as a **reproducible empirical voltage-amplitude difference** than as a unique reaction assignment. QOCV local slope ~1.7× steeper with Mg at 0.90V while A does not proportionally increase; derived slope-normalized descriptor differs, but all derive from same GITT and do not independently measure a migrated charge fraction.

**Null model:** when later-cycles hump lies roughly at half of total Q, an increase in total capacity alone predicts increase in post-hump charge. After removing uniform total-capacity scaling, nominal BM excess after hump +31/+22 mAh/g lies within a ±one-pulse anchor-choice sensitivity envelope (~±37). Thus **do not promote apparent 71–73% post-hump BM excess as proven selective reaction targeting**. The same sign of C1 R2 BM gain and later total/post charge is not a causal R2→later-reaction mapping.

## 6. Original raw relaxation shapes and t63 region validation (Nov 14 conversation)

Near hump ±3 600s pulses, directly measured 3–3600s **normalized** relaxation fraction recovered in first 300s:

| material | C1 F(300s) | C2/C3 mean F(300s) | C1 after 1200s contribution | C2/C3 after 1200s |
|---|---:|---:|---:|---:|
| HEO | ~41.6% | ~50.2% | ~26.0% | ~21.5% |
| BM-HEO | ~44.1% | ~48.6% | ~25.3% | ~22.1% |
| Mg-HEO | ~44.5% | ~49.7% | ~25.6% | ~21.9% |
| BM-Mg-HEO | ~43.8% | ~49.0% | ~26.1% | ~21.9% |

First-to-later: early fractional recovery increases; late fractional contribution decreases; C2/C3 full normalized curves strongly resemble each other in same-cell history. Nonnegative exponentially mixed spectrum yields a decreasing relative >1000s weight (~43→35% HEO, ~41→36% BM, ~42→36% Mg, ~42→36% BM-Mg), direction robust to some regularization choices; **exact spectrum peaks/mode weights are NOT uniquely identifiable** within finite 3–3600s window, especially for tau beyond rest. Single exponential RMSE ~0.068–0.090 vs two exp ~0.010–0.013 vs regularized many-exponential ~0.0002–0.001 (more parameters), so monotone t63 is not a one-phase or one-exponential proof.

**Recheck entire first-lithiation R1–R4 boundaries against original full raw relaxation shapes** (~245 full-rest pulses across four electrodes). R2→R3 transition is usually a **minimum or slope reversal** in t63, not a discontinuity:
- HEO boundary ~417 mAh/g, local slope −10.3 to +5.9 s/pulse; within lowest ~9% of adjacent full-shape-change magnitudes.
- BM boundary ~633, +0.2 to +3.5 s/pulse; ~23rd percentile.
- Mg boundary 400, −2.7 to +0.9; ~9th percentile.
- BM-Mg boundary ~583, −3.6 to +6.9; ~7th percentile.

Conclusion: operational R1–R4 bins are real/fixed but a **t63 slope change does not demonstrate discontinuous new chemical reaction**. Normalized full-rest F(t) and fitted slow-band components vary relatively smoothly across boundaries. Region charge changes also reflect **moving t63-defined boundary locations** under modifications: BM-free shifts R2/R3 +217 mAh/g while R1/R2 +50 → R2 gain +167; therefore region-charge difference is not intrinsically equivalent to growth of one chemically isolated process. First-lithiation R3 hump HEO/Mg is inside R3; BM shoulder locations weak.

## 7. C1 additional capacity, R1+R2 and delithiation (Nov 14 continuation)

First C1 lithiation extra vs C2/C3 mean: HEO +383, BM +425, Mg +342, BM-Mg +383 mAh/g. First-lithiation-minus-first-delithiation nominal `irreversible` GITT pulse charge difference ~HEO 333, BM 417, Mg 300, BM-Mg 367. These are similar **orders of magnitude** but are not reaction-specific or necessarily same charge; finite terminal pulses and full-rest selection matter.

R1+R2 C1 nominal charge: HEO **417**, BM **633**, Mg **400**, BM-Mg **583** mAh/g. Contrast with C1 extra *before hump*: HEO 458, BM~350, Mg 400, BM-Mg~342. BM differs by ~240–280 mAh/g; therefore **cannot equate all of R1+R2 with the C1-specific irreversible upfront reaction**, nor infer C1 R3 contribution uniquely by subtracting.

First and second *delithiation total* differ only about **+16.7 mAh/g in C1** for all four under complete-rest full-pulse-count comparison, despite first lithiation extra 342–425; this supports similar amount of recovered charge from C1 delithiation onward, not atomically precise mapping of where the C1 extra was lost.

First delithiation QOCV vs normalized charge is close in shape to C2/C3 but shifted downward by roughly **60–120 mV** depending electrode; empirically adding constant voltage to first delithiation registers its *QOCV curve* with residual RMSE ~HEO 18.7mV, BM 8.2, Mg 28.2, BM-Mg 14.6. Shift is phenomenological, **not a physical voltage-correction model**. First delithiation C1 QOCV–charge curve gets closer to C2/C3, but aligned t63 and |ΔErest| DO NOT jointly collapse under same voltage shift. On same fixed QOCV 0.3–1.7V, t63 RMSE C1 versus C2/C3 avg HEO 45.3s, BM 17.9, Mg 51.3, BM-Mg 35.4, versus C2-vs-C3 HEO 10.9, BM 7.4, Mg 21.4, BM-Mg 24.7; |ΔErest| C1-to-later RMSE HEO 8.1 mV, BM 4.0, Mg 8.4, BM-Mg 5.4. First delithiation *qualitatively* establishes a later-like response but full kinetic relaxation stabilizes further after C1.

The same QOCV 0.4–1.65 V constant shift often **worsens** voltage-rest-amplitude registration (example pre→post RMSE: HEO 8.5→11.7 mV, BM 4.1→10.9, Mg 5.7→16.9, BM-Mg 4.2→15.0). This makes separating charge–voltage topology and dynamic relaxation essential.

First delithiation vs later delithiation charge distribution is shifted over voltage despite similar total, so **do not assert that C1-specific lithiation charge is irreversibly lost in one delithiation voltage interval**. GITT alone cannot trace a Li atom or elementary reaction one-to-one between halfcycles.

## 8. Treatment contrasts: what survives as robust and what does NOT

First-cycle total modification differences vs mean later-cycle total (complete pulses):

| treatment − reference | C1 total charge change | later C2/C3 total charge change | dominant C1 region change |
|---|---:|---:|---|
| BM-HEO − HEO | +183 | +142 | R2 +167 |
| BM-Mg − Mg | +133 | +92 | R2 +150 |
| Mg − HEO | −283 | −242 | R3 −200 |
| BM-Mg − BM | −333 | −292 | R3 −183 |

Differences between C1 and later matched contrasts in above accounting happen to be 41.7 mAh/g; **do not overinterpret a few whole GITT pulses**. Important: retained *direction* of modification in later capacity is a real practical observation; it cannot uniquely attribute that retained capacity to first R2 or R3 chemistry.

The first-lithiation corresponding R-region partition may respond primarily to how the operational boundary moved with modification and to overlapping reactions, not reaction-exclusive capacity. A linked **hump** or **~0.9V dQ/dV** landmark remains useful for repeatedly tracking response across cycles, not uniquely assigning it.

## 9. Scientific decision and recommended next action

- Keep article narrative, PI-approved Abstract/Introduction and original kinetic-region R1–R4 analysis intact **unless the PI explicitly authorizes manuscript rewriting**.
- Current strongest supported statement: large first-cycle-specific charge/kinetic history; C1 delithiation already generally later-like; C2/C3 share highly repeatable GITT relaxation/voltage profiles; modified HEOs show persistent but material-dependent capacity and relaxation-amplitude contrasts.
- First-cycle distinct early insertion/reconstruction vs later reconstructed conversion is a useful **hypothesis consistent with prior spinel-oxide studies**, not direct proof of the current four samples' exact phases. Hump interpreted as marker of a putative shared dominant process is an exploratory assumption; “dominant process” may change in charge weight, QOCV, t63 with cycle and sample. C1 vs C2/C3 identical reaction identity not yet shown.
- Next high-value experiment-free calculation before expanding manuscript: **compare full normalized raw delithiation rest-voltage shapes at the same QOCV across C1/C2/C3**, and test whether first-delithiation shape is later-like while absolute amplitude/t63 differs. Potentially use an explicit generative physics model/FEM only if it can discriminate first-cycle-pristine-to-reconstructed-state vs simple whole-capacity/OCV/polarization shift (see simulation decision note). Model parameter identifiability, experimental geometry, and false mechanism attribution are critical.
- Do not keep adding fitting flexibility without a falsifiable hypothesis. Report current measured observations and sensitivity checks separately from suggested mechanisms.

## 10. Locally created visuals, CSV, scripts: provenance **without claiming GitHub binary uploads**

The previous chat showed many sandbox assets with names including: `HEO_hump_anchor_deltaErest_zoom_2x2.png`, `HEO_hump_raw_relaxation_normalized_C1_C3_2x2.png`, `HEO_hump_exponential_mixture_slow_weight_summary.png`, `HEO_C1_R1_R4_F_shape_steps_2x2.png`, `HEO_C1_R1_R4_t63_2x2.png`, `HEO_C1_Rregions_vs_later_hump_aligned_charge_2x2.png`, `HEO_delith_C1_C3_dErest_vs_QOCV_2x2.png`, `HEO_delith_C1_QOCV_offset_registration_2x2.png`, `HEO_delith_C1C3_t63_vs_normalized_capacity_2x2.png`, `HEO_delith_C1C3_t63_QOCV_independent_shift_control_2x2.png`, and their downloadable numerical CSV/script companions (`HEO_C1_region_vs_hump_early_excess_balance.csv`, `HEO_C1_region_charge_boundary_shift_identities.csv`, `HEO_delith_C1C3_relaxation_metric_comparisons.csv`, `HEO_delith_independent_QOCV_shift_kinetics_control.csv`, etc.).

**Current GitHub update creates durable research TEXT records only.** Previous conversation-generated sandbox files may expire and are not verified as available in new chats. Recompute if raw sources available or explicitly request uploads as needed; never invent a link or claim that file binaries are in GitHub.

## 11. Workflow instructions locked by PI

- **GitHub update only when the user explicitly requests it.** Do not auto-commit at the end of each analytical step. The present Nov 16 request explicitly authorizes these documentation updates.
- **Do not create/revise Word files** unless explicitly requested; user often wants paste-ready replacement paragraphs, captions and comment replies in chat.
- Preserve accepted Abstract/Introduction exactly. Revisit scientifically only by explicit PI decision, not silent stylistic editing.
- Numerical source hierarchy and boundary selection as in manuscript authoritative science and Nov 11 Fig3 records.
- Latest open prompt before this requested documentation: **“시뮬레이션을 추가하는건 어떤가 FEM이나”**. No simulation decision or run was completed before the request switched to GitHub continuity; treat as **open research option**, not implemented result.

