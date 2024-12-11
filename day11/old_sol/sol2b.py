def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


data = read_file('../data/1/11.txt')
# data = read_file('data/task1.txt')
current_length = len(data)

for i in range(75):
    x = 0
    result = []
    for this_number in data:
        if this_number == '0':  # Rule 1
            result.append('1')
            x += 1

        elif len(this_number) % 2 == 0:  # Rule 2
            half = len(this_number) // 2
            first_part = this_number[:half]
            second_part = str(int(this_number[half:]))
            result.extend([first_part, second_part])  # Flatten by extending

            x += 1

        else:
            result.append(str(int(this_number) * 2024))
            x += 1
    data = result
    print(i)

print(len(data))
