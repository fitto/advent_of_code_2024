from typing import List


def read_file(file_name: str) -> List[List[str]]:
    output = []

    with open(file_name, "r") as file:
        for line in file:
            row = []
            for char in line.rstrip():
                row.append(char)
            output.append(row)
    return output


x = read_file('data/test1.txt')
# x = read_file('data/task1.txt')
print(x)
