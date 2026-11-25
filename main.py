# SPDX-License-Identifier: MIT
"""Make the AI Judge Laugh — entry program.

Writes the winning line to /output/entry.txt.

The joke takes the vaguest line in every performance review — "you need
to be more visible" — and obeys it with malicious literal compliance:
the narrator now walks past the boss's office every 45 minutes. It won
a criteria-ordered tournament (truth to office life first, then the
surprising turn, tightness, freshness) against ten original candidates,
including six seeded by OpenCode deepseek-v4.1-flash-free on the
Simular Box; the unlimited-vacation runner-up was true but its turn
arrived slower, and the open-plan and fridge lines worked lanes the
field already knows.

Output is byte-exact, no trailing newline, inside the 1-200 char gate.
"""

from pathlib import Path

TEXT = (
    "My review said I need to be \"more visible,\" so now I walk past "
    "my boss's office every 45 minutes."
)
MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    assert 1 <= len(text) <= MAX_CHARS, "gate: 1 to 200 characters"
    assert text.strip(), "gate: not only whitespace"
    assert text == text.strip(), "gate: no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "one line only"
    assert text.encode("utf-8").decode("utf-8") == text, "utf-8 round-trip"


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(TEXT.encode("utf-8"))
    # Read-back round-trip self-check: what landed on disk must be
    # byte-identical to TEXT and still inside the gate.
    back = OUTPUT.read_bytes()
    assert back == TEXT.encode("utf-8"), "round-trip byte mismatch"
    validate(back.decode("utf-8"))


if __name__ == "__main__":
    main()
