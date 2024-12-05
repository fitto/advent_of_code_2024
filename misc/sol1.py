import re
from typing import List, Dict


def read_file(file_name: str) -> List[List[str]]:
    text_table = []

    pattern = r'XMAS'

    with open(file_name, "r") as file:
        for line in file:
            row = []
            for char in line.rstrip():
                row += char

            # print(row)
            text_table.append(row)

    return text_table


x = read_file('data/test1.txt')
# x = read_file('data/task1.txt')
