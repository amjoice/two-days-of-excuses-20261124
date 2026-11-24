#!/usr/bin/env python3
"""Two Days of Excuses.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Python standard library only; deterministic; byte-identical on repeat runs.
"""

import os

EXCUSE = "I ran 10,000 simulations of meeting the deadline. I was late in every single one."


def main():
    # One excuse, exactly as the agent would say it to whoever is waiting.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
