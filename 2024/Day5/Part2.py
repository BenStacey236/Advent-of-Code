filePath = '2024/Day5/Day5Input.txt'

def isValidUpdate(update: str, updateRules: list[tuple[int, int]]) -> bool:
    cache: list[int] = []
    
    updates = [int(i) for i in update.split(',')]
    for num in updates:
        cache.append(num)
        for rule1, rule2 in updateRules:
            if num == rule2 and rule1 in updates and rule1 not in cache:
                return False
            
    return True


def sortInvalidUpdate(update: str, updateRules: str) -> list[int]:
    updates = [int(i) for i in update.split(',')]
    changes: int = 0

    for i, num in enumerate(updates):
        num2 = updates[i-1]
        for rule1, rule2 in updateRules:
            if i != 0 and (num == rule1 or num == rule2) and (num2 == rule1 or num2 == rule2):
                if num == rule1:
                    changes += 1
                    updates[i-1], updates[i] = num, num2

    if changes > 0:
        updates = sortInvalidUpdate(','.join([str(i) for i in updates]), updateRules)

    return updates


updateRules: list[tuple[int, int]] = []
updates: list[str] = []

with open(filePath) as f:
    isRules: bool = True
    for line in f.readlines():
        if line == "\n":
            isRules = False

        elif isRules:
            rule = line.split('|')
            updateRules.append((int(rule[0]), int(rule[1])))

        else:
            updates.append(line.strip('\n'))

sortedMids: int = 0

for update in updates:
    if not isValidUpdate(update, updateRules):
        sortedUpdates = sortInvalidUpdate(update, updateRules)
        sortedMids += sortedUpdates[len(sortedUpdates)//2]

print(sortedMids)
