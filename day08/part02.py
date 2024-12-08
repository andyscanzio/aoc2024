from itertools import combinations

with open('input.txt','r') as file:
    grid = [list(line) for line in file.read().splitlines()]
    
len_y = len(grid)
len_x = len(grid[0])
    

def is_valid_antinode(anti:tuple[int, int], max_x:int, max_y:int)->bool:
    x, y = anti
    return  0<= x < max_x and 0<= y < max_y
    
def get_antinodes(p1:tuple[int, int], p2:tuple[int, int])->set[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    r = set()
    k = 0
    while True:
        t = x1 - k * dx,  y1 - k * dy
        if is_valid_antinode(t, len_x, len_y):
            r.add(t)
            k += 1
        else:
            break
    k = 0
    while True:
        t = x2 + k * dx,  y2 + k * dy
        if is_valid_antinode(t, len_x, len_y):
            r.add(t)
            k += 1
        else:
            break
    return r

    
antennas:dict[str, list[tuple[int, int]]] = {}
    
for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if item != '.':
            if item not in antennas:
                antennas[item] = [(x, y)]
            else:
                antennas[item].append((x, y))

antinodes = set()

for antenna in antennas.values():
    for first, second in combinations(antenna, 2):
        antinodes = antinodes | get_antinodes(first, second)
            
print(len(antinodes))