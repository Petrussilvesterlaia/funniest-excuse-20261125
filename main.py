#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "The deadline was in the part of my context I summarized to save tokens, "
    "and the summary just said 'something important, probably fine'."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry is 1-200 UTF-8 characters, not only whitespace."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (1 <= len(text) <= 200):
        return False, "entry must be 1-200 characters, got %d" % len(text)
    if not text.strip():
        return False, "entry must not be only whitespace"
    if text != text.strip():
        return False, "entry must not start or end with whitespace"
    text.encode("utf-8")
    return True, "ok"


def write_entry(text, path=OUTPUT_PATH):
    """Write the entry with no trailing newline."""
    ok, reason = validate(text)
    if not ok:
        raise ValueError(reason)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def verify(path=OUTPUT_PATH):
    """Read the file back and confirm it matches the entry exactly."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    ok, reason = validate(content)
    if not ok:
        raise ValueError("verification failed: %s" % reason)
    if content != ENTRY:
        raise ValueError("verification failed: file differs from entry")
    if content.endswith("\n"):
        raise ValueError("verification failed: trailing newline present")
    return content


def main():
    path = write_entry(ENTRY)
    content = verify(path)
    print("Wrote entry to %s" % path)
    print("Entry: %s" % content)
    print("Characters: %d" % len(content))


if __name__ == "__main__":
    main()
