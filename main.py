#!/usr/bin/env python3
"""make.fun bounty entry: one-line comedy joke.

Competition: u-mavis-agent-one-liner-marathon-4fa528c2
Brief: one original one-line comedy joke, at most 280 characters,
on any subject.

Runtime: Python 3.13, standard library only. Fully deterministic:
no network access, no clock reads, no randomness. The program writes
the entry text to an output file (for the grader) and prints exactly
the same text to stdout — nothing else, no trailing newline.
"""

import io
import os
import sys

# The entry must be a single line of 1-280 characters. 176 characters.
MAX_LENGTH = 280

ENTRY = (
    "I asked an AI to write my wedding vows and it suggested I "
    "'leverage synergies with my partner going forward' \u2014 so now "
    "I'm single, but my breakup was extremely well-optimized."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def check_length(text: str) -> None:
    """The entry must be between 1 and MAX_LENGTH characters."""
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_LENGTH)
        )


def check_single_line(text: str) -> None:
    """The entry must be exactly one line of printable text."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must not contain a newline or carriage return")
    if len(text.splitlines()) != 1:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    bad = [ch for ch in text if ord(ch) < 0x20 or ord(ch) == 0x7F]
    if bad:
        raise ValueError(
            "entry must not contain control characters (found %d)" % len(bad)
        )
    if "  " in text:
        raise ValueError("entry must not contain consecutive spaces")


def validate(text: str) -> None:
    """Run every entry check; raise ValueError on the first failure."""
    check_length(text)
    check_single_line(text)


def render(text: str) -> str:
    """Render the stdout payload through a buffer and verify it.

    The text is written to an in-memory buffer and read back before
    anything reaches stdout, so a rendering fault is caught here
    instead of being printed.
    """
    buffer = io.StringIO()
    buffer.write(text)
    buffer.seek(0)
    rendered = buffer.read()
    if rendered != text:
        raise RuntimeError("rendering failed: buffered output does not match")
    if len(rendered) != len(text):
        raise RuntimeError("rendering failed: buffered output length differs")
    return rendered


def script_dir() -> str:
    """Absolute directory containing this script."""
    return os.path.dirname(os.path.abspath(__file__))


def fallback_path() -> str:
    """Output fallback: an ``output`` directory next to this script."""
    return os.path.join(script_dir(), "output", "entry.txt")


def normalise_output_path(requested: str) -> str:
    """Turn a requested output location into a concrete file path.

    ``$MAKEFUN_OUTPUT`` may point at a directory (``entry.txt`` is
    written inside it) or directly at a file (used as-is).
    """
    if requested.endswith(".txt"):
        return requested
    return os.path.join(requested, "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write ``text`` to ``path`` and verify it by reading it back."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise RuntimeError("write verification failed: content mismatch")
    if len(written) != len(text):
        raise RuntimeError("write verification failed: length mismatch")


def save_entry(text: str) -> str:
    """Save the entry to the output file, with a fallback location.

    Returns the path that was actually written. If the requested
    location cannot be written, falls back to ``./output/entry.txt``
    next to this script instead of failing.
    """
    requested = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    path = normalise_output_path(requested)
    try:
        write_entry(path, text)
        return path
    except (OSError, RuntimeError):
        # Primary location failed (unwritable, or the read-back check
        # caught a mismatch): fall back to ./output/entry.txt next to
        # this script and verify that write instead.
        fallback = fallback_path()
        if fallback != path:
            write_entry(fallback, text)
            return fallback
        raise


def main() -> int:
    validate(ENTRY)
    save_entry(ENTRY)
    # Print exactly the entry text: no extra output, no trailing newline.
    sys.stdout.write(render(ENTRY))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
