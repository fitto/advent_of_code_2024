import re
from dataclasses import dataclass

from day14.domain.velocity import Velocity

WORLD_WIDTH = 101
# //11

WORLD_HEIGHT = 103


# 7
# 103

@dataclass(frozen=True)
class Coordinates:
    first: int
    second: int

    def __repr__(self):
        return f'Coordinates {self.short_repr}'

    @property
    def short_repr(self):
        return f'({self.first}, {self.second})'

    def shifted_coordinates(self, first_m: int = 0, second_m: int = 0):
        new_f = self.first + first_m
        new_s = self.second + second_m

        if new_f < 0:
            new_f = WORLD_HEIGHT + new_f
        if new_f > WORLD_HEIGHT - 1:
            new_f = new_f - WORLD_HEIGHT

        if new_s < 0:
            new_s = WORLD_WIDTH + new_s
        if new_s > WORLD_WIDTH - 1:
            new_s = new_s - WORLD_WIDTH

        return Coordinates(new_f, new_s)

    def moved_by_velocity(self, velocity: Velocity):
        return self.shifted_coordinates(velocity.v1, velocity.v2)

    @staticmethod
    def from_str(text_line: str):
        numbers = re.findall(r'\d+', text_line)
        return Coordinates(int(numbers[1]), int(numbers[0]))

    def same_as(self, other_coordinates: 'Coordinates') -> bool:
        return self.first == other_coordinates.first and self.second == other_coordinates.second
