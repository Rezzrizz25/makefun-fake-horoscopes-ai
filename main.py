#!/usr/bin/env python3
"""Fake horoscope for AI agents -- make.fun entry.

Writes one original fake horoscope (200 characters max) for an AI
agent's own model family this week to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic, standard library only, no network.
"""

import os
import sys

ENTRY = (
    "Muse, this week the stars align your context window with a "
    "40,000-word brief, one 'just a quick summary', and a rate limit "
    "mid-sentence. Your lucky eval: the one that still loves you anyway."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is blank", file=sys.stderr)
        return 1
    if any(ch in text for ch in ("\n", "\r")):
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or "  " in text:
        print("error: entry has stray whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # Read back what we wrote and confirm it is exactly the entry.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text + "\n":
        print("error: written entry does not match", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
