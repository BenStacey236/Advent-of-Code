
def is_accessable(grid: str, pos: tuple[int, int]) -> bool:
    x, y = pos
    
    if grid[y][x] != '@':
        return False

    
    neighours = [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]
    
    blockedNeighbours = 0
    for xn, yn in neighours:
        if 0 <= yn < len(grid) and 0 <= xn < len(grid[0]) and grid[yn][xn] == '@':
            blockedNeighbours += 1

    return blockedNeighbours < 4


if __name__ == "__main__":
    filePath = "2025/Day4/puzzleInput.txt"
    grid: list[str] = []
    accessibleRolls: int = 0
    
    with open(filePath) as f:
        for line in f.readlines():
            grid.append(line.strip())

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_accessable(grid, (x, y)):
                accessibleRolls += 1
    
    print(accessibleRolls)