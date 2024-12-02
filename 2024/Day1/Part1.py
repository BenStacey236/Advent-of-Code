filePath = '2024/Day1/Day1Input.txt'

list1: list[int] = []
list2: list[int] = []

with open(filePath) as f:
    for line in f.readlines():
        list1.append(int(line.strip('\n').split()[0]))
        list2.append(int(line.strip('\n').split()[1]))

list1.sort()
list2.sort()

totalDifference: int = 0

for (l1, l2) in zip(list1, list2):
    totalDifference += abs(l1-l2)

print(totalDifference)