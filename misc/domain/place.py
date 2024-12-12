from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

from misc.domain.coordinates import Coordinates
from misc.domain.directions.direction import Direction

ValueType = TypeVar('ValueType')


@dataclass(frozen=True)
class Place(Generic[ValueType]):
    coordinates: 'Coordinates'  # Replace with the actual type of Coordinates
    value: Optional[ValueType]

    def adjacent_to(self, other_place: 'Place') -> Optional[Direction]:
        return self.coordinates.adjacent_to(other_place.coordinates)

    def same_coordinates(self, other_place: 'Place') -> bool:
        return self.coordinates.same_as(other_place.coordinates)

    def same_value(self, other_place: 'Place') -> bool:
        return self.value == other_place.value

    def has_value(self, other_value: ValueType) -> bool:
        return self.value == other_value

    def shifted_coordinates(self, first_m: int = 0, second_m: int = 0, new_value: Optional[ValueType] = None):
        new_coordinates = self.coordinates.shifted_coordinates(first_m, second_m)
        new_val = new_value if new_value else self.value
        return Place(new_coordinates, new_val)

    def __repr__(self):
        return f'{self.coordinates.short_repr} {self.value}'
