f = open("input.txt", "r")

lines = [l.removesuffix("\n") for l in f.readlines()]

counter = 0

for l in lines:
    # [['13-53'], ['17-82']]
    raw_pairs = list(map(lambda x: x.split('-'), l.split(',')))
    pairs = [
        [int(raw_pairs[0][0]), int(raw_pairs[0][1])],
        [int(raw_pairs[1][0]), int(raw_pairs[1][1])]
    ]

    if set(range(pairs[0][0], pairs[0][1] + 1)).issubset(range(pairs[1][0], pairs[1][1] + 1)):
        counter += 1
        continue

    if set(range(pairs[1][0], pairs[1][1] + 1)).issubset(range(pairs[0][0], pairs[0][1] + 1)):
        counter += 1
        continue

print('Result:', counter)
