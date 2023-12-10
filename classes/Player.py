class Player:
    """
    Represents a player in the Connect Four game.

    Attributes:
    - _name (str): The name of the player.
    - _symbol (str): The symbol representing the player's pieces on the board.
    - _is_human (bool): True if the player is human, False if it's a CPU player.

    Methods:
    - __init__(self, name, symbol, is_human=True): Initializes a player with a name, symbol, and human status.
    - make_move(self, board): Allows the player to make a move on the board.
    """

    def __init__(self, name, symbol, is_human=True):
        """
        Initialize a player with a name, symbol, and human status.

        Parameters:
        - name (str): The name of the player.
        - symbol (str): The symbol representing the player's pieces on the board.
        - is_human (bool): True if the player is human, False if it's a CPU player.
        """
        self._name = name
        self._symbol = symbol
        self._is_human = is_human

    def make_move(self, board):
        """
        Allows the player to make a move on the board.

        Parameters:
        - board (Board): The game board.

        Returns:
        - int: The column where the player wants to make the move.
        """
        column = int(input(f'{self._name}, choose a column (1-7): ')) - 1
        return column
