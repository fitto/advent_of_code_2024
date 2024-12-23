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


def check_n_computers(computers: List[str],
                      all_connections: Dict[str, List[str]]
                      ) -> bool:
    for i in range(len(computers)):
        for j in range(i + 1, len(computers)):
            if computers[j] not in all_connections.get(computers[i], []):
                return False
    return True


def is_in_connected_n(computer: str,
                      connections: Dict[str, List[str]],
                      n: int
                      ) -> Set[frozenset]:
    connected_pcs = connections.get(computer, [])
    if len(connected_pcs) < n - 1:
        return set()
    else:
        output_lists: Set[frozenset] = set()

        all_n_comb = list(combinations(connected_pcs, n))
        for comb in all_n_comb:
            comb_and_c = list(comb)
            comb_and_c.append(computer)
            if check_n_computers(list(comb_and_c), connections):
                short_set = frozenset(comb_and_c)
                output_lists.add(short_set)

        return output_lists


# connections = read_all('data/11.txt')
connections = read_all('data/task1.txt')
# print(connections)

previous_lan_parties: Set[frozenset] = set()
i = 2
while True:
    lan_parties: Set[frozenset] = set()

    for this_computer in connections:
        # if this_computer[0] == 't':
        lan_parties |= is_in_connected_n(this_computer, connections, i)

    if len(lan_parties) == 0:
        print(f'max i is {i}')
        break
    else:
        i += 1
        previous_lan_parties = lan_parties

this_list = list(previous_lan_parties.pop())
this_list = sorted(this_list)
print(this_list)
# 'aj','ds','gg','id','im','jx','kq','nj','ql','qr','ua','yh','zn'


# 'ae','bm','ei','mz','oe','ri','rq','tz','uf','vo','xd','ym'
# 'cr','ev','if','lk','lp','ng','pa','pv','sq','tn','vk','yk'
