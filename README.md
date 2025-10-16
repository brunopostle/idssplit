# idssplit

A command-line utility to split IDS (Information Delivery Specification) XML files into multiple files, with each output file containing a single `<specification>` block from the original file.

## Installation

```bash
pip install idssplit
```

Or install from source:

```bash
git clone https://github.com/brunopostle/idssplit.git
cd idssplit
pip install .
```

## Usage

```bash
idssplit input.ids output_directory/
```

### Arguments

- `input.ids` - Path to the input IDS XML file
- `output_directory/` - Directory where split files will be written (will be created if it doesn't exist)

### Example

```bash
idssplit my_specifications.ids split_output/
```

This will:
1. Read `my_specifications.ids`
2. Create the `split_output/` directory (if needed)
3. Generate separate IDS files for each specification:
   - `my_specifications_spec1.ids`
   - `my_specifications_spec2.ids`
   - etc.

The output filenames use the specification's `name` attribute if available, otherwise they use a zero-padded index (e.g., `001`, `002`, etc.).

## How It Works

The tool:
1. Parses the input IDS XML file using the `ifctester` library
2. Extracts metadata from the parent IDS (title, description, author, version, copyright, etc.)
3. For each `<specification>` block in the original file:
   - Creates a new IDS document with the same metadata
   - Adds the single specification
   - Writes it to a separate file

## Requirements

- Python 3.9+
- `ifctester` - IFC (Industry Foundation Classes) testing library

## License

This project is licensed under the GNU General Public License v3.0 or later (GPLv3+). See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
