filePath = 'Day1/Day1Input.txt'

list1: list[int] = []
list2: list[int] = []

with open(filePath) as f:
    for line in f.readlines():
        list1.append(int(line.strip('\n').split()[0]))
        list2.append(int(line.strip('\n').split()[1]))

counter: dict[int: int] = {}
for number in list2:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

similarity: int = 0

for number in list1:
    if number in counter:
        similarity += number * counter[number]

print(similarity)