
def get_area(point1: tuple[int, int], point2: tuple[int, int]):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x2-x1+1) * abs(y2-y1+1)


if __name__ == "__main__":
    filePath = "2025/Day9/puzzleInput.txt"
    maxArea = 0

    with open(filePath) as f:
        reds = [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f.readlines()]

    for p1 in reds:
        for p2 in reds:
            if p1 == p2:
                continue
            
            maxArea = max(maxArea, get_area(p1, p2))

    print(maxArea)