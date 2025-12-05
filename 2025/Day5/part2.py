
def get_num_fresh(ranges: list[tuple[int, int]]) -> int:
    num_fresh = 0

    ranges = sorted(ranges, key=lambda r: r[0])

    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            num_fresh += current_end + 1 - current_start
            current_start, current_end = start, end

    num_fresh += current_end + 1 - current_start

    return num_fresh


if __name__ == "__main__":
    filePath = "2025/Day5/puzzleInput.txt"
    ranges: list[tuple[int, int]] = []
    fresh: int = 0

    with open(filePath) as f:
        for line in f.readlines():
            if '-' in line:
                l, r = line.split('-')
                ranges.append((int(l), int(r)))
            else:
                break

    print(get_num_fresh(ranges))