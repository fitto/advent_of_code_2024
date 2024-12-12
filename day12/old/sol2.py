# from dataclasses import dataclass
# from typing import Tuple, List, Optional, Set
#
#
# @dataclass(frozen=True)
# class Place:
#     coordinates: Tuple[int, int]
#     plant_type: str
#
#     # adjacent_places_coordinates: List[Tuple[int, int]]
#
#     # adjacent_places: List['Place'] = field(default_factory=list)
#     #
#     # def add_adjacent_place(self, ad_place: 'Place') -> 'Place':
#     #     new_adjacent_places = list(self.adjacent_places)
#     #     return Place(
#     #         self.id,
#     #         self.pos1,
#     #         self.pos2,
#     #         self.height.__eq__(new_adjacent_places)
#     #     )
#
#     def __eq__(self, other):
#         if not isinstance(other, Place):
#             return NotImplemented
#         return self.coordinates == other.coordinates
#
#     def __hash__(self):
#         return hash(self.coordinates)
#
#     def __repr__(self):
#         return f'Place({self.coordinates[0]}, {self.coordinates[1]}): {self.plant_type}'
#
#
# @dataclass(frozen=True)
# class Region:
#     id: int
#     places: List[Place]
#
#     def add_place(self, place: Place) -> 'Region':
#         new_places = [c for c in self.places]
#         new_places.append(place)
#         return Region(self.id, new_places)
#
#     def __repr__(self):
#         return f'Region({self.id}) {self.plant_type}: {len(self.places)}'
#
#     @property
#     def plant_type(self) -> Optional[str]:
#         return self.places[0].plant_type or None
#
#     @property
#     def area(self):
#         return len(self.places)
#
#     def perimeter(self, this_map: List[List[str]]):
#         if self.area == 1:
#             return 4
#         elif self.area == 2:
#             return 6
#         else:
#             sum_walls = 0
#             for place in self.places:
#                 i = place.coordinates[0]
#                 j = place.coordinates[1]
#
#                 cand_coordinates = [
#                     (i - 1, j),
#                     (i + 1, j),
#                     (i, j - 1),
#                     (i, j + 1)
#                 ]
#
#                 for x in cand_coordinates:
#                     if not check_if_in_place(len(this_place[0]), len(this_place), x):
#                         sum_walls += 1
#                     else:
#                         if this_map[x[0]][x[1]] != self.plant_type:
#                             sum_walls += 1
#
#             return sum_walls
#
#     def perimeter_places(self, this_map: List[List[str]]) -> Set[Place] | None:
#         if self.area == 1 or self.area == 2:
#             return None
#         else:
#             wall_places `= set()
#             for place in self.places:
#                 for x in place_neighbours_all(place):
#                     if not check_if_in_place(len(this_place[0]), len(this_place), x):
#                         wall_places.add(Place(x, 'xxxxx'))
#                     else:
#                         if this_map[x[0]][x[1]] != self.plant_type:
#                             wall_places.add(Place(x, this_map[x[0]][x[1]]))
#
#             return wall_places
#
#     def walls_no(self, this_map: List[List[str]]) -> int:
#         if self.area == 1:
#             return 4
#         elif self.area == 2:
#             return 4
#         else:
#             found_walls_no = 0
#             all_perimeter_places = self.perimeter_places(this_map)
#
#             while len(all_perimeter_places) > 0:
#                 max_0 = max([x.coordinates[0] for x in all_perimeter_places])
#                 max_1 = max([x.coordinates[1] for x in all_perimeter_places if x.coordinates[0] == max_0])
#
#                 this_point = \
#                     [x for x in all_perimeter_places if x.coordinates[0] == max_0 and x.coordinates[1] == max_1][0]
#                 # print(f'     traversed: {this_point}')
#                 all_perimeter_places.remove(this_point)
#
#                 has_horizontal = False
#                 while True:
#                     nbr_in_same_line = neighbours_in_same_line(all_perimeter_places, this_point)
#                     # nbr_in_same_line = [x for x in nbr_in_same_line if x in all_perimeter_places]
#
#                     if len(nbr_in_same_line) > 0:
#                         has_horizontal = True
#
#                         nbr_in_same_line = sorted(nbr_in_same_line, key=lambda place: place.coordinates[1])
#                         this_neighbour = nbr_in_same_line.pop()
#
#                         if abs(this_neighbour.coordinates[1] - this_point.coordinates[
#                             1]) == 1 and this_neighbour in all_perimeter_places:
#                             # traversed_points.append(this_neighbour)
#                             all_perimeter_places.remove(this_neighbour)
#                             this_point = this_neighbour
#
#                             # print(f'     traversed: {this_point}')
#
#                     else:
#                         # found_walls_no += 1
#                         # print('   end of wall')
#                         break
#
#                 has_vertical = False
#                 while True:
#                     nbr_in_same_column = neighbours_in_same_row(all_perimeter_places, this_point)
#                     nbr_in_same_column = [x for x in nbr_in_same_column if x in all_perimeter_places]
#
#                     if len(nbr_in_same_column) > 0:
#                         has_vertical = True
#
#                         nbr_in_same_column = sorted(nbr_in_same_column, key=lambda place: place.coordinates[0])
#                         this_neighbour = nbr_in_same_column.pop()
#
#                         if abs(this_neighbour.coordinates[0] - this_point.coordinates[0]) == 1:
#                             all_perimeter_places.remove(this_neighbour)
#                             # traversed_points.append(this_neighbour)
#                             this_point = this_neighbour
#                             # print(f'     traversed: {this_point}')
#
#                     else:
#                         # if this_point in saw_places and has_vertical:
#                         #     # print(f'SAW: {this_point}')
#                         #     found_walls_no += 1
#                         break
#
#                 if has_horizontal or has_vertical:
#                     found_walls_no += 1
#                 if has_horizontal and has_vertical:
#                     found_walls_no += 1
#                 if not has_horizontal and not has_vertical:
#                     found_walls_no += 1
#
#         return found_walls_no
#
#     def has_place(self, place: Place):
#         return place in self.places
#
#
# def neighbours_in_same_line(all_perimeter_places: set[Place], this_point: Place) -> List[Place]:
#     return [x for x in all_perimeter_places if
#             x.coordinates in place_neighbours_all(this_point) and x.coordinates[0] ==
#             this_point.coordinates[0]]
#
#
# def neighbours_in_same_row(all_perimeter_places: set[Place], this_point: Place) -> List[Place]:
#     return [x for x in all_perimeter_places if
#             x.coordinates in place_neighbours_all(this_point) and x.coordinates[1] ==
#             this_point.coordinates[1]]
#
#
# def check_if_in_place(width: int,
#                       height: int,
#                       this_point_coord: Tuple[int, int]
#                       ):
#     return -1 < this_point_coord[0] < height and -1 < this_point_coord[1] < width
#
#
# def read_file(file_name: str) -> List[List[str]]:
#     output = []
#
#     with open(file_name, "r") as file:
#         for line in file:
#             row = line.rstrip()
#             this_row = []
#             for r in row:
#                 this_row.append(r)
#
#             output.append(this_row)
#
#     return output
#
#
# def place_neighbours_all(this_point: Place,
#                          ) -> List[Tuple[int, int]]:
#     i = this_point.coordinates[0]
#     j = this_point.coordinates[1]
#
#     return [
#         (i - 1, j),
#         (i + 1, j),
#         (i, j - 1),
#         (i, j + 1)
#     ]
#
#
# def place_neighbours_on_map(this_point: Place,
#                             this_map: List[List[str]]
#                             ) -> List[Place]:
#     cand_coordinates = place_neighbours_all(this_point)
#
#     return [Place(x, this_map[x[0]][x[1]]) for x in cand_coordinates if
#             check_if_in_place(len(this_place[0]), len(this_place), x)]
#
#
# def find_regions(this_map: List[List[str]]) -> List[Region]:
#     output = []
#
#     saw_places = set()
#
#     width = len(this_map[0])
#     heigth = len(this_map)
#
#     rid = 1
#
#     for i in range(width):
#         for j in range(heigth):
#             if (i, j) not in saw_places:
#                 initial_place = Place((i, j), this_map[i][j])
#                 this_region = Region(rid, [initial_place])
#                 rid += 1
#
#                 place_cand = place_neighbours_on_map(initial_place, this_map)
#                 while len(place_cand) > 0:
#                     cnd = place_cand.pop()
#
#                     if this_region.plant_type == cnd.plant_type and cnd.coordinates not in saw_places and not this_region.has_place(
#                             cnd):
#                         this_region = this_region.add_place(cnd)
#                         saw_places.add(cnd.coordinates)
#                         place_cand = place_cand + place_neighbours_on_map(cnd, this_map)
#
#                 output.append(this_region)
#
#     return output
#
#
# this_place = read_file('../data/1/11.txt')
# # this_place = read_file('data/task1.txt')
# # print(this_place)
#
# all_regions = find_regions(this_place)
# # print(all_regions)
# outpt = 0
# for r in all_regions:
#     if r.plant_type == 'C':
#         print(r)
#         print(f'   walls_no {r.walls_no(this_place)}')
#         print(f'   area {r.area}')
#         # print(f'   perimeter {r.perimeter(this_place)}')
#         # outpt += r.area * r.perimeter(this_place)
#         outpt += r.walls_no(this_place) * r.area
#         # print(f'walls_no {r.walls_no(this_place) * r.perimeter(this_place)}')
# print(outpt)
