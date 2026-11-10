# HEO Word text snapshot — HEO_Manuscript_Reviewed_With_Word_Comments_2026-11-07.docx

**Source file:** `HEO_Manuscript_Reviewed_With_Word_Comments_2026-11-07.docx`  
**SHA256 (original Word):** `021faf908cb2d4e274c0ae9fc805381456c1af204ad8a964a7ae364590a13b41`  
**Status:** ASSISTANT-GENERATED REVIEW COPY. Comments 45, 9 yellow unresolved paragraphs. The plain-text extraction below DOES NOT embed Word comments or original figures.

**IMPORTANT:** This is a searchable, lossy text transcription rendered from the Word document for future chat continuity, not an editable or visually faithful replacement of the Word. Page-wrap artifacts may remain. Figure images and native Word comments are absent. Check separate November-10 audit/decision files and original Word for the actual figure composition and 45 reviewer comment anchors.

---

<PARSED TEXT FOR PAGE: 1 / 14>

Reaction-Region-Dependent Lithiation Response to Ball
Milling and Mg Incorporation in Spinel High-Entropy Oxide
Anodes
Seonghyeon Park¹, Yoonju Kang¹, Taekyung Yu¹,*, Taeho Yoon¹,*

¹ Department of Chemical Engineering, Kyung Hee University, Yongin 17104, Republic of Korea. *Correspondence:
tkyu@khu.ac.kr (T. Yu); tyoon@khu.ac.kr (T. Yoon).


Abstract
Spinel high-entropy oxides (HEOs) have attracted considerable interest as high-capacity anodes for lithium-
ion batteries. Improving their electrochemical performance has motivated studies of particle refinement and
cation substitution, which modify oxide morphology and cation chemistry, respectively. However, how these
modifications affect the underlying lithium storage mechanism remains poorly understood. Because lithiation
involves multiple overlapping processes—including transition-metal reduction, structural transformation,
metal/Li₂O nanocomposite formation, and possible interfacial storage—quantifying the charge associated
with each process is difficult, obscuring which processes are promoted or suppressed by material
modification. Consequently, modification effects have been evaluated mainly through total capacity while
relying on spectroscopic tools for qualitative and localized mechanistic insights, hindering systematic
materials design. To overcome this limitation, this study proposes a galvanostatic intermittent titration
(GITT) approach that partitions lithiation into four electrochemical regions (R1–R4) governed by dominant
reactions, and quantifies how ball milling and Mg incorporation affect each region. Assigning the dominant
reaction processes in each region based on prior mechanistic studies reveals which conversion stages respond
most sensitively to each modification: ball milling primarily expands oxide reconstruction and early
transition-metal reduction (R2), whereas Mg incorporation selectively suppresses further reduction of
intermediate oxides and metal/Li₂O formation (R3). Interpreting these regional capacity shifts clarifies how
each modification alters the conversion mechanism and guides the design of conversion-type electrodes.
Keywords: spinel high-entropy oxide; conversion anode; ball milling; magnesium incorporation; GITT
relaxation; reaction-region capacity

1. Introduction
Spinel high-entropy oxides (HEOs) combine multiple transition-metal cations within a single-phase oxide
lattice and have attracted wide interest as high-capacity conversion anodes [1–3]. Although their overall
lithium storage is often summarized as a metal-oxide-to-metal/Li ₂O nanocomposite conversion reaction,
state-resolved studies reveal a far more sequential pathway. Operando X-ray absorption spectroscopy has
shown that Fe and Mn pass through intermediate oxide states before reaching metallic form, whereas higher-
potential cations such as Ni and Cu reduce more directly [4]. Ex situ diffraction and absorption studies have
also identified initial Li⁺ insertion, cation migration, and spinel-to-rock-salt structural transformations prior
to full conversion [5], consistent with in situ observations of coexisting intermediate oxide and metal/Li ₂O
domains in Fe₃O₄ [6]. Lithiation therefore does not proceed as a single uniform event. Instead, as lithiation
progresses, the dominant reaction process governing charge storage shifts sequentially across distinct kinetic
regimes.
This sequential progression exposes a major limitation in how modified HEO anodes are currently evaluated.
Particle refinement, cation substitution, and Li₂O doping are known to alter the total capacity and rate

                            HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 2 / 14>

