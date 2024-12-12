from typing import Tuple, List


def check_if_in_place(width: int,
                      height: int,
                      this_point_coord: Tuple[int, int]
                      ):
    return -1 < this_point_coord[0] < height and -1 < this_point_coord[1] < width


def read_file(file_name: str) -> List[List[str]]:
    output = []

    with open(file_name, "r") as file:
        for line in file:
            row = line.rstrip()
            this_row = []
            for rr in row:
                this_row.append(rr)

            output.append(this_row)

    return output


this_place = read_file('data/1/11.txt')
# this_place = read_file('data/task1.txt')
print(this_place)
