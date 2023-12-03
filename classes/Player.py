from random import choice

class Player:
    """
    Represents a player in the Connect Four game.

    Attributes:
    - name (str): The name of the player.
    - symbol (str): The symbol representing the player's pieces on the board.
    - is_human (bool): True if the player is human, False if it's a CPU player.

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
        self.name = name
        self.symbol = symbol
        self.is_human = is_human

    def make_move(self, board):
        """
        Allow the player to make a move on the board.

        Parameters:
        - board (Board): The game board.
        """
        valid_move = False
        while not valid_move:
            column = int(input(f'{self.name}, choose a column (1-{board.columns}): ')) - 1
            if 0 <= column < board.columns:
                if board.grid[0][column] == ' ':
                    board.drop_piece(column, self.symbol)
                    valid_move = True
                else:
                    print('Column is full. Please choose a different column.')
            else:
                print('Invalid move. Please choose a different column.')

class CpuPlayer(Player):
    """
    Represents a CPU player in the Connect Four game, inheriting from the Player class.

    Attributes:
    - symbol (str): The symbol representing the CPU player's pieces on the board.

    Methods:
    - __init__(self, symbol='O'): Initializes a CPU player with a specified symbol and human status set to False.
    - get_priority_columns(self, board): Gets columns with a priority for the CPU based on the current board state.
    - make_move(self, board): Makes a move for the CPU player, considering priority columns and available columns.
    """

    def __init__(self, symbol='O'):
        """
        Initialize a CPU player with a name 'CPU', a specified symbol, and human status set to False.

        Parameters:
        - symbol (str): The symbol representing the CPU player's pieces on the board.
        """
        super().__init__('CPU', symbol, False)

    def get_priority_columns(self, board):
        """
        Get columns with a priority for the CPU based on the current board state.

        Parameters:
        - board (Board): The game board.

        Returns:
        - list of int: Columns with priority for the CPU.
        """
        priority_columns = []

        col = 0
        while col < len(board.grid[0]):
            if board.grid[0][col] == self.symbol:
                priority_columns.append(col)

            col += 1

        return priority_columns # Doesn't works correctly

    def make_move(self, board):
        """
        Make a move for the CPU player, considering priority columns and available columns.

        Parameters:
        - board (Board): The game board.
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
            available_columns = [] # Maybe it would be good to review it in the future
            col = 0
            while col < len(board.grid[0]):
                if board.grid[0][col] == ' ':
                    available_columns.append(col)
                col += 1
            # It always gives [0, 1, 2, 3, 4, 5, 6]
            if available_columns:
                chosen_column = choice(available_columns)
                row = len(board.grid) - 1

                while row >= 0 and board.grid[row][chosen_column] != ' ':
                    row -= 1

                if row >= 0:
                    board.drop_piece(chosen_column, self.symbol)
        print()  # Add a newline for better readability
