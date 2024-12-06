filePath = '2024/Day6/Day6Input.txt'


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

        newPos = move_guard(grid, guardPos, guardDirection)[0]

    grid[guardPos[0]][guardPos[1]] = 'X'

    return newPos, guardDirection
            


directions: dict[str:tuple[int, int]] = {'^': (-1, 0), '>': (0, 1), 'v':(1, 0), '<': (0, -1)}
grid: list[list[str]] = []

with open(filePath) as f:
    for line in f.readlines():
        grid.append([char for char in line.strip('\n')])

guardPos: tuple[int, int] = get_guard_pos(grid)
guardDirection: str = grid[guardPos[0]][guardPos[1]]

while is_in_grid(grid, guardPos):
    guardPos, guardDirection = move_guard(grid, guardPos, guardDirection)

totalVisited: int = 0

for row in grid:
    totalVisited += row.count('X')

print(totalVisited)

