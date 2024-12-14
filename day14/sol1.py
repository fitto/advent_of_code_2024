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

TIME = 100

for _ in range(TIME):
    new_robots = []
    for robot in all_robots:
        r_moved = robot.moved()
        new_robots.append(r_moved)
        all_robots = new_robots

places_count = {}
for r in all_robots:
    places_count[r.current_coordinates] = places_count.get(r.current_coordinates, 0) + 1

this_w_mid = WORLD_WIDTH / 2 - 0.5
this_h_mid_1 = WORLD_HEIGHT / 2 - 0.5
# this_h_mid_2 = WORLD_HEIGHT / 2 + 0.5

q1 = []
q2 = []
q3 = []
q4 = []

for place, val in places_count.items():
    if -1 < place.first < this_h_mid_1 and -1 < place.second < this_w_mid:
        q1.append(val)
    if this_h_mid_1 < place.first < WORLD_HEIGHT and -1 < place.second < this_w_mid:
        q2.append(val)

    if -1 < place.first < this_h_mid_1 and this_w_mid < place.second < WORLD_WIDTH:
        q3.append(val)
    if this_h_mid_1 < place.first < WORLD_HEIGHT and this_w_mid < place.second < WORLD_WIDTH:
        q4.append(val)

print(sum(q1) * sum(q2) * sum(q3) * sum(q4))

# --212202585
