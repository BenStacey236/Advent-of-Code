filePath = '2024/Day4/Day4Input.txt'

wordsearch: list[str] = []
numOccurrences: int = 0

def count_occurrences(grid: list[str], row: int, col: int):
    occurrences: int = 0
    
    if row-1 < 0 or col-1 < 0:
        return 0

    try:
        d1 = ''.join([grid[row-1][col-1], grid[row][col], grid[row+1][col+1]])
        d2 = ''.join([grid[row-1][col+1], grid[row][col], grid[row+1][col-1]])

        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            occurrences = 1
    except:
        pass
    
    return occurrences


with open(filePath) as f:
    wordsearch = f.readlines()

numRows: int = len(wordsearch)
numColumns: int = len(wordsearch[0])-1

for row in range(numRows):
    for col in range(numColumns):
        numOccurrences += count_occurrences(wordsearch, row, col)

print(numOccurrences)