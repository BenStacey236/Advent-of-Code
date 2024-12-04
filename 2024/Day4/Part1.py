filePath = '2024/Day4/Day4Input.txt'

wordsearch: list[str] = []
numOccurrences: int = 0

def count_occurrences(line: str):
    occurrences: int = 0
    for quad in [line[start:start+4] for start in range(len(line)) if start+4 < len(line)+1]:
        if quad == "XMAS" or quad == "SAMX":
            occurrences += 1
    
    return occurrences


with open(filePath) as f:
    wordsearch = f.readlines()

numRows: int = len(wordsearch)
numColumns: int = len(wordsearch[0])-1

# Checking all rows
for row in wordsearch:
    numOccurrences += count_occurrences(row)

# Checking all columns
for column in [''.join([wordsearch[row][col] for row in range(numRows)]) for col in range(numColumns)]:
    numOccurrences += count_occurrences(column)

# Checking diagonals
diagonals: list[str] = []

for d in range(numRows + numColumns - 1):
        diagonal: list[str] = []
        for i in range(max(0, d - numColumns + 1), min(d + 1, numRows)):
            diagonal.append(wordsearch[i][d - i])
        diagonals.append(''.join(diagonal))

for d in range(numRows + numColumns - 1):
        diagonal: list[str] = []
        for i in range(max(0, d - numColumns + 1), min(d + 1, numRows)):
            diagonal.append(wordsearch[i][numColumns - 1 - (d - i)])
        diagonals.append(''.join(diagonal))

for diagonal in diagonals:
    numOccurrences += count_occurrences(diagonal)

print(numOccurrences)

