from collections import deque
from typing import Dict, Set, List

from day18.coordinates import Coordinates
from day21.keypads.keypads import KEYPAD_BIG, KEYPAD_SMALL

POSSIBLE_MOVES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}


def bfs_all_shortest_paths(start_key: str,
                           target_key: str,
                           keypad: Dict[str, Coordinates]
                           ):
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
        big_keypad_options = full_paths(this_string,
                                        KEYPAD_BIG
                                        )
        # print(big_keypad_options)

        first_small_keypad_options: Set[str] = set()
        for big_keypad_option in big_keypad_options:
            paths = full_paths(big_keypad_option,
                               KEYPAD_SMALL)
            # print(f'{big_keypad_option} - and {len(paths)} solutions are: {paths}')
            first_small_keypad_options |= paths

        print(f'first_small_keypad_options len = {len(first_small_keypad_options)}')
        # print('v<<A>>^A<A>AvA<^AA>A<vAAA>^A' in first_small_keypad_options)

        second_small_keypad_options: Set[str] = set()
        for first_small_keypad_option in first_small_keypad_options:
            paths = full_paths(first_small_keypad_option,
                               KEYPAD_SMALL)
            # print(f'{big_keypad_option} - and {len(paths)} solutions are: {paths}')
            second_small_keypad_options |= paths

        print(f'second_small_keypad_options len = {len(second_small_keypad_options)}')
        # print('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A' in second_small_keypad_options)

        # third_small_keypad_options: Set[str] = set()
        # for second_small_keypad_option in second_small_keypad_options:
        #     paths = full_paths(second_small_keypad_option,
        #                        KEYPAD_SMALL)
        #     # print(f'{big_keypad_option} - and {len(paths)} solutions are: {paths}')
        #     third_small_keypad_options |= paths
        # x = full_paths('A029A')
        # print(x)

        min_length = min(len(s) for s in second_small_keypad_options)
        numeric_part = int(this_string[:-1])

        output += min_length * numeric_part
        print(min_length)
        # print(numeric_part)
        # print('---------------------')
    return output


this_test = [
    '029A',
    '980A',
    '179A',
    '456A',
    '379A'
]

this_task = [
    '463A',
    '340A',
    '129A',
    '083A',
    '341A'
]

x = solve(this_task)
print(x)
# --94 426