
def is_accessable(grid: list[str], pos: tuple[int, int]) -> bool:
    x, y = pos
    
    if grid[y][x] != '@':
        return False

    neighours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    
    blockedNeighbours = 0
    for xn, yn in neighours:
        if 0 <= yn < len(grid) and 0 <= xn < len(grid[0]) and grid[yn][xn] == '@':
            blockedNeighbours += 1

    return blockedNeighbours < 4


def complete_pass(grid: list[str]) -> tuple[list[str], int]:
    accessibleRolls: int = 0
    indexes: set[tuple[int, int]] = set()

    newGrid: list[str] = []
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if is_accessable(grid, (x, y)):
                accessibleRolls += 1
                row += 'X'
            else:
                row += grid[y][x]

        newGrid.append(row)
    
    return newGrid, accessibleRolls


if __name__ == "__main__":
    filePath = "2025/Day4/puzzleInput.txt"
    grid: list[str] = []
    total: int = 0
    prev: int = 0
    
    with open(filePath) as f:
        for line in f.readlines():
            grid.append(line.strip())

    while True:  
        grid, collected = complete_pass(grid)
        total += collected
        if collected == prev:
            break
    
    print(total)