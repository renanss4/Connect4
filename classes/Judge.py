from classes.Board import Board
from classes.Player import Player, CpuPlayer

class Judge:
    """
    The Judge class represents the game judge responsible for determining the winner
    or a draw in a Connect Four game played on a specified game board.

    Attributes:
    - board (Board): The game board.
    - current_player_index (int): The index of the current player.
    - players (list): List containing the created players.
    """
    def __init__(self):
        """
        Initialize the Judge instance.

        Attributes:
        - board (Board): The game board.
        - current_player_index (int): The index of the current player.
        - players (list): List containing the created players.
        """
        self.board = Board()
        self.current_player_index = 0
        self.players = []

    def create_board(self):
        """
        Creates a new game board and prints its initial state.
        """
        self.board.print_board()

    def create_players(self):
        """
        Create players based on user input.

        Returns:
        - list: A list containing the created players.
        """
        valid_players = False
        while not valid_players:
            num_players = int(input('Enter the number of players (1 or 2): '))
            if num_players == 1:
                self.players = [Player('Player 1', 'X'), CpuPlayer()]
                valid_players = True
            elif num_players == 2:
                self.players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
                valid_players = True
            else:
                print('Only one or two players can play.')
        return self.players

    def check_winner(self, symbol):
        """
        Check if the specified symbol has won the Connect Four game.

        Args:
        - symbol (str): The symbol representing the player (e.g., 'X' or 'O').

        Returns:
        - bool: True if the player with the given symbol has won, False otherwise.
        """
        # Check for a horizontal win
        row = 0
        while row < self.board.rows:
            col = 0
            while col < self.board.columns - 3:
                if self.board.grid[row][col] == symbol and self.board.grid[row][col + 1] == symbol and self.board.grid[row][col + 2] == symbol and self.board.grid[row][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a vertical win
        row = 0
        while row < self.board.rows - 3:
            col = 0
            while col < self.board.columns:
                if self.board.grid[row][col] == symbol and self.board.grid[row + 1][col] == symbol and self.board.grid[row + 2][col] == symbol and self.board.grid[row + 3][col] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from top-left to bottom-right)
        row = 0
        while row < self.board.rows - 3:
            col = 0
            while col < self.board.columns - 3:
                if self.board.grid[row][col] == symbol and self.board.grid[row + 1][col + 1] == symbol and self.board.grid[row + 2][col + 2] == symbol and self.board.grid[row + 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from bottom-left to top-right)
        row = 3
        while row < self.board.rows:
            col = 0
            while col < self.board.columns - 3:
                if self.board.grid[row][col] == symbol and self.board.grid[row - 1][col + 1] == symbol and self.board.grid[row - 2][col + 2] == symbol and self.board.grid[row - 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        return False

    def check_draw(self):
        """
        Check if the Connect Four game is a draw.

        Returns:
        - bool: True if the game is a draw, False otherwise.
        """
        # Check for a draw by examining the top row of the board
        col = 0
        while col < self.board.columns:
            if self.board.grid[0][col] == ' ':
                return False
            col += 1
        return True

    def switch_player(self):
        """
        Switch the current player index for alternating turns.
        """
        self.current_player_index = 1 - self.current_player_index

    def validate_move(self, current_player):
        """
        Validate the current player's move and update the game board.

        Args:
        - current_player (Player): The player making the move.

        Returns:
        - None
        """
        valid_move = False
        while not valid_move:
            column = current_player.make_move()  # Use make_move from the current player
            if 0 <= column < self.board.columns:
                if self.board.grid[0][column] == ' ':
                    self.board.drop_piece(column, current_player.symbol)
                    valid_move = True
                else:
                    print('Column is full. Please choose a different column.')
            else:
                print('Invalid move. Please choose a different column.')
        print()  # Add a newline for better readability

    def get_current_player(self):
        """
        Gets the current player based on the current player index.

        Returns:
        - Player: The current player object.
        """
        return self.players[self.current_player_index]
