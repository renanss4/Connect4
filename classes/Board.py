class Board:
    """
    Represents the game board.

    Attributes:
    - rows (int): The number of rows in the game board.
    - columns (int): The number of columns in the game board.
    - grid (list): A 2D list representing the current state of the game board.

    Methods:
    - __init__: Initializes a new Board instance.
    - print_board: Displays the current state of the game board in the terminal.
    - drop_piece: Drops a game piece into the specified column and updates the board.
    """

    def __init__(self, rows=6, columns=7):
        """
        Initializes a new Board instance.

        Parameters:
        - rows (int, optional): The number of rows in the game board (default is 6).
        - columns (int, optional): The number of columns in the game board (default is 7).
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]

    def print_board(self):
        """
        Displays the current state of the game board in the terminal.
        """
        for row in self.grid:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print()
            print('-' * (4 * self.columns + 1))

    def drop_piece(self, column, symbol):
        """
        Drops a game piece into the specified column and updates the board.

        Parameters:
        - column (int): The column in which the game piece should be dropped.
        - symbol (str): The symbol representing the player on the game board.

        Returns:
        - int: The row where the game piece was placed.
        """
        row = self.rows - 1
        while row >= 0:
            if self.grid[row][column] == ' ':
                self.grid[row][column] = symbol
                return row
            row -= 1
        return None
