from pprint import pprint
f = open("input.txt", "r")

#
# Part 1
#

#     [S] [C]         [Z]
# [F] [J] [P]         [T]     [N]
# [G] [H] [G] [Q]     [G]     [D]
# [V] [V] [D] [G] [F] [D]     [V]
# [R] [B] [F] [N] [N] [Q] [L] [S]
# [J] [M] [M] [P] [H] [V] [B] [B] [D]
# [L] [P] [H] [D] [L] [F] [D] [J] [L]
# [D] [T] [V] [M] [J] [N] [F] [M] [G]
#  1   2   3   4   5   6   7   8   9

# move 3 from 4 to 6
# move 1 from 5 to 8
# move 3 from 7 to 3


lines = [l.removesuffix("\n") for l in f.readlines()]

empty_line_idx = lines.index("")

stacks = [[] for _ in range(0, 9)]

for l in lines[:empty_line_idx]:
    if l == ' 1   2   3   4   5   6   7   8   9':
        continue

    for i in range(0, len(l), 4):
        crate = l[i + 1]
        if crate == " ":
            continue
        stacks[i//4].insert(0, crate)


# pprint(stacks)

instructions = []

for l in lines[empty_line_idx + 1:]:
    _, move_x, __, from_s, ___, to_s = [x for x in l.split(' ')]
    instructions.append([int(move_x), int(from_s) - 1, int(to_s) - 1])

# print("instructions:", instructions)

# for move_x, from_s, to_s in instructions:
#     for _ in range(move_x):
#         stacks[to_s].append(stacks[from_s].pop())


# # pprint(stacks)

# res = [y[-1] for y in stacks]

# pprint(res)


for move_x, from_s, to_s in instructions:
    stacks[to_s].extend(stacks[from_s][-move_x:])
    del stacks[from_s][-move_x:]

# pprint(stacks)

res = [y[-1] for y in stacks]

pprint(''.join(res))
