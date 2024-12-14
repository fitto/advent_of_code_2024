from dataclasses import dataclass

from day14.domain.coordinates import Coordinates


@dataclass(frozen=True)
class World:
    width: int
    heigth: int

    def has_coordinates(self, coordinates: Coordinates) -> bool:
        x1 = coordinates.first
        x2 = coordinates.second

        return -1 < x1 < self.heigth and -1 < x2 < self.width
