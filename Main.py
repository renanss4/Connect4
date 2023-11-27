from classes.Board import Board
from classes.Player import CpuPlayer, Player
from classes.Judge import Judge

class Main:
    """
    Represents the main game manager.

    Attributes:
    - board (Board): The game board.
    - players (list): A list containing instances of players participating in the game.
    - current_player_index (int): Index of the current player in the players list.

    Methods:
    - __init__: Initializes a new Main instance.
    - switch_player: Switches the turn to the next player.
    - run: Controls the main game loop.
    """

    def __init__(self):
        """
        Initializes a new Main instance.
        Creates instances of players, the judge, and the board based on user input.
        """
        self.board = Board()
        self.judge = Judge()
        num_players = int(input("Enter the number of players (1 or 2): "))
        if num_players == 1:
            self.players = [Player('Player 1', "X"), CpuPlayer()]
        elif num_players == 2:
            self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        else:
            print('ERROR')

    def switch_player(self):
        """
        Switches the turn to the next player.
        """
        self.current_player_index = 1 - self.current_player_index

    def run(self):
        """
        Controls the main game loop.
        Displays the game board, allows each player to make a move in turn, and switches players.
        """
        self.current_player_index = 0

        running = True

        while running:
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            current_player.make_move(self.board)

            self.switch_player()

if __name__ == "__main__":
    game = Main()
    game.run()
