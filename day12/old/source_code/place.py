from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Place:
    coordinates: Tuple[int, int]
    plant_type: str

    # adjacent_places_coordinates: List[Tuple[int, int]]

    # adjacent_places: List['Place'] = field(default_factory=list)
    #
    # def add_adjacent_place(self, ad_place: 'Place') -> 'Place':
    #     new_adjacent_places = list(self.adjacent_places)
    #     return Place(
    #         self.id,
    #         self.pos1,
    #         self.pos2,
    #         self.height.__eq__(new_adjacent_places)
    #     )

    def __eq__(self, other):
        if not isinstance(other, Place):
            return NotImplemented
        return self.coordinates == other.coordinates

    def __hash__(self):
        return hash(self.coordinates)

    def __repr__(self):
        return f'Place({self.coordinates[0]}, {self.coordinates[1]}): {self.plant_type}'
