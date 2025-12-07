instructions = []

p1sum = 0
p2sum = 0
number = 50

with open("1.input") as f:
    for instruction in [int(line.replace("R", "").replace("L", "-")) for line in f.readlines()]:
        mirror = instruction < 0
        if mirror and number > 0:
            number = 100 - number
        number += abs(instruction)
        p2sum += number // 100
        number = number % 100
        if mirror and number > 0:
            number = 100 - number
        if number == 0:
            p1sum += 1

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")
