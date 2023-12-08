from classes.Judge import Judge

def run():
    """
    Run the Connect Four game.

    Executes the main game loop, allowing players to take turns until there is a winner or draw.
    Prints the current state of the board after each turn.
    """
    judge = Judge()
    judge.create_players()

    running = True

    while running:
        # Print the current state of the board
        judge.create_board()

        # Get the current player and make their move
        current_player = judge.get_current_player()

        if current_player.is_human:
            judge.validate_move(current_player)  # Validate the move using Judge
        else:
            # CPU player makes a move
            current_player.make_move(judge.board)

        # Check for a winner or draw
        if judge.check_winner(current_player.symbol):
            judge.create_board()
            print(f'{current_player.name} wins! Congratulations!')
            running = False
        elif judge.check_draw():
            judge.create_board()
            print("It's a Draw!")
            running = False

        # Switch to the next player for the next turn
        judge.switch_player()

if __name__ == '__main__':
    run()
