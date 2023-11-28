class Judge:
    # quais os atributos e parametros?
    # checar no diagrama corretamente
    # será que os parametros não são as jogadas dos jogadores e o tabuleiro?
    def __init__(self):
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_winner(self, board, symbol):
        # Verificar horizontal
        row = 0
        while row < board.rows:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row][col + 1] == symbol and board.grid[row][col + 2] == symbol and board.grid[row][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Verificar vertical
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns:
                if board.grid[row][col] == symbol and board.grid[row + 1][col] == symbol and board.grid[row + 2][col] == symbol and board.grid[row + 3][col] == symbol:
                    return True
                col += 1
            row += 1

        # Verificar diagonal principal
        row = 0
        while row < board.rows - 3:
            col = 0
            while col < board.columns - 3:
                if board.grid[row][col] == symbol and board.grid[row + 1][col + 1] == symbol and board.grid[row + 2][col + 2] == symbol and board.grid[row + 3][col + 3] == symbol:
                    return True
                col += 1
            row += 1

        # Verificar diagonal secundária
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
        col = 0
        while col < board.columns:
            if board.grid[0][col] == ' ':
                return False
            col += 1
        return True

    def check_incorrect_move(self, board, column):
        if column < 0 or column >= board.columns:
            return True  # Movimento fora dos limites

        if board.grid[0][column] != ' ':
            return True  # Coluna cheia

        return False


