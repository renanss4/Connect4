import pygame
import sys
from classes.Judge import Judge

# Inicializa a instância do Judge (Juiz)
judge = Judge()

# Configurações do jogo
judge.create_board()
square_size = 100
board_width = judge.board.columns * square_size
board_height = judge.board.rows * square_size

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

# Inicialização do Pygame
pygame.init()

# Configuração da tela
screen_width = board_width  # Largura da janela
screen_height = board_height  # Altura da janela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Connect Four")

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(judge.board.rows):
        for col in range(judge.board.columns):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size), 0) # desenha o tabuleiro todo azul no fundo
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 3)  # Adiciona borda ao retângulo
            pygame.draw.circle(screen, white, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 5) # Desenha os circulos

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha o tabuleiro
    screen.fill(white)
    draw_board()

    # Atualiza a tela
    pygame.display.flip()
