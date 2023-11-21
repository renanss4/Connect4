import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello, Pygame!")

# Cor de fundo da janela
background_color = (255, 255, 255)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche o fundo com a cor definida
    screen.fill(background_color)

    # Desenha o texto "Hello, World!" no centro da janela
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, World!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização (FPS)
    pygame.time.Clock().tick(60)
