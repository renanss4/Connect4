from random import choice

class Player:
    def __init__(self, name, symbol, is_human=True):
        self.name = name
        self.symbol = symbol
        self.is_human = is_human

    def make_move(self, board):
        column = int(input(f"{self.name}, choose a column (1-{board.columns}): "))
        self.current_column = column-1
        board.drop_piece(column-1, self.symbol)

class CpuPlayer(Player):
    def __init__(self, symbol='O'):
        super().__init__('CPU', symbol, False)

    def get_priority_columns(self, board):
        priority_columns = []

        col = 0
        while col < len(board.grid[0]):
            if board.grid[0][col] == self.symbol:
                priority_columns.append(col)
            elif col + 1 < len(board.grid[0]) and board.grid[0][col + 1] == self.symbol:
                priority_columns.append(col + 1)

            col += 1

        # TODO: Add logic for additional conditions

        return priority_columns  # Adicione esta linha para retornar as colunas prioritárias


    def make_move(self, board):
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
