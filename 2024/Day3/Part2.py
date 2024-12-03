import re

filePath = '2024/Day3/Day3Input.txt'

def calc_mul(mul: str) -> int:
    values: list[int] = [int(num) for num in mul.strip("mul()").split(',')]
    
    return values[0]*values[1]

total: int = 0
includeMul: bool = True

with open(filePath) as f:
    for line in f.readlines():
        validMuls = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", line)

        for result in validMuls:
            if includeMul and result != "do()" and result != "don't()":
                total += calc_mul(result)
            
            elif result == "do()":
                includeMul = True

            elif result == "don't()":
                includeMul = False

print(total)