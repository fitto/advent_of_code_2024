from typing import Set

from day14.domain.coordinates import WORLD_WIDTH, WORLD_HEIGHT, Coordinates

# TREE_COORDINATES = []
#
# TREE_COORDINATES.append(Coordinates(0, WORLD_WIDTH // 2))
#
# c1 = WORLD_WIDTH // 2
# c2 = WORLD_WIDTH // 2
#
# for i in range(WORLD_HEIGHT // 2, WORLD_HEIGHT):
#     c1 -= 1
#     c2 += 1
#
#     TREE_COORDINATES.append(Coordinates(i, c1))
#     TREE_COORDINATES.append(Coordinates(i, c2))


TREE_COORDINATES = set()

p1 = Coordinates(WORLD_HEIGHT - 1, 0)
p2 = Coordinates(WORLD_HEIGHT - 1, WORLD_WIDTH - 1)

while not p1.same_as(p2):
    TREE_COORDINATES.add(p1)
    TREE_COORDINATES.add(p2)

    p1 = p1.shifted_coordinates(-1, 1)
    p2 = p2.shifted_coordinates(-1, -1)

TREE_COORDINATES.add(p1)

MIN_TREE_DEPTH = 5


def check_x_tree_shape(all_coordinates: Set[Coordinates]):
    for tree_top in all_coordinates:
        depth = 1
        pp1 = tree_top.shifted_coordinates(1, -1)
        pp2 = tree_top.shifted_coordinates(1, +1)

        while True:
            if pp1 in all_coordinates and pp2 in all_coordinates:
                depth += 1
            else:
                break

            if depth > MIN_TREE_DEPTH:
                print(f'-----------------------------')
                print(f'Tree Top = {tree_top}')
                print(f'Depth = {MIN_TREE_DEPTH}')
                print(f'-----------------------------')
                return True

            pp1 = pp1.shifted_coordinates(1, -1)
            pp2 = pp2.shifted_coordinates(1, +1)

    return False
