import pygame

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Brush
brush_size = 10
brush_color = BLACK

# Drawing tools
drawing = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                brush_color = RED
            elif event.key == pygame.K_g:
                brush_color = GREEN
            elif event.key == pygame.K_b:
                brush_color = BLUE
            elif event.key == pygame.K_w:
                brush_color = WHITE
            elif event.key == pygame.K_e:
                brush_color = BLACK

    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, pos, brush_size)

    pygame.display.flip()

pygame.quit()
