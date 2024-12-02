filePath = '2024/Day2/Day2Input.txt'


def isSafeReport(levels: list[int]):
    increasing: bool = False
    decreasing: bool = False

    for i, level in enumerate(levels):
        if i > 0:
            difference: int = level-levels[i-1]

            if abs(difference) > 3 or difference == 0:
                return False
            
            elif not increasing and not decreasing:
                if difference > 0:
                    increasing = True
                else:
                    decreasing = True

            elif increasing:
                if difference < 0:
                    return False
                
            elif decreasing:
                if difference > 0:
                    return False
        
    return True


def testSafety(filePath: str):
    numSafe: int = 0

    with open(filePath) as f:
        for report in f.readlines():
            levels = [int(i) for i in report.split()]
            if isSafeReport(levels):
                numSafe += 1

    return numSafe


print(testSafety(filePath))