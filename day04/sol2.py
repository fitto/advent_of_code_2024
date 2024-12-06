from typing import List


def read_file(file_name: str) -> List[List[str]]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            row = []
            for char in line.rstrip():
                row += char

            # print(row)
            text_table.append(row)

    return text_table


def find_strings(text_table: List[List[str]],
                 ) -> int:
    instances = 0
    for x in range(len(text_table) - 2):
        for y in range(len(text_table[0]) - 2):
            if text_table[x][y] == 'M' and text_table[x][y + 2] == 'S' and text_table[x + 1][y + 1] == 'A' and \
                    text_table[x + 2][y] == 'M' and text_table[x + 2][y + 2] == 'S':
                print(x)
                print(y)
                print('-----------')
                instances += 1
            if text_table[x][y] == 'S' and text_table[x][y + 2] == 'S' and text_table[x + 1][y + 1] == 'A' and \
                    text_table[x + 2][y] == 'M' and text_table[x + 2][y + 2] == 'M':
                print(x)
                print(y)
                print('-----------')
                instances += 1
            if text_table[x][y] == 'S' and text_table[x][y + 2] == 'M' and text_table[x + 1][y + 1] == 'A' and \
                    text_table[x + 2][y] == 'S' and text_table[x + 2][y + 2] == 'M':
                print(x)
                print(y)
                print('-----------')
                instances += 1
            if text_table[x][y] == 'M' and text_table[x][y + 2] == 'M' and text_table[x + 1][y + 1] == 'A' and \
                    text_table[x + 2][y] == 'S' and text_table[x + 2][y + 2] == 'S':
                print(x)
                print(y)
                print('-----------')
                instances += 1

    return instances


# matrix = [
#     ['t', 'e', 's', 't', 'a'],
#     ['u', 'p', 't', 'o', 'a'],
#     ['d', 'i', 'a', 'g', 'a'],
#     ['t', 'a', 'b', 'l', 'a'],
#     ['e', 'x', 't', 'r', 'a']
# ]
# x = prepare_all_tables(matrix)
# for x1 in x.keys():
#     print(f'{x1} : {x[x1]}')

# x = read_file('data/test1.txt')
read_file = read_file('data/task1.txt')

found_strings = find_strings(read_file)
print(found_strings)
