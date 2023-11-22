"""
Description:
- Defines a class responsible for updating the game board
    after moves and displaying the current state in the terminal.
"""

class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = []
        row = 0
        while row < rows:
            new_row = []
            col = 0
            while col < columns:
                new_row.append(' ')
                col += 1
            self.grid.append(new_row)
            row += 1

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
                return row  # Retorna a linha onde a peça foi colocada
            row -= 1
        return None
# testing
# connect4_board = Board()
# connect4_board.print_board()
