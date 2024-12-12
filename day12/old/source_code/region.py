from collections import Counter
from dataclasses import dataclass
from typing import List, Optional, Tuple

from day12.old.source_code.place import Place


@dataclass(frozen=True)
class Region:
    id: int
    places: List[Place]

    def add_place(self, place: Place) -> 'Region':
        new_places = [c for c in self.places]
        new_places.append(place)
        return Region(self.id, new_places)

    def __repr__(self):
        return f'Region({self.id}) {self.plant_type}: {len(self.places)}'

    @property
    def plant_type(self) -> Optional[str]:
        return self.places[0].plant_type or None

    @property
    def area(self):
        return len(self.places)

    def perimeter(self, this_map: List[List[str]]):
        if self.area == 1:
            return 4
        elif self.area == 2:
            return 6
        else:
            sum_walls = 0
            for place in self.places:
                i = place.coordinates[0]
                j = place.coordinates[1]

                cand_coordinates = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1)
                ]

                for x in cand_coordinates:
                    if not check_if_in_place(len(this_map[0]), len(this_map), x):
                        sum_walls += 1
                    else:
                        if this_map[x[0]][x[1]] != self.plant_type:
                            sum_walls += 1

            return sum_walls

    def perimeter_places(self, this_map: List[List[str]]) -> List[Place] | None:
        if self.area == 1 or self.area == 2:
            return None
        else:
            wall_places = []
            for place in self.places:
                for x in place_neighbours_all(place):
                    if not check_if_in_place(len(this_map[0]), len(this_map), x):
                        wall_places.append(Place(x, 'xxxxx'))
                    else:
                        if this_map[x[0]][x[1]] != self.plant_type:
                            wall_places.append(Place(x, this_map[x[0]][x[1]]))

            return wall_places

    def walls_no(self, this_map: List[List[str]]) -> int:
        if self.area == 1:
            return 4
        elif self.area == 2:
            return 4
        else:
            found_walls_no = 0
            all_perimeter_places = self.perimeter_places(this_map)

            counter = Counter(all_perimeter_places)
            dupes = [item for item, count in counter.items() if count > 1]

            all_perimeter_places = sorted(all_perimeter_places,
                                          key=lambda place: (place.coordinates[0], place.coordinates[1]))

            i = 0
            itr_max = len(all_perimeter_places)

            not_starting_points_horizonatl = set()
            not_starting_points_vertical = set()
            # saw_places = set()

            while i < itr_max:
                this_point = all_perimeter_places[i]

                if this_point in not_starting_points_horizonatl:
                    this_line = []
                else:
                    this_line = [this_point]

                    while True:
                        nbr_in_same_line = neighbours_in_same_line(all_perimeter_places, this_point)
                        nbr_in_same_line = [x for x in nbr_in_same_line if
                                            x in all_perimeter_places and x not in this_line]

                        if len(nbr_in_same_line) > 0:
                            nbr_in_same_line = sorted(nbr_in_same_line, key=lambda place: place.coordinates[1])
                            this_neighbour = nbr_in_same_line.pop()

                            if this_neighbour.coordinates[1] - this_point.coordinates[1] == 1:
                                this_line.append(this_neighbour)
                                this_point = this_neighbour
                            else:
                                break

                        else:
                            break

                if this_point in not_starting_points_vertical:
                    this_line2 = []
                else:
                    this_line2 = [this_point]
                    while True:
                        nbr_in_same_column = neighbours_in_same_row(all_perimeter_places, this_point)
                        nbr_in_same_column = [x for x in nbr_in_same_column if
                                              x in all_perimeter_places and x not in this_line2]

                        if len(nbr_in_same_column) > 0:
                            nbr_in_same_column = sorted(nbr_in_same_column, key=lambda place: place.coordinates[0])
                            this_neighbour = nbr_in_same_column.pop()

                            if this_neighbour.coordinates[0] - this_point.coordinates[0] == 1:
                                this_line2.append(this_neighbour)
                                this_point = this_neighbour
                            else:
                                break
                        else:
                            break

                # print(this_line)
                # print(this_line2)

                if len(this_line) > 1:
                    found_walls_no += 1
                    # print(f'added 1')

                    for i in range(len(this_line)):
                        not_starting_points_horizonatl.add(this_line[i])
                        if i != len(this_line) - 1:
                            not_starting_points_vertical.add(this_line[i])

                    if len(this_line2) == 1:
                        for p in this_line2:
                            not_starting_points_vertical.add(p)

                if len(this_line2) > 1:
                    found_walls_no += 1
                    # print(f'added2')

                    for i in range(len(this_line2)):
                        not_starting_points_vertical.add(this_line2[i])
                        if i != len(this_line2) - 1:
                            not_starting_points_horizonatl.add(this_line2[i])

                    if len(this_line) == 1:
                        for p in this_line:
                            not_starting_points_horizonatl.add(p)

                if len(this_line2) == 1 and len(this_line) == 1:
                    found_walls_no += 1
                    # print(f'added3')
                    not_starting_points_horizonatl.add(this_line2[0])
                    not_starting_points_vertical.add(this_line2[0])

                i += 1

        return found_walls_no + len(dupes)

    def has_place(self, place: Place):
        return place in self.places


def check_if_in_place(width: int,
                      height: int,
                      this_point_coord: Tuple[int, int]
                      ):
    return -1 < this_point_coord[0] < height and -1 < this_point_coord[1] < width


def find_regions(this_map: List[List[str]]) -> List[Region]:
    output = []

    saw_places = set()

    width = len(this_map[0])
    heigth = len(this_map)

    rid = 1

    for i in range(width):
        for j in range(heigth):
            if (i, j) not in saw_places:
                initial_place = Place((i, j), this_map[i][j])
                this_region = Region(rid, [initial_place])
                rid += 1

                place_cand = place_neighbours_on_map(initial_place, this_map)
                while len(place_cand) > 0:
                    cnd = place_cand.pop()

                    if this_region.plant_type == cnd.plant_type and cnd.coordinates not in saw_places and not this_region.has_place(
                            cnd):
                        this_region = this_region.add_place(cnd)
                        saw_places.add(cnd.coordinates)
                        place_cand = place_cand + place_neighbours_on_map(cnd, this_map)

                output.append(this_region)

    return output


def place_neighbours_all(this_point: Place,
                         ) -> List[Tuple[int, int]]:
    i = this_point.coordinates[0]
    j = this_point.coordinates[1]

    return [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1)
    ]


def place_neighbours_on_map(this_point: Place,
                            this_map: List[List[str]]
                            ) -> List[Place]:
    cand_coordinates = place_neighbours_all(this_point)

    return [Place(x, this_map[x[0]][x[1]]) for x in cand_coordinates if
            check_if_in_place(len(this_map[0]), len(this_map), x)]


def neighbours_in_same_line(all_perimeter_places: List[Place], this_point: Place) -> List[Place]:
    return [x for x in all_perimeter_places if
            x.coordinates in place_neighbours_all(this_point) and x.coordinates[0] ==
            this_point.coordinates[0]]


def neighbours_in_same_row(all_perimeter_places: List[Place], this_point: Place) -> List[Place]:
    return [x for x in all_perimeter_places if
            x.coordinates in place_neighbours_all(this_point) and x.coordinates[1] ==
            this_point.coordinates[1]]

