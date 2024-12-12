with open("input.txt", "r") as file:
    lines = file.read().splitlines()

split_idx = lines.index("")
rules = [tuple(line.split("|")) for line in lines[:split_idx]]
updates = [line.split(",") for line in lines[split_idx + 1 :]]


def right_order(update, rules):
    for a, b in rules:
        if a in update and b in update and update.index(a) > update.index(b):
            return False
    return True


res = 0
for update in updates:
    if right_order(update, rules):
        res += int(update[len(update) // 2])

print(res)
