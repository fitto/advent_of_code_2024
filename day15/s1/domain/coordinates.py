# from dataclasses import dataclass
# from typing import Optional
#
# from misc.domain.directions.direction import Direction
# from misc.domain.directions.direction_horizontal import DirectionHorizontal
# from misc.domain.directions.direction_vertical import DirectionVertical
#
#
# @dataclass(frozen=True)
# class Coordinates:
#     first: int
#     second: int
#
#     def __repr__(self):
#         return f'Coordinates {self.short_repr}'
#
#     @property
#     def short_repr(self):
#         return f'({self.first}, {self.second})'
#
#     def adjacent_to(self, other_coordinates: 'Coordinates') -> Optional[Direction]:
#         dx = abs(other_coordinates.first - self.first)
#         dy = abs(other_coordinates.second - self.second)
#
#         if dx == 1 and dy == 0:
#             return DirectionHorizontal()
#         elif dx == 0 and dy == 1:
#             return DirectionVertical()
#         else:
#             return None
#
#     def same_as(self, other_coordinates: 'Coordinates') -> bool:
#         return self.first == other_coordinates.first and self.second == other_coordinates.second
#
#     def shifted_coordinates(self, first_m: int = 0, second_m: int = 0):
#         return Coordinates(self.first + first_m, self.second + second_m)
#
#     @property
#     def neighbouring_coordinates(self):
#         i = self.first
#         j = self.second
#         return [
#             (i - 1, j),
#             (i + 1, j),
#             (i, j - 1),
#             (i, j + 1)
#         ]
#
#     @property
#     def coord_value(self):
#         return 100 * self.first + self.second
