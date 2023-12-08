import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Move Object to Mouse Click")

# Configurações do objeto
object_width = 50
object_height = 50
object_color = (255, 0, 0)  # Cor vermelha (R, G, B)
obj_surface = pygame.Surface((object_width, object_height))
obj_surface.fill(object_color)

# Posição inicial do objeto
x, y = screen_width // 2, screen_height // 2

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Define a posição do objeto para a posição do clique do mouse
            x, y = pygame.mouse.get_pos()

    # Limpa a tela
    screen.fill((255, 255, 255))

    # Desenha o objeto na janela
    screen.blit(obj_surface, (x - object_width // 2, y - object_height // 2))

    # Atualiza a exibição
    pygame.display.flip()

    # Controla a taxa de quadros por segundo (FPS)
    clock.tick(60)

# Finaliza o Pygame
pygame.quit()
sys.exit()
