import copy
from typing import List, Tuple, Set


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
         ) -> Set[Tuple[int, int]] | None:
    positions = set([])
    this_position = position[0], position[1], position[2]
    positions.add(this_position)

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
            # print_plot(plot)
            output = set([(p1, p2) for p1, p2, p3 in positions])
            return output

        if place[next_position[0]][next_position[1]] in OBSTACLES:
            new_direction = this_position[2] + 1
            if new_direction > 3:
                new_direction = 0
            next_position = this_position[0], this_position[1], new_direction

        this_position = next_position

        if this_position in positions:
            return None
        else:
            positions.add((this_position[0], this_position[1], this_position[2]))

            # xx.append((this_position[0], this_position[1]))

            # plot[this_position[0]][this_position[1]] = 'X'
            # i += 1

            # if i // 10 == 0:
            # print(i)
            # print_plot(plot)


def print_plot(plot: List[list[str]]):
    for row in plot:
        print(''.join(row))
    print('')


def modified_places(place: List[list[str]],
                    place_candidates: List[Tuple[int, int]],
                    initial_position: Tuple[int, int, int]
                    ):
    new_places = []

    for place_candiate in place_candidates:
        if place_candiate[0] == initial_position[0] and place_candiate[1] == initial_position[1]:
            print('skipping initial')
        else:
            new_place = copy.deepcopy(place)

            new_place[place_candiate[0]][place_candiate[1]] = OBSTACLES[0]
            new_places.append(new_place)

    # print('11')
    return new_places


# this_place = read_file('data/test1.txt')
this_place = read_file('data/task1.txt')
guard_position = find_guard(this_place)
distinct_positions = move(this_place, guard_position)

# print(len(distinct_positions))

modified_places_list = modified_places(this_place,
                                       list(distinct_positions),
                                       guard_position
                                       )
# print(len(modified_places_list))

counter = 0
for modified_place in modified_places_list:
    # print_plot(modified_place)

    distinct_positions = move(modified_place, guard_position)
    if distinct_positions is None:
        counter += 1

print(counter)

#
# for
#
# print(len(modified_places_list))
# y = read_updates_file('data/task1_data.txt')

# --5176
