from dataclasses import dataclass, field

from day15.s2.domain.coordinates import Coordinates
from day15.s2.domain.world_object import WorldObject


@dataclass(frozen=True)
class Wall(WorldObject):
    current_coordinates: Coordinates
    obj_name: str = field(default="Wall", init=False)

    def __repr__(self):
        return f'Wall - P:{self.current_coordinates.short_repr}'

    def __str__(self):
        return '#'
