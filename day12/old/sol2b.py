# from typing import List
#
# from day12.old.source_code.region import find_regions
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
# this_place = read_file('../data/1/33.txt')
# # this_place = read_file('data/task1.txt')
# # print(this_place)
#
# all_regions = find_regions(this_place)
# # print(all_regions)
# outpt = 0
# for r in all_regions:
#     # if r.plant_type == 'C':
#     # print(r)
#     # print(f'   walls_no {r.walls_no(this_place)}')
#     # print(f'   area {r.area}')
#     # print(f'   perimeter {r.perimeter(this_place)}')
#     # outpt += r.area * r.perimeter(this_place)
#     outpt += r.walls_no(this_place) * r.area
#     # print(f'walls_no {r.walls_no(this_place) * r.perimeter(this_place)}')
# print(outpt)
#
# # --879146
