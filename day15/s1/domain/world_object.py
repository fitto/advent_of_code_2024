# from abc import ABC
# from typing import Tuple
#
# from day15.s1.domain.coordinates import Coordinates
#
#
# class WorldObject(ABC):
#     def moved(self, move: Tuple) -> 'WorldObject':
#         from day15.s1.domain.nothing import Nothing
#         from day15.s1.domain.robot import Robot
#         from day15.s1.domain.box import Box
#
#         if self.obj_name == 'Robot':
#             return Robot(self.current_coordinates.shifted_coordinates(move[0], move[1]))
#         if self.obj_name == 'Box':
#             return Box(self.current_coordinates.shifted_coordinates(move[0], move[1]))
#         if self.obj_name == 'Nothing':
#             return Nothing(self.current_coordinates.shifted_coordinates(move[0], move[1]))
#         else:
#             print('WHOOP WIHOOP')
#
#     @staticmethod
#     def from_i_j(i: int, j: int, val: str):
#         from day15.s1.domain.nothing import Nothing
#         from day15.s1.domain.robot import Robot
#         from day15.s1.domain.wall import Wall
#         from day15.s1.domain.box import Box
#
#         if val == '@':
#             return Robot(Coordinates(i, j))
#         if val == '#':
#             return Wall(Coordinates(i, j))
#         if val == 'O':
#             return Box(Coordinates(i, j))
#         else:
#             return Nothing(Coordinates(i, j))
