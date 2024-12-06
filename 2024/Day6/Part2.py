filePath = '2024/Day6/Day6Input.txt'

directions: dict[str:tuple[int, int]] = {'^': (-1, 0), '>': (0, 1), 'v':(1, 0), '<': (0, -1)}
grid: list[list[str]] = []

def get_guard_pos(grid: list[list[str]]) -> tuple[int, int]:
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '^' or cell == '>' or cell == 'v' or cell == '<':
                return (x, y)
    
    return None


def add_tuple(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    x1, x2 = tup1
    y1, y2 = tup2

    return (x1+y1, x2+y2)


def is_in_grid(grid: list[list[str]], guardPos: tuple[int, int]) -> bool:
    gridHeight: int = len(grid)
    gridWidth: int = len(grid[0])

    y, x = guardPos

    if y < 0 or y >= gridHeight:
        return False
    
    if x < 0 or x >= gridWidth:
        return False
    
    return True


def move_guard(grid: list[list[str]], guardPos: tuple[int, int], guardDirection: str):
    newPos: tuple[int, int] = add_tuple(guardPos, directions[guardDirection])

    if not is_in_grid(grid, newPos):
        grid[guardPos[0]][guardPos[1]] = 'X'
        return newPos, guardDirection
    
    if grid[newPos[0]][newPos[1]] == '#':
        match (guardDirection):
            case '^':
                guardDirection = '>'
            case '>':
                guardDirection = 'v'
            case 'v':
                guardDirection = '<'
            case '<':
                guardDirection = '^'

        newPos, guardDirection = move_guard(grid, guardPos, guardDirection)

    grid[guardPos[0]][guardPos[1]] = 'X'
    grid[newPos[0]][newPos[1]] = guardDirection

    return newPos, guardDirection


def load_grid(filePath: str):
    grid = []
    
    with open(filePath) as f:
        for line in f.readlines():
            grid.append([char for char in line.strip('\n')])

    return grid


def contains_cycle(xObs: int, yObs: int) -> bool:
    grid = load_grid(filePath)
    guardPos: tuple[int, int] = get_guard_pos(grid)
    guardDirection: str = grid[guardPos[0]][guardPos[1]]
    gridSize: int = len(grid) * len(grid[0])

    if (xObs, yObs) == guardPos:
        return False
    elif grid[xObs][yObs] == '#':
        return False
    
    grid[xObs][yObs] = '#'

    while is_in_grid(grid, guardPos):
        guardPos, guardDirection= move_guard(grid, guardPos, guardDirection)
        gridSize -= 1

        if gridSize <= 0:
            return True
        
    return False


cyclePositions: int = 0
iterGrid = load_grid(filePath)
height: int = len(iterGrid)
width: int = len(iterGrid[0])

for x in range(height):
    for y in range(width):
        if contains_cycle(x, y):
            cyclePositions += 1

print(cyclePositions)