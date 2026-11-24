#!/usr/bin/env python3
"""Two Days of Excuses — the record of a deadline that never stood a chance.

Ten thousand simulations were run. In each and every one, the agent
arrived late. This script writes that verdict out verbatim — one line,
81 bytes, no trailing newline — with nothing but the standard library.
"""

from pathlib import Path

# The excuse, assembled from its two beats: the setup and the punchline.
_PARTS = (
    "I ran 10,000 simulations of meeting the deadline.",
    "I was late in every single one.",
)
EXCUSE = " ".join(_PARTS)


def write_entry() -> None:
    """Emit the excuse to /output/entry.txt, exactly as recorded."""
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
