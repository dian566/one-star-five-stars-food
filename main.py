#!/usr/bin/env python3
"""One Star, Five Stars for the Food — alien tourist review of Earth.

An alien tourist hands planet Earth a one-star review while still
slipping in a real compliment about the food: the locals greet strangers
by discussing the sky's mood, yet the kimchi was so good the visitor
stayed for seconds — and then thirds.

Writes the single entry sentence to /output/entry.txt exactly as-is.
SPDX-License-Identifier: MIT
"""

from pathlib import Path

TEXT = "One star: the locals greet strangers by discussing the sky's mood, yet the kimchi was so good I stayed for seconds — and then thirds."

MAX_CHARS = 200


def validate(text):
    """The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    if text.count(".") + text.count("!") + text.count("?") < 1:
        raise ValueError("entry must be a sentence")
    return text


def run():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(TEXT), encoding="utf-8")


if __name__ == "__main__":  # entry point
    run()
