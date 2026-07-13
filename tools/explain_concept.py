#!/usr/bin/env python3
"""AI Knowledge Commons — concept explainer.

A tiny, dependency-free open-source utility that prints a short explanation of
an AI concept from the project's `content/` folder. It demonstrates the
project's commitment to simple, reproducible, openly licensed tooling that
anyone can run without installing anything.

Usage:
    python tools/explain_concept.py                # list available topics
    python tools/explain_concept.py 01-what-is-ai.md
"""

import argparse
import os
import sys

# Ensure UTF-8 output so content with non-ASCII characters (e.g. ►) prints
# correctly on Windows terminals that default to a non-UTF-8 codec.
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content")


def list_concepts():
    if not os.path.isdir(CONTENT_DIR):
        return []
    return sorted(f for f in os.listdir(CONTENT_DIR) if f.endswith(".md"))


def explain(concept):
    path = os.path.join(CONTENT_DIR, concept)
    if not os.path.isfile(path):
        available = ", ".join(list_concepts()) or "(none)"
        print(f"Concept '{concept}' not found. Available: {available}")
        return 1
    with open(path, encoding="utf-8") as fh:
        print(fh.read())
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Print an AI concept explainer from the content/ folder."
    )
    parser.add_argument(
        "concept",
        nargs="?",
        help="Concept filename, e.g. 01-what-is-ai.md",
    )
    args = parser.parse_args(argv)

    if not args.concept:
        concepts = list_concepts()
        if not concepts:
            print("No concepts found in content/.")
            return 0
        print("Available concepts:")
        for c in concepts:
            print(f"  - {c}")
        return 0

    return explain(args.concept)


if __name__ == "__main__":
    sys.exit(main())
