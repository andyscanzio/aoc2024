from itertools import pairwise


def is_safe(line: list[int]) -> bool:
    if line[1] == line[0]:
        return False
    sign = (line[1] - line[0]) // abs(line[1] - line[0])
    for a, b in pairwise(line):
        if b == a:
            return False
        if (b - a) // abs(b - a) != sign:
            return False
        if abs(b - a) > 3:
            return False
    return True


def is_safe_damp(line: list[int]) -> bool:
    if is_safe(line):
        return True
    for i in range(len(line)):
        temp = [x for j, x in enumerate(line) if j != i]
        if is_safe(temp):
            return True
    return False


with open("input.txt", "r") as file:
    res = sum(
        is_safe_damp(list(map(int, line.rstrip("\n").split(" ")))) for line in file
    )
print(res)
