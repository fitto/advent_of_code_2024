from typing import Dict, List

from day18.coordinates import Coordinates


# X,Y
# X2,Y1 -? X is the distance from the left edge of your memory space and Y is the distance from the top edge of your memory space


def read_all(file_name: str) -> List[Coordinates]:
    coordinates = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.rstrip()
            split_line = line.split(',')
            coordinates.append(Coordinates(int(split_line[1]), int(split_line[0])))

    return coordinates


# ALL_BYTES = read_all('data/11.txt')
ALL_BYTES = read_all('data/task1.txt')

MAX_H = 70
MAX_w = 70
# MAX_H = 6
# MAX_w = 6

START_COORD = Coordinates(0, 0)
END_COORD = Coordinates(MAX_H, MAX_w)


def c_in_map(coordinates: Coordinates) -> bool:
    return -1 < coordinates.first < MAX_H + 1 and -1 < coordinates.second < MAX_w + 1


def find_all_paths(starting_coord: Coordinates,
                   fallen_bytes_coordinates: List[Coordinates],
                   ) -> Dict[Coordinates, Dict[Coordinates, int]]:
    output = {}
    seen_positions = set()

    positions_to_be_checked = [starting_coord]

    while len(positions_to_be_checked) > 0:
        this_position = positions_to_be_checked.pop()
        if this_position not in seen_positions:
            seen_positions.add(this_position)
            next_postion_options = this_position.neighbouring_coordinates
            next_postion_options = [Coordinates(x[0], x[1]) for x in next_postion_options]
            next_postion_options = [x for x in next_postion_options if x not in fallen_bytes_coordinates]
            next_postion_options = [x for x in next_postion_options if c_in_map(x)]
            next_postion_options_map = {x: 1 for x in next_postion_options}

            for k, v in next_postion_options_map.items():
                cur = output.get(this_position, {})
                cur[k] = v

                output[this_position] = cur

                cur2 = output.get(k, {})
                cur2[this_position] = v

                output[k] = cur2

                positions_to_be_checked.append(k)

    return output


def dijkstra(graph: Dict[Coordinates, Dict[Coordinates, int]],
             start_pos: Coordinates
             ) -> tuple[dict[Coordinates, float], Dict[Coordinates, List[Coordinates]]]:
    distances = {node: float('inf') for node in graph.keys()}
    distances[start_pos] = 0

    nodes_before_this = {node: [] for node in graph}

    priority_queue = [(0, start_pos)]

    while priority_queue:
        priority_queue.sort(key=lambda xx: xx[0])
        current_distance, current_node = priority_queue.pop(0)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                nodes_before_this[neighbor] = [current_node]
                priority_queue.append((distance, neighbor))
            elif distance == distances[neighbor]:
                nodes_before_this[neighbor].append(current_node)

    return distances, nodes_before_this


# def can_be_at_steps(step: int) -> list[Coordinates]:
#     number_of_steps = 1
#
#     dj_s = -1
#     while dj_s < 0:
#         bits_so_far = ALL_BYTES[:number_of_steps]
#         print(f'len is {len(bits_so_far)}')
#         paths_at_step = find_all_paths(START_COORD, bits_so_far)
#         shortest_paths_at_step, _ = dijkstra(paths_at_step, START_COORD)
#
#         if END_COORD not in shortest_paths_at_step.keys():
#             print(f'    falling of on {number_of_steps}')
#             return -1
#
#         print(f'on {number_of_steps} and is {shortest_paths_at_step[END_COORD]}')
#
#         min_no_steps = int(shortest_paths_at_step[END_COORD])
#
#         if number_of_steps >= min_no_steps:
#             return min_no_steps
#         else:
#             number_of_steps += 1
#
#
# def simulate():
#     all_positions_at_step = {}

def visualize(time: int):
    for ii in range(MAX_H + 1):
        this_line = ''

        jj = 0
        while jj < MAX_w + 1:
            if Coordinates(ii, jj) in ALL_BYTES[:time +1]:
                this_line += '#'
            else:
                this_line += '.'
            jj += 1

        print(this_line)


for i in range(24):
    visualize(i)
    print(f'i = {i} and last fallen = {ALL_BYTES[i]}')
    print('')
    print('')
    # sleep(1)

all_paths = find_all_paths(START_COORD, ALL_BYTES[:1024])
dj, bt = dijkstra(all_paths, START_COORD)

all_shortest_paths = dj[END_COORD]
print(all_shortest_paths)
#
# # x = do_steps()
# # print(x)
# # # -140
# # # 142
