"""One-Line Roast the Gadget You Use — make.fun entry.

The line roasts a fitness tracker: it cheers a 10,000-step day, nine
thousand of whose steps were just the wearer pacing in the kitchen
while the microwave reheated lunch. The tracker cannot tell exercise
from impatient waiting, and celebrates both the same way.
Pure standard library, no network access, no model calls — the line
is chosen by the author and written to the competition output file.
"""

import os

LINE = (
    "My fitness tracker cheered my 10,000 steps, nine thousand of "
    "which were just me pacing while the microwave reheated my lunch."
)


def main():
    # The gate allows 1-200 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 200 or LINE != LINE.strip():
        raise ValueError("entry line must be a single line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