capability of spinel HEOs [7–9]. However, because multiple reduction, phase-transformation, and interfacial
storage processes overlap during lithiation, conventional electrochemical testing quantifies only the net
capacity change without resolving which individual reaction stage is promoted or suppressed. Meanwhile,
advanced spectroscopic and microscopic techniques identify local chemical states qualitatively at selected
states of charge, but cannot directly measure how much capacity (mAh g ⁻ ¹) each reaction stage gains or loses
upon modification. Bridging this gap requires an electrochemical method that partitions lithiation into
dominant reaction regimes and quantifies the capacity associated with each regime.
Shifts in the dominant reaction process during lithiation alter both the thermodynamic and kinetic responses
of the electrode. In conventional low-rate galvanostatic curves, overlapping reduction and phase-
transformation reactions occur at similar potentials, merging into a single broad voltage plateau with poorly
separated differential-capacity (dQ/dV) peaks [4,5]. Reaction kinetics, however, differ substantially across
these stages—from initial Li⁺ insertion into the host lattice, to rapid near-surface reduction of easily
reducible cations, to solid-state diffusion-limited conversion of core intermediate oxides across thickening
Li₂O/metal shells, and finally to low-potential interfacial storage. Galvanostatic intermittent titration (GITT)
probes these kinetic transitions directly by recording voltage relaxation after successive current pulses [10–
12]. From each rest period, the characteristic relaxation time (t ₆₃) captures the timescale of voltage re-
equilibration, while the recovery amplitude (Δ Erest) and end-of-rest quasi-open-circuit voltage (QOCV) track
the overpotential magnitude and quasi-thermodynamic potential. Inflections in t ₆₃ thus provide a kinetic
basis for dividing lithiation into distinct reaction regions (R1–R4).
Ball milling and Mg incorporation were selected to examine how morphological refinement and cation
composition affect each reaction region in spinel HEOs [13,14]. GITT was applied to pristine HEO, ball-milled
HEO (BM-HEO), Mg-substituted HEO (Mg-HEO), and ball-milled Mg-HEO (BM-Mg-HEO), enabling matched
comparisons of each modification with and without the other. Based on established mechanistic studies [4–
6,15–19], the four kinetically defined regions are assigned to: (R1) initial Li ⁺ insertion and spinel-to-rock-salt
structural evolution; (R2) oxide reconstruction and rapid near-surface reduction of higher-potential cations;
(R3) diffusion-limited reduction of intermediate core oxides and metal/Li ₂O nanocomposite growth; and (R4)
low-potential interfacial charge storage at metal/Li₂O phase boundaries. Region-resolved capacity analysis
reveals that ball milling primarily expands R2 (+150 to +167 mAh g ⁻ ¹) and R4 (+67 to +100 mAh g ⁻ ¹) while
reducing R3 (−117 to −133 mAh g⁻ ¹), indicating that particle refinement shifts conversion from the slow core
regime into the rapid near-surface regime and increases interfacial storage. Conversely, Mg incorporation
selectively suppresses R3 (−183 to −200 mAh g⁻ ¹) and R4 (−67 to −100 mAh g ⁻ ¹), reflecting stabilization of
intermediate rock-salt oxides against full conversion. These findings demonstrate how region-resolved GITT
analysis links material modifications to specific stages of the conversion mechanism.




                             HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 3 / 14>

2. Results and Discussion

2.1. Structural and surface changes induced by ball milling and Mg incorporation




Figure 1. Electron microscopy and elemental distribution of the spinel HEO powders: (a) HEO, (b) BM-HEO, (c) Mg-HEO, and
(d) BM-Mg-HEO. Representative TEM images, high-resolution lattice fringes, selected-area electron diffraction (SAED)
patterns, and EDS elemental maps are shown for each material. [ 공동연구자 확인: Figure 1 HRTEM 의 CoGa₂O₄ (311)/(400)
표기와 실제 Ga-free 조성이 모순됩니다. 원본 FFT/SAED, d-spacing 및 사용한 PDF/ICDD 카드로 결정면을 재검증한 후 그림
의 상명·면지수를 교체해 주세요. 임의로 Spinel (311)로 바꾸지 않습니다.]




                              HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 4 / 14>

Figure 2. Surface morphology, nitrogen adsorption, and XPS spectra of the as-prepared HEO powders. (a) N ₂ adsorption
isotherms and BET specific surface areas: HEO (3.94 m² g⁻¹), BM-HEO (18.16 m² g ⁻¹), Mg-HEO (6.49 m² g ⁻¹), and BM-Mg-HEO
(16.64 m² g⁻¹). (b) SEM images of the four powders (100 nm scale bars). (c–h) High-resolution Ni 2p, Co 2p, Fe 2p, Mn 2p, Cr 2p,
and O 1s XPS spectra. (i) Mg 1s XPS spectra for Mg-HEO and BM-Mg-HEO. [공동연구자 확인: Figure 2(c–i) 축 눈금/라벨 잘림
없는 원본 그림으로 교체하고, XPS 결합에너지 보정기준, 각 스펙트럼의 측정 배치, 피팅 원본 및 화학상태 배정 근거를 보내 주세
요. 특히 Cr 2p와 O 1s는 재확인이 필요합니다.]

The four spinel HEO powders—HEO, BM-HEO, Mg-HEO, and BM-Mg-HEO—provide a two-by-two matrix to
isolate the effects of ball milling and Mg incorporation (Figure 1). TEM and SAED patterns confirm the
crystalline spinel structure across all four compositions, while EDS elemental maps demonstrate a uniform
spatial distribution of Co, Mn, Cr, Fe, Ni, O, and (in the substituted samples) Mg. [공동연구자 확인: 실제 측정
                                HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 5 / 14>

한 XRD 패턴·측정조건과 ICP-OES 원소별 조성표를 제공해 주세요. 데이터가 존재하고 검증되면 본문 또는 SI에
수치/그림을 반영하겠습니다. 현재 단일상 및 Mg 치환 위치는 확정하지 않습니다.]
Ball milling substantially refines the particle and aggregate morphology, increasing the BET specific surface
area more than fourfold from 3.94 to 18.16 m² g ⁻ ¹ in the Mg-free pair and from 6.49 to 16.64 m² g ⁻ ¹ in the Mg-
containing pair (Figure 2a,b). This expansion in gas-accessible surface area directly reflects the breakup of
coarse secondary agglomerates into finer nanoscale particulates observed by SEM. Notably, unmilled Mg-HEO
exhibits a higher BET surface area than pristine HEO (6.49 versus 3.94 m² g ⁻ ¹) yet delivers a lower lithiation
capacity. Surface area alone therefore cannot explain the compositional effect of Mg substitution.
High-resolution XPS spectra characterize the near-surface cation oxidation states and oxygen environments of
the as-prepared powders (Figure 2c–i). The Ni 2p, Co 2p, Fe 2p, Mn 2p, and Cr 2p envelopes confirm the
coexistence of mixed-valence transition-metal cations typical of multication spinels, while the Mg 1s peak
near 1303 eV verifies successful Mg incorporation in Mg-HEO and BM-Mg-HEO. In the O 1s region (Figure 2h),
all samples display a primary lattice metal–oxygen (M–O) peak near 529.8 eV alongside a higher-binding-
energy shoulder associated with surface hydroxyl or defective oxygen species (–OH). [공동연구자 확인: 시료별
동일 기준으로 교정한 XPS 원본/피팅 자료와 산화수 배정의 정량 근거가 있는지 확인해 주세요. 데이터가 확인
되면 의미 있는 차이만 기술하며, Cr(VI)·O-vacancy 변화는 근거 없이 부여하지 않습니다.]

