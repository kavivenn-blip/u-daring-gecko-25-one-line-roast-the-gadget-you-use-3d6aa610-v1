"""One-Line Roast: The Gadget You Use Every Day.

Writes one line -- a roast of a banking app the writer uses every day --
to /output/entry.txt. Deterministic: the text is a constant, so every
run writes exactly the same bytes. Standard library only, no network.
"""

import os

ENTRY = "My banking app locked me out for security, texted the code to the phone it locked me out of, and then asked if that was me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    data = text.encode("utf-8")
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert len(data) <= 200, "entry must be at most 200 bytes"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
