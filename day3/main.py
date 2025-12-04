banks = []

with open("3.input") as f:
    banks = [r.strip() for r in f.readlines()]

def process_p1(bank: str) -> int:
    max_not_end = 0
    for index, char in enumerate(bank):
        if index == len(bank) - 1:
            break
        if (pmax := int(char)) > max_not_end:
            max_not_end = pmax
    
    first_max_index = 0
    for index, char in enumerate(bank):
        if int(char) == max_not_end:
            first_max_index = index
            break
    
    post_max = 0
    for index, char in enumerate(bank[first_max_index + 1:]):
        if (pmax := int(char)) > post_max:
            post_max = pmax
    
    return 10 * max_not_end + post_max

def max_excluding_last(string: str, last: int) -> str:
    if last == 0:
        substr = string
    else:
        substr = string[:-last]
    if not substr:
        return None
    return max(substr)

def process_p2(bank: str) -> int:
    modbank = bank
    built = ""

    for i in range(11, -1, -1):
        biggest = max_excluding_last(modbank, i)
        built += biggest
        index = modbank.index(biggest)
        modbank = modbank[index + 1:]

    return int(built)


p1sum = 0
p2sum = 0
for bank in banks:
    p1sum += process_p1(bank)
    p2sum += process_p2(bank)

print(f"Part 1: {p1sum}")
print(f"Part 2: {p2sum}")