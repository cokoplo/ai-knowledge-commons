# Roadmap

*AI Knowledge Commons — public roadmap (living document)*

This roadmap is intentionally public so that contributors and fiscal sponsors can
see where the project is headed. It is non-binding and updated as we learn.

## What we have shipped

- ✅ Core AI-literacy explainers: what AI is, how LLMs work, AI literacy and
  ethics.
- ✅ Practical guides: spotting AI-generated content, responsible use, and open
  models.
- ✅ Initial personal knowledge OS positioning for unifying chat logs,
  developer tools, and second-brain notes.
- ✅ Public glossary and generated `docs/GLOSSARY.md`.
- ✅ Open-source tooling: `explain_concept.py` and `build_glossary.py` (no
  dependencies).
- ✅ Automated checks (CI) that run our tools on every push.

## Near term

- [ ] Define an open context-pack format for AI chat logs, coding-agent sessions,
  commits, issues, and Markdown notes.
- [ ] Draft a privacy and provenance model for user-owned AI memory.
- [ ] Add import/export examples for common second-brain workflows such as
  Markdown folders, backlinks, tags, and reading notes.
- [ ] Create a small local prototype that indexes the repository's Markdown
  materials and generates a reviewable context brief.
- [ ] Continue translations of the core materials, starting with Chinese and
  Spanish.

## Longer term

- [ ] Browser-based explorer for a local personal knowledge archive.
- [ ] Connectors for exported chat logs, repositories, issue trackers, and note
  systems.
- [ ] Knowledge graph views that show how chats, code, notes, and decisions
  connect.
- [ ] Evaluation recipes for checking whether generated summaries preserve
  provenance and avoid leaking sensitive context.
- [ ] Contributor onboarding path for first-time open-source participants.

## How to influence this

Open an issue or discussion. Because all materials are openly licensed, anyone
can propose additions, examples, or workflows — that is the point of the project.

## Principles that guide priorities

1. **User control first.** Personal AI memory should be owned, inspectable, and
   portable by default.
2. **Privacy before convenience.** Context import and AI sharing must be explicit
   and reviewable.
3. **Open by default.** Code, text, formats, and tooling stay openly licensed
   and runnable.
4. **Accuracy over hype.** We would rather say "we don't know" than overclaim.
