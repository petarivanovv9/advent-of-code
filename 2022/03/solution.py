f = open("input.txt", "r")

#
# Part 1
#

# The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
# a and A refer to different types of items
# A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment,
# while the second half of the characters represent items in the second compartment.
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52


def find_common_elem(str1: str, str2: str):
    arr = set(str1).intersection(str2)
    return arr.pop()


def get_priority(c: str):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 1 + 26


lines = [l.removesuffix("\n") for l in f.readlines()]

sum_priorities = 0

for l in lines:
    half = len(l) // 2
    common_elem = find_common_elem(l[0:half], l[half:len(l)])
    sum_priorities += get_priority(common_elem)

print('Result:', sum_priorities)
