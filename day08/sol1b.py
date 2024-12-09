from typing import List, Tuple


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

    def is_in_line_with_antena(self,
                               other_antena: 'Antena'
                               ) -> bool:
        if self.first_coordinate == other_antena.first_coordinate:
            return True
        if self.second_coordinate == other_antena.second_coordinate:
            return True

        cor_1, cor_2 = self.first_coordinate, self.second_coordinate

        while cor_1 < 51 and cor_2 > 0:
            cor_1 += 1
            cor_2 -= 1
            if other_antena.first_coordinate == cor_1 and other_antena.second_coordinate == cor_2:
                return True

        cor_1, cor_2 = self.first_coordinate, self.second_coordinate
        while cor_1 > 0 and cor_2 < 51:
            cor_1 -= 1
            cor_2 += 1
            if other_antena.first_coordinate == cor_1 and other_antena.second_coordinate == cor_2:
                return True

        cor_1, cor_2 = self.first_coordinate, self.second_coordinate
        while cor_1 > -1 and cor_2 > -1:
            cor_1 -= 1
            cor_2 -= 1
            if other_antena.first_coordinate == cor_1 and other_antena.second_coordinate == cor_2:
                return True

        cor_1, cor_2 = self.first_coordinate, self.second_coordinate
        while cor_1 < 51 and cor_2 < 51:
            cor_1 += 1
            cor_2 += 1
            if other_antena.first_coordinate == cor_1 and other_antena.second_coordinate == cor_2:
                return True

        return False

    def get_antinodes(self,
                      other_antena: 'Antena'
                      ) -> List[Tuple[int, int]]:

        fc_dist = abs(self.first_coordinate - other_antena.first_coordinate)
        sc_dist = abs(self.second_coordinate - other_antena.second_coordinate)

        if self.first_coordinate <= other_antena.first_coordinate and self.second_coordinate <= other_antena.second_coordinate:
            return [
                (self.first_coordinate - fc_dist, self.second_coordinate - sc_dist),
                (other_antena.first_coordinate + fc_dist, other_antena.second_coordinate + sc_dist),
            ]
        elif self.first_coordinate <= other_antena.first_coordinate and self.second_coordinate > other_antena.second_coordinate:
            return [
                (self.first_coordinate - fc_dist, self.second_coordinate + sc_dist),
                (other_antena.first_coordinate + fc_dist, other_antena.second_coordinate - sc_dist),
            ]
        elif self.first_coordinate > other_antena.first_coordinate and self.second_coordinate > other_antena.second_coordinate:
            return [
                (self.first_coordinate + fc_dist, self.second_coordinate + sc_dist),
                (other_antena.first_coordinate - fc_dist, other_antena.second_coordinate - sc_dist),
            ]
        elif self.first_coordinate > other_antena.first_coordinate and self.second_coordinate < other_antena.second_coordinate:
            return [
                (self.first_coordinate + fc_dist, self.second_coordinate - sc_dist),
                (other_antena.first_coordinate - fc_dist, other_antena.second_coordinate + sc_dist),
            ]
        else:
            print('WUT??')
            return []


def check_if_in_place(this_place: list[list[str]],
                      this_point: Tuple[int, int]
                      ):
    return -1 < this_point[0] < len(this_place) and -1 < this_point[1] < len(this_place[0])


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


read_file_data = read_file('data/task1.txt')
place = read_file_data[0]
print(f'x_dimensions = {len(place)}')
print(f'y_dimensions = {len(place[0])}')

antenas = [a for a in read_file_data[1]]

# print(place)
# print(antenas)

all_antinodes = []

for i in range(len(antenas)):
    this_antena = antenas[i]
    # print('--------------')
    # print(this_antena)
    for other_antena_itm in [x for j, x in enumerate(antenas) if j != i]:
        if this_antena.letter == other_antena_itm.letter:
            # print(other_antena_itm)
            new_antinodes = this_antena.get_antinodes(other_antena_itm)
            # print(new_antinodes)
            all_antinodes.extend(new_antinodes)

# print(all_antinodes)
all_antinodes_set = set(all_antinodes)
print(len(all_antinodes_set))
for an in all_antinodes_set:
    print(an)

all_antinodes_in_place = [x for x in all_antinodes_set if check_if_in_place(place, x)]
print(len(all_antinodes_in_place))
#
