#!/usr/bin/env python3
"""Two Lines to Your Past Self entry for make.fun.

Writes one original two-line warning to a past self to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

TEXT = (
    "Don't eat the last slice of pizza at 2 a.m. on 14 March 2019 in Tom's "
    "kitchen \u2014 put it back in the box and go to bed.\n"
    "That slice gave you food poisoning on the morning of your first proper "
    "job interview, and missing it is why you ended up in the career you "
    "actually liked."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read back and verify the written bytes match exactly, and that the
    # entry stays inside the competition gate of 1-280 characters.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == TEXT, "entry.txt bytes differ from TEXT"
    assert 1 <= len(written) <= 280, "entry.txt must be 1-280 characters"
    assert written.count("\n") == 1, "entry must be exactly two lines"


if __name__ == "__main__":
    main()
