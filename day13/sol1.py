from typing import List

from day13.objects.game_option import GameOption


def read_file(file_name: str) -> List[GameOption]:
    otp = []

    with open(file_name, 'r') as file:
        line_group = []

        for line in file:
            line = line.rstrip()
            if line:

                line_group.append(line)

                if len(line_group) == 3:
                    this_option = GameOption.from_str(line_group)
                    otp.append(this_option)
                    line_group = []
    return otp


# all_options = read_file('data/2/21.txt')
all_options = read_file('data/task1.txt')
# print(all_options)

# x = all_options[0].solve_option()
output = 0

for opt in all_options:
    # print(opt)
    # x = opt.solve_option()
    x = opt.solution_cost()
    if x is not None:
        output += x

print(output)
# --9892418352287151
