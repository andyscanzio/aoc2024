from collections import defaultdict
from pathlib import Path
from heapq import heappush, heappop

folder = Path(__file__).parent
test = folder / "test.txt"
test2 = folder / "test2.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

start = (0, 0)
end = (0, 0)
grid = [list(row) for row in data.splitlines()]
for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if item == "S":
            start = (x, y)
        elif item == "E":
            end = (x, y)

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


def find_all_lowest_cost_paths(grid, start, end, turn_penalty):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heappush(pq, (0, start, None, [start]))

    min_cost = defaultdict(lambda: float("inf"))
    paths = defaultdict(list)

    min_cost[(start, None)] = 0
    paths[(start, None)].append([start])

    lowest_cost = float("inf")
    lowest_cost_paths = []

    while pq:
        cost, (x, y), prev_dir, path = heappop(pq)

        if (x, y) == end:
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_paths = [path]
            elif cost == lowest_cost:
                lowest_cost_paths.append(path)
            continue

        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[ny][nx] != "#":
                new_cost = cost + 1
                if prev_dir and prev_dir != direction:
                    new_cost += turn_penalty

                if new_cost <= min_cost[((nx, ny), direction)]:
                    min_cost[((nx, ny), direction)] = new_cost

                    new_path = path + [(nx, ny)]
                    paths[((nx, ny), direction)].append(new_path)

                    heappush(pq, (new_cost, (nx, ny), direction, new_path))

    return lowest_cost_paths


paths = find_all_lowest_cost_paths(grid, start, end, 1000)

all_paths = set()
for path in paths:
    all_paths.update(path)

print(len(all_paths))
