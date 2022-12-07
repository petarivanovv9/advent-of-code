f = open("input.txt", "r")

lines = [l.removesuffix("\n") for l in f.readlines()]

line = lines[0]

#
# Part 1
#

# len_marker = 4

# res = -1

# for i in range(0, len(line) - len_marker):
#     if len(set(line[i:i + len_marker])) == len_marker:
#         res = i + len_marker
#         break

# print('Res:', res)

#
# Part 2
#

len_marker = 14

res = -1

for i in range(0, len(line) - len_marker):
    if len(set(line[i:i + len_marker])) == len_marker:
        res = i + len_marker
        break

print('Res:', res)
