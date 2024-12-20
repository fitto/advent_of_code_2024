import copy
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


COORD_MEM = set()

# start, end, all_walls_positions, mh, mw = find_key_points('data/11.txt')
start, end, all_walls_positions, mh, mw = find_key_points('data/task1.txt')
EXPECTED_SHORTER_BY = 100

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
distance, shortest_path = dijkstra_between(all_paths, start, end)

initial_cost_no_cheats = int(distance)

threshold = initial_cost_no_cheats - EXPECTED_SHORTER_BY
print(f'initial_cost_no_cheats={initial_cost_no_cheats} and threshold is {threshold}')

shortest_path_to_traverse = copy.deepcopy(shortest_path)

steps_so_far = -1
shrter_paths = 0
all_paths_with_cheat = copy.deepcopy(all_paths)

while len(shortest_path_to_traverse) > 0:
    place_to_check = shortest_path_to_traverse.pop(0)
    steps_so_far += 1
    # print(f'traversing {place_to_check}')
    print(steps_so_far)

    place_to_check_neigbours = place_to_check.neighbouring_coordinates
    for neighbour_tpl in place_to_check_neigbours:
        first_neigbour = Coordinates(neighbour_tpl[0], neighbour_tpl[1])
        if first_neigbour in all_walls_positions:

            second_neigbour = first_neigbour.shifted_coordinates(first_neigbour.first - place_to_check.first,
                                                                 first_neigbour.second - place_to_check.second
                                                                 )

            if second_neigbour not in all_walls_positions and c_in_map(second_neigbour):
                remianing_dist, _ = dijkstra_between(all_paths, second_neigbour, end)
                if remianing_dist + steps_so_far + 1 < threshold:
                    shrter_paths += 1

print(shrter_paths)
