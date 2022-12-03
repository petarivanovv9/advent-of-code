f = open("input.txt", "r")

#
# Part 1
#

# A - Rock     - X - 1 point
# B - Paper    - Y - 2 points
# C - Scissors - Z - 3 points
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# mapping = {
#     'A X': 3 + 1,
#     'A Y': 6 + 2,
#     'A Z': 0 + 3,
#     'B X': 0 + 1,
#     'B Y': 3 + 2,
#     'B Z': 6 + 3,
#     'C X': 6 + 1,
#     'C Y': 0 + 2,
#     'C Z': 3 + 3
# }

# sum_points = 0

# for line in f.readlines():
#     sum_points += mapping[line.strip('\n')]


# print('Result:', sum_points)


#
# Part 2
#

# A - Rock     - X - 1 point
# B - Paper    - Y - 2 points
# C - Scissors - Z - 3 points
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

mapping = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 6 + 2,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6
}

sum_points = 0

for line in f.readlines():
    sum_points += mapping[line.strip('\n')]


print('Result:', sum_points)
