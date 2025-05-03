import os
import sys
import shutil

a = sys.argv[1:]

if len(a) < 2:
    print("Usage: collect_files.py input_dir output_dir [--max_depth N]")
    sys.exit(1)

i = a[0]
o = a[1]
d = None

if len(a) == 4 and a[2] == "--max_depth":
    try:
        d = int(a[3])
    except ValueError:
        print("Error: max_depth must be an integer")
        sys.exit(1)

if not os.path.exists(o):
    os.makedirs(o)

m = {}

for r, ds, fs in os.walk(i):
    p = os.path.relpath(r, i)
    lvl = p.count(os.sep)

    if d is not None and lvl >= d:
        continue

    for f in fs:
        s = os.path.join(r, f)
        t = f

        if t in m:
            b, e = os.path.splitext(f)
            c = m[f]
            t = f"{b}{c}{e}"
            m[f] = c + 1
        else:
            m[f] = 1

        x = os.path.join(o, t)
        shutil.copy2(s, x)
