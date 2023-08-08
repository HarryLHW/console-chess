from typing import Dict, Optional

from Piece import Color, Piece


class Empty(Piece):
    _instance: Optional['Empty'] = None
    unicodes = {Color.EMPTY_SQUARE: ' '}

    def __new__(cls) -> 'Empty':
        if cls._instance is None:
            cls._instance = super().__new__(Empty)
        return cls._instance

    def __init__(self) -> None:
        super().__init__(Color.EMPTY_SQUARE)