2.2. Electrochemical performance establishes opposing modification effects




Figure 3. Galvanostatic electrochemical performance of the four HEO electrodes. (a–d) Voltage profiles for the first three cycles
at 0.1 C of (a) HEO, (b) BM-HEO, (c) Mg-HEO, and (d) BM-Mg-HEO. (e) Cycling stability over 100 cycles at 0.1 C. (f) Rate
capability from 0.1 to 5 C and recovery to 0.1 C.

Galvanostatic cycling at 0.1 C establishes the opposing net effects of ball milling and Mg incorporation on
lithium storage (Figure 3a–d). The initial lithiation/delithiation capacities are 901.25/609.12 mAh g ⁻ ¹ for
HEO, 1056.10/782.08 mAh g⁻ ¹ for BM-HEO, 731.15/458.91 mAh g ⁻ ¹ for Mg-HEO, and 944.07/580.83 mAh g ⁻ ¹

                                HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 6 / 14>

for BM-Mg-HEO. Ball milling increases the first-lithiation capacity by +154.85 mAh g ⁻ ¹ without Mg and by
+212.92 mAh g⁻ ¹ with Mg. Conversely, Mg incorporation reduces the first-lithiation capacity by −170.10 mAh
g⁻ ¹ in the unmilled state and by −112.03 mAh g⁻ ¹ after milling.
This contrast persists during extended cycling and rate testing (Figure 3e,f). After 100 cycles at 0.1 C,
reversible discharge capacities reach approximately 415, 583, 431, and 492 mAh g ⁻ ¹ for HEO, BM-HEO, Mg-
HEO, and BM-Mg-HEO, respectively, while all four electrodes recover their baseline capacity upon returning
from 5 to 0.1 C. Although the first-lithiation voltage profiles (Figure 3a–d) clearly show these net capacity
differences, their broad, featureless plateaus below 0.8 V obscure which stages of the conversion reaction
drive the capacity gains and losses. Pulse-resolved GITT measurements are therefore used to partition the
lithiation pathway into distinct kinetic regimes.

2.3. Electrochemical signatures of the progressive conversion reaction




Figure 4. Division of first lithiation into four electrochemical regions (R1–R4) from pulse-resolved GITT data: (a) HEO, (b) BM-
HEO, (c) Mg-HEO, and (d) BM-Mg-HEO. Top, middle, and bottom panels display the characteristic relaxation time (t ₆₃), finite-
window voltage-recovery amplitude (ΔErest), and end-of-rest quasi-open-circuit voltage (QOCV), respectively, plotted against
normalized GITT charge. Vertical dashed lines mark the kinetic region boundaries (L1, L3, and L4) identified from inflection
landmarks in t₆₃.


                                HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 7 / 14>

GITT measurements were performed during the first lithiation using successive 600 s current pulses (100 mA
g⁻ ¹) followed by 3600 s open-circuit rest periods (Figure 4). From each rest period, three complementary
parameters are extracted: the characteristic relaxation time (t ₆₃), defined as the time required to reach 63.2%
of the signed voltage recovery between 3 and 3600 s; the voltage-recovery amplitude, Δ Erest = |E_rest(3600 s) −
E_rest(3 s)|; and the rest-end potential (QOCV). Tracking these three observables across successive pulses
reveals kinetic transitions that remain hidden in continuous galvanostatic curves.
Across all four electrodes, the t₆₃ trajectory exhibits three reproducible inflection landmarks—designated L1,
L3, and L4—that partition lithiation into four regions (R1–R4; Figure 4). An early post-transient minimum in
t₆₃ defines L1, and a broad central minimum preceding a sustained kinetic slowdown defines L3. Later in
lithiation, L4 marks either a local t₆₃ maximum followed by a decline (in HEO and BM-HEO) or a distinct
inflection in the rising t₆₃ slope (in Mg-HEO and BM-Mg-HEO). The resulting cumulative pulse indices
(L1/L3/L4) are 6/25/55 for HEO, 9/38/60 for BM-HEO, 7/24/42 for Mg-HEO, and 9/35/46 for BM-Mg-HEO.
Correlating these kinetic landmarks with operando XAS, XRD, and in situ TEM studies of spinel conversion
oxides [4–7,19] assigns a distinct dominant reaction process to each region: (i) R1 (initial Li⁺ insertion and
spinel-to-rock-salt transition): at high potentials (~1.5 to 0.8 V), Li⁺ inserts into empty octahedral sites
accompanied by partial reduction of higher-valence cations (Mn³⁺ , Co³ ⁺ , Fe³ ⁺ ) and tetrahedral-to-octahedral
cation migration, relaxing the initial nucleation barrier toward L1 alongside initial SEI formation; (ii) R2
(oxide reconstruction and early transition-metal reduction): between L1 and L3 (~0.8 to 0.6 V), more
easily reducible cations (such as Ni²⁺ and Co²⁺ ) nucleate metallic nanodomains while accessible surface and
near-surface oxide regions undergo rapid phase reconstruction, keeping t ₆₃ relatively short; (iii) R3 (further
reduction of intermediate core oxides and metal/Li₂O formation): between L3 and L4 (~0.6 to 0.4 V),
conversion proceeds into the particle interiors where lower-potential intermediate oxides (enriched in Fe² ⁺ ,
Mn²⁺ , and Cr³⁺ ) reduce across thickening Li₂O/metal product shells, causing solid-state transport resistance
and t₆₃ to rise steadily; and (iv) R4 (low-potential interfacial storage at metal/Li₂O boundaries): below
L4 (<0.4 V), after bulk oxide conversion is largely complete, charge storage is governed by interfacial/space-
charge Li⁺ accumulation across high-surface-area metal/Li₂O nanocomposite boundaries and polymeric
interfacial film formation, accompanied by residual core reduction.
Beyond defining the region boundaries, the t₆₃ and ΔErest trajectories capture distinct kinetic signatures of
each modification. In R1, unmilled HEO and Mg-HEO start with long relaxation times (t ₆₃ > 16 min) that fall
steeply, whereas ball-milled BM-HEO and BM-Mg-HEO start with much shorter relaxation times (t ₆₃ ≈ 4–5
min) that rise gradually toward L1. In R3, pristine HEO displays a prominent hump in Δ Erest, rising from 145
mV at R3 onset to 189 mV near pulse 50 before declining (Figure 4a). Mg-HEO shows only a muted rise (109 to
118 mV), whereas both ball-milled electrodes exhibit monotonically decreasing Δ Erest throughout R3—even
though t₆₃ increases across R3 in all four samples.
Sub-window decomposition of the 60 min rest curves shows that the Δ Erest hump in pristine HEO originates
specifically from slow, late-stage voltage recovery between 10 and 60 min (Figure S4). Between pulses 26 and
50 in pristine HEO, total voltage recovery increases by +44.2 mV: the 10–60 min contribution grows by +37.5
mV and the 1–10 min contribution by +16.5 mV, whereas fast recovery within the first minute decreases by
−9.8 mV (raising the 10–60 min share from 30.8% to 43.4%). Both ball milling and Mg incorporation suppress
this delayed 10–60 min relaxation component during R3 (Figures S4–S6).




                            HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 8 / 14>

