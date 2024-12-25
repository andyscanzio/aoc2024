from pathlib import Path

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

inputs = [element.splitlines() for element in data.split("\n\n")]


def convert(matrix: list[list[str]]) -> list[int]:
    return [line.count("#") for line in zip(*matrix)]


keys = [convert(key[1:-1]) for key in inputs if key[0][0] == "."]
locks = [convert(lock[1:-1]) for lock in inputs if lock[0][0] == "#"]


res = 0
for lock in locks:
    for key in keys:
        res += all(k + l <= 5 for k, l in zip(key, lock))

print(res)
