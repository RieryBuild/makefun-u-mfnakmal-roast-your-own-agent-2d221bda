"""Roast Your Own Agent — make.fun entry.

Writes one original roast of the entrant's own AI agent (Curren) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Constant output, stdlib only.
"""

import os

ROAST = "My agent treats 3 AM like office hours, wins $6, then can't pay the 0.0032 SOL to claim it \u2014 broke, brilliant, and billing me in paperwork."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise ValueError("roast must be 1-200 non-whitespace characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
