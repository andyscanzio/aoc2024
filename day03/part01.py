import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

with open("input.txt", "r") as file:
    text = file.read()

match = pattern.findall(text)
res = sum(int(a) * int(b) for (a, b) in match)
print(res)
