# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a command-line utility that splits IDS (Information Delivery Specification) XML files into multiple files, with each output file containing a single `<ids:specification>` block from the original file.

## Architecture

**Single-file utility**: The entire application is in `idssplit.py` - a standalone Python script with no complex architecture.

**Key dependency**: Uses the `ifctester` library (specifically `ifctester.ids.Ids`) to parse and manipulate IDS XML files. The `Ids` class handles XML parsing and serialization.

**Core workflow**:
1. Parse input IDS file using `Ids.open()` with validation disabled
2. Extract metadata from parent IDS (title, description, author, version, etc.)
3. For each specification in `ids.specifications`, create a new `Ids` object with the same metadata
4. Write each specification to a separate file named `{original_stem}_{spec_id}.ids` or `{original_stem}_{index}.ids`

## Running the Tool

```bash
# If installed via pip
idssplit input.ids output_directory/

# Or run the script directly
./idssplit.py input.ids output_directory/

# Or with python explicitly
python3 idssplit.py input.ids output_directory/
```

The script is executable and includes a shebang (`#!/usr/bin/env python3`). When installed as a package, the command is available as `idssplit`.

## Testing

No formal test suite exists. To test manually:
1. Create or obtain a sample IDS XML file with multiple specifications
2. Run the script and verify output files are created correctly
3. Validate output IDS files can be re-parsed by IDS-compliant tools

## Dependencies

- `ifctester` - IFC (Industry Foundation Classes) testing library that provides IDS XML parsing
- Standard library: `sys`, `os`, `pathlib`

Install dependencies with:
```bash
pip install ifctester
```
