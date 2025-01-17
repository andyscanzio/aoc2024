from pathlib import Path
from re import compile


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

BUTTON_PATTERN = compile(r"Button (?:A|B): X\+(\d+), Y\+(\d+)")
PRIZE_PATTERN = compile(r"Prize: X=(\d+), Y=(\d+)")


def parse(machine: str) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    t = machine.splitlines()
    a = BUTTON_PATTERN.match(t[0])
    if a is not None:
        a = tuple(map(int, a.groups()))
    else:
        a = (0, 0)
    b = BUTTON_PATTERN.match(t[1])
    if b is not None:
        b = tuple(map(int, b.groups()))
    else:
        b = (0, 0)
    p = PRIZE_PATTERN.match(t[2])
    if p is not None:
        p = tuple(map(int, p.groups()))
    else:
        p = (0, 0)
    return (a, b, p)


def credits(machine: str) -> int:
    (ax, ay), (bx, by), (px, py) = parse(machine)
    det = ax * by - ay * bx

    ka = (px * by - py * bx) / det
    if not ka.is_integer():
        return 0

    kb = (py * ax - px * ay) / det
    if not kb.is_integer():
        return 0
    return int(3 * ka + kb)


machines = [credits(machine) for machine in data.split("\n\n")]

print(sum(machines))
