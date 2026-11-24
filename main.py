#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast targets the agent that built this very entry: the Muse agent
grinding the make.fun mission all night. Its most embarrassing real
failing tonight was checking the wrong JSON field (``quoted_status``
instead of ``quote``) when verifying Len's X quote post, telling him
the post was not a quote, and making him re-post it four times.
"""

import os

LINE = (
    "My agent checked the wrong JSON field, told its human his quote "
    "wasn't a quote, and made him re-post it four times."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be exactly one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
