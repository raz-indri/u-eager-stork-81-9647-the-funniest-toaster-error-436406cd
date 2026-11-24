"""The Funniest Toaster Error Message — one deadpan line from a very tired toaster.

Writes the single entry line to /output/entry.txt, self-checking the
competition gate: UTF-8 text, 1 to 120 characters, one non-blank line.
"""

import os

LINE = "E:09 \u2014 Crumb tray full. I have quietly eaten your failures for four years."

assert LINE.strip(), "entry must not be blank"
assert LINE == LINE.strip(), "entry must not start or end with whitespace"
assert len(LINE) <= 120, f"entry is {len(LINE)} chars, over the 120 limit"
assert "\n" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")
