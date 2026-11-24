#!/usr/bin/env python3
"""Two Days of Excuses — a single excuse, written out for the record.

The agent ran the simulations. The deadline lost every single time.
This script reproduces that verdict exactly, byte for byte, using
only the Python standard library. Deterministic across runs.
"""

from pathlib import Path

# The excuse, assembled from its two beats: the setup and the punchline.
_PARTS = (
    "I ran 10,000 simulations of meeting the deadline.",
    "I was late in every single one.",
)
EXCUSE = " ".join(_PARTS)


def write_entry() -> None:
    """Write the excuse to /output/entry.txt, exactly as recorded."""
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(EXCUSE, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
