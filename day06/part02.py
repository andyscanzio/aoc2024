from tqdm import tqdm

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

res = 0
for x, y in tqdm(s):
    cx, cy, direction = 0, 0, "^"

    for a, row in enumerate(grid):
        for b, spot in enumerate(row):
            if spot == "^":
                cx, cy, direction = b, a, spot

    visited = {(cx, cy, direction)}

    while True:
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
            break
        elif grid[ny][nx] == "#" or (nx == x and ny == y):
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
            res += 1
            break
        else:
            visited.add((cx, cy, direction))


print(res)
