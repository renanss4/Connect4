from classes.Board import Board
from classes.Player import CpuPlayer, Player
from classes.Judge import Judge

def run():
    """
    Run the Connect Four game.

    Executes the main game loop, allowing players to take turns until there is a winner or draw.
    Prints the current state of the board after each turn.
    """
    board = Board()
    judge = Judge()

    # Create players based on user input
    valid_players = False
    while not valid_players:
        # Get the number of players from user input
        num_players = int(input('Enter the number of players (1 or 2): '))
        if num_players == 1:
            players = [Player('Player 1', 'X'), CpuPlayer()]
            valid_players = True
        elif num_players == 2:
            players = [Player('Player 1', 'X'), Player('Player 2', 'O')]
            valid_players = True
        else:
            print('Only one or two players can play.')

    current_player_index = 0
    running = True

    while running:
        # Print the current state of the board
        board.print_board()

        # Get the current player and make their move
        current_player = players[current_player_index]
        
        if current_player.is_human:
            current_player.make_move(board)
        else:
            current_player.make_move(board)  # Assume the CPU player makes a move instantly

        # Check for a winner or draw
        if judge.check_winner(board, current_player.symbol):
            board.print_board()
            print(f'{current_player.name} wins! Congratulations!')
            running = False
        elif judge.check_draw(board):
            board.print_board()
            print(f"It's a Draw!")
            running = False

        # Switch to the next player for the next turn
        current_player_index = judge.switch_player(current_player_index)

# Run the game if the script is executed directly
if __name__ == '__main__':
    run()
