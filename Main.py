from classes.Board import Board
from classes.Player import CpuPlayer, Player

"""
Description:
- Manages the overall program flow by creating instances of players,
    the judge, and the board, and controlling the main game loop.
"""

class Main:
    def __init__(self):
        self.board = Board()
        num_players = int(input("Enter the number of players (1 or 2): "))
        if num_players == 1:
            # name_player = input("Enter the your name: ")
            self.players = [Player('Player 1', "X"), CpuPlayer()]
        elif num_players == 2:
            self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        else:
            print('ERROOR')

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def run(self):

        self.current_player_index = 0

        runnng = True

        while runnng:
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            current_player.make_move(self.board)


            self.switch_player()


if __name__ == "__main__":
    game = Main()
    game.run()

