filePath = "2024/Day9/Day9Input.txt"


def generate_disk(diskDescription: str) -> list[str]:
    disk: list[str] = []
    empty: bool = True
    id: int = 0
    
    for item in diskDescription:
        empty = not empty
        if empty:
            disk += ['.' for i in range(int(item))]
        else:
            disk += [str(id) for i in range(int(item))]
            fileLengths[str(id)] = int(item)
            id += 1

    return disk


def get_empty_lengths(disk: list[str]) -> int:
    startI: int = None
    length: int = 0
    
    emptyLengths: dict[int: int] = {}

    for i, item in enumerate(disk):
        if item == '.' and not startI:
            startI = i

        if item != '.' and startI:
            length = i-startI
            
            emptyLengths[startI] = length
            startI = None

    if startI:
        emptyLengths[startI] = len(disk) - startI

    return emptyLengths


def compact_disk(disk: list[str], fileLengths: dict[str: int]):
    fileLengths.pop("0")
    for id, fileLength in fileLengths.items().__reversed__():
        emptyLengths: dict[int: int] = get_empty_lengths(disk)

        for startI, emptyWidth in emptyLengths.items():
            if fileLength <= emptyWidth and startI < disk.index(id):
                disk = [item if item != id else '.' for item in disk]
                for num in range(fileLength):
                    disk[startI+num] = id
                break

    return disk
        

def generate_checksum(compactedDisk: list[str]) -> int:
    checksum: int = 0
    
    for index, item in enumerate(compactedDisk):
        if item == '.':
            continue
        checksum += index * int(item) 

    return checksum


fileLengths: dict[str: int] = {}

with open(filePath) as f:
    diskDescription: str = f.readline()
    disk: list[str] = generate_disk(diskDescription)

print(generate_checksum(compact_disk(disk, fileLengths)))