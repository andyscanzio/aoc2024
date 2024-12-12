with open("input.txt", "r") as file:
    lines = [i.removesuffix("\n").split("   ") for i in file.readlines()]

left = sorted([int(x) for (x, _) in lines])
right = sorted([int(x) for (_, x) in lines])

res = sum(abs(a - b) for (a, b) in zip(left, right))
print(res)
