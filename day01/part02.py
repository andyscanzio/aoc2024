from collections import Counter

with open("input    .txt", "r") as file:
    lines = [i.removesuffix("\n").split("   ") for i in file.readlines()]

left = [int(x) for (x, _) in lines]
right = Counter([int(x) for (_, x) in lines])

res = sum(l * right[l] for l in left)
print(res)
