import re
from typing import List


def read_file(file_name: str) -> List[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    output = []

    with open(file_name, "r") as file:
        for line in file:
            txt = line.rstrip()

            while re.findall(pattern, txt.rstrip()):
                # while True:
                dont_txt_pos = txt.find("don't()")
                if dont_txt_pos != -1:
                    this_line = txt[:dont_txt_pos]
                else:
                    this_line = txt

                output += re.findall(pattern, this_line)

                txt = txt.removeprefix(this_line)
                end_pos = txt.find("do()") + len('do()')
                txt = txt[end_pos:]
                print(txt)

    return output


def parse_and_multiply(input_text: str):
    # print(input_text)
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    txt = re.sub(pattern, r'\1,\2', input_text)

    numbers = txt.split(',')
    # print(int(numbers[0]))
    # print(int(numbers[1]))
    return int(numbers[0]) * int(numbers[1])


x = read_file('t2/task1.txt')
# x = read_file('t2/test2.txt')
b = 0
for itm in x:
    b += parse_and_multiply(itm)

print(b)
# --878753185
# 79897239
# 328546034
# 273334766
# not tried: 87163705
