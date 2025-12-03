
def process_bank(bank: str) -> int:
    max1 = max(bank[:-1])
    i = bank.index(max1)

    return int(max1 + max(bank[i+1:]))


if __name__ == "__main__":
    filePath = "2025/Day3/puzzleInput.txt"
    totalJoltage = 0

    with open(filePath) as f:
        for line in f.readlines():
            totalJoltage += process_bank(line.strip())

    print(totalJoltage)