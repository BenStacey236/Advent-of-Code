
def get_pairs(filePath: str) -> list[str]:
    with open(filePath) as f:
        pairs = [tuple(pair.split('-')) for pair in f.readline().split(',')]

    return pairs


def is_repeating(id: str) -> bool:
    mid = len(id) // 2

    if len(id) % 2 == 1:
        return False

    return id[:mid] == id[mid:]


def contains_repeating(pair: tuple[str, str]) -> int:
    low, high = pair
    repeatingTotal = 0

    for id in range(int(low), int(high) + 1):
        if is_repeating(str(id)):
            repeatingTotal += id
        
    return repeatingTotal


if __name__ == "__main__":
    filePath = "2025/Day2/puzzleInput.txt"

    total = 0

    pairs = get_pairs(filePath)
    for pair in pairs:
        total += contains_repeating(pair)

    print(total)
    