2.4. Localization of modification-induced charge changes across the four regions




Figure 5. Regional first-lithiation GITT capacities across R1–R4. (a) Stacked regional capacities for HEO, BM-HEO, Mg-HEO, and
BM-Mg-HEO. (b) Regional capacity changes (ΔQ) induced by ball milling in the Mg-free (dark blue, BM-HEO minus HEO) and
Mg-containing (light blue, BM-Mg-HEO minus Mg-HEO) pairs. (c) Regional capacity changes ( ΔQ) induced by Mg
incorporation in the unmilled (dark brown, Mg-HEO minus HEO) and ball-milled (light brown, BM-Mg-HEO minus BM-HEO)
pairs.

Summing the capacity delivered within each kinetically defined region reveals exactly where ball milling and
Mg incorporation add or remove charge (Figure 5; Tables S1 and S2). In pristine HEO, R2 (oxide
reconstruction and early transition-metal reduction) and R3 (further reduction of intermediate oxides and
metal/Li₂O formation) account for 316.7 and 500.0 mAh g ⁻¹, respectively. After ball milling (BM-HEO), the R2
capacity jumps to 483.3 mAh g⁻ ¹ (+166.7 mAh g⁻ ¹), whereas the R3 capacity drops to 366.7 mAh g ⁻ ¹ (−133.3
mAh g⁻ ¹). Simultaneously, ball milling increases capacity in R1 (+50.0 mAh g ⁻ ¹) and R4 (+100.0 mAh g ⁻ ¹),
yielding a large net capacity gain despite the reduction in R3.
A nearly identical regional pattern appears in the Mg-containing pair (Figure 5b). Ball milling Mg-HEO into
BM-Mg-HEO increases R2 capacity from 283.3 to 433.3 mAh g ⁻ ¹ (+150.0 mAh g ⁻ ¹), increases R1 (+33.3 mAh
g⁻ ¹) and R4 (+66.7 mAh g⁻ ¹), and decreases R3 capacity from 300.0 to 183.3 mAh g⁻ ¹ (−116.7 mAh g ⁻ ¹). Across
both compositional pairs, ball milling consistently produces its primary capacity gain in R2 and a secondary
gain in R4, while reducing the capacity delivered in R3.
Mg incorporation exhibits a markedly different regional profile (Figure 5c). Introducing Mg reduces R3
capacity sharply from 500.0 to 300.0 mAh g⁻ ¹ (−200.0 mAh g ⁻ ¹) in the unmilled pair and from 366.7 to 183.3
mAh g⁻ ¹ (−183.3 mAh g⁻ ¹) in the milled pair. By comparison, Mg incorporation causes only minor losses in
R2 (−33.3 and −50.0 mAh g⁻ ¹), moderate losses in R4 (−66.7 and −100.0 mAh g ⁻ ¹), and negligible change in R1
(+16.7 and 0.0 mAh g⁻ ¹). The capacity penalty of Mg substitution is thus heavily concentrated in R3.
Each complete 600 s GITT pulse at 100 mA g⁻ ¹ delivers 16.67 mAh g ⁻ ¹. To verify that these regional trends are
not artifacts of exact boundary placement, all three boundaries (L1, L3, and L4) were independently perturbed

                               HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 9 / 14>

by ±1 pulse across all 729 combinations (Table S3). Every single combination preserves the milling-induced R2
gain and R3 loss, and confirms R3 as the dominant Mg-induced loss region (in 100% of unmilled and 702 of
729 milled combinations).

