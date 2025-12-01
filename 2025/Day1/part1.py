def turn_safe(pos: int, turn: str) -> int:
    if turn.startswith("L"):
        pos -= int(turn[1:])

    else:
        pos += int(turn[1:])

    return pos % 100

safePos = 50
inputFile = "2025/Day1/testInput.txt"
with open(inputFile, "r") as f:
    lines = f.readlines()

timesAtZero = 0
for line in lines:
    safePos = turn_safe(safePos, line.strip("\n"))
    if safePos == 0:
        timesAtZero += 1

print(timesAtZero)