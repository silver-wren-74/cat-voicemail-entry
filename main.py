#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Writes a single voicemail greeting, as if a cat recorded it, to
/output/entry.txt (UTF-8, 1-120 characters).
"""

import os

LINE = (
    "You've reached the cat. I heard it ring, I chose the warm laptop. "
    "Leave a message; I'll sit on that too."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
