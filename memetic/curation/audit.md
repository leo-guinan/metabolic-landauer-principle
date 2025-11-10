# Curator Audit Checklist

## Pre-Audit Requirements

- [ ] Dataset hash matches release artifact
- [ ] Analysis script hash matches release artifact
- [ ] All raw data files present and accessible

## Inclusion/Exclusion Verification

- [ ] Inclusion/exclusion rules applied exactly as preregistered
- [ ] Document any deviations with justification
- [ ] Count of excluded participants: ___
- [ ] Count of included participants: ___

## Outlier Handling

- [ ] Outlier handling per prereg (list rule + counts)
- [ ] Outlier rule applied: ___
- [ ] Number of outliers removed: ___
- [ ] Number of outliers winsorized: ___

## Reproduction Check

Running the provided script yields the reported:

- [ ] n participants: ___
- [ ] n cities: ___
- [ ] n quantified nodes: ___
- [ ] effect_direction_pct (≥ 70%): ___%
- [ ] sensor_corrob_pct (≥ 60%): ___%

## Data Integrity

- [ ] All participant IDs are pseudonymous
- [ ] No personally identifiable information in dataset
- [ ] Consent timestamps verified
- [ ] Deletion timestamps within valid range

## Curator Signatures

- [ ] Curator 1 signature (PGP or typed + key id): ___
- [ ] Curator 2 signature (PGP or typed + key id): ___
- [ ] Both curators agree on all checks above

## Freeze Confirmation

- [ ] Data archived at write-once location: ___
- [ ] Code archived at write-once location: ___
- [ ] Archive hashes recorded: ___
- [ ] No further modifications to frozen dataset

## Notes

_Additional observations or concerns:_

