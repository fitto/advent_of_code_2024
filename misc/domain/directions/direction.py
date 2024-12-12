from abc import ABC


class Direction(ABC):
    direction_name: str

    def __repr__(self):
        return self.direction_name
