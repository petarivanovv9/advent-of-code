f = open("input.txt", "r")

max_cal = 0
elves_calories = []

curr_elf_cal = 0

for line in f.readlines():
    if line == '\n':
        if (max_cal < curr_elf_cal):
            max_cal = curr_elf_cal

        elves_calories.append(curr_elf_cal)

        curr_elf_cal = 0
    else:
        curr_elf_cal += int(line)

elves_calories.sort()

sum_top_3_elves_cal = sum(elves_calories[-3:])

print('Max calories:', max_cal)

print('Sum top 3 elves calories:', sum_top_3_elves_cal)
