from typing import List, Dict


def read_file(file_name: str) -> tuple[List[int], Dict[int, int]]:
    list_a = []
    dict_b = {}

    with open(file_name, "r") as file:
        for line in file:
            numbers_in_line = line.rstrip().replace('   ', ',').split(',')

            list_a.append(int(numbers_in_line[0]))

            no_2 = int(numbers_in_line[1])
            dict_b[no_2] = dict_b.get(no_2, 0) + 1

    return list_a, dict_b


def get_similarity(list_1: List[int],
                   dict_2: Dict[int, int]
                   ) -> int:
    return sum([itm_a * dict_2.get(itm_a, 0) for itm_a in list_1])


# test1
# print(read_file('test1.txt'))
# a, b = read_file('test1.txt')
# print(get_similarity(a, b))

# task1
a, b = read_file('task1.txt')
print(get_similarity(a, b))
