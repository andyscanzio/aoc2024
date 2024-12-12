from pathlib import Path

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

disk = []
id = 0
for i, size in enumerate(data):
    if i % 2 == 0:
        disk.extend([id] * int(size))
        id += 1
    else:
        disk.extend([None] * int(size))

left, right = 0, len(disk) - 1

while left < right:
    if disk[left] is not None:
        left += 1
    elif disk[right] is None:
        right -= 1
    else:
        disk[left], disk[right] = disk[right], disk[left]

res = sum(i * j for i, j in enumerate(disk) if j is not None)
print(res)
