from pathlib import Path


folder = Path(__file__).parent
test = folder / "test.txt"
test2 = folder / "test2.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()


grid, sequence = data.split("\n\n")
grid = [list(row) for row in grid.splitlines()]
sequence = "".join(sequence.split("\n"))

px, py = (0, 0)

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == "@":
            px, py = (j, i)
            grid[py][px] = "."

dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}

for move in sequence:
    dx, dy = dirs[move]
    tx, ty = dirs[move]
    while grid[py + ty][px + tx] == "O":
        tx += dx
        ty += dy
    if grid[py + ty][px + tx] == ".":
        grid[py + ty][px + tx], grid[py + dy][px + dx] = (
            grid[py + dy][px + dx],
            grid[py + ty][px + tx],
        )
        px += dx
        py += dy

res = 0
for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item == "O":
            res += 100 * i + j
print(res)
