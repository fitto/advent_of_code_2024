# from dataclasses import dataclass
# from typing import Tuple, List, Optional
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
#     def has_place(self, place: Place):
#         return place in self.places
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
# def place_neighbours(this_point: Place,
#                      this_map: List[List[str]]
#                      ) -> List[Place]:
#     i = this_point.coordinates[0]
#     j = this_point.coordinates[1]
#
#     cand_coordinates = [
#         (i - 1, j),
#         (i + 1, j),
#         (i, j - 1),
#         (i, j + 1)
#     ]
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
#                 place_cand = place_neighbours(initial_place, this_map)
#                 while len(place_cand) > 0:
#                     cnd = place_cand.pop()
#
#                     if this_region.plant_type == cnd.plant_type and cnd.coordinates not in saw_places and not this_region.has_place(
#                             cnd):
#                         this_region = this_region.add_place(cnd)
#                         saw_places.add(cnd.coordinates)
#                         place_cand = place_cand + place_neighbours(cnd, this_map)
#
#                 output.append(this_region)
#
#     return output
#
#
# # this_place = read_file('data/1/33.txt')
# this_place = read_file('data/task1.txt')
# # print(this_place)
#
# all_regions = find_regions(this_place)
# # print(all_regions)
# outpt = 0
# for r in all_regions:
#     # print(r)
#     # print(f'   area {r.area}')
#     # print(f'   perimeter {r.perimeter(this_place)}')
#     outpt += r.area * r.perimeter(this_place)
# print(outpt)
