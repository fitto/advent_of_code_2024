from collections import deque
from typing import Dict, Tuple, Set, Optional


class BFS:
    def __init__(self,
                 possible_moves: Optional[Dict[str, Tuple[int, int]]] = None
                 ):
        if possible_moves is None:
            self.POSSIBLE_MOVES = {
                "^": (-1, 0),
                "v": (1, 0),
                "<": (0, -1),
                ">": (0, 1)
            }
        else:
            self.POSSIBLE_MOVES = possible_moves

    def bfs_all_shortest_paths(self,
                               start_key: str,
                               target_key: str,
                               keypad: Dict[str, Tuple[int, int]],
                               ) -> Set[str]:
        start_coordinates = keypad[start_key]
        target_coordinates = keypad[target_key]

        queue = deque([(start_coordinates, '')])

        visited: Dict[Tuple[int, int], int] = {start_coordinates: 0}

        shortest_paths: Set[str] = set()
        shortest_length = float('inf')

        while queue:
            current_coordinates, path = queue.popleft()

            # here an additional condition to not continue searches when anyway now path is too long  - possible because cost is always 1
            if len(path) <= shortest_length:
                if current_coordinates == target_coordinates:
                    if len(path) < shortest_length:
                        shortest_length = len(path)
                        shortest_paths = {path}

                    elif len(path) == shortest_length:
                        shortest_paths.add(path)
                    continue

                for move_name, (i, j) in self.POSSIBLE_MOVES.items():
                    next_coordinates = (current_coordinates[0] + i, current_coordinates[1] + j)

                    if next_coordinates in keypad.values():
                        if next_coordinates not in visited or len(path) + 1 <= visited[next_coordinates]:
                            visited[next_coordinates] = len(path) + 1
                            queue.append((next_coordinates, path + move_name))

        return shortest_paths
