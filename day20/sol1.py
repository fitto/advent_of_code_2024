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


def find_all_wall_to_dissapear_candidates_pairs(all_walls: Set[Coordinates]) -> set[frozenset[Coordinates]]:
    output = set()

    for this_wall in all_walls:
        cands_for_this_wall = this_wall.neighbouring_coordinates
        cands_for_this_wall = [Coordinates(x[0], x[1]) for x in cands_for_this_wall]

        for cand in cands_for_this_wall:
            if cand in all_walls:
                this_set = {this_wall, cand}
                this_set = frozenset(this_set)

                output.add(this_set)

    return output


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


def visualize(all_walls_positions: List[Coordinates],
              start_coord: Coordinates,
              end_coord: Coordinates
              ):
    for ii in range(MAX_H + 1):
        this_line = ''

        jj = 0
        while jj < MAX_W + 1:
            if Coordinates(ii, jj) in all_walls_positions:
                this_line += '#'
            elif Coordinates(ii, jj) == start_coord:
                this_line += 'S'
            elif Coordinates(ii, jj) == end_coord:
                this_line += 'E'
            else:
                this_line += '.'
            jj += 1

        print(this_line)


# start, end, all_walls_positions, mh, mw = find_key_points('data/11.txt')
start, end, all_walls_positions, mh, mw = find_key_points('data/task1.txt')

print(f'start coord {start}')
print(f'end coord {end}')
# visualize(list(all_walls_positions),
#           start,
#           end
#           )

MIN_H = 0
MAX_H = mh
# print(MIN_H)
# print(MAX_H)

MIN_W = 0
MAX_W = mw
# print(MIN_W)
# print(MAX_W)

all_paths = find_all_paths(start, list(all_walls_positions))
dj, _ = dijkstra(all_paths, start)

all_shortest_paths = dj[end]
initial_cost_no_cheats = all_shortest_paths
print(f'initial_cost_no_cheats={initial_cost_no_cheats}')

MAX_H = end.first + 11
# print(MIN_H)
# print(MAX_H)

MAX_W = end.second + 11
# print(MIN_W)
# print(MAX_W)

all_walls_positions = [x for x in all_walls_positions if
                       0 <= x.first < MAX_H and 0 <= x.second < MAX_W]

possible_removals = set()
# find_all_wall_to_dissapear_candidates_pairs(all_walls_positions))
for x in all_walls_positions:
    nc = x.neighbouring_coordinates
    nc = [Coordinates(x[0], x[1]) for x in nc]

    nc_that_are_walls = [x for x in nc if x in all_walls_positions]
    if len(nc_that_are_walls) < 3:
        nc_that_are_outside = [x for x in nc if not c_in_map(x)]
        if len(nc_that_are_outside) > 0:
            this_set = {x}
            this_set = frozenset(this_set)

            possible_removals.add(this_set)

solutions = {}
i = 0
print(f'found {len(possible_removals)} possible_removals')
for element in possible_removals:
    print(f'analyzing {element} - {i}')
    i += 1

    element_list = list(element)
    # if Coordinates(7, 10) in element and len(element) == 1:
    #     print('checking')

    all_walls_positions_removed = [x for x in all_walls_positions if x not in element_list]

    all_paths_with_cheat = find_all_paths(start, list(all_walls_positions_removed))
    dj, _ = dijkstra(all_paths_with_cheat, start)

    shortes_path_cheats = dj[end]

    saved_time = shortes_path_cheats - initial_cost_no_cheats
    if saved_time < 0:
        solutions[element] = - saved_time

print(solutions)
output = []
for sol_key, sol_val in solutions.items():
    if sol_val > 100:
        output.append({sol_key: sol_val})

print(len(output))

# +11 -
