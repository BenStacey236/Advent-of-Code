filePath = "2024/Day8/Day8Input.txt"


def add_tuples(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    x1, x2 = tup1
    y1, y2 = tup2

    return (x1+y1, x2+y2)


def sub_tuples(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    x1, x2 = tup1
    y1, y2 = tup2

    return (x1-y1, x2-y2)


def is_valid_antinode(node: tuple[int, int]):
    for type, points in antenna.items():
        for point in points:
            difference = sub_tuples(point, node)
            if add_tuples(point, difference) in antenna[type] and difference != (0, 0):
                return True
            
    return False


grid: list[str] = []
antenna: dict[str: list[tuple[int, int]]] = {}

with open(filePath) as f:
    for x, row in enumerate(f.readlines()):
        grid.append([])
        for y, cell in enumerate(row.strip('\n')):
            grid[x].append(cell)

            if cell != '.' and cell not in antenna:
                antenna[cell] = [(x, y)]
            elif cell in antenna:
                antenna[cell].append((x, y))


numAntinodes: int = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if is_valid_antinode((x, y)):
            numAntinodes += 1

print(numAntinodes)