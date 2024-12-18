from pathlib import Path
from collections import deque

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

width, height = 71, 71
steps = 1024

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

fallen = set([tuple(map(int, item.split(","))) for item in data.splitlines()][:steps])

start = 0, 0
end = width - 1, height - 1

queue = deque()
explored = {start}
queue.append((start, []))
while len(queue) > 0:
    (x, y), path = queue.popleft()
    if (x, y) == end:
        print(len(path))
        break
    else:
        for dx, dy in dirs:
            tx = x + dx
            ty = y + dy
            if (
                0 <= tx < width
                and 0 <= ty < height
                and (tx, ty) not in fallen
                and (tx, ty) not in explored
            ):
                explored.add((tx, ty))
                queue.append(((tx, ty), path + [(x, y)]))
