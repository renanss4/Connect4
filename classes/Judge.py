class Judge:
    """
    The Judge class represents the game judge responsible for determining the winner
    or a draw in a game played on a specified game board.

    Attributes:
    - name (str): The name of the game judge.

    Methods:
    - __init__(self, name=None): Initializes the game judge.
    - check_winner(self, board, symbol): Checks if the specified symbol has won the game.
    - check_draw(self, board): Checks if the game is a draw.
    """

    def __init__(self, name=None):
        """
        Initialize the game judge.

        Args:
        - name (str): The name of the game judge.
        """
        self.name = name

    def check_winner(self, board, symbol):
        """
        Check if the specified symbol has won the game.

        Args:
        - board (Board): The game board.
        - symbol (str): The symbol representing the player (e.g., 'X' or 'O').

        Returns:
        - bool: True if the player with the given symbol has won, False otherwise.
        """
        # Check for a horizontal win
        row = 0
        while row < board.rows:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row][col + 1] == symbol and board.grid[row][col + 2] == symbol and board.grid[row][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a vertical win
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns:
                if board.grid[row][col] == symbol and board.grid[row + 1][col] == symbol and board.grid[row + 2][col] == symbol and board.grid[row + 3][col] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from top-left to bottom-right)
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row + 1][col + 1] == symbol and board.grid[row + 2][col + 2] == symbol and board.grid[row + 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from bottom-left to top-right)
        row = 3
        while row < board.rows:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row - 1][col + 1] == symbol and board.grid[row - 2][col + 2] == symbol and board.grid[row - 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        return False

    def check_draw(self, board):
        """
        Check if the game is a draw.

        Args:
        - board (Board): The game board.

        Returns:
        - bool: True if the game is a draw, False otherwise.
        """
        # Check for a draw by examining the top row of the board
        col = 0
        while col < board.columns:
            if board.grid[0][col] == ' ':
                return False
            col += 1
        return True
