from collections import deque
from pathlib import Path
from itertools import combinations


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

grid = [[item for item in row] for row in data.splitlines()]
lx, ly = len(grid), len(grid[0])

visited = set()

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def neigbors(x, y, grid):
    return [
        (x + dx, y + dy)
        for dx, dy in directions
        if 0 <= x + dx < lx and 0 <= y + dy < ly
    ]


def bfs(grid, sx, sy, type, explored):
    queue = deque([(sx, sy)])
    explored.add((sx, sy))
    region = [(sx, sy)]
    while len(queue) > 0:
        (x, y) = queue.popleft()
        for nx, ny in neigbors(x, y, grid):
            if (nx, ny) not in explored and grid[ny][nx] == type:
                explored.add((nx, ny))
                region.append((nx, ny))
                queue.append((nx, ny))
    return region


def perimeter(region):
    a = 4 * len(region)
    for (ax, ay), (bx, by) in combinations(region, 2):
        a -= (
            2
            if (ax == bx and abs(ay - by) == 1) or (ay == by and abs(ax - bx) == 1)
            else 0
        )
    return a


def price(region):
    return len(region) * perimeter(region)


regions = []

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if (x, y) not in visited:
            regions.append(bfs(grid, x, y, grid[y][x], visited))


print(sum(map(price, regions)))
