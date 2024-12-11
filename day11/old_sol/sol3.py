import math


def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


# data = read_file('data/1/22.txt')
data = read_file('../data/task1.txt')
data = [int(a) for a in data]

current_length = len(data)

for i in range(75):
    result = []
    for this_number in data:
        if this_number == 0:  # Rule 1
            result.append(1)
        else:
            lngth = int(math.log10(this_number)) + 1
            if lngth % 2 == 0:  # Rule 2
                a = 10 ** (lngth // 2)
                result.append(this_number // a)
                result.append(this_number % a)
            else:
                result.append(this_number * 2024)

    data = result
    print(i)
    # print(data)

print(len(data))
