from classes.Board import Board
from classes.Player import CpuPlayer, Player
from classes.Judge import Judge

class Main:
    """
    The main class for running the Connect Four game.

    Attributes:
    - board (Board): The game board.
    - judge (Judge): The judge responsible for determining the game's outcome.
    - players (list): A list containing Player objects representing the players.
    - current_player_index (int): The index of the current player in the players list.
    """

    def __init__(self):
        """
        Initialize the Connect Four game.

        Prompts the user for the number of players and creates the necessary components.
        """
        self.board = Board()
        self.judge = Judge()

        # Create players based on the user input
        valid_players = False
        while not valid_players:
            # Get the number of players from user input
            num_players = int(input("Enter the number of players (1 or 2): "))
            if num_players == 1:
                self.players = [Player('Player 1', "X"), CpuPlayer()]
                valid_players = True
            elif num_players == 2:
                self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
                valid_players = True
            else:
                print('Only one or two players can play.')

    def switch_player(self):
        """
        Switch the current player index for alternating turns.
        """
        self.current_player_index = 1 - self.current_player_index

    def run(self):
        """
        Run the Connect Four game.

        Executes the main game loop, allowing players to take turns until there is a winner or draw.
        Prints the current state of the board after each turn.
        """
        self.current_player_index = 0
        running = True

        while running:
            # Print the current state of the board
            self.board.print_board()

            # Get the current player and make their move
            current_player = self.players[self.current_player_index]
            current_player.make_move(self.board)

            # Check for a winner or draw
            if self.judge.check_winner(self.board, current_player.symbol):
                self.board.print_board()
                print(f'{current_player.name} wins! Congratulations!')
                running = False
            elif self.judge.check_draw(self.board):
                self.board.print_board()
                print(f"It's a Draw!")
                running = False
            
            # Switch to the next player for the next turn
            self.switch_player()

# Run the game if the script is executed directly
if __name__ == "__main__":
    game = Main()
    game.run()
