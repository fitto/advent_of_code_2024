from typing import Dict, Set

from day16.domain.coordinates import Coordinates
from day16.domain.position import Position


def find_key_points(file_name: str):
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
            if char == '#':
                all_walls.add(Coordinates(i, j))
            # if char == '.':
            #     all_allowed.add(Coordinates(i, j))

            if char == '\n':
                i += 1
                j = 0
            else:
                j += 1

    return s, e, all_walls


def find_all_paths(starting_pos: Position,
                   all_walls_coordinates: Set[Coordinates],
                   ) -> Dict[Position, Dict[Position, int]]:
    output = {}
    seen_positions = set()

    positions_to_be_checked = [starting_pos]

    while len(positions_to_be_checked) > 0:
        this_position = positions_to_be_checked.pop()
        if this_position not in seen_positions:
            seen_positions.add(this_position)
            next_postion_options = this_position.move_options_with_cost()

            for k, v in next_postion_options.items():
                if k.coordinates not in all_walls_coordinates:
                    cur = output.get(this_position, {})
                    cur[k] = v

                    output[this_position] = cur

                    cur2 = output.get(k, {})
                    cur2[this_position] = v

                    output[k] = cur2

                    positions_to_be_checked.append(k)

    return output


def dijkstra(graph: Dict[Position, Dict[Position, int]],
             start: Position
             ) -> dict[Position, float]:
    distances = {node: float('inf') for node in graph.keys()}
    distances[start] = 0

    # Priority queue as a standard list
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        # Sort the list by distance and pop the smallest element
        priority_queue.sort(key=lambda x: x[0])  # Sort by distance (O(n log n))
        current_distance, current_node = priority_queue.pop(0)  # Remove the smallest (O(1))

        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))  # Add new entry (O(1))

    return distances


# start, end, all_walls_positions = find_key_points('data/22.txt')
start, end, all_walls_positions = find_key_points('data/task1.txt')
print(f'start coord {start}')
print(f'end coord {end}')

start_position = Position(start, '>')
pths = find_all_paths(start_position, all_walls_positions)

sp = dijkstra(pths, start_position)

end_positions = [
    Position(end, '>'),
    Position(end, '<'),
    Position(end, '^'),
    Position(end, 'v')
]

m = float('inf')
for x in end_positions:
    gt_o = sp.get(x, -1)
    print(f'{x.__repr__()}: {gt_o}')
    if gt_o < m:
        m = gt_o

print(m)
