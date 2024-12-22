from typing import Set, List, Dict, Tuple

from bfs import BFS


class KeypadSolver:
    def __init__(self,
                 debug: bool = False
                 ):
        self.total_robots: int = -1

        self.MEMORY_SOLVE: Dict[Tuple[str, int], int] = {}
        self.bfs = BFS()

        self.debug = debug

        self.KEYPAD_BIG = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '0': (3, 1),
            'A': (3, 2)
        }

        self.KEYPAD_SMALL = {
            '^': (0, 1),
            'A': (0, 2),
            '<': (1, 0),
            'v': (1, 1),
            '>': (1, 2)
        }

    def solve(self,
              sequences_list: List[str],
              robots: int
              ) -> Dict[str, int]:
        self.total_robots = robots
        output: Dict[str, int] = {}

        for sequence in sequences_list:
            output[sequence] = self._solve_sub_sequence_for_n(sequence, robots)

        return output

    def _solve_sub_sequence_for_n(self,
                                  sequence: str,
                                  robots: int,
                                  ) -> int:
        if self.debug:
            print('-----------------------------------------------')
            print(f'fired for sequence={sequence}, robots={robots}')
        if robots == self.total_robots:
            keypad = self.KEYPAD_BIG

        else:
            if self.MEMORY_SOLVE.get((sequence, robots)):
                return self.MEMORY_SOLVE[(sequence, robots)]
            keypad = self.KEYPAD_SMALL

        full_sequence = 'A' + sequence
        if self.debug:
            print(f'full_sequence is {full_sequence}')

        full_length = 0
        for i in range(len(full_sequence) - 1):
            if self.debug:
                print(f'analyzing subsequence {full_sequence[i]} to {full_sequence[i + 1]}')
            shortest_paths = self.bfs.bfs_all_shortest_paths(full_sequence[i],
                                                             full_sequence[i + 1],
                                                             keypad
                                                             )
            shortest_paths = {''.join(segment) + 'A' for segment in shortest_paths}

            if robots == 0:
                min_length = min([len(x) for x in shortest_paths])
                full_length += min_length
                if self.debug:
                    print(f'   robots == 0 and full_length is {full_length}')
            else:
                all_oucomes_for_paths: Set[int] = set()
                for shortest_path in shortest_paths:
                    iter_outcome = self._solve_sub_sequence_for_n(
                        shortest_path,
                        robots - 1
                    )
                    all_oucomes_for_paths.add(iter_outcome)
                    if self.debug:
                        print(
                            f'   shortest_path is {shortest_path} and all_oucomes_for_paths is {all_oucomes_for_paths}')
                min_length = min(all_oucomes_for_paths)
                if self.debug:
                    print(f'   min_length is {min_length}')

                full_length += min_length
                if self.debug:
                    print(f'   full_length is {full_length}')

        self.MEMORY_SOLVE[(sequence, robots)] = full_length
        return full_length
