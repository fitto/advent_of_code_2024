from dataclasses import dataclass
from typing import Tuple, List, Optional, Set


@dataclass(frozen=True)
class Place:
    coordinates: Tuple[int, int]
    plant_type: str

    def __eq__(self, other):
        if not isinstance(other, Place):
            return NotImplemented
        return self.coordinates == other.coordinates

    def __hash__(self):
        return hash(self.coordinates)

    def __repr__(self):
        return f'Place({self.coordinates[0]}, {self.coordinates[1]}): {self.plant_type}'

    def is_adjacent_to(self, other_place: 'Place') -> Optional[str]:
        x1 = self.coordinates[0]
        y1 = self.coordinates[1]

        x2 = other_place.coordinates[0]
        y2 = other_place.coordinates[1]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dx == 1 and dy == 0:
            return "horizontal"
        elif dx == 0 and dy == 1:
            return "vertical"
        else:
            return None

    def create_wall(self, other_place: 'Place'):
        otp = self.is_adjacent_to(other_place)
        if otp is None:
            return None
        else:
            return Wall(otp, self, other_place)


@dataclass(frozen=True)
class WallLine:
    wall_line_type: str
    walls: Tuple['Wall', ...]  # Changed from list to tuple

    def __post_init__(self):
        # Convert list to tuple to make it hashable
        object.__setattr__(self, 'walls', tuple(self.walls))

    def __hash__(self):
        return hash((self.wall_line_type, self.walls))

    # @property
    # def extreme_points(self) -> List['Wall']:
    #     if len(self.walls) == 1:
    #         return self.walls
    #     else:
    #         if self.wall_line_type == 'vertical':

    def add_wall(self, that_wall: 'Wall') -> Optional['WallLine']:
        for w in self.walls:
            if w.is_in_wall_with(that_wall):
                new_walls = [x for x in self.walls]
                new_walls.append(that_wall)

                return WallLine(self.wall_line_type, tuple(new_walls))
        return None


@dataclass(frozen=True)
class Wall:
    wall_type: str
    first: Place
    second: Place

    def __post_init__(self):
        if self.wall_type == 'horizontal':
            if self.first.coordinates[0] > self.second.coordinates[0]:
                # Swap first and second if first x-coordinate is greater
                object.__setattr__(self, 'first', self.second)
                object.__setattr__(self, 'second', self.first)
        elif self.wall_type == 'vertical':
            if self.first.coordinates[1] > self.second.coordinates[1]:
                # Swap first and second if first y-coordinate is greater
                object.__setattr__(self, 'first', self.second)
                object.__setattr__(self, 'second', self.first)

    def is_in_wall_with(self, other_wall: 'Wall') -> bool:
        if self.first.is_adjacent_to(other_wall.first) and self.second.is_adjacent_to(
                other_wall.second) and self.wall_type == other_wall.wall_type:
            return True
        return False


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
                    if not check_if_in_place(len(this_place[0]), len(this_place), x):
                        sum_walls += 1
                    else:
                        if this_map[x[0]][x[1]] != self.plant_type:
                            sum_walls += 1

            return sum_walls

    def all_walls(self, this_map: List[List[str]]) -> Set['Wall'] | None:
        if self.area == 1 or self.area == 2:
            return None
        else:
            walls_around = set()
            for place in self.places:
                for x in place_neighbours_all(place):

                    if not check_if_in_place(len(this_map[0]), len(this_map), x):
                        new_pl = Place(x, 'xxxxx')
                    else:
                        new_pl = Place(x, this_map[x[0]][x[1]])

                    if new_pl.plant_type != place.plant_type:
                        wl = place.create_wall(new_pl)
                        if wl:
                            walls_around.add(wl)

            return walls_around

    def walls_no(self, this_map: List[List[str]]) -> int:
        if self.area == 1:
            return 4
        elif self.area == 2:
            return 4
        else:
            walls_around = self.all_walls(this_map)
            walls_around = sorted(walls_around,
                                  key=lambda wall: (wall.first.coordinates[0], wall.first.coordinates[1]))

            all_wall_lines = []

            while len(walls_around) > 0:
                this_wall = walls_around.pop()
                this_wall_line = WallLine(this_wall.wall_type, (this_wall,))

                cand = []
                if this_wall.wall_type == 'horizontal':
                    cand = [x for x in walls_around if x.wall_type == 'horizontal']

                if this_wall.wall_type == 'vertical':
                    cand = [x for x in walls_around if x.wall_type == 'vertical']

                added_sth = True
                while added_sth and len(cand) > 0:
                    added_sth = False
                    for this_cand in cand:
                        wall_line_add = this_wall_line.add_wall(this_cand)

                        if wall_line_add is not None:
                            this_wall_line = wall_line_add

                            cand.remove(this_cand)
                            walls_around.remove(this_cand)

                            added_sth = True
                            break

                all_wall_lines.append(this_wall_line)

            all_wall_lines = set([x for x in all_wall_lines])

            return len(all_wall_lines)

    def has_place(self, place: Place):
        return place in self.places


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
            check_if_in_place(len(this_place[0]), len(this_place), x)]


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


# this_place = read_file('data/2/25.txt')
this_place = read_file('data/task1.txt')
# print(this_place)

all_regions = find_regions(this_place)
# print(all_regions)
outpt = 0
for r in all_regions:
    # if r.plant_type == 'C':
    # print(r)
    # print(f'   walls_no {r.walls_no(this_place)}')
    # print(f'   area {r.area}')
    # print(f'   perimeter {r.perimeter(this_place)}')
    # outpt += r.area * r.perimeter(this_place)
    outpt += r.walls_no(this_place) * r.area
    # print(f'walls_no {r.walls_no(this_place) * r.perimeter(this_place)}')
print(outpt)
