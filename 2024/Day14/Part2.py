filePath: str = '2024/Day14/Day14Input.txt'

class Robot:
    def __init__(self, pos: tuple[int, int], vel: tuple[int, int]) -> None:
        self.pos: tuple[int, int] = pos
        self.vel: tuple[int, int] = vel

    
    def move(self, grid: list[list[str]]) -> None:
        height: int = len(grid)
        width: int = len(grid[0])

        self.pos = self.add_tuple(self.pos, self.vel)
        self.pos = (self.pos[0]%width, self.pos[1]%height)

    
    def add_tuple(self, tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
        x1, x2 = tup1
        y1, y2 = tup2

        return (x1+y1, x2+y2)


def is_christmas_tree(grid: list[list[int]]) -> bool:
    for row in grid:
        if '1111111' in ''.join([str(i) for i in row]):
            return True

    return False


robots: list[Robot] = []

with open(filePath) as f:
    for line in f.readlines():
        x, y = line.strip('\n').split()[0][2:].split(',')
        pos: tuple[int, int] = (int(x), int(y))

        x, y = line.strip('\n').split()[1][2:].split(',')
        vel: tuple[int, int] = (int(x), int(y))
        
        robots.append(Robot(pos, vel))


elapsedSeconds: int = 0

while True:
    grid: list[list[str]] = [[0 for i in range(101)] for j in range(103)]
    elapsedSeconds += 1

    for robot in robots:
        robot.move(grid)
        grid[robot.pos[1]][robot.pos[0]] += 1

    if is_christmas_tree(grid): break


for row in grid:
    print(''.join(['.' if tile == 0 else str(tile) for tile in row]))

print(f'Elapsed Time: {elapsedSeconds}')