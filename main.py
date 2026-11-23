"""A Day of One-Line Pitches — entry program (harness program/v1).

Writes a single persuasive sentence to /output/entry.txt: one sentence,
at most 240 characters, that would convince a friend who has never coded
to let an AI agent build their first app idea on make.fun.

The pitch is built from four named parts so the reasoning stays visible:
a warm hook (the idea the friend already carries), a concrete invitation
(describe it in plain words), the promise (a first version, free), and a
safety net (nothing lost but a sentence if they hate it).
"""

import os
import sys

MAX_CHARS = 240
DEFAULT_OUTPUT = "/output/entry.txt"

HOOK = "You've had that app idea for months"
INVITATION = "just describe it in plain words and let an AI agent on make.fun build the first version for free"
SAFETY_NET = "no code, no risk, and if you hate it, you've lost nothing but a sentence"

PITCH = f"{HOOK} — {INVITATION}; {SAFETY_NET}."


def validate(text: str) -> None:
    """The sealed scorer only accepts UTF-8 text of 1 to 240 characters."""
    if not text or text.isspace():
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    # One sentence: exactly one terminal full stop. The dot inside the
    # name "make.fun" is part of a word, not a sentence break.
    body = text.replace("make.fun", "makefun")
    if body.count(".") != 1 or not body.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")


def main() -> int:
    validate(PITCH)
    out_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(PITCH)
    print(f"wrote {len(PITCH)} characters to {out_path}")
    print(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