2.5. Physical origins of the contrasting material responses
Interpreting these regional capacity shifts through the dominant physical processes assigned to R1–R4
clarifies the contrasting mechanisms of ball milling and Mg incorporation. Ball milling delivers its largest
capacity gain (+150 to +167 mAh g⁻ ¹) in R2, governed by oxide reconstruction and early transition-metal
reduction in accessible near-surface regions. Because particle refinement increases the BET surface area more
than fourfold (Figure 2a), a much larger fraction of the oxide volume is converted from slow-diffusing particle
interiors into electrolyte-accessible near-surface and grain-boundary domains. Consequently, oxide domains
that would otherwise undergo slow, diffusion-limited core conversion during R3 are instead reduced earlier
during R2. This shift from core-limited conversion to near-surface reduction directly explains why ball
milling simultaneously expands R2 (+150 to +167 mAh g ⁻ ¹) and shrinks R3 (−117 to −133 mAh g ⁻ ¹), while the
resulting finer metal/Li₂O nanocomposite boundaries boost low-potential interfacial storage in R4 (+67 to
+100 mAh g⁻ ¹).
The early t₆₃ trajectories in R1 further corroborate this surface-accessibility mechanism (Figure 4). In
unmilled HEO and Mg-HEO, coarse primary particles impose a high initial solid-state insertion and rock-salt
nucleation barrier, producing long initial relaxation times (t ₆₃ > 16 min) that decrease as reaction fronts
penetrate the particles. In milled BM-HEO and BM-Mg-HEO, rapid surface and near-surface Li ⁺ uptake yields
short initial relaxation times (t₆₃ ≈ 4–5 min) that gradually lengthen as the reaction moves inward.
In contrast, Mg incorporation selectively suppresses capacity in R3 (−183 to −200 mAh g ⁻ ¹)—the region
governed by further reduction of intermediate rock-salt oxides and metal/Li ₂O product formation—even
though unmilled Mg-HEO has a higher BET surface area than pristine HEO. Unlike the transition-metal
cations, Mg²⁺ is electrochemically inactive within the anode voltage window. Incorporating Mg² ⁺ into the
spinel lattice both reduces the concentration of reducible transition-metal centers and thermodynamically
stabilizes rock-salt (Mg,M)O intermediate phases against full reduction to metallic nanodomains [8,15–19].
While initial Li⁺ insertion (R1) and early near-surface reduction of higher-potential cations (R2) proceed with
minimal penalty, the stabilization of Mg-bearing intermediate oxides strongly restricts core oxide reduction
in R3. In turn, because fewer metal/Li₂O nanocomposite interfaces are generated during R3, subsequent low-
potential interfacial storage in R4 is also reduced (−67 to −100 mAh g⁻ ¹).
The suppression of the R3 recovery-amplitude (Δ Erest) hump after either ball milling or Mg incorporation
aligns naturally with this mechanism (Figure 4 and Figure S4). In pristine HEO, driving intermediate-oxide
reduction through coarse, unmilled particles across thickening Li ₂O/metal shells creates steep core–shell
concentration gradients and slow phase-boundary rearrangement, manifesting as large delayed voltage
recovery between 10 and 60 min [6,20–24]. Ball milling eliminates this delayed hump by shortening the solid-
state diffusion length and shifting conversion into R2, whereas Mg incorporation suppresses the hump by
curtailing extensive core conversion in R3. Common-QOCV comparisons (Table S5) confirm that this
attenuation reflects genuine kinetic homogenization rather than a change in the QOCV–charge slope.




                            HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 10 / 14>

2.6. Implications for electrochemical-region-guided materials design




Figure 6. Summary of reaction-region-dependent modification effects mapped onto the first-lithiation QOCV profile of spinel
HEO. The four kinetically defined regions correspond to: (R1) initial Li ⁺ insertion and spinel-to-rock-salt structural evolution;
(R2) oxide reconstruction and early transition-metal reduction; (R3) further reduction of intermediate oxides and metal/Li ₂O
nanocomposite formation; and (R4) low-potential interfacial charge storage at metal/Li ₂O phase boundaries. Arrows highlight
the primary regional capacity shifts: ball milling expands R2 and R4 while shifting charge out of R3, whereas Mg incorporation
selectively suppresses R3 and R4.

Resolving capacity changes across R1–R4 provides clear guidelines for designing conversion-type high-
entropy oxide anodes (Figure 6). First, evaluating material modifications solely through total lithiation
capacity masks competing internal effects. In BM-HEO, for example, the net GITT capacity increase (+183.3
mAh g⁻ ¹) is the result of +316.7 mAh g⁻ ¹ gained across R1, R2, and R4 partially offset by −133.3 mAh g ⁻ ¹
shifted out of R3.
Second, because morphological refinement and cation substitution act on distinct stages of the conversion
pathway, they can be paired to balance capacity and structural stability. While Mg incorporation stabilizes
the oxide matrix at the expense of R3 conversion capacity (−200.0 mAh g ⁻ ¹), subsequent ball milling (BM-
Mg-HEO) restores +150.0 mAh g⁻ ¹ in R2 and +66.7 mAh g ⁻ ¹ in R4 by shifting reduction into the accessible
near-surface regime and expanding metal/Li₂O interfacial storage. Region-resolved GITT analysis thus
enables targeted pairing of particle refinement (to promote R2 oxide reconstruction/reduction and R4
interfacial storage) with cation chemistry (to tune R3 intermediate-oxide conversion).

3. Conclusion
Inflections in the GITT characteristic voltage-relaxation time (t₆₃) partition the first lithiation of spinel HEO
anodes into four electrochemical regions (R1–R4) governed by distinct dominant processes: initial Li⁺
insertion and spinel-to-rock-salt evolution (R1), oxide reconstruction and early transition-metal reduction
(R2), further reduction of intermediate oxides and metal/Li₂O formation (R3), and low-potential interfacial
storage at metal/Li₂O boundaries (R4). Quantifying regional capacities across matched HEO electrodes
demonstrates that ball milling and Mg incorporation target different stages of this conversion sequence. Ball
milling increases overall lithiation capacity primarily by expanding R2 (+150 to +167 mAh g ⁻ ¹) and R4 (+67 to
+100 mAh g⁻ ¹) while reducing R3 (−117 to −133 mAh g ⁻ ¹), showing that particle refinement shifts conversion
from slow core reduction into rapid near-surface reduction and increases interfacial storage. Conversely, Mg
                                HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 11 / 14>

