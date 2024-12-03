import re
from typing import List


def read_file(file_name: str) -> List[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    with open(file_name, "r") as file:
        for line in file:
            print(line)
            matches = re.findall(pattern, line.rstrip())

    return matches


def parse_and_multiply(input_text: str):
    # print(input_text)
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    txt = re.sub(pattern, r'\1,\2', input_text)

    numbers = txt.split(',')
    # print(int(numbers[0]))
    # print(int(numbers[1]))
    return int(numbers[0]) * int(numbers[1])


x = read_file('t1/task1.txt')

print(len(x))

b = 0
for itm in x:
    b += parse_and_multiply(itm)

print(b)
# --28858842
# --mul(198,240)
