import os

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

cycle = 0
next_cycle = 20
sum_signals = 0
registry = 1

# 20th, 60th, 100th, 140th, 180th, and 220th cycles

for line in lines:
    instr = line.split(" ")[0]

    if instr == "noop":
        cycle += 1
    else:
        cycle += 2

    if cycle >= next_cycle:
        sum_signals += next_cycle * registry
        next_cycle += 40

    if instr != "noop":
        registry += int(line.split(" ")[1])


print('Res:', sum_signals)
