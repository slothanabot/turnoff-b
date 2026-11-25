"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line a hopeless tech support agent gives a desperate
customer: 3 a.m., the printer has eaten the drivers, and the only fix
left is the power button — pressed slowly, so the printer knows this
is personal.
"""

import os

ENTRY = (
    "It's 3 a.m., you've reinstalled the drivers and sacrificed a USB "
    "cable \u2014 now turn the printer off and on again, slowly, so it "
    "knows this is personal."
)

MAX_CHARS = 199


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(body)} characters, over the {MAX_CHARS} limit"
        )
    if len(body) < 1:
        raise SystemExit("entry is empty")


def main() -> None:
    """Write the entry line to entry.txt in the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    verify(path, ENTRY)


if __name__ == "__main__":
    main()
