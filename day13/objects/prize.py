import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Prize:
    x_val: int
    y_val: int

    @staticmethod
    def from_str(text_line: str):
        numbers = re.findall(r'\d+', text_line)
        return Prize(int(numbers[0]), int(numbers[1]))
