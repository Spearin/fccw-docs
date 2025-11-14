#!/usr/bin/env python3
"""
cleanup_inner_maps.py

Run this from inside the Maps/ directory.

It will:
  1. Walk every subfolder under the current folder.
  2. Skip the 'map-images' folder entirely.
  3. Delete any files ending in .png, .jpg, .jpeg, .gif, or .svg elsewhere.
"""
import os
from pathlib import Path

# Target extensions
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.svg'}

def delete_images(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        # If this directory is 'map-images', don't descend into it
        if Path(dirpath).name == 'map-images':
            dirnames.clear()
            continue

        for fname in filenames:
            if Path(fname).suffix.lower() in IMAGE_EXTS:
                file_path = Path(dirpath) / fname
                try:
                    file_path.unlink()
                    # Print path relative to Maps/ directory
                    print(f"Deleted: {file_path.relative_to(root)}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

if __name__ == '__main__':
    maps_dir = Path('.').resolve()
    delete_images(maps_dir)
