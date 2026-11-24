#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — a make.fun entry.

Writes one haiku about debugging to /output/entry.txt, the file the
grader reads: three lines in the 5-7-5 syllable shape, seventeen
syllables in all. Standard library only, no network, and the output
is byte-identical on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The approved line, laid out at its own 5-7-5 syllable boundaries:
#   The(1) bug(2) was(3) in(4) line(5)
#   nine(1) all(2) this(3) time(4) it(5) just(6) sat(7)
#   there(1) smil-ing(2-3) at(4) me(5)
LINES = (
    "The bug was in line",
    "nine all this time; it just sat",
    "there smiling at me.",
)


def main() -> None:
    text = "\n".join(LINES)
    # The gate takes UTF-8 text of 1 to 200 characters, not only white
    # space; fail loudly here rather than hand the grader a bad file.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise SystemExit(f"entry text fails the gate: {len(text)} chars")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
