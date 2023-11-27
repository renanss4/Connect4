class Judge:
    # quais os atributos e parametros?
    # checar no diagrama corretamente
    # será que os parametros não são as jogadas dos jogadores e o tabuleiro?
    def __init__(self):
        pass

    def check_winner(self):
        # verificar diagonal, vertical e horizontal
        # se ter uma sequencia de simbolo igual vence
        # se nãoo, troca o joogador
        pass

    def check_draw(self):
        # se todas as coolunas estão cheias defiine empate e finaliza o jogo
        pass

    def check_incorrect_move(self, board, column):
        # se jogar em um tamanho maior que 7 ou menor que 1
        # se coluna está cheia
        # pede para o jogador repetir jogada
        pass

