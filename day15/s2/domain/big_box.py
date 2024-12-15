from dataclasses import dataclass, field
from typing import Tuple

from day15.s2.domain.coordinates import Coordinates
from day15.s2.domain.world_object import WorldObject


@dataclass(frozen=True)
class BigBox(WorldObject):
    current_coordinates_1: Coordinates
    current_coordinates_2: Coordinates
    obj_name: str = field(default="BigBox", init=False)

    def __repr__(self):
        return f'{self.obj_name} - P:{self.current_coordinates_1.short_repr}/{self.current_coordinates_2.short_repr} '

    def __str__(self):
        return '[]'

    def moved(self, move: Tuple) -> 'BigBox':
        return BigBox(
            self.current_coordinates_1.shifted_coordinates(move[0], move[1]),
            self.current_coordinates_2.shifted_coordinates(move[0], move[1])
        )
