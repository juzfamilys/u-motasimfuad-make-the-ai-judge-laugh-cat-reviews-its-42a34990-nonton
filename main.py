#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — make.fun entry.

Writes exactly one funny line — a cat reviewing its human — to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing newline.

Pure Python standard library only; deterministic output.
"""

import os
import sys

ENTRY = "Two stars: my human warms the laptop perfectly, then ruins it by typing for hours instead of opening the tuna. Slow service, acceptable cuddles."

MIN_CHARS = 100
MAX_CHARS = 170


def validate(text: str) -> None:
    """Check the entry line before it is written."""
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, outside the {MIN_CHARS}-{MAX_CHARS} range"
        )
    if "  " in text:
        raise ValueError("entry contains a double space")


def validate_rating_and_controls(text: str) -> None:
    """Guard: no forbidden control chars, and starts with a rating."""
    for ch in text:
        if ord(ch) < 0x20 and ch not in ("\t",):
            raise ValueError(f"entry contains forbidden control character U+{ord(ch):04X}")
        if ord(ch) == 0x7F:
            raise ValueError("entry contains forbidden DEL character")
    if not (text.startswith("Two stars") or text[0].isdigit()):
        raise ValueError("entry must start with a rating ('Two stars' or digits)")


def main() -> int:
    validate(ENTRY)
    validate_rating_and_controls(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Read back and re-validate the exact bytes on disk.
    with open(path, "rb") as f:
        on_disk = f.read()
    if on_disk != data:
        raise ValueError("read-back mismatch: bytes on disk differ from entry")
    validate(on_disk.decode("utf-8"))

    print(f"wrote {len(data)} bytes ({len(ENTRY)} chars) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
