from dataclasses import dataclass
from typing import Dict

from day16.domain.coordinates import Coordinates

COMANDS_WITH_COSTS = {
    "<":
        {
            "^": 1000,
            "v": 1000,
            "<": 1
        },
    "^":
        {
            ">": 1000,
            "<": 1000,
            "^": 1
        },
    ">":
        {
            "^": 1000,
            "v": 1000,
            ">": 1
        },
    "v":
        {
            ">": 1000,
            "<": 1000,
            "v": 1}
}

COMMAND_VECTOR = {
    "<": (0, -1),
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0)
}


@dataclass(frozen=True)
class Position:
    coordinates: Coordinates
    direction: str

    def __repr__(self):
        return f'P {self.coordinates.short_repr} {self.direction}'

    def move_options_with_cost(self) -> Dict['Position', int]:
        options = {}
        opts = COMANDS_WITH_COSTS[self.direction]

        for cmd_opt, cmd_cost in opts.items():
            if cmd_cost == 1000:
                options[Position(self.coordinates, cmd_opt)] = cmd_cost
            else:
                vector = COMMAND_VECTOR[cmd_opt]
                options[Position(self.coordinates.shifted_coordinates(vector[0], vector[1]), cmd_opt)] = cmd_cost

        return options