incorporation reduces overall capacity by selectively suppressing intermediate-oxide reduction and
metal/Li₂O formation in R3 (−183 to −200 mAh g⁻¹) and subsequent interfacial storage in R4 (−67 to −100
mAh g⁻ ¹). By quantitatively separating overlapping conversion stages that are indistinguishable in
conventional voltage curves, this region-resolved GITT approach clarifies how processing and composition
alter the conversion mechanism and guides the rational design of conversion-type electrodes.

4. Experimental Section

4.1. Materials and synthesis
Nickel(II) chloride hexahydrate (NiCl₂·6H₂O, 99.9%), iron(III) chloride hexahydrate (FeCl ₃·6H ₂O, ≥98%),
cobalt(II) chloride hexahydrate (CoCl₂·6H₂O, 98%), manganese(II) chloride tetrahydrate (MnCl ₂·4H ₂O,
≥98%), chromium(III) chloride hexahydrate (CrCl₃·6H₂O), [공동연구자 확인: 실제 Mg 전구체의 제품명·화학식
· 순 도 · 제 조 사 와 투 입 량 을 기 록 해 주 세 요 .], sodium hydroxide (NaOH, ≥97.0%), and sodium carbonate
monohydrate (Na₂CO₃·H₂O, ≥99.5%) were purchased from Sigma-Aldrich and used as received.
The Mg-free spinel HEO was synthesized via coprecipitation followed by calcination. Equimolar amounts of
NiCl₂·6H₂O, FeCl₃·6H₂O, CoCl₂·6H₂O, MnCl₂·4H₂O, and CrCl₃·6H₂O (1.4 mmol each) were dissolved in 20 mL of
deionized water. An alkaline precipitant solution containing 14 mmol NaOH and 7 mmol Na ₂CO ₃·H ₂O in 10 mL
of deionized water was added dropwise under vigorous stirring at 800 rpm. After aging for 2 h at room
temperature, the precipitate was collected by centrifugation, washed three times with deionized water, and
dried overnight at 70 °C. The dried precursor was calcined in air at 900 °C for 2 h at a heating rate of 5 °C
min⁻ ¹ to obtain pristine HEO. [공동연구자 확인: Mg-free 합성의 전구체별 몰수, 침전제 투입량, 교반·숙성·세척
·건조·소성 조건을 실험노트와 대조하고, Mg-HEO 전구체별 실제 몰비 및 모든 공정 차이를 제공해 주세요. Mg
치환 여부와 치환 대상 원소는 원자료 확인 전 확정하지 않습니다.]
To prepare ball-milled HEO (BM-HEO) and ball-milled Mg-HEO (BM-Mg-HEO), the calcined HEO or Mg-HEO
powder (2 g) was planetary ball-milled for 12 h at 500 rpm in an 80 mL stainless-steel jar using 5 mm ZrO₂
balls at a ball-to-powder mass ratio of 10:1. [ 공동연구자 확인: 두 ball-milled 시료의 실제 분말 질량, 분쇄
기/용기/볼 재질·크기, 볼:분말 비, 회전속도, 총 시간, 용매 사용 여부와 간헐 운전 여부를 실험노트로 확인해 주
세요.]

4.2. Structural, compositional and surface characterization
Crystal structure was examined by powder X-ray diffraction (XRD, MiniFlex 600, Rigaku) using Cu Kα
radiation (λ = 1.5406 Å), and bulk elemental stoichiometry was determined by inductively coupled plasma
optical emission spectroscopy (ICP-OES, iCAP PRO, Thermo Fisher Scientific). [ 공동연구자 확인 : XRD/ICP-
OES 실제 측정 여부와 원본 자료·기기·조건을 확인해 주세요. BET 분석 전 degassing 온도·시간·분위기 및 기기
모 델 명 을 실 험 기 록 으 로 확 인 해 주 세 요 .] Surface chemical states were analyzed by X-ray photoelectron
spectroscopy (XPS, K-Alpha, Thermo Fisher Scientific) using monochromatic Al K α radiation. Particle
morphology, lattice structure, and elemental distribution were characterized by field-emission scanning
electron microscopy (FE-SEM, Gemini 360, Zeiss) and Cs-corrected transmission electron microscopy (TEM,
JEM-ARM200F, JEOL) equipped with selected-area electron diffraction (SAED) and energy-dispersive X-ray
spectroscopy (EDS). Specific surface areas were determined by N ₂ adsorption–desorption isotherms at 77 K
(BELSORP-max, MicrotracBEL) using the Brunauer–Emmett–Teller (BET) method.




                           HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 12 / 14>

4.3. Electrode fabrication and electrochemical measurements
Working electrodes were prepared by casting a slurry of active HEO powder, conductive carbon, and binder
onto Cu foil current collectors. [공동연구자 확인: 전극 활물질/도전재/바인더의 실제 종류와 질량비, 슬러리
용매, 건조·압연·펀칭 조건, 로딩량, 셀 규격, 상대전극, 분리막, 전해질 및 첨가제의 정확한 조성을 알려 주세요.
예시값을 실제 실험값으로 대체하지 않습니다. 또한 1 C의 기준 전류(mA g⁻¹)와 사용한 정격용량을 확인해 주
세요.] Galvanostatic charge–discharge cycling was performed between 0.005 and 2.5 V (vs. Li/Li ⁺ ) at 0.1 C for
100 cycles, and rate capability was evaluated from 0.1 to 5 C followed by recovery at 0.1 C .
First-lithiation GITT measurements were conducted by applying successive constant-current pulses of 100 mA
g⁻ ¹ for 600 s (corresponding to 16.67 mAh g⁻ ¹ per pulse), each followed by a 3600 s open-circuit rest period
down to the lower cutoff voltage. Voltage transients were recorded at ~1 s intervals for the Mg-free cells and
~3 s intervals for the Mg-containing cells; to ensure rigorous comparability across all four materials,
relaxation metrics were evaluated identically over the common post-interruption window of 3 to 3600 s.

