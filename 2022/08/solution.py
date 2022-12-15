import os
# from pprint import pprint

f = open(os.path.dirname(__file__) + "/input.txt", "r", encoding="utf-8")

lines = [l.removesuffix("\n") for l in f.readlines()]

matrix = []

# 3 0 3 7 3
# 2 5 5 1 2
# 6 5 3 3 2
# 3 3 5 4 9
# 3 5 3 9 0

for l in lines:
    row_numbers = [int(c) for c in l]
    matrix.append(row_numbers)

m = len(matrix)  # height
n = len(matrix[0])  # width

res = 0

for i in range(m):  # rows
    for j in range(n):  # columns
        if i == 0 or j == 0 or i == m - 1 or j == n - 1:
            res += 1
        else:
            val = matrix[i][j]

            row = matrix[i]
            col = [row[j] for row in matrix]

            if max(row[:j]) < val or max(row[j + 1:]) < val or max(col[:i]) < val or max(col[i + 1:]) < val:
                res += 1

print('Res:', res)


#
# Part 2
#

m = len(matrix)  # height
n = len(matrix[0])  # width

max_score = 0

for i in range(m):  # rows
    for j in range(n):  # columns
        score = 1

        tree_score = 0
        for x in range(j-1, -1, -1):  # left
            tree_score += 1
            if matrix[i][x] >= matrix[i][j]:
                break
        score *= tree_score

        tree_score = 0
        for x in range(j+1, n):  # right
            tree_score += 1
            if matrix[i][x] >= matrix[i][j]:
                break
        score *= tree_score

        tree_score = 0
        for y in range(i-1, -1, -1):  # up
            tree_score += 1
            if matrix[y][j] >= matrix[i][j]:
                break
        score *= tree_score

        tree_score = 0
        for y in range(i+1, m):  # down
            tree_score += 1
            if matrix[y][j] >= matrix[i][j]:
                break
        score *= tree_score

        max_score = max(max_score, score)


print('Res:', max_score)
