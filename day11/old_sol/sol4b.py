# import math
# from typing import List
#
#
# def read_file(file_name: str) -> list[str]:
#     text_table = []
#
#     with open(file_name, "r") as file:
#         for line in file:
#             line_v = line.rstrip()
#
#             text_table = text_table + line_v.split(' ')
#
#     return text_table
#
#
# MEMORY = {}
#
#
# def blink(stone, times) -> int:
#     if stone in MEMORY.keys():
#         return MEMORY[stone]
#     else:
#         these_stones = [stone]
#
#         for i in range(times):
#             new_these_stones = []
#             for stone in these_stones:
#                 one_or_two = get_stones_from_stone(stone)
#                 new_these_stones.append(one_or_two[0])
#                 if len(one_or_two) > 1:
#                     new_these_stones.append(one_or_two[1])
#
#             these_stones = new_these_stones
#
#         MEMORY[stone] = len(these_stones)
#         return len(these_stones)
#
#
# def get_stones_from_stone(stone) -> List[int]:
#     if stone == 0:  # Rule 1
#         return [1]
#     else:
#         lngth = int(math.log10(stone)) + 1
#         if lngth % 2 == 0:  # Rule 2
#             a = 10 ** (lngth // 2)
#             return [stone // a, stone % a]
#         else:
#             return [stone * 2024]
#
#
# # data = read_file('data/1/22.txt')
# data = read_file('../data/task1.txt')
# data = [int(a) for a in data]
#
# output = 0
# for stone in data:
#     output += blink(stone, 75)
#
# print(output)
