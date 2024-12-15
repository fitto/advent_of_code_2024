from abc import ABC
from typing import Tuple

from day15.s2.domain.coordinates import Coordinates


# noinspection PyUnresolvedReferences
class WorldObject(ABC):
    def moved(self, move: Tuple) -> 'WorldObject':
        # from day15.s2.domain.nothing import Nothing
        from day15.s2.domain.robot import Robot

        if self.obj_name == 'Robot':
            return Robot(self.current_coordinates.shifted_coordinates(move[0], move[1]))
        if self.obj_name == 'BigBox':
            return self.moved_box(move)
        # if self.obj_name == 'Nothing':
        #     return Nothing(self.current_coordinates.shifted_coordinates(move[0], move[1]))
        else:
            print('WHOOP WIHOOP')

    @staticmethod
    def from_i_j(i: int, j: int, val: str):
        from day15.s2.domain.nothing import Nothing
        from day15.s2.domain.robot import Robot
        from day15.s2.domain.big_box import BigBox
        from day15.s2.domain.wall import Wall

        if val == '@':
            return Robot(Coordinates(i, j))
        if val == '#':
            return Wall(Coordinates(i, j))
        if val == '[':
            return BigBox(Coordinates(i, j), Coordinates(i, j + 1))
        if val == ']':
            return None
        else:
            return Nothing(Coordinates(i, j))
