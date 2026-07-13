# AI Knowledge Commons

> Free, open-source educational resources for public AI literacy.

**AI Knowledge Commons** is an independent, non-commercial initiative dedicated to
open-source technology research and public AI literacy education. We break down
complex technical concepts into free, accessible, and openly licensed materials
for learners worldwide.

## Mission

We believe that understanding artificial intelligence is a public good. Our
mission is to lower the barrier to AI literacy by publishing clear, accurate, and
up-to-date educational materials under open-source licenses, so that anyone —
regardless of background — can learn how modern AI systems work and how to use
them responsibly.

## What We Do

- **Open educational content.** We publish plain-language explainers on AI
  fundamentals, large language models, and responsible use (`content/`).
- **Open-source research.** We maintain curated, cited notes and reproducible
  examples that anyone can review and improve.
- **Open tooling.** We ship small, dependency-free utilities (`tools/`) that
  support self-guided learning.
- **Community contribution.** All materials are open for public contribution
  under an open-source license.

## Why It Matters

The gap between how fast AI is evolving and how well the public understands it is
widening. We exist to close that gap with free, neutral, and accessible knowledge.

## Repository Structure

```
content/      Educational explainers (Markdown)
tools/        Small open-source utilities that support learning
resources/    Curated list of free learning resources
```

## Getting Started

Browse `content/` to start learning. Each topic is a self-contained Markdown file.
You can also run the bundled explainer:

```bash
python tools/explain_concept.py            # list available topics
python tools/explain_concept.py 01-what-is-ai.md
```

## Contributing

We welcome contributions of all sizes. Please read `CONTRIBUTING.md` and our
`CODE_OF_CONDUCT.md` first.

## License

All code in this repository is released under the [MIT License](LICENSE).
Educational text is additionally available under CC BY 4.0 where noted in the
individual file header.

## Contact

Questions, corrections, and suggestions are welcome as issues or discussions.
