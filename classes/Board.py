class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]

    def print_board(self):
        for row in self.grid:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print()
            print('-' * (4 * self.columns + 1))

    def drop_piece(self, column, symbol):
        row = self.rows - 1
        while row >= 0:
            if self.grid[row][column] == ' ':
                self.grid[row][column] = symbol
                return row
            row -= 1
        return None
