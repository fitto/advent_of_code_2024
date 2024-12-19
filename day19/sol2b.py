from collections import defaultdict
from typing import Tuple, List, Dict


def read_all(file_name: str) -> Tuple[List[str], List[str]]:
    towel_targets = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        towel_options = lines[0].rstrip().split(', ')

        for line in lines[2:]:
            towel_targets.append(line.rstrip())

    return towel_options, towel_targets


def count_combinations(twl: str) -> int:
    if twl in MEMORY.keys():
        return MEMORY[twl]

    if len(twl) == 0:
        return 1

    total_count = 0

    for pos in get_matching_strings(twl, POSSIBLE_TWL):
        new_twl = twl[len(pos):]
        total_count += count_combinations(new_twl)

    MEMORY[twl] = total_count
    return total_count


def preprocess_possible_twl(possible_twl: List[str]) -> Dict[int, List[str]]:
    length_dict = defaultdict(list)
    for string in possible_twl:
        length_dict[len(string)].append(string)
    return length_dict


def get_matching_strings(input_string: str,
                         length_dict: Dict[int, List[str]]
                         ) -> List[str]:
    input_length = len(input_string)
    matching_strings = []

    for length in range(1, input_length + 1):
        if length in length_dict:
            # Filter strings that match the input string
            matching_strings.extend([s for s in length_dict[length] if input_string.startswith(s)])

    matching_strings = sorted(matching_strings, key=lambda x: (len(x), x))
    return matching_strings


# options, targets = read_all('data/1.txt')
options, targets = read_all('data/task1.txt')

verbose = False
MEMORY: Dict[str, int] = {}
POSSIBLE_TWL = preprocess_possible_twl(options)

targets = sorted(targets, key=lambda x: (len(x), x))
options = sorted(options, key=lambda x: (len(x), x))
for o in options:
    count_combinations(o)

options = sorted(options, key=lambda x: (-len(x), x))

output = 0
i = 0
for t in targets:
    comb = count_combinations(t)
    # print(f'all combinatiosn for {t} are {comb}')
    output += comb
    print(f'analyzed {i}')
    i += 1
print(output)

# x = check_if_possible(targets[0], options)

# for target in targets:
# 246
# 227
# 231
# 256
