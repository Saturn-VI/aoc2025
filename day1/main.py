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
# bad solution but whatever :(
# 6738
for instruction in instructions:
    # n = -1 if instruction < 0 else 1
    # for i in range(abs(instruction)):
    #     number += n
    #     if number % 100 == 0:
    #         zero_passed_count += 1
    number += instruction
    diff = abs(int(number / 100))
    if number < 0:
        diff += 1
    zero_passed_count += diff
    number = ((number % 100) + 100) % 100


print(f"Part 1: {zero_count}")
print(f"Part 2: {zero_passed_count}")