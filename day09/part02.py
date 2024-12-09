from pathlib import Path
from tqdm import tqdm

folder = Path(__file__).parent 
test = folder / 'test.txt'
input = folder / 'input.txt'

with open(input, 'r') as file:
    data = file.read()
    
disk = []
id = 0
for i, size in enumerate(data):
    if i % 2 == 0:
        disk.extend([id] * int(size))
        id += 1
    else:
        disk.extend([None] * int(size))

right = len(disk) - 1
file, space = 0, 0

for right in tqdm(range(len(disk) - 1, 1, -1)):
    if disk[right - 1] == disk[right]:
        file += 1
    elif disk[right] is None:
        file = 0
    else:
        left = 0
        while left < right:
            if all(i is None for i in disk[left : left + file + 1]):
                disk[left : left + file + 1], disk[right : right + file + 1] = disk[right : right + file + 1], disk[left : left + file + 1]
                break
            left += 1
        file = 0
    right -= 1
        
        

res = sum(i * j for i, j in enumerate(disk) if j is not None)
print(res)

