from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class Place:
    coordinates: Tuple[int, int]
    height: int
    adjacent_places_coordinates: List[Tuple[int, int]]

    # adjacent_places: List['Place'] = field(default_factory=list)
    #
    # def add_adjacent_place(self, ad_place: 'Place') -> 'Place':
    #     new_adjacent_places = list(self.adjacent_places)
    #     return Place(
    #         self.id,
    #         self.pos1,
    #         self.pos2,
    #         self.height.__eq__(new_adjacent_places)
    #     )

    def __eq__(self, other):
        if not isinstance(other, Place):
            return NotImplemented
        return self.coordinates == other.coordinates

    def __hash__(self):
        return hash(self.coordinates)


def check_if_in_place(width: int,
                      height: int,
                      this_point: Tuple[int, int]
                      ):
    return -1 < this_point[0] < height and -1 < this_point[1] < width


def read_file(file_name: str) -> dict[tuple[int, int], Place]:
    output = {}

    with open(file_name) as file:
        lines = file.readlines()
        lines = [x.rstrip() for x in lines]
        height = len(lines)
        width = len(lines[0])

        for i in range(len(lines)):

            for j in range(len(lines[i])):

                this_place_coordinates = (i, j)
                this_place_height = lines[i][j]

                if this_place_height != '.':
                    x1 = (i - 1, j)
                    x2 = (i + 1, j)
                    x3 = (i, j - 1)
                    x4 = (i, j + 1)

                    place_cand = [x1, x2, x3, x4]
                    places = []

                    for pl_cand in place_cand:
                        c1 = check_if_in_place(width, height, pl_cand)
                        if c1:
                            c2 = lines[pl_cand[0]][pl_cand[1]]
                            if c2 != '.':
                                places.append(pl_cand)

                    output[this_place_coordinates] = Place(coordinates=this_place_coordinates,
                                                           height=int(this_place_height),
                                                           adjacent_places_coordinates=places)
    return output


def find_paths(all_places: dict[tuple[int, int], Place],
               seen_places: List[Place],
               output: List[List[Place]]
               ) -> List[List[Place]]:
    this_place = seen_places[-1]
    if this_place is None:
        print('ALARMO')
        return []

    if this_place.height == 9:
        return [seen_places]

    options = []
    directions = this_place.adjacent_places_coordinates
    for direction in directions:
        candidate = all_places[direction]

        if candidate.height - this_place.height == 1:
            options.append(candidate)

    new_output = list(output)
    for option in options:
        new_seen_places = list(seen_places)
        new_seen_places.append(option)

        this_output = find_paths(all_places,
                                 new_seen_places,
                                 output
                                 )
        if len(this_output) > 0:
            new_output = new_output + this_output

    return new_output


read_file_data = read_file('data/task1.txt')
# print(read_file_data)

trail_heads = {}
for place in read_file_data.values():
    if place.height == 0:
        paths = find_paths(
            read_file_data,
            [place],
            []
        )
        trail_heads[place] = paths

print(f'number of trailheads {len(trail_heads.keys())}')
otuput = 0
for trail_head_key, trail_head_value in trail_heads.items():
    # print('-------')
    print(f'trailhead {trail_head_key}')
    # print(f'no trails {len(trail_head_value)}')
    all_nines = set([x[-1] for x in trail_head_value])
    print(len(all_nines))
    otuput += len(all_nines)

print(otuput)
