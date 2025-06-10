# DOCX to Markdown Converter

A simple Python utility to convert Microsoft Word (`.docx`) manuals into Markdown files.

## Features

* **Per-section export**: Splits each document into separate Markdown files for every top-level heading.
* **Single-file export**: Optionally output the entire document as one Markdown file.
* **Admonition support**: Converts `Note:`, `Warning:`, and `Tip:` lines into Material for MkDocs admonitions.
* **List formatting**: Corrects ordered list numbering and indents nested unordered lists.
* **Image placeholders**: Strips embedded images and adds a notice to refer to the original DOCX for figures.
* **Section exclusion**: Skip specific numbered sections (and their sub‑headings) via command‑line.

---

## Prerequisites

* Python 3.7+
* [mammoth](https://github.com/mwilliamson/python-mammoth) Python package:

  ```bash
  pip install mammoth
  ```

## Directory Structure

```text
docs/utils/
├── doc_convert.py      # Converter script
├── src/                # Place your .docx files here
└── output/             # Generated Markdown folders appear here
```

## Usage

Run the converter from the `docs/utils/` directory:

```bash
python doc_convert.py [OPTIONS]
```

### Command-Line Options

* `--exclude N [M …]`
  Skip top-level headings numbered `N`, `M`, … and all their sub-sections.
  *Example:* `--exclude 2 5`

* `--single-file`
  Export each document as **one** Markdown file instead of multiple files per section.

* `--verbose`
  Enable debug-level console logging to trace internal processing steps.

## Examples

### Split into multiple files (default)

```bash
python doc_convert.py
```

* Input: `src/MyManual.docx`
* Output:

  ```text
  output/
  └── mymanual/
      ├── introduction.md
      ├── chapter-1.md
      ├── chapter-2.md
      └── appendices.md
  ```

### Single-file output

```bash
python doc_convert.py --single-file
```

* Output:

  ```text
  output/
  └── mymanual/
      └── mymanual.md
  ```

### Exclude specific sections

```bash
python doc_convert.py --exclude 3 4
```

* Skips headings `3.` and `4.` (and everything under them) in each document.

### Verbose logging

```bash
python doc_convert.py --verbose
```

* Prints detailed debug information during conversion.

---

## Troubleshooting

* **Mammoth warnings** about encoding can be ignored if conversion succeeds.
* Ensure your DOCX uses **enumerated** top-level headings (`1.`, `2.`, etc.).
* If output looks incorrect, run with `--verbose` to inspect the processing log.

## License

This tool is released under the MIT License. Feel free to modify and integrate into your workflow.
