"""Self-checkout machine, one judgmental line.

Writes a single funny remark in the voice of a smug self-checkout
machine to /output/entry.txt (the gate: UTF-8 text, 1-200 chars).

The line: the till watches a shopper buy twelve yoghurts and nothing
else, and its petty machine brain does the only thing it can do --
scan them twice, the second time out of concern. The joke lands cold,
needs no setup, and the sting is the machine pretending to care.
"""

import os
import sys

# The entry: one line, 87 characters, no setup, no padding.
LINE = "Twelve yoghurts and nothing else. I scanned them twice, the second time out of concern."


def main() -> int:
    # Gate check, same as the sealed scorer: 1-200 chars, not blank.
    text = LINE.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
