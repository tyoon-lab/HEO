# HEO Project

## Start here

This repository is maintained so a new chat/session can resume **without a separate handoff message**.

Read first:

`START_HERE_CURRENT_STATE_2026-10-03.md`

That file is the single authoritative current-state entry point.

## Current paper direction

Working target: **Advanced Functional Materials (AFM)**.

The former working title centered on a capacity–kinetics mismatch and is now under revision.

### Latest scientific pivot

The paper no longer treats accessible capacity as a direct conversion-kinetic speed coordinate.

Current central question:

> **Does conversion-region polarization magnitude track the timescale of post-interruption relaxation?**

Raw GITT analysis shows that the two responses do not move along one universal fast–slow axis.

Read:

- `manuscript/HEO_POLARIZATION_T63_PIVOT_LOCK_2026-10-03.md`
- `modeling/HEO_CONVERSION_POLARIZATION_T63_AUDIT_2026-10-03.md`
- `modeling/HEO_CONVERSION_POLARIZATION_T63_SUMMARY_2026-10-03.csv`

## Current scientific chain

Figure 1–2: materials structure/composition/morphology  
→ Figure 3: electrochemical capacity/performance as outcomes only  
→ Figure 4: direct conversion-region polarization and t63 comparison  
→ Figure 5: localization of the polarization/recovery feature to the conversion region  
→ Figure 6: **reopened; experimental cycle-history robustness is now preferred over the former capacity-based microkinetic model**

## Locked first-cycle result

Over z = 0.40–0.90:

| Sample | Delta E_pol,60 (mV) | t63 (min) |
|---|---:|---:|
| HEO | 195.9 | 10.37 |
| BM-HEO | 182.6 | 13.02 |
| Mg-HEO | 126.4 | 10.53 |
| BM-Mg-HEO | 148.2 | 12.70 |

Key contrasts:

- HEO -> BM: polarization slightly down, t63 up;
- HEO -> Mg: polarization strongly down, t63 nearly unchanged;
- Mg -> BM-Mg: polarization up, t63 up.

Safe central statement:

**Material modification changes conversion-region polarization magnitude and post-interruption relaxation timescale in distinct ways; the two responses do not collapse onto one material-independent kinetic fast–slow coordinate.**

## Capacity boundary

Capacity remains an important performance outcome.

Do not claim:
- larger capacity proves faster conversion kinetics;
- terminal polarization determines the capacity ordering;
- the old Q-based R2/R3 model explains the experimental capacity difference.

## Figure 5 localization

Using the same background protocol, the conversion-associated polarization-excess peak remains within about 32 mV of the corresponding cathodic dQ/dV peak for all four materials.

Thus the conversion-localization result survives the new polarization definition.

## Model / Dapp status

- Former Q-based four-step model: historical/optional SI, not current Main endpoint.
- Conventional Dapp disagreement: still valid, but secondary; Main vs SI placement remains open.

## Manuscript authorities

The existing text authorities remain:

- `manuscript/HEO_MANUSCRIPT_V17_PI_COMMENTS_INTEGRATED_2026-09-30.md`
- `manuscript/HEO_SUPPORTING_INFORMATION_V14_MAIN_V17_ALIGNED_2026-09-30.md`

They have **not yet been rewritten** after the latest pivot.

## Immediate next task

1. freeze the new Figure 4 polarization–t63 architecture;
2. update Figure 5 quantity/wording if needed;
3. test cycle-history data as the new Figure 6;
4. decide Main vs SI placement of conventional Dapp;
5. only then revise manuscript prose globally.

Do not restart from older model states unless auditing history.
