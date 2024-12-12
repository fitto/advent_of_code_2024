from dataclasses import dataclass
from typing import List, Optional

from misc.domain.coordinates import Coordinates
from misc.domain.place import Place


@dataclass(frozen=True)
class World:
    places_as_table: List[List]

    def width(self, row: int = 0):
        return len(self.places_as_table[row])

    def height(self):
        return len(self.places_as_table)

    @property
    def all_places(self) -> List[Place]:
        output = []
        for i in range(self.height()):
            for j in range(self.width()):
                output.append(self.places_as_table[i][j])
        return output

    def has_place(self, place: Place) -> bool:
        return self.has_coordinates(place.coordinates)

    def has_coordinates(self, coordinates: Coordinates) -> bool:
        x1 = coordinates.first
        x2 = coordinates.second

        return -1 < x1 < self.height() and -1 < x2 < self.width()

    def row(self, i: int) -> List[Place]:
        output = []
        if -1 < i < self.height():
            output = self.places_as_table[i]
        return output

    def col(self, j: int) -> List[Place]:
        output = []
        if -1 < j < self.width():
            output = [x[j] for x in self.places_as_table]
        return output

    def place_from_coordinates(self, coordinates: Coordinates, also_outside=False) -> Optional[Place]:
        if not self.has_coordinates(coordinates):
            if also_outside:
                return Place(coordinates, 'OUTSIDE_PLACE')
            else:
                return None
        else:
            return self.places_as_table[coordinates.first][coordinates.second]

    def place_neighbours(self, place: Place, also_outside=False):
        output = []
        for ng in place.coordinates.neighbouring_coordinates:
            output.append(self.place_from_coordinates(ng, also_outside))
        return output

    @staticmethod
    def from_file(file_name: str):
        output = []

        with open(file_name, "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                for j in range(len(lines[i].rstrip())):
                    output.append(Place(Coordinates(i, j), lines[i][j]))

        return output
