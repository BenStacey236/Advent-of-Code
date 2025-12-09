
if __name__ == "__main__":
    filePath = "2025/Day6/puzzleInput.txt"
    total = 0

    with open(filePath) as f:
        columns: list[list[int]] = [[int(i)] for i in f.readline().strip().split()]
        ops: list = []

        for line in f.readlines():
            for i, val in enumerate(line.strip().split()):
                if val in ["+", "*"]:
                    ops.append(val)
                else:    
                    columns[i].append(int(val))

    for col, op in zip(columns, ops):
        if op == "+":
            total += sum(col)
        elif op == "*":
            res = col[0]
            for val in col[1:]:
                res *= val

            total += res

    print(total)
