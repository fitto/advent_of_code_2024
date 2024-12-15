# from dataclasses import dataclass
# from typing import List, Tuple
#
# from day15.s1.domain.box import Box
# from day15.s1.domain.coordinates import Coordinates
# from day15.s1.domain.nothing import Nothing
# from day15.s1.domain.robot import Robot
# from day15.s1.domain.wall import Wall
# from day15.s1.domain.world_object import WorldObject
#
#
# @dataclass(frozen=True)
# class World:
#     robot_position: Coordinates
#     places_as_table: List[List[WorldObject]]
#
#     def width(self, row: int = 0):
#         return len(self.places_as_table[row])
#
#     def height(self):
#         return len(self.places_as_table)
#
#     def has_coordinates(self, coordinates: Coordinates) -> bool:
#         x1 = coordinates.first
#         x2 = coordinates.second
#
#         return -1 < x1 < self.height() and -1 < x2 < self.width()
#
#     def object_at(self, coordinates: Coordinates):
#         return self.places_as_table[coordinates.first][coordinates.second]
#
#     def move_objects(self, objects_list: List[WorldObject], direction: Tuple) -> 'World':
#         new_places_as_table_copy = self.places_as_table.copy()
#
#         moving_object = objects_list.pop(-1)
#         if not isinstance(moving_object, Nothing):
#             print('ALARMO !!!!!!!!!!!')
#         last_obj = moving_object
#
#         while len(objects_list) > 1:
#             moving_object = objects_list.pop(-1)
#             new_obj = moving_object.moved(direction)
#
#             if last_obj.current_coordinates.first != new_obj.current_coordinates.first or last_obj.current_coordinates.second != new_obj.current_coordinates.second:
#                 print('A L A R M O')
#             new_places_as_table_copy[last_obj.current_coordinates.first][last_obj.current_coordinates.second] = new_obj
#             last_obj = moving_object
#
#         moving_object = objects_list.pop(-1)
#         if not isinstance(moving_object, Robot):
#             print('ALARMO !!!!!! !!!!!! !!!!!')
#         new_robot = moving_object.moved(direction)
#         new_places_as_table_copy[new_robot.current_coordinates.first][new_robot.current_coordinates.second] = new_robot
#         new_places_as_table_copy[moving_object.current_coordinates.first][
#             moving_object.current_coordinates.second] = Nothing(
#             moving_object.current_coordinates)
#
#         return World(new_robot.current_coordinates, new_places_as_table_copy)
#
#     def robot_move(self, move: str) -> 'World':
#         command_switch = {
#             "<": (0, -1),
#             "^": (-1, 0),
#             ">": (0, 1),
#             "v": (1, 0)
#         }
#         tpl = command_switch[move]
#
#         moving_objects = [self.object_at(self.robot_position)]
#         if not isinstance(moving_objects[-1], Robot):
#             print('ALARMO')
#
#         while True:
#             new_coord = moving_objects[-1].current_coordinates.shifted_coordinates(tpl[0], tpl[1])
#             found_object = self.object_at(new_coord)
#             # print(f'    {found_object}')
#
#             if isinstance(found_object, Nothing):
#                 moving_objects.append(found_object)
#                 return self.move_objects(moving_objects, tpl)
#             if isinstance(found_object, Wall):
#                 return self
#             else:
#                 moving_objects.append(found_object)
#
#     @staticmethod
#     def from_file(file_name: str):
#         output = []
#
#         with open(file_name, "r") as file:
#             lines = file.readlines()
#
#             for i in range(len(lines)):
#                 line = []
#                 for j in range(len(lines[i].rstrip())):
#                     obj = WorldObject.from_i_j(i, j, lines[i][j])
#                     if isinstance(obj, Robot):
#                         robots_position = obj.current_coordinates
#                     line.append(obj)
#                 output.append(line)
#
#         return World(robots_position, output)
#
#     # def visualize(self):
#     #     for ii in range(self.height()):
#     #         this_line = ''
#     #         for jj in range(self.width()):
#     #             this_line += self.places_as_table[ii][jj].__str__()
#     #
#     #         print(this_line)
#
#     @property
#     def all_coordinates_value(self) -> int:
#         output = 0
#         for ii in range(self.width()):
#             for jj in range(self.height()):
#                 found_object = self.places_as_table[ii][jj]
#                 if isinstance(found_object, Box):
#                     output += found_object.current_coordinates.coord_value
#
#         return output
