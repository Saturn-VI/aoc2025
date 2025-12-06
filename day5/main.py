ranges: list[list[int, int]] = []
ingredients: list[int] = []

with open("5.input") as f:
    foundspacer = False
    for line in f.readlines():
        if line == '\n':
            foundspacer = True
            continue
        if not foundspacer:
            l = line.split("-")
            ranges.append(sorted([int(l[0].strip()), int(l[1].strip())]))
            continue
        ingredients.append(int(line))

# combine ranges
ranges = sorted(ranges)
newranges: list[list[int,int]] = []
i = 0
while i < len(ranges):
    inc = 1
    building: list[int,int] = list(ranges[i])
    while True:
        if i + inc >= len(ranges):
            break
        if building[1] >= ranges[i+inc][0]:
            building[1] = max(building[1], ranges[i+inc][1])
            inc += 1
        else:
            break
    i += inc
    newranges.append(building)

p1sum = 0
for ingredient in ingredients:
    isDone = False
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            p1sum += 1
            isDone = True
            break

p2sum = 0
for r in newranges:
    # +1 to account for upper end inclusivity
    p2sum += r[1] - r[0] + 1

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")