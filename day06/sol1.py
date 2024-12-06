from typing import List


def read_file(file_name: str) -> list[list[str]]:
    output = []

    with open(file_name, "r") as file:
        for line in file:
            row = []
            for char in line.rstrip():
                row.append(char)
            output.append(row)
    return output


def find_guard(place: List[list[str]]) -> (int, int, int):
    for x in range(len(place)):
        for y in range(len(place[x])):
            if place[x][y] == '^':
                return x, y, 0
            if place[x][y] == '>':
                return x, y, 1
            if place[x][y] == 'v':
                return x, y, 2
            if place[x][y] == '<':
                return x, y, 3


OBSTACLES = ['#']


def move(place: List[list[str]],
         position: (int, int, int),
         ):
    positions = set([])
    this_position = position[0], position[1], position[2]
    positions.add((position[0], position[1]))

    i = 0
    plot = place.copy()

    while True:
        # print(this_position)
        next_position = this_position

        if this_position[2] == 0:
            next_position = this_position[0] - 1, this_position[1], this_position[2]
        elif this_position[2] == 1:
            next_position = this_position[0], this_position[1] + 1, this_position[2]
        elif this_position[2] == 2:
            next_position = this_position[0] + 1, this_position[1], this_position[2]
        elif this_position[2] == 3:
            next_position = this_position[0], this_position[1] - 1, this_position[2]

        if next_position[0] == len(place) or next_position[0] < 0 or next_position[1] == len(place[next_position[0]]) or \
                next_position[1] < 0:
            print_plot(plot)
            return len(positions)

        if place[next_position[0]][next_position[1]] in OBSTACLES:
            new_direction = this_position[2] + 1
            if new_direction > 3:
                new_direction = 0
            this_position = this_position[0], this_position[1], new_direction
        else:
            this_position = next_position
            positions.add((this_position[0], this_position[1]))

            # xx.append((this_position[0], this_position[1]))

            plot[this_position[0]][this_position[1]] = 'X'
            i += 1

            # if i // 10 == 0:
            # print(i)
            # print_plot(plot)


def print_plot(plot: List[list[str]]):
    for row in plot:
        print(''.join(row))
    print('')


read_file = read_file('data/test1.txt')
# x = read_file('data/task1.txt')
guard_pos = find_guard(read_file)
move_output = move(read_file, guard_pos)
print(move_output)
# y = read_updates_file('data/task1_data.txt')

# --5176
