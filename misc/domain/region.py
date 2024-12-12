from dataclasses import dataclass
from typing import List

from misc.domain.place import Place


@dataclass(frozen=True)
class Region:
    id: int
    places: List[Place]

    def add_place(self, place: Place) -> 'Region':
        new_places = [c for c in self.places]
        new_places.append(place)
        return Region(self.id, new_places)

    def __repr__(self):
        return f'Region({self.id}) {self.area}'

    @property
    def area(self):
        return len(self.places)

    def has_place(self, place: Place) -> bool:
        return place in self.places