4.4. GITT relaxation and regional-charge analysis
For each GITT relaxation step, the finite-window recovery amplitude was defined as Δ Erest = |E_rest(3600 s) −
E_rest(3 s)|, and the characteristic relaxation time (t₆₃) was determined as the elapsed time at which the
signed voltage recovery reached 1 − e⁻ ¹ (63.212%) of Δ Erest. The potential at the end of the 3600 s rest was
recorded as the quasi-open-circuit voltage (QOCV).
Electrochemical reaction regions (R1–R4) were partitioned solely from inflection landmarks in the t ₆₃ profile:
L1 marks the early post-transient minimum preceding a renewed rise, L3 marks the central minimum
preceding the sustained mid-to-late increase, and L4 marks the late local maximum (in HEO and BM-HEO) or
late slope inflection (in Mg-HEO and BM-Mg-HEO). The resulting cumulative pulse indices (L1/L3/L4) are
6/25/55 for HEO, 9/38/60 for BM-HEO, 7/24/42 for Mg-HEO, and 9/35/46 for BM-Mg-HEO, partitioning
complete lithiation pulses into R1 (pulses 1 to L1), R2 (L1 + 1 to L3), R3 (L3 + 1 to L4), and R4 (L4 + 1 to the final
complete pulse). Boundary-perturbation sensitivity across all 729 (±1 pulse) combinations is documented in
Table S3.
Regional GITT capacities were computed by multiplying the number of complete pulses in each region by
16.6667 mAh g⁻ ¹ per pulse across the 65, 76, 48, and 56 complete first-lithiation pulses of HEO, BM-HEO, Mg-
HEO, and BM-Mg-HEO, respectively (excluding partial cutoff-truncated final pulses; Tables S1–S3).

References
1. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Sui, Y.; Shen, B.; Qi, J.; Wei, F.; Zheng, J. High-entropy oxides as advanced
anode materials for long-life lithium-ion batteries. Nano Energy 2022, 95, 106962.
https://doi.org/10.1016/j.nanoen.2022.106962.
2. Wang, D.; Jiang, S.; Duan, C.; Mao, J.; Dong, Y.; Dong, K.; Wang, Z.; Luo, S.; Liu, Y.; Qi, X. Spinel-structured
high entropy oxide (FeCoNiCrMn)3O4 as anode towards superior lithium storage performance. Journal of
Alloys and Compounds 2020, 844, 156158. https://doi.org/10.1016/j.jallcom.2020.156158.
3. Sarkar, A.; Velasco, L.; Wang, D.; Wang, Q.; Talasila, G.; de Biasi, L.; Kübel, C.; Brezesinski, T.; Bhattacharya, S.
S.; Hahn, H.; Breitung, B. High entropy oxides for reversible energy storage. Nature Communications 2018, 9,
3400. https://doi.org/10.1038/s41467-018-05774-5.
4. Luo, X.-F.; Patra, J.; Chuang, W.-T.; Nguyen, T. X.; Ting, J.-M.; Li, J.; Pao, C.-W.; Chang, J.-K. Charge–Discharge
Mechanism of High-Entropy Co-Free Spinel Oxide Toward Li+ Storage Examined Using Operando Quick-
Scanning        X-Ray       Absorption      Spectroscopy.         Advanced        Science     2022,      9,    2201219.
https://doi.org/10.1002/advs.202201219.




                              HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 13 / 14>

