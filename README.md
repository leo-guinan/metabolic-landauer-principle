# Metabolic Landauer Principle Papers

This repository renders the Metabolic Landauer Principle into two complementary artifacts. Both share a common LaTeX preamble and macros, but diverge in voice, structure, and intended audience.

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

## Contributing / Editing
1. Update section files under the relevant `sections/` directory.
2. Share macros or styling tweaks via `tex/common/`.
3. Rebuild with the appropriate `make` target and review the generated PDF.

Questions, edits, or new experimental memes? Document them and keep the pattern library growing. Git gud.

