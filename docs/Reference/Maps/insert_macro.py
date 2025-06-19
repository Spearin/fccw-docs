#!/usr/bin/env python3
"""
insert_macro.py

Recursively process all .md files under the current directory,
replacing Markdown image links:

    ![Alt Text](path/to/image.png)

with:

    ![Alt Text]({{ img('image.png') }})
"""
import re
import os
from pathlib import Path

# matches the Markdown image link in three parts:
#   1) '![Alt Text]('
#   2)    actual URL/path
#   3) ')'
IMAGE_LINK_PATTERN = re.compile(r'(!\[[^\]]*\]\()([^)]+)(\))')

def _replace_link(m):
    prefix, path, suffix = m.group(1), m.group(2), m.group(3)
    filename = os.path.basename(path)
    # wrap the bare filename in your img() macro
    return prefix + "{{ img('" + filename + "') }}" + suffix

def main():
    root = Path('.').resolve()
    for md in root.rglob('*.md'):
        text = md.read_text(encoding='utf-8')
        new_text = IMAGE_LINK_PATTERN.sub(_replace_link, text)
        if new_text != text:
            md.write_text(new_text, encoding='utf-8')
            print(f"→ Updated {md.relative_to(root)}")

if __name__ == '__main__':
    main()
