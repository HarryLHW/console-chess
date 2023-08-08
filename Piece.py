from enum import Enum
from typing import Dict


class Color(Enum):
    WHITE = 'white'
    BLACK = 'black'
    EMPTY_SQUARE = 'empty_square'


class Piece:
    unicodes: Dict[Color, str]

    def __init__(self, color: Color) -> None:
        self.color = color
        self.icon = self.unicodes[color]

    def __str__(self) -> str:
        return self.icon
