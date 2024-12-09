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
new_table = ['.' for x in everything]
num_count = sum(1 for char in text if char != '.')

x = 0
no_y = len(everything) - 1
while x < num_count:
    # print(f'x: {everything[x]}')
    if everything[x] != '.':
        new_table[x] = everything[x]
        x += 1
    else:
        # print(f'y: {everything[no_y]}')
        if everything[no_y] != '.':
            new_table[x] = everything[no_y]
            x += 1
        no_y -= 1
    if everything[x] == '.' and everything[no_y] == '.':
        no_y -= 1

    # print(new_table)

# print(new_table)

otucome = 0
for x_n in range(len(new_table)):
    if new_table[x_n] != '.':
        otucome += int(new_table[x_n]) * x_n

print(otucome)

# print(blocks)
# sorted_blocks = [blocks.pop(0)]
#
# while len(blocks) > 0:
#     sorted_blocks.append(blocks.pop())
# while len(spaces) > 0:
#     popped = spaces.pop()
#     if popped:
#         sorted_blocks.append(popped)
#
# print(sorted_blocks)
