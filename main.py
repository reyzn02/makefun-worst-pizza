#!/usr/bin/env python3
"""The Worst Pizza Topping.

Writes one funny line, under 200 characters, pitching a terrible pizza
topping. Python standard library only, no network calls, deterministic
output.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line is validated before writing.

v1 (round-1 tournament champion, 144 chars): the raw potato. One whole
raw potato, no slices, no seasoning — a topping with no preparation at
all, staring back at the eater like a fellow diner who also didn't
order this. Vivid, specific, one clean surprising turn.

v2 (round-2 champion, 127 chars): the raw egg. Beat-the-top showed v1
losing to the strongest visible lines (pickled herring, gas-station
sushi, durian — all multi-beat escalations), so a fresh round was run.
The egg wins: three causal beats (hatches in the oven, the chick looks
up at you, suddenly you're the topping) with a role-reversal turn that
no visible line uses — "hatch" appears in zero of 1,866 entries — and
it duels the top lines on the brief's own order (a real joke with a
surprising turn, not just a gross-out). v1's single turn was outgunned;
v2 keeps the deadpan sales voice and adds a story.
"""

import os

LINE = (
    "Try our new pizza topped with one raw egg \u2014 it hatches in the "
    "oven, the chick looks up at you, and suddenly you\u2019re the topping."
)


def main():
    text = LINE
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
