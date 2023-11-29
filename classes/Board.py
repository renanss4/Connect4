class Board:
    def __init__(self, rows=6, columns=7):
        """
        Initialize the game board.

        Args:
        - rows (int): The number of rows on the board.
        - columns (int): The number of columns on the board.
        """
        # Initialize the board with the specified number of rows and columns
        self.rows = rows
        self.columns = columns
        self.grid = []

        # Populate the grid with empty spaces
        for i in range(rows):
            row = [' '] * columns
            self.grid.append(row)

    def print_board(self):
        """
        Print the current state of the board to the console.
        """
        # Print the current state of the board to the console
        for row in self.grid:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print()
            print('-' * (4 * self.columns + 1))

    def drop_piece(self, column, symbol):
        """
        Drop a game piece into the specified column.

        Args:
        - column (int): The column where the piece should be placed.
        - symbol (str): The symbol representing the player (e.g., 'X' or 'O').

        Returns:
        - int or None: The row where the piece was placed, or None if the column is full.
        """
        # Drop a game piece into the specified column
        row = self.rows - 1
        while row >= 0:
            if self.grid[row][column] == ' ':
                self.grid[row][column] = symbol
                return row  # Return the row where the piece was placed
            row -= 1
        return None  # Return None if the column is full
