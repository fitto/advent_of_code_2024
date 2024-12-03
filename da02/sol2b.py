import re
from typing import List


def read_file(file_name: str) -> List[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    txt_to_analyze = []


    output = []

    with open(file_name, "r") as file:
        for line in file:




            strings_split = re.split("don't()|do()", line)
            output = [element for element in strings_split if element != '' and element is not None]
            print(output)

            # while re.findall(pattern, line.rstrip()):
            #     # while True:
            #     dont_txt_pos = line.find("don't()")
            #     this_line = line[:dont_txt_pos]
            #
            #     output += re.findall(pattern, this_line.rstrip())
            #
            #     do_txt_pos = line.find("do()")
            #     end_pos = do_txt_pos + len('do()')
            #     line = line[end_pos:]

    return output


def parse_and_multiply(input_text: str):
    # print(input_text)
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    txt = re.sub(pattern, r'\1,\2', input_text)

    numbers = txt.split(',')
    # print(int(numbers[0]))
    # print(int(numbers[1]))
    return int(numbers[0]) * int(numbers[1])


x = read_file('t2/test2.txt')
b = 0
for itm in x:
    b += parse_and_multiply(itm)

print(b)
# --878753185
