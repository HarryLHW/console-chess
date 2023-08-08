from typing import List

from Piece import Color, Piece
from Pieces.Bishop import Bishop
from Pieces.Empty import Empty
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class Board:
    setup = [
        [Rook(Color.BLACK), Knight(Color.BLACK), Bishop(Color.BLACK), Queen(Color.BLACK), King(Color.BLACK),
         Bishop(Color.BLACK), Knight(Color.BLACK), Rook(Color.BLACK)],
        [Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK),
         Pawn(Color.BLACK), Pawn(Color.BLACK), Pawn(Color.BLACK)],
        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
        [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
        [Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE),
         Pawn(Color.WHITE), Pawn(Color.WHITE), Pawn(Color.WHITE)],
        [Rook(Color.WHITE), Knight(Color.WHITE), Bishop(Color.WHITE), Queen(Color.WHITE), King(Color.WHITE),
         Bishop(Color.WHITE), Knight(Color.WHITE), Rook(Color.WHITE)]
    ]

    def __init__(self, initial_board: List[List[Piece]] | None = None) -> None:
        self.board = self.setup if initial_board is None else initial_board

    def __str__(self) -> str:
        board_string = '\n'.join(''.join(map(str, row)) for row in self.board)
        return f'\n{board_string}\n'
