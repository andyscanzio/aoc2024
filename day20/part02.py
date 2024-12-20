from copy import deepcopy
from pathlib import Path


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

start, end = 0, 0

maze: dict[complex, str] = {}
for y, line in enumerate(data.splitlines()):
    for x, ch in enumerate(line):
        maze[y + x * 1j] = ch
        if ch == "S":
            start = y + x * 1j
        if ch == "E":
            end = y + x * 1j


def best(
    maze: dict[complex, str],
    current: complex,
    end: complex,
) -> dict[complex, int]:
    visited: dict[complex, int] = {current: 0}
    while current != end:
        [new] = [
            n
            for d in [-1, 1, 1j, -1j]
            if maze[(n := current + d)] != "#" and n not in visited
        ]
        visited[new] = visited[current] + 1
        current = new
    return visited


def find_cheats(
    track: dict[complex, int],
    max_d: int = 20,
    max_save: int = 99,
) -> int:
    cheats = 0
    for k, v in list(track.items()):
        for k1, v1 in track.items():
            if 0 < (cur_dist := abs((d := k1 - k).real) + abs(d.imag)) <= max_d:
                if abs(v1 - v) - cur_dist > max_save:
                    cheats += 1
        del track[k]
    return cheats


track = best(maze, start, end)
print(find_cheats(deepcopy(track), 20))
