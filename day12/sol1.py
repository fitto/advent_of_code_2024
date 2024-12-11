def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


# read_file_data = read_file('data/1/22.txt')
read_file_data = read_file('data/task1.txt')
print(read_file_data)
