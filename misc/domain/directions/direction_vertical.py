from abc import ABC
from dataclasses import dataclass

from misc.domain.directions.direction import Direction


@dataclass(frozen=True)
class DirectionVertical(Direction, ABC):
    direction_name: str

    def __init__(self):
        pass

    def __post_init__(self):
        # Convert list to tuple to make it hashable
        object.__setattr__(self, 'direction_name', 'vertical')
