from itertools import combinations

with open("input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

len_y = len(grid)
len_x = len(grid[0])


def get_antinodes(
    p1: tuple[int, int], p2: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - (x2 - x1), y1 - (y2 - y1)), (x2 + (x2 - x1), y2 + (y2 - y1))


def is_valid_antinode(anti: tuple[int, int], max_x: int, max_y: int) -> bool:
    x, y = anti
    return 0 <= x < max_x and 0 <= y < max_y


antennas: dict[str, list[tuple[int, int]]] = {}

for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if item != ".":
            if item not in antennas:
                antennas[item] = [(x, y)]
            else:
                antennas[item].append((x, y))

antinodes = set()

for antenna in antennas.values():
    for first, second in combinations(antenna, 2):
        anti1, anti2 = get_antinodes(first, second)
        if is_valid_antinode(anti1, len_x, len_y):
            antinodes.add(anti1)
        if is_valid_antinode(anti2, len_x, len_y):
            antinodes.add(anti2)

print(len(antinodes))
