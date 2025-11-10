# Memetic Verification Criteria (M-VTE Stop Condition)

Community verification is reached at the first instant that ALL of the following are true:

## 1) Effect Direction Consistency

≥ 70% of participants show ΔEnergy_post − ΔEnergy_pre ≥ +10 (0–100 scale) within 24 hours of a logged deletion event.

## 2) Replication Count

≥ 150 independent participants across ≥ 3 cities have completed at least one valid deletion event with pre-post measures.

## 3) Sensor Corroboration (Quantified Nodes)

Among participants who shared wearable data (target n ≥ 50), ≥ 60% show either:

- HRV RMSSD increase ≥ +5 ms within 24 h of the deletion event, OR
- Sleep efficiency increase ≥ +2 percentage points on the first sleep episode after the event.

## 4) Curator Audit

Two independent curators sign the audit checklist (see `curation/audit.md`) confirming:

- prereg inclusion/exclusion rules applied,
- outlier handling as declared,
- de-identified data + code reproduce the reported numbers.

## Timer

The M-VTE clock starts at the shared Hypothesis Lock (tag: `v1.0-lock`) and stops at the earliest timestamp when all four conditions are satisfied.

