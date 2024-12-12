from tqdm import tqdm


test1 = "0 1 10 99 999"
test2 = "125 17"
input = "8793800 1629 65 5 960 0 138983 85629"

stones = list(map(int, input.split(" ")))
print(stones)

for _ in tqdm(range(25)):
    temp = []
    for stone in stones:
        if stone == 0:
            temp.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            l = len(s)
            a, b = s[0 : l // 2], s[l // 2 :]
            temp.extend((int(a), int(b)))
        else:
            temp.append(2024 * stone)
    stones = temp
print(len(stones))
