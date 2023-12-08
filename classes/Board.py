class Board:
    """
    The Board class represents the game board on which players make their moves.

    Attributes:
    - _rows (int): The number of rows on the board.
    - _columns (int): The number of columns on the board.
    - _grid (list): A 2D list representing the current state of the board.

    Methods:
    - __init__(self, rows=6, columns=7): Initializes the game board.
    - print_board(self): Prints the current state of the board to the console.
    - drop_piece(self, column, symbol): Drops a game piece into the specified column.
    """

    def __init__(self, rows=6, columns=7):
        """
        Initialize the game board.

        Args:
        - rows (int): The number of rows on the board.
        - columns (int): The number of columns on the board.
        """
        # Initialize the board with the specified number of rows and columns
        self._rows = rows
        self._columns = columns
        self._grid = []

        # Populate the grid with empty spaces
        i = 0
        while i < rows:
            row = [' '] * columns
            self._grid.append(row)
            i += 1

    def print_board(self):
        """
        Print the current state of the board to the console.
        """
        for row in self._grid:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print()
            print('-' * (4 * self._columns + 1))

    def drop_piece(self, column, symbol):
        """
        Drop a game piece into the specified column.

        Args:
        - column (int): The column where the piece should be placed.
        - symbol (str): The symbol representing the player (e.g., 'X' or 'O').

        Returns:
        - int or None: The row where the piece was placed, or None if the column is full.
        """
        row = self._rows - 1
        while row >= 0:
            if self._grid[row][column] == ' ':
                self._grid[row][column] = symbol
                print()  # Add a newline for better readability
                return row  # Return the row where the piece was placed
            row -= 1
        print()  # Add a newline for better readability
        return None  # Return None if the column is full
