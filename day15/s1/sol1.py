# from day15.s1.domain.world import World
#
# # this_world = World.from_file('data/1/12/12map.txt')
# this_world = World.from_file('data/task1map.txt')
# # this_world.visualize()
#
#
# def do_moves(file_name: str, initial_world: World) -> World:
#     wrld = initial_world
#
#     with open(file_name, 'r') as file:
#         # Read the file character by character
#         for char in file.read():
#             # Ignore newline characters
#             if char != '\n':
#                 wrld = wrld.execute_move(char)
#                 # print('')
#                 # print('------------------')
#                 # print('')
#                 # print(f'MOVING: {char}')
#                 # wrld.visualize()
#
#     return wrld
#
#
# # end_world = do_moves('data/1/12/12moves.txt', this_world)
# end_world = do_moves('data/task1moves.txt', this_world)
# # end_world.visualize()
# print(end_world.all_coordinates_value)
