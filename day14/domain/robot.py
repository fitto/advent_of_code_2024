from dataclasses import dataclass

from day14.domain.coordinates import Coordinates
from day14.domain.velocity import Velocity


@dataclass(frozen=True)
class Robot:
    r_id: int
    current_coordinates: Coordinates
    velocity: Velocity

    @staticmethod
    def from_str(rid: int, text_line: str):
        c, v = text_line.split(' ')
        return Robot(rid, Coordinates.from_str(c), Velocity.from_str(v))

    def __repr__(self):
        return f'R{self.r_id} P:{self.current_coordinates.short_repr}, V:{self.velocity.short_repr}'

    def moved(self):
        return Robot(self.r_id, self.current_coordinates.moved_by_velocity(self.velocity), self.velocity)
