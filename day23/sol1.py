from itertools import combinations
from typing import List, Dict, Set


def read_all(file_name: str) -> Dict[str, List[str]]:
    output: Dict[str, List[str]] = {}

    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.rstrip()
            split_line = line.split('-')

            this_list = output.get(split_line[0], [])
            this_list.append(split_line[1])
            output[split_line[0]] = this_list

            this_list = output.get(split_line[1], [])
            this_list.append(split_line[0])
            output[split_line[1]] = this_list

    return output


def check_three_computers(c1: str, c2: str, c3: str, all_connections: Dict[str, List[str]]) -> bool:
    if c2 in all_connections.get(c1, []) and c3 in all_connections.get(c1, []) and c3 in all_connections.get(c2, []):
        return True
    return False


def is_in_connected_three(computer: str,
                          connections: Dict[str, List[str]]
                          ) -> Set[frozenset]:
    connected_pcs = connections.get(computer, [])
    if len(connected_pcs) < 2:
        return set()
    else:
        output_lists: Set[frozenset] = set()

        all_three_comb = list(combinations(connected_pcs, 2))
        for comb in all_three_comb:
            if check_three_computers(comb[0], comb[1], computer, connections):
                short_set = frozenset([comb[0], comb[1], computer])

                output_lists.add(short_set)

        return output_lists


# connections = read_all('data/11.txt')
connections = read_all('data/task1.txt')
# print(connections)

all_threes: Set[frozenset] = set()

for this_computer in connections:
    if this_computer[0] == 't':
        all_threes |= is_in_connected_three(this_computer, connections)

print(all_threes)
print(len(all_threes))
# --2297