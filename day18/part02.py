from pathlib import Path
from collections import deque
from time import sleep

from tqdm import tqdm

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

width, height = 71, 71

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

fallen = [tuple(map(int, item.split(","))) for item in data.splitlines()]

start = 0, 0
end = width - 1, height - 1

for i, item in enumerate(fallen):
    if i < 1024:
        continue
    queue = deque()
    explored = {start}
    queue.append((start, []))
    found = False
    fallen_set = set(fallen[: i + 1])
    while len(queue) > 0:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            found = True
            break
        else:
            for dx, dy in dirs:
                tx = x + dx
                ty = y + dy
                if (
                    0 <= tx < width
                    and 0 <= ty < height
                    and (tx, ty) not in fallen_set
                    and (tx, ty) not in explored
                ):
                    explored.add((tx, ty))
                    queue.append(((tx, ty), path + [(x, y)]))
    if not found:
        a, b = item
        print(f"{a},{b}")
        break
