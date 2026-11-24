"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes exactly one original line of fortune-cookie wisdom for a
software developer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Pure standard library (os only). Deterministic: the same line every run.
"""

import os

# The fortune: a prediction in classic fortune-cookie voice, built on a
# truth every developer recognises — the throwaway name that never dies.
LINE = "The function you name 'temp' will outlive the company that hired you."


def validate(line):
    """Enforce the competition gate: one UTF-8 line, 1-120 chars, not blank."""
    text = line.strip()
    if not text:
        raise ValueError("fortune must not be empty")
    if len(text) > 120:
        raise ValueError("fortune exceeds 120 characters: %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    text.encode("utf-8")  # raises on non-UTF-8-encodable content
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print("wrote %s (%d chars)" % (path, len(text)))


if __name__ == "__main__":
    main()
