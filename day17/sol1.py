# from typing import Dict, Set, List
#
# from day16.domain.coordinates import Coordinates
# from day16.domain.position import Position
#
#
# def find_key_points(file_name: str):
#     s = None
#     e = None
#     all_walls = set()
#
#     with open(file_name, 'r') as file:
#         i = 0
#         j = 0
#         for char in file.read():
#             if char == 'S':
#                 s = Coordinates(i, j)
#             if char == 'E':
#                 e = Coordinates(i, j)
#             if char == '#':
#                 all_walls.add(Coordinates(i, j))
#             # if char == '.':
#             #     all_allowed.add(Coordinates(i, j))
#
#             if char == '\n':
#                 i += 1
#                 j = 0
#             else:
#                 j += 1
#
#     return s, e, all_walls
#
#
# def find_all_paths(starting_pos: Position,
#                    all_walls_coordinates: Set[Coordinates],
#                    ) -> Dict[Position, Dict[Position, int]]:
#     output = {}
#     seen_positions = set()
#
#     positions_to_be_checked = [starting_pos]
#
#     while len(positions_to_be_checked) > 0:
#         this_position = positions_to_be_checked.pop()
#         if this_position not in seen_positions:
#             seen_positions.add(this_position)
#             next_postion_options = this_position.move_options_with_cost()
#
#             for k, v in next_postion_options.items():
#                 if k.coordinates not in all_walls_coordinates:
#                     cur = output.get(this_position, {})
#                     cur[k] = v
#
#                     output[this_position] = cur
#
#                     cur2 = output.get(k, {})
#                     cur2[this_position] = v
#
#                     output[k] = cur2
#
#                     positions_to_be_checked.append(k)
#
#     return output
#
#
# def dijkstra(graph: Dict[Position, Dict[Position, int]],
#              start: Position
#              ) -> tuple[dict[Position, float], Dict[Position, List[Position]]]:
#     distances = {node: float('inf') for node in graph.keys()}
#     distances[start] = 0
#
#     nodes_before_this = {node: [] for node in graph}
#
#     priority_queue = [(0, start)]
#
#     while priority_queue:
#         priority_queue.sort(key=lambda x: x[0])
#         current_distance, current_node = priority_queue.pop(0)
#
#         if current_distance > distances[current_node]:
#             continue
#
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 nodes_before_this[neighbor] = [current_node]
#                 priority_queue.append((distance, neighbor))
#             elif distance == distances[neighbor]:
#                 nodes_before_this[neighbor].append(current_node)
#
#     return distances, nodes_before_this
#
#
# COORD_MEM = set()
# def reconstruct_all_paths(before_dict: Dict[Position, List[Position]],
#                           start: Position,
#                           end: Position
#                           ) -> List[List[Position]]:
#     memory = {}
#     def backtrack(path):
#         to_be_checked = path[-1]
#         COORD_MEM.add(to_be_checked.coordinates)
#
#         if to_be_checked in memory.keys():
#             return memory[to_be_checked]
#
#         if to_be_checked == start:
#             all_paths.append(path[::-1])
#             return
#
#         for pred in before_dict[path[-1]]:
#             backtrack(path + [pred])
#
#         memory[to_be_checked] = all_paths
#
#     all_paths = []
#     backtrack([end])
#     return all_paths
#
#
# # start, end, all_walls_positions = find_key_points('data/22.txt')
# start, end, all_walls_positions = find_key_points('data/task1.txt')
# # print(f'start coord {start}')
# # print(f'end coord {end}')
#
# start_position = Position(start, '>')
# pths = find_all_paths(start_position, all_walls_positions)
#
# path_weigths, back_dict = dijkstra(pths, start_position)
#
# end_positions = [
#     Position(end, '>'),
#     Position(end, '<'),
#     Position(end, '^'),
#     Position(end, 'v')
# ]
#
# min_wigth = float('inf')
# for x in end_positions:
#     gt_o = path_weigths.get(x, -1)
#     print(f'{x.__repr__()}: {gt_o}')
#     if gt_o < min_wigth:
#         min_wigth = gt_o
#
# print(min_wigth)
#
# all_pos = set()
# for x in end_positions:
#     this_weigth = path_weigths.get(x, -1)
#     if this_weigth == min_wigth:
#         positions_list = reconstruct_all_paths(back_dict, start_position, x)
#
#         # for this_list in positions_list:
#         #     for pi in this_list:
#         #         all_pos.add(pi.coordinates)
#
#         # print(len(all_pos))
#
# # print(len(all_pos))
# print(len(COORD_MEM))
# # --546
