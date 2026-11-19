#!/usr/bin/env python3
"""news-image-daily entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a one-day world-news
infographic drawn for Wednesday 18 November 2026, with eight labelled
story cards covering the day's most consequential stories across regions
and fields. The program copies it to /output/entry.png, byte for byte,
so both grading runs produce the same file. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    if not SOURCE.is_file():
        raise RuntimeError("entry.png is missing from the repository")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The gate reads exactly the bytes copied, so fail loudly rather
    # than hand it a partial file if the copy ever falls short, and
    # refuse to hand it anything that is not a whole PNG.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")
    with target.open("rb") as handle:
        if handle.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise RuntimeError("entry.png is not a PNG file")


if __name__ == "__main__":
    main()
