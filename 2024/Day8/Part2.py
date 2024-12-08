filePath = "2024/Day8/Day8Input.txt"


def add_tuples(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    x1, x2 = tup1
    y1, y2 = tup2

    return (x1+y1, x2+y2)


def sub_tuples(tup1: tuple[int, int], tup2: tuple[int, int]) -> tuple[int, int]:
    x1, x2 = tup1
    y1, y2 = tup2

    return (x1-y1, x2-y2)


def find_difference_hcf(values: tuple[int, int]):
   x, y = values
   while(y):
       x, y = y, x % y
   return x


def is_valid_antinode(node: tuple[int, int]):
    for type, points in antenna.items():
        for point in points:
            difference = sub_tuples(point, node)
            hcf = abs(find_difference_hcf(difference))
        
            if hcf == 0:
                gradient = difference
            else:
                gradient = (difference[0]//hcf, difference[1]//hcf)
            check = add_tuples(node, gradient)

            if gradient == (0, 0) and len(antenna[type]) > 1:
                return True

            while check[0] >= 0 and check[0] <= len(grid) and check[1] >= 0 and check[1] <= len(grid[0]) and gradient != (0, 0):
                if check in antenna[type] and check != point:
                    return True
                else:
                    check = add_tuples(check, gradient)

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