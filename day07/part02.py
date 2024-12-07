from itertools import product
from tqdm import tqdm
import re

    
with open('input.txt') as file:
    input = [
        [int(x) for x in re.findall(r"\d+", line)]
        for line in  file.read().strip().splitlines()
    ]
calc = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '.': lambda a, b: int(f"{a}{b}"),
}

def solve(symbols):
    sum = 0

    for left, *nums in tqdm(input):
        first, *rest = nums
        for ops in product(symbols, repeat=len(rest)):
            right = first
            for op, num in zip(ops, rest):
                if right > left:
                    continue
                right = calc[op](right, num)
            if left == right:
                sum += left
                break
    return sum


print(solve('+*.'))