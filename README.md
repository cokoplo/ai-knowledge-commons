# AI Knowledge Commons

> Free, public-interest AI literacy education for the public.

**AI Knowledge Commons** is an independent, non-commercial **public-interest
technology education** initiative. We close the digital divide in understanding
artificial intelligence by turning complex, fast-moving technical concepts into free,
accessible, and openly licensed materials for learners worldwide — grounded in
human-centered, public-interest values.

## Mission

We believe that understanding artificial intelligence is a public good. Our
mission is to lower the barrier to AI literacy by publishing clear, accurate, and
up-to-date educational materials under open-source licenses, so that anyone —
regardless of background — can learn how modern AI systems work and how to use
them responsibly.

## What We Do

- **Public AI-literacy education.** We publish plain-language explainers on AI
  fundamentals, large language models, spotting AI-generated content, responsible
  use, and open models (`content/`).
- **Cited educational research.** We maintain curated, cited notes and a public
  glossary that anyone can review and improve.
- **Open learning utilities.** We ship small, dependency-free Python utilities
  (`tools/`) that support self-guided learning and are run automatically on every
  push (CI) — open licensing here is a means to public access.
- **Community contribution.** All materials are open for public contribution under
  open, non-commercial licenses.

## Why It Matters

The gap between how fast AI is evolving and how well the public understands it is
widening. We exist to close that gap with free, neutral, and accessible knowledge.

## Learning Path

Start with the explainers in `content/`, in this order:

1. `01-what-is-ai.md` — what AI is, and what it is not
2. `02-how-large-language-models-work.md` — how LLMs are built and trained
3. `03-ai-literacy-and-ethics.md` — thinking critically and ethically about AI
4. `04-spotting-ai-generated-content.md` — tells and habits for the wild
5. `05-responsible-use-of-ai-tools.md` — practical, safe everyday habits
6. `06-open-weights-and-open-models.md` — what "open" means and why it matters
7. `glossary.md` — the shared vocabulary used across all materials

A generated, single-page version of the vocabulary lives at `docs/GLOSSARY.md`.

## 中文内容（Chinese）

All explainers above are also available in Chinese under [`content/zh/`](content/zh/),
mirroring the English topics. This keeps the materials accessible to a wider,
Chinese-reading audience.

## Repository Structure

```
content/        Educational explainers (Markdown), including glossary.md
content/zh/     Chinese versions of the explainers
tools/          Small open-source utilities that support learning
resources/      Curated list of free learning resources
docs/           ROADMAP.md and the generated GLOSSARY.md
.github/        CI workflow that runs the tools on every push
```

## Getting Started

Browse `content/` to start learning. Each topic is a self-contained Markdown file.
You can also run the bundled open-source tools locally:

```bash
python tools/explain_concept.py                 # list available topics
python tools/explain_concept.py 01-what-is-ai.md
python tools/build_glossary.py                  # print the glossary
python tools/build_glossary.py --write docs/GLOSSARY.md
```

All tools are dependency-free and run on Python 3.8+.

## Automated Checks

Every push runs a CI workflow (`.github/workflows/ci.yml`) that executes both
tools, so the repository's utilities are verified to keep working as content grows.

## Contributing

We welcome contributions of all sizes. Please read `CONTRIBUTING.md` and our
`CODE_OF_CONDUCT.md` first. See `docs/ROADMAP.md` for where the project is headed.

## License

All code in this repository is released under the [MIT License](LICENSE).
Educational text is additionally available under CC BY 4.0 where noted in the
individual file header.

## Contact

Questions, corrections, and suggestions are welcome as issues or discussions.
