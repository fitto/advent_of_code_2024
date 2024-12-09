def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            for char in line.rstrip():
                text_table.append(char)

    return text_table


read_file_data = read_file('data/task1.txt')
# print(read_file_data)

text = []

fileId = 0
i = 0

everything = []

while i < len(read_file_data):
    file_block = read_file_data[i]
    if i + 1 < len(read_file_data):
        free_space = read_file_data[i + 1]
    else:
        free_space = '0'

    # this_block = []
    for x in range(int(file_block)):
        text.append(fileId)
        # this_block.append(fileId)
        everything.append(fileId)

    # this_space = []
    if int(free_space) > 0:
        for y in range(int(free_space)):
            # text.append('.')
            # this_space.append('.')
            everything.append('.')

    i += 2
    fileId += 1

# print(everything)
new_table = [x for x in everything]

no_y = len(everything) - 1

last_moved_pos = 0

while no_y > -1:
    if everything[no_y] != '.':
        found_y = no_y

        ts_letter = everything[no_y]
        found_block = []
        while everything[no_y] == ts_letter:
            found_block.append(everything[no_y])
            no_y -= 1

        x = 0
        while x < no_y:
            if new_table[x] != '.':
                x += 1
            else:
                spaces = []
                while everything[x] == '.':
                    spaces.append(everything[x])
                    x += 1

                if len(spaces) >= len(found_block):
                    this_x = x - len(spaces)

                    for blk in found_block:
                        new_table[this_x] = blk
                        this_x += 1
                        new_table[found_y] = '.'
                        found_y -= 1

                    last_moved_pos = this_x
                    break
    else:
        no_y -= 1
    # print(new_table)

otucome = 0
for x_n in range(len(new_table)):
    if new_table[x_n] != '.':
        otucome += int(new_table[x_n]) * x_n

print(otucome)
