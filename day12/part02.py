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


def count_common_sides(region):
    ct = 0
    for x, y in region:
        if (x - 1, y) in region:
            for y2 in [y - 1, y + 1]:
                if (x, y2) not in region and (x - 1, y2) not in region:
                    ct += 1
        if (x, y - 1) in region:
            for x2 in [x - 1, x + 1]:
                if (x2, y) not in region and (x2, y - 1) not in region:
                    ct += 1
    return ct


def perimeter(region):
    a = 4 * len(region)
    for (ax, ay), (bx, by) in combinations(region, 2):
        a -= (
            2
            if (ax == bx and abs(ay - by) == 1) or (ay == by and abs(ax - bx) == 1)
            else 0
        )
    return a


def sides(region):
    return perimeter(region) - count_common_sides(region)


def price(region):
    return sides(
        region,
    ) * len(region)


regions = []

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if (x, y) not in visited:
            regions.append(bfs(grid, x, y, grid[y][x], visited))


print(sum(map(price, regions)))
