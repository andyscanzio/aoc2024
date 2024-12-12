from functools import cache

test1 = "0 1 10 99 999"
test2 = "125 17"
input = "8793800 1629 65 5 960 0 138983 85629"

stones = list(map(int, input.split(" ")))
print(stones)


@cache
def calculate(stone, step):
    if step == 0:
        return 1

    if stone == 0:
        return calculate(1, step - 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        l = len(s)
        a, b = s[0 : l // 2], s[l // 2 :]
        return calculate(int(a), step - 1) + calculate(int(b), step - 1)
    else:
        return calculate(stone * 2024, step - 1)


print(sum(calculate(stone, 75) for stone in stones))
