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
            id += 1

    return disk


def compact_disk(disk: list[str]) -> list[str]:
    while '.' in disk:
        i = disk.index('.')
        if i == len(disk) - 1:
            break

        disk[i] = disk.pop(-1)

    return disk


def generate_checksum(compactedDisk: list[str]) -> int:
    checksum: int = 0
    
    for index, item in enumerate(compactedDisk):
        if item == '.':
            continue
        checksum += index * int(item) 

    return checksum


with open(filePath) as f:
    diskDescription: str = f.readline()
    disk: list[str] = generate_disk(diskDescription)

print(generate_checksum(compact_disk(disk)))