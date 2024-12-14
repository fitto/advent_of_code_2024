from dataclasses import dataclass


@dataclass(frozen=True)
class Velocity:
    v1: int
    v2: int

    @staticmethod
    def from_str(text_line: str):
        numbers = text_line.split(',')
        return Velocity(int(numbers[1]), int(numbers[0][2:]))

    @property
    def short_repr(self):
        return f'({self.v1}, {self.v2})'
