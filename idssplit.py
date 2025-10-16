#!/usr/bin/env python3

"""
idssplit: Split an IDS XML file into multiple files,
each containing a single <ids:specification> block.

Usage:
    idssplit input.ids output_directory/
"""

import sys
import os
from pathlib import Path
from ifctester.ids import Ids, open as ids_open


def split_ids(input_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    ids = ids_open(input_path, validate=False)
    total = len(ids.specifications)
    print(f"Found {total} <specification> block(s).")

    # Calculate padding width based on total number of specifications
    pad_width = len(str(total))

    for idx, spec in enumerate(ids.specifications, start=1):
        new_ids = Ids(
            title=ids.info.get('title'),
            description=ids.info.get('description'),
            author=ids.info.get('author'),
            version=ids.info.get('version'),
            date=ids.info.get('date'),
            purpose=ids.info.get('purpose'),
            milestone=ids.info.get('milestone'),
            copyright=ids.info.get('copyright'),
        )

        new_ids.specifications.append(spec)

        # Use zero-padded index as suffix
        suffix = f"{idx:0{pad_width}}"
        filename = Path(output_dir) / f"{Path(input_path).stem}_{suffix}.ids"

        new_ids.to_xml(str(filename))
        print(f"Wrote: {filename.name}")


def main():
    if len(sys.argv) != 3:
        print("Usage: idssplit <input.ids> <output_directory>")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_directory = Path(sys.argv[2])

    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)

    split_ids(input_file, output_directory)


if __name__ == "__main__":
    main()

