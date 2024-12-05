filePath = '2024/Day5/Day5Input.txt'

def isValidUpdate(update: str, updateRules: list[tuple[int, int]]):
    cache: list[int] = []
    
    updates = [int(i) for i in update.split(',')]
    for num in updates:
        cache.append(num)
        for rule1, rule2 in updateRules:
            if num == rule2 and rule1 in updates and rule1 not in cache:
                return 0
            
    return updates[(len(updates))//2]

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

middlePagesTotal: int = 0

for update in updates:
    middlePagesTotal += isValidUpdate(update, updateRules)

print(middlePagesTotal)