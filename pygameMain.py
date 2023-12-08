import pygame
import sys
from classes.Judge import Judge

# Inicializa a instância do Judge (Juiz)
judge = Judge()

# Configurações do jogo
judge.create_board()
square_size = 100
width = judge.board.columns * square_size
height = judge.board.rows * square_size

# Cores
white = (255, 255, 255)
blue = (0, 0, 255)

# Inicialização do Pygame
pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect Four")

# Função para desenhar o tabuleiro
def draw_board():
    for row in range(judge.board.rows):
        for col in range(judge.board.columns):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size), 0)
            pygame.draw.circle(screen, white, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 5)

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
