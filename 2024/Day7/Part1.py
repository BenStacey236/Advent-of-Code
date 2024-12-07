filePath = '2024/Day7/Day7Input.txt'


def eval_expression(operands: list[int], operations: list[str]) -> int:
    ops = operands.copy()
    ops.reverse()

    while len(ops) > 1:
        op1: int = ops.pop(-1)
        op2: int = ops.pop(-1)
        operation: str = operations.pop(0)

        if operation == '0':
            ops.append(op1 + op2)
        elif operation == '1':
            ops.append(op1 * op2)

    return ops[0]


def is_target_obtainable(target: int, operands: list[int]) -> bool:
    numOperations: int = len(operands)
    for pattern in range(2**numOperations):
        operations = [i for i in str(bin(pattern))[2:]]
        operations = ['0' for i in range(numOperations - len(operations) - 1)] + operations
        if eval_expression(operands, operations) == target:
            return True

    return False


totalObtainable: int = 0

with open(filePath) as f:
    for line in f.readlines():
        target = int(line.strip('\n').split(':')[0])

        if is_target_obtainable(target, [int(i) for i in line.strip('\n').split(':')[1].split()]):
            print(target)
            totalObtainable += target

print(totalObtainable)