from pathlib import Path
from pprint import pprint
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


def shortest_path_with_turns(maze, start, end, turn_penalty):
    rows, cols = len(maze), len(maze[0])
    directions = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
    pq = []
    heappush(pq, (0, start[0], start[1], "RIGHT"))
    visited = set()
    while pq:
        cost, x, y, current_direction = heappop(pq)
        if (x, y) == end:
            return cost
        if (x, y, current_direction) in visited:
            continue
        visited.add((x, y, current_direction))
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[ny][nx] in (".", "S", "E"):
                new_cost = (
                    cost + (turn_penalty if current_direction != direction else 0) + 1
                )
                heappush(pq, (new_cost, nx, ny, direction))
    return -1


result = shortest_path_with_turns(grid, start, end, 1000)
print(result)
