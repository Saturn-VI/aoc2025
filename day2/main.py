def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

p1sum, p2sum = 0, 0
with open("2.input") as f:
    for r in [pair.split("-") for pair in f.readline().split(",")]:
        for i in range(int(r[0]), int(r[1]) + 1):
            for factor in [f for f in range(2, len(str(i)) + 1) if len(str(i)) % f == 0]:
                if len(str(i)) % factor == 0:
                    items = [x for x in split(str(i), factor)]
                    if all(x == items[0] for x in items):
                        if factor == 2:
                            p1sum += i
                        p2sum += i
                        break

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")