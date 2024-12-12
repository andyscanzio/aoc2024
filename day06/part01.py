with open("input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

lx = len(grid)
ly = len(grid[0])

cx, cy, direction = 0, 0, "^"

for y, row in enumerate(grid):
    for x, spot in enumerate(row):
        if spot == "^":
            cx, cy, direction = x, y, spot


visited = {(cx, cy, direction)}

has_visited = False

while not has_visited:
    nx, ny = cx, cy
    match direction:
        case "^":
            nx, ny = cx, cy - 1
        case ">":
            nx, ny = cx + 1, cy
        case "v":
            nx, ny = cx, cy + 1
        case "<":
            nx, ny = cx - 1, cy

    if ny >= ly or nx >= lx or ny < 0 or nx < 0:
        has_visited = True
    elif grid[ny][nx] == "#":
        match direction:
            case "^":
                direction = ">"
            case ">":
                direction = "v"
            case "v":
                direction = "<"
            case "<":
                direction = "^"
    else:
        cx, cy = nx, ny

    if (cx, cy, direction) in visited:
        has_visited = True
    else:
        visited.add((cx, cy, direction))


s = {(x, y) for (x, y, _) in visited}
print(s)
print(len(s))
