from typing import Tuple, List, Dict


def read_all(file_name: str) -> Tuple[List[str], List[str]]:
    towel_targets = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        towel_options = lines[0].rstrip().split(', ')

        for line in lines[2:]:
            towel_targets.append(line.rstrip())

    return towel_options, towel_targets


verbose = False
CAN_BE_DONE: Dict[str, bool] = {}


def check_if_possible(twl: str,
                      possible_twl: List[str]
                      ) -> bool:
    if verbose:
        print(f'------------ looking at {twl}')

    if twl in CAN_BE_DONE.keys():
        if verbose:
            print(f'- found in mem')
        return CAN_BE_DONE[twl]

    if len(twl) == 0:
        if verbose:
            print(f'- len is 0')
        CAN_BE_DONE[twl] = True
        return True

    else:
        for pos in possible_twl:
            if twl.startswith(pos):
                if verbose:
                    print(f'- twl starts with {pos}')

                new_towel = twl
                new_towel = new_towel.removeprefix(pos)

                checked = check_if_possible(new_towel, possible_twl)

                if checked:
                    CAN_BE_DONE[pos] = checked
                    if verbose:
                        print(f'---- returning here {checked}')
                    return checked

    CAN_BE_DONE[twl] = False
    if verbose:
        print(f'---- returning False')
    return False


# options, targets = read_all('data/1.txt')
options, targets = read_all('data/task1.txt')

options = sorted(options, key=lambda x: (-len(x), x))
targets = sorted(targets, key=lambda x: (len(x), x))

output = 0
for t in targets:
    possible = check_if_possible(t, options)
    # print(f'{"xxxx" if not possible else ''} towel is: {t} and it {possible}')
    if check_if_possible(t, options):
        output += 1
print(output)

# x = check_if_possible(targets[0], options)

# for target in targets:
# 246
# 227
# 231
# 256
