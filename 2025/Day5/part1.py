
def is_fresh(ranges: list[tuple[int, int]], id: int) -> bool:
    for l, r in ranges:
        if l <= id <= r:
            return True
        
    return False

if __name__ == "__main__":
    filePath = "2025/Day5/testInput.txt"
    ranges: list[tuple[int, int]] = []
    fresh: int = 0

    with open(filePath) as f:
        for line in f.readlines():
            if '-' in line:
                l, r = line.split('-')
                ranges.append((int(l), int(r)))
            elif line != '\n':
                if is_fresh(ranges, int(line)): fresh += 1

    print(fresh)