
if __name__ == "__main__":
    filePath = "2025/Day7/puzzleInput.txt"
    splits: int = 0

    with open(filePath) as f:
        prevLazerLocations = set([f.readline().index('S')])

        for line in f.readlines():
            lazerLocations = set()
            for loc in prevLazerLocations:
                if line[loc] == '^':
                    splits += 1
                    lazerLocations.add(loc-1)
                    lazerLocations.add(loc+1)
                else:
                    lazerLocations.add(loc)

            prevLazerLocations = lazerLocations

    print(splits)


        