from pathlib import Path
from functools import cache

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

pieces, designs = data.split('\n\n')
pieces = pieces.split(', ')
designs = designs.splitlines()

@cache
def is_doable(design:str)->bool:
    if not design:
        return True
    for piece in pieces:
        if design.startswith(piece):
            res = is_doable(design[len(piece):])
            if res:
                return True
    return False

print(sum(map(is_doable, designs)))