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


with open("input.txt", "r") as file:
    res = sum(is_safe(list(map(int, line.rstrip("\n").split(" ")))) for line in file)
print(res)
