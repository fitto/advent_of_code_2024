import re
from os.path import samefile
from typing import List, Dict, Tuple, Any, Set


class Antena:
    def __init__(self,
                 first_coordinate: int,
                 second_coordinate: int,
                 letter: str,
                 ):
        self.first_coordinate = first_coordinate
        self.second_coordinate = second_coordinate
        self.letter = letter

    def __str__(self) -> str:
        return f"Antena(first_coordinate={self.first_coordinate}, second_coordinate={self.second_coordinate}, letter={self.letter})"

    def __repr__(self) -> str:
        return f"Antena(first_coordinate={self.first_coordinate}, second_coordinate={self.second_coordinate}, letter={self.letter})"

    def __hash__(self) -> int:
        return hash((self.first_coordinate, self.second_coordinate, self.letter))

    def is_same_letter(self,
                       other: 'Antena') -> bool:
        return self.letter == other.letter


def read_file(file_name: str) -> tuple[list[list[str]], set[Antena]]:
    text_table = []
    all_antenas = set()

    with open(file_name, "r") as file:
        x = 0
        for line in file:
            row = []
            y = 0
            for char in line.rstrip():
                row += char
                if char != '.':
                    all_antenas.add(Antena(x, y, char))
                y += 1
            x += 1

            # print(row)
            text_table.append(row)

    return text_table, all_antenas


def check_antena_lines(antena: Antena,
                       place_table: List[List[str]]
                       ) -> Dict[str, List[str]]:
    points = []
    output = {}

    horizontal_line = place_table[antena.first_coordinate]
    if horizontal_line.count(antena.letter) > 1:
        point_coord = []

        for x in range(len(horizontal_line)):
            if horizontal_line[x] == antena.letter:
                point_coord.append(x)

        if len(point_coord) > 2:
            print('ALARMOOOO')
        else:
            p1 = point_coord[0]
            p2 = point_coord[1]
            dist = p2 - p1

            if p1 - dist > -1:
                points.append((antena.first_coordinate, p1 - dist))
            if p2 + dist < len(horizontal_line) - 1:
                points.append((antena.first_coordinate, p2 + dist))

    output['horizontal_line'] = horizontal_line

    vertical_line = [row[antena.second_coordinate] for row in place_table]
    output['horizontal_line'] = vertical_line

    # diagonal1 - left down to top right
    diagonal_1 = []
    cor_1, cor_2 = antena.first_coordinate, antena.second_coordinate

    while cor_1 < len(place_table) - 1 and cor_2 > 0:
        cor_1 += 1
        cor_2 -= 1
        diagonal_1 += place_table[cor_1][cor_2]

    diagonal_1.reverse()

    cor_1, cor_2 = antena.first_coordinate, antena.second_coordinate
    diagonal_1.append(place_table[cor_1][cor_2])
    while cor_1 > 0 and cor_2 < len(place_table[0]) - 1:
        cor_1 -= 1
        cor_2 += 1
        diagonal_1 += place_table[cor_1][cor_2]

    output['diagonal_1'] = diagonal_1

    # diagonal2 -> left_top to right bottom
    diagonal_2 = []
    cor_1, cor_2 = antena.first_coordinate, antena.second_coordinate
    while cor_1 > -1 and cor_2 > -1:
        cor_1 -= 1
        cor_2 -= 1
        diagonal_2 += place_table[cor_1][cor_2]

    diagonal_2.reverse()

    cor_1, cor_2 = antena.first_coordinate, antena.second_coordinate
    diagonal_2.append(place_table[cor_1][cor_2])
    while cor_1 < len(place_table) - 1 and cor_2 < len(place_table[0]) - 1:
        cor_1 += 1
        cor_2 += 1
        diagonal_2 += place_table[cor_1][cor_2]

    output['diagonal_2'] = diagonal_2

    return output


read_file_data = read_file('../data/test0.txt')
place = read_file_data[0]
print(f'x_dimensions = {len(place)}')
print(f'y_dimensions = {len(place[0])}')

antenas = [a for a in read_file_data[1]]

print(place)
print(antenas)
#

print(antenas[0])
all_lines = check_antena_lines(antenas[0],
                               place,
                               )
print(all_lines)

