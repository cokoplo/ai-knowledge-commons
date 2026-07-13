#!/usr/bin/env python3
"""Build a glossary of key terms from the content/ articles.

This is a small, dependency-free open-source utility maintained by
AI Knowledge Commons. It scans every Markdown file under ``content/`` for
glossary entries written in the form::

    **Term** - definition text
    **Term** — definition text
    **Term**: definition text

and prints a Markdown glossary to standard output. It is intentionally simple so
that it runs anywhere (including our CI) without third-party packages.

Usage:
    python tools/build_glossary.py
    python tools/build_glossary.py --write docs/GLOSSARY.md
"""

import argparse
import os
import re
import sys

# Ensure UTF-8 output so definitions with non-ASCII text print correctly on
# Windows terminals that default to a non-UTF-8 codec.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content")

# Matches: **Term** followed by " - ", " — ", or ": " and then a definition.
ENTRY_RE = re.compile(r"^\*\*([^*]+?)\*\*\s*(?:[-—:]\s*)(.+)$")

# Lines we never want to treat as glossary entries.
SKIP_TERMS = {"note", "example", "important", "warning", "tip"}


def iter_entries():
    if not os.path.isdir(CONTENT_DIR):
        return
    for name in sorted(os.listdir(CONTENT_DIR)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(CONTENT_DIR, name)
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = ENTRY_RE.match(line.strip())
                if not m:
                    continue
                term = m.group(1).strip()
                definition = m.group(2).strip()
                if term.lower() in SKIP_TERMS:
                    continue
                yield term, definition


def build_glossary():
    entries = {}
    order = []
    for term, definition in iter_entries():
        if term not in entries:
            order.append(term)
        entries[term] = definition
    return order, entries


def render_markdown(order, entries):
    lines = ["# Glossary", "", "Key terms from the AI Knowledge Commons materials.", ""]
    for term in order:
        lines.append(f"- **{term}** — {entries[term]}")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Build a glossary from content/.")
    parser.add_argument(
        "--write",
        metavar="FILE",
        help="Write the glossary to FILE instead of printing to stdout.",
    )
    args = parser.parse_args()

    order, entries = build_glossary()
    if not order:
        print("No glossary entries found in content/.", file=sys.stderr)
        return 1

    markdown = render_markdown(order, entries)

    if args.write:
        out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), args.write)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(markdown)
        print(f"Wrote {len(order)} terms to {args.write}")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
