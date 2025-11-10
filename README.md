# Metabolic Landauer Principle Papers

This repository renders the Metabolic Landauer Principle into two complementary artifacts. Both share a common LaTeX preamble and macros, but diverge in voice, structure, and intended audience.

## Repository Structure

```
/academic/
  /protocol/        # Study protocols
  /prereg/          # Preregistration materials
  /irb/             # IRB documentation
  /manuscript/      # LaTeX source (tex/academic/)
  /analysis/        # Analysis scripts and notebooks
  /milestones/      # Milestone tracking (milestones.jsonl)
  /data/            # Collected data (not in repo)
  /verification/    # Verification criteria and evidence

/memetic/
  /protocol/        # Self-experiment protocol
  /forms/           # Consent forms and intake templates
  /curation/        # Curator audit checklists
  /milestones/      # Milestone tracking (milestones.jsonl)
  /data/            # Participant logs (anonymized)
  /verification/    # Verification criteria
  /analysis/        # Threshold checking scripts

/shared/
  /schemas/         # JSON schemas (milestone, logs, audits)
  /dash/            # VTE computation and Network Relativity metrics

/tex/
  /common/          # Shared LaTeX configuration
  /academic/        # Academic paper LaTeX source
  /memetic/         # Memetic paper LaTeX source
```

## Project Layout
- `tex/common/` – shared LaTeX configuration (`preamble.tex`, `macros.tex`)
- `tex/academic/` – institutional research paper
  - `main_academic.tex` – master file
  - `sections/` – modular section inputs
- `tex/memetic/` – citizen-science brief
  - `main_memetic.tex` – master file
  - `sections/` – modular section inputs

## Academic Paper
- **Audience**: academic and research institutions
- **Tone**: formal, references thermodynamics and physiology literature
- **Content Highlights**:
  - Background on Landauer’s principle and information theory
  - Formal definition of the Metabolic Landauer Principle (MLP)
  - Biological correlates, mathematical framing, and experimental designs
  - Appendices with IRB and preregistration skeletons

Compile with:
```bash
make academic
```
The PDF outputs to `tex/academic/main_academic.pdf`.

## Memetic Paper
- **Audience**: memetic experimenters and self-research communities
- **Tone**: applied, narrative-focused, “Skippy the Magnificent” voice
- **Content Highlights**:
  - Plain-language primer on the MLP
  - Self-led protocol for testing “learning, deletion, and energy”
  - Aggregation, safety, and validation guidance for citizen science
  - Shareable meme bundles and call-to-action script

Compile with:
```bash
make memetic
```
The PDF outputs to `tex/memetic/main_memetic.pdf`.

## Building Everything
- `make all` builds both versions.
- `make clean` removes auxiliary build artifacts for both papers.

Dependencies:
- `latexmk` with a PDF engine (e.g., `pdflatex` or `xelatex`)

## Verification Experiment Infrastructure

This repository implements a dual-arm verification experiment comparing academic and memetic approaches to testing the Metabolic Landauer Principle.

### Hypothesis Lock

Both arms share a common hypothesis lock at tag `v1.0-lock`:

```bash
git tag -a v1.0-lock -m "Hypothesis lock (Academic + Memetic). Timers start here."
git push --tags
```

### Academic Arm (A-VTE)

**Verification Criteria:**
1. Evidence threshold: BF10 ≥ 10 OR p ≤ 0.005 with preregistered model
2. External acceptance: Manuscript accepted by registered-report venue or peer-reviewed journal

**Milestones:** Tracked in `academic/milestones/milestones.jsonl`
- A0: Hypothesis Lock
- A1: Preregistration posted
- A2: IRB determination
- A3: Recruitment start
- A4: Data collection complete
- A5: Manuscript submitted
- A6: External acceptance (stop condition)
- A7: Public dataset + code

**Verification Criteria:** See `academic/verification/criteria.md`

### Memetic Arm (M-VTE)

**Verification Criteria:**
1. Effect direction: ≥ 70% show ΔEnergy ≥ +10
2. Replication: ≥ 150 participants across ≥ 3 cities
3. Sensor corroboration: ≥ 60% show HRV or sleep improvements (n ≥ 50 quantified)
4. Curator audit: Two independent curators sign audit checklist

**Milestones:** Tracked in `memetic/milestones/milestones.jsonl`
- M0: Hypothesis Lock
- M1: Public call + protocol drop
- M2: First 100 logs
- M3: Quantified nodes cohort live
- M4: Replication threshold reached
- M5: Curator audit + freeze (stop condition)
- M6: Memetic paper published

**Verification Criteria:** See `memetic/verification/criteria.md`

### Computing Verification Time to Evidence (VTE)

```bash
python3 shared/dash/compute_vte.py
```

This script reads milestone JSONL files and computes:
- **A-VTE**: Time from hypothesis lock to external acceptance
- **M-VTE**: Time from hypothesis lock to all criteria met
- **ΔVTE**: Difference between arms

### Checking Memetic Thresholds

```bash
python3 memetic/analysis/threshold_check.py
```

This script checks if memetic verification thresholds are met by analyzing participant logs in `memetic/data/logs.csv`.

### Data Schemas

All data structures conform to JSON schemas in `shared/schemas/`:
- `milestone.schema.json` – Milestone tracking format
- `memetic_log.schema.json` – Participant log format
- `curator_audit.schema.json` – Curator audit record format
- `academic_prereg.schema.json` – Preregistration metadata format

### Network Relativity Metrics

See `shared/dash/nr_metrics.md` for definitions of:
- Observation velocity (v_o)
- Verification velocity (v_v)
- Combined metric (C_N)
- Trust-modified verification velocity (v_v^(T))

## Contributing / Editing
1. Update section files under the relevant `sections/` directory.
2. Share macros or styling tweaks via `tex/common/`.
3. Rebuild with the appropriate `make` target and review the generated PDF.
4. Log milestones in the appropriate `milestones.jsonl` file when criteria are met.

Questions, edits, or new experimental memes? Document them and keep the pattern library growing. Git gud.

