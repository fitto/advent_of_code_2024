from collections import deque
from typing import Dict, Set, List, Tuple

from day21.keypads.keypads import KEYPAD_BIG

POSSIBLE_MOVES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

MEMORY_BIG_KEYBOARD = {}


def bfs_all_shortest_paths(start_key: str,
                           target_key: str,
                           keypad: Dict[str, Tuple[int, int]],
                           ) -> List[str]:
    if (start_key, target_key) in MEMORY_BIG_KEYBOARD:
        return MEMORY_BIG_KEYBOARD[(start_key, target_key)]

    start_coordinates = keypad[start_key]
    target_coordinates = keypad[target_key]

    queue = {(start_coordinates, ''}

    visited = {start_coordinates: 0}
    shortest_length = float('inf')
    shortest_paths = []

    while queue:
        current_coordinates, path = queue.pop(0)

        if current_coordinates == target_coordinates:
            if len(path) < shortest_length:
                shortest_length = len(path)
                shortest_paths = path
            elif len(path) == shortest_length:
                shortest_paths += path
            continue

        for move_name, (i, j) in POSSIBLE_MOVES.items():
            next_coordinates = (current_coordinates[0] + i, current_coordinates[1] + j)

            if next_coordinates in keypad.values():
                if next_coordinates not in visited or len(path) + 1 <= visited[next_coordinates]:
                    visited[next_coordinates] = len(path) + 1
                    queue.append((next_coordinates, path + move_name))

    output = shortest_paths
    MEMORY_BIG_KEYBOARD[(start_key, target_key)] = output
    return output


def full_paths(needed_combination: str,
               keypad: Dict[str, Tuple[int, int]],
               ) -> Set[str]:
    all_solutions = {''}

    current_letter = 'A'
    for char in needed_combination:
        fst = bfs_all_shortest_paths(current_letter, char, keypad)

        # if not fst:
        #     return set()
        #
        # fst = {''.join(segment) + 'A' for segment in fst}
        # all_solutions = {s + f for s in all_solutions for f in fst}
        current_letter = char
        print(fst)


    return all_solutions


x = full_paths('029A', KEYPAD_BIG)
