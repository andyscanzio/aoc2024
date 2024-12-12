from operator import add, mul
from itertools import product

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


def is_valid(tot: int, args: list[int]) -> bool:
    possibilities = product((add, mul), repeat=len(args) - 1)
    for ops in possibilities:
        temp = args[0]
        for i, op in enumerate(ops):
            temp = op(temp, args[i + 1])
            if temp == tot:
                return True
    return False


res = 0
for line in lines:
    tot, args = line.split(":")
    args = list(map(int, args.split()))
    tot = int(tot)
    if is_valid(tot, args):
        res += tot
print(res)
