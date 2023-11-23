import random

'''
Description:
- Defines a class to represent players, storing player details,
    and providing methods for players within in game.
'''

# class Player():
class Player:
    def __init__(self, name, symbol, is_human=True):
        self.name = name
        self.symbol = symbol
        self.is_human = is_human

    def make_move(self, board):
        column = int(input(f"{self.name}, choose a column (0-{board.columns - 1}): "))
        row = board.drop_piece(column, self.symbol)
        if row is not None:
            return
        
class CpuPlayer(Player):
    def __init__(self, symbol='O'):
        super().__init__('CPU', symbol, False)

    def make_move(self, board):
        available_columns = []
        for col in board.grid[0]:
            if col == ' ':
                available_columns.append(col)

        if available_columns:
            column = random.choice(available_columns)
            board.drop_piece(column, self.symbol)
