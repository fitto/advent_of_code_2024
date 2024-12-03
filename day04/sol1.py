import re
from typing import List


def read_file(file_name: str):
    txt = ''

    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    with open(file_name, "r") as file:
        for line in file:
            print(line.rstrip())
            txt = re.sub(pattern, r'\1,\2', line)

    return txt


x = read_file('data/test1.txt')
print(x)
