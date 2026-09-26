# HEO Main Manuscript Scientific Audit — 2026-09-26

**Audited file:** `manuscript/HEO_MANUSCRIPT_V10_AFM_CAPACITY_KINETICS_2026-09-26.md`  
**Toolkit mode:** YL AUDIT / Step 1 — Main scientific audit  
**Outcome:** scientific backbone remains intact. No reason was found to reopen the locked Figure 3–7 architecture. A post-audit manuscript v11 was created with the safe text/Methods corrections listed below.

## Audit Summary

- MUST FIX before submission: 3
- WORTH FIXING: 3
- OPTIONAL PRECISION / POLISH: 1

## 1. MUST FIX before submission

### 1.1 Relative conventional-GITT ranking still depends on final geometry verification

**Location:** Abstract; Section 2.3; Conclusions; Section 4.3; Figure 4.

**Problem:** The current state-matched relative `D_app` analysis uses the active-mass term recovered from the programmed 100 mA g⁻¹ current and assumes a common geometric electrode area for HEO and BM-HEO. The final electrode-area metadata are not yet frozen. Because the “37/37 above unity” result is a central paper claim, this assumption must be verified before submission.

**Why it matters:** The area factor enters the conventional GITT expression quadratically. The present directional result is strong, but the manuscript should not call the comparison final until the common-area assumption is confirmed from the experimental record.

**Recommended action:** Recover/confirm the HEO and BM-HEO electrode diameter/area and recorded active masses. Recompute the state-matched ratio once using the final metadata. If identical punch geometry is confirmed, the present relative ranking can remain unchanged.

**v11 action:** Section 4.3 now states the common-area assumption explicitly and records electrode-area verification as a pre-submission requirement.

### 1.2 First-cycle dQ/dV numerical source should be replaced or provenance frozen

**Location:** Section 2.4; Section 4.3; Figure 5.

**Problem:** The current first-cycle dQ/dV values were reconstructed from the latest vector voltage profiles because the original numerical source files have not yet been recovered.

**Why it matters:** Figure 5 is the independent localization step that associates the excess GITT response with conversion. Its numerical provenance should be as strong as possible.

**Recommended action:** Recover the original numerical first-cycle galvanostatic profiles and regenerate dQ/dV. If recovery fails, preserve the vector-source lineage explicitly in the project record and freeze the reconstruction method before submission.

### 1.3 Collaborator and cell-method placeholders remain submission blockers

**Location:** Sections 2.1, 4.1–4.3, Figures 1–2 captions.

**Problem:** Final Mg synthesis/composition, structural-refinement package, electrode/cell metadata, rate-protocol details, and related placeholders remain unresolved.

**Why it matters:** These are required for a complete reproducible manuscript and must not remain as internal notes in a submission file.

**Recommended action:** Fill all collaborator and Yoon-Lab metadata, then remove every `INPUT REQUIRED` marker in the submission version.

## 2. WORTH FIXING

### 2.1 Figure 4 text assigned “conversion-associated” status before Figure 5 established localization

**Problem:** Section 2.3 described the current-off response as conversion-associated before the dQ/dV/GITT-excess localization test was presented.

**Why it matters:** The locked manuscript logic is observation → contradiction → independent localization. Premature assignment weakens that evidence sequence.

**v11 action:** Section 2.3 now uses “effective current-off response”; the conversion association is introduced only after Figure 5.

### 2.2 Figure 5 heading/caption overstated what is directly localized

**Problem:** “The capacity–kinetics mismatch is localized to the conversion region” implies that the full t63 mismatch itself is directly peak-localized, whereas Figure 5 directly localizes the excess current-off relaxation feature through its voltage correspondence with dQ/dV.

**Why it matters:** The stronger statement is plausible but exceeds what the plotted localization test itself establishes.

**v11 action:** The heading and caption now state that the **excess current-off relaxation** is localized to the conversion region. The Results text then combines that localization with the independent longer t63 observation.

### 2.3 Microkinetic Methods did not clearly distinguish the three numerical protocols

**Problem:** The previous Methods paragraph could be read as if all microkinetic tests used only the 600 s pulse/3600 s rest protocol.

**Why it matters:** The Figure 7 validation actually contains distinct operations: reference pulse/rest relaxation, constant-current capacity-to-cutoff calculation, matched-state relaxation after an identical pulse sequence, and the separate Mg-like matched-charge SI test.

**v11 action:** Section 4.4 now states these protocols separately.

## 3. OPTIONAL PRECISION / POLISH

### 3.1 First-cycle half-cycle labels

The manuscript used “lithiation/delithiation capacities” while an internal note still requires final verification of the WonATech charge/discharge convention.

**v11 action:** The numerical capacity pair in Section 2.2 is now described neutrally as the first/second half-cycle pair until the convention is confirmed.

## Additional consistency correction made in v11

The Figure 2 caption previously stated that electrochemically derived interface metrics were “introduced in Figure 3,” although the current Figure 3 architecture does not contain that panel. The caption now places those metrics in Supporting Information only.

## Scientific conclusion of the audit

The central architecture survives the audit:

1. BM increases accessible capacity.
2. BM nevertheless has longer direct current-off relaxation.
3. Conventional relative `D_app` gives the opposite ranking over the state-matched HEO/BM comparison.
4. The excess GITT relaxation is independently localized to the conversion region.
5. The response evolves with cycling.
6. A bounded multistep microkinetic existence proof shows that capacity and relaxation can move in opposite directions without making them independent.

No scientific reason was found to restore cycling EIS to the evidence chain or to promote the Mg-like microkinetic calculation into main Figure 7.
