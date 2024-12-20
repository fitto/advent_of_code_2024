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


def has_path_shorter_than(
        graph: Dict[Coordinates, Dict[Coordinates, int]],
        start_pos: Coordinates,
        end_pos: Coordinates,
        max_length: int
) -> bool:
    distances = {node: float('inf') for node in graph.keys()}
    distances[start_pos] = 0
    priority_queue = [(0, start_pos)]

    while priority_queue:
        priority_queue.sort(key=lambda x: x[0])
        current_distance, current_node = priority_queue.pop(0)

        if current_distance >= max_length:
            continue

        if current_node == end_pos and current_distance <= max_length:
            return True

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance >= max_length:
                continue

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))

    return False


COORD_MEM = set()


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


# start, end, all_walls_positions, mh, mw = find_key_points('data/11.txt')
start, end, all_walls_positions, mh, mw = find_key_points('data/task1.txt')
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

EXPECTED_SHORTER_BY = 1
threshold = initial_cost_no_cheats - EXPECTED_SHORTER_BY
print(f'initial_cost_no_cheats={initial_cost_no_cheats} and threshold is {threshold}')

shortest_path_to_traverse = copy.deepcopy(shortest_path)

candidates_to_check = set()
while len(shortest_path_to_traverse) > 0:
    place_to_check = shortest_path_to_traverse.pop()

    if 0 < place_to_check.first < MAX_H + 1 and 0 < place_to_check.second < MAX_W + 1:
        place_to_check_neigbours = place_to_check.neighbouring_coordinates
        for neighbour_tpl in place_to_check_neigbours:
            first_neigbour = Coordinates(neighbour_tpl[0], neighbour_tpl[1])
            if first_neigbour in all_walls_positions and c_in_map(first_neigbour):

                second_neigbour = first_neigbour.shifted_coordinates(place_to_check.first - first_neigbour.first,
                                                                     place_to_check.second - first_neigbour.second
                                                                     )

                if second_neigbour not in all_walls_positions and c_in_map(second_neigbour):
                    candidates_to_check.add(first_neigbour)

print(f'found {len(candidates_to_check)} candidates_to_check')

solutions_count = 0
i = 0
for wall_to_be_removed in candidates_to_check:
    if i % 100 == 0:
        print(f'analyzing {wall_to_be_removed} - {i}')
    i += 1

    # all_wall_positions_with_cheat = copy.deepcopy(all_walls_positions)
    # all_wall_positions_with_cheat = [x for x in all_wall_positions_with_cheat if x != this_candidate]
    #
    # all_paths_with_cheat = find_all_paths(start, all_wall_positions_with_cheat)

    all_paths_with_cheat = copy.deepcopy(all_paths)

    removed_wall_neighbour_coordinates = wall_to_be_removed.neighbouring_coordinates
    for removed_wall_neighbour_coord in removed_wall_neighbour_coordinates:
        this_wall_beighbour = Coordinates(removed_wall_neighbour_coord[0], removed_wall_neighbour_coord[1])
        # print(f'this_wall_beighbour {this_wall_beighbour}')
        if this_wall_beighbour not in all_walls_positions and c_in_map(this_wall_beighbour):
            current_dict_for_nb = all_paths_with_cheat.get(this_wall_beighbour, {})
            current_dict_for_nb[wall_to_be_removed] = 1

            all_paths_with_cheat[this_wall_beighbour] = current_dict_for_nb

            current_dict_for_nb2 = all_paths_with_cheat.get(wall_to_be_removed, {})
            current_dict_for_nb2[this_wall_beighbour] = 1

            all_paths_with_cheat[wall_to_be_removed] = current_dict_for_nb2

    # print(all_paths_with_cheat[wall_to_be_removed])

    option_outcome, _ = dijkstra_between(all_paths_with_cheat, start, end)
    if initial_cost_no_cheats - option_outcome >= EXPECTED_SHORTER_BY:
        solutions_count += 1
    # if has_path_shorter_than(all_paths_with_cheat, start, end, int(threshold)):
    #     solutions_count += 1

print(solutions_count)
# --437
#  --0
# 1418
# --6904