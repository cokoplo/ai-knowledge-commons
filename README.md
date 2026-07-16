# AI Knowledge Commons

> An AI-driven personal knowledge OS that unifies your chat logs, developer
> tools, and second brain.

**AI Knowledge Commons** is an independent, non-commercial **public-interest
technology** project for building an open, user-controlled personal knowledge
operating system. It turns scattered AI chats, coding sessions, issue threads,
notes, and research clips into searchable, reusable context for people and the AI
tools they choose to use.

The goal is simple: your working memory should be portable, inspectable, and
useful across tools instead of being locked inside one chat app, editor, or note
system.

## Mission

We believe personal AI memory should belong to the person who created it. Our
mission is to help people collect, understand, and reuse their own knowledge
across chat logs, developer tools, and second-brain systems while preserving
privacy, attribution, and control.

This repository is the open foundation for that work: product notes, educational
explainers, shared vocabulary, and small dependency-free utilities that make the
ideas easy to inspect and improve.

## What We Do

- **Personal knowledge OS design.** We document how an AI-assisted knowledge
  layer can unify chat logs, repositories, notes, bookmarks, and tool output
  without trapping users in one vendor.
- **Context and memory workflows.** We define practical patterns for turning
  messy transcripts, commits, issues, and notes into context packs that people
  and AI agents can reuse.
- **AI literacy for builders and users.** We keep plain-language explainers on
  LLMs, responsible AI use, open models, and AI-generated content so the system
  remains understandable instead of magical.
- **Open learning utilities.** We ship small, dependency-free Python utilities
  (`tools/`) that support self-guided learning and are run automatically on every
  push.
- **Community contribution.** All project materials are open for review and
  improvement under open licenses.

## Why It Matters

Modern knowledge work is fragmented. A useful answer may depend on a ChatGPT
thread, a Codex session, a Git commit, a design note, a bug report, and a private
Markdown file. Today those records usually live in separate silos.

An AI-driven personal knowledge OS gives the user a stable layer above those
tools: one place to preserve provenance, search across work history, prepare
context for AI assistants, and decide what should or should not be shared.

## Project Tracks

Start here if you want the product direction:

1. `07-personal-knowledge-os.md` — the core concept for unifying chat logs,
   developer tools, and second-brain notes
2. `glossary.md` — shared vocabulary used across the project

The AI-literacy foundation remains useful because a personal knowledge OS needs
users to understand what AI can and cannot safely do:

1. `01-what-is-ai.md` — what AI is, and what it is not
2. `02-how-large-language-models-work.md` — how LLMs are built and trained
3. `03-ai-literacy-and-ethics.md` — thinking critically and ethically about AI
4. `04-spotting-ai-generated-content.md` — tells and habits for the wild
5. `05-responsible-use-of-ai-tools.md` — practical, safe everyday habits
6. `06-open-weights-and-open-models.md` — what "open" means and why it matters

A generated, single-page version of the vocabulary lives at `docs/GLOSSARY.md`.

## 中文内容（Chinese）

Chinese versions of the core explainers and the personal knowledge OS concept
are available under [`content/zh/`](content/zh/). The Chinese materials keep the
project accessible to a wider, Chinese-reading audience as the product direction
evolves.

## Repository Structure

```
content/        Product notes and educational explainers, including glossary.md
content/zh/     Chinese versions of the project materials
tools/          Small open-source utilities that support learning
resources/      Curated list of free learning resources
docs/           ROADMAP.md and the generated GLOSSARY.md
.github/        CI workflow that runs the tools on every push
```

## Getting Started

Browse `content/` to understand the project direction. Each topic is a
self-contained Markdown file. You can also run the bundled open-source tools
locally:

```bash
python tools/explain_concept.py
python tools/explain_concept.py 07-personal-knowledge-os.md
python tools/build_glossary.py
python tools/build_glossary.py --write docs/GLOSSARY.md
```

All tools are dependency-free and run on Python 3.8+.

## Design Targets

The personal knowledge OS is intended to connect three kinds of user-owned
context:

- **Chat logs:** AI conversations, prompt history, summaries, decisions, and
  follow-up tasks.
- **Developer tools:** repositories, commits, issues, pull requests, terminal
  logs, test output, documentation, and coding-agent sessions.
- **Second brain systems:** Markdown notes, bookmarks, reading highlights,
  personal knowledge bases, tags, and backlinks.

The expected output is not just search. The system should produce reviewable
context packs, timelines, glossaries, briefs, and retrieval indexes that make a
person's own knowledge easier to use with AI.

## Privacy Principles

This project does not operate a hosted data service. Future tools and prototypes
should be designed around these principles:

- User-owned archives before vendor-owned memory.
- Local-first processing where practical.
- Clear provenance for every imported item and generated summary.
- Reversible imports and exports using open formats.
- Explicit review before sensitive context is shared with any AI model.

## Automated Checks

Every push runs a CI workflow (`.github/workflows/ci.yml`) that executes both
tools, so the repository's utilities are verified to keep working as content
grows.

## Contributing

We welcome contributions of all sizes. Please read `CONTRIBUTING.md` and our
`CODE_OF_CONDUCT.md` first. See `docs/ROADMAP.md` for where the project is
headed.

## License

All code in this repository is released under the [MIT License](LICENSE).
Educational and product text is additionally available under CC BY 4.0 where
noted in the individual file header.

## Contact

Questions, corrections, and suggestions are welcome as issues or discussions.
