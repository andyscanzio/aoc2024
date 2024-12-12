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


def reorder(update, rules):
    corrected = True
    while corrected:
        corrected = False
        for i, page in enumerate(update):
            for a, b in rules:
                if page == a and b in update:
                    j = update.index(b)
                    if i > j:
                        corrected = True
                        update[i], update[j] = update[j], update[i]


res = 0
for update in updates:
    if not right_order(update, rules):
        reorder(update, rules)
        res += int(update[len(update) // 2])

print(res)
