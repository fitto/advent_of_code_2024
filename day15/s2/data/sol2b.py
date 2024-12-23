# from typing import List
#
# from day15.s2.domain.world import World
#
#
# def read_file(file_name: str) -> List[List[str]]:
#     output = []
#
#     with open(file_name, 'r') as file:
#         for line in file:
#             line = line.rstrip()
#
#             this_line = []
#             for char in line:
#                 if char == '#':
#                     this_line.append('#')
#                     this_line.append('#')
#                 elif char == 'O':
#                     this_line.append('[')
#                     this_line.append(']')
#                 elif char == '.':
#                     this_line.append('.')
#                     this_line.append('.')
#                 elif char == '@':
#                     this_line.append('@')
#                     this_line.append('.')
#                 else:
#                     print('WHOOPS')
#
#             output.append(this_line)
#
#     output[0] = output[0][:len(output[1])]
#     output[len(output) - 1] = output[len(output) - 1][:len(output[1])]
#     return output
#
#
# # new_input = read_file('data/22map.txt')
# new_input = read_file('task1map.txt')
# this_world = World.from_list(new_input)
# initial_world = this_world
#
#
# this_world.visualize()
#
#
# def do_moves(file_name: str, initial_world: World) -> World:
#     wrld = initial_world
#
#     with open(file_name, 'r') as file:
#         # Read the file character by character
#         # i = 1
#         for char in file.read():
#             # Ignore newline characters
#             if char != '\n':
#                 wrld = wrld.execute_move(char)
#                 # if i % 100 == 0:
#                 # print('')
#                 # print('------------------')
#                 # print('')
#                 # print(f'MOVING: {char}')
#                 # wrld.visualize()
#                 # i += 1
#
#     return wrld
#
#
# # end_world = do_moves('data/22moves.txt', this_world)
# end_world = do_moves('task1moves.txt', this_world)
#
# end_world.visualize()
#
# print(end_world.all_coordinates_value)
#
# print(initial_world.walls_count)
# print(end_world.walls_count)
#
# print(initial_world.big_boxes_count)
# print(end_world.big_boxes_count)
#
# # 1536343
# # 1525312 bad for Nothing
