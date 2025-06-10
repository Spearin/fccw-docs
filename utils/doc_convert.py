#!/usr/bin/env python3
# docs/utils/doc_convert.py
# Converts DOCX files in docs/utils/src/ to Markdown folders under docs/utils/output,
# skipping images, converting admonitions, fixing lists, and generating nav.yml for sequence.

import os
import re
import argparse
import logging
import mammoth

def slugify(text: str) -> str:
    """
    Create a URL-friendly slug from header text or filename.
    """
    text = text.lower().strip()
    text = re.sub(r"<[^>]+>", "", text)        # strip HTML tags
    text = re.sub(r"[^\w\s-]", "", text)      # remove non-word chars
    text = re.sub(r"[\s]+", "-", text)        # collapse whitespace to hyphens
    return text.strip('-')

def convert_admonitions(md: str) -> str:
    """
    Replace inline Note:/Warning:/Tip: lines with MkDocs block admonitions.
    """
    pattern = re.compile(
        r"^[\s_*]*(?P<kind>Note|Warning|Tip):\s*(?P<text>.+?)[\s_*]*$",
        re.IGNORECASE | re.MULTILINE
    )
    def repl(m):
        kind = m.group('kind').lower()
        raw  = m.group('text').strip()
        lines = raw.splitlines()
        indented = "".join(f"    {line}\n" for line in lines)
        return f"!!! {kind}\n\n{indented}\n"
    return pattern.sub(repl, md)

def convert_lists(md: str) -> str:
    """
    Fix ordered list numbering and indent nested unordered lists.
    """
    lines = md.splitlines()
    out = []
    ol_counter = None
    last_was_ol = False
    last_indent = ""
    for line in lines:
        m_ol = re.match(r'^(?P<indent>\s*)(?P<num>\d+)\.\s+(?P<text>.+)$', line)
        if m_ol:
            indent, _, text = m_ol.group('indent','num','text')
            if ol_counter is None or not last_was_ol:
                ol_counter = 1
            else:
                ol_counter += 1
            out.append(f"{indent}{ol_counter}. {text}")
            last_was_ol = True
            last_indent = indent
            continue
        if last_was_ol and line.strip() == "":
            # skip blank line immediately after an OL item
            continue
        m_ul = re.match(r'^\s*[-*]\s+(?P<text>.+)$', line)
        if last_was_ol and m_ul:
            text = m_ul.group('text')
            out.append(f"{last_indent}    - {text}")
            continue
        out.append(line)
        last_was_ol = False
    return "\n".join(out)

def preprocess(md: str) -> str:
    """
    Apply global transformations: remove embedded images, strip HTML,
    convert admonitions, and fix lists.
    """
    # remove embedded data URIs
    md = re.sub(
        r"!\[.*?\]\(data:[^)]+\)",
        "> **Note**: Image omitted — refer to original DOCX for figures.\n\n",
        md, flags=re.DOTALL
    )
    # strip HTML anchors and tags
    md = re.sub(r"<a[^>]*></a>", "", md)
    md = re.sub(r"<[^>]+>", "", md)
    # admonitions and lists
    md = convert_admonitions(md)
    md = convert_lists(md)
    return md

def process_and_split(md: str, output_dir: str, exclude_ids: set) -> list:
    """
    Split processed markdown by level-1 headers into separate files.
    Returns list of filenames in sequence.
    """
    header_re = re.compile(
        r'^(?P<hashes>#+)\s+(?P<num>\d+(?:\.\d+)*\s+)?(?P<title>.+)$',
        re.MULTILINE
    )
    lines = md.splitlines(keepends=True)
    current = None
    skipping = False
    filenames = []

    for line in lines:
        m = header_re.match(line)
        if m and len(m.group('hashes')) == 1:
            # close previous
            if current:
                current.close()
            num   = m.group('num') or ""
            title = m.group('title').strip()
            hid   = None
            if num:
                try:
                    hid = int(num.split('.')[0])
                except ValueError:
                    hid = None
            if hid in exclude_ids:
                skipping = True
                continue
            slug     = slugify(title)
            filename = f"{slug}.md"
            path     = os.path.join(output_dir, filename)
            logging.info(f"Writing section: {title} → {path}")
            current = open(path, 'w', encoding='utf-8')
            current.write(f"# {title}\n\n")
            current.write("> **Note**: Images omitted — refer to original DOCX for figures.\n\n")
            skipping = False
            filenames.append(filename)
            continue

        if not skipping and current:
            current.write(line)

    if current:
        current.close()

    return filenames

def process_full(md: str, output_path: str) -> list:
    """
    Write entire processed markdown to a single file.
    Returns a list containing that filename.
    """
    logging.info(f"Writing single file: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    return [os.path.basename(output_path)]

def write_nav_yaml(output_dir: str, filenames: list):
    """
    Generate a nav.yml listing filenames in their processed order.
    """
    nav_path = os.path.join(output_dir, '.nav.yml')
    logging.info(f"Writing navigation file: {nav_path}")
    with open(nav_path, 'w', encoding='utf-8') as nav:
        nav.write("nav:\n")
        for fn in filenames:
            nav.write(f"  - {fn}\n")

def convert_docx(path: str, base_output: str, exclude_ids: set, single_file: bool):
    """
    Convert a single DOCX to Markdown files (split or single) in its own folder.
    """
    filename = os.path.splitext(os.path.basename(path))[0]
    folder   = os.path.join(base_output, slugify(filename))
    os.makedirs(folder, exist_ok=True)
    logging.info(f"Created output directory: {folder}")

    with open(path, 'rb') as f:
        res = mammoth.convert_to_markdown(f)
    for msg in res.messages:
        logging.warning(msg)

    md = preprocess(res.value)

    if single_file:
        outfile = os.path.join(folder, f"{slugify(filename)}.md")
        files = process_full(md, outfile)
    else:
        files = process_and_split(md, folder, exclude_ids)

    write_nav_yaml(folder, files)

def main():
    parser = argparse.ArgumentParser(
        description="Convert DOCX → Markdown folders with .nav.yml."
    )
    parser.add_argument(
        '--exclude', nargs='*', type=int, default=[],
        help="Top-level header numbers to skip."
    )
    parser.add_argument(
        '--single-file', action='store_true',
        help="Export the entire document as a single Markdown file."
    )
    parser.add_argument(
        '--verbose', action='store_true',
        help="Enable debug logging."
    )
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')

    base       = os.path.dirname(__file__)
    src        = os.path.join(base, 'src')
    output_dir = os.path.join(base, 'output')
    os.makedirs(output_dir, exist_ok=True)

    exclude_ids = set(args.exclude)

    for fname in os.listdir(src):
        if fname.lower().endswith('.docx'):
            convert_docx(
                os.path.join(src, fname),
                output_dir,
                exclude_ids,
                args.single_file
            )

    logging.info("Conversion complete.")

if __name__ == "__main__":
    main()
