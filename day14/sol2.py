import time
from typing import Dict

from day14.domain.coordinates import Coordinates
from day14.domain.coordinates import WORLD_WIDTH, WORLD_HEIGHT
from day14.domain.robot import Robot
from day14.domain.xmas_tree import check_x_tree_shape


def read_file(file_name: str):
    robots_output_list = []

    cci = 0
    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()

            robots_output_list.append(Robot.from_str(cci, line))

            cci += 1

    return robots_output_list


# all_robots = read_file('data/1/12.txt')
all_robots = read_file('data/task1.txt')


# print(all_robots)

# def check_if_tree(all_cord: set[Coordinates]):
#     for tc in TREE_COORDINATES:
#         if tc not in all_coordinates:
#             return False
#     return True

def visualize_map(robot_coords: Dict[Coordinates, int]):
    for ii in range(WORLD_HEIGHT):
        this_line = ''
        for jj in range(WORLD_WIDTH):
            coord = Coordinates(ii, jj)
            this_line = this_line + str(robot_coords.get(coord, '.'))

        print(this_line)


i = 0
while True:
    new_robots = []

    if check_x_tree_shape(set(x.current_coordinates for x in all_robots)):
        print(i)
        places_count = {}
        for r in all_robots:
            places_count[r.current_coordinates] = places_count.get(r.current_coordinates, 0) + 1
        visualize_map(places_count)
        time.sleep(3)

    for robot in all_robots:
        r_moved = robot.moved()
        new_robots.append(r_moved)

        all_robots = new_robots

    i += 1
    if i % 1000 == 0:
        print(i)

    # time.sleep(1)
