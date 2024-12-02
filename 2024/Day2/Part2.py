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


def validateReport(levels: list[int]):
    for i in range(len(levels)):
        if isSafeReport(levels[:i]+levels[i+1:]):
            return True

    if isSafeReport(levels):
        return True
    
    return False


def testSafety(filePath: str):
    numSafe: int = 0

    with open(filePath) as f:
        for report in f.readlines():
            levels = [int(i) for i in report.split()]
            if validateReport(levels):
                numSafe += 1

    return numSafe


print(testSafety(filePath))