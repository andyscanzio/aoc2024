import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)")

with open("input.txt", "r") as file:
    text = file.read()

match = pattern.findall(text)
do_mult = True
res = 0
for a, b, do, dont in match:
    if do:
        do_mult = True
    elif dont:
        do_mult = False
    elif do_mult:
        res += int(a) * int(b)
print(res)
