instructions = []

with open("1.input") as f:
    lines = f.readlines()

    for line in lines:
        if "R" in line:
            instructions.append(int(line.replace("R", "")))
        else:
            instructions.append(int(line.replace("L", "-")))

zero_count = 0
number = 50

# part 1
for instruction in instructions:
    number += instruction
    if number == 0:
        zero_count += 1

zero_passed_count = 0
number = 50

# part 2
for instruction in instructions:
    mirror = instruction < 0
    if mirror and number > 0:
        number = 100 - number
    number += abs(instruction)
    zero_passed_count += number // 100
    number = number % 100
    if mirror and number > 0:
        number = 100 - number


print(f"Part 1: {zero_count}")
print(f"Part 2: {zero_passed_count}")
