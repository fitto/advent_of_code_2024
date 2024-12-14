from day14.domain.coordinates import WORLD_WIDTH, WORLD_HEIGHT
from day14.domain.robot import Robot


def read_file(file_name: str):
    robots = []

    i = 0
    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()

            robots.append(Robot.from_str(i, line))

            i += 1

    return robots


# all_robots = read_file('data/1/12.txt')
all_robots = read_file('data/task1.txt')
# print(all_robots)
