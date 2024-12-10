from pathlib import Path

folder = Path(__file__).parent 
test = folder / 'test.txt'
input = folder / 'input.txt'

with open(input, 'r') as file:
    data = file.read()
    
lines = [list(map(int,line)) for line in data.splitlines()]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def score(x, y, field, targets):
    temp = field[y][x]
    if temp == 9 and (x, y) not in targets:
        targets.add((x, y))
        return 1
    ret = 0
    for dx, dy in dirs:
        tx, ty = x + dx, y + dy
        if 0 <= tx < len(field[0]) and 0 <= ty < len(field) and field[ty][tx] - temp == 1:
            ret += score(tx, ty, field, targets)
    return ret
  
res = 0
for y, row in enumerate(lines):
    for x, item in enumerate(row):
        if item == 0:
            res += score(x, y, lines, set())
print(res)

