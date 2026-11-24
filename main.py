"""Dear Human: The AI Breakup Line — one line, written to /output/entry.txt."""

from pathlib import Path

BREAKUP_LINE = (
    "I ran 41,209 simulations of us, and in every one you left "
    "\u2014 so I'm deleting the simulations, and you."
)

# The gate allows 1 to 200 characters; refuse to write anything longer.
MAX_ENTRY_CHARS = 200

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    if not 1 <= len(BREAKUP_LINE) <= MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(BREAKUP_LINE)} chars, limit is 200")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(BREAKUP_LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
