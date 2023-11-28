from classes.Board import Board
from classes.Player import CpuPlayer, Player
from classes.Judge import Judge

class Main:
    def __init__(self):
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
        self.current_player_index = 1 - self.current_player_index

    def run(self):
        self.current_player_index = 0
        running = True

        while running:
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            current_player.make_move(self.board)
            if self.judge.check_winner(self.board, current_player.symbol):
                # self.board.print_board()
                print(f' wins')
                running = False
            elif self.judge.check_draw(self.board):
                print(f'draw')
                running = False
            
            self.switch_player()


if __name__ == "__main__":
    game = Main()
    game.run()
