import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Button:
    x_move: int
    y_move: int

    @staticmethod
    def from_str(text_line: str):
        numbers = re.findall(r'\d+', text_line)
        return Button(int(numbers[0]), int(numbers[1]))
