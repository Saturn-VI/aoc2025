initgrid = []

fname = "6.input"

with open(fname) as f:
    g = [line.split() for line in f.readlines()]
    initgrid = list(map(list, zip(*g)))[::-1]

p1sum = 0
for row in initgrid:
    op = row[-1]
    p1sum += eval(op.join(row[:-1]))

p2sum = 0
with open(fname) as f:
    rotlines = list(map(list, zip(*f.readlines()[::-1])))
    needinit = True
    curval = rotlines[0][-1]
    curop = rotlines[0][0]
    for line in rotlines:
        if all((c == ' ' or c == '\n' for c in line)):
            p2sum += curval
            needinit = True
            continue
        if needinit:
            curop = line[0]
            curval = 0 if curop == '+' else 1
            needinit = False
        lval = int(''.join([v for v in reversed(line[1:]) if v.isdigit()]))
        curval = eval(f"{curval}{curop}{lval}")

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")