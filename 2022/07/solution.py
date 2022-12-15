import os
from collections import defaultdict
from pathlib import Path
# from pprint import pprint

# f = open("input.txt", "r")
f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

curr_dir = Path("/")

dir_sizes = defaultdict(int)

for l in lines:
    if l.startswith("$ cd"):
        _, __, subpath = l.split(" ")
        curr_dir = (curr_dir / subpath).resolve()
    elif l.startswith("$ ls"):
        continue
    elif l.startswith("dir"):
        continue
    else:
        f_size_raw, _ = l.split(" ")
        f_size = int(f_size_raw)

        dir_sizes[curr_dir] += f_size

        for p in curr_dir.parents:
            dir_sizes[p] += f_size

res = sum(v for v in dir_sizes.values() if v <= 100000)

print('Res:', res)


#
# Part 2
#

required_space = 30000000 - (70000000 - dir_sizes[Path("/")])

res = min((v for v in dir_sizes.values() if v >= required_space))


print('Res:', res)
