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

MIN_H = 0
MAX_H = mh

MIN_W = 0
MAX_W = mw

# ----------------------------
# CALCULATING TRUE SHORTEST PATH
# ----------------------------
all_paths = find_all_paths(start, list(all_walls_positions))
distance, shortest_path = dijkstra_between(all_paths, start, end)

initial_cost_no_cheats = int(distance)

EXPECTED_SHORTER_BY = 100
threshold = initial_cost_no_cheats - EXPECTED_SHORTER_BY
print(f'initial_cost_no_cheats={initial_cost_no_cheats} and threshold is {threshold}')

all_shortest_path_coords_neigbouting_coordinates: Set[Coordinates] = set()
for coord_on_shortest_path in shortest_path:
    coord_on_shortest_path_neigbour_tuples = coord_on_shortest_path.neighbouring_coordinates

    for this_neighbour_tuple in coord_on_shortest_path_neigbour_tuples:
        this_coordinate_cand = Coordinates(this_neighbour_tuple[0], this_neighbour_tuple[1])

        # if is on map and is a wall
        if (this_coordinate_cand not in shortest_path
                and c_in_map(this_coordinate_cand)
                and this_coordinate_cand in all_walls_positions):
            all_shortest_path_coords_neigbouting_coordinates.add(this_coordinate_cand)

print(
    f'found={len(all_shortest_path_coords_neigbouting_coordinates)} distinct all_shortest_paht_coords_neighbours on the map')

# all_walls_positions = ALL_WALLS_POSITIONS
# all_paths = ALL_PATHS

possible_removals: Set[frozenset[Coordinates]] = set()
# find_all_wall_to_dissapear_candidates_pairs(all_walls_positions))
for x in all_walls_positions:
    # if wall neighbouring to the shortest path and is valid
    if x in all_shortest_path_coords_neigbouting_coordinates:
        nc = x.neighbouring_coordinates
        nc = [Coordinates(x[0], x[1]) for x in nc]

        nc_that_are_walls = [x for x in nc if x in all_walls_positions]

        # if this candidate does not border with 3 other walls where removal does not change anything
        if len(nc_that_are_walls) < 3:
            nc_that_are_outside = [x for x in nc if not c_in_map(x)]

            # if this is not a border wall
            if len(nc_that_are_outside) > 0:
                this_set = frozenset([x])

                possible_removals.add(this_set)

solutions_count = 0
i = 0
print(f'found {len(possible_removals)} possible_removals')
for element_frozenset in possible_removals:

    if i % 100 == 0:
        print(f'analyzing {element_frozenset} - {i}')
    i += 1

    this_coord_to_be_removed = next(iter(element_frozenset))

    all_paths_with_cheat = copy.deepcopy(all_paths)
    element_coord_neighbours = this_coord_to_be_removed.neighbouring_coordinates

    for nbr in element_coord_neighbours:
        nbr_coord = Coordinates(nbr[0], nbr[1])
        if nbr_coord not in all_walls_positions and c_in_map(nbr_coord):
            current_dict_for_nb = all_paths_with_cheat.get(nbr_coord, {})
            current_dict_for_nb[this_coord_to_be_removed] = 1

            all_paths_with_cheat[nbr_coord] = current_dict_for_nb

            current_dict_for_nb2 = all_paths_with_cheat.get(this_coord_to_be_removed, {})
            current_dict_for_nb2[nbr_coord] = 1

            all_paths_with_cheat[this_coord_to_be_removed] = current_dict_for_nb

    if has_path_shorter_than(all_paths_with_cheat, start, end, int(threshold)):
        solutions_count += 1

print(solutions_count)
# --437
#  --0
