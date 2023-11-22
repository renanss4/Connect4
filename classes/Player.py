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