from pathlib import Path
from pprint import pprint
from queue import Queue


folder = Path(__file__).parent
test = folder / "test.txt"
test2 = folder / "test2.txt"
test3 = folder / "test3.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()


def show_grid(px, py, grid):
    for row in grid:
        print("".join(row))


grid, sequence = data.split("\n\n")
_grid = [list(row) for row in grid.splitlines()]
subst = {"#": ["#", "#"], "O": ["[", "]"], ".": [".", "."], "@": ["@", "."]}
grid = []
for row in _grid:
    _row = []
    for item in row:
        _row.extend(subst[item])
    grid.append(_row)
sequence = "".join(sequence.split("\n"))

px, py = (0, 0)

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == "@":
            px, py = (j, i)

dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}


def move_and_push(grid, start_r, start_c, dr, dc) -> tuple[int, int]:
    """Determines if the move is valid. If so, pushes all of the boxes that are in the
    way of the direction of travel. Returns the next position of the robot."""
    stack = []
    path = [(start_r, start_c)]
    visited = set()
    while path:
        r, c = path.pop()
        if (r, c) in visited or grid[r][c] == ".":
            continue
        visited.add((r, c))
        if grid[r][c] == "#":
            return (start_r, start_c)
        stack.append(((grid[r][c], r, c)))
        path.append((r + dr, c + dc))
        if grid[r][c] == "[":
            path.append((r, c + 1))
        if grid[r][c] == "]":
            path.append((r, c - 1))
    if dr > 0:
        stack.sort(key=lambda path: path[1])
    if dr < 0:
        stack.sort(key=lambda path: -path[1])
    if dc > 0:
        stack.sort(key=lambda path: path[2])
    if dc < 0:
        stack.sort(key=lambda path: -path[2])

    while stack:
        char, old_r, old_c = stack.pop()
        grid[old_r + dr][old_c + dc] = char
        grid[old_r][old_c] = "."

    return (start_r + dr, start_c + dc)


for move in sequence:
    dx, dy = dirs[move]
    py, px = move_and_push(grid, py, px, dy, dx)


res = 0
for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == "[":
            res += 100 * i + j
print(res)
