beamstate: list[int] = []
splitterarray: list[list[bool]] = []

with open("7.input") as f:
    beamstate = [1 if c == "S" else 0 for c in f.readline()]
    f.readline()
    splitterarray = [[True if c == "^" else False for c in l] for l in f.readlines()[::2]]

p1sum = 0
for line in splitterarray:
    buffer: list[int] = beamstate.copy()
    for index, issplitter in enumerate(line):
        if not issplitter:
            continue
        if beamstate[index] > 0:
            p1sum += 1
            if index != 0:
                buffer[index - 1] += buffer[index]
            if index != len(buffer) - 1:
                buffer[index + 1] += buffer[index]
        buffer[index] = 0
    beamstate = buffer

print(f"Part 1: {p1sum}")
print(f"Part 2: {sum(beamstate)}")