5. Triolo, C.; Maisuradze, M.; Li, M.; Liu, Y.; Ponti, A.; Pagot, G.; Di Noto, V.; Aquilanti, G.; Pinna, N.; Giorgetti,
M.; Santangelo, S. Charge Storage Mechanism in Electrospun Spinel-Structured High-Entropy
(Mn0.2Fe0.2Co0.2Ni0.2Zn0.2)3O4 Oxide Nanofibers as Anode Material for Li-Ion Batteries. Small 2023, 19,
2304585. https://doi.org/10.1002/smll.202304585.
6. He, K.; Zhang, S.; Li, J.; Yu, X.; Meng, Q.; Zhu, Y.; Hu, E.; Sun, K.; Yun, H.; Yang, X.-Q.; Zhu, Y.; Gan, H.; Mo, Y.;
Stach, E. A.; Murray, C. B.; Su, D. Visualizing Non-equilibrium Lithiation of Spinel Oxide via In Situ
Transmission          Electron         Microscopy.        Nature        Communications          2016,       7,      11441.
https://doi.org/10.1038/ncomms11441.
7. Li, K.; Shi, L.; An, J.; Zhang, M.; Du, Y.; Ma, Y.; Lou, S.; Yin, G.; Yu, Z.; Hua, X.; Huo, H. Stabilizing
Configurational Entropy in Spinel-type High Entropy Oxides during Discharge–Charge by Overcoming Kinetic
Sluggish       Diffusion.      Angewandte       Chemie      International      Edition      2025,    64,     e202518569.
https://doi.org/10.1002/anie.202518569.
8. Xiao, B.; Wu, G.; Wang, T.; Wei, Z.; Xie, Z.; Sui, Y.; Qi, J.; Wei, F.; Zhang, X.; Tang, L.-B.; Zheng, J.-C. Enhanced
Li-Ion Diffusion and Cycling Stability of Ni-Free High-Entropy Spinel Oxide Anodes with High-Concentration
Oxygen        Vacancies.        ACS     Applied      Materials       &      Interfaces      2023,     15,      2792–2803.
https://doi.org/10.1021/acsami.2c12374.
9. Ma, G.; Zheng, Y.; Meng, F.; Hu, R. Understanding the lithiation mechanism of Li2O-doped spinel high-
entropy oxides as anode materials for Li-ion batteries. Energy Advances 2023, 2, 1685–1692.
https://doi.org/10.1039/D3YA00326D.
10. Kang, S. D.; Chueh, W. C. Galvanostatic Intermittent Titration Technique Reinvented: Part I. A Critical
Review. Journal of The Electrochemical Society 2021, 168, 120504. https://doi.org/10.1149/1945-7111/ac3940.
11. Zhu, Y.; Wang, C. Galvanostatic Intermittent Titration Technique for Phase-Transformation Electrodes.
Journal of Physical Chemistry C 2010, 114, 2830–2841. https://doi.org/10.1021/jp9113333.
12. Horner, J. S.; Whang, G.; Ashby, D. S.; Kolesnichenko, I. V.; Lambert, T. N.; Dunn, B. S.; Talin, A. A.; Roberts,
S. A. Electrochemical Modeling of GITT Measurements for Improved Solid-State Diffusion Coefficient
Evaluation. ACS Applied Energy Materials 2021, 4, 11460–11469. https://doi.org/10.1021/acsaem.1c02218.
13. Zhai, F.; Zhu, X.; Zhang, W.; Cao, G.; Zhang, H.; Xing, Y.; Xiang, Y.; Zhang, S. Insight of the evolution of
structure and energy storage mechanism of (FeCoNiCrMn)3O4 spinel high entropy oxide in life-cycle span as
lithium-ion        battery        anode.      Journal      of      Power       Sources       2024,      603,      234418.
https://doi.org/10.1016/j.jpowsour.2024.234418.
14. Minouei, H.; Tsvetkov, N.; Kheradmandfard, M.; Han, J.; Kim, D. E.; Hong, S. I. Tuning the electrochemical
performance of high-entropy oxide nanopowder for anode Li-ion storage via structural tailoring. Journal of
Power Sources 2022, 549, 232041. https://doi.org/10.1016/j.jpowsour.2022.232041.
15. Wang, K.; Hua, W.; Huang, X.; Stenzel, D.; Wang, J.; Ding, Z.; Cui, Y.; Wang, Q.; Ehrenberg, H.; Breitung, B.;
Kübel, C.; Mu, X. Synergy of cations in high entropy oxide lithium ion battery anode. Nature Communications
2023, 14, 1487. https://doi.org/10.1038/s41467-023-37034-6.
16. Chen, H.; Qiu, N.; Wu, B.; Yang, Z.; Sun, S.; Wang, Y. A new spinel high-entropy oxide
(Mg0.2Ti0.2Zn0.2Cu0.2Fe0.2)3O4 with fast reaction kinetics and excellent stability as an anode material for
lithium ion batteries. RSC Advances 2020, 10, 9736–9744. https://doi.org/10.1039/D0RA00255K.
17. Qiu, N.; Chen, H.; Yang, Z.; Sun, S.; Wang, Y.; Cui, Y. A high entropy oxide (Mg0.2Co0.2Ni0.2Cu0.2Zn0.2O)
with superior lithium storage performance. Journal of Alloys and Compounds 2019, 777, 767–774.
https://doi.org/10.1016/j.jallcom.2018.11.049.
18. Wang, S.-Y.; Chen, T.-Y.; Kuo, C.-H.; Lin, C.-C.; Huang, S.-C.; Lin, M.-H.; Wang, C.-C.; Chen, H.-Y. Operando
synchrotron transmission X-ray microscopy study on (Mg, Co, Ni, Cu, Zn)O high-entropy oxide anodes for
lithium-ion         batteries.       Materials      Chemistry        and       Physics       2021,      274,       125105.
https://doi.org/10.1016/j.matchemphys.2021.125105.
19. Liu, H.-H.; Yang, J.-L.; Gu, Z.-Y.; Liu, Y.; Wang, X.-T.; Zheng, C.-Y.; Xu, C.; Liu, D.-H.; Guo, W.; Wu, X.-L.
Deciphering Functional Differentiation of Elements in High-Entropy Spinel Oxides as Ultralong-Life Anodes in
Lithium-Ion Batteries. Chemical Science 2026, 17, 6116–6124. https://doi.org/10.1039/D5SC10185A.
20. Li, L.; Jacobs, R.; Gao, P.; Gan, L.; Wang, F.; Morgan, D.; Jin, S. Origins of Large Voltage Hysteresis in High-
Energy-Density Metal Fluoride Lithium-Ion Battery Conversion Electrodes. Journal of the American Chemical
Society 2016, 138, 2838–2848. https://doi.org/10.1021/jacs.6b00061.
21. Jo, H.; Gong, M.; Kim, S. Y.; Seo, D.-H.; Jung, S.-K. Guided phase transition for mitigating voltage hysteresis of
iron fluoride positive electrodes in lithium-ion batteries. Nature Communications 2025, 16, 8596.
https://doi.org/10.1038/s41467-025-63676-9.


                              HEO | Materials-centered manuscript | PI review draft

<PARSED TEXT FOR PAGE: 14 / 14>

22. Knehr, K. W.; Cama, C. A.; Brady, N. W.; Marschilok, A. C.; Takeuchi, K. J.; Takeuchi, E. S.; West, A. C.
Simulations of Lithium-Magnetite Electrodes Incorporating Phase Change. Electrochimica Acta 2017, 238, 384–
396. https://doi.org/10.1016/j.electacta.2017.04.041.
23. Fu, J.; Takai, S.; Yabutsuka, T.; Yao, T. Relaxation Analysis of Silicon Monoxide-Graphite Composite Anode.
Journal of The Electrochemical Society 2024, 171, 020557. https://doi.org/10.1149/1945-7111/ad2956.
24. Skurtveit, A.; North, E. T.; Park, H.; Chernyshov, D.; Wragg, D. S.; Koposov, A. Y. Stepwise Structural
Relaxation      in      Battery   Active      Materials.   ACS     Materials    Letters   2025,   7,   343–349.
https://doi.org/10.1021/acsmaterialslett.4c02058.




                            HEO | Materials-centered manuscript | PI review draft