import re

filePath = '2024/Day3/Day3Input.txt'

def calc_mul(mul: str) -> int:
    values: list[int] = [int(num) for num in mul.strip("mul()").split(',')]
    
    return values[0]*values[1]

total: int = 0

with open(filePath) as f:
    for line in f.readlines():
        validMuls = re.findall(r"mul\(\d+,\d+\)", line)
        for mul in validMuls:
            total += calc_mul(mul)

print(total)
