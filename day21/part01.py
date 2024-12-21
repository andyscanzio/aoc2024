from itertools import permutations
from pathlib import Path


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

data = data.splitlines()

numeric_keypad = {
    "7": 0j + 0,
    "8": 0j + 1,
    "9": 0j + 2,
    "4": 1j + 0,
    "5": 1j + 1,
    "6": 1j + 2,
    "1": 2j + 0,
    "2": 2j + 1,
    "3": 2j + 2,
    "0": 3j + 1,
    "A": 3j + 2,
}

directional_keypad = {
    "^": 0j + 1,
    "A": 0j + 2,
    "<": 1j + 0,
    "v": 1j + 1,
    ">": 1j + 2,
}
DIRECTIONS = {"^": -1j + 0, ">": 0j + 1, "v": 1j + 0, "<": 0j - 1}


def find_sequence(
    code: str,
    depth: int,
    is_directional: bool = False,
    current: complex | None = None,
) -> int:
    if not code:
        return 0
    keypad = directional_keypad if is_directional else numeric_keypad

    start_point = current if current is not None else keypad["A"]
    end_point = keypad[code[0]]
    path = end_point - start_point
    dx, dy = int(path.real), int(path.imag)
    moves = "v" * dy if dy > 0 else "^" * (-dy)
    moves += ">" * dx if dx > 0 else "<" * (-dx)

    if not depth:
        a = len(moves) + 1 + find_sequence(code[1:], depth, is_directional, end_point)
        return a

    candidates = []
    for permutation in set(permutations(moves)):
        new_start_point = current if current is not None else keypad["A"]
        for move in permutation:
            d = DIRECTIONS[move]
            new_start_point = new_start_point + d

            if new_start_point not in keypad.values():
                break
        else:
            candidates.append(
                find_sequence("".join(permutation) + "A", depth - 1, True)
            )
    min_len = min(candidates) if candidates else -1
    assert min_len > 0, f"Invalid sequence: {code}"
    return min_len + find_sequence(code[1:], depth, is_directional, end_point)


def score(code: str) -> int:
    return int(code[:-1]) * find_sequence(code, 2)


print(sum(map(score, data)))
