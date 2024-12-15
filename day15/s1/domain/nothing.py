from dataclasses import dataclass, field

from day15.s1.domain.coordinates import Coordinates
from day15.s1.domain.world_object import WorldObject


@dataclass(frozen=True)
class Nothing(WorldObject):
    current_coordinates: Coordinates
    obj_name: str = field(default="Nothing", init=False)

    def __repr__(self):
        return f'Nothing - P:{self.current_coordinates.short_repr}'

    def __str__(self):
        return '.'
