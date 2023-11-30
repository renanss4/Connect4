import pytest
from ..classes.Board import Board

def test_board_initialization():
    # Testa se o tabuleiro é inicializado corretamente
    board = Board.Board()
    assert board.rows == 6
    assert board.columns == 7
    assert len(board.grid) == 6
