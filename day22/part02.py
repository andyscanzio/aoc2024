from functools import reduce
from pathlib import Path
from collections import deque


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()
data = map(int, data.splitlines())


def mix(num: int, secret: int) -> int:
    return num ^ secret


def prune(num: int) -> int:
    return num % 16777216


def next_secret(secret: int) -> int:
    secret = prune(mix(64 * secret, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(2048 * secret, secret))
    return secret


def chain(secret: int) -> dict[tuple[int, int, int, int], int]:
    prices: dict[tuple[int, int, int, int], int] = {}
    diffs: deque[int] = deque(maxlen=4)
    init_price = secret % 10
    for _ in range(2000):
        secret = next_secret(secret)
        final_price = secret % 10
        diff = final_price - init_price
        diffs.append(diff)
        init_price = final_price
        if len(diffs) == 4:
            key = (diffs[0], diffs[1], diffs[2], diffs[3])
            if key not in prices:
                prices[key] = final_price
    return prices


prices = list(map(chain, data))

only_keys = map(lambda x: x.keys(), prices)
final_keys = reduce(lambda x, y: x | y, only_keys)
total_max = 0
max_key = None
for key in final_keys:
    cur_max = 0

    for price in prices:
        cur_max += price.get(key, 0)

    if cur_max > total_max:
        total_max = cur_max
        max_key = key

print(total_max, max_key)
