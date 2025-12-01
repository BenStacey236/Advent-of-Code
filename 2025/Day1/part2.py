def turn_safe(pos: int, turn: str) -> tuple[int, int]:
    startsZero = pos == 0
    timesPassedZero = 0

    rotation = int(turn[1:])
    timesPassedZero = rotation // 100
    leftover = rotation % 100

    if turn.startswith("L"):
        pos -= leftover

    else:
        pos += leftover

    if not startsZero and pos <= 0 or pos >= 100:
        timesPassedZero += 1

    return pos % 100, timesPassedZero


safePos = 50
inputFile = "2025/Day1/puzzleInput.txt"
with open(inputFile, "r") as f:
    lines = f.readlines()

timesPassesZero = 0
for line in lines:
    safePos, passed = turn_safe(safePos, line.strip("\n"))
    timesPassesZero += passed

print(timesPassesZero)