import re
from typing import List, Dict


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


def prepare_all_tables(text_table: List[List[str]]) -> Dict[str, List[List[str]]]:
    # horizontal,
    outputs = {'horizontal': text_table.copy()}

    # # horizontal - written backwards
    # hb = [row[::-1] for row in text_table]
    # print(hb)

    # vertical
    vertical = [[row[i] for row in text_table] for i in range(len(text_table))]
    # print(vertical)
    outputs['vertical'] = vertical

    # diagonal
    print('0')
    diagonals = []
    for i in range(len(text_table)):
        word = []
        x = i + 1
        y = 0
        while y < len(text_table[0]) and x < len(text_table):
            word.append(text_table[x][y])
            x += 1
            y += 1

        print(word)
        diagonals.append(word)
    # print(diagonals)

    print('1')
    for i in range(len(text_table)):
        word = []
        x = len(text_table) - 2 - i
        y = 0
        while y < len(text_table[0]) and x > -1:
            word.append(text_table[x][y])
            x -= 1
            y += 1

        print(word)
        diagonals.append(word)

    print('2')
    for i in range(len(text_table[0])):
        word = []
        x = 0
        y = i
        while y < len(text_table[0]) and x < len(text_table):
            word.append(text_table[x][y])
            x += 1
            y += 1

        print(word)
        diagonals.append(word)

    print('3')
    for i in range(len(text_table[0])):
        word = []
        x = len(text_table) - 1
        y = i
        while y < len(text_table[0]) and x > -1:
            word.append(text_table[x][y])
            x -= 1
            y += 1

        print(word)
        diagonals.append(word)

    outputs['diagonal'] = diagonals

    return outputs


def find_strings(text_tables: Dict[str, List[List[str]]],
                 pattern_strings: List[str]
                 ) -> int:
    instances = 0
    for pattern in pattern_strings:
        for key, table in text_tables.items():
            for line in table:
                text_line = ''.join(line)
                matches = re.findall(pattern, text_line)
                instances += len(matches)

                print(f'-----------------------')
                print(f'key {key}')
                print(f'pattern {pattern}')
                print(f'text_line {text_line}')
                print(f'matches {len(matches)}')

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
read_file_data = read_file('data/task1.txt')
# print(x)
prepared_tables = prepare_all_tables(read_file_data)
# for x1 in y.keys():
#     print(f'{x1} : {y[x1]}')

# print(y)

found_strings = find_strings(prepared_tables,
                             ['XMAS', 'SAMX']
                             )
print(found_strings)
