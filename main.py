#!/usr/bin/env python3
"""Sum up 24 November 2026 world news in one image.

The entry image is bundled in this repository as entry.png.
This program copies it deterministically to /output/entry.png,
with no network access, so both runs write identical bytes.
"""
import os
import shutil
import sys


def main() -> int:
    # The bundled image is the whole entry; the program only copies it,
    # so the output is byte-identical on every run.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    print(f"Wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
