from collections import deque
from itertools import combinations
from typing import Dict, Set, List

from day18.coordinates import Coordinates
from day21.keypads.keypads import KEYPAD_BIG, KEYPAD_SMALL

POSSIBLE_MOVES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

MEMORY_BIG_KEYBOARD = {}


def bfs_all_shortest_paths(start_key: str,
                           target_key: str,
                           keypad: Dict[str, Coordinates]
                           ):
    if keypad == KEYPAD_BIG:
        check = MEMORY_BIG_KEYBOARD.get((start_key, target_key), None)
        if check:
            return check

    start_coordinates = keypad[start_key]
    target_coordinates = keypad[target_key]

    queue = deque([(start_coordinates, [])])

    visited = {start_coordinates: 0}  # Track visited positions with their path length

    shortest_paths = []
    shortest_length = float('inf')

    while queue:
        current_coordinates, path = queue.popleft()

        if current_coordinates == target_coordinates:
            if len(path) < shortest_length:
                shortest_length = len(path)
                shortest_paths = [path]
            elif len(path) == shortest_length:
                shortest_paths.append(path)
            continue

        for move_name, (i, j) in POSSIBLE_MOVES.items():
            next_coordinates = current_coordinates.shifted_coordinates(i, j)

            # Check if the next position is valid
            if next_coordinates in keypad.values():
                if next_coordinates not in visited or len(path) + 1 <= visited[next_coordinates]:
                    visited[next_coordinates] = len(path) + 1
                    queue.append((next_coordinates, path + [move_name]))

    MEMORY_BIG_KEYBOARD[(start_key, target_key)] = shortest_paths
    return shortest_paths


def full_paths(needed_combination: str,
               keypad: Dict[str, Coordinates]
               ) -> Set[str]:
    all_solutions = {''}

    current_letter = 'A'
    for char in needed_combination:
        fst = bfs_all_shortest_paths(current_letter, char, keypad)
        fst = {''.join(segment) + 'A' for segment in fst}

        all_solutions = {s + f for s in all_solutions for f in fst}
        current_letter = char

    return all_solutions


def solve(input_table: List[str]) -> int:
    output = 0
    for this_string in input_table:
        print(f'analyzing {this_string}')

        big_keypad_options = full_paths(this_string,
                                        KEYPAD_BIG
                                        )

        temp = {}
        min_val = float('inf')
        for opt in big_keypad_options:
            cst = get_cost(opt)

            if cst <= min_val:
                temp[opt] = cst
                min_val = cst

        small_keypad_options = set(key for key, val in temp.items() if val == min_val)

        for i in range(ROBOTS_NO):
            print(f'iteration: {i}')

            new_small_keypad_options: Set[str] = set()
            for small_keypad_option in small_keypad_options:
                paths = full_paths(small_keypad_option,
                                   KEYPAD_SMALL)

                temp = {}
                min_val = float('inf')

                for opt in paths:
                    cst = get_cost(opt)
                    # print(f'{opt} and cost is {cst}')

                    if cst <= min_val:
                        temp[opt] = cst
                        min_val = cst

                all_shortest_opt = set(key for key, val in temp.items() if val == min_val)

                new_small_keypad_options |= all_shortest_opt

        numeric_part = int(this_string[:-1])
        min_length = min(len(s) for s in new_small_keypad_options)
        output += min_length * numeric_part
        print(min_length)
        print(numeric_part)
        print('---------------------')
    return output


def get_cost(this_string: str) -> int:
    cost = 0

    for i in range(len(this_string) - 1):
        cost += ALL_COSTS.get((this_string[i], this_string[i + 1]), 0)

    return cost


this_test = [
    '029A',
    '980A',
    '179A',
    '456A',
    '379A'
]

this_task = [
    '463A'
    # ,
    # '340A',
    # '129A',
    # '083A',
    # '341A'
]

ROBOTS_NO = 1

ALL_COSTS = {
{('<', '>'): 1, ('<', 'A'): 2, ('>', 'A'): 1, ('^', '<'): 1, ('^', '>'): 2, ('^', 'A'): 1, ('^', 'v'): 1, ('v', '<'): 1, ('v', '>'): 1, ('v', 'A'): 2}


# PRECALCULATION
all_combinations = []


options = list(POSSIBLE_MOVES.keys())
options.append('A')

for i in range(ROBOTS_NO):
    for r in range(1, len(POSSIBLE_MOVES) + 1):  # r is the length of combinations
        all_combinations.extend([''.join(comb) for comb in combinations(options, r)])

    all_combinations = [x for x in all_combinations if len(x) == 2]
    for x in all_combinations:
        for x in all_combinations:
            b = bfs_all_shortest_paths(x[0], x[1], KEYPAD_SMALL)
            # print(f'x is {x} - b is {b}')

            ALL_COSTS[(x[0], x[1])] = len(b)

# print(all_combinations)
#
x = solve(this_test)
print(f'OUTPUT is {x}')
