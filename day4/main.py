initarr = []

with open("4.input") as f:
    initarr = [[True if c == "@" else False for c in line] for line in f.readlines()]
    
def removable(iny, inx, grid: list[list[bool]]):
    if not grid[iny][inx]:
        return False
    ys = [iny-1, iny, iny+1]
    xs = [inx-1, inx, inx+1]
    s = 0
    for y in ys:
        if y < 0 or y >= len(grid):
            continue
        for x in xs:
            if x < 0 or x >= len(grid[0]):
                continue
            if y == iny and x == inx:
                continue
            s += grid[y][x]
    return s < 4

def getRemovable(array):
    positions: list[tuple[int, int]] = []
    for yind, y in enumerate(array):
        for xind, x in enumerate(array):
            if removable(yind, xind, array):
                positions.append((yind, xind))
    return positions

p1sum = len(getRemovable(initarr))

p2sum = 0
cloneArr = initarr.copy()
while True:
    remRolls = getRemovable(cloneArr)
    if len(remRolls) == 0:
        break
    p2sum += len(remRolls)
    for pos in remRolls:
        cloneArr[pos[0]][pos[1]] = False

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")