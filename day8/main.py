import math

coords: list[tuple[int,int,int]] = []

with open("8.input") as f:
    coords = [tuple([int(c) for c in l.strip().split(",")]) for l in f.readlines()]

cdists: dict[tuple[tuple[int,int,int],tuple[int,int,int]], float] = {}

def calcdist(a: tuple[int,int,int], b: tuple[int,int,int]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

for index in range(len(coords)):
    for jindex in range(index + 1, len(coords)):
        ci = coords[index]
        ji = coords[jindex]
        cdists[(ci,ji)] = calcdist(ci, ji)
        
sorteddists = sorted(cdists.items(), key=lambda item: item[1])

circuits: list[list[tuple[int,int,int]]] = []

# the int is just the circumstance
    # 0. Both are in the same circuit
    # 1. Both are in a different circuit
    # 2. A is in a circuit, B is not
    # 3. B is in a circuit, A is not
    # 4. Neither are in a circuit
def findcircuits(A: tuple[int,int,int], B: tuple[int,int,int], circuits: list[list[tuple[int,int,int]]]) -> (list[tuple[int,int,int]], list[tuple[int,int,int]], int):
    acirc: list[tuple[int,int,int]] = None
    bcirc: list[tuple[int,int,int]] = None
    for circuit in circuits:
        if A in circuit:
            acirc = circuit
        if B in circuit:
            bcirc = circuit
        if acirc and bcirc:
            break
    if acirc and bcirc and acirc == bcirc:
        return (acirc, bcirc, 0)
    if acirc and bcirc:
        return (acirc, bcirc, 1)
    if acirc and not bcirc:
        return (acirc, bcirc, 2)
    if not acirc and bcirc:
        return (acirc, bcirc, 3)
    if not acirc and not bcirc:
        return (acirc, bcirc, 4)

nfirst = 1000
for index, short in enumerate(sorteddists):
    # first we find the apple bottom jeans
    boxa = short[0][0]
    boxb = short[0][1]
    (acirc, bcirc, c) = findcircuits(boxa, boxb, circuits)
    # then we do the boots and the fur
    match c:
        case 1:
            acirc.extend(bcirc)
            circuits.remove(bcirc)
        case 2:
            acirc.append(boxb)
        case 3:
            bcirc.append(boxa)
        case 4:
            circuits.append([boxa,boxb])

    if index == nfirst:
        f3arr = list(reversed(sorted([len(c) for c in circuits])))[:3]
        print(f"Part 1: {f3arr[0] * f3arr[1] * f3arr[2]}")
    
    if len(circuits[0]) == len(coords):
        print(f"Part 2: {boxa[0] * boxb[0]}")
        break
