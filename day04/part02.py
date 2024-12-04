with open('input.txt', 'r') as file:
    field = file.read().splitlines()

def get_cross(field, x, y):
    return field[y][x] + field[y][x+2] + field[y+1][x+1] + field[y+2][x] + field[y+2][x+2]

res = 0
for y, row in enumerate(field):
    for x, char in enumerate(row):
        if len(field)  >= 3 + y and len(row) >= 3 + x:
            cross = get_cross(field, x, y)
            res += cross == 'MMASS'
            res += cross == 'MSAMS'
            res += cross == 'SMASM'
            res += cross == 'SSAMM'
            
print(res)