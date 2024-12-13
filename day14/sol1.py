def read_file(file_name: str):
    output = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()
            output.append(line)

            #             line_group.append(line)
            #
            #             if len(line_group) == 3:
            #                 this_option = GameOption.from_str(line_group)
            #                 output.append(this_option)
            #                 line_group = []
    return output


# all_options = read_file('data/2/21.txt')
all_options = read_file('data/task1.txt')
# print(all_options)
