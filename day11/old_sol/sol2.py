def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


def blink(input_table: list[str]) -> list[str]:
    result = []
    for this_number in input_table:
        if this_number == '0':  # Rule 1
            result.append('1')
        elif len(this_number) % 2 == 0:  # Rule 2
            half = len(this_number) // 2
            first_part = this_number[:half]
            second_part = str(int(this_number[half:]))
            result.extend([first_part, second_part])  # Flatten by extending
        else:  # Rule 3
            result.append(str(int(this_number) * 2024))
    return result


# data = read_file('data/1/22.txt')
data = read_file('../data/task1.txt')

for i in range(75):
    data = blink(data)
    # print(data)
    print(i)

print(len(data))
