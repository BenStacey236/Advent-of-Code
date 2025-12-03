
def process_bank(bank: str) -> int:
    leftToFind = 12
    joltages: list[str] = []
    prevLoc = 0

    for i in range(leftToFind-1, -1, -1):
        sub = bank[prevLoc:len(bank) - (i)]
        big = max(sub)
        prevLoc = prevLoc + sub.index(big) + 1
        joltages.append(big)

    return int(''.join(joltages))


if __name__ == "__main__":
    filePath = "2025/Day3/puzzleInput.txt"
    totalJoltage = 0

    with open(filePath) as f:
        for line in f.readlines():
            totalJoltage += process_bank(line.strip())

    print(totalJoltage)