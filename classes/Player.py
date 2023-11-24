from random import choice

class Player:
    """
    Represents a player in the game.

    Attributes:
    - name (str): The name of the player.
    - symbol (str): The symbol representing the player on the game board.
    - is_human (bool): Indicates whether the player is a human player (default is True).

    Methods:
    - __init__: Initializes a new Player instance.
    - make_move: Takes user input to make a move on the game board.
    """

    def __init__(self, name, symbol, is_human=True):
        """
        Initializes a new Player instance.

        Parameters:
        - name (str): The name of the player.
        - symbol (str): The symbol representing the player on the game board.
        - is_human (bool, optional): Indicates whether the player is a human player (default is True).
        """
        self.name = name
        self.symbol = symbol
        self.is_human = is_human

    def make_move(self, board):
        """
        Takes user input to make a move on the game board.

        Parameters:
        - board: The game board on which the move is to be made.
        """
        column = int(input(f"{self.name}, choose a column (1-{board.columns}): "))
        board.drop_piece(column-1, self.symbol)

class CpuPlayer(Player):
    """
    Represents a CPU player in the game, inheriting from the Player class.

    Attributes:
    - symbol (str): The symbol representing the CPU player on the game board.

    Methods:
    - __init__: Initializes a new CpuPlayer instance.
    - get_priority_columns: Retrieves priority columns for the CPU player.
    - make_move: Makes a move for the CPU player on the game board.
    """

    def __init__(self, symbol='O'):
        """
        Initializes a new CpuPlayer instance.

        Parameters:
        - symbol (str, optional): The symbol representing the CPU player on the game board (default is 'O').
        """
        super().__init__('CPU', symbol, False)

    def get_priority_columns(self, board):
        """
        Retrieves priority columns for the CPU player.

        Parameters:
        - board: The game board for which priority columns are to be determined.
        """
        priority_columns = []

        col = 0
        while col < len(board.grid[0]):
            if board.grid[0][col] == self.symbol:
                priority_columns.append(col)
            elif col + 1 < len(board.grid[0]) and board.grid[0][col + 1] == self.symbol:
                priority_columns.append(col + 1)

            col += 1

        # TODO: Add logic for additional conditions

    def make_move(self, board):
        """
        Makes a move for the CPU player on the game board.

        Parameters:
        - board: The game board on which the move is to be made.
        """
        priority_columns = self.get_priority_columns(board)

        if priority_columns:
            chosen_column = choice(priority_columns)
            row = len(board.grid) - 1

            while row >= 0 and board.grid[row][chosen_column] != ' ':
                row -= 1

            if row >= 0:
                board.drop_piece(chosen_column, self.symbol)
        else:
            available_columns = []
            col = 0
            while col < len(board.grid[0]):
                if board.grid[0][col] == ' ':
                    available_columns.append(col)
                col += 1

            if available_columns:
                chosen_column = choice(available_columns)
                row = len(board.grid) - 1

                while row >= 0 and board.grid[row][chosen_column] != ' ':
                    row -= 1

                if row >= 0:
                    board.drop_piece(chosen_column, self.symbol)
