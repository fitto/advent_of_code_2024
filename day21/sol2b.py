from collections import deque
from typing import Dict, Set, Tuple, Optional

from typing_extensions import List

from day21.keypads.keypads import KEYPAD_BIG, KEYPAD_SMALL

POSSIBLE_MOVES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

MEMORY_BFS = {}


def bfs_all_shortest_paths(start_key: str,
                           target_key: str,
                           keypad: Dict[str, Tuple[int, int]]
                           ) -> Set[str]:
    if MEMORY_BFS.get((start_key, target_key)):
        return MEMORY_BFS[(start_key, target_key)]

    start_coordinates = keypad[start_key]
    target_coordinates = keypad[target_key]

    queue = deque([(start_coordinates, '')])

    visited = {start_coordinates: 0}

    shortest_paths = set()
    shortest_length = float('inf')

    while queue:
        current_coordinates, path = queue.popleft()

        if len(path) <= shortest_length:

            if current_coordinates == target_coordinates:
                if len(path) < shortest_length:
                    shortest_length = len(path)
                    shortest_paths = {path}
                elif len(path) == shortest_length:
                    shortest_paths.add(path)
                continue

            for move_name, (i, j) in POSSIBLE_MOVES.items():
                next_coordinates = (current_coordinates[0] + i, current_coordinates[1] + j)

                if next_coordinates in keypad.values():
                    if next_coordinates not in visited or len(path) + 1 <= visited[next_coordinates]:
                        new_len = len(path) + 1
                        if new_len <= shortest_length:
                            visited[next_coordinates] = new_len
                            queue.append((next_coordinates, path + move_name))

    MEMORY_BFS[(start_key, target_key)] = shortest_paths
    return shortest_paths


MEMORY_FULL_PATHS: Dict[str, Tuple[Set[str], int]] = {}


def full_paths(needed_combination: str,
               keypad: Dict[str, Tuple[int, int]],
               max_cost: Optional[int] = None
               ) -> Tuple[Set[str], int]:
    cached_response = COST_MEM.get(needed_combination)
    if cached_response is not None:
        if max_cost is not None and cached_response[1] > max_cost:
            return set(), max_cost
        else:
            return cached_response

    all_solutions = {''}

    current_letter = 'A'
    for char in needed_combination:
        fst = bfs_all_shortest_paths(current_letter, char, keypad)
        fst = {''.join(segment) + 'A' for segment in fst}
        all_solutions = {s + f for s in all_solutions for f in fst}
        current_letter = char

    min_cost = None
    if max_cost is not None:
        costs = {s: get_cost(s, max_cost) for s in all_solutions}
        min_cost = min((cost for cost in costs.values() if cost is not None), default=None)

        filtered_solutions = {s for s, cost in costs.items() if cost == min_cost}
    else:
        filtered_solutions = all_solutions

    MEMORY_FULL_PATHS[needed_combination] = (filtered_solutions, min_cost)
    return filtered_solutions, min_cost


def solve(input_table: List[str]) -> int:
    output = 0
    for this_string in input_table:
        print(f'Analyzing {this_string}')
        big_keypad_options_response = full_paths(this_string,
                                                 KEYPAD_BIG,
                                                 None
                                                 )

        this_big_keypad_options = big_keypad_options_response[0]
        for i in range(ROBOTS):
            print(f'   iteration: {i}')
            max_cost = None

            big_keypad_next_options: Set[str] = set()

            for big_keypad_option in this_big_keypad_options:
                big_keypad_options_response = full_paths(big_keypad_option,
                                                         KEYPAD_SMALL,
                                                         max_cost)

                max_cost = big_keypad_options_response[1]
                big_keypad_next_options |= big_keypad_options_response[0]

            this_big_keypad_options = big_keypad_next_options

        min_length = min(len(s) for s in this_big_keypad_options)
        numeric_part = int(this_string[:-1])

        output += min_length * numeric_part
    return output


COST_MEM = {}


def get_cost(this_string: str,
             max_cost: int
             ) -> Optional[int]:
    cached_cost = COST_MEM.get(this_string)
    if cached_cost:
        return None if cached_cost > max_cost else cached_cost

    cost = 0
    if len(this_string) > 0:

        for i in range(len(this_string) - 1):
            cost += ALL_COSTS[(this_string[i], this_string[i + 1])]
            if cost > max_cost:
                return None

    COST_MEM[this_string] = cost
    return cost


ALL_COSTS = {
    ('^', '^'): 0,
    ('^', 'v'): 1,
    ('^', '<'): 2,
    ('^', '>'): 2,
    ('^', 'A'): 1,

    ('v', 'v'): 0,
    ('v', '^'): 1,
    ('v', '<'): 1,
    ('v', '>'): 1,
    ('v', 'A'): 2,

    ('<', '<'): 0,
    ('<', '^'): 2,
    ('<', 'v'): 1,
    ('<', '>'): 2,
    ('<', 'A'): 3,

    ('>', '>'): 0,
    ('>', '^'): 2,
    ('>', 'v'): 1,
    ('>', '<'): 2,
    ('>', 'A'): 1,

    ('A', 'A'): 0,
    ('A', '^'): 1,
    ('A', 'v'): 2,
    ('A', '<'): 3,
    ('A', '>'): 1,
}

ROBOTS = 25

this_task = [
    '463A',
    '340A',
    '129A',
    '083A',
    '341A'
]

# x = full_paths('029A', KEYPAD_BIG)
x = solve(this_task)
print(x)
