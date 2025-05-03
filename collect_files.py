#!/usr/bin/env python3
import os
import sys
import shutil

def collect_files(input_dir, output_dir, max_depth=None):
    os.makedirs(output_dir, exist_ok=True)
    seen = {}

    for root, dirs, files in os.walk(input_dir):
        for fname in files:
            src = os.path.join(root, fname)

            rel = os.path.relpath(os.path.dirname(src), input_dir)
            chain = [] if rel == '.' else rel.split(os.sep)
            if max_depth is not None:
                allowed = max_depth - 1
                if len(chain) > allowed:
                    chain = chain[-allowed:]

            target_dir = os.path.join(output_dir, *chain) if chain else output_dir
            os.makedirs(target_dir, exist_ok=True)

            key = (target_dir, fname)
            if key in seen:
                base, ext = os.path.splitext(fname)
                out_name = f"{base}{seen[key]}{ext}"
                seen[key] += 1
            else:
                out_name = fname
                seen[key] = 1

            shutil.copy2(src, os.path.join(target_dir, out_name))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: collect_files.py input_dir output_dir [--max_depth N]")
        sys.exit(1)

    inp, out = sys.argv[1], sys.argv[2]
    md = None
    if len(sys.argv) == 5 and sys.argv[3] == "--max_depth":
        try:
            md = int(sys.argv[4])
            if md < 1:
                raise ValueError()
        except ValueError:
            print("Error: max_depth must be a positive integer")
            sys.exit(1)

    collect_files(inp, out, max_depth=md)
