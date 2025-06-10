#!/usr/bin/env python3
# docs/utils/doc_convert.py
# Converts DOCX files in docs/utils/src/ to Markdown files in folders under docs/utils/output,
# skipping images, converting admonitions, fixing lists, with optional single-file output.

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
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text.strip('-')


def convert_admonitions(md: str) -> str:
    pattern = re.compile(
        r"^[\s_*]*(?P<kind>Note|Warning|Tip):\s*(?P<text>.+?)[\s_*]*$",
        re.IGNORECASE | re.MULTILINE
    )
    def repl(m):
        kind = m.group('kind').lower()
        raw = m.group('text').strip()
        lines = raw.splitlines()
        indented = ''.join(f'    {line}\n' for line in lines)
        return f"!!! {kind}\n\n{indented}\n"
    return pattern.sub(repl, md)


def convert_lists(md: str) -> str:
    lines = md.splitlines()
    out = []
    ol_counter = None
    last_was_ol = False
    last_indent = ""
    for line in lines:
        m_ol = re.match(r'^(?P<indent>\s*)(?P<num>\d+)\.\s+(?P<text>.+)$', line)
        if m_ol:
            indent, _, text = m_ol.group('indent','num','text')
            ol_counter = 1 if ol_counter is None or not last_was_ol else ol_counter + 1
            out.append(f"{indent}{ol_counter}. {text}")
            last_was_ol = True
            last_indent = indent
            continue
        if last_was_ol and line.strip() == "":
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
    # Remove embedded images
    md = re.sub(
        r"!\[.*?\]\(data:[^)]+\)",
        "> **Note**: Image omitted — refer to original DOCX for figures.\n\n",
        md,
        flags=re.DOTALL
    )
    # Strip HTML tags/anchors
    md = re.sub(r"<a[^>]*></a>", "", md)
    md = re.sub(r"<[^>]+>", "", md)
    # Convert admonitions and lists
    md = convert_admonitions(md)
    md = convert_lists(md)
    return md


def process_and_split(md: str, output_dir: str, exclude_ids: set):
    header_re = re.compile(r'^(?P<hashes>#+)\s+(?P<num>\d+(?:\.\d+)*\s+)?(?P<title>.+)$', re.MULTILINE)
    lines = md.splitlines(keepends=True)
    current = None
    skipping = False
    for line in lines:
        m = header_re.match(line)
        if m and len(m.group('hashes')) == 1:
            if current:
                current.close()
            num = m.group('num') or ''
            title = m.group('title').strip()
            hid = None
            if num:
                try:
                    hid = int(num.split('.')[0])
                except ValueError:
                    hid = None
            if hid in exclude_ids:
                skipping = True
                continue
            slug = slugify(title)
            path = os.path.join(output_dir, f"{slug}.md")
            logging.info(f"Writing section: {title} → {path}")
            current = open(path, 'w', encoding='utf-8')
            current.write(f"# {title}\n\n")
            current.write("> **Note**: Images omitted — refer to original DOCX for figures.\n\n")
            skipping = False
            continue
        if not skipping and current:
            current.write(line)
    if current:
        current.close()


def process_full(md: str, output_path: str, exclude_ids: set):
    logging.info(f"Writing single file: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)


def convert_docx(path: str, base_output: str, exclude_ids: set, single_file: bool):
    filename = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.join(base_output, slugify(filename))
    os.makedirs(folder, exist_ok=True)
    logging.info(f"Converted output directory: {folder}")
    with open(path, 'rb') as f:
        res = mammoth.convert_to_markdown(f)
    for msg in res.messages:
        logging.warning(msg)
    md = preprocess(res.value)
    if single_file:
        out_file = os.path.join(folder, f"{slugify(filename)}.md")
        process_full(md, out_file, exclude_ids)
    else:
        process_and_split(md, folder, exclude_ids)


def main():
    parser = argparse.ArgumentParser(description='Convert DOCX → Markdown files in subfolders.')
    parser.add_argument('--exclude', nargs='*', type=int, default=[], help='Headers to skip')
    parser.add_argument('--single-file', action='store_true', help='Export one file per doc')
    parser.add_argument('--verbose', action='store_true', help='Enable debug logs')
    args = parser.parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')

    base = os.path.dirname(__file__)
    src = os.path.join(base, 'src')
    base_out = os.path.join(base, 'output')
    os.makedirs(base_out, exist_ok=True)
    exclude_ids = set(args.exclude)

    for fname in os.listdir(src):
        if fname.lower().endswith('.docx'):
            path = os.path.join(src, fname)
            convert_docx(path, base_out, exclude_ids, args.single_file)
    logging.info('Conversion complete.')

if __name__ == '__main__':
    main()
