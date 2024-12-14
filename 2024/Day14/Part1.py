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


def calc_safety(grid: list[list[int]]):
    safetyTL: int = 0
    safetyTR: int = 0
    safetyBL: int = 0
    safetyBR: int = 0
    
    midY: int = len(grid)//2
    midX: int = len(grid[0])//2

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if y < midY and x < midX:
                safetyTL += tile

            elif y < midY and x > midX:
                safetyTR += tile

            elif y > midY and x < midX:
                safetyBL += tile

            elif y > midY and x > midX:
                safetyBR += tile

    return safetyTL * safetyTR * safetyBL * safetyBR


grid: list[list[str]] = [[0 for i in range(101)] for j in range(103)]
robots: list[Robot] = []

with open(filePath) as f:
    for line in f.readlines():
        x, y = line.strip('\n').split()[0][2:].split(',')
        pos: tuple[int, int] = (int(x), int(y))

        x, y = line.strip('\n').split()[1][2:].split(',')
        vel: tuple[int, int] = (int(x), int(y))
        
        robots.append(Robot(pos, vel))


for i in range(100):
    for robot in robots:
        robot.move(grid)


for robot in robots:
    grid[robot.pos[1]][robot.pos[0]] += 1

print(calc_safety(grid))