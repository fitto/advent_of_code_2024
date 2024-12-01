from typing import List


def read_file(file_name: str) -> tuple[List[int], List[int]]:
    list_a = []
    list_b = []

    with open(file_name, "r") as file:
        for line in file:
            numbers_in_line = line.rstrip().replace('   ', ',').split(',')

            list_a.append(int(numbers_in_line[0]))
            list_b.append(int(numbers_in_line[1]))

    return list_a, list_b


def get_distance(list_1: List[int],
                 list_2: List[int]
                 ) -> int:
    zipped = zip(sorted(list_1), sorted(list_2))

    return sum([abs(itm_a - itm_b) for itm_a, itm_b in zipped])


# test1
# print(read_file('test1.txt'))
# a, b = read_file('test1.txt')
# print(get_distance(a, b))

# task1
a, b = read_file('task1.txt')
print(get_distance(a, b))
