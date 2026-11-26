import os
import shutil

ENTRY = "entry.txt"


def main():
    # A museum label is a finished text, settled before the program runs,
    # not something to compose on the spot. This program only carries the
    # finished placard into the output directory unchanged.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(ENTRY, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
