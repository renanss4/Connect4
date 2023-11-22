from classes.Board import Board
from classes.Player import Player

"""
Description:
- Manages the overall program flow by creating instances of players,
    the judge, and the board, and controlling the main game loop.
"""

class Main:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0

    def switch_player(self):
        # self.current_player_index = 1
        self.current_player_index = 1 - self.current_player_index

    def run(self):
        runnng = True

        while runnng:
            self.board.print_board()
            current_player = self.players[self.current_player_index] # 0
            current_player.make_move(self.board)


            self.switch_player()


if __name__ == "__main__":
    game = Main()
    game.run()

