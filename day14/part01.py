from functools import reduce
from operator import mul
from pathlib import Path
from re import compile


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

ROBOT_PATTERN = compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

lx, ly = 101, 103
# lx, ly = 11, 7


def parse(robot: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    match = ROBOT_PATTERN.match(robot)
    assert match is not None
    gr = match.groups()
    assert gr is not None
    px, py, vx, vy = tuple(map(int, gr))
    return (px, py), (vx, vy)


def move(px: int, py: int, vx: int, vy: int, t: int) -> tuple[int, int]:
    nx, ny = (px + t * vx) % lx, (py + t * vy) % ly
    return (nx, ny)


def simulate(
    t: int, robots: list[tuple[tuple[int, ...], tuple[int, ...]]]
) -> list[tuple[int, int]]:
    return [move(px, py, vx, vy, t) for (px, py), (vx, vy) in robots]


robots = [parse(robot) for robot in data.splitlines()]


q = [0, 0, 0, 0]
for x, y in simulate(100, robots):
    if x < lx // 2 and y < ly // 2:
        q[0] += 1
    elif x > lx // 2 and y < ly // 2:
        q[1] += 1
    elif x > lx // 2 and y > ly // 2:
        q[2] += 1
    elif x < lx // 2 and y > ly // 2:
        q[3] += 1

print(reduce(mul, q, 1))
