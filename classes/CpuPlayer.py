from classes.Player import Player
from random import choice

class CpuPlayer(Player):
    """
    Represents a CPU player in the Connect Four game, inheriting from the Player class.

    Attributes:
    - _symbol (str): The symbol representing the CPU player's pieces on the board.

    Methods:
    - __init__(self, symbol='O'): Initializes a CPU player with a specified symbol and human status set to False.
    - make_move(self, board): Makes a move for the CPU player, considering available columns.

    Parameters:
    - board (Board): The game board.
    
    Returns:
    - int or None: The row where the piece was placed, or None if no valid move is possible.
    """

    def __init__(self, symbol='O'):
        """
        Initialize a CPU player with a name 'CPU', a specified symbol, and human status set to False.

        Parameters:
        - symbol (str): The symbol representing the CPU player's pieces on the board.
        """
        super().__init__('CPU', symbol, False)

    def make_move(self, board):
        """
        Makes a move for the CPU player, considering available columns.

        Parameters:
        - board (Board): The game board.
        
        Returns:
        - int or None: The row where the piece was placed, or None if no valid move is possible.
        """
        available_columns = []
        col = 0
        while col < len(board._grid[0]):
            if board._grid[0][col] == ' ':
                available_columns.append(col)
            col += 1

        if available_columns:
            chosen_column = choice(available_columns)
            row = len(board._grid) - 1

            while row >= 0 and board._grid[row][chosen_column] != ' ':
                row -= 1

            if row >= 0:
                return board.drop_piece(chosen_column, self._symbol)
        else:
            return None
