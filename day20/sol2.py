import copy
import time
from typing import Dict, Set, List, Tuple

from day16.domain.coordinates import Coordinates


def find_key_points(file_name: str) -> Tuple[Coordinates, Coordinates, Set[Coordinates], int, int]:
    s = None
    e = None
    all_walls = set()

    with open(file_name, 'r') as file:
        i = 0
        j = 0
        for char in file.read():
            if char == 'S':
                s = Coordinates(i, j)
            if char == 'E':
                e = Coordinates(i, j)
            if char == '#':  # or char == 'S' or char == 'E':
                all_walls.add(Coordinates(i, j))
            # if char == '.':
            #     all_allowed.add(Coordinates(i, j))

            if char == '\n':
                i += 1
                j = 0
            else:
                j += 1

    # max height, max_width
    return s, e, all_walls, i, j - 1


def c_in_map(coordinates: Coordinates) -> bool:
    return MIN_H - 1 < coordinates.first < MAX_H + 1 and MIN_W - 1 < coordinates.second < MAX_W + 1


def find_all_paths(starting_coord: Coordinates,
                   all_walls_coordinates: List[Coordinates],
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

            next_postion_options = [x for x in next_postion_options if x not in all_walls_coordinates]
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


def dijkstra_between(
        graph: Dict[Coordinates, Dict[Coordinates, int]],
        start: Coordinates,
        end: Coordinates
) -> tuple[float, list[Coordinates]]:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    parents = {start: None}

    while priority_queue:
        priority_queue.sort(key=lambda x: x[0])
        current_distance, current_node = priority_queue.pop(0)

        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parents.get(current_node)
            return current_distance, path[::-1]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                priority_queue.append((distance, neighbor))

    return float('inf'), []


def reconstruct_all_paths(before_dict: Dict[Coordinates, List[Coordinates]],
                          start_maze_pos: Coordinates,
                          end_maze_pos: Coordinates) -> List[List[Coordinates]]:
    stack = [(end_maze_pos, [end_maze_pos])]
    all_paths = []
    visited = set()

    while stack:
        current, path = stack.pop()

        if current == start_maze_pos:
            all_paths.append(path[::-1])
            continue

        if current in visited:
            continue

        visited.add(current)

        for predecessor in before_dict.get(current, []):
            stack.append((predecessor, path + [predecessor]))

    return all_paths


COORD_MEM = set()

last_time = time.time()
# start, end, all_walls_positions, mh, mw = find_key_points('data/11.txt')
start, end, all_walls_positions, mh, mw = find_key_points('data/task1.txt')
EXPECTED_SHORTER_BY = 100
CHEAT_LENGTH = 20

print(f'start {start}')
print(f'end {end}')
print(f'all_walls_positions {len(all_walls_positions)}')

MIN_H = 0
MAX_H = mh
print(f'MAX_H {MAX_H}')

MIN_W = 0
MAX_W = mw
print(f'MAX_W {MAX_W}')

# ----------------------------
# CALCULATING TRUE SHORTEST PATH
# ----------------------------
all_paths = find_all_paths(start, list(all_walls_positions))
all_path_prices, back_track_dict = dijkstra(all_paths, end)

initial_cost_no_cheats = all_path_prices[start]

shortest_path_coords_list = reconstruct_all_paths(back_track_dict, end, start)[0]

threshold = initial_cost_no_cheats - EXPECTED_SHORTER_BY

this_time = time.time()
time_diff = this_time - last_time
last_time = this_time

print(
    f'initial_cost_no_cheats={initial_cost_no_cheats} and threshold is {threshold} - calculated in {time_diff:.2f} seconds')

shortest_path_to_traverse = copy.deepcopy(shortest_path_coords_list)
shortest_path_to_traverse.reverse()

steps_so_far = -1
shrter_paths = 0
all_paths_with_cheat = copy.deepcopy(all_paths)

# ----------------------------
# CALCULATING THeoretical_Paths - no walls
# ----------------------------
ALL_PATHS_THEORETICAL_BELOW_THRESHOLD_MEM = {}
for i in range(MAX_H + 1):
    for j in range(MAX_H + 1):
        this_coord = Coordinates(i, j)
        if this_coord not in all_walls_positions:
            all_paths_theoretical = find_all_paths(this_coord, [])
            distances_theoretical, _ = dijkstra(all_paths_theoretical, this_coord)

            distances_in_cheat_length = {key: value for key, value in distances_theoretical.items() if
                                         CHEAT_LENGTH >= value > 0
                                         and key not in all_walls_positions
                                         }

            ALL_PATHS_THEORETICAL_BELOW_THRESHOLD_MEM[this_coord] = distances_in_cheat_length

this_time = time.time()
time_diff = this_time - last_time
last_time = this_time
print(
    f'Claculted ALL_PATHS_THEORETICAL_BELOW_THRESHOLD_MEM in  {time_diff:.2f} seconds')

i = 0
while len(shortest_path_to_traverse) > 0:
    place_to_check = shortest_path_to_traverse.pop(0)
    steps_so_far += 1
    if i % 100 == 0:
        this_time = time.time()
        time_diff = this_time - last_time
        last_time = this_time
        print(
            f'traversing {place_to_check} - {i} and {len(shortest_path_to_traverse)} remaining - last iter lasted {time_diff:.2f} seconds')
    i += 1

    # print(place_to_check)

    possible_coordinates_and_costs_dict = ALL_PATHS_THEORETICAL_BELOW_THRESHOLD_MEM[place_to_check]

    for place_to_check_key, place_to_check_cheat_length in possible_coordinates_and_costs_dict.items():
        remianing_dist = all_path_prices[place_to_check_key]
        if remianing_dist + steps_so_far + place_to_check_cheat_length <= threshold:
            print(
                f'   place_to_check_key {place_to_check_key}, place_to_check_cheat_length {place_to_check_cheat_length}')
            shrter_paths += 1

print(shrter_paths)
