from classes.Player import Player, CpuPlayer

class Judge:
    """
    The Judge class represents the game judge responsible for determining the winner
    or a draw in a Connect Four game played on a specified game board.

    Attributes:
    - name (str): The name of the game judge.

    Methods:
    - create_players(): Creates a list of players based on user input.
    - check_winner(board, symbol): Checks if the specified symbol has won the game.
    - check_draw(board): Checks if the game is a draw.
    - switch_player(current_player_index): Switches the current player index for alternating turns.
    - validate_move(current_player, board): Validates the current player's move and updates the game board.
    """

    def __init__(self, name=None):
        """
        Initialize the game judge.

        Args:
        - name (str): The name of the game judge.
        """
        self.name = name # I don't use this
    
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
                players = [Player('Player 1', 'X'), CpuPlayer()]
                valid_players = True
            elif num_players == 2:
                players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
                valid_players = True
            else:
                print('Only one or two players can play.')
        return players

    def check_winner(self, board, symbol):
        """
        Check if the specified symbol has won the Connect Four game.

        Args:
        - board (Board): The game board.
        - symbol (str): The symbol representing the player (e.g., 'X' or 'O').

        Returns:
        - bool: True if the player with the given symbol has won, False otherwise.
        """
        # Check for a horizontal win
        row = 0
        while row < board.rows:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row][col + 1] == symbol and board.grid[row][col + 2] == symbol and board.grid[row][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a vertical win
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns:
                if board.grid[row][col] == symbol and board.grid[row + 1][col] == symbol and board.grid[row + 2][col] == symbol and board.grid[row + 3][col] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from top-left to bottom-right)
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row + 1][col + 1] == symbol and board.grid[row + 2][col + 2] == symbol and board.grid[row + 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Check for a diagonal win (from bottom-left to top-right)
        row = 3
        while row < board.rows:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row - 1][col + 1] == symbol and board.grid[row - 2][col + 2] == symbol and board.grid[row - 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        return False

    def check_draw(self, board):
        """
        Check if the Connect Four game is a draw.

        Args:
        - board (Board): The game board.

        Returns:
        - bool: True if the game is a draw, False otherwise.
        """
        # Check for a draw by examining the top row of the board
        col = 0
        while col < board.columns:
            if board.grid[0][col] == ' ':
                return False
            col += 1
        return True

    def switch_player(self, current_player_index):
        """
        Switch the current player index for alternating turns.

        Args:
        - current_player_index (int): The current index of the player in the players list.

        Returns:
        - int: The index of the switched player.
        """
        return 1 - current_player_index

    def validate_move(self, current_player, board):
        """
        Validate the current player's move and update the game board.

        Args:
        - current_player (Player): The player making the move.
        - board (Board): The game board.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        valid_move = False
        while not valid_move:
            column = current_player.make_move()  # Use make_move from current player
            if 0 <= column < board.columns:
                if board.grid[0][column] == ' ':
                    board.drop_piece(column, current_player.symbol)
                    valid_move = True
                else:
                    print('Column is full. Please choose a different column.')
            else:
                print('Invalid move. Please choose a different column.')
        print()  # Add a newline for better readability
