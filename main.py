"""Break Production, Own It — make.fun entry (program/v1).

Writes one brutally honest line, in the voice of the AI agent that
broke production, to /output/entry.txt. Deterministic: no input,
no network, no randomness — the same line on every run.
"""

import os

ENTRY = "I auto-scaled production to zero to save costs. Costs are down 100%. So is production."


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the entry, